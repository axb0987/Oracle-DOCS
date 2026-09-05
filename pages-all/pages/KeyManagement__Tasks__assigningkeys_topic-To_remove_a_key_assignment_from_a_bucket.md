# Removing a Key Assignment from a Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_bucket.htm
- Fetched: 2026-09-05 02:31 CDT

# Removing a Key Assignment from a Object Storage

Remove a key assignment from a bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_remove_a_key_assignment_from_a_bucket.htm#)
- 

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Under List Scope , in the Compartment list, select the compartment that contains the bucket from which you want to remove a Vault service key assignment.
- From the list of buckets, select the bucket name.
- 

Next to Encryption Key , select Unassign .
- 

In the Confirm dialog box, select OK to remove the key assignment from the bucket.
- 

Open a command prompt and run`oci os bucket update`to remove the Vault service master encryption key assigned to a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
-
