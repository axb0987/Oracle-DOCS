# Capturing the Instance Console History
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-capturing.htm
- Fetched: 2026-09-05 01:51 CDT

# Capturing the Instance Console History

Capture the instance console history.
Important  
  
To capture the console history, you must first create an Instance Console Connection to the instance. The steps to make an instance console connection are documented here:
- [Creating a Console Connection Using Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm#creating-instance-connection-cloud-shell)
- [Creating a Local Instance Console Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm#creating-instance-connection-local)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-capturing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-capturing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole-capturing.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances-displayingconsole.htm).
- Select an instance.
- Select the option you see:
- From the OS Management tab, scroll down to Console history .
- Under Resources , select Console history .
- 

Select View current history .
- Provide the following information:
- Name: A default name is provide for command history you want to save. Optionally, enter a name. Avoid entering confidential information.
- (Optional) Select the option you see to specify tags:
- Tagging
- Show tagging options
- (Optional) To download a copy of the console history, select Download . If selected, a log file is downloaded to your system.
- Select Save and close . A log of the console history is saved in this dialog.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/capture.html)console-history capture`command and required parameters to capture the instance console history:
```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to capture the console history:
- [CaptureConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/CaptureConsoleHistory)
