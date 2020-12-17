import json, os
from .app import App, ConfigFile
        


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
                print(json.dumps(secret))
    elif command == 'write':
        app = App(path)
        app.write(args.name, args.value)
    elif command == 'inject':
        print('not implemented yet')
