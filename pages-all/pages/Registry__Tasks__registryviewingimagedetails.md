# Getting an Image's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm
- Fetched: 2026-09-05 02:54 CDT

# Getting an Image's Details

Find out how to get details of an image in a repository in Container Registry.

To make sure you pull the correct image or to identify images that you no longer need, you can get detailed information about the images in Container Registry.

When using the CLI and the API, you can use the image OCID or the image URI to identify the image that you want to get information about.

Your permissions control which images you can get information about (see[Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Concepts/registrypolicyrepoaccess.htm)). You can get information about images in repositories that you've created, and in repositories that the groups to which you belong have been granted access by IAM policies. If you belong to the Administrators group, you can get information about images in any repository in the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryviewingimagedetails.htm#)
- 

- On the Container Registry list page, select the repository that you want to work with. If you need help finding the list page or the repository, see[Listing Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/../Tasks/list-repository.htm).
- On the details page, select the Image versions tab.
All images in the repository, including their version identifiers, are displayed in a table.
- Select the image.
- Perform the following tasks to see the image's details:

- Select the Details tab to see the size of the image, when it was pushed and by which user, and the number of times the image has been pulled.
- Select the Versions tab to see the full path for the image with the version identifier you select.
- Select the Layers tab to see the SHA message digest of each layer in the selected image.
- Select the Signatures tab to see details of signatures created if the image was signed. For more information, see[Signing Images for Security](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).
- Select the Scan Results tab to see a summary of each scan of the image for the last 13 months. For more information, see[Scanning Images for Vulnerabilities](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registryscanningimagesforvulnerabilities.htm).
- Select the Tags tab to see the free-form tags and defined tags applied to the image. For more information, see[Applying Free-form Tags and Defined Tags to Repositories, Images, and Image Signatures](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrytaggingresourceswithfreeformdefinedtags.htm).
- (Optional) To pull an image, select Copy pull command . The command you copy includes the fully qualified path to the image's location in Container Registry, in the format`<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`.

For example,`docker pull ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test`. See[Pulling Images Using the Docker CLI](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm).
- 

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).

Using the image's OCID to get image details:

Use the[oci artifacts container image get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/get.html)command and required parameters to get details of an image:

```

```

For example:

```

```

Using the image's URI to get image details:

Use the[oci artifacts container image lookup](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/artifacts/container/image/lookup.html)command and required parameters to get details of an image:

```

```

where`image-uri`identifies a particular image in a registry, and includes a version identifier, or an image digest, or both. Note that`image-uri`does not include a registry domain.

For example:

```

```

```

```

```

```

- 

To use the image's OCID to get image details, run the[GetContainerImage](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/GetContainerImage)operation.

To use the image's URI to get image details, run the[LookupContainerImageByUri](https://docs.oracle.com/iaas/api/#/en/registry/latest/ContainerImage/LookupContainerImageByUri)
