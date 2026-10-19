# hashlib works on bytes, not text, so we encode the string first
import hashlib

# NOTE A hash function takes any input and turns it into a fixed-size “fingerprint”. 
# SHA-256 always gives 256 bits (32 bytes), no matter how big or small the input is.

message = "Hello, Khemshield"

# encode Turns your text into bytes. 
# If you pass a plain string, Python will give you a TypeError. 
message_bytes = message.encode("utf-8")
message_hash = hashlib.sha256(message_bytes)
# hashlib.new("sha256", message_bytes) allow us to choose the algorithm by name

# digest gives the raw 32 bytes, which is what computers usually store or compare.
message_hash_digest_raw = message_hash.digest()

# hexdigest gives a readable string of 64 characters (each hex character holds 4 bits, so 64 × 4 = 256).
message_hash_digest_readable = message_hash.hexdigest()

print("Message: ", message)
print("Message Bytes: ", message_bytes)
print("Message Hash: ", message_hash)
print("Message Hash Digest: ", message_hash_digest_raw)
print("Message Hash Digest Readable: ", message_hash_digest_readable, "\nLen:", len(message_hash_digest_readable))

# NOTE A bytes literal: you can put b in front of the quotes (works for plain English/ASCII text)
print("\n=== Using the b'' literal ===\n", hashlib.sha256(b"Hello, Khemshield").hexdigest())

# Function helpers
def sha256_text(text: str):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


print("\n=== SHA-256 helper ===\n", sha256_text("Love Me Please"))

# NOTE A simple rule to remember: 
# text goes in as bytes, and results come out as bytes (.digest()) 
# unless you ask for a readable version (.hexdigest()).