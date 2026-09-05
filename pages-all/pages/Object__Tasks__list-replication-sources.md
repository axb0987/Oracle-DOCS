# Listing Replication Sources for an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm
- Fetched: 2026-09-05 02:50 CDT

# Listing Replication Sources for an Object Storage Bucket

View a list of replication sources for an Object Storage replication destination bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm#)
- 

This task can't be performed using the OCI Console.
- 

Use the[oci os replication list-replication-sources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/list-replication-sources.html)command and required parameters to list the sources of a replication policy for an Object Storage replication destination bucket:

```

```

If you're replicating to a destination bucket in a different region, include the`region`parameter and the region identifier. For example:

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListReplicationSources](https://docs.oracle.com/iaas/api/#23/en/objectstorage/latest/Replication/ListReplicationSources)
