# Creating a Kafka Connect Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-connect-harness.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Kafka Connect Configuration

Create a Kafka Connect configuration in the Streaming service.

To review requirements for working with Kafka Connect, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-connect-harness.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-connect-harness.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-connect-harness.htm#)
- 

- On the Kafka Connect configurations list page, select Create Kafka Connect configuration . If you need help finding the list page, see[Listing Kafka Connect Configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-connect-harness.htm).
The Create Kafka Connect configuration panel opens.
- Enter a name for the configuration. Avoid entering confidential information.
- Select a compartment for the configuration.
- (Optional) In the Tags section, add one or more tags to the Kafka Connect configuration.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
The details page for the new Kafka Connect configuration opens. A read-only text box labeled Kafka Connect storage topics lists the connector configuration.
- Select Copy to copy the connector configuration so that you can paste it into the`connect-distributed.properties`file for your Kafka connector.
For more information, see[the official Kafka Connect documentation](https://docs.confluent.io/current/connect/index.html).
- 

Use the[oci streaming admin connect-harness create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/connect-harness/create.html)command and required parameters to create a Kafka Connect configuration:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateConnectHarness](https://docs.oracle.com/iaas/api/#/en/streaming/latest/ConnectHarness/CreateConnectHarness)operation to create a Kafka Connect configuration.

## Using the SDK for Java

The following code example shows how to create a Kafka Connect harness using the OCI SDK for Java:

```

```

To use Kafka Connect with Streaming, you need a Kafka Connect configuration, or Kafka Connect harness . You can retrieve the OCID for a harness when you[create a new harness](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-connect-harness.htm)or use an existing one. For more information, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm)
