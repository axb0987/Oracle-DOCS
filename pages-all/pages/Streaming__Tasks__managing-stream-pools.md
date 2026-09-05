# Managing Stream Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managing-stream-pools.htm
- Fetched: 2026-09-05 03:06 CDT

# Managing Stream Pools

Configure, create, view, and delete stream pools in the Streaming service. A stream pool is a grouping that you can use to organize and manage streams, including any shared Kafka or security settings.

Use stream pools to:
- Organize streams into groups matching your organizational structure or a specific solution
- Restrict access to a specified virtual cloud network (VCN) inside your tenancy so that streams in the pool aren't accessible through the internet
- Specify whether to encrypt the data in the pool's streams using your own Vault encryption key or an Oracle-managed key

When you[create a stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm), you must specify the stream pool to contain it. You can select an existing stream pool or a new, automatically created (default) stream pool. There is no limit to the number of stream pools you can create.

Note  
  
Stream names must be unique within a stream pool.

## Tasks

- [Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm)
- [Creating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm)
- [Getting Details for a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream-pool.htm)
- [Updating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm)
- [Managing a Stream Pool's Security Attributes](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/manage-security-attributes.htm#top)
- [Moving a Stream Pool to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm)
- [Deleting a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-stream-pool.htm)

## Required IAM Policy

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

If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). For information about Streaming permissions, see[Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/streamingpolicyreference.htm).

## Stream Pools and Apache Kafka

Stream pools serve as the root of a virtual Apache Kafka cluster when you use Kafka with Streaming. All streams within the pool share the same Kafka configuration, encryption, and access control settings. Every action on that virtual cluster is scoped to that stream pool.

You can configure the stream pool to automatically create streams, or Kafka topics, and call`KafkaAdminClient::createTopic`to create a stream or topic in that stream pool.

Note  
  

When specifying the SASL Connection string to use with Kafka Java client, the following user name is required:

username="&lt;Namespace&gt;/&lt;identity_domain_name&gt;/&lt;username&gt;/&lt;stream_pool_id&gt;"

For more information, see[Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
