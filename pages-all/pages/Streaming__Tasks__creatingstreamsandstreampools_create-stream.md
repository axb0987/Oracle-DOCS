# Creating a Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm
- Fetched: 2026-09-05 03:05 CDT

# Creating a Stream

Configure and create a stream in the Streaming service.

Before publishing messages to a stream or consuming messages from a stream, you must first create a stream. When creating a stream, consider your[partitioning](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/partitioningastream.htm)and[security](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streamsecurity.htm)strategies. To review requirements for creating and managing streams, see[Getting Started with Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streaminggettingstarted.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm#)
- 

- On the Streams list page, select Create stream . If you need help finding the list page, see[Listing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm).
- Enter the following information:

- Stream name : Enter a name for the stream. The name doesn't have to be unique within the compartment, but must be unique to the stream pool. The stream name can't be changed. Avoid entering confidential information.
- Compartment : Select the compartment in which to create the stream.
- Tags : (Optional) Add one or more tags to the stream.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select the stream pool to contain your stream.

- If the compartment has an existing stream pool, you can select it.
- If no stream pool exists in the compartment, you can select one of the following options:
- Select Auto-Create a default stream pool . A default stream pool is created for you when you create the stream.
- Select Create new stream pool and configure the stream pool. For instructions, see step 5 in[Creating a Stream Pool](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creating-stream-pools.htm).
- Provide values for Define stream settings :

- Retention (in hours) : Enter the number of hours (from 24 to 168) to retain messages in this stream. The default value is 24.
- 

Number of partitions: Enter the number of partitions for the stream. The maximum number is based on the limits for your tenancy.

The maximum Total write rate and Total read rate values for the stream are displayed as you adjust the number of partitions.
- Select Create .
- 

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
Note  
  
The examples in this section use the full syntax for all parameters, for example`--compartment-id`. For some parameters, there are shortened versions that you can use instead, like`-c`. See the CLI online help for instances of a shortened parameter associated with a command.

You can create a stream in a compartment or a stream pool. The`--compartment-id`and`--stream-pool-id`parameters cannot be specified at the same time.

```

```

```

```

For example:
```

```

- 

Use the[CreateStream](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Stream/CreateStream)API operation to create streams.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Using OCI SDKs

To create a stream, use the`createStream`method of`StreamAdminClient`.

See the[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm)for detailed SDK examples.

## Using Resource Manager and Terraform

Use the`oci_streaming_stream`resource in Terraform configurations to create a stream in a compartment.

For example:
```

```

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
