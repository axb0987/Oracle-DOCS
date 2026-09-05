# Can't Delete a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cannot_delete_a_file_system.htm
- Fetched: 2026-09-05 02:05 CDT

# Can't Delete a File System

Deleting a file system fails.

Cause 1: The file system has exports in one or more mount targets. Before you can delete a file system, all of its exports must first be deleted.

Solution 1: Delete all of the file system's exports, then delete the file system. See[Deleting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-file-system.htm)for instructions.

Cause 2: The file system is the root of a clone tree. Before you can delete the root of a clone tree, all of its descendant clones must first be deleted.
Solution 2: Locate and delete all of the file system's descendant clones:
- Visit the file system Details page and note down the file system OCID. See[Getting a File System's Details](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/get-file-system-details.htm)for more information.
- Use the Command Line Interface (CLI) to[list all of the file system's clones](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/find-clones.htm). Use the following command, and replace &lt;parent_filesystem_id&gt; with the file system OCID you obtained in step 1. For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

```

```

- Delete all of the file systems in the resulting output list.
- Delete the parent file system.

You can also use the API to locate all of the file systems with a specified parent. For more information, see[ListFileSystems](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystemSummary/ListFileSystems).

Cause 3: Clones or siblings of the file system are currently being deleted.

Solution 3 : Wait until the clones or siblings have all finished deleting, and then try again.

Cause 4: The file system is currently being cloned.

Solution 4: Wait until the clone operation succeeds, and then try again.

For general information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm)and[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingfilesystems.htm)
