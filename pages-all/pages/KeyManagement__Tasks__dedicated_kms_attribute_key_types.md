# Attribute Key Types
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_attribute_key_types.htm
- Fetched: 2026-09-05 02:32 CDT

# Attribute Key Types

Summary of PKCS #11 attributes and its key types.
Following are the attributes supported in PKCS #11 standard to perform cryptographic operations:

Attribute

Key Type

EC Private

EC Public

RSA Private

RSA Public

AES
CKA Class yes yes yes yes yes
CKA_KEY_TYPE yes yes yes yes yes
CKA_LABEL yes yes yes yes yes
CKA_ID yes yes yes yes yes
CKA_LOCAL yes yes yes yes yes
CKA_TOKEN yes yes yes yes yes
CKA_PRIVATE yes yes yes yes yes
CKA_ENCRYPT No No No yes yes
CKA_DECRYPT No No yes No yes
CKA_DERIVE yes yes yes yes yes
CKA_MODIFIABLE yes yes yes yes yes
CKA_DESTROYABLE yes yes yes yes yes
CKA_SIGN yes No yes No yes
CKA_SIGN_RECOVER No No yes No No
CKA_VERIFY No yes No yes yes
CKA_VERIFY_RECOVER No No No yes No
CKA_WRAP No No No yes yes
CKA_WRAP_TEMPLATE No yes No yes yes
CKA_TRUSTED No yes No yes yes
CKA_WRAP_WITH_TRUSTED yes No yes No yes
CKA_UNWRAP No No yes No yes
CKA_UNWRAP_TEMPLATE yes No yes No yes
CKA_SENSITIVE yes No yes No yes
CKA_EXTRACTABLE yes No yes No yes
CKA_NEVER_EXTRACTABLE yes No yes No yes
CKA_ALWAYS_SENSITIVE R R R R R
CKA_MODULUS No No yes yes No
CKA_MODULUS_BITS No No No yes No
CKA_PRIME_1 No No S No No
CKA_PRIME_2 No No S No No
CKA_COEFFICIENT No No S
CKA_EXPONENT_1 No No S No No
CKA_EXPONENT_2 No No S No No
CKA_PRIVATE_EXPONENT No No S No No
CKA_PUBLIC_EXPONENT No yes yes yes
CKA_EC_PARAMS Yes yes No No No
CKA_EC_POINT No yes No No No
CKA_VALUE S No No No yes
CKA_VALUE_LEN No No No No yes
