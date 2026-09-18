import hmac
import hashlib

def sign(secret_key: bytes, message: bytes):
    """
    Produce an HMAC-SHA256 signature for a message, using a secret key.
    Returns the signature as a hex string, plain text, easy to store
    or send over a network.
    """
    signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
    
    return signature


def verify(secret_key: bytes, message: bytes, signature: str):
    """
    Recompute what the signature SHOULD be right now, using the same
    key, and check it against a signature that was given to us.
    Returns True only if they match exactly.
    """
    
    expected_signature = sign(secret_key, message)
    verification = hmac.compare_digest(expected_signature, signature)
    
    return verification


# Actual Document
message = b"Love Me"
message_sig = sign(b"mykey", message)

# The key used and the message has to be the same
verification_result = verify(b"mykey", b"Love Me", message_sig)

print(verification_result)

# --- Using it ---
print("--- Using it ---")
secret_key = b"a-secret-only-the-signer-should-know"

# Step 1: sign a message
message = b"transfer $500 to account 12345"
signature = sign(secret_key, message)

# Step 2: verify it, correctly, nothing has changed
is_valid = verify(secret_key, message, signature)
# True
print(is_valid)

# Step 3: verify it AFTER the message has been changed
tampered_message = b"transfer $5000 to account 12345"
is_valid_after_tamper = verify(secret_key, tampered_message, signature)
# False
print(is_valid_after_tamper)