# Downloading the Instance Console History
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-downloading.htm
- Fetched: 2026-09-05 01:51 CDT

# Downloading the Instance Console History

Download the instance console history.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-downloading.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-downloading.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-downloading.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances-displayingconsole.htm).
- Select an instance.
- Select the option you see:
- From the OS Management tab, scroll down to Console history .
- Under Resources , select Console history .
- In the console history list, for the console history capture that you want to download, from the Actions menu (three dots) select Download , and then save the file.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/get-content.html)compute console-history get-content`command and required parameters to download the instance console history:
```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to download the console history:
- [GetConsoleHistoryContent](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/GetConsoleHistoryContent)
