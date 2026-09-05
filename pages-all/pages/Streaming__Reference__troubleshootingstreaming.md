# Troubleshooting Streaming
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/troubleshootingstreaming.htm
- Fetched: 2026-09-05 03:05 CDT

# Troubleshooting Streaming

Learn how to troubleshoot common issues with Streaming.

This topic covers various issues related to Oracle Cloud Infrastructure Streaming and how you can address them. Details about common API errors that all services return are detailed in[API Errors](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm).

- [Troubleshooting Access and Permissions](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/troubleshootingstreaming.htm#troubleshooting_access_issues)
- [Troubleshooting Limits and Throttling](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/troubleshootingstreaming.htm#troubleshooting_limit_issues)
- [Troubleshooting Production and Consumption](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/troubleshootingstreaming.htm#troubleshooting_production_and_consumption)
- [Troubleshooting Streaming and Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/troubleshootingstreaming.htm#troubleshooting_streaming_and_kafka)

## Troubleshooting Access and Permissions

### Request returns a "Processing exception while communicating" message and a -1 error

When you use the Streaming client to send a request, you might see the following error message:
```

```

This error is related to the client or the client's environment. The Streaming service doesn't send it, which means that the request never made it to the service.

Ensure that you can reach your Streaming endpoint. You can use telnet to test connectivity to our public endpoints. Streaming currently uses ports 443 and 9092. Port 443 is used by the Streaming API and the Oracle Cloud Infrastructure SDKs. Port 9092 is used by the Kafka protocol. Your telnet test should specify the appropriate port for your use case.

For example:

```

```

```

```

A successful connection to the Streaming service returns a`Connected to cell-1.streaming.region.oci.oraclecloud.com.`message.

If telnet returns an`Unable to connect to remote host`message, investigate your network for possible blocking issues, such as a firewall policy or network security group rules.

### Request returns a NotAuthorizedOrNotFound message and a 404 error

When you send a request to Streaming, you might see an error message similar to the following:
```

```

A 404 error usually means that the needed resource isn't found or that you don't have access to it. An example is when the stream-push policy is missing, or the stream has been deleted or is not accessible. Ensure that all the permissions are correctly set.

### Request returns a "Not Found" message and a 404 error

When you send a request to Streaming, you might see an error message similar to the following:
```

```

This error indicates a permission-related issue. Ensure that all the permissions are correctly set.

### Request returns a "The following tag namespaces/keys are not authorized or not found" message

This error suggests that there is a tag on the stream that your user is not authorized to use. Remove the tag or authorize the user. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)for more information.

### Request returns a "bad handshake" message and a 104 error

When you send a request to Streaming, you might see an error message similar to the following:
```

```

This error typically means that your system doesn't have the CA that the certificates were signed by. You may need to install the ca-certificates package on your host or pull the CA certificate from the target endpoint and import it into your system trust store by using`update-ca-trust`command.

## Troubleshooting Limits and Throttling

[Limits on Streaming Resources](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm)describes the service and resource limits that might result in the following scenarios.

### Partial failures

Streaming supports partial failures caused by throttling, per partition. When a partial failure occurs, the service returns a`200`status code and indicates the failure in the response payload.

If an entire request is throttled, Streaming returns a[`429`status code](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/troubleshootingstreaming.htm#troubleshooting_limit_issues__429_too_many_requests).

### Request returns a "Too many requests message" and a 429 error

When you send a request to Streaming, you might see an error message that includes the following:
```

```

This error is caused by the throttling mechanism in the service. It indicates that too many requests per second per partition are being received.

If this error occurs on the producer side, ensure that the total data write rate of 1 MB per second per partition is not exceeded by:
- Lowering the amount of requests per second.
- Decreasing message size by batching.

If this error occurs on the consumer side, ensure that:
- The cursor uses[`commitOnGet(true)`](https://docs.oracle.com/iaas/tools/java/latest/com/oracle/bmc/streaming/model/CreateGroupCursorDetails.Builder.html#commitOnGet-java.lang.Boolean-).
- You reduce the number of requests, keeping in mind that the maximum data read rate is 5 GET requests per second per partition per consumer group.
- The`limit`is set for each GET request.

### Request returns a "Request size is limited to 1 MiB" message and a 400 error

When you send a request to Streaming, you might see an error message similar to the following:
```

```

This error occurs because the`PutMessages`call sent to the service is too large. The size must be less than or equal to 1 MB.

### Stream creation fails with a "You exceed the number of allowed partitions" message

This error occurs when you try to create more partitions than your tenancy is allowed. You can[request an increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).

## Troubleshooting Production and Consumption

### Messages don't appear in the Console after publishing them to a stream

You must select Refresh to show the first 100 messages. For more information, see[Showing Recent Messages in a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/show-recent-messages.htm).

Because streams using[private endpoints](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Concepts/streamsecurity.htm#private_endpoints)aren't accessible from the internet, their messages don't show in the Console.

### Consumers receive a "The cursor is outside the retention period and is now invalid" message and a 400 error

When requesting messages from a stream, a consumer might see an error message such as the following:
```

```

This error means that the offsets stored for one or more of your partitions has fallen behind the trim horizon. Some data loss has occurred, and the data that was produced to the stream is no longer available for consumption. Data that's outside the retention period can't be recovered. At this point, the administrator must decide the best course of action for the use case.

This error can happen if you're not committing offsets regularly, or if your consumer falls behind constantly. For more information, see[Getting Messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/using_a_single_consumer.htm#consuming_topic-Getting_Messages).

A manual call to the`UpdateGroup`method is required to reset the cursor for the instances within a consumer group.

### Consumers receive a "Trying to commit unreserved partition" message and a 400 error

When requesting messages from a stream, a consumer that's part of a consumer group might see an error message such as the following:
```

```

This error means that the consumer tried to commit an offset for a partition that wasn't reserved for that particular consumer. This error can happen when the consumer appears to have timed out, partitions are rebalanced to another consumer, and then the consumer tries to commit offsets. The default timeout is 30 seconds for a consumer. Timeouts for a consumer can be extended by sending a heartbeat. See[Consuming as a Group](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/using_consumer_groups.htm#consuming_as_a_group_topic-consuming_as_a_group)for more information.

This error can also occur when pipelining (`commitOnGet=false`) and no commits occurred for a significant amount of time (more than 30 seconds).

### Request fails with an "Unable to parse JSON body" message and a 400 error

When you send a request to Streaming, you might see an error message similar to the following:
```

```

This error generally means that the JSON body contains an entry in an invalid format.

### Ruby SDK requests fail with an "Unable to parse JSON body" message and a 400 error

When you send a request to Streaming using the[Ruby SDK](https://docs.oracle.com/iaas/Content/API/SDKDocs/rubysdk.htm), you might see an error message similar to the following:
```

```

The Ruby SDK doesn't do any encoding. You must use`Base64`to encode the strings that are sent in the key and value fields. For example:
```

```

## Troubleshooting Streaming and Kafka

### Kafka Connect configuration creation fails

When you try to create a Kafka Connect configuration, you might see an error message such as the following:
```

```

To create a Kafka Connect configuration, you need to create the correct IAM policy in your tenancy. For example:
```

```

For more information, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/kafkacompatibility_topic-Kafka_Connect.htm#policy)
