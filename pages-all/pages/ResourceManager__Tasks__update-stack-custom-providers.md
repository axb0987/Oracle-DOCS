# Using Custom Providers with a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm
- Fetched: 2026-09-05 02:56 CDT

# Using Custom Providers with a Stack

Update a stack to fetch custom providers from Object Storage buckets.

- Limit the bucket to files that are intended for use with Terraform.
- If the stack was created before custom providers were available, then first[update the stack to use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm). This update enables the stack to use custom providers.

When you update a stack, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Before You Begin

Follow these steps to add a custom provider to a bucket.

- Set up the bucket for the custom provider. See[Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm).

- 

To store amd/x86 binaries, create a directory under the root of the bucket with the following name:

`linux_amd64`
- 

To store Arm binaries, create a directory under the root of the bucket with the following name:

`linux_arm64`
- Confirm that the name of each custom provider binary file aligns with the following convention:

`terraform-provider- <TYPE> _v <MAJOR.MINOR.PATCH>`

With optional suffix (example:`x5`or`x4`):

`terraform-provider- <TYPE> _v <MAJOR.MINOR.PATCH> _ <OPTIONAL-SUFFIX>`
- Upload the custom provider binary files to the bucket. See[Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm).
Limit the bucket to files that are intended for use with Terraform.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#)
- 

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Edit .
- On the Edit stack page, select Use custom providers .
- Select the bucket that contains the custom providers.
Limit the bucket to files that are intended for use with Terraform.
- Select Next twice.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)oci resource-manager stack update`command and required parameters to use custom providers with stacks.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack)operation to update the custom providers used by a stack.

For an example of the`CustomTerraformProvider`part of the request, see[CustomTerraformProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CustomTerraformProvider)
