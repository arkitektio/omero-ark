# omero-ark

[![codecov](https://codecov.io/gh/arkitektio/omero-ark/branch/master/graph/badge.svg?token=UGXEA2THBV)](https://codecov.io/gh/arkitektio/arkitektio)
[![PyPI version](https://badge.fury.io/py/rekuest.svg)](https://pypi.org/project/rekuest/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://pypi.org/project/rekuest/)
![Maintainer](https://img.shields.io/badge/maintainer-jhnnsrs-blue)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/rekuest.svg)](https://pypi.python.org/pypi/rekuest/)
[![PyPI status](https://img.shields.io/pypi/status/rekuest.svg)](https://pypi.python.org/pypi/rekuest/)

self-documenting asynchronous scalable RPC based on provisionable untrusted actors

## Idea

rekuest is the python client for the rekuest server, it provides a simple interface both register and provide nodes (functionality)
and call other nodes in async and synchronous manner. Contrary to most RPC services, Rekuest is focussed on providing functionaly on the Client, and is especially tailored for secnarious where apps can be developed to perform tasks on users behalves, therefore requiring fine grained access control.

## Prerequesits

Currently rekuest is only compatible within the context of the arkitekt platform, as it relies on "lok" for the authentication and authorization of users and applications. This is however a temporary limitation and will be removed in the future. You should then be able to use rekuest with any authentication and authorization service.


## Install

```python
pip install arkitekt[rekuest]
```

rekuest is relying heavily on asyncio patters and therefore only supports python 3.7 and above. Its api provides sync and async
interfaces through koil.

> If you are working in image analysis checkout the arkitekt platform that also provides data structures for image analysis (composed in the arkitekt platform)

## Get started