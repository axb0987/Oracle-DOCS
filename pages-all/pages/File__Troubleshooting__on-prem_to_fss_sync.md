# On-Premises Transfers to File Storage Are Slow
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/on-prem_to_fss_sync.htm
- Fetched: 2026-09-05 02:06 CDT

# On-Premises Transfers to File Storage Are Slow

When a File Storage file system is directly mounted on an on-premises server, transferring files from the on-premises server to OCI File Storage is slow.

Cause: Directly mounting a File Storage file system on an on-premises instance is very slow because the NFS protocol is chatty over the internet.

Solution: Use instance-to-instance streaming for on-premises to OCI File Storage transfers using parallel`rsync`tools such as`fpsync`. For example:
- If needed,[create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)in the same subnet as the existing File Storage mount target. Then set security rules and export options so that you can[mount the file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingfilesystems.htm)from the instance.
- Add the on-premises root user's SSH public key into the OCI instance's`~/.ssh/authorized_keys`file. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- 

Linux users can download`fpsync`from a yum repository. The commands differ depending on the version of Linux.
- 

Download from the repository.

Linux 8 users can download the tool using the following command:

```

```

Linux 9 users can download the tool using the following command:

```

```

- Install the tool:

```

```

- 

As the root user of the on-premises instance, run the transfer to OCI File Storage using the new OCI instance:
```

```

Consider the following when using the`fpsync`command:
- Ensure that the ${src} and ${dest} have a trailing`/`to do a content-only copy of the source.
- When using a File Storage mount target as the source, exclude the`.snapshot`directory, otherwise the copy time increases significantly.
- Because the current`fpsync`release doesn't accept the`rsync`option`-a`, the command uses`-lpgtoD`.

For more information and options, see the[`fpsync`man page](http://manpages.ubuntu.com/manpages/xenial/man1/fpsync.1.html)
