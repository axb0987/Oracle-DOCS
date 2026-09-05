# Deleting Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-delete.htm
- Fetched: 2026-09-05 01:50 CDT

# Deleting Custom Images

Delete a Compute custom image in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-delete.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- For the custom image that you're interested in, from the Actions menu (three dots) select Delete .
- Confirm when prompted.
- 

Use the[image delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/delete.html)command and required parameters to delete a custom image:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to delete an image:
- [DeleteImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/DeleteImage)
