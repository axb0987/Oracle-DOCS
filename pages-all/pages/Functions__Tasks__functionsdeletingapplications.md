# Deleting an Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingapplications.htm
- Fetched: 2026-09-05 02:08 CDT

# Deleting an Application

Find out how to delete an application with OCI Functions.

Note that having deleted an application, you cannot undelete the application later.

For prerequisites and more information, see[Deleting Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingapplications-about.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingapplications.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingapplications.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingapplications.htm#)
- 

When using the Console to delete applications, note the following points:
- When you delete an application in the Console, all its functions are also deleted.
- When you delete an application in the Console, you're always prompted to confirm deletion because you can't undelete an application or function later.

To delete an application in OCI Functions using the Console:
- On the Applications list page, locate the application that you want to delete. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- 

From the Actions menu (three dots) for the application, select Delete and confirm that you want to delete the application:
- If the application doesn't contain any functions, select Delete to confirm that you want to delete the application.
- If the application does contain functions, a list of the functions in the application is shown. To delete the application, enter`DELETE <APPLICATION-NAME>`in the text box, and select Delete .

Deleting an application and all its functions doesn't delete the Docker images on which the functions are based. To delete the images, you must delete them explicitly. For more information, see[Deleting and Undeleting an Image](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrydeletingimages.htm).
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

When using the Fn Project CLI to delete applications, note that you cannot delete an application if it contains functions. If an application contains functions, you must delete the functions first before you can delete the application (see[Deleting Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeletingfunctions-about.htm)).

To delete an application in OCI Functions using the Fn Project CLI:
- 

Log in to your development environment as a functions developer.
- 

Enter the following command to delete the application:

```

```

where`<app-name>`is the name of the application to delete.

For example:

```

```

- 

Verify that the application has been deleted by entering:

```

```

Using the OCI CLI

Use the[oci fn application delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/application/delete.html)command and required parameters to delete an application:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[DeleteApplication](https://docs.oracle.com/iaas/api/#/en/functions/latest/Application/DeleteApplication)
