# Getting a Replication Policy's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm
- Fetched: 2026-09-05 02:52 CDT

# Getting a Replication Policy's Details

View the details of the replication policy for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Replication policy (Source) section.
The replication policy for the selected bucket is displayed in a table.

The Replication policy list displays the details of the replication policy, including its destination region, destination bucket, and the time of the last replication.
- 

Use the[oci os replication get-replication-policy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/get-replication-policy.html)command and required parameters to get the details of a replication policy for an Object Storage bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetReplicationPolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/GetReplicationPolicy)
