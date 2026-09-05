# Copy Fails with "Not Enough Free Space" Error
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/win-not-enough-free-space.htm
- Fetched: 2026-09-05 02:07 CDT

# Copy Fails with "Not Enough Free Space" Error

Attempts to copy data on a File Storage drive mounted on a Windows machine fail with a "There is not enough space" error message.

Cause: Windows does a check for free space for copy and paste operations on the same machine. If the mount target's[Reported Size is set to a value lesser than the utilization of file systems mounted through the mount target, this error can occur.

Solution: The File Storage service does not have space limitation on storage, and a mount target's Reported Size is a soft limit. Windows uses the`fsstat`call to determine free space before attempting to write the data, and the reply to that`fsstat`call uses the Reported Size as the total size.

By default, File Storage reports file system capacity as 8589934592 gibibytes (GiB), but it is possible to specify a lower value. If the value was modified,[reset it](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/change-file-system-size.htm)
