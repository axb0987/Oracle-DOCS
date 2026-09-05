# Removing a Vault Key from an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Removing a Vault Key from an Object Storage Bucket

Remove a Vault master encryption key from an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, find Encryption key .
- From the Actions menu (three dots) , select Unassign key .
- When prompted, confirm the unassignment.
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to remove a Vault key to a bucket.

```

```

where the`kms-key-id`parameter has the value`""`.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
-
