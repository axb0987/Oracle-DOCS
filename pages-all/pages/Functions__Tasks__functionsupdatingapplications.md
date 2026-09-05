# Updating an Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingapplications.htm
- Fetched: 2026-09-05 02:09 CDT

# Updating an Application

Find out how to update applications with OCI Functions.

Having previously created an application in OCI Functions, you can change some, but not all, of the application's details. For example, you can change the application's signature verification policy.

For more information about applications, see[Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Concepts/functionsconcepts.htm#applications).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingapplications.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingapplications.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingapplications.htm#)
- 

- On the Applications list page, select the application that you want to update. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- Use the different tabs to update some or all the following information:
- Network security groups: See[Adding Applications to Network Security Groups (NSGs)](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingnsgs.htm)
- Configuration: See[Passing Custom Configuration Parameters to Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams-about.htm).
- Signature verification: See[Signing Function Images and Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsenforcingsignedimagesfromocir.htm).
- Logs: See[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm).
- Traces: See[Distributed Tracing for Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstracing.htm).
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To use the Fn Project CLI to update an existing application in the OCI Functions server:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, update properties of an existing application by entering:

```

```

where:
- `<app-name>`is the name of the existing application you want to update.
- `--<property> <value>`is the property you want to update, and the new value you want it to have. Enter`fn update app --help`to see a list of properties and valid values.

For example:

```

```

The properties of the existing application are updated with the values you specified.
- 

Verify that the application has been updated by entering:

```

```

For example:

```

```

Output:
```

```

Using the OCI CLI

Use the[oci fn application update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/application/update.html)command and required parameters to update an application:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/UpdateApplication)
