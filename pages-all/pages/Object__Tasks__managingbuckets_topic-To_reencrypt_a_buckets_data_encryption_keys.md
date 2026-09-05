# Re-encrypting an Object Storage Bucket's Data Encryption Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm
- Fetched: 2026-09-05 02:51 CDT

# Re-encrypting an Object Storage Bucket's Data Encryption Keys

Re-encrypt the unique data encryption key that encrypts each object written to an Object Storagebucket by using the most recent version of the master encryption key.

See[Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm)for more information.

## Encrypting the Bucket Key Only and Skipping the Re-Encryption of the Object Data Encryption Key

Use the option to only re-encrypt the bucket key when the bucket key is already enabled for the bucket. This option re-encrypts the bucket key for the bucket and skips re-encrypting the data encryption keys for objects. To migrate existing objects to the bucket key wrapping after enabling bucket key, run the bucket re-encryption without this option.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
The Buckets list page opens. All buckets in the selected compartment are displayed in a table.
- From the Actions menu , select Re-encrypt .
- Select Re-encrypt bucket keys for buckets using bucket level keys
- Select Re-encrypt bucket keys and objects for buckets using both bucket and object level encryption
- 

Use the[oci os bucket reencrypt](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/reencrypt.html)command and required parameters to re-encrypt the unique data encryption key that encrypts each object written to the bucket by using the most recent version of the master encryption key assigned to the bucket.

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ReencryptBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ReencryptBucket)operation to re-encrypt the unique data encryption key that encrypts each object written to the bucket by using the most recent version of the master encryption key assigned to the bucket.

When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```

```
