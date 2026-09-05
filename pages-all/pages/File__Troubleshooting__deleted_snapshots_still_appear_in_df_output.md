# Deleted Snapshots Still Appear in DF Output
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/deleted_snapshots_still_appear_in_df_output.htm
- Fetched: 2026-09-05 02:05 CDT

# Deleted Snapshots Still Appear in DF Output

Learn how to resolve an issue where deleted snapshots still appear in DF output with "stale file handle".

Symptom: Deleted snapshots still appear in`df`output with the message`stale file handle`.

Cause: When you use an NFSv3 client to perform operations such as`ls`,`du`, or`find`on the snapshot directory, the service automatically exports the directory. The client uses`nfs_d_automount()`to detect and mount the directory. After the directory is detected and mounted the first time, the client mounts the directory automatically.

If you then delete the snapshot, the mount becomes disconnected. The client still holds an active reference to the snapshot, but can no longer access the snapshot itself, so it reports`stale file handle`.

Solution: Manually unmount the snapshot. For example:
```

```

If the unmount command fails with the message`device busy`, use the`-f`flag to force the command and ignore the stale file handles. For example:
```

```
