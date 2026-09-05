# Moving a File System to Another Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-file-system-to-subnet.htm
- Fetched: 2026-09-05 02:04 CDT

# Moving a File System to Another Subnet

Move a file system to another subnet.

There might be situations where you need to move a file system to a different subnet. For example, because you can't change subnet size, you might need to move the file system to a larger or smaller subnet as your needs change.
- Create the new subnet. See[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)for instructions.
- [Create a new mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm)in the new subnet.
- 

Create new export with the same export path in the new mount target to the file system. See[Creating an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)for instructions.
- Select Select an existing mount target
- Be sure that the export path for the new export is exactly the same as the export path for the original export. The original and new mount target can exist at the same time without issue.
- Switch over the instance mount point to the new mount target. This can be done at any time convenient to your maintenance schedule:
- Stop any workload application processes running on the instance mount point.
- Unmount the file system. See[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)for instructions.
- 

Mount the file system using the new mount target , but the same mount point that was previously used.

For example: If the file system was mounted with the original mount target like this:

```

```

Then the new mount command would look like this:

```

```

See[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)for instructions.
- Update any system configuration files that use the old export path. For example,`/etc/fstab`.
- Start workload applications and verify that they can access the file system as expected.
-
