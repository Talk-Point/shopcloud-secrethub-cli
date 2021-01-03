python3 -m shopcloud_secrethub write talk-point/test-repo/file-as-secret -i app.temp.yaml
python3 -m shopcloud_secrethub read talk-point/test-repo/file-as-secret
python3 -m shopcloud_secrethub read talk-point/test-repo/file-as-secret -o json
python3 -m shopcloud_secrethub read talk-point/test-repo/file-as-secret -o raw