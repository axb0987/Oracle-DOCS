# Editing a Key to a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm
- Fetched: 2026-09-05 02:31 CDT

# Editing a Key to a Block Volume

Editing a key to a block volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm#)
- 

Important  
  
The Block Volume service does not support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This applies to block volumes and boot volumes.
- Open the navigation menu and select Storage . Under Block Storage , select Block Volume Backups .
- Under List Scope , in the Compartment list, select the compartment that contains the block volume that you want to encrypt with a Vault service master encryption key.
- From the list of volumes, select the volume name.
- 

Then, do one of the following:
- If the volume already has a key assigned to it, next to Encryption Key , select Edit to assign a different key.
- If the volume doesn't already have a key assigned to it, next to Encryption Key , select Assign .
- 

Select the vault compartment, vault, key compartment, and key.
- 

When you're finished, select Assign or Update , as appropriate.
- 

Open a command prompt and run`oci bv volume-kms-key update`to assign a new Vault service master encryption key to an existing block volume:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Run the[UpdateVolumeKmsKey](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeKmsKey/UpdateVolumeKmsKey)operation to update a key for a block volume.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
