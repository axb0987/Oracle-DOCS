# Getting Details for a Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm
- Fetched: 2026-09-05 03:06 CDT

# Getting Details for a Stream

Get the details for a stream in the Streaming service. Stream details include the Messages endpoint and the stream OCID.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm#)
- 

On the Streams list page, select the stream that you want to work with. If you need help finding the list page or the stream, see[Listing Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/listing-streams.htm).
- 

Use the[oci streaming admin stream get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream/get.html)command and required parameters to get details for a stream:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetStream](https://docs.oracle.com/iaas/api/#/en/streaming/latest/Stream/GetStream)operation to get details for a stream.

## Using OCI SDKs

Use the`getStream`method to get details about a stream.

For detailed SDK examples, see[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm).

## Using Resource Manager and Terraform

Use the`oci_streaming_stream`data source to get the details for a stream.

For example:
```

```

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/get-stream.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
