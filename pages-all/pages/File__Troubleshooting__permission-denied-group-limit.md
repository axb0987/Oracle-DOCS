# Access to File System Denied to Certain Users
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/permission-denied-group-limit.htm
- Fetched: 2026-09-05 02:06 CDT

# Access to File System Denied to Certain Users

A user is unable to access a file or directory even though the user is a member of a group that has been given access to the file or directory.

Cause: The user is a member of more than 16 groups and the group with access to the file or directory is not within the first 16 groups. NFS protocol is used to access File Storage. NFS clients use the AUTH_SYS authentication scheme, which has a limitation of 16 groups.

On Linux, you can run the`id`command to verify if the user is member of more than 16 groups.

Workaround:[Use LDAP](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/ldap.htm)to[map groups](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/ldap.htm#ldap-mapping)
