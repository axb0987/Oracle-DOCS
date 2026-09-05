# Disabling Instance Pools Pre-termination Lifecycle Actions
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-disable.htm
- Fetched: 2026-09-05 01:51 CDT

# Disabling Instance Pools Pre-termination Lifecycle Actions

Disable a pre-termination lifecycle action when you want an instance pool to stop pausing termination before future scale-in or pool termination events. To disable the feature, set`isEnabled`to`false`.

The pre-termination settings remain part of the pool configuration and can be enabled again later by setting`isEnabled`back to`true`.

## Before You Begin

Before disabling a pre-termination action, consider the following.
- Make sure that you have permission to update instance pools in the target compartment.
- Identify the instance pool that you want to update.
- Keep the current`timeout`value, in seconds, and preservation settings available so that you can include them in CLI or API update payloads.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-disable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-disable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-lifecycle-disable.htm#)
- 

To disable a instance pool pre-termination action, follow these steps.
- Navigate to the Instance Pools page in the Console, and then open the instance pool that you want to update.
- Open the Lifecycle management tab to review the current pre-termination settings.
- Select Actions , and then select Edit lifecycle management .
- In Edit lifecycle management , turn off Pre-termination .
- Select Update .
- 

To update the size of an instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html)instance-pool update`command:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

In`disable.json`, include the pre-termination settings and set`isEnabled`to`false`. Example:

```

```

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the`UpdateInstancePool`operation:

```

```

Include the updated`lifecycleManagement.lifecycleActions.preTermination`fields in the request body and set`isEnabled`to`false`
