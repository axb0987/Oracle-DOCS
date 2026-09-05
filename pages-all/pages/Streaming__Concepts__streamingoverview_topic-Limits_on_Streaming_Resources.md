# Limits on Streaming Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm
- Fetched: 2026-09-05 03:05 CDT

# Limits on Streaming Resources

Review limits on Streaming resources.

The Streaming service has the following limits:
- The maximum retention period for messages in a stream is seven days. The minimum retention period is 24 hours. All messages in a stream are deleted after the retention period passes, whether or not they have been read.
- The retention period for a stream can't be changed after creation of the stream.
- A tenancy has a default limit of 200 partitions (Monthly Universal Credits) or 50 partition (Pay-as-You-Go or Promo). If your throughput requires more partitions, you can[request more](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).
- The number of partitions for a stream can't be changed after creation of the stream.
- A single stream can support up to 50 consumer groups reading from the stream.
- Each partition can support:
- A total data write rate of 1 MB per second. There is no limit on the number of PUT requests, provided the limit of 1 MB per second per partition isn't exceeded.
- 5 GET requests per second per consumer group. Since a single stream can support up to 50 consumer groups, and a single partition in a stream can be read by at-most one consumer in a consumer group, a partition can support up to 250 GET requests per second (5 GET requests per second per consumer in all 50 consumer groups).
- The maximum size of a unique message that producers can publish to a stream is 1 MB.
- The maximum size of any single request is 1 MB. A request's size is the sum of its keys and messages after they've been decoded from Base64.

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm), see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

## Other Limits

The following information provides other limits that apply if you need to further customize certain streaming configurations. The default limits are listed for each configuration.

Configuration Requests per Second Description
`KafkaSaslHandshake`500 The first step in the authentication sequence that uses Simple Authentication and Security Layer (SASL) to authenticate Kafka producers and consumers.
`KafkaMetadata`500 Metadata describes a Kafka cluster (and is created) for KafkaConsumer and KafkaProducer.
`KafkaHeartbeat`5 Controls how often the KafkaConsumer poll() method sends a heartbeat to the group coordinator.
`KafkaOffsetFetch`10 Retrieves the offset value for one or more topic partitions of a Kafka consumer group.
`KafkaOffsetCommit`10 Indicates the position of the next message to be consumed within a partition by committing an offset value.
`ConsumerHeartbeat`5 Controls how often the KafkaConsumer poll() method sends a heartbeat to the group coordinator.
Stream Create 5 Create operation in streams.
Stream Get/List 5 Read operation in streams.
Stream Update 5 Update operation in streams.
Stream Delete 5 Delete operation in streams.
StreamPool Create 5 Create operation on a stream pool.
StreamPool Get/List 5 Read operation on a stream pool.
StreamPool Update 5 Update operation on a stream pool.
StreamPool Delete 5 Delete operation on a stream pool.
`CreateCursor`5 Creates a cursor. Cursors are used to consume a stream, starting from a specific point in the partition and going forward.
`GetGroup`5 Returns the current state of a consumer group.
`UpdateGroup`5 Forcefully changes the committed location of a group on a stream.
`ConsumerCommit`5 Commits processed offsets to the consumer group state.
`CreateGroupCursor`5 Creates a group-cursor for the specified stream. A cursor is used to consume a stream.
ConnectHarness Create 5 Create operation on a connect harness.
ConnectHarness Get/List 5 Read operation on a connect harness.
ConnectHarness Update 5 Update operation on a connect harness.
