import argparse
from . import cli

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='SecretHub',
        prog='shopcloud-secrethub'
    )

    subparsers = parser.add_subparsers(help='authentication', title='auth')
    parser_a = subparsers.add_parser('auth', help='generate auth file')
    parser_a.set_defaults(which='auth')

    parser_b = subparsers.add_parser('read', help='read a secret')
    parser_b.add_argument('name', type=str, help='secret name')
    parser_b.add_argument('--output', help='Output Format', choices=['text', 'json'])
    parser_b.set_defaults(which='read')

    args = parser.parse_args()
    cli.main(args)
