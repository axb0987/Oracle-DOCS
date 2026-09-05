# Verifying Resource Principal Access to Encryption Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/verify-encryption-key-principal.htm
- Fetched: 2026-09-05 02:05 CDT

# Verifying Resource Principal Access to Encryption Keys

If a file system is encrypted with your own key, IAM policies are required for the file system to read the keys stored in Vault. We recommend using the resource principal in these policies.

You can use the CLI or API to verify whether a file system is using the resource principal. If the file system uses the service principal,[update the IAM policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm#required-iam-policy)so that the resource principal has access.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/verify-encryption-key-principal.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/verify-encryption-key-principal.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/verify-encryption-key-principal.htm#)
- 

You can't use the Console to verify which principal the file system uses to read the encryption keys stored in Vault.
- 

Use the[`fs file-system get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/get.html)command and required parameters to get details about a file system:

```

```

The`lifecycle-details`attribute includes details about the principal used by the file system to access the key stored in Vault.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/GetFileSystem)operation to get details about a file system.

The`lifecycleDetails`attribute includes details about the principal used by the file system to access the key stored in Vault.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
