# Listing Repositories
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm
- Fetched: 2026-09-05 02:53 CDT

# Listing Repositories

Find out how to list the repositories in Container Registry.

Your permissions control which repositories you can list (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can list repositories that you've created, and repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can list any repository in the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-repository.htm#)
- 

- Open the navigation menu and select Developer Services . Under Containers &amp; Artifacts , select Container Registry .
The Container Registry list page opens.
- Select the region that contains the registry.
- To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

The Container Registry list page displays the repositories in the selected region and compartment to which you have access.
- 

Use the[oci artifacts container repository list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/list.html)command and required parameters to list repositories:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListContainerRepositories](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/ListContainerRepositories)
