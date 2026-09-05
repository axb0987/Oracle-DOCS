# Listing Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsviewingfunctionsapps.htm
- Fetched: 2026-09-05 02:09 CDT

# Listing Functions

Find out how to list functions with OCI Functions.

You can list functions using the Console, the Fn Project CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsviewingfunctionsapps.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsviewingfunctionsapps.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsviewingfunctionsapps.htm#)
- 

- Sign in to the Console as a functions developer.
- Open the navigation menu and select Developer Services . Under Functions , select Applications .

The Applications list page opens. All applications in the selected compartment are displayed in a table.
- Select the region you're using with OCI Functions.

We recommend that you use the same region as the Docker registry that's specified in the Fn Project CLI context. See[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm).
- Select the compartment specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)). Alternatively, to view the applications in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select the name of an application, and then select Functions to see the functions within the application.
The Functions list page opens. All functions within the application you selected are displayed in a table, including the following information:
- The Docker image created for each function.
- When the function was last updated.
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To list functions deployed to OCI Functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

Enter the following command to see a simple list of functions in a particular application:

```

```

For example:
```

```

Enter`fn list functions --help`to see more list options.

Using the OCI CLI

Use the[oci fn function list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/function/list.html)command and required parameters to list functions:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListFunctions](https://docs.oracle.com/iaas/api/#/en/functions/latest/FunctionSummary/ListFunctions)
