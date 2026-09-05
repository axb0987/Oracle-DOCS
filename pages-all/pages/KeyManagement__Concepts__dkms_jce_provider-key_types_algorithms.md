# Key Types and Algorithms
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-key_types_algorithms.htm
- Fetched: 2026-09-05 02:31 CDT

# Key Types and Algorithms

Learn what key types and algorithms are supported for the Dedicated Key Management JCE provider.

Key Types and Algorithms

Key Type Description
AES Generate symmetric AES keys with sizes of 128, 192, and 256 bits. AES (Advanced Encryption Standard) is widely used for securing sensitive data in various encryption applications.
Triple DES (3DES, DESede) Generate a 192-bit Triple DES (3DES) key, providing enhanced security over standard DES. This key type is supported only on Non-FIPS (Federal Information Processing Standards) clusters and is commonly used for legacy applications.
EC (Elliptic Curve) Generate elliptic curve (EC) key pairs based on NIST-defined curves. Supported curves include secp224r1 (P-224), secp256r1 (P-256), secp256k1 (Blockchain), secp384r1 (P-384), and secp521r1 (P-521). These EC keys are typically used in modern cryptographic protocols, such as SSL/TLS and blockchain technologies.
RSA Generate RSA key pairs ranging from 2048-bit to 4096-bit, in increments of 256 bits. RSA is a widely-used asymmetric encryption algorithm for securing communications, with larger key sizes providing stronger security.
Message Digest Generate cryptographic hash values for data integrity verification. Supported algorithms include SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, which produce fixed-length digests from arbitrary data.
HMAC (Hash-based Message Authentication Code) Generate HMAC keys for cryptographic hash functions: SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512. HMAC is used for verifying data integrity and authenticity by applying a secret key with a hash function.
