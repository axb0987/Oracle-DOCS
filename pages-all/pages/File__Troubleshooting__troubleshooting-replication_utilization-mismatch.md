# Target and Source File Systems Do Not Report the Same Utilization
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/troubleshooting-replication_utilization-mismatch.htm
- Fetched: 2026-09-05 02:06 CDT

# Target and Source File Systems Do Not Report the Same Utilization

The target file system does not report the same utilization as the source file system even though the replication progress indicator shows 100%.

It can take the File Storage service up to one hour to report the correct usage.

Wait at least an hour before checking the metrics again.
Note  
  
The size of the target file system will be the size of the source file system at the time of the creation of the last replication snapshot.

If the problem persists, contact[contact support](https://www.oracle.com/support/cloud.html#infrastructure-tab)
