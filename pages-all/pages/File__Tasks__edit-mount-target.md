# Editing a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-mount-target.htm
- Fetched: 2026-09-05 02:03 CDT

# Editing a Mount Target

Change a File Storage mount target.

You can change the display name of the mount target. You can also[add a mount target to a Network Security Group](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/add-mount-target-to-nsg.htm),[set the reported size of a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size-mt.htm),[change the a mount target's performance level](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm), add[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm)[security associations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/zpr-mount-target.htm), and[tag a mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-mount-target.htm).
Note  
  
Changing the display name doesn't affect mounting file systems exported through the mount target.

Mount targets configuration options are also used when[setting up LDAP for authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm)and[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-mount-target.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select Rename .
- Enter the new mount target name. Avoid entering confidential information. Then select Update .
- 

Use the[`fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command and required parameters to edit a mount target:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)operation to update a mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
