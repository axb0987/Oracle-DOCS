# Deleting an Image
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm
- Fetched: 2026-09-05 02:54 CDT

# Deleting an Image

Find out how to delete an image from Container Registry.

When you no longer need an image or you want to clean up the list of image versions in a repository, you can delete images from Container Registry.

Your permissions control which images you can delete (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can delete images from repositories that you've created, and from repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can delete images from any repository in the tenancy.

In addition to deleting individual images as described in this topic, you can set up image retention policies to delete images automatically based on selection criteria that you specify. See[Retaining and Deleting Images Using Retention Policies](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymanagingimageretention.htm).

When you delete an image, it can take up to 48 hours for the deletion to take effect and for storage to be released. If you're deleting images to release storage, you can also[contact us](https://support.oracle.com/)to obtain more storage.

You can undelete an image that you've previously deleted, for up to 48 hours after you deleted it (see[Undeleting (Restoring) an Image](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/undelete-image.htm)). After that time, the image is permanently removed from Container Registry.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrydeletingimages.htm#)
- 

- On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- On the details page, select the Image versions tab.
All images in the repository, including their version identifiers, are displayed in a table.
- Select Delete from the Actions menu (three dots) beside the image that you want to remove.
- When prompted, confirm the deletion.

The image you deleted no longer appears on the Versions tab.
- 

Use the[oci artifacts container image delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/delete.html)command and required parameters to delete an image:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[DeleteContainerImage](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/DeleteContainerImage)
