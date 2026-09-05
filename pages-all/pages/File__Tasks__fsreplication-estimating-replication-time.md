# Estimating Replication Time
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm
- Fetched: 2026-09-05 02:03 CDT

# Estimating Replication Time

When you create a replication for a file system, the process includes an initial sync of the data from the source file system to the target file system. Depending on the amount of data written to the file system, this sync can take hours. To help plan a replication, File Storage provides a tool you can use to estimate how long the initial sync could take.
Caution  
  
The replication estimator uses historical data of the source file system to provide its estimates. If the file system is new, the estimate might not be accurate.

The replication time estimator analyzes the source file system and provides the following details:

Field Description
Replication Supported Whether this file system supports replication.
Minimum Supported Replication Interval in Minutes The minimum supported replication interval for specified file system in minutes. A value of`-1`indicates that the system can't provide an accurate estimate or replication is unsupported.
Estimated Base Copy Time in Minutes The approximate time required for the base sync between source and target to finish. A value of`-1`indicates that the system can't provide an accurate estimate or replication is unsupported.
Detected Change Rate in MBps The rate of change on source file system which was used to provide the default estimate in megabytes per second. A value of`-1`indicates that the system can't provide an accurate estimate or replication is unsupported.
Change Rate in MBps The rate of change on source file system which was used to provide the estimate in megabytes per second.
Allowed Target Regions The regions that support a replication target for this file system. If the file system doesn't support replication, this field is empty. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm#limitations-and-considerations)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Replications .
- From the Actions menu, Select Replication estimator .
- (Optional) In the Replication estimator panel , update the Change rate in MBps to see how the file system's rate of change affects replication time.
- Select Calculate .
- 

Use the[`fs file-system estimate-replication`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/estimate-replication.html)command and required parameters to estimate the replication time for source the file system:

```

```

For example:
```

```

Note  
  
If you don't provide the optional`change-rate`parameter, the tool uses[historical data](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm)to create the estimate.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`EstimateReplication`](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/EstimateReplication)operation to estimate the replication time for source the file system.
Note  
  
If you don't provide the optional`changeRateInMBps`parameter, the tool uses[historical data](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm)to create the estimate.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
