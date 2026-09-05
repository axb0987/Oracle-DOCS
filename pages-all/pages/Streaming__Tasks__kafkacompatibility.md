# Using Streaming with Apache Kafka
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm
- Fetched: 2026-09-05 03:06 CDT

# Using Streaming with Apache Kafka

Use Apache Kafka with Oracle Cloud Infrastructure Streaming.

Oracle Cloud Infrastructure Streaming lets users of Apache Kafka offload the setup, maintenance, and infrastructure management that hosting your own Zookeeper and Kafka cluster requires.

Streaming is compatible with most Kafka APIs, allowing you to use applications written for Kafka to send messages to and receive messages from the Streaming service without having to rewrite your code. See[Using Kafka APIs](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Configuration.htm)for more information.

Streaming can also use the Kafka Connect ecosystem to interface directly with external sources such as databases, object stores, or any microservice on the Oracle Cloud. Kafka connectors can easily and automatically create, publish to, and deliver topics while taking advantage of the Streaming service's high throughput and durability. See[Using Kafka Connect](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility_topic-Kafka_Connect.htm)for more information.

Use cases for Streaming and Kafka include:
- 

Move data from Streaming to Autonomous AI Lakehouse through the JDBC Connector to perform advanced analytics and visualization.
- 

Use the Oracle GoldenGate connector for Big Data Service to build an event-driven application.
- 

Move data from Streaming to Oracle Object Storage through the HDFS/S3 Connector for long term storage, or to run Hadoop/Spark jobs.

## Kafka API Support

Streaming is fully upstream compatible with the latest versions of Kafka APIs. Streaming supports the following Kafka APIs:
- [Producer](https://kafka.apache.org/documentation/#producerapi)(v0.10.0 and later)
- [Consumer](https://kafka.apache.org/documentation/#consumerapi)(v0.10.0 and later)
- [Connect](https://kafka.apache.org/documentation/#connectapi)(v0.10.0.0 and later)
- [Admin](https://kafka.apache.org/documentation/#adminapi)(v0.10.1.0 and later)
- [Group Management](https://cwiki.apache.org/confluence/display/KAFKA/A+Guide+To+The+Kafka+Protocol)(v0.10.0 and later)

The following Kafka APIs and features are not yet implemented in the Streaming service:
- [Kafka Streams](https://kafka.apache.org/documentation/streams/)
- [Compaction](https://kafka.apache.org/081/documentation.html#compaction)
- [Transactions](https://www.confluent.io/blog/transactions-apache-kafka/)
- [Dynamic Partition Addition](https://docs.confluent.io/1.0/kafka/post-deployment.html)
- [Idempotent production](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/)

## Kafka Clients

While many Kafka clients are available, we recommend the clients that have been fully tested and certified to work with the Streaming service.

Streaming supports all versions of[apache-kafka-java](https://github.com/apache/kafka).

Streaming also supports the following Kafka clients on a best-effort basis:
- [librdkafka](https://github.com/edenhill/librdkafka)
- [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python)

## Requirements and Limitations

The implementation of the Kafka compatibility in Streaming results in the following configurations, limitations, and behaviors.

### Lossless Configuration

Streaming only supports lossless Kafka configurations. Data is replicated three ways. Messages from producers do not initiate an acknowledgment (ACK) from Streaming until at least two replicas are in sync.

### Unique Stream Names

If you have streams with the same names in a compartment, you can't use Kafka with Streaming until you delete the duplicated streams, unless the streams are in different[stream pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managing-stream-pools.htm). Two streams with the same name can exist in the same compartment only if the streams are in different stream pools.

Duplicate stream names otherwise manifest through an "authentication failed" error. If you do not want to delete your streams, contact the Streaming team so we can rename your streams without data loss.

### Load Balancing Connection Recycling
