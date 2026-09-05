# Renaming an External Key Management Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_renaming_vault.htm
- Fetched: 2026-09-05 02:35 CDT

# Renaming an External Key Management Vault

Learn how to rename a vault in OCI External Key Management.

After you create a vault, you can rename it by accessing the Vault Details page.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_renaming_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_renaming_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_renaming_vault.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select External Key Management .
- On the External key Management home page, select the name of the vault you want to rename to see the vault's details.
- Select Edit Name .
- Enter a new name for the vault name and then select Update .
- 

Use the[oci kms management vault update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/update.html)command to rename a vault in External Key Management.

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateVault](https://docs.oracle.com/iaas/api/#/en/key/release/Vault/UpdateVault)API to update the details of an External KMS vault.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
