# Deleting a Kafka Connect Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-connect-harness.htm
- Fetched: 2026-09-05 03:05 CDT

# Deleting a Kafka Connect Configuration

Delete a Kafka Connect configuration in the Streaming service.
Caution  
  
Kafka Connect configurations are deleted immediately. You can't recover a deleted configuration.

To review requirements for working with Kafka Connect, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-connect-harness.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-connect-harness.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-connect-harness.htm#)
- 

- On the Kafka Connect configurations list page, find the Kafka Connect configuration that you want to work with. If you need help finding the list page or the Kafka Connect configuration, see[Listing Kafka Connect Configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-connect-harness.htm).
- From the Actions menu (three dots) for the configuration, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci streaming admin connect-harness delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/connect-harness/delete.html)command and required parameters to delete a Kafka Connect configuration:

```

```

For example:
```

```

Select`y`and press`Enter`. The Kafka Connect configuration is deleted with no further prompting.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteConnectHarness](https://docs.oracle.com/iaas/api/#/en/streaming/latest/ConnectHarness/DeleteConnectHarness)
