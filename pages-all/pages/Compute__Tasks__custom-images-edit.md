# Editing Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-edit.htm
- Fetched: 2026-09-05 01:50 CDT

# Editing Custom Images

Edit a Compute custom image in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-edit.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Select the custom image that you're interested in.
- On the details page, perform one of the following actions depending on the option that you see:
- From Actions menu, select Edit details .
- Select the Edit details button.
- Edit the name. Avoid entering confidential information.
- Add and remove compatible shapes for the custom image. To configure the number of OCPUs and amount of memory that users can select when they use this image on a[flexible shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm#flexible), select the down arrow in the row for the shape. Then, enter values in the fields for minimum and maximum OCPU count and memory.
- 

Select Save changes .
Note  
  
After you add shape compatibility to an image, test the image on the shape to ensure that the image works on the shape. Some images (especially Windows) might never be cross-compatible with other shapes because of driver or hardware differences.
- 

Use the[image update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/update.html)command and required parameters to edit a custom image:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to edit instances:
- [UpdateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/UpdateImage)
- [AddImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/AddImageShapeCompatibilityEntry)
- [GetImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageCompatibilityEntry/GetImageCompatibilityEntry)
- [ListImageShapeCompatibilityEntries](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/ListImageShapeCompatibilityEntries)
- [RemoveImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/RemoveImageShapeCompatibilityEntry)
