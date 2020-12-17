# Shopcloud SecretHub CLI

SecretHub CLI Tool for the Secrethub Service

## install

```
$ pip install shopcloud-secrethub
```

### usage

```
$ python3 -m shopcloud-secrethub auth
$ python3 -m shopcloud-secrethub read <secret-name>
$ python3 -m shopcloud-secrethub write <secret-name> <value>
```

### Deploy to PyPi

```
$ pip3 install wheel twine
$ python3 setup.py sdist bdist_wheel
$ twine upload dist/* 
```