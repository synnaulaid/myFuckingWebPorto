#!/usr/bin/env bash
set -e

URL=${1:-http://localhost:5000/github/webhook}
SECRET=${2:-sipersecret}

payload='{"ref":"refs/heads/main","repository":{"full_name":"user/repo"},"pusher":{"name":"tester"}}'
sig='sha256='$(printf '%s' "$payload" | openssl dgst -sha256 -hmac "$SECRET" -binary | xxd -p -c 256)

curl -s -X POST "$URL" \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: push" \
  -H "X-Hub-Signature-256: $sig" \
  -d "$payload"
echo
