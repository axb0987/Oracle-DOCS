# Updating a Kafka Connect Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-connect-harness.htm
- Fetched: 2026-09-05 03:06 CDT

# Updating a Kafka Connect Configuration

Update a Kafka Connect configuration in the Streaming service. You can update tags.

To review requirements for working with Kafka Connect, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-connect-harness.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-connect-harness.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-connect-harness.htm#)
- 

- On the Kafka Connect configurations list page, select the Kafka Connect configuration that you want to work with. If you need help finding the list page or the Kafka Connect configuration, see[Listing Kafka Connect Configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-connect-harness.htm).
- On the Kafka Connect configuration details page, select Tags .
- Add one or more tags to the Kafka Connect configuration.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Use the[oci streaming admin connect-harness update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/connect-harness/update.html)command and required parameters to update a Kafka Connect configuration:

```

```

For example:
```

```

Select`y`and press`Enter`. The Kafka Connect configuration is updated:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateConnectHarness](https://docs.oracle.com/iaas/api/#/en/streaming/latest/ConnectHarness/UpdateConnectHarness)
