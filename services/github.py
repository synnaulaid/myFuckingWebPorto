# service/github.py
import hmac
import hashlib

def verify_webhook(signature_header: str, payload: bytes, secret: str) -> bool:
    """
    Verifikasi X-Hub-Signature-256 dari GitHub.
    """
    if not signature_header or not signature_header.startswith("sha256="):
        return False

    sig = signature_header.split("=", 1)[1]
    mac = hmac.new(secret.encode(), msg=payload, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(mac, sig)

# Opsional: helper untuk debug
def hmac_signature(payload: bytes, secret: str) -> str:
    return "sha256=" + hmac.new(secret.encode(), msg=payload, digestmod=hashlib.sha256).hexdigest()
