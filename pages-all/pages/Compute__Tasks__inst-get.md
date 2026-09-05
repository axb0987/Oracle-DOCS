# Getting an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-get.htm
- Fetched: 2026-09-05 01:51 CDT

# Getting an Instance

Get the details for a Compute instance in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-get.htm#)
- 

On the Compute Instances list page, select the instance that you want to view. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).

The details page opens and provides information about the instance. Example data includes:
- OCID
- Image
- Shape
- Security settings
- Networking settings
- Work requests related to this instance
- Tags assigned to this instance

The preceding list isn't comprehensive, additional information about the instance is also available on the page.
- 

Use the[instance get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/get.html)command and required parameters to get instance details:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to get an instance:
- [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance)
