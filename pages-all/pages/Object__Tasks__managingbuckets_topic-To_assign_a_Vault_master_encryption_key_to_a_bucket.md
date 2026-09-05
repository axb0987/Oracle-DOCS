# Assigning a Key to an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Assigning a Key to an Object Storage Bucket

Assign a Vault master encryption key to an Object Storage bucket.
You can encrypt the data encryption keys that encrypt the objects in a bucket by using your own Vault master encryption key. By default, buckets are encrypted with keys managed by Oracle. For more information, see[Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm)and[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
Important  
  
Buckets in a security zone can't use the default encryption key managed by Oracle. You must use your own Vault master encryption key.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, find Encryption key . and select Assign .
The Assign master encryption key panel opens.
- Enter the following information:

- Enable bucket key : Enable this option to use the Bucket Key with SSE-KMS. We recommend this setting when using SSE-KMS key to reduce calls from Object Storage to KMS, which lowers PUT and GET latency, and decreases the likelihood of KMS throttling.
- The Vault compartment and vault that contain the master encryption key you want to use. The current compartment is displayed by default.
- The master encryption key compartment and master encryption key. The current compartment is displayed by default.
- Select Assign or Edit .
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to assign a Vault key to a bucket. We recommended that you enable Bucket Key with SSE-KMS because this setting reduces calls from Object Storage to KMS, which lowers PUT and GET latency, and decreases the likelihood of KMS throttling.

```

```

For example:
```

```

If you're updating the key, run the same[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command with the updated`kms_key_id`value.

See[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for more details.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
-
