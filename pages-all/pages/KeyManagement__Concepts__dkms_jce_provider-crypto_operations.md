# Crypto Operations and Mechanisms
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-crypto_operations.htm
- Fetched: 2026-09-05 02:31 CDT

# Crypto Operations and Mechanisms

Learn about the operations, mechanisms, and algorithms supported by the Dedicated Key Management JCE provider.

## Generate Keys and Key Pairs

Use the JCE provider to generate keys of the following types:
- 

RSA: RSA is widely used for secure data transmission, digital signatures, and key exchange protocols.
- 

EC (Elliptic Curve): Elliptic curve cryptography offers high security with smaller key sizes, making it efficient for modern cryptographic applications such as SSL/TLS and blockchain.
- 

AES (Advanced Encryption Standard): AES is a widely adopted encryption standard for protecting sensitive data, providing strong security for both data-at-rest and data-in-transit.
- 

DESede (Triple DES): Triple DES is an enhancement of the original DES algorithm, offering improved security through several rounds of encryption. DESede is supported only on non-FIPS clusters, and is typically used for legacy applications that require backward compatibility.

## Convert Keys with Key Factories

Key factories are used to convert keys to conform with a given key specifications. See[Interface KeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html)in the Java Platform API documentation for more information. The two primary types of key factories for JCE are:

### SecretKeyFactory

