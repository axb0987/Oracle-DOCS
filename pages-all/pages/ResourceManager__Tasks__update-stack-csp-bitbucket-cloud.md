# Updating the Bitbucket Cloud Configuration Source Provider for a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp-bitbucket-cloud.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating the Bitbucket Cloud Configuration Source Provider for a Stack

Update the Bitbucket Cloud configuration source provider used by a stack in Resource Manager. The updated configuration source provider is used when you run jobs on the stack.

When you update a stack, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

For more information about configuration source providers, see[Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp-bitbucket-cloud.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp-bitbucket-cloud.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp-bitbucket-cloud.htm#)
- 

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Edit .
- On the Edit stack page, select a different Bitbucket Cloud configuration source provider.
If you need to create a Bitbucket Cloud configuration source provider, select Create configuration source provider and enter values. For information about these fields, see[Creating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm).
- Select the Bitbucket Cloud workspace, repository, and branch.
- Change other values as needed.
For information about the fields, see[Creating a Stack from Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm).
- Select Next twice.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update-from-bitbucket-cloud.html)oci resource-manager stack update-from-bitbucket-cloud`command and required parameters to update a stack's Bitbucket Cloud configuration source provider.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack)operation to update the Bitbucket Cloud configuration source provider used by a stack.

For an example of the`configSource`part of the request, see[UpdateBitbucketCloudConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateBitbucketCloudConfigSourceDetails)
