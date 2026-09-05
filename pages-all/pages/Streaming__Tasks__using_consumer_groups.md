# Using Consumer Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm
- Fetched: 2026-09-05 03:06 CDT

# Using Consumer Groups

Consume messages from a stream using consumer groups.

Consumers can be configured to consume messages as part of a group. In a production environment with multiple partitions, using a consumer group is our recommended method of consuming Streaming messages.

Each stream partition is assigned to a member of a consumer group. An individual member of a consumer group is called an instance . Each instance in a consumer group receives messages from one or more partitions, unless there are more instances than partitions. Instances in excess of the partition count for the stream don't receive messages.

Consumer groups handle the coordination that's required for multiple consumers to share the consumption of a stream. A consumer group automatically:
- Assigns one or more partitions to an instance
- Tracks the messages received by the group and manages commits
- Requests the proper partitions and offsets on behalf of each instance
- Balances the group as instances join or leave

Up to 50 consumer groups can read from a single stream. Each consumer group receives all messages in the stream at least once.

Consumer groups are ephemeral. They disappear when they're not used for the retention period of the stream.

## Creating a Consumer Group

A consumer group is created on the first[CreateGroupCursor](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Cursor/CreateGroupCursor)request (see[Creating a Group Cursor](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-group-cursor.htm)). Group cursors define a group name/instance name pair. When you create your group cursor, provide the ID of the stream, a group name, an instance name, and one of the following supported cursor types:
- `TRIM_HORIZON`- The group starts consuming from the oldest available message in the stream.
- `AT_TIME`- The group starts consuming from a specific time. The timestamp of the returned message is on or after the supplied time.
- `LATEST`- The group starts consuming messages that were published after you created the cursor.

Group cursor types are ignored on[CreateGroupCursor](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Cursor/CreateGroupCursor)calls that include the name of an existing group. That group's[committed offsets](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm#consuming_as_a_group_topic-consuming_as_a_group__offsets_and_commits)are used instead of the provided cursor type.

Streaming uses the instance name to identify members of the group when managing offsets. Use unique instance names for each instance of the consumer group.

If you want the Streaming service to handle[committing offsets](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm#consuming_as_a_group_topic-consuming_as_a_group__offsets_and_commits), then leave the group cursor's`commitOnGet`value set to`true`. We recommend using this method to reduce application complexity so that your application doesn't have to handle commits.

## Consuming as a Group

After your instances join the consumer group, they can read messages from the stream using[GetMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/GetMessages)(see[Creating a Group Cursor](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-group-cursor.htm)). Each GetMessages call returns the cursor to use in the next GetMessages call as the`opc-next-cursor`header value. The returned cursor is never null, but it expires in five minutes. As long as you keep consuming, you don't need to re-create a cursor.

When Streaming receives a request for messages from an instance, the service:
- Checks to see whether a group[rebalance](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm#consuming_as_a_group_topic-consuming_as_a_group__balancing_and_rebalancing)is necessary
- [Commits the offset(s)](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm#consuming_as_a_group_topic-consuming_as_a_group__offsets_and_commits)from that instance's previous request, if any
- Responds with the messages defined by the request's cursor

[GetMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/GetMessages)batch sizes are based on the average message size published to that stream. By default, the service returns as many messages as possible. You can use the`limit`parameter to specify any value up to 10,000, but consider your average message size to avoid exceeding throughput on the stream or timeouts.

If there are no more unread messages in the partition, Streaming returns an empty list of messages.

Because consumer groups remove instances that have stopped consuming messages for more than 30 seconds, request fewer messages to avoid timeouts, or extend the timeout using[ConsumerHeartbeat](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Group/ConsumerHeartbeat)(see[Sending a Heartbeat](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/send-heartbeat-consumer-group.htm)).

A partition can't be assigned to multiple instances within the same consumer group. If you have more instances than partitions, the unassigned instances can send GetMesages requests, but they don't receive any messages. They remain otherwise idle until the consumer group needs to replace an instance, such as when an existing member of the group doesn't act within the timeout period.

If you need to manually update the group's position, you can use[UpdateGroup](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Group/UpdateGroup)(see[Updating a Consumer Group](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-consumer-group.htm)) to reset the location of all consumers in the group to the specified location in the stream.

### Offsets and Commits

Offsets indicate the location of a message within a partition. If a consumer restarts or you need to recover from a failure, you can use the offset to restart reading from the stream.

When you use a consumer group, Streaming handles offsets automatically. The default behavior of`commitOnGet=true`means that offsets from the previous request are committed. For example:

For consumer A :
- A calls[GetMessages](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Message/GetMessages)and receives messages from an arbitrary partition, with offsets of 1–100.
- A processes all 100 messages successfully.
- A calls GetMessages, and the Streaming service commits offset 100 and returns messages with offsets 101–200.
- A processes 15 messages, and then goes offline unexpectedly (for more than 30 seconds).

A new consumer B :
- B calls GetMessages, and the Streaming service uses the latest committed offset and returns messages with offsets 101–200.
- B continues the message loop.

In this example, a portion (15) of the messages were processed at least once, which means that they could have been processed more than once, but no data is lost.

Streaming provides "at-least-once" semantics for consumer groups. Consider when offsets are committed in a message loop. If a consumer goes offline before committing a batch of messages, that batch might be given to another consumer. When a partition is given to another consumer, the consumer uses the latest committed offset to start consumption. The consumer doesn't get messages before the committed offset. We recommend that consumer applications take care of duplicates.
Note  
  
Message offsets aren't dense. Offsets are monotonically increasing numbers. They don't decrease, and sometimes they increase by more than one. For example, if you publish two messages to the same partition, the first message could have an offset of 42 and the second message could have an offset of 45 (offsets 43 and 44 being non-existent).

To override the default offset behavior and implement a custom offset commit mechanism, set`commitOnGet`to`false`when creating the group cursor. You can use[ConsumerCommit](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Group/ConsumerCommit)(see[Manually Committing an Offset](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm)) to commit messages without reading more messages. ConsumerCommit returns a cursor for you to use in your next request.
Caution  
  
Writing custom commit logic is complicated and full of race conditions and considerations. Many cases exist in which some internal state is changed, and the client is required to handle the situation.

### Balancing and Rebalancing

Streaming considers the number of partitions in the stream and the number of instances in the consumer group when assessing balance. Group balancing is automatic. Each consumer is assigned to one or more partitions based on the following calculation:

( n Partitions / n Consumers ) ± 1

For example, if there are eight partitions in the stream and four consumers in the group, each consumer is assigned to two partitions. If there are 10 partitions in the stream and four consumers in the group, two consumers are assigned to two partitions, and two consumers are assigned to three partitions.

As instances join or leave a consumer group and requests are made for messages, partition assignments are reassessed. If the stream has at least one partition more than the number of current instances in the group, and a new instance joins, partitions are reassigned to all instances, including the new one. If an instance in the group stops consuming messages for more than 30 seconds, or fails to send a[ConsumerHeartbeat](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Group/ConsumerHeartbeat)within 30 seconds, that instance is removed from the consumer group and its partition is reassigned, if possible, to another instance.

These events are called rebalancing . The instances in the group aren't aware of the rebalancing process, but the group has coordinated to own a mutually exclusive set of partitions in the stream.

At the end of a successful rebalance operation for a consumer group, every partition within the stream is owned by an instance within the group.
