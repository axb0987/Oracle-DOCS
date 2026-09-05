# Listing Streams
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm
- Fetched: 2026-09-05 03:06 CDT

# Listing Streams

List streams in the Streaming service.

For stream pools, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm#)
- 

- Open the navigation menu and select Analytics &amp; AI . Under Messaging , select Streaming .
- To view the streams in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
A list of existing streams is displayed.
- 

Use the[oci streaming admin stream list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream/list.html)command and required parameters to list streams:

```

```

By default, the first 10 streams are returned.

You can list streams by compartment or by stream pool.

Compartment example:
```

```

Stream pool example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListStreams](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamSummary/ListStreams)operation to list streams.

## Using OCI SDKs

Use the`listStreams`method to return a list of streams for the specified compartment or stream pool.

For detailed SDK examples, see[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/developing.htm).

## Using Resource Manager and Terraform

Use the`oci_streaming_streams`data source to list streams in a compartment.

For example:
```

```

Example representation of a stream (a`oci_streaming_stream`resource):
```

```

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/listing-streams.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
