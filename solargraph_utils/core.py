# -*- coding: utf-8 -*-
import os
import re
import json
import subprocess
import signal
from urllib.error import HTTPError

from . import helpers
from .helpers import *

class Server:
    def __init__(self, command='solargraph', args=['--port', '0']):
        # --port=0 Use free port
        self.command = command
        self.args = args
        self.proc = None
        self.port = None
        self.start()
        signal.signal(signal.SIGTERM, lambda num, stack : self.stop())
        signal.signal(signal.SIGHUP, lambda num, stack : self.stop())
        signal.signal(signal.SIGINT, lambda num, stack : self.stop())
        self.host = 'localhost'
        self.url = 'http://{}:{}/'.format(self.host, self.port)

    def start(self):
        env = os.environ.copy()
        self.proc = subprocess.Popen(
            [self.command, 'server', *self.args],
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        # until to get port number
        output = ''
        while True:
            line = self.proc.stdout.readline().decode('utf-8')

            if not line:
                raise ServerError('Failed to start server' + (output and ':\n' + output))

            match = re.search(r'port=(\d+)', line)
            if match:
                self.port = int(match.group(1))
                break

            output += line

    def stop(self):
        if self.proc is None:
            return

        self.proc.stdout.close()
        self.proc.kill()
        self.proc = None
        self.port = None

    def is_started(self):
        return self.proc is not None and self.port is not None


class Client:
    def __init__(self, url):
        self.url = url

    def request(self, path, params):
        try:
            result = post_request(self.url, path, params)
            return json.loads(result.decode('utf8'))
        except HTTPError as error:
            raise ClientError(str(error)) from error

    def prepare(workspace):
        return self.request('prepare', {'workspace': workspace})

    def update(filename, workspace=None):
        return self.request('update', {'filename': filename, 'workspace': workspace})

    def suggest(self, text, line, column, filename=None, workspace=None, with_snippets=None, with_all=None):
        params = {
            'text': text,
            'line': line,
            'column': column,
            'filename': filename,
            'workspace': workspace,
            'with_snippets': with_snippets,
            'all': with_all,
        }
        return self.request('suggest', params)

    def define(self, text, line, column, filename=None, workspace=None):
        params = {
            'text': text,
            'line': line,
            'column': column,
            'filename': filename,
            'workspace': workspace,
        }
        return self.request('define', params)

    def resolve(self, path, filename, workspace):
        params = {
            'path': path,
            'filename': filename,
            'workspace': workspace,
        }
        return self.request('resolve', params)

    def signify(self, text, line, column, filename=None, workspace=None):
        params = {
            'text': text,
            'line': line,
            'column': column,
            'filename': filename,
            'workspace': workspace,
        }
        return self.request('signify', params)
