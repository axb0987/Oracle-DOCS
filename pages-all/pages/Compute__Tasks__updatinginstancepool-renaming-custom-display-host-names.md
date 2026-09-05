# Editing Custom Instance Display and Instance Host Names
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm
- Fetched: 2026-09-05 01:52 CDT

# Editing Custom Instance Display and Instance Host Names

Change custom instance display name and host name for instances you create in an instance pool.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm#)
- 

- Navigate to the Instance pools list page.If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the name of the instance pool that you want to edit to display the details page.
- Select Edit .
- In the Instance display name formatter field, enter a new text string that includes lowercase alphanumeric characters, symbols, and dashes. The name must include the`${launchCount}`token. For example:`my-string-${launchCount}`.
- In the Instance host name formatter field, enter a new text string that includes lowercase alphanumeric characters, symbols, and dashes. The name must include the`${launchCount}`token. For example:`my-string-${launchCount}`.
- Select Save .
- 

Use the[instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html)command to change the custom display name for instances you create in an instance pool.

```

```

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool)
