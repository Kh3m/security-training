# Security Training

This repository holds notes and hands-on experiments from my ongoing security learning. Unlike a course or a single project, this is meant to keep growing over time, cryptography today, other areas of security as I work through them.

Each topic gets its own folder, with working code I actually ran and tested myself, not just theory copied down.

## Repository Structure

    security-training/
    │
    └── cryptography/
        │
        ├── 00-foundations/
        │   ├── 01-bits-bytes-hex.ipynb     # bits vs bytes, 0-255, binary and hex
        │   │                               # with format codes, bytes-to-hex math
        │   └── 02-bytes-and-encoding.ipynb # str vs bytes, UTF-8, encode/decode,
        │                                   # hex and Base64, common mistakes
        │
        ├── 01-hmac/
        │   └── 00-hmac.py                  # HMAC-SHA256 signing and verification,
        │                                   # with a tamper-detection demo
        │
        ├── 02-hashlib/
        │   ├── 01-sha256-basics.ipynb      # SHA-256 with hashlib, digest vs
        │   │                               # hexdigest, bytes literals, verifying
        │   ├── 02-one-small-change.ipynb   # avalanche effect: one-bit input change
        │   │                               # flips about half the output bits
        │   ├── 03-hashing-files.ipynb      # (in progress)
        │   ├── 04-hash-vs-hmac.ipynb       # (in progress)
        │   └── examples/
        │       └── verify_download.py      # (in progress)
        │
        └── 03-digital-signatures/
            └── 00-digital-signatures.py    # (in progress)

Folders are numbered in the order I'd work through them. Notebooks inside a folder are numbered too. `00-foundations` comes first because everything after it, hashing, HMAC, signatures, works on bytes rather than text, and it starts with what a byte actually is before moving on to how text becomes bytes.

More top-level folders will be added as I move into other areas, web security, network security, whatever comes next.

## Setup

The cryptography examples currently use only Python's standard library, `hmac` and `hashlib`, so nothing needs installing to run the scripts.

    python cryptography/01-hmac/00-hmac.py

The `.ipynb` files are Jupyter notebooks. Open them in VS Code with the Jupyter extension, or run them with Jupyter:

    pip install notebook
    jupyter notebook cryptography/00-foundations/01-bits-bytes-hex.ipynb

If a later topic needs external packages, they'll go in a `requirements.txt` and this section will be updated.

## Goals

- Build a real, working understanding of security concepts, not just read about them
- Keep a running, organized record of what I've actually worked through
- Support my broader work in AI security research, where a lot of this groundwork directly applies

## Topics Covered

- Foundations: bits and bytes, why a byte holds 0 to 255, writing numbers in binary and hex with `format()` codes, why one byte is two hex characters
- Encoding: text vs bytes, Unicode code points and UTF-8, encoding and decoding, why the same text in different encodings hashes differently, and showing bytes as hex or Base64
- Hashing: SHA-256 with `hashlib`, raw `digest()` vs readable `hexdigest()`, why hash functions need bytes, and verifying a hash with `hmac.compare_digest`, including what a matching hash does not prove (who sent it)
- Avalanche effect: changing one input bit flips about half of SHA-256's 256 output bits, measured on one pair and averaged over 1,000 messages
- HMAC: HMAC-SHA256 signing and verification, why the construction prevents length extension attacks, and why constant-time comparison matters

## Up Next

- Hashing files and hash vs HMAC (notebooks in `02-hashlib/`)
- Verifying a downloaded file against a published checksum
- Digital signatures
