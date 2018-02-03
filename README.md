# solargraph-utils.py

A utilities of [solargraph](https://github.com/castwide/solargraph) for python inspired by [solargraph-utils](https://github.com/castwide/solargraph-utils).  

## Current supported APIs

* `/prepare`
* `/update`
* `/suggest`
* `/define`
* `/resolve`
* `/signify`

[solargraph API docs](https://github.com/castwide/solargraph/blob/master/SERVER.md).  

## Example

```python
import solargraph_utils

text = "String."
line = 0
column = 7

server = solargraph_utils.Server(command='solargraph')
client = solargraph_utils.Client(server.url)

result = client.suggest(text=text, line=line, column=column)
print(result)

server.stop()
```
