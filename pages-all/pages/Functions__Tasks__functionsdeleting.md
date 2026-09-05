# Deleting a Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeleting.htm
- Fetched: 2026-09-05 02:08 CDT

# Deleting a Function

Find out how to delete a function with OCI Functions.

For prerequisites and more information, see[Deleting Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingfunctions-about.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeleting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeleting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeleting.htm#)
- 

When using the Console to delete functions, note the following points:
- You can delete functions individually, or you can delete all the functions in an application by deleting the application itself (hence the potential requirement for the FN_APP_DELETE permission).
- You're always prompted to confirm deletion because you cannot undelete an application or function later.

To delete an individual function without deleting the application:
- On the Applications list page, select the application that contains the function that you want to delete. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- 

Select the Functions tab.

The Functions list page opens. All functions in the selected application are displayed in a table.
- From the Actions menu (three dots) for the function, select Delete and confirm that you want to delete the function.

Deleting a function doesn't delete the Docker image on which the function is based. To delete the image, you must delete it explicitly. See[Deleting and Undeleting an Image](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrydeletingimages.htm).

To delete all the functions in an application by deleting the application:
- On the Applications list page, locate the application that contains the functions that you want to delete. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- 

From the Actions menu (three dots) for the application, select Delete and confirm that you want to delete the application:
- If the application doesn't contain functions, select Delete to confirm that you want to delete the application.
- If the application does contain functions, a list of the functions in the application is shown. To delete the application, enter`DELETE <APPLICATION-NAME>`in the text box, and select Delete .

Deleting an application and all its functions doesn't delete the Docker images on which the functions are based. To delete the images, you must delete them explicitly. For more information, see[Deleting and Undeleting an Image](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrydeletingimages.htm).
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

When using the Fn Project CLI to delete functions, note that you cannot delete an application if it contains functions (you must delete the functions first).

To delete a function in OCI Functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

Enter the following command to delete the function:

```

```

where:
- `<app-name>`is the name of the application containing the function you want to delete.
- `<function-name>`is the name of the function you want to delete.

For example:

```

```

- 

Verify that the function has been deleted by entering:

```

```

For example:

```

```

Using the OCI CLI

Use the[oci fn function delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/function/delete.html)command and required parameters to delete a function:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[DeleteFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/DeleteFunction)
