# Developer Guide to Streaming
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm
- Fetched: 2026-09-05 03:05 CDT

# Developer Guide to Streaming

Use OCI SDKs to interact with Streaming without creating a framework.

The OCI SDKs let you manage[manage streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managingstreams.htm),[manage stream pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managing-stream-pools.htm), and[manage Kafka Connect configurations](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm), and[publish](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishing.htm)and[consume](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/consuming.htm)messages. See the[Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview.htm)for key concepts and more information.

This section includes the following topics to help you get started quickly with Streaming and the OCI SDK of your choice:
- [SDK for Java Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-java.htm)
- [SDK for Python Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-python.htm)
- [SDK for JavaScript Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-javascript.htm)
- [SDK for TypeScript Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-typescript.htm)
- [SDK for .NET Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-dotnet.htm)
- [SDK for Go Streaming Quickstart](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/streaming-quickstart-oci-sdk-for-go.htm)

For more information about using the OCI SDKs, see the[SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Because Oracle Cloud Infrastructure Streaming is compatible with most Kafka APIs, you can use applications written for Kafka to send messages to and receive messages from the Streaming service. See[Developing with Kafka and Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing-kafka.htm)for more information.

## Streaming Clients

The SDKs encapsulate the Streaming service in two clients: the`StreamAdminClient`and the`StreamClient`.

### StreamAdminClient

The`StreamAdminClient`incorporates the control plane operations of Streaming. You can use it to create, delete, update, modify, and list streams.

To instantiate the`StreamAdminClient`object:

```

```

### StreamClient

The`StreamClient`is used to publish and consume messages.

To instantiate a`StreamClient`object:

```

```
