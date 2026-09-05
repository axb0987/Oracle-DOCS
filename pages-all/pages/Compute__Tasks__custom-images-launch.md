# Launching Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm
- Fetched: 2026-09-05 01:50 CDT

# Launching Custom Images

Launch a Compute custom image in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Select the custom image that you're interested in.
- On the details page, select Create instance .
- Provide additional details as described in[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).
- 

Use the[instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command and required parameters to create an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to launch instances:
- [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)
- [GetInstanceDefaultCredentials](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials)
