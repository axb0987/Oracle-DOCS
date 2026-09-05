# Listing Stream Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm
- Fetched: 2026-09-05 03:06 CDT

# Listing Stream Pools

List streams pools in the Streaming service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm#)
- 

- Open the navigation menu and select Analytics &amp; AI . Under Messaging , select Streaming .
- Under Analytics &amp; AI , select Stream Pools .
The Stream pool list page opens. All stream pools in the selected compartment are displayed in a table.
- To view the stream pools in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

Use the[oci streaming admin stream-pool list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/list.html)command and required parameters to list stream pools:

```

```

By default, the first 10 stream pools are returned.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListStreamPools](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPoolSummary/ListStreamPools)operation to list stream pools.

## Using Resource Manager and Terraform

Use the`oci_streaming_stream_pool`data source to list stream pools in a compartment.

Example representation of a stream pool (a`oci_streaming_stream_pool`resource):
```

```

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/list-stream-pools.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
