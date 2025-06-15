# Zero-Knowledge Proof (ZKP) Authentication Concept

This repository contains a conceptual Python mock demonstrating the fundamental principles of Zero-Knowledge Proofs (ZKPs) in authentication flows.

## Project Context
This code was developed as an exploratory proof-of-concept for my MSc dissertation: *"A Privacy-Preserving, Zero-Trust Smart Contract Compliance Auditing SaaS using Zero-Knowledge Proofs and DLT."*

It serves to demonstrate how cryptographic commitment schemes can be used to prove knowledge of a secret (like a password or an audit state) without ever transmitting or exposing the underlying secret data over the network.

## How it works
1. **The Prover** generates a random salt and creates a SHA-256 hash commitment of the `secret + salt`.
2. **The Network** only sees the opaque hash and the salt. The plaintext secret is never transmitted.
3. **The Verifier** uses the salt to independently verify the commitment.

This foundational concept scales up into complex `zk-SNARK` implementations used in decentralized ledgers and privacy-preserving compliance auditing.

## Usage
```bash
python3 src/zkp_mock.py
```
