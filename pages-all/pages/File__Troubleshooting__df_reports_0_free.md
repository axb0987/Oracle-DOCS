# DF Operation Reports File System as 100% Used (0% Free)
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/df_reports_0_free.htm
- Fetched: 2026-09-05 02:05 CDT

# DF Operation Reports File System as 100% Used (0% Free)

Running the`df`command on a mounted file system unexpectedly reports zero available space (100% used, 0% free), rather than a realistic value.

Cause: The mount target that exports the file system has its Reported Size value set incorrectly.
Solution: Reset the mount target's Reported Size (GiB) to the default value of 8589934592 GiB. For instructions, see[Setting a File System's Reported Size](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/change-file-system-size.htm).
Important
