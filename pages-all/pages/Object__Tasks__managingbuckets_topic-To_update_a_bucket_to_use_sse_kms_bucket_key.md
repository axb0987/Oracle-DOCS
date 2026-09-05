# Updating an Object Storage Bucket to Use an SSE-KMS Bucket Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_a_bucket_to_use_sse_kms_bucket_key.htm
- Fetched: 2026-09-05 02:51 CDT

# Updating an Object Storage Bucket to Use an SSE-KMS Bucket Key

Update a bucket to use the bucket key. By default, the bucket key is disabled.
Note  
  

When you enable SSE-KMS Bucket Key, only new objects written after enabling Use Bucket Key . Existing objects remain encrypted under their previous wrapping. To migrate existing objects, run bucket re-encryption to re-encrypt the data encryption keys associated with those objects.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_a_bucket_to_use_sse_kms_bucket_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_a_bucket_to_use_sse_kms_bucket_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_a_bucket_to_use_sse_kms_bucket_key.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
The Buckets list page opens. All buckets in the selected compartment are displayed in a table.
- From the Actions menu (three dots) next to the relevant bucket, enable or disable Use Bucket Key .
- 

Use the[`oci os bucket update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command to enable the bucket key. For full command details, see[`oci os bucket update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html).

```

```

For example:
```

```

Note  
  

If the bucket already has a KMS key associated, don't pass the`--kms-key-id`option again unless you're changing the key. Instead, just enable the bucket key.
- 

Run the[UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket)operation.

When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```

```
