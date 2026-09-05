# Restoring from a Snapshot on a Unix-style Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/restore-from-snapshot.htm
- Fetched: 2026-09-05 02:04 CDT

# Restoring from a Snapshot on a Unix-style Instance

Learn how to restore a File Storage file system from a snapshot on the instance.

Snapshots are created under the root folder of your file system, in a hidden directory named`.snapshot`. You can restore a file within the snapshot, or an entire snapshot using the`cp`command. Use the`-r`option when restoring a snapshot that contains subdirectories.

For example:

```

```

Optionally, you can use`rsync`,`tar`, or another tool that supports NFSv3 to copy your data to another remote location. For optimal performance, use the[Parallel File Tools](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#install_par_tools).

For example:

```

```

To create a new file system from a snapshot, see[Cloning a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm)
