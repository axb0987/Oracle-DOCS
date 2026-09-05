# Updating a Stream Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm
- Fetched: 2026-09-05 03:06 CDT

# Updating a Stream Pool

Change a stream pool's settings for Kafka use and encryption (master encryption key).

When you update a stream pool, you can also update the following:
- Tags : For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm).

For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Security attributes : For instructions, see[Managing a Stream Pool's Security Attributes](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/manage-security-attributes.htm#top).

For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

To review requirements for creating and managing streams, see[Getting Started with Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streaminggettingstarted.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm#)
- 

- On the Stream pool list page, select the stream pool that you want to work with. If you need help finding the list page or the stream pool, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-stream-pools.htm).
- On the details page, select Edit settings .
- To use the stream pool with Kafka, select Auto create topics and configure the stream settings:

- Default retention period (Hours): Specify a number of hours for the stream's retention period.
- Default number of partitions : Specify the default number of partitions for the stream.
- To encrypt the data in the streams in this stream pool by using your own Vault encryption key, select Encrypt using customer-managed keys . To use the Vault service for your encryption needs, you need access to a vault and key, and you must allow the service to use the key.

- Vault : Select the compartment that contains the vault with the master encryption key that you want to use, and then select the vault.
- Master encryption key : Select the compartment that contains the master encryption key that you want to use, and then select the key.

For more information about encryption with a Vault key that you manage, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).
Note  
  

You can also update encryption settings from the details page.
- To stop using an Oracle-managed key in favor of a Vault master encryption key that you manage, select Assign , select a vault and encryption key you have access to, and then select Assign .
- To select a different Vault master encryption key that you manage, select Update , select a vault and encryption key you have access to, and then select Update .
- To remove the assigned Vault master encryption key and let Oracle manage the encryption key, select Unassign and then select Unassign again to confirm the removal of the existing key assignment.
- Select Edit settings to save changes.
- 

Use the[oci streaming admin stream-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/update.html)command and required parameters to update a stream pool:

```

```

For example:
```

```

Tip  
  
Provide input for`--custom-encryption-key-details`,`--private-endpoint-details`, and`--kafka-settings`as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/UpdateStreamPool)operation to update a stream pool.

## Using OCI SDKs

See the[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm)for detailed SDK examples.

## Using Resource Manager and Terraform

Update the`oci_streaming_stream_pool`resource in your Terraform configuration and[edit your stack](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/update-stack.htm)or run a`terraform apply`job.

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/updating-stream-pools.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
