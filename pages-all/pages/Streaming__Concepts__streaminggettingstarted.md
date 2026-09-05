# Getting Started with Streaming
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streaminggettingstarted.htm
- Fetched: 2026-09-05 03:05 CDT

# Getting Started with Streaming

Learn about the Streaming service and start working with streams.

Get started with Streaming by familiarizing yourself with the service and the ways you can access it:
- [Overview of Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm)
- [Accessing Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/accessing-streaming.htm)
- [Limits on Streaming Resources](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm)
- [Partitioning a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/partitioningastream.htm)
- [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streaminggettingstarted.htm#creating_stream_pools_iam)

Then, move on to stream creation, production, and consumption:
- [Managing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/managingstreams.htm)
- [Managing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/managing-stream-pools.htm)
- [Publishing Messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/publishing.htm)
- [Consuming Messages](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/consuming.htm)
- [Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/kafkacompatibility.htm)

## Required IAM Policy

Configure required policies to grant access to Streaming resources.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let streaming admins manage streaming resources](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#streaming-manage-streams)lets the specified group do everything with streaming and related Streaming service resources.

### Policies for Private Endpoints

To set up a private endpoint, you must have access to a VCN with a private subnet where DNS resolution is enabled. For general information about policies and permissions to do this, see[IAM Policies for Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). Specifically, you need use permissions for a VNIC, a network security group, if you specify one, and a subnet. For example:

```

```

### Policies for Encryption Keys

To use your own encryption key, you must let the Streaming service use a Vault key to encrypt data in streams in this stream pool. For example:
```

```

The preceding policy also requires a companion policy to let Streaming use a key on behalf of a user group to create a stream pool that uses the key for cryptographic purposes. For example:

```

```

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). For more information about writing policies for the Streaming service, see[Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/streamingpolicyreference.htm)in the IAM policy reference and[Accessing Streaming Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/../Tasks/accessing-streaming-resources-across-tenancies.htm)
