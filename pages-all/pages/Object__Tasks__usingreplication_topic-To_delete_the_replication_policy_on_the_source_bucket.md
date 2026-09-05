# Deleting the Replication Policy from an Object Storage Source Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm
- Fetched: 2026-09-05 02:52 CDT

# Deleting the Replication Policy from an Object Storage Source Bucket

Delete the replication policy for an Object Storage bucket.

For information about how replication works, see[Using Replication](https://docs.oracle.com/iaas/Content/Object/Tasks/usingreplication.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Replication policy (Source) section.
The replication policy for the selected bucket is displayed in a table.
- From the Actions menu for the replication policy, select Delete policy .
- When prompted, confirm the deletion.
The Replication policy (Source) list no longer has an entry and the (Source) indicator no longer appears in the bucket's Replication policy section header. The bucket reverts to being read/write.
- 

Use the[oci os replication delete-replication-policy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/delete-replication-policy.html)command and required parameters to delete the replication policy associated with an Object Storage source bucket.

```

```

For example:
```

```

If the command is successful, you're returned to the prompt.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteReplicationPolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/DeleteReplicationPolicy)
