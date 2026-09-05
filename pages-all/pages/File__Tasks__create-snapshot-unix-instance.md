# Creating a Snapshot from a Unix-style Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot-unix-instance.htm
- Fetched: 2026-09-05 02:03 CDT

# Creating a Snapshot from a Unix-style Instance

You can create a snapshot from an instance that you've mounted the file system to. Snapshots are created under the root folder of the file system, in a hidden directory named`.snapshot`.

- Connect to the instance and open a command window.
- 

Navigate to the file system's hidden`.snapshot`directory. Type the following, replacing`yourmountpoint`with the name of the directory where you mounted the file system.

```

```

- 

Use the`mkdir`command to create a directory in the hidden`.snapshot`directory. The directory you create is the snapshot. Give the snapshot a name that helps you identify it. Avoid using confidential information in the snapshot name. For example:

```

```

- 

Use the`ls`command to verify that a snapshot has been created in the`.snapshot`directory.

```

```
