# Editing a key to an Object Storage bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Object_Storage_bucket.htm
- Fetched: 2026-09-05 02:31 CDT

# Editing a key to an Object Storage bucket

Editing or modifying a key to an existing Object Storage bucket using the OCI Console and CLI interface.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Object_Storage_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Object_Storage_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Object_Storage_bucket.htm#)
- 

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Under List Scope , in the Compartment list, select the compartment that contains the bucket that you want to encrypt with a Vault service master encryption key.
- 

From the list of buckets, select the bucket name.
- 

Do one of the following:
- If the bucket already has a key assigned to it, next to Encryption Key , click Edit to assign a different key.
- If the bucket does not already have a key assigned to it, next to Encryption Key , click Assign .
- 

Select the vault compartment, vault, key compartment, and key.
- 

When you are finished, select Assign or Update , as appropriate.
- 

This topic describes how to update the key assigned to an Object Storage bucket using the Command Line Interface (CLI)

Open a command prompt and run`oci os bucket update`to update the Vault service master encryption key assigned to a bucket:
```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
-
