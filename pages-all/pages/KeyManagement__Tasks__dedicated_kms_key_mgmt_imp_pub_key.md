# Importing a Public Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_imp_pub_key.htm
- Fetched: 2026-09-05 02:32 CDT

# Importing a Public Key

Configure command for exporting a Public Key.

The`importPubkey`command enables you to import a PEM-encoded public key (RSA/EC) into the HSM.
Note  
  
You must wait for the encryption key to get replicated to all replicas before you start using the key. To verify the key replication status, you can run the "getKeyInfo" command in Global mode using the OCI HSM User Management Utility.
Open a command prompt and run`importPubkey`command to import a`PEM-encoded`public key (RSA/EC) into the HSM.
Note  
  
When you generate or import keys, we recommend you to set the "min_srv" value as 2.

Syntax
```

```

Where,

Parameter Description
-h Displays this information.
-l Label for the new key, if label contains spaces it should be written in between " characters.
-t File containing the PEM encoded public key.
-min_srv Specifies the minimum number of servers on which the inserted masked object is synchronized before the timeout parameter expires. The default value is 2.
-f

Filename containing the key to import. File size for each key type:

AES = 16, 24, or 32 bytes
-w Wrapping key handle (KEK = 4).
-timeout Indicates the wwait time (in seconds) for the key to sync across servers.

Example
```

```
