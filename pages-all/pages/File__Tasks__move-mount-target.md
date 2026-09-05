# Moving a Mount Target Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-mount-target.htm
- Fetched: 2026-09-05 02:04 CDT

# Moving a Mount Target Between Compartments

Move File Storage mount targets from one compartment to another.

When you move a mount target to a new compartment, its associated export set and exports move with it. After you move the mount target to the new compartment, inherent policies apply immediately and affect access to the mount target, export set, and exports through the Console. Moving these resources doesn't affect access to file systems and snapshots from mounted instances. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-mount-target.htm#)
- 

- On the Mount Targets list page, find the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- From the Actions menu (three dots) for the mount target, select Move resource .
- Select the Destination compartment from the list.
- Select Move resource .
- 

Use the[`fs mount-target change-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/change-compartment.html)command and required parameters to move a mount target to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeMountTargetCompartment](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/ChangeMountTargetCompartment)operation to move a mount target to another compartment.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
