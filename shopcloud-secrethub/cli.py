import configparser
import getpass
import os
import requests
from typing import List


class ConfigFile:
    def __init__(self, path):
        self.path = path
        self.config = None
        self._load()

    def _load(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read(self.path)
            self.config['default']
        except Exception as e:
            print("can not load token. init with auth command")

    @property
    def token(self):
        return self.config['default']['token']

    @staticmethod
    def generate(path: str, token: str):
        config = configparser.ConfigParser()
        config.add_section('default')
        config['default']['token'] = token

        with open(path, 'w') as configfile:
            config.write(configfile)


class App:
    def __init__(self, path, **kwargs):
        self.config = ConfigFile(path)
        self.endpoint = kwargs.get('endpoint', 'shopcloud-secrethub.ey.r.appspot.com')
    
    def read(self, secretname) -> List:
        response = requests.get(
            f'https://{self.endpoint}/hub/api/secrets',
            headers={
                'Authorization': self.config.token,
                'User-Agent': 'secrethub-cli',
            },
            params={
                'q': secretname,
            }
        )

        if not (200 <= response.status_code <= 299):
            raise Exception('API wrong answer')

        return response.json().get('results', [])

    def write(self, secretname, value):
        response = requests.post(
            f'https://{self.endpoint}/hub/api/secrets/write/',
            headers={
                'Authorization': self.config.token,
                'User-Agent': 'secrethub-cli',
            },
            json={
                'name': secretname,
                'value': value
            }
        )
        return response.json()
        


def main(args):
    path = os.path.expanduser('~/.secrethub')
    command = args.which

    if command == 'auth':
        token = getpass.getpass('Token:')
        ConfigFile.generate(path, token)
    elif command == 'read':
        app = App(path)
        secrets = app.read(args.name)
        if args.output is None:
            for secret in secrets:
                value = secret.get('value').encode('unicode_escape').decode('utf-8')
                print(f"{secret.get('name')}={value}")
        elif args.output == 'json':
            for secret in secrets:
                print(secret)
    elif command == 'write':
        app = App(path)
        app.write(args.name, args.value)
    elif command == 'inject':
        print('not implemented yet')
