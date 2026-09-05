# Partitioning a Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/partitioningastream.htm
- Fetched: 2026-09-05 03:05 CDT

# Partitioning a Stream

To take full advantage of the Streaming service's ability to operate at scale, configure the number of partitions in the stream.

Before creating a stream, consider the expected stream throughput, partition key strategy, and how your stream will be consumed. Most configuration values cannot be changed after the stream has been created. For example, after a stream is created, you can't change the message retention time or number of partitions.

## Partitions and Throughput

When you create a stream, you must specify how many partitions the stream has. The expected throughput of your application can help you determine the number of partitions for your stream.

Multiply the average message size by the maximum number of messages written per second to estimate your expected throughput. Because a single partition is limited to a 1 MB per second data write rate, and 5 GET requests per second per consumer group, a higher throughput requires more partitions to avoid throttling. Keep additional[Streaming limits](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm)in mind when making your design decisions.
Tip  
  

To help you manage application spikes, we recommend allocating partitions slightly higher than your maximum throughput.

## Publishing to Partitions

The content of the messages you intend to publish to a stream can also help you determine how many partitions your stream should have.

A message is published to a partition in the stream. If there is more than one partition, the partition where the message is published is calculated using the message's key.

For more information, see[Publishing Messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/publishing.htm).

### Key to partition mapping

Messages with the same key go to the same partition. Messages with different keys might go to different partitions or to the same partition. If you don't specify a key, Streaming recognizes the null key and generates a random key on the behalf of the user. If a user publishes the same message twice, it could go to different partitions, because a completely new key is generated. Don't expect all messages with a null key to go to the same partition.

By default, Streaming provides uniform and predictable distribution of messages to a stream's partitions. Streaming APIs don't let you specify exactly which partition data is published to, because this can introduce a risk of hotspotting a single partition if a user isn't aware of the nuances of Streaming. However, if you use[Kafka APIs](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/kafkacompatibility_topic-Configuration.htm)to interact with Streaming, you might do custom partitioning and explicitly map messages to partitions, although we don't recommend it.

### Effective partitioning keys

To ensure uniform distribution of messages, you need effective values for your message keys. To create an effective value, consider the selectivity and cardinality of your Streaming data.

Cardinality: Consider the total number of unique keys that could potentially be generated based on the specific use case. Higher key cardinality generally means better distribution.

Selectivity: Consider the number of messages with each key. Higher selectivity means more messages per key, which can lead to hotspots.

Always aim for high cardinality and low selectivity.

### Ordering

Messages with the same key are guaranteed to be stored in the order they're published, and delivered to consumers in the same order they were produced. Because messages with the same key go to the same partition, this guarantee only applies at the partition level.

## Partitions and Consumer Groups

If your stream will be consumed by one or more consumer groups, then factor that into your decision on the number of its partitions. Partition reads are balanced among the instances in a consumer group.

Consumer groups can only use a single instance at a time if the stream has only one partition. If your stream has multiple partitions, you can scale the number of instances up to the number of the partitions and have one instance in the group reading from one partition in the stream.

For more information, see[Using Consumer Groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/using_consumer_groups.htm)
