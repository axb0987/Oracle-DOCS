# Unversioning an Image
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm
- Fetched: 2026-09-05 02:54 CDT

# Unversioning an Image

Find out how to unversion an image in Container Registry.

When you want to clean up the list of images in a repository without actually deleting images, you can remove the version identifier from images in Oracle Cloud Infrastructure Registry (also known as Container Registry). Removing version identifiers is referred to as 'unversioning'.

Your permissions control the images in Container Registry that you can unversion (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can unversion images in repositories you've created, and images in repositories that the groups to which you belong have been granted access by identity policies. If you belong to the Administrators group, you can unversion images in any repository in the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryuntaggingimages.htm#)
- 

- On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- On the details page, select the Image versions tab.
All images in the repository, including their version identifiers, are displayed in a table.
- Select the image.
The details page for the image opens.
- Select the Versions tab.
- Select Delete from the Actions menu (three dots) beside the image that you want to unversion.
- When prompted, confirm the removal of the version identifier.
- 

Use the[oci artifacts container image remove-version](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/remove-version.html)command and required parameters to unversion an image:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[RemoveContainerVersion](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/RemoveContainerVersion)
