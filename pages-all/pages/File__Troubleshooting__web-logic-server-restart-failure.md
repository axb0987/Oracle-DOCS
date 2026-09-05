# WebLogic Server Doesn't Restart After Failure
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/web-logic-server-restart-failure.htm
- Fetched: 2026-09-05 02:07 CDT

# WebLogic Server Doesn't Restart After Failure

After a node failure, WebLogic Server fails to start.

The WebLogic service log contains an error message similar to the following:
```

```

Cause 1: NFSv3 servers don't include a lock lease feature, so lock states aren't stored and locks can't be released after the node failure.

Solution 1: Request removal of file locks. For more information, see[Removing File Locks from a Host that is No Longer Available](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/filelocks.htm).

Cause 2: Sometimes, the`[](https://man7.org/linux/man-pages/man8/statd.8.html)rpc-statd`service, which is needed for NFSv3 locking, is in an unhealthy state after the server failure. This can be verified by running a sample lock test using`fcntl`module. For example:
```

```

Solution 2: Restart the`rpc-statd`service.
- 

Open a terminal window on the instance and use the following commands as the root user:
```

```

- Verify that the`fcntl`sample lock test completes without error.
- Start the WebLogic server.

Cause 3: NFSv3 doesn't track lock owners. So, NFS holds the lock indefinitely if a lock owner fails. After a node failure, a WebLogic restart attempt can't acquire a lock.

Solution 3: This is a general NFSv3 limitation. Immediate mitigation and long-term design considerations are provided in WebLogic's documentation. For more information, see[Verifying Server Restart Behavior](https://docs.oracle.com/en/middleware/fusion-middleware/12.2.1.3/ashia/jms-and-jta-high-availability.html#GUID-7A2C6451-A293-4398-BE0E-F10BC8C8B2AE)
