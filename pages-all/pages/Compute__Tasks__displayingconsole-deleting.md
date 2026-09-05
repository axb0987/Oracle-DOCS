# Deleting an Instance Console History Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-deleting.htm
- Fetched: 2026-09-05 01:51 CDT

# Deleting an Instance Console History Log

Delete an instance console history log.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-deleting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-deleting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-deleting.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances-displayingconsole.htm).
- Select an instance.
- Select the option you see:
- From the OS Management tab, scroll down to Console history .
- Under Resources , select Console history .
- 

In the console history list, for the console history capture that you want to delete, from the Actions menu (three dots) select Delete . You are prompted for confirmation.
- Select Delete console history to delete the log entry.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/delete.html)compute console-history`command and required parameters to delete an instance console history log:
```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to delete a console history log:
- [DeleteConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/DeleteConsoleHistory)
