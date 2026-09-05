# Creating a Stream Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Stream Pool

Create a stream pool in the Streaming service. A stream pool is a logical grouping for streams.

Every stream must be a member of a stream pool. If you don't create a stream pool or specify an existing stream pool when creating a stream, then the Streaming service uses a default pool to contain the stream. To review requirements for creating and managing streams, see[Getting Started with Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streaminggettingstarted.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm#)
- 

- On the Stream pool list page, select Create stream pool . If you need help finding the list page, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm).
- Enter a name for the stream pool. Avoid entering confidential information.
- Select the compartment for the stream pool.
- (Optional) In the Tags section, add one or more tags to the stream pool.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Under Select endpoint type , select Public endpoint or Private endpoint , depending on whether you want to restrict traffic to streams in this stream pool to a private endpoint that doesn't require traffic to traverse the internet.

To create a private endpoint, you need access to a virtual cloud network (VCN) with a private subnet. Select a VCN with a private subnet where DNS resolution is also enabled, and then select the subnet.

If instead you want to assign a specific private IP address, you must select one that belongs to the subnet's CIDR. By default, the Networking service assigns a random private IP address on your behalf and applies no security rules to the stream pool. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).

You can also select an existing network security group to apply the same set of security rules to each stream in the pool.
- Under Configure encryption settings , select how to encrypt the streams in the stream pool.

By default, Encrypt using Oracle-managed keys is selected. To encrypt the data in the streams in this stream pool by using your own Vault encryption key, select Encrypt using customer-managed keys . To use the Vault service, you need access to a vault and key, and you must allow the service to use the key.
- Vault : Select the compartment that contains the vault with the master encryption key that you want to use, and then select the vault.
- Master encryption key : Select the compartment that contains the master encryption key that you want to use, and then select the key.

For more information about encryption with a Vault key that you manage, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).
- (Optional) If you intend to use Kafka with this stream pool, select Advanced options .
- Select Auto create topics and configure the stream settings:

- Default retention period (Hours) : Specify the number of hours for the stream's retention period.
- Default number of partitions : Specify the default number of partitions for the stream.
- Select View Kafka settings after the stream pool is created to display the Kafka Connection settings for the stream pool after it's created.
- (Optional) If you selected a private endpoint type, you can add security attributes to control access to resources through the Zero Trust Packet Routing service. You can add up to three security attributes per stream pool. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
- Select Show security attributes .
- Select a security attribute namespace and key, then enter a value.
- To add more security attributes, select Add security attribute .
- Select Create .
- 

Use the[oci streaming admin stream-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/create.html)command and required parameters to create a stream pool:

```

```

For example:
```

```

Tip  
  
Provide input for`--custom-encryption-key-details`,`--private-endpoint-details`, and`--kafka-settings`as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/CreateStreamPool)API operation to create a stream pool.

## Using OCI SDKs

To create a stream pool, use the`createStreamPool`method of`StreamAdminClient`.

See the[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm)for detailed SDK examples.

## Using Resource Manager and Terraform

Use the`oci_streaming_stream_pool`resource to create a stream pool with optional private endpoint and Kafka compatibility settings. Private endpoint settings require a VCN, a subnet, and a network security group. This example Terraform configuration creates those resources as well.

For example:
```

```

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
