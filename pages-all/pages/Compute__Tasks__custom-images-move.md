# Moving a Custom Image to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-move.htm
- Fetched: 2026-09-05 01:50 CDT

# Moving a Custom Image to a Different Compartment

Move a Compute custom image to a different Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-move.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Select the custom image that you're interested in.
- Select the option you see:
- Actions then Move resource .
- Move resource .
- Select the destination compartment from the list.
- Select Move resource .
- 

Use the[image change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/change-compartment.html)command and required parameters to change the compartment of a custom image:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move an image to a different compartment:
- [ChangeImageCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ChangeImageCompartment)
