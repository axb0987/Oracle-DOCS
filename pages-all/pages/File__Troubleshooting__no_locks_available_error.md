# Operations on a File System Fail With Error: 37: No Locks Available
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/no_locks_available_error.htm
- Fetched: 2026-09-05 02:06 CDT

# Operations on a File System Fail With Error: 37: No Locks Available

Operations on the file system sometimes fail with`Linux-x86_64 Error: 37: No locks available`.

Cause: The`[](https://man7.org/linux/man-pages/man8/statd.8.html)rpc-statd`service and`lockd`daemon are not running on the client.
Solution: Enable and start the`rpc-statd`service to initialize the`lockd`service:
- Open a terminal window on the instance and use the following commands to enable the`rpc-statd`service:
```

```
