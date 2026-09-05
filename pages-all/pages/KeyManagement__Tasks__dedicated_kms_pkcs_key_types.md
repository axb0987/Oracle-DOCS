# Key Types
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_pkcs_key_types.htm
- Fetched: 2026-09-05 02:33 CDT

# Key Types

PKCS #11 key types.

Following are the supported key types in PCKS#11 library.

Key Type Supported Sizes
AES 128, 192, and 256 bits
RSA

1024 - 4096-bit modulus in steps of 256 bits.

Note : Key generation of 1024 modulus size key is supported only in the non-FIPS mode of operation.
ECDSA

Curves supported:

P-256, P-384 Note : Only Curves P-256 and P-384 are supported for sign and verify operations.
The PKCS #11 library supports the following crypto operations:
- Encryption and decryption using AES and RSA algorithms
- Sign and verify using RSA, ECDSA, and HMAC algorithms
- Generate Symmetric Key and Key Pairs using RSA, AES, and ECDSA algorithms
-
