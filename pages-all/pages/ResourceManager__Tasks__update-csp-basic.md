# Updating a Configuration Source Provider (Any Type)
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-basic.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating a Configuration Source Provider (Any Type)

Update a configuration source provider in Resource Manager.
When you update a configuration source provider, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-basic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-basic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-basic.htm#)
- 

- On the Configuration source providers list page, select the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see[Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm).
- On the configuration source provider's details page, select Edit .
- To change the connection details, in the Edit configuration source provider panel, edit one or more of the following values:

- To use a different[private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm#private-git), select the endpoint and then select an SSL certificate. This option is available when the configuration source provider was created with a private endpoint.
- Edit server and other connection values associated with the type of configuration source provider. For reference, see[Creating a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp.htm).
- Optionally change the compartment, name, or description.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/update.html)oci resource-manager configuration-source-provider update`command and required parameters to update a configuration source provider.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[UpdateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/UpdateConfigurationSourceProvider)
