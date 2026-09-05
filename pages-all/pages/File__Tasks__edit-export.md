# Editing an Export and Export Options
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-export.htm
- Fetched: 2026-09-05 02:03 CDT

# Editing an Export and Export Options

Update a File Storage export and its options.

To be sure you be sure that you edit the correct export, check the following details:
- 

The export path : This[path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm)uniquely identifies the file system within the mount target. No two exports in a mount target can have the same export path, even if the exports are for the same file system.
Note  
  
Export paths can't be edited after the export is created. To use a different export path, you must create a new export with the preferred path. Optionally, you can then delete the export with the old path.
- The mount target name : File systems can be exported through more than one mount target. Be sure to select the export for the correct mount target.

For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/exportoptions.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-export.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-export.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-export.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- Select the compartment that has the export you want to work with.
- On the file systems details page, select the name of the file system that has the export you want to edit, then select Exports .
- On the Exports page, select the export you want to edit.
- On the export's details page, select NFS client Export options and then select Edit options .
- In the Edit options panel, update the following information and
- Change any of the export option entries in the list.
- Select Add option to create a new export option entry.

For more information, see[NFS Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#Export).
- Select Update .
- 

Use the[`fs export update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/update.html)command and include the`--export-options`parameter to update export options:

```

```

If you don't want a file system to be visible to any clients through this export, you can set`source`to an empty value. For example:

```

```

Important  
  
Updates to`--export-options`will replace any existing values.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/UpdateExport)operation to update an export and its options.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
