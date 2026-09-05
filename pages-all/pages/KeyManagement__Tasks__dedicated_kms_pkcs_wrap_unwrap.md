# Wrapping a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_pkcs_wrap_unwrap.htm
- Fetched: 2026-09-05 02:33 CDT

# Wrapping a Key

Configure command to wrap a key.

The`wrapKey`command enables you to wrap sensitive keys from HSM to host. You can identify the key by its handle.

Open a command prompt and run`wrapKey`command to wrap sensitive keys from HSM to host. You can identify the key by its handle.
Note  
  
Only a key owner can delete a key.

Syntax
```

```
Where,

Parameter Description
`-h`displays this information
`-f`specifies the key handle to wrap
`-w`specifies the wrapping key. enter the key handle of an AES key or RSA key value on the HSM.
-m The value representing the wrapping mechanism.
-out The path and output file name.
-aad name of the file containing aad.
-noheader Omits the header that specifies CloudHSM-specific key attributes.
-i The initialization vector (IV) (hex value).
-iv_file The file in which you want to write the IV value obtained in response.
-tag_size The size of tag to be saved along with wrapped blob.

Example
```

```
