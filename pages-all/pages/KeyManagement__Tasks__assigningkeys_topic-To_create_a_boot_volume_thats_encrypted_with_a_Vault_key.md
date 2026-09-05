# Creating a Boot Volume Encrypted with a Vault key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_boot_volume_thats_encrypted_with_a_Vault_key.htm
- Fetched: 2026-09-05 02:31 CDT

# Creating a Boot Volume Encrypted with a Vault key

Learn how to create an encrypted boot volume in OCI using a master encryption key.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_boot_volume_thats_encrypted_with_a_Vault_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_boot_volume_thats_encrypted_with_a_Vault_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_boot_volume_thats_encrypted_with_a_Vault_key.htm#)
- 

This task isn't available in the OCI Console.
- 

Open a command prompt and run`oci bv boot-volume create`to create a boot volume that is encrypted with a Vault service master encryption key:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Use the[CreateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume)API to create a boot volume using a vault key.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
