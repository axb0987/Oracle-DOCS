# Exporting a Symmetric Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_kgmt_mgmt_export_symkey.htm
- Fetched: 2026-09-05 02:32 CDT

# Exporting a Symmetric Key

Configure command for exporting a Symmetric Key.

The exSymKey command exports plain text copy of a symmetric key from the HSM and saves it in a file on the disk.

Open a command prompt and run`exSymKey`command to export a symmetric key.

Syntax
```

```

Where,

Parameter Description
-h displays this information
-w specifies the handle of the wrapping key
-k specifies the public key handle
-m Specifies the wrapping mechanism (Optional) CLOUDHSM_AES_KEY_WRAP and NIST_AES_WRAP_PAD. Default value is 4.
-wk Specifies the AES key to unwrap the key that is being exported. Enter the path and name of a file that contains a plaintext AES key.

Example
```

```
