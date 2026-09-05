# Cannot Delete VCN- Mount Target VNIC Still Attached
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/orphanedmounttarget.htm
- Fetched: 2026-09-05 02:06 CDT

# Cannot Delete VCN- Mount Target VNIC Still Attached

A mount target is an NFS endpoint that lives in a VCN subnet of your choice and provides network access for the file systems that it exports. Each mount target has a VNIC to enable network access. Mount target VNICs that remain in a VCN must be deleted before you can delete the VCN.

Deleting a mount target also deletes all of the exports of associated file systems that exist in its export set. Data in the file systems is not affected, but the file systems are no longer available through the deleted mount target. You can create new exports for the file system in a different mount target and subnet.

For more information, see[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingmounttargets.htm).

[To resolve this issue using the Console](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/orphanedmounttarget.htm#)

- 

Note the OCID in the error message you receive when you attempt to delete the VCN. Mount target OCIDs contain the identifier`mounttarget`. For example:
```

```

- Note the Compartment and Subnet information of the VCN you want to delete, and to assist navigation and choosing the correct mount target to delete.
- 

Delete the mount target using the following steps:
- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- 

In the List Scope section, select a compartment.
- Find the mount target you want to delete.
- Click the Actions menu (three dots) , and then click Delete .
Caution  
  

Deleting the mount target also deletes all of its exports of associated file systems. File systems are no longer available through the deleted mount target.
Tip  
  
In the Console, the mount target OCID can be seen in the mount target details page in the Mount Target Information tab. See[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingmounttargets.htm)for more information about how to view the mount target details page. Be sure the mount target OCID seen on the details page matches the mount target OCID provided by the VCN delete process error message.
- Delete the VCN.

[To resolve this issue using the API](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/orphanedmounttarget.htm#)

- 

Note the OCID in the error message you receive when you attempt to delete the VCN. Mount target OCIDs contain the identifier`mounttarget`. For example:
```

```

- 

Delete the mount target using the following steps:
- 

Use[DeleteMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/DeleteMountTarget)to delete the mount target. For example:

```

```

- 

You can use[GetMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/DeleteMountTarget)to verify that the mount target has been deleted. For example:

```

```

The API should return`Status 404 Not Found`.

[To resolve this issue using the CLI](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/orphanedmounttarget.htm#)

For general information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Note the OCID in the error message you receive when you attempt to delete the VCN. Mount target OCIDs contain the identifier`mounttarget`. For example:
```

```

- 

Delete the mount target using the following steps:
- 

Use`oci fs mount-target delete`to delete the mount target. For example:

```

```

- 

You can use`oci fs export get`to verify that the mount target has been deleted. For example:

```

```

The CLI should return a message indicating the mount target is not found. For example:
```

```

If you still can't delete the VCN, be sure there are no other resources remaining in the VCN that might prevent it. For more information, see[Subnet or VCN Deletion](https://docs.oracle.com/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion)
