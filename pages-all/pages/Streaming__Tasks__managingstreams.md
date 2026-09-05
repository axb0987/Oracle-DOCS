# Managing Streams
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managingstreams.htm
- Fetched: 2026-09-05 03:06 CDT

# Managing Streams

List, create, get, update, move, and delete streams in the Streaming service. A stream is a partitioned, append-only log of messages.

For requirements to create and manage streams, see[Getting Started with Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streaminggettingstarted.htm).

For stream pools, see[Managing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managing-stream-pools.htm).

## Tasks

- [Listing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm)
- [Creating a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm)
- [Getting Details for a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm)
- [Updating a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-streams.htm)
- [Moving a Stream to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/moving-streams.htm)
- [Deleting a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/deleting-streams.htm)

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

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
