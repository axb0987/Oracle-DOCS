# Generating an AES Symmetric Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicate_kms_key_mgmt_gen_aes_key.htm
- Fetched: 2026-09-05 02:32 CDT

# Generating an AES Symmetric Key

Learn how to generate an AES symmetric key with the Dedicated KMS user management utility.

The genSymKey command generates a symmetric key in your HSMs. You can specify the key type and size, assign an ID and label, and share the key with other HSM users.
Note  
  
You must wait for the encryption key to get replicated to all replicas before you start using the key. To verify the key replication status, you can run the "getKeyInfo" command in Global mode.

Open a command prompt and run`genSymKey`command to generate an AES type (-t 31) symmetric key in a partition.

Syntax
```

```

Where,

Parameter Description
-h Displays this information
-l specifies the Key Label, if label contains spaces it should be written in between " characters.
-t Specifies the key type (31 = AES)
-s Specifies the key size in bytes for AES : 16, 24, 32
-sess Specifies key as session key
-min_srv Specifies the minimum number of HSMs in which the key is synchronized before the value of the -timeout parameter expires. If the key is not synchronized to the specified number of servers in the time allotted, it is not created. Dafault value for min_srv is 2.
-timeout Specifies the number of seconds to wait for the key to get synced when min_srv option is used. If nothing is specified, the polling will continue forever.
-nex set the key as non-extractable

Example
```

```
