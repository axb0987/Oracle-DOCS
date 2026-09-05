# Listing Mount Targets
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm
- Fetched: 2026-09-05 02:04 CDT

# Listing Mount Targets

List the mount targets that provide access to File Storage file systems.
You can use the Console to list mount targets exporting a specific file system. Use the API or CLI to list all mount targets in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- 

To view the mount targets in a different compartment, switch to a different Compartment .

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

Use the[`fs mount-target list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/list.html)command and required parameters to list mount targets:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListMountTargets](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTargetSummary/ListMountTargets)operation to list mount targets.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
