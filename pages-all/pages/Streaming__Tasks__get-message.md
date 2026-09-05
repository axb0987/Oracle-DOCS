# Getting (Reading) Messages
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm
- Fetched: 2026-09-05 03:05 CDT

# Getting (Reading) Messages

Using a specified cursor, get (or read) messages from a stream in the Streaming service. A message is a Base64-encoded message that's published to a stream.
For information about consumer groups and individual consumers for getting messages, see[Using Consumer Groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm)and[Using Individual Consumers](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci streaming stream message get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/stream/message/get.html)command and required parameters to get messages from a stream:

```

```

Your first request to get messages should use the value returned when you created a cursor. Each subsequent request should use the`opc-next-cursor`value returned in the previous response.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/GetMessages)
