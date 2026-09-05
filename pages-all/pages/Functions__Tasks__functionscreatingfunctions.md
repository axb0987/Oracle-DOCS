# Creating Functions from Existing Docker Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm
- Fetched: 2026-09-05 02:08 CDT

# Creating Functions from Existing Docker Images

Find out how to create functions from existing Docker images with OCI Functions.

You can create a new function definition in the OCI Functions server in different ways:
- Using the Console, a CLI command, or an API operation to create a new function based on an existing Docker image that has already been pushed to the Docker registry (as described in this topic).
- Using the single Fn Project CLI command`fn deploy`to build a new Docker image, push the image to the Docker registry, and create a new function based on the image in one step (as described in[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm)).
- Using Code Editor (see[Creating Functions Using Code Editor](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingfunctions-usingcodeeditor.htm)).
- Using pre-built functions (see[Creating Functions Using Pre-Built Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functions_pbf_creating_prebuilt.htm)).

When creating a new function based on an existing Docker image, you specify function metadata to store in the OCI Functions server. For example, the maximum length of time the function is allowed to execute for.

The existing image on which you base a new function must be suitable for use with OCI Functions. Typically, to build and push a suitable image, you or somebody else will use Fn Project CLI commands and/or Docker CLI commands. For example, having written your function code and a func.yaml file containing function metadata (perhaps based on the template helloworld function and func.yaml created using`fn init`), you can:
- Use`fn build`to build a new Docker image from the function.
- Use`docker push`to push the image to the Docker registry.

With the image in the Docker registry, you can then use the Console, a CLI command, or an API operation to create a function based on the image, as described in this topic.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm#)
- 

- On the Applications list page, select the application in which you want to create the function. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/list-applications.htm).
- 

Select the Functions tab.

The Functions list page opens. All functions in the selected application are displayed in a table.
- Select Create from existing image , and specify the following details:
- Name: A name for the new function. Avoid entering confidential information.
- Repository compartment: The compartment containing the repository in OCI Container Registry in the current region that contains the image.
- Repository: The repository in OCI Container Registry in the current region that contains the image.
- Image: The existing image in the OCI Container Registry repository in the current region. The image architecture must be compatible with the application's shape (see[Specifying the Compute Architecture on Which to Run Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsspecifyingcomputearchitectures.htm)).
- Memory (in MBs): The maximum amount of memory that the function can use while running.
- Synchronous invocation timeout (in seconds): The maximum amount of time that the function can run for, when invoked in Sync mode. For more information about invoking functions in Sync mode, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm).
- Detached invocation configuration: Specify how to run the function, when invoked in Detached mode:
- Detached invocation timeout (in seconds): The maximum amount of time that the function can run for, when invoked in Detached mode.
- Success destination: (optional) When the function is invoked in Detached mode, the destination to which to write invocation records when the detached invocation succeeds. Supported destinations for the results of detached invocations are the Notifications service, the Queue service, and the Streaming service. Depending on the destination you select, you are prompted to enter additional details (for example, in the case of the Notifications service, you select a Topic compartment and a Topic ). To write to the destination service, OCI Functions requires IAM permissions. If the necessary permissions do not already exist, you are prompted to confirm that you want a suitable IAM policy created for you (see[Creating IAM Policies for Detached Invocation Success and Failure Destinations](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions__section_detached-invocation-policies)).
- Failure destination: (optional) When the function is invoked in Detached mode, the destination to which to write invocation records when the detached invocation fails. Supported destinations for the results of detached invocations are the Notifications service, the Queue service, and the Streaming service. Depending on the destination you select, you are prompted to enter additional details (for example, in the case of the Notifications service, you select a Topic compartment and a Topic ). To write to the destination service, OCI Functions requires IAM permissions. If the necessary permissions do not already exist, you are prompted to confirm that you want a suitable IAM policy created for you (see[Creating IAM Policies for Detached Invocation Success and Failure Destinations](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm#functionsinvokingdetachedfunctions__section_detached-invocation-policies)).

For more information about invoking functions in Detached mode, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm).
- Enable provisioned concurrency: You can minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available.

If you select this option, you enter a value for Provisioned concurrency units (PCUs) to specify the minimum number of concurrent function invocations. The actual PCUs value you enter must be a multiple of 10. If Memory is set to 256 MB, the PCUs value must be a multiple of 20; if Memory is set to 128 MB, the PCUs value must be a multiple of 40. The total number of PCUs available depends on the size of the function, the tenancy limit, and whether provisioned concurrency has been enabled for other functions in the tenancy. For more information about provisioned concurrency, see[Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsusingprovisionedconcurrency.htm).
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select one of the following options:
- To create the function in the OCI Functions server now, select Create . The new function is shown in the Console, in the list of functions in the application you selected.
- To create the function later using Resource Manager and Terraform, select Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

Using the Fn Project CLI
Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

To use the Fn Project CLI to create a new function in the OCI Functions server from an existing Docker image that has already been pushed to the Docker registry:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, create a new function by entering:

```

```

where:
- `<app-name>`is the name of an existing application in which to create the new function.
- `<function-name>`is the name of the new function you want to create. Avoid entering confidential information.
- `<image-name>`is the name of the existing image in the Docker registry on which to base the new function. The image architecture must be compatible with the application's shape (see[Specifying the Compute Architecture on Which to Run Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsspecifyingcomputearchitectures.htm)).
- `--<property> <value>`(optionally) is the property you want to set, and the value you want it to have. Enter`fn create function --help`to see a list of properties and valid values.

For example:

```

```

A new function is created in OCI Functions, based on the existing image and with the name you specified
- 

Verify that the new function has been created by entering:

```

```

For example:
```

```

Using the OCI CLI

Use the[oci fn function create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fn/function/create.html)command and required parameters to create a function:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/CreateFunction)
