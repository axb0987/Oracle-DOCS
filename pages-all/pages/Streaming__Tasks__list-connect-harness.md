# Listing Kafka Connect Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-connect-harness.htm
- Fetched: 2026-09-05 03:06 CDT

# Listing Kafka Connect Configurations

List Kafka Connect configurations in the Streaming service.

To review requirements for working with Kafka Connect, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-connect-harness.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-connect-harness.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-connect-harness.htm#)
- 

- Open the navigation menu and select Analytics &amp; AI . Under Messaging , select Streaming .
- Under Analytics &amp; AI , select Kafka Connect Configurations .
The Kafka Connect configurations list page opens. All configurations in the selected compartment are displayed in a table.
- To view the Kafka Connect configurations in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

Use the[oci streaming admin connect-harness list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/connect-harness/list.html)command and required parameters to list Kafka Connect configurations:

```

```

For example:
```

```

By default, getting a list of Kafka Connect configurations returns up to the first 10 configurations in the compartment.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListConnectHarnesses](https://docs.oracle.com/iaas/api/#/en/streaming/latest/ConnectHarnessSummary/ListConnectHarnesses)operation to list Kafka Connect configurations.

## Using the SDK for Java

The following code example shows how to list Kafka Connect harnesses using the OCI SDK for Java:

```

```

To use Kafka Connect with Streaming, you need a Kafka Connect configuration, or Kafka Connect harness . You can retrieve the OCID for a harness when you[create a new harness](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-connect-harness.htm)or use an existing one. For more information, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm)
