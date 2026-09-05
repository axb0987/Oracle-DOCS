# Sending a Heartbeat
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/send-heartbeat-consumer-group.htm
- Fetched: 2026-09-05 03:06 CDT

# Sending a Heartbeat

Send a heartbeat to avoid consumer group timeouts in the Streaming service. A consumer group is a set of instances that coordinate to consume messages from all partitions in a stream.
For more information about consumer groups, including the automatic rebalancing process, see[Using Consumer Groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/send-heartbeat-consumer-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/send-heartbeat-consumer-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/send-heartbeat-consumer-group.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci streaming stream group heartbeat](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/stream/group/heartbeat.html)command and required parameters to send a heartbeat:

```

```

Your first heartbeat request should use the value returned when you created a group cursor. Each subsequent request should use the`value`returned in the previous response.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ConsumerHeartbeat](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Group/ConsumerHeartbeat)
