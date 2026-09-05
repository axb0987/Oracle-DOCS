# Metadata Operations Such as ls -l, du, or find are Slow
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/SlowLS.htm
- Fetched: 2026-09-05 02:05 CDT

# Metadata Operations Such as ls -l, du, or find are Slow

When a directory exceeds 100,000 files, metadata operations such as`ls -l`,`du`, or`find`are slow.

Generally,`ls -l`against a File Storage directory with 100,000 files is expected to complete in &lt;= 10 seconds. Directory size doesn't significantly affect File Storage write throughput. If you see read/write slowness, ensure that you're not using`rsize`and`wsize`NFS mount options with a value of less than 1048576. As a best practice, don't specify`rsize`and`wsize`mount options, leave them at their default value of 1048576.

Cause: Directory scanning operations such as`ls`,`du`,`find`, and`rsync`on a directory containing 100,000 files takes longer in File Storage.

Solutions:
- 

Redistribute files to subdirectories instead of storing a large volume of files in a single directory. We recommended using subdirectories to keep directory sizes under 100,000 files.
Tip  
  
Keeping directory sizes small by using subdirectories is a best practice for File Storage.
- Use`ls -ld`or`stat`instead of`ls -l`. These operations are much quicker on large directories than`ls -l`.

For example:

```

```

- 

Sometimes, an NFS client issue could cause directory scanning operations to enter into a loop and lead to an increase in scanning time. This issue affected the following Oracle Linux versions:
- Oracle Linux 7 with Unbreakable Enterprise Kernel (UEK) versions earlier than 4.14.35-1902.301.1

Oracle Linux 7 users can run the`uname -a`command to check the version of UEK. If the UEK version is earlier than 4.14.35-1902.301.1, upgrade to a later kernel version. The patch addressing this behavior was made available on April 17, 2020 and can be installed with Oracle Ksplice.

Oracle Ksplice lets you apply important security updates and other critical kernel updates without a reboot. Oracle Ksplice must be installed on the instance. After you install Ksplice, you can install available Ksplice patches. See[Oracle Ksplice](https://docs.oracle.com/iaas/oracle-linux/ksplice/index.htm)for instructions.

After you install the patch, you can verify the effective kernel version. Ksplice`uptrack`doesn't change the output of the`uname`command.`uname`continues to reflect the version of the kernel the instance was booted into.

Instead, use`uptrack-uname`to see what effective kernel an instance is running.`uptrack-uname`has the same format as`uname`and supports the common`uname`flags, including`-r`and`-a`.

For example:

```

```

- 

Directory scanning operations invoke the`READDIRPLUS`NFS call which is expensive when the directory contains many files. Instances can disable`READDIRPLUS`calls by using the`nordirplus`option when mounting. To disable the`READDIRPLUS`NFS operations on the instance:
- Open a terminal window on the instance.
- 

Unmount the file system with the`umount`command. For example:

```

```

- 

Remount the file system, and include the`-o nordirplus`option to disable`READDIRPLUS`. For example:

```

```
