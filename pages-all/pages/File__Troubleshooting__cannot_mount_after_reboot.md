# Mount Fails With USE -NOLOCK Error After Instance Reboot
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cannot_mount_after_reboot.htm
- Fetched: 2026-09-05 02:05 CDT

# Mount Fails With USE -NOLOCK Error After Instance Reboot

Cannot re-mount a file system after rebooting the instance. Manual re-mount fails with`use -nolock`error.

Cause: The NFS client services aren't running on the instance.

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
