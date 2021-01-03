import os

def test_read():
    from shopcloud_secrethub import SecretHub
    hub = SecretHub(user_app="test-script", api_token=os.environ.get('AUTH_TOKEN'))
    secret = hub.read('talk-point/test-repo/secret_key')
    assert secret is not None
