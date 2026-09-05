# Renaming an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/renaminginstance.htm
- Fetched: 2026-09-05 01:52 CDT

# Renaming an Instance

You can rename an instance without changing its Oracle Cloud Identifier (OCID).

For permissions, see[Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-permissions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/renaminginstance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/renaminginstance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/renaminginstance.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Select Actions then More actions then Edit .
- Select More actions then Edit .
- Enter a new name. Avoid entering confidential information.
- Select Save changes .
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to rename an instance:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
