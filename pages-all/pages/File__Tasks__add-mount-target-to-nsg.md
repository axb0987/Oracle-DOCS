# Adding a Mount Target to a Network Security Group
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/add-mount-target-to-nsg.htm
- Fetched: 2026-09-05 02:02 CDT

# Adding a Mount Target to a Network Security Group

Add a File Storage mount target to one or more Network Security Groups (NSGs).

File Storage requires specific rules to be configured for NSGs that are associated with mount targets. For more information, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/add-mount-target-to-nsg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/add-mount-target-to-nsg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/add-mount-target-to-nsg.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, from the Actions menu, select Edit network security groups .
- In the Edit network security groups panel:
- Select a Network security group compartment .
- Select a Network security group .
- (Optional) Select Add network security group to add more NSGs.
- Select Update .
- 

Use the[`fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command and the`--nsg-ids`parameter to add a mount target to an NSG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)operation and include the`nsgIds`parameter to add a mount target to an NSG.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
