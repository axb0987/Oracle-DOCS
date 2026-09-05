# Listing Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm
- Fetched: 2026-09-05 02:53 CDT

# Listing Images

Find out how to list the images in repositories in Container Registry.

Using the Console, you can list all the images in a repository. Using the CLI and the API, you have more options to filter the list of images.

Your permissions control which images you can list (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can list images in repositories that you've created, and in repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can list images in any repository in the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/list-images.htm#)
- 

- On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- On the details page, select the Image versions tab.

All images in the repository, including their version identifiers, are displayed in a table.
- 

Use the[oci artifacts container image list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/list.html)command and required parameters to list images:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListContainerImages](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImageSummary/ListContainerImages)
