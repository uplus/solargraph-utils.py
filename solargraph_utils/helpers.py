# -*- coding: utf-8 -*-
import platform
import urllib.request
import urllib.parse

is_windows = platform.system() == 'Windows'
is_darwin = platform.system() == 'Darwin'
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

class ServerError(Exception):
    pass


class ClientError(Exception):
    pass


def post_request(url, path, params):
    url = urllib.parse.urljoin(url, path)
    params = collect_not_none(params)
    data = urllib.parse.urlencode(params).encode('ascii')

    req = opener.open(url, data)
    return req.read()


def collect_not_none(d):
    return {key: d[key] for key in d if d[key] is not None}
