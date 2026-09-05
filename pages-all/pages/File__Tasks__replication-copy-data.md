# Using Replication for Data Transfer
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-copy-data.htm
- Fetched: 2026-09-05 02:04 CDT

# Using Replication for Data Transfer

Learn how to use File Storage replication to copy data from one availability domain to another.

You can use replication for a one-time data transfer between availability domains or regions. For example, to move data from File System A to File System B:
- [Create a file system (File System B) in the availability domain or region where you want to copy data to. Be sure that it's a targetable (unexported) file system.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)
- [Create a replication in the source file system (File System A) and specify the target as File System B.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm)
- Wait for the replication cycle to complete and bring File System B up-to-date with File System A. You can check that the file systems are in sync by verifying that the initial replication snapshot appears in both File System A and File System B.
- If the source and destination must be identical, which is most often the case for data migration scenarios, stop writing to the source file system and[delete its exports](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm).
- [Delete the replication resource using the "replicate and delete" or`one_more_cycle`method.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
- (Optional)[Create an export in File System B.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)
- (Optional)[Mount File System B so applications can access it.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)
