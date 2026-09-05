# Updating a Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-streams.htm
- Fetched: 2026-09-05 03:06 CDT

# Updating a Stream

Move a stream to a different stream pool, or update its tags.

When you update a stream, you can also update its tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

For instructions to move a stream to a different compartment, see[Moving a Stream to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/moving-streams.htm).

For stream pools, see[Updating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-streams.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-streams.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-streams.htm#)
- 

- On the Streams list page, select the stream that you want to work with. If you need help finding the list page or the stream, see[Listing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/listing-streams.htm).
- To move the stream to a different stream pool:
- Select Move next to the current Stream pool value.
- In the Move stream panel, select the compartment and stream pool that you want to move the stream to, and then select Move stream .
- To add one or more tags to the stream, select Tags .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Use the[oci streaming admin stream update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream/update.html)command and required parameters to update a stream:

```

```

Example for moving the stream to a different stream pool:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateStream](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Stream/UpdateStream)
