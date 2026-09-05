# Getting an Application's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-application.htm
- Fetched: 2026-09-05 02:09 CDT

# Getting an Application's Details

Find out how to get details of an application with OCI Functions.

For more information about applications, see[Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Concepts/functionsconcepts.htm#applications).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-application.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-application.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/get-application.htm#)
- 

On the Applications list page, select the application that you want to get information about. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).

The application's details page opens and displays more information about the application. Some items on the page are read-only, and other items enable you to edit and update the application's configuration. Access the various resources associated with the application by selecting their links or tabs.
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To get details of an application using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

Enter the following command to get details about a particular application:

```

```

For example:
```

```

Using the OCI CLI

Use the[oci fn application get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/application/get.html)command and required parameters to get details about an application:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/GetApplication)
