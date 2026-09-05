# Moving a Repository Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm
- Fetched: 2026-09-05 02:54 CDT

# Moving a Repository Between Compartments

Find out how to move a repository in Container Registry from one compartment to another.

When you create a new repository in Container Registry, you specify the compartment in which to create it. Having created the repository in one compartment, you can subsequently move it to a different compartment. For example, to change the users who are authorized to use the repository, or to change how billing for a repository is charged.

Only users with appropriate permissions can access the repository in the compartment that you move it to.

Your permissions control which repositories you can move, and the compartments that you can move them to (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can move repositories that you've created (and repositories that the groups to which you belong have been granted access by IAM policies) to any compartment to which you have access. If you belong to the Administrators group, you can move any repository in the tenancy to any compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm#)
- 

- On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- From the Actions menu for the repository, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .

The repository is moved to the compartment you selected. Only users with appropriate permissions can now access the repository in the compartment that you've moved it to.
- 

Use the[oci artifacts container repository change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/change-compartment.html)command and required parameters to move repositories between compartments:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ChangeContainerRepositoryCompartment](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/ChangeContainerRepositoryCompartment)
