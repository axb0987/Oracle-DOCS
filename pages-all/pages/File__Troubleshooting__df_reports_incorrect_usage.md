# DF Operation and Utilization Values Don't Reflect Recent File Deletions
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/df_reports_incorrect_usage.htm
- Fetched: 2026-09-05 02:05 CDT

# DF Operation and Utilization Values Don't Reflect Recent File Deletions

You recently deleted files from a file system to reclaim space, but running the`df`command on the mounted file system doesn't reflect these updates and the command continues to report incorrect usage.

The Console reports a Utilization value for the file system that's incorrect. Running the`du`command shows the correct usage.

Cause:[Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingsnapshots.htm),[clones](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm), or both, are present on the file system.

Solution: Snapshots and clones contribute to metered usage. Deleted files are still referenced by snapshots and clones.
- Check to see if the file system has snapshots. For more information, see[Listing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/list-snapshots.htm).
- To reclaim space,[delete snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-snapshot.htm)after performing necessary backups.
- Check to see if the file system has any clones. For more information, see[Finding and Listing Clones](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/find-clones.htm).
- To reclaim space, either[detach clones](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/detach-clone.htm)or[delete the cloned file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-file-system.htm).

See[Metering and Service Cost](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Concepts/FSutilization.htm#Metering_and_Service_Cost)and[Using DF and DU Commands](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Concepts/FSutilization.htm#Using)
