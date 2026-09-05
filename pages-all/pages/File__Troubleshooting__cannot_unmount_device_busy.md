# Cannot Unmount a File System: Device is Busy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cannot_unmount_device_busy.htm
- Fetched: 2026-09-05 02:05 CDT

# Cannot Unmount a File System: Device is Busy

Unmounting (`umount`) fails with a message:`device is busy`.

For example:
```

```

Cause 1: You're attempting to run the`umount`command from within the`mountpoint`directory.

Solution 1: Move to a directory outside the file system mount point, and retry the`umount`command.

Cause 2: An abrupt disconnect from the file system's mount target occurred.
More Information: An NFS message similar to the example below is displayed:
```

```

Solution 2:
- Use the`fuser`or`lsof`operation to find the process that has locked the file and note its ID.

See[lsof(8) - Linux Man Page for information about how to use`lsof`.

See[fuser(1) - Linux Man Page for information about how to use`fuser`.
- After you've identified the process that has locked the file, stop the process using the`kill`command. For example:
```

```

See[kill(1) - Linux Man Page for more information.
- Retry the`umount`
