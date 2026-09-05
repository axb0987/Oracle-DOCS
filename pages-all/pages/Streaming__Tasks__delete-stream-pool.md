# Deleting a Stream Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-stream-pool.htm
- Fetched: 2026-09-05 03:05 CDT

# Deleting a Stream Pool

Delete a stream pool in the Streaming service.
Caution  
  
The stream pool and all streams within the pool are deleted immediately. You can't recover a deleted stream pool.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-stream-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-stream-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-stream-pool.htm#)
- 

- On the Stream pool list page, find the stream pool that you want to work with. If you need help finding the list page or the stream pool, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-stream-pools.htm).
- From the Actions menu (three dots) for the stream pool, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci streaming admin stream-pool delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/delete.html)command and required parameters to delete a stream pool:

```

```

For example:
```

```

Select`y`and press`Enter`. The stream pool is deleted with no further prompting.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/DeleteStreamPool)operation to delete a stream pool.

## Using OCI SDKs

For detailed SDK examples, see[Developer Guide to Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/developing.htm).

## Using Resource Manager and Terraform

To delete a Streaming resource from Resource Manager:[run a destroy job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm)and then[delete your stack](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/delete-stack.htm).

To delete a Streaming resource from the Terraform CLI, run`terraform destroy`.

[About Resource Manager and Terraform](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/delete-stream-pool.htm#)

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)is an Oracle Cloud Infrastructure (OCI) service that allows you to automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model.

A Terraform configuration codifies your infrastructure in declarative configuration files. The configuration defines the resources you intend to provision, variables, and specific instructions for provisioning the resources

You can use Resource Manager or the Terraform CLI with the[OCI Terraform provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)to see how your streams and stream pools are represented in Terraform configuration files.

For more information about writing configurations for use with Resource Manager, see[Terraform Configurations for Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm)and[Terraform Configuration](https://www.terraform.io/docs/configuration/index.html)
