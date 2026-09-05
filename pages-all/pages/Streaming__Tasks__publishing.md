# Publishing Messages
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishing.htm
- Fetched: 2026-09-05 03:06 CDT

# Publishing Messages

Emit, or publish, messages to a stream in the Streaming service.

Once a stream is created and active, you can publish messages. See[Publishing a Test Message to a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm)or the[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm)for details on publishing, and familiarize yourself with[partitioning](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishing.htm#partitions),[large messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishing.htm#handling_large_messages), and[batching and throttling](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishing.htm#publishing_topic_batching_and_throttling)for additional context.
Tip  
  
You can also use[Oracle Cloud Infrastructure Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)to publish data to a stream from supported source services, such as Logging.

While you can use the Console to[publish test messages to a stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/publishingmessages.htm#console), you should use the CLI, API, or an SDK to populate your stream.

To publish messages using the Oracle Cloud Infrastructure (OCI) SDKs, see the[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm).

If you take advantage of Streaming's Kafka compatibility, see[Developing with Kafka and Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing-kafka.htm).

You can also use[Oracle Cloud Infrastructure Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)to publish data to a stream from supported source services, such as Logging.

## Messages and Partitions

Messages are published to a single partition in a stream. If there is more than one partition in the stream, the decision of which partition to publish the message to depends on whether your producers are using the Streaming API and[PutMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/PutMessages), or taking advantage of the Kafka compatibility in Streaming and[using the Kafka API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm).

If your producers are using the Streaming API, partitioning is handled server-side by the Streaming service. If your producers are using the Kafka API, partitioning is handled client-side by Kafka.

### Server-side Partitioning

The partition where a message is published is calculated using the message's key. If the key is null, the partition is calculated using a random 16-byte value. You can't specify which partition a key uses.

Passing a null key puts the message in a random partition. If a user publishes the same message twice, it could go to different partitions, because a completely new key is generated. Don't expect all messages with a null key to go to the same partition. To ensure that messages with the same value go to the same partition, use the same key for those messages.

For more information, see[Publishing to Partitions](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/partitioningastream.htm#publishing_to_partitions).

## Handling Large Messages

If your messages are larger than the 1 MB limit, you can either use chunking or send the message by using Oracle Cloud Infrastructure Object Storage.
- Chunking : You can split large payloads into multiple, smaller chunks that the Streaming service can accept. The chunks are stored in the service in the same way that ordinary (non-chunked) messages are stored. The only difference is that the consumer must keep the chunks and combine them into the message when all the chunks have been collected. The chunks in the partition can be interwoven with ordinary messages.
- 

Object Storage : A large payload is placed in Object Storage and only the pointer to that data is transferred. The receiver recognizes this type of pointer payload, transparently reads the data from Object Storage, and provides it to the end user.

## Batching and Throttling

We recommend batching messages to avoid throttling and enable better throughput. The size of a batch of messages shouldn't exceed 1 MB. If this limit is exceeded, the message fails to validate.

The throttling mechanism for[PutMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/PutMessages)is activated when data write rates exceed 1 MB per second per partition. There is no limitation on the number of writes to a stream, as long as you're under the 1 MB per second per partition throughput.

See[Limits on Streaming Resources](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm)for more information.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let streaming admins manage streaming resources](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#streaming-manage-streams)lets the specified group do everything with streaming and related Streaming service resources.

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). For more information about writing policies for the Streaming service, see[Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/streamingpolicyreference.htm)in the IAM policy reference and[Accessing Streaming Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/accessing-streaming-resources-across-tenancies.htm)
