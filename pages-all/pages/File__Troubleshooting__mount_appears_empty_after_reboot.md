# File System Appears Empty After Instance Reboot
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/mount_appears_empty_after_reboot.htm
- Fetched: 2026-09-05 02:06 CDT

# File System Appears Empty After Instance Reboot

After a rebooting an instance, the file system appears empty.

Cause: The file system was not automatically remounted after the reboot.

More Information: The`rpcbind`and`nfslock`services don't automatically start at reboot by default.
Solution:
- Add the file system to the instance`/etc/fstab`file, so the file system is automatically remounted after reboot.
- See[To auto-mount a file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingunixstyleos.htm#CLIautomount)for instructions.
- Set the`rpcbind`and`nfslock`services to start automatically on every reboot.
- Use the following commands to start the`rpcbind`and`nfslock`services:
```

```

- Verify that the`rpcbind`and`nfslock`services are running:
```

```

- Enable the services to start automatically at reboot:
```

```
