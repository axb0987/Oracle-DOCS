# Updating a Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions.htm
- Fetched: 2026-09-05 02:09 CDT

# Updating a Function

Find out how to update existing functions in the OCI Functions server.

For prerequisites and more information, see[Updating Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions-about.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions.htm#)
- 

- On the Applications list page, select the application that contains the function that you want to work with. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- 

Select the Functions tab.

The Functions list page opens. All functions in the selected application are displayed in a table.
- From the Actions menu (three dots) for the function that you want to update, select Edit and update some or all the following properties:
- Repository compartment: The compartment containing the repository in OCI Container Registry in the current region that contains the image.
- Repository: The repository in the OCI Container Registry in the current region that contains the image.
- Image: The existing image in the OCI Container Registry repository in the current region. If the image has the same name and tag as the image on which the function was originally based, see[Notes About Image Digests](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions-about.htm#notesdigest).
- Memory (in MBs): The maximum amount of memory that the function can use while running.
- Synchronous invocation timeout (in seconds): The maximum amount of time that the function can run for, when invoked in Sync mode. For more information about invoking functions in Sync mode, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm).
- Detached invocation configuration: Specify how to run the function, when invoked in Detached mode:
- Detached invocation timeout (in seconds): The maximum amount of time that the function can run for, when invoked in Detached mode.
- Success destination: (optional) When the function is invoked in Detached mode, the destination to which to write invocation records when the detached invocation succeeds. Supported destinations for the results of detached invocations are the Notifications service, the Queue service, and the Streaming service. Depending on the destination you select, you are prompted to enter additional details (for example, in the case of the Notifications service, you select a Topic compartment and a Topic ). To write to the destination service, OCI Functions requires IAM permissions. If the necessary permissions do not already exist, you are prompted to confirm that you want a suitable IAM policy created for you (see[Creating IAM Policies for Detached Invocation Success and Failure Destinations](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions__section_detached-invocation-policies)).
- Failure destination: (optional) When the function is invoked in Detached mode, the destination to which to write invocation records when the detached invocation fails. Supported destinations for the results of detached invocations are the Notifications service, the Queue service, and the Streaming service. Depending on the destination you select, you are prompted to enter additional details (for example, in the case of the Notifications service, you select a Topic compartment and a Topic ). To write to the destination service, OCI Functions requires IAM permissions. If the necessary permissions do not already exist, you are prompted to confirm that you want a suitable IAM policy created for you (see[Creating IAM Policies for Detached Invocation Success and Failure Destinations](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions__section_detached-invocation-policies)).

For more information about invoking functions in Detached mode, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm).
- Enable provisioned concurrency: You can minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available.

If you select this option, you enter a value for Provisioned concurrency units (PCUs) to specify the minimum number of concurrent function invocations. The actual PCUs value you enter must be a multiple of 10. If Memory is set to 256 MB, the PCUs value must be a multiple of 20; if Memory is set to 128 MB, the PCUs value must be a multiple of 40. The total number of PCUs available depends on the size of the function, the tenancy limit, and whether provisioned concurrency has been enabled for other functions in the tenancy. For more information about provisioned concurrency, see[Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm).
- Select Save changes to update the function in the OCI Functions server.
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To use the Fn Project CLI to update an existing function in the OCI Functions server:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, update properties of an existing function by entering:

```

```

where:
- `<app-name>`is the name of an existing application containing the existing function.
- `<function-name>`is the name of the existing function you want to update.
- `--image <image-name>`(optionally) is the name of an existing image in the Docker registry that you now want to base the function on, instead of the previously specified image. If the image has the same name and tag as the image on which the function was originally based, see[Notes About Image Digests](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsupdatingfunctions-about.htm#notesdigest).
- `--<property> <value>`(optionally) is the property you want to update, and the new value you want it to have. Enter`fn update function --help`to see a list of properties and valid values.

For example:

```

```

```

```

The properties of the existing function are updated with the values you specified.
- 

Verify that the function has been updated by entering:

```

```

For example:

```

```

Output:
```

```

Using the OCI CLI

Use the[oci fn function update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/function/update.html)command and required parameters to update a function:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/UpdateFunction)
