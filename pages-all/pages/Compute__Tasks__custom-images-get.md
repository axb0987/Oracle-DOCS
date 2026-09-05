# Getting a Custom Image
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm
- Fetched: 2026-09-05 01:50 CDT

# Getting a Custom Image

Get the details of a Compute custom image in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Select the custom image that you're interested in.

The details page opens and displays the following information about the image:
- Details such as OCID, original image, and size
- Image capabilities which are the configuration options available when launching an instance from an image.
- Compatible shapes for this image.
- Work requests related to this image.
- Tags assigned to this image.
- 

Use the[image get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/get.html)command and required parameters to get a custom image:

```

```

Use the[image-shape-compatibility-entry list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image-shape-compatibility-entry/list.html)command and required parameters to get the list of compatible shapes:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to get a cluster network:
- [GetImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/GetImage)
- [ListImageShapeCompatibilityEntries](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/ListImageShapeCompatibilityEntries)
