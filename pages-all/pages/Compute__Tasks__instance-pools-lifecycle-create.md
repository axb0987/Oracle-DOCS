# Creating an Instance Pools Pre-termination Lifecycle Action
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-create.htm
- Fetched: 2026-09-05 01:51 CDT

# Creating an Instance Pools Pre-termination Lifecycle Action

Use a pre-termination lifecycle action when you create an instance pool and you want the pool to pause instance termination during future scale-in or pool termination events. While an instance is in`TerminationAwait`, the automation can finish cleanup before termination continues.

## Before You Begin

Before you create a pre-termination action, consider the following.
- Ensure that you have permission to create instance pools in the target compartment.
- Create or identify the instance configuration that the pool uses.
- Gather the placement details that the pool needs, such as availability domain and subnet.
- Decide the completion timeout duration and the preservation behavior for boot volumes and block volumes.
Tip  
  
In the console, enter the duration in minutes. For CLI and API payloads, set`timeout`in seconds.

## Configuration Considerations

When you configure the instance pool for lifecycle actions, consider these options.
- For CLI and API payloads,`timeout`is measured in seconds. The value must be non-negative and can't exceed the maximum value allowed by the service.
- `onTimeout.preserveBootVolumeMode`and`onTimeout.preserveBlockVolumeMode`are both required.
- Valid preservation policy values are`PRESERVE_ALWAYS`,`PRESERVE_ON_TIMEOUT`, and`DELETE_ALWAYS`.
- The pre-termination configuration applies to future scale-in and pool termination events after the pool is created.

You can configure boot volume and block volume handling independently. For each volume type, select one of these options:
- `PRESERVE_ALWAYS`: Preserve that volume type whenever termination continues.
- `PRESERVE_ON_TIMEOUT`: Preserve that volume type only when the configured timeout expires before you send the termination proceed action.
- `DELETE_ALWAYS`: Delete that volume type whenever termination continues.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-create.htm#)
- 

Follow these steps to create an instance pool with lifecycle management.
- Navigate to the Instance Pools page in the Console. If you need help finding the page, see[Creating Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm).
- Select Create instance pool .
- Complete the Basic information and Instance pool placement steps.
- Open Lifecycle management .
- In Pre-termination , turn on the feature.
- Enter the Completion timeout duration , in minutes.
- Under On completion timeout , select Preserve boot volume and Preserve block volume as needed.
- Open Review and create , verify the lifecycle-management values.
- Select Create .
- 

To create an instance pool, use the[instance-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/create.html)command:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

In`instancepool.json`, include the pre-termination settings. Example:

```

```

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the`CreateInstancePool`operation:

```

```

Include the same`lifecycleManagement.lifecycleActions.preTermination`
