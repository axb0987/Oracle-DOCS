# Cloning a File System Doesn't Replicate File System Data
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cloning_a_file_system_doesn_t_replicate_file_system_data.htm
- Fetched: 2026-09-05 02:05 CDT

# Cloning a File System Doesn't Replicate File System Data

Find out why cloning is not suitable for data replication of file systems for data protection purposes, and what to do instead.

Problem: You want to use the cloning feature to replicate a file system in another location in Oracle Cloud Infrastructure for data protection purposes.
More information: File system clones are not a data protection or replication solution. There are two reasons for this:
- Clones can only be created in the same availability domain as the parent file system. You can't specify a target location for a file system clone.
- Creating a clone doesn't replicate or move any data from the parent to the clone. Instead, the clone references the parent file system for any data they share.

Solution: You can use File Storage Parallel Tools to copy or sync your file system data between locations.
The toolkit includes:
- `partar:`Use this command to create and extract tarballs in parallel.
- `parrm:`You can use this command to recursively remove a directory in parallel.
- `parcp:`Use this command to recursively copy a directory in parallel.

See[Using File Storage Parallel Tools](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/using_file_storage_parallel_tools.htm)
