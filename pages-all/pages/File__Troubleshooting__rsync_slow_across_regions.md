# Copying Files from Region to Region Using RSYNC or FPSYNC is Slow
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/rsync_slow_across_regions.htm
- Fetched: 2026-09-05 02:06 CDT

# Copying Files from Region to Region Using RSYNC or FPSYNC is Slow

Using`rsync`or`fpsync`to copy data from a file system in one region to a file system in another region results in slow progress.

Cause: NFS traffic from region to region is generally expensive. File copies between two NFS servers, each in a different region, can take time.

Solution: Instead of using`rsync`or`fpsync`to copy data between mounted file systems in different regions, use`fpsync`and instance-to-instance streaming.

The`fpsync`tool is a parallel wrapper of`rsync`. To install`fpsync`, enable the Oracle Linux developer repository, which includes the`fpsync`utility, on an OCI instance using a command such as the following:

```

```

```

```

Note  
  
The command differs based on the version of Oracle Linux in use.

A standard command such as this copies data:
```

```

After installing the tool, use instance-to-instance streaming and a command such as this:
```

```

For more information and options, see the[`fpsync`man page](http://manpages.ubuntu.com/manpages/xenial/man1/fpsync.1.html).

[Performance Comparison](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/rsync_slow_across_regions.htm#)

An example showing the performance difference between the two approaches follows:
```

```
