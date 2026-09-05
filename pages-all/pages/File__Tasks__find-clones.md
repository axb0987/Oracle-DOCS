# Finding and Listing Clones
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/find-clones.htm
- Fetched: 2026-09-05 02:03 CDT

# Finding and Listing Clones

Find the File Storage clones created from a specific source snapshot or parent file system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/find-clones.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/find-clones.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/find-clones.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Clones .

You can also use Search to find the clones created from a source snapshot or parent file system. In the top navigation bar, select Search for resources, services, documentation, and Marketplace , and then select Advanced resource query . This query retrieves all clones for specific snapshot:

```

```

This query retrieves all clones for a parent file system:

```

```

For more information about using search to find resources, see[Overview of Search](https://docs.oracle.com/iaas/Content/Search/Concepts/queryoverview.htm)and[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm).
- 

Use the[`fs file-system list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/list.html)command and include either`--source-snapshot-id`or`--parent-file-system-id`to find clones created from a snapshot or file system.

An example using`--source-snapshot-id`:

```

```

An example using`--parent-file-system-id`:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListFileSystems](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystemSummary/ListFileSystems)operation with the`sourceSnapshotId`or`parentFileSystemId`parameter to find clones.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
