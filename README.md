# solargraph-utils.py

[solargraph-utils](https://github.com/castwide/solargraph-utils) for python

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
