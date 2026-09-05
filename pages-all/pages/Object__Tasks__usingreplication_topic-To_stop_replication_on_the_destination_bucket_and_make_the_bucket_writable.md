# Stopping Replication to the Object Storage Destination Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm
- Fetched: 2026-09-05 02:52 CDT

# Stopping Replication to the Object Storage Destination Bucket

Stop replication to the Object Storage destination bucket and make the bucket writable.
Note  
  
If you stop replication, the policy is removed from the destination bucket and can't be recovered. The bucket reverts to a standard read/write bucket and is no longer a replication target.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm#)
- 

- On the Buckets list page, select the Object Storage destination bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
If your replication destination bucket is on a different compartment than your source bucket, you must switch over to that compartment.
- On the details page of the destination bucket, select Policies and find the Replication policy (Destination) section.
The replication policy for the selected bucket is displayed in a table.
- Select Stop replication .
- When prompted, confirm stopping the replication.
The source bucket's replication policy no longer appears in the Replication policy list no longer has an entry and the (Destination) indicator no longer appears in the Replication policy section heading. The bucket reverts to being read/write.
- 

Use the[oci os replication make-bucket-writable](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/make-bucket-writable.html)command and required parameters to stop replication to the Object Storage destination bucket and make the bucket writable.

```

```

If you're replicating to a destination bucket in a different region, include the`region`parameter and the region identifier. For example:
```

```

If the command is successful, you're returned to the prompt.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[MakeBucketWritable](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/MakeBucketWritable)
