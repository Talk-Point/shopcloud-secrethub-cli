# Shopcloud SecretHub CLI

The SecretHub CLI provides the command-line interface to interact with the SecretHub API.

## install

```
$ pip install shopcloud-secrethub
```

### Usage


__Reading and writing secrets:__  

```
$ python3 -m shopcloud-secrethub auth
$ python3 -m shopcloud-secrethub read <secret-name>
$ python3 -m shopcloud-secrethub write <secret-name> <value>
```


__Provisioning your applications with secrets:__  

Provision a template file

```
$ python3 -m shopcloud-secrethub inject -i app.temp.yaml -o app.yaml

# app.temp.yaml
env_variables:
  ENV: {{ talk-point/test-repo/env }}
  SECRET_KEY: {{ talk-point/test-repo/secret_key }}

```

### Deploy to PyPi

```
$ pip3 install wheel twine
$ python3 setup.py sdist bdist_wheel
$ twine upload dist/* 
```