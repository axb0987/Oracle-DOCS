# Size Mismatch Between Clone and Parent
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/clone-parent-size-mismatch.htm
- Fetched: 2026-09-05 02:05 CDT

# Size Mismatch Between Clone and Parent

A new clone differs in size from the parent file system.

A clone is metered only for its metadata and incremental changes made to its data. Its utilization represents only the differentiated data unique to the clone. You're not metered more than once for data shared between a file system and its clone. For more information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm)and[Metering and Billing](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm#Metering_and_Billing).

If the parent file system is no longer needed, you can free up space by:
- [Detaching the clone](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/detach-clone.htm)from the parent to create an independent file system. After the clone is detached, its size is updated and it's metered and billed independently.
- [Deleting the parent file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-file-system.htm)
