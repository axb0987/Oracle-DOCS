# Getting a Function's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-function.htm
- Fetched: 2026-09-05 02:09 CDT

# Getting a Function's Details

Find out how to get details of a function deployed to OCI Functions.

For more information about functions, see[Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Concepts/functionsconcepts.htm#functions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-function.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-function.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-function.htm#)
- 

- On the Applications list page, select the application that contains the function that you want to work with. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- 

Select the Functions tab.

The Functions list page opens. All functions in the selected application are displayed in a table.

The Functions list page shows particularly significant information about all the functions in the application that you selected, including the following:
- The Docker image created for each function.
- The function's invoke endpoint.
- When the function was last updated.
- On the Functions list page, select the function that you want to work with.

The function's details page opens and displays more information about the function. Some items on the page are read-only, and other items enable you to edit and update the function's configuration. Access the various resources associated with the function by selecting their links or tabs.
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To get details of a function deployed to OCI Functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

Enter the following command to get details about a particular function:

```

```

For example:
```

```

Using the OCI CLI

Use the[oci fn function get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/function/get.html)command and required parameters to get details about a function:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/GetFunction)
