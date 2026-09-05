# Access to File System is Denied Due to Stale File Handle
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/stale_file_handle.htm
- Fetched: 2026-09-05 02:06 CDT

# Access to File System is Denied Due to Stale File Handle

Access to a file system fails with a message:`stale file handle`.

For example:
```

```

Cause: This issue happens when an application opens or creates a file, deletes and closes it, and then attempts to access or delete the same file again.

Solution1: Restart the application.
Solution 2: If Solution 1 doesn't solve the issue, unmount and re-mount the file system. This might require using the`-f`flag in the`umount`command. For example:
```

```

Note  
  
If the unmount command fails with the message`device busy`, see[Cannot Unmount a File System: Device is Busy](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cannot_unmount_device_busy.htm)for a solution to this problem.
