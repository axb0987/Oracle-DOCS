# Increasing File Storage Throughput
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/increasing-throughput.htm
- Fetched: 2026-09-05 02:06 CDT

# Increasing File Storage Throughput

Learn how to increase the throughput of File Storage file systems.

File systems with heavy read/write workloads might experience throughput saturation reflected in[its metrics](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Reference/filemetrics.htm).

Solution : A file system's performance is mainly determined by its[mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingmounttargets.htm). A file system can be exported through more than one mount target if more throughput is needed.

As an example, a particular file system's metrics might report read/write throughput of about 750 MBps. That file system is mounted on ten instances and accessed concurrently. If you use two mount targets for the same file system, and each mount target is used by five instances, the file system's throughput increases to about 1500 MBps.
Note  
  

Increasing throughput by using multiple mount targets can result in a slight increase in latency. When a file system is exported through more than one mount target, File Storage's NFS server cache is disabled. Disabling this cache can impact metadata heavy operations, but read/write operations benefit from the increased throughput without negative impact.

For more details, see the[File Storage service performance guide](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/file-storage-performance-guide.pdf)
