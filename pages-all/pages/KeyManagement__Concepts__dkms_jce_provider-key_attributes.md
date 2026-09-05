# Key Attributes for the JCE Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-key_attributes.htm
- Fetched: 2026-09-05 02:31 CDT

# Key Attributes for the JCE Provider

The key attributes in this topic can be set during key generation and key importing when using the Dedicated KMS JCE Provider.

## Specifying Key Attributes

The following example shows how to specify attributes when using the key generator:
```

```

## Key Attributes Reference

Attribute Supported Values Default Value Notes
CRT_COEFFICIENT For use in the RSA Key Factory. Represents the Chinese Remainder Theorem coefficient q-1 mod p as byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information
CURVE_TYPE secp224r1 (P-224), secp256r1 (P-256), secp256k1 (Blockchain), secp384r1 (P-384), and secp521r1 (P-521) For use in the EC key pair generator. Used to specify an elliptic curve (EC) for a key pair generator. The EC curve is then used in EC related cryptographic operations.
EC_PARAMS For use in the EC Key Factory. Use`EC_PARAMS`in an elliptic curve key factory to represent the elliptic curve using`ECParameterSpec`, with a`byte[]`representation for serialization.
EC_POINT For use in the EC Key Factory. Use EC_POINT in an elliptic curve key factory to specify a point on a elliptic curve, with a`byte[]`representation for serialization.
EXTRACTABLE True or False (Boolean) True (symmetric key, asymmetric private key) True indicates you can export this key from the HSM.
ID A user-defined value used to identify the key.
KEY_TYPE AES, DESede, EC, RSA The type of key.
LABEL A user-defined string to identify keys on your HSM. We recommend using a unique label for each key.
MODULUS Represents the modulus n as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PERSISTENT True or False (Boolean) False Set to TRUE to make a persistent key. Set to FALSE to create an ephemeral key which is automatically erased when the connection to the HSM is broken or logged out.
PRIME_EXPONENT_P For use in the RSA key factory. Represents the d mod (q-1) as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PRIME_EXPONENT_Q For use in the RSA key factory. Represents the d mod (q-1) as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PRIME_P For use in the RSA key factory. Represents the prime factor p of n as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PRIME_Q For use in the RSA key factory. Represents the prime factor q of n as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PRIVATE_EXPONENT For use in the RSA key factory. Represents the private exponent d as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PRIVATE_LABEL Specifies a user defined label for the private-key.
PUBLIC_EXPONENT For use in the RSA key factory. Represents the public exponent e as a byte array. See[PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.txt)for more information.
PUBLIC_LABEL Specifies a user defined label for the public-key.
SIZE See[Key Types and Algorithms](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-key_types_algorithms.htm)for valid key size values. The size of a key.
