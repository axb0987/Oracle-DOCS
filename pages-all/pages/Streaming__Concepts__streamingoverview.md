# Overview of Streaming
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm
- Fetched: 2026-09-05 03:05 CDT

# Overview of Streaming

The Oracle Cloud Infrastructure Streaming service provides a fully managed, scalable, and durable solution for ingesting and consuming high-volume data streams in real-time. Use Streaming for any use case in which data is produced and processed continually and sequentially in a publish-subscribe messaging model.

You can use Streaming for: Messaging Use Streaming to decouple the components of large systems. Producers and consumers can use Streaming as an asynchronous message bus and act independently and at their own pace. Metric and log ingestion Use Streaming as an alternative for traditional file-scraping approaches to help make critical operational data more quickly available for indexing, analysis, and visualization. Web or mobile activity data ingestion Use Streaming for capturing activity from websites or mobile apps, such as page views, searches, or other user actions. You can use this information for real-time monitoring and analytics, and in data warehousing systems for offline processing and reporting. Infrastructure and apps event processing Use Streaming as a unified entry point for cloud components to report their lifecycle events for audit, accounting, and related activities.

## Streaming Features

Streaming provides the following features: Fully managed Streaming is fully managed, from the underlying infrastructure to its provisioning, deployment, maintenance, security patching, and replication. Integration with Monitoring and default metrics make operations easy.

Oracle manages stream partitions and consumer groups can handle your message offsets. Durability and Availability Messages published to the Streaming service are synchronously replicated across three[availability domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)when available. In regions with a single availability domain, the data is replicated across multiple fault domains. This ensures that even the failure of an availability domain or fault domain does not result in data loss. The result is highly durable data.

Oracle Cloud Infrastructure provides a service-level agreement (SLA) for Streaming. Refer to the[Oracle Cloud Infrastructure Service Level Agreement page](https://cloud.oracle.com/iaas/sla)for details. Security

Streaming data is encrypted both at rest and in transit, ensuring message integrity. You can let Oracle manage encryption, or use the[Oracle Cloud Infrastructure Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)service to securely store and manage your own encryption keys if you need to meet specific compliance or security standards.

Integration with[Oracle Cloud Infrastructure Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm)(IAM) lets you control who and what services can access which keys and what they can do with those resources.

[Private endpoints](https://docs.oracle.com/iaas/Content/Network/Concepts/privateaccess.htm#private-endpoints)restrict access to a specified virtual cloud network (VCN) within your tenancy so that its streams cannot be accessed through the internet.

For more information, see[Security Best Practices for Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamsecurity.htm). Stream processing Streaming's integration with[Oracle Cloud Infrastructure Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)means that you can designate a stream as a data source, use[Oracle Cloud Infrastructure Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)to transform the stream's messages, and output the transformed messages to[Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)or any other supported Connector Hub target while maintaining Streaming's order guarantees. Kafka compatibility Streaming makes it possible to offload the setup, maintenance, and management of the infrastructure that hosting your own Apache Kafka cluster requires.

Streaming is compatible with[most Kafka APIs](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/kafkacompatibility.htm#kafka_apis), allowing you to use applications written for Kafka to send messages to and receive messages from the Streaming service without having to rewrite your code. See[Using Kafka APIs](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/kafkacompatibility_topic-Configuration.htm)for more information.

Streaming also takes advantage of the Kafka Connect ecosystem to interface directly with first-party and third-party products by using out-of-the-box Kafka source and sink connectors. See[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/kafkacompatibility_topic-Kafka_Connect.htm)for more information.

## How Streaming Works

Here's how Streaming works:

A producer publishes messages to a stream , which is an append-only log. These messages are distributed among Oracle-managed partitions for scalability.

Partitions allow you to distribute a stream by splitting messages across multiple nodes (or brokers). Each partition can be placed on a separate machine, allowing multiple consumers to read a stream in parallel.

A consumer reads messages from one or more partitions. Consumers can read from any partition regardless of where the partition is hosted. Each message within a stream is marked with an offset value, so a consumer can pick up where it left off if it is interrupted. Messages from a partition are guaranteed to be delivered in the same order they were produced.
Consumers can read messages explicitly by providing the partition and offset, or as a member of a consumer group , which coordinates the consumption of an entire stream by the members of the group.
Note  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:32094)to the Streaming service.

For more information, see:

- [Stream data to an autonomous database in real time](https://docs.oracle.com/en/solutions/streaming-data-to-an-adb/index.html#GUID-B4183462-0428-43A9-B15D-8E4B38F1ACE1)
- [Stream IoT data to an autonomous database using serverless functions](https://docs.oracle.com/en/solutions/iot-streaming-oci/index.html#GUID-BAE48036-286B-49CE-A6AA-5870CAD689D2)

## Streaming Concepts

The following concepts are essential to understanding and working with Streaming. stream A partitioned, append-only log of messages. stream pool

A grouping that you can use to organize and manage streams, including any shared Kafka or security settings. partition A section of a stream. Partitions allow you to distribute a stream by splitting messages across multiple nodes. This also allows multiple consumers to read from a stream in parallel. cursor

A pointer to a location in a stream. This location could be a pointer to a specific offset or time in a partition, or to a group's current location. message A Base64-encoded message that is published to a stream. Streaming is schema-agnostic and accepts any message format, including XML, JSON, CSV, and even compressed formats such as gzip. Producers and consumers should agree upon the message format. producer An entity that publishes messages to a stream. consumer An entity that reads messages from one or more streams. consumer group A set of instances which coordinate to consume messages from all partitions in a stream. At any given time, the messages from a specific partition can only be consumed by a single consumer in the group. instance A member of a consumer group. Instances are defined when a group cursor is created. Group membership is maintained through interaction; lack of interaction results in a timeout, removing the instance from the consumer group. key An identifier used to group related messages. offset The location of a message within a partition. Each message within the partition is identified by its offset. Consumers can read messages starting from any chosen offset. You can use the offset to restart reading from a stream if interrupted.

## Benefits of Streams
