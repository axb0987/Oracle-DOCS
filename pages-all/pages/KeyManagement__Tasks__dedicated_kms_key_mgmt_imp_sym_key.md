# Importing a Symmetric Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_imp_sym_key.htm
- Fetched: 2026-09-05 02:32 CDT

# Importing a Symmetric Key

Configure command for importing a Symmetric Key.

The`imSymKey`command enables you to import a symmetric key into the HSM.

Open a command prompt and run`imSymKey`command to import a symmetric key into the HSM.

Syntax
```

```

Where,

Parameter Description
`-h`Displays this information
`-l`Private key label.
`-t`

Key type:`31`= AES
`-f`

Filename containing the key to import. File size for each key type:

AES = 16, 24, or 32 bytes
`-w`Wrapping key handle (KEK = 4).
`-s`Specifies the key size in bytes for AES : 16, 24, 32
`-sess`specifies key as session key.
`-min_srv`specifies the minimum number of HSMs in which the key is synchronized before the value of the -timeout parameter expires. If the key is not synchronized to the specified number of servers in the time allotted, it is not created. Default value for min_srv is 2.
`-timeout`Specifies the number of seconds to wait for the key to get synced when min_srv option is used. If nothing is specified, the polling will continue forever.

Example
```

```
