# Editing a Repository
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm
- Fetched: 2026-09-05 02:53 CDT

# Editing a Repository

Find out how to edit a repository in Container Registry.

Having created a repository in Container Registry, you can edit its properties. For example, you might want to change access to a repository from private access to public access.

Your permissions control the repositories in Container Registry that you can edit (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can edit repositories you've created, and repositories that the groups to which you belong have been granted access by identity policies. If you belong to the Administrators group, you can edit any repository in the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/edit-repository.htm#)
- 

- On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
The repository's details page opens.
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm).

For example:
- Select the Details tab and make the following edits:
- 

Select the Edit button beside Access to change access to the repository (either Private or Public ).
- 

From the Actions menu, select Add scanner or Remove scanner to enable image scanning by adding an image scanner to the repository, or to disable image scanning (see[Scanning Images for Vulnerabilities](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm)).
- 

From the Actions menu, select Move resource to move the repository from one compartment to another (see[Moving a Repository Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrymovingrepos.htm)).
- 

Select the Readme tab to view and edit the readme containing information about the repository.
- 

Select the Image versions tab to view information about different image versions in the repository, delete image versions, and manage tags applied to image versions.
- 

Select the Tags tab, to apply additional free-form tags and defined tags to the repository, or to modify or remove existing tags. To apply a defined tag, you must have permissions to use the tag namespace. For more information, see[Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm).
- 

Use the[oci artifacts container repository update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/repository/update.html)command and required parameters to edit repository properties:

```

```

For example:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateContainerRepository](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerRepository/UpdateContainerRepository)
