# Moving a Kafka Connect Configuration to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-connect-harness.htm
- Fetched: 2026-09-05 03:05 CDT

# Moving a Kafka Connect Configuration to a Different Compartment

Move a Kafka Connect configuration in the Streaming service to a different compartment.

To review requirements for working with Kafka Connect, see[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-connect-harness.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-connect-harness.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-connect-harness.htm#)
- 

- On the Kafka Connect configurations list page, find the Kafka Connect configuration that you want to work with. If you need help finding the list page or the Kafka Connect configuration, see[Listing Kafka Connect Configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-connect-harness.htm).
- From the Actions menu (three dots) for the configuration, select Move resource .
- In the Move resource dialog box, select the compartment that you want to move the Kafka Connect configuration to.
- Select Move resource .
- 

Use the[oci streaming admin connect-harness change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/connect-harness/change-compartment.html)command and required parameters to move a Kafka Connect configuration to a different compartment:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeConnectHarnessCompartment](https://docs.oracle.com/iaas/api/#/en/streaming/latest/ConnectHarness/ChangeConnectHarnessCompartment)
