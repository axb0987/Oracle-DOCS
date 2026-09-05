# Moving a Stream Pool to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm
- Fetched: 2026-09-05 03:05 CDT

# Moving a Stream Pool to a Different Compartment

Move a stream pool in the Streaming service to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm#)
- 

- On the Stream pool list page, find the stream pool that you want to work with. If you need help finding the list page or the stream pool, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-stream-pools.htm).
- From the Actions menu (three dots) for the stream pool, select Move resource .
- In the Move resource dialog box, select the compartment that you want to move the stream pool to.
- Select Move resource .
- 

Use the[oci streaming admin stream-pool change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/change-compartment.html)command and required parameters to move a stream pool to a different compartment:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeStreamPoolCompartment](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/ChangeStreamPoolCompartment)operation to move a stream pool to a different compartment.

## Using OCI SDKs

For detailed SDK examples, see[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/developing.htm).

## Using Resource Manager and Terraform

Update the`oci_streaming_stream_pool`resource in your Terraform configuration and[edit your stack](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/update-stack.htm)or run a`terraform apply`job.

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/change-compartment-stream-pool.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
