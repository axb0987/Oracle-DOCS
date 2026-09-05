# Mount Target Creation Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/mounttargetlimit.htm
- Fetched: 2026-09-05 02:06 CDT

# Mount Target Creation Fails

File Storage mount target creation can fail for various reasons.

Some of these reasons include:
- 

You've exceeded your mount target limit.

Each availability domain is limited to two mount targets by default. If you create both a file system and a mount target at the same time, it is possible for the file system to be successfully created but the mount target creation to fail because of this limitation. This limitation can be avoided by reusing a previously created mount target for new file systems. You can reuse a single mount target to make as many file systems available on the network as you wish.
- To reuse a mount target when creating a new file system, select Select an Existing Mount Target . The workflow creates a new export for the file system in the existing mount target of your choice.
- To reuse a mount target for an existing file system, you must manually create a new export for the file system in the mount target. For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/exportoptions.htm). See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.
- There aren't enough available IP addresses in your subnet.

Each mount target requires three internal IP addresses in the subnet to function:
- Two of the IP addresses are used during mount target creation. The third IP address must remain available for the mount target to use for high availability failover.
- The third IP address is used to create a new VNIC for the mount target during failover. The original primary IP address is retained.
- The File Storage service doesn't "reserve" the third IP address required for high availability failover.
- Use care to ensure that enough unallocated IP addresses remain available for your mount targets to use during failover.
-
