# Moving a Stream to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/moving-streams.htm
- Fetched: 2026-09-05 03:06 CDT

# Moving a Stream to a Different Compartment

Move a stream to a different compartment.

For instructions to move a stream to a different stream pool, see[Updating a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-streams.htm).

For stream pools, see[Moving a Stream Pool to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/moving-streams.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/moving-streams.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/moving-streams.htm#)
- 

- On the Streams list page, find the stream that you want to work with. If you need help finding the list page or the stream, see[Listing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/listing-streams.htm).
- From the Actions menu (three dots) for the stream, select Move resource .
- In the Move resource dialog box, select the compartment that you want to move the stream to.
- Select Move resource .
- 

Use the[oci streaming admin stream change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream/change-compartment.html)command and required parameters to move a stream to a different compartment:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeStreamCompartment](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Stream/ChangeStreamCompartment)operation to move a stream to a different compartment.

## Using OCI SDKs

For detailed SDK examples, see[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/developing.htm)
