# Manually Committing an Offset
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm
- Fetched: 2026-09-05 03:05 CDT

# Manually Committing an Offset

Commit offsets associated with the specified cursor in the Streaming service. An offset is the location of a message within a partition. Each message within the partition is identified by its offset. Consumers can read messages starting from any chosen offset. You can use the offset to restart reading from a stream if interrupted. Manually committing an offset extends the timeout on each of the affected partitions and returns an updated cursor.

Note  
  
[Consumer groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm)remove the need for manual commits of offsets. For information about how consumer groups use commits and offsets, see[Offsets and Commits](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm#consuming_as_a_group_topic-consuming_as_a_group__offsets_and_commits).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci streaming stream group commit](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/stream/group/commit.html)command and required parameters to commit an offset:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ConsumerCommit](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Group/ConsumerCommit)
