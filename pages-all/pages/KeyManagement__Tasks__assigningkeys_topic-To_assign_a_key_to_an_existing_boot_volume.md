# Assigning a Key to a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_boot_volume.htm
- Fetched: 2026-09-05 02:31 CDT

# Assigning a Key to a Boot Volume

Assigning a key to a boot volume using the OCI Console and CLI interface.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_boot_volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_boot_volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_boot_volume.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes . In the Block Storage menu on the sidebar, select Boot Volumes .
- Under List Scope , in the Compartment list, select the compartment that contains the boot volume that you want to encrypt with a Vault service master encryption key.
- From the list of volumes, select the volume name.
- 

Do one of the following:
- If the volume already has a key assigned to it, next to Encryption Key , select Edit to assign a different key.
- If the volume does not already have a key assigned to it, next to Encryption Key , select Assign .
- 

Select the vault compartment, vault, key compartment, and key.
- 

When you are finished, select Assign or Update , as appropriate.
- 

Open a command prompt and run`oci bv boot-volume-kms-key update`to assign a new Vault service master encryption key to an existing boot volume:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Run the[AssignKeytoBootVolume](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/WorkRequest/GetWorkRequest)operation to &lt;task-being-performed&gt;.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
