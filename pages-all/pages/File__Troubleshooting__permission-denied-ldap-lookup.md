# Permission Denied When Accessing Files or Directories
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/permission-denied-ldap-lookup.htm
- Fetched: 2026-09-05 02:06 CDT

# Permission Denied When Accessing Files or Directories

When accessing files or directories on a file system that uses LDAP for authorization, a "Permission Denied" error occurs.

This issue can occur when an LDAP lookup operation fails. A failure to successfully lookup the user's[secondary group memberships](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/ldap.htm#ldap-mapping)can also result in this error.

Verify that a user entry is present under Search Base for Users with uid, uidNumber and gidNumber attributes in the LDAP server. Check the mount target's charts and logs, if[logging is enabled](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Concepts/logging.htm), to see if there are errors in the[LDAP Connection Errors chart or LDAP Request Errors chart](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Reference/filemetrics.htm#Tips_for_Working_with_File_Storage_Metrics__mt-nfs-charts).

For more information, see[LDAP Connection Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-connectivity)and[LDAP Request Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-request)
