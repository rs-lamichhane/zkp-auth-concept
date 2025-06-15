import hashlib
import os

class ZKPMockProver:
    """
    A conceptual mock of a Zero-Knowledge Proof (ZKP) prover.
    Demonstrates how a client can prove knowledge of a secret without transmitting the secret itself,
    using a salted hash commitment scheme.
    """
    def __init__(self, secret_password):
        self._secret = secret_password
        self.salt = os.urandom(16).hex()
        
    def generate_commitment(self):
        """Generates a cryptographic commitment."""
        payload = f"{self._secret}:{self.salt}".encode('utf-8')
        return hashlib.sha256(payload).hexdigest()

class ZKPMockVerifier:
    """
    A conceptual mock of a ZKP verifier.
    """
    def __init__(self, registered_secret):
        self._registered_secret = registered_secret
        
    def verify(self, commitment, salt):
        """Verifies the commitment matches the expected hash structure."""
        expected_payload = f"{self._registered_secret}:{salt}".encode('utf-8')
        expected_hash = hashlib.sha256(expected_payload).hexdigest()
        return commitment == expected_hash

if __name__ == "__main__":
    print("--- Zero-Knowledge Proof (ZKP) Authentication Concept ---")
    
    user_password = "super_secret_password_123"
    
    # 1. Registration Phase (Server knows the secret initially for setup)
    verifier = ZKPMockVerifier(user_password)
    
    # 2. Authentication Phase (Client proves knowledge without sending password)
    prover = ZKPMockProver(user_password)
    
    # Client sends ONLY the commitment and the salt over the network
    commitment = prover.generate_commitment()
    salt = prover.salt
    
    print(f"[Network Intercept] Transmitting Commitment: {commitment}")
    print(f"[Network Intercept] Transmitting Salt: {salt}")
    print("[Network Intercept] Note: The actual password is NEVER transmitted.\n")
    
    # 3. Server verifies
    is_valid = verifier.verify(commitment, salt)
    
    if is_valid:
        print("[+] Authentication Successful: Prover demonstrated knowledge of the secret.")
    else:
        print("[-] Authentication Failed.")
