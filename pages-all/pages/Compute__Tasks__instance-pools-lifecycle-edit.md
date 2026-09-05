# Editing Instance Pools Pre-termination Lifecycle Actions
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-edit.htm
- Fetched: 2026-09-05 01:51 CDT

# Editing Instance Pools Pre-termination Lifecycle Actions

Edit a pre-termination lifecycle action when you want to change the timeout, update the preservation behavior, or enable pre-termination for an existing instance pool.

## Before You Begin

Before you begin editing a instance pool pre-termination action, consider the following.
- Make sure that you have permission to update instance pools in the target compartment.
- Identify the instance pool that you want to update.
- Decide the new completion timeout duration and the preservation behavior for boot volumes and block volumes. In Console, enter the duration in minutes. For CLI and API payloads, set`timeout`in seconds.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-edit.htm#)
- 

Perform these steps to edit the instance pool pre-termination action.
- Navigate to the Instance Pools page in the Console, and then open the instance pool that you want to update.
- Open the Lifecycle management tab to review the current pre-termination settings.
- Select Actions , and then select Edit lifecycle management .
- In Edit lifecycle management , update Pre-termination , Completion timeout duration in minutes, Preserve boot volume , and Preserve block volume as needed.
- Select Update .
- 

To update the size of an instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html)instance-pool update`command:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

In`update.json`, include the pre-termination settings and set`isEnabled`to`true`. Example:

```

```

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the`UpdateInstancePool`operation:

```

```

Include the updated`lifecycleManagement.lifecycleActions.preTermination`
