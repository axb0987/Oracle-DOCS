# Using Individual Consumers
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm
- Fetched: 2026-09-05 03:06 CDT

# Using Individual Consumers

Consume messages from a stream using an individual consumer.

If you use individual consumers to consume messages from your streams instead of using[consumer groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm), you can't take advantage of many of the benefits of Streaming, such as service-managed coordination, horizontal scaling, and offset management. Your applications will need to handle these scenarios, and many more, programmatically.

For these reasons, we recommend[using consumer groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm)in a production environment, but it might be useful to use individual consumers for testing or proof-of-concept applications.

## Using Cursors

A cursor is a pointer to a location in a stream. The location could be a specific offset or time in a partition.

Before you start to consume messages, you need to indicate the point from which you want to start consumption. You can do this by[creating a cursor](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-cursor.htm).

There are five supported cursor types:
- `TRIM_HORIZON`- Start consuming from the oldest available message in the stream. Create a cursor at the`TRIM_HORIZON`to consume all messages in a stream.
- `AT_OFFSET`- Start consuming at a specified offset. The offset must be greater than or equal to the offset of the oldest message and less than or equal to the latest published offset.
- `AFTER_OFFSET`- Start consuming after the given offset. This cursor has the same restrictions as the`AT_OFFSET`cursor.
- `AT_TIME`- Start consuming from a given time. The timestamp of the returned message will be on or after the supplied time.
- `LATEST`- Start consuming messages that were published after you created the cursor.

When you create a cursor for an individual consumer, you need to specify the partition in the stream for the cursor to use. If your stream has more than one partition with messages, you need to create multiple cursors to read them.

After creating a cursor, you can start to[consume messages by getting them](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm).

As long as you keep consuming messages, you don't need to re-create a cursor. Create cursors outside of your loops to get messages.

## Getting Messages

After creating a cursor,[get (read) messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm), specifying that cursor to start consuming messages. The service responds with your messages and the`opc-next-cursor`header value. Use the returned header value in your next GetMessages call. The returned cursor is never null, but it expires in five minutes. If you stop consuming messages for longer than five minutes, you will need to re-create a cursor.

If you have more than one consumer reading from the same partition, they receive the same messages. Decide how your application processes these messages.

If there are no more unread messages in the partition, Streaming returns an empty list of messages.

GetMessages batch sizes are based on the average message size published to the stream. By default, the service returns as many messages as possible. You can use the`limit`parameter to specify any value up to 10,000, but consider your average message size to avoid exceeding throughput on the stream.

### Falling behind

To determine if your consumer is falling behind (you're producing faster than you're consuming), you can use the timestamp of the message. If the consumer is falling behind, consider spawning more consumers to take over some of the partitions from the first consumer. There's no way to recover if you're falling behind on a single partition.

Consider the following options:
- Create a new stream with more partitions.
- Use[consumer groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm).
- If the issue is caused by a hotspot, change the message key strategy.
- Reduce message processing time, or handle requests in parallel.

To find out how many messages remain to consume in a particular partition, use a cursor of type`LATEST`, get the offset of the next published message, and make the delta with the offset that you're currently consuming.

## Managing Offsets

Offsets indicate the location of a message within a partition. If your consumer restarts or you need to recover from a failure, you can use the offset to restart reading from the stream.
Tip  
  

[Consumer groups](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm)can manage offset commits automatically.

When you use individual consumers, your consumer application must manage processed offsets (see[Manually Committing an Offset](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm)). The consumer is responsible for storing which offsets it reached or stopped at, for each partition. When your consumer restarts, read the offset of the last message that you processed, and then create a cursor of type`AFTER_OFFSET`and specify the offset that you just got. We don't provide any guidance for storing the offset of the last message that you processed. You can use any method, such as another stream, a file on your machine, or Object Storage.
Note
