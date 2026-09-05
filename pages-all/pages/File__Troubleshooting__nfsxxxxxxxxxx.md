# Presence of .nfsxxxxxxxxxx Files
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/nfsxxxxxxxxxx.htm
- Fetched: 2026-09-05 02:06 CDT

# Presence of .nfsxxxxxxxxxx Files

When looking at the contents of a file system, you see files with a`.nfsxxxxxxxxxx`extension.

Cause : Stale files are represented as`.nfsxxxxxxxxxx`files. Often, this means that there was a file opened by a process in an NFS client, but then some other process removed the file or moved it to a different location. The process that deleted or moved the file could be a process in the same instance, or a different instance.

Resolution :

- To find out which instance's process removed or modified the original file, run the`lsof .nfsxxxxxxxxxx`command on all the Linux instances where the file system is mounted.

The output contains the program and the process ID holding up the file. If the output in any of the instances shows that the`.nfsxxxxxxxxxx`file isn't required by the holding process, it may be removed.
- (Optional) If the process is obsolete, you can terminate it.
- Remove the`.nfsxxxxxxxxxx`file.

Note  
  
If a new`.nfsxxxxxxxxxx`
