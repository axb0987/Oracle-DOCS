# Editing an Instance Console History Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-editing.htm
- Fetched: 2026-09-05 01:51 CDT

# Editing an Instance Console History Log

Edit an instance console history log.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-editing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-editing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-editing.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances-displayingconsole.htm).
- Select an instance.
- Select the option you see:
- From the OS Management tab, scroll down to Console history .
- Under Resources , select Console history .
- 

In the console history list, for the console history capture that you want to view, from the Actions menu (three dots) select View details . The console history and metadata are displayed.
- Edit the Name or tagging as needed. Avoid entering confidential information.
- Select Save and close to save your changes.
- (Optional) Select Download to download the console history log to your local system.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/update.html)compute console-history update`command and required parameters to edit an instance console history log:
```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to get the console history details:
- [UpdateConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/UpdateConsoleHistory)
