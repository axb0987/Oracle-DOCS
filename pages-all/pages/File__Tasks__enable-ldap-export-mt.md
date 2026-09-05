# Enabling Secondary Group Lists with LDAP
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/enable-ldap-export-mt.htm
- Fetched: 2026-09-05 02:03 CDT

# Enabling Secondary Group Lists with LDAP

Enable the lookup of secondary group lists from an LDAP server for a File Storage export.
Using secondary group lists requires additional configuration and several prerequisites. For more information, see[Using LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/enable-ldap-export-mt.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/enable-ldap-export-mt.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/enable-ldap-export-mt.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- Select the compartment that has the export you want to work with.
- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select Exports .
- Select the export that you want to update.
- On the export's details page, select Edit next to Use LDAP for group list .
- In the Edit Use LDAP for group list dialog box, turn on Use LDAP for group list and select Save .
- 

Use the[`fs export update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/update.html)command and include the`--is-idmap-groups-for-sys-auth`parameter to update an export to use LDAP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/UpdateExport)operation with the`isIdmapGroupsForSysAuth`parameter to update an export.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
