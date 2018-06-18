![Coverage Status](https://coveralls.io/repos/github/bcb/jsonrpcclient/badge.svg?branch=master)
![PyPI](https://img.shields.io/pypi/v/jsonrpcclient.svg)

# jsonrpcclient

Send [JSON-RPC](http://www.jsonrpc.org/) requests in Python.

```sh
pip install "jsonrpcclient[requests]"
```

```python
import jsonrpcclient
jsonrpcclient.request('http://cats.com', 'speak')
```

Full documentation is at [jsonrpcclient.readthedocs.io](https://jsonrpcclient.readthedocs.io/).

See also: [jsonrpcserver](https://github.com/bcb/jsonrpcserver)

## Testing

```sh
pip install "jsonrpcclient[unittest]"
python -m unittest discover
```
