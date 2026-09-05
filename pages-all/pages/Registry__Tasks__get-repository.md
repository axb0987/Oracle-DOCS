# Getting a Repository's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm
- Fetched: 2026-09-05 02:53 CDT

# Getting a Repository's Details

Find out how to get details of a specific repository in Container Registry.

You can get detailed information about the repositories in Container Registry.

Your permissions control which repositories you can get information about (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can get information about repositories that you've created, and repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can get information about any repository in the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/get-repository.htm#)
- 

On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).

The details page opens and displays information about the repository. Access the various resources associated with the repository by selecting their tabs.
- 

Use the[oci artifacts container repository get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/get.html)command and required parameters to get details of a repository:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetContainerRepository](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/GetContainerRepository)