The`SecretKeyFactory`factory is designed for importing or deriving symmetric keys. It lets you to pass a supported`Key`or`KeySpec`to import symmetric keys. See[Class SecretKeyFactory](https://docs.oracle.com/javase/8/docs/api/javax/crypto/SecretKeyFactory.html)in the Java Platform API documentation for more information.

The following`KeySpec`classes are compatible with the`generateSecret`method:
- KeyAttributesMap: This class lets you import key bytes along with associated attributes.
- SecretKeySpec: This class is used to import symmetric key specifications. See[Interface SecretKey](https://docs.oracle.com/javase/8/docs/api/javax/crypto/SecretKey.html)in the Java Platform API documentation for more information.
- DESedeKeySpec: This class is used only with the DESedeKeyFactory, and lets you import the DESedeKey specification. Note that DESede is supported only on non-FIPS clusters. See[Class DESedeKeySpec](https://docs.oracle.com/javase/8/docs/api/javax/crypto/spec/DESedeKeySpec.html)in the Java Platform API documentation for more information. This class lets you derive symmetric keys based on an existing DKMS AES key.

The`translateKey`method can accept any key that implements the`Key`interface, which provides flexibility in key handling. To translate a persistent key, set`DEDICATED_KMS_JCE_TRANSLATE_KEY_PERSISTENT`as`TRUE`in your environment variables or system properties.

### KeyFactory

The`KeyFactory`factory is used for importing asymmetric keys. By passing a valid`Key`or`KeySpec`, you can import asymmetric keys into Dedicated Key Management. See[Class KeyFactory](https://docs.oracle.com/javase/8/docs/api/java/security/KeyFactory.html)in the Java Platform API documentation for more information.

The following`KeySpec`classes are supported for the`generatePublic`method:
- KeyAttributesMap: Available for both RSA and EC KeyTypes.
- X509EncodedKeySpec: This class is for`generatePublic`in the`RSAKeyFactory`and`EcKeyFactory`, and is used to import the X509 encoded key specification. See[Class X509EncodedKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/X509EncodedKeySpec.html)in the Java Platform API documentation for more information.
- RSAPublicKeySpec: For`generatePublic`in the`RSAKeyFactory`. Use this class to import the RSA public key specification. See[Class RSAPublicKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/RSAPublicKeySpec.html)in the Java Platform API documentation for more information.
- ECPublicKeySpec: For`generatePublic`in the`EcKeyFactory`. Use this class to import the EC public key specification. See[Class ECPublicKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/ECPublicKeySpec.html)in the Java Platform API documentation for more information.

The following`KeySpec`classes are supported for the`generatePrivate`method:
- PKCS8EncodedKeySpec: Used for both EC and RSA private keys. See[Class PKCS8EncodedKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/PKCS8EncodedKeySpec.html)in the Java Platform API documentation for more information.
- RSAPrivateCrtKeySpec: For for RSA private keys only. See[Class RSAPrivateCrtKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/RSAPrivateCrtKeySpec.html)in the Java Platform API documentation for more information.
- ECPrivateKeySpec: For for EC private keys only. See[Class ECPrivateKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/ECPrivateKeySpec.html)in the Java Platform API documentation for more information.

The`translateKey`method accepts any key that implements the`Key`interface, providing seamless conversion between different key formats.

## Cipher Functions

The Dedicated Key Management JCE provider supports following combinations of algorithm, mode, and padding.

Algorithm Mode Padding Notes
AES CBC

AES/CBC/NoPadding

AES/CBC/PKCS5Padding

Implements Cipher.ENCRYPT_MODE and Cipher.DECRYPT_MODE.

Implements Cipher.UNWRAP_MODE for AES/CBC NoPadding
AES ECB

AES/ECB/PKCS5Padding

AES/ECB/NoPadding Implements Cipher.ENCRYPT_MODE and Cipher.DECRYPT_MODE.
AES CTR AES/CTR/NoPadding Implements Cipher.ENCRYPT_MODE and Cipher.DECRYPT_MODE.
AES GCM AES/GCM/NoPadding

Implements Cipher.WRAP_MODE, Cipher.UNWRAP_MODE, Cipher.ENCRYPT_MODE, and Cipher.DECRYPT_MODE.

When performing AES-GCM encryption, the HSM ignores the initialization vector (IV) in the request and uses an IV that it generates. When the operation completes, you must call Cipher.getIV() to get the IV.
AESWrap ECB

AESWrap/ECB/NoPadding

AESWrap/ECB/PKCS5Padding

AESWrap/ECB/ZeroPadding Implements Cipher.WRAP_MODE and Cipher.UNWRAP_MODE.
DESede (Triple DES) CBC

DESede/CBC/PKCS5Padding

DESede/CBC/NoPadding

Implements Cipher.ENCRYPT_MODE and Cipher.DECRYPT_MODE.

DESede is supported only on non-FIPS clusters.
DESede (Triple DES) ECB

DESede/ECB/NoPadding

DESede/ECB/PKCS5Padding

Implements Cipher.ENCRYPT_MODE and Cipher.DECRYPT_MODE.

DESede is supported only on non-FIPS clusters.
RSA ECB

RSA/ECB/PKCS1Padding see note[1](https://docs.aws.amazon.com/cloudhsm/latest/userguide/java-lib-supported_5.html#java-gen-key-pairs-5-note-1)

RSA/ECB/OAEPPadding

RSA/ECB/OAEPWithSHA-1ANDMGF1Padding

RSA/ECB/OAEPWithSHA-224ANDMGF1Padding

RSA/ECB/OAEPWithSHA-256ANDMGF1Padding

RSA/ECB/OAEPWithSHA-384ANDMGF1Padding

RSA/ECB/OAEPWithSHA-512ANDMGF1Padding Implements Cipher.WRAP_MODE, Cipher.UNWRAP_MODE, Cipher.ENCRYPT_MODE, and Cipher.DECRYPT_MODE.
RSA ECB RSA/ECB/NoPadding Implements Cipher.ENCRYPT_MODE and Cipher.DECRYPT_MODE.
RSAAESWrap ECB

RSAAESWrap/ECB/OAEPPadding

RSAAESWrap/ECB/OAEPWithSHA-1ANDMGF1Padding

RSAAESWrap/ECB/OAEPWithSHA-224ANDMGF1Padding

RSAAESWrap/ECB/OAEPWithSHA-256ANDMGF1Padding

RSAAESWrap/ECB/OAEPWithSHA-384ANDMGF1Padding

RSAAESWrap/ECB/OAEPWithSHA-512ANDMGF1Padding Implements Cipher.WRAP_MODE and Cipher.UNWRAP_MODE.

## Sign and Verify Functions

DKMS JCE provider supports the following types of signature and verification:

RSA Signature Types
- 

NONEwithRSA
- 

RSASSA-PSS
- 

SHA1withRSA
- 

SHA1withRSA/PSS
- 

SHA1withRSAandMGF1
- 

SHA224withRSA
- 

SHA224withRSAandMGF1
- 

SHA224withRSA/PSS
- 

SHA256withRSA
- 

SHA256withRSAandMGF1
- 

SHA256withRSA/PSS
- 

SHA384withRSA
- 

SHA384withRSAandMGF1
- 

SHA384withRSA/PSS
- 

SHA512withRSA
- 

SHA512withRSAandMGF1
- 

SHA512withRSA/PSS

ECDSA Signature Types
- 

NONEwithECDSA
- 

SHA1withECDSA
- 

SHA224withECDSA
- 

SHA256withECDSA
- 

SHA384withECDSA
- 

SHA512withECDSA

## Message Digest Functions

Generate cryptographic hash values for data integrity verification. DKMS JCE provider supports the following message digests.
- 

SHA-1
- 

SHA-224
- 

SHA-256
- 

SHA-384
- 

SHA-512

## Hash-based Message Authentication Code (HMAC) Functions

Generate hash-based message authentication code (HMAC) keys for cryptographic hash functions. HMAC is used for verifying data integrity and authenticity by applying a secret key with a hash function. The Dedicated Key Management JCE provider supports the following HMAC algorithms:
- 

HmacSHA1 (Maximum data size in bytes: 16288)
- 

HmacSHA224 (Maximum data size in bytes: 16256)
- 

HmacSHA256 (Maximum data size in bytes: 16288)
- 

HmacSHA384 (Maximum data size in bytes: 16224)
- 

HmacSHA512 (Maximum data size in bytes: 16224)

## Cipher-based message authentication code (CMAC)

Generate cipher-based message authentication codes (CMACs) using block ciphers (for example, AES) to produce an authentication code that ensures message integrity and authenticity. CMAC operates similarly to HMAC but uses a symmetric key cipher for the cryptographic operation.
