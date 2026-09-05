# Generating an RSA Key Pair
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_gen_rsa_session_key_pair.htm
- Fetched: 2026-09-05 02:32 CDT

# Generating an RSA Key Pair

Learn how to generate an RSA key pair using the Key Management utility.

The genRSAKeyPair command generates an RSA asymmetric key pair. You specify the key type, modulus length, and a public exponent.
Note  
  
You must wait for the encryption key to get replicated to all replicas before you start using the key. To verify the key replication status, you can run the "getKeyInfo" command in Global mode using the OCI HSM User Management Utility.
Generate RSA key pair specifying modulus length, public exponent, and key label.
Note  
  
When you generate or import keys, we recommend you to set the "min_srv" value as 2.

Syntax
```

```

Where,

Parameter Description
-h displays this information
-m specifies the modulus length: eg. 2048
-e specifies the public exponent: any odd number typically &gt;= 65537 to 2^31 - 1
-l Specifies the key label, if label contains spaces it should be written in between " characters.
-sess Specifies key as session key
-nex set the key as non-extractable
-min_srv Specifies the minimum number of HSMs in which the key is synchronized before the value of the -timeout parameter expires. If the key is not synchronized to the specified number of servers in the time allotted, it is not created. Dafault value for min_srv is 2.
-timeout Specifies the number of seconds to wait for the key to get synced when min_srv option is used. If nothing is specified, the polling will continue forever

Example
```

```
