# Generating an ECC Key Pair
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicate_kms_key_mgmt_gen_ecc_key_pair.htm
- Fetched: 2026-09-05 02:32 CDT

# Generating an ECC Key Pair

Learn how to generate an ECC Key pair using the Dedicated Key Management utility.

The genECCKeyPair command generates an Elliptic Curve Cryptography (ECC) key pair in the HSMs.
Note  
  
You must wait for the encryption key to get replicated to all replicas before you start using the key. To verify the key replication status, you can run the "getKeyInfo" command in Global mode using the Key Management Utility.

Open a command prompt and run`genECCKeyPair`command to generate an ECC key pair in a partition.
Note  
  
When you generate or import keys, we recommend you to set the "min_srv" value as 3.

Syntax
```

```

Parameter Description
-h Displays this information
-i specifies the Curve ID
-l specifies the key label, if label contains spaces, it should be written in between " characters.
-sess specifies key as session key
-min_srv specifies the minimum number of HSMs in which the key is synchronized before the value of the -timeout parameter expires. If the key is not synchronized to the specified number of servers in the time allotted, it is not created. Dafault value for min_srv is 2.
-timeout specifies the number of seconds to wait for the key to get synced when min_srv option is used. If nothing is specified, the polling will continue forever.
-nex set the key as non-extractable
The following are HSM supported ECC CurveIds NID_X9_62_prime192v1 = 1 NID_X9_62_prime256v1 = 2 NID_sect163k1 = 3 NID_sect163r2 = 4 NID_sect233k1 = 5 NID_sect233r1 = 6 NID_sect283k1 = 7 NID_sect283r1 = 8 NID_sect409k1 = 9 NID_sect409r1 = 10 NID_sect571k1 = 11 NID_sect571r1 = 12 NID_secp224r1 = 13 NID_secp384r1 = 14 NID_secp521r1 = 15 NID_secp256k1 = 16 NID_secp192k1 = 17 NID_brainpoolP160r1 = 18 NID_brainpoolP192r1 = 19 NID_brainpoolP224r1 = 20 NID_brainpoolP256r1 = 21 NID_brainpoolP320r1 = 22 NID_brainpoolP384r1 = 23 NID_brainpoolP512r1 = 24 CUSTOMIZED_NID_FRP256V1 = 25 NID_X25519 = 26 NID_X448 = 27 NID_ED25519 = 28 NID_secp224k1 = 29

Example
```

```
