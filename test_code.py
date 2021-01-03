import os

def test_read():
    from shopcloud_secrethub import SecretHub
    hub = SecretHub(user_app="test-script", api_token='d7d76aaf-f054-456d-a458-382729d24f01')
    secret = hub.read('talk-point/test-repo/secret_key')
    assert secret is not None
