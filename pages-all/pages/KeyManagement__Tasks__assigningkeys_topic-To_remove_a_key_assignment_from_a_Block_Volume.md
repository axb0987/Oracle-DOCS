# Removing a Key Assignment from a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_Block_Volume.htm
- Fetched: 2026-09-05 02:31 CDT

# Removing a Key Assignment from a Block Volume

Remove a key assignment from a Block Volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_Block_Volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_Block_Volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_Block_Volume.htm#)
- 

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes .
- Under List Scope , in the Compartment list, select the compartment that contains the block volume from which you want to remove a Vault service key assignment.
- From the list of volumes, select the volume name.
- 

Next to Encryption Key , select Unassign .
- 

In the Confirm dialog box, select OK to remove the key assignment from the volume.
- 

Open a command prompt and run`oci bv boot-volume-kms-key delete`to remove the Vault service master encryption key assigned to an existing boot volume:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
-
