# Security Training

This repository holds notes and hands-on experiments from my ongoing security learning. Unlike a course or a single project, this is meant to keep growing over time, cryptography today, other areas of security as I work through them.

Each topic gets its own folder, with working code I actually ran and tested myself, not just theory copied down.

## Repository Structure

    security-training/
    │
    ├── cryptography/          # HMAC, hashing, and related primitives
    │   └── hmac_demo.py       # HMAC-SHA256 signing and verification, with
    │                          # a tamper-detection demo
    │
    └── requirements.txt       # dependencies, once any topic needs one

More folders will be added here as I move into other areas, web security, network security, whatever comes next.

## Setup

The cryptography examples currently use only Python's standard library, `hmac` and `hashlib`, so nothing needs installing to run them.

    python3 cryptography/hmac_demo.py

If a later topic needs external packages, they'll be added to `requirements.txt` and this section will be updated.

## Goals

- Build a real, working understanding of security concepts, not just read about them
- Keep a running, organized record of what I've actually worked through
- Support my broader work in AI security research, where a lot of this groundwork directly applies

## Topics Covered

- Cryptography: HMAC-SHA256 signing and verification, why the construction prevents length extension attacks, and why constant-time comparison matters