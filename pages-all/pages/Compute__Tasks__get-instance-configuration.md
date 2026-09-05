# Getting an Instance Configuration Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-instance-configuration.htm
- Fetched: 2026-09-05 01:51 CDT

# Getting an Instance Configuration Details

Get information about a Compute instance configuration using the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-instance-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-instance-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-instance-configuration.htm#)
- 

- On the Instance Configuration list page, select a instance configuration to view its details page. If you need help, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/list-instances.htm).
- 

The details page displays information about the instance configuration under Details, Networking, Storage, Security, Work Requests and tags tabs.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/get.html)instance-configuration get`command and required parameters to get information about an instance configuration:

```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[GetInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/GetInstanceConfiguration)
