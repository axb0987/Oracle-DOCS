# Listing Resource Discovery Services
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Resource Discovery Services

List services that are supported for resource discovery in Resource Manager.

When you create a stack from a compartment, the stack represents all[supported resources](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#supported-resources)in the entire compartment, at the appropriate scope. If you select the root compartment for your tenancy, then the scope is the tenancy level, such as users and groups. If you select a non-root compartment, then the scope is compartment level, such as Compute instances.

For more information about resource discovery, see[Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm#)
- 

Begin the stack creation process for an existing compartment to view the list of[resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm)services.

- On the Stacks list page, select Create stack . If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
- On the Create stack page, under Choose the origin of the Terraform configuration , select Existing compartment .
- (Optional) To filter for specific[services supported for resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Reference/services-reference.htm#supported-services), select Selected and then select the services you want.

Note  
  
This setting can't be changed when editing the stack later.
- (Optional) To finish creating a stack from a compartment, provide values for other fields and select Create .
For information about the fields, see[Creating a Stack from an Existing Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list-resource-discovery-services.html)oci resource-manager stack list-resource-discovery-services`command and required parameters to list services for resource discovery.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ListResourceDiscoveryServices](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/ListResourceDiscoveryServices)
