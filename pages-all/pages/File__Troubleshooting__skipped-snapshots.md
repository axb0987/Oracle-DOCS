# Scheduled Policy-Based Snapshot is Skipped
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/skipped-snapshots.htm
- Fetched: 2026-09-05 02:06 CDT

# Scheduled Policy-Based Snapshot is Skipped

Learn why a File Storage policy-based snapshot scheduled to be created could be skipped.

Cause 1 :

A snapshot policy contains more than one schedule. At least two schedules would create a snapshot at the same time.

When multiple schedules within a snapshot policy would create a snapshot at the same time, the File Storage service creates only a single snapshot. The schedule with the longest configured[retention duration](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/snapshot-policies-and-schedules.htm#snapshot-policies-and-schedules__retention)is prioritized.

Cause 2 :
