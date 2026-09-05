# Consuming Messages
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/consuming.htm
- Fetched: 2026-09-05 03:05 CDT

# Consuming Messages

Using a specified cursor, consume messages from a stream in the Streaming service.

Consuming messages from a stream requires you to:
- Create a cursor.
- Use the cursor to get, or read, messages.
- Use the returned cursor to continue reading messages.

You can[use an individual consumer to read messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_a_single_consumer.htm)from one or more streams, or[use consumer groups to read messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/using_consumer_groups.htm)from a stream.

Following are tasks that you can do related to consuming messages.
- [Creating a Cursor](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-cursor.htm)
- [Creating a Group Cursor](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/create-group-cursor.htm)
- [Getting (Reading) Messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-message.htm)
- [Sending a Heartbeat](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/send-heartbeat-consumer-group.htm)
- [Manually Committing an Offset](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/commit-consumer-group.htm)
- [Getting the Current State of a Consumer Group](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-consumer-group.htm)
- [Updating a Consumer Group](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-consumer-group.htm)
Tip  
  
You can also use[Oracle Cloud Infrastructure Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)to consume data from a stream and pass messages to[Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)or any other supported Connector Hub target.

You can[show the latest messages in a stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/show-recent-messages.htm)using the Console. However, to consume messages from the stream, you use the CLI, API, or an SDK to create and use cursors.

To consume messages using OCI SDKs, see the[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm). See also[Developing with Kafka and Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing-kafka.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let streaming admins manage streaming resources](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#streaming-manage-streams)lets the specified group do everything with streaming and related Streaming service resources.

You can create a policy that gives a tenant stream-pull access to consume data from a stream in another tenant. For more information about Streaming policies, see[Accessing Streaming Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/accessing-streaming-resources-across-tenancies.htm)and[Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/streamingpolicyreference.htm).

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)
