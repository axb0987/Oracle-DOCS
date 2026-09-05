# RSYNC is Slow When Copying Files
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/rsync_is_slow_copying_files.htm
- Fetched: 2026-09-05 02:06 CDT

# RSYNC is Slow When Copying Files

The`rsync`operation runs very slowly against a file system.

Cause:`rsync`is a serial operation, so it's slow when copying a large file system, especially if snapshots are included in the process.

Solution: Use one of the following alternatives:
- GNU Parallel to run`rsync`in parallel. For example:

```

```

For more information, see[GNU Parallel - GNU Project](https://www.gnu.org/software/parallel/).
- File Storage Parallel Tools

For more information and examples, see[Using File Storage Parallel Tools](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/using_file_storage_parallel_tools.htm).
- The`find`command with the`xargs`option. For example:

```

```

See[find(1) - Linux Man Page and[xargs(1) - Linux Man Page for more information.
- If you're using`rsync`to copy files from one region to another, see[Copying Files from Region to Region Using RSYNC or FPSYNC is Slow](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/rsync_slow_across_regions.htm)
