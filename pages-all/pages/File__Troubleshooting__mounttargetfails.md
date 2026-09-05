# Mount Target is in Failed State
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/mounttargetfails.htm
- Fetched: 2026-09-05 02:06 CDT

# Mount Target is in Failed State

A mount target reports a Failed state. File systems might not be accessible using the mount target's IP address. If you're creating a new mount target and an export for a file system, the export might get stuck in a Creating state.

Cause : There are insufficient unallocated IP addresses in the subnet. The mount target can't fail over successfully.

Each mount target requires three internal IP addresses in the subnet to function:
- Two of the IP addresses are used during mount target creation. The third IP address must remain available for the mount target to use for high availability failover.
- The third IP address is used to create a new VNIC for the mount target during failover. The original primary IP address is retained.
- The File Storage service doesn't reserve the third IP address required for high availability failover.
- Use care to ensure that enough unallocated IP addresses remain available for your mount targets to use during failover.
- Do not use /30 or smaller subnets for mount target creation because they do not have sufficient available IP addresses for mount target creation.

Resolution :

- [Delete the failed mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-mount-target.htm).
- Export the file system through an active mount target. You can[create a replacement mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/create-mount-target.htm)and then[create an export for the file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/create-export.htm), or create an export for the file system in a pre-existing mount target.

- You can use the same export paths for the associated file systems as the previous mount target. However, the export path must be unique for each file system within the mount target.
- If you create a replacement mount target, you can use the same IP address as the previous mount target, if available. Be sure to explicitly specify the desired IP address when you create the mount target.
- If necessary,[mount the file systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingfilesystems.htm)again.

Note  
  
If a replacement mount target uses exactly the same IP address and export paths as previously existed in the deleted mount target, mounted instances reconnect automatically.
- To prevent a recurrence of this issue, ensure that sufficient unallocated IP addresses remain available in the subnet.

Cause : The mount target DNS name has an underscore.

The mount target DNS name cannot have an underscore due to the RFC 952 and RFC 1123 standards. The mount target details page might include the following message:
```

```

If you're creating a new export for a file system and creating the mount target, the export might get stuck in a Creating state.

Resolution :

- [Delete the failed mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-mount-target.htm).
- [Create a new mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/create-mount-target.htm)
