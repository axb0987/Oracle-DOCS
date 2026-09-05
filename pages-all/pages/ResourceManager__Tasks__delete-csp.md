# Deleting a Configuration Source Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm
- Fetched: 2026-09-05 02:55 CDT

# Deleting a Configuration Source Provider

Delete a configuration source provider in Resource Manager.

Note  
  
A configuration source provider can be deleted only if it's not associated with a stack. To remove an association with a stack,[edit the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm#)
- 

- On the Configuration source providers list page, find the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see[Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm).
- From the Actions menu (three dots) for the configuration source provider, select Delete configuration source provider .
- When prompted, confirm the deletion.
- 

Note  
  
A configuration source provider cannot be deleted if it is associated with a stack. To remove the association from the stack,[update the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp.htm).

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/delete.html)oci resource-manager configuration-source-provider delete`command and required parameters to delete a configuration source provider.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[DeleteConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/DeleteConfigurationSourceProvider)
