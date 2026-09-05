# File and Folder Names That Use Non-ANSI Characters are Garbled
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/windows-garbled-non-ANSI-names.htm
- Fetched: 2026-09-05 02:07 CDT

# File and Folder Names That Use Non-ANSI Characters are Garbled

Learn how to troubleshoot an issue where file and folder names that use non-ANSI character sets are garbled when the file system is mounted in Windows.

Cause: Currently, a limitation exists when viewing non-ANSI characters in Windows NFS client v.3. File Storage uses NFS v.3 with the`lang=ANSI`option by default. Characters in other encodings don't appear correctly.

Solution: Use the`-o lang`option to specify the character encoding of the file system. See the[mount documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mount)for a list of acceptable values. For example:

```

```

The following command mounts the file system with lang=EUC-JP to display Japanese characters correctly:
```

```

Limitations and considerations for this solution:
- This solution only works with Windows operating systems. Operating systems such as Linux use UTF-8 encoding.
- This solution can cause issues with Universal Naming Convention (UNC) paths. For example,`\\ server_name \ folder_name \ file_name`
