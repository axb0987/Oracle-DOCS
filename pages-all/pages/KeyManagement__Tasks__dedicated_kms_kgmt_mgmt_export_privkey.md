# Export a Private Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_kgmt_mgmt_export_privkey.htm
- Fetched: 2026-09-05 02:32 CDT

# Export a Private Key

Configure command for exporting a private Key.

The`exportPrivateKey`command exports asymmetric private key from an HSM to a file.

Open a command prompt and run`exportPrivateKey`command to export asymmetric private key from an HSM to a file.

Syntax
```

```

Where,

Parameter Description
-h displays this information
-w specifies the handle of the wrapping key
-k specifies the private key handle of the private key to be exported.
-m Specifies the wrapping mechanism with which to wrap the private key being exported. For example, CLOUDHSM_AES_KEY_WRAP and NIST_AES_WRAP mechanism. Default value is 4.
-out specifies the file to write the exported private key
-wk Specifies the key for unwrapping the key being exported. Enter the path and name of a file that contains a plaintext AES key.

Example
```

```
