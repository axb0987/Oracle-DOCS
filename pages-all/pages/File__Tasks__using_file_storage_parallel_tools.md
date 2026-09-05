# Using File Storage Parallel Tools
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm
- Fetched: 2026-09-05 02:05 CDT

# Using File Storage Parallel Tools

The Parallel File Tools suite provides parallel versions of`tar`,`rm`, and`cp`. These tools can run requests on large file systems in parallel, maximizing performance for data protection operations.

The toolkit includes:
- `partar`: Use this command to create and extract tarballs in parallel.
Note  
  
The`partar`tool supports the extraction of`tar`files created in the GNU basic`tar`POSIX 1003.1-1990 format. Files created in other archive formats, such as`PAX`, are not supported.
- `parrm`: You can use this command to recursively remove a directory in parallel.
- `parcp`: Use this command to recursively copy a directory in parallel.

## Installing the Parallel File Tools

The tool suite is distributed as an RPM for Oracle Linux, Red Hat Enterprise Linux, and CentOS.

[To install Parallel File Tools on Linux](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

To install Parallel File Tools on an Oracle Linux instance:
- Open a terminal window on the destination instance.
- Type the following command:

```

```

[To install Parallel File Tools on Oracle Linux 8](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

To install Parallel File Tools on an Oracle Linux 8 instance:
- Open a terminal window on the destination instance.
- Install the Oracle Linux developer repository, if needed, by using the following command:

```

```

- Install the Parallel File Tools from the developer repository using the following command:

```

```

[To install Parallel File Tools on CentOS and Red Hat 6.x](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

To install Parallel File Tools on CentOS and Red Hat 6.x:
- Open a terminal window on the destination instance.
- Type the following command:

```

```

[To install Parallel File Tools on CentOS and Red Hat 7.x](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

- Open a terminal window on the destination instance.
- Type the following command:

```

```

## Using the Tools - Basic Examples

Here are some simple examples of how the different tools are commonly used in Oracle Cloud Infrastructure File Storage.

[To copy all files and folders from one directory to another](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

In this example,`parcp`is used to copy the directory "folder" in`/source`to`/destination`. The`-P`option is used to set the number of parallel threads you want to use.

```

```

In the following example,`parcp`is used to copy the contents of the directory "folder" in`/source`to`/destination`. The "folder" directory itself is not copied.

```

```

[To create a .TAR archive of a directory](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

The following command creates a`.tar`archive of the contents of the specified directory, and stores it as a`tarball`in the directory. In the example below, the name of the directory that is being used to create the tarball is`example`.

```

```

You can also create a tarball and send it to a different directory. In the example below, the directory being used to create the tarball is`example`. The tarball is being created in the`/test`directory.

```

```

## Using the Tools - Advanced Examples

Here are some examples of how the different tools are used in more advanced scenarios.

[To copy selected files or folders into a .TAR archive and exclude others](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

You can specify which files and folders are included when you create a`.tar`archive using`partar`. Let's say you have a directory that looks like this:
```

```

The following command creates a`.tar`archive that:
- Contains a`mydir`directory named as specified.
- Includes`File1.txt`,`File2.txt`,`File3.txt`, and`File4.txt`.
- Excludes all`.log`and`.error`files.
- Sends the`.tar`ball from`/sourcedir`to`/mnt/destinationdir`
- Extracts the`.tar`archive

```

```

Performing`ls -l`on`/mnt/destinationdir/mytar`shows that only the desired files have been copied.

```

```

When excluding a directory or file from the archive, provide only the name of the directory or file. The`--exclude`option does not support use of an absolute path. Using an absolute path in the`--exclude`option will not exclude the specified directory or files from the`.tar`archive. For example, if you need to exclude a directory called`testing`from the path of the source directory, you would specify that in a command like the following:
```

```

Note  
  
All files or directories that match the`--exclude`pattern under the path of the source directory will be excluded from the`partar`archive.

[To copy selected files or folders from one directory to another](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

You can specify which files and folders are included when you use`parcp`to copy from one directory to another. Let's say you have a directory that looks like this:

```

```

First, create a`.txt`file containing a list of files you want to exclude. In this example, it's`/home/opc/list.txt`.

The following command copies the contents from`sourcedir`to`/mnt/destinationdir`and:
- Copies`File1.txt`,`File2.txt`, and`File3.txt`.
- Excludes`File4.txt`and the`.log`and`.error`files, as listed in`/home/opc/list.txt`.

```

```

Performing`ls -l`on`/mnt/destinationdir`shows that only the desired files have been copied.

```

```

[To use PARCP as an effective alternative for RSYNC in parallel](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#)

The`--restore`option in`parcp`is similar to using the`-a -r -x`and`-H`options in`rsync`. (See[rsync(1) - Linux Man Page .) The`-P`option is used to set the number of parallel threads you want to use.

The`restore`option includes the following behavior:
- Recurse into directories
- Stop at file system boundaries
- Preserve hard links, symlinks, permissions, modification times, group, owners, and special files such as`named sockets`and`fifo`files

```

```

You can use`parcp`with the`--restore`and`--delete`options to sync files between a source and target folder. This is a good substitute for using`rsync`in parallel. As files are added or removed from the source directory, you can run this command at regular intervals to add or remove the same files from the destination directory. You can automate syncing by using this command option in a[cron job](https://linux.die.net/man/8/cron).

```

```
