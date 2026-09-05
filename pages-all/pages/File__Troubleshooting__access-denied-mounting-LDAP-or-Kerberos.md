# Access Denied When Mounting a File System with Kerberos Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/access-denied-mounting-LDAP-or-Kerberos.htm
- Fetched: 2026-09-05 02:05 CDT

# Access Denied When Mounting a File System with Kerberos Authentication

When mounting a file system that uses Kerberos authentication, access is denied.

The mount target's[Kerberos Errors chart](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Reference/filemetrics.htm#Tips_for_Working_with_File_Storage_Metrics__mt-nfs-charts)can include the following error types:
- Kerberos no keytab
- Kerberos no key
- Kerberos key version number mismatch
- Kerberos clock skew
- Oracle Cloud Infrastructure File Storage allows up to 300 seconds for clock skew when using Kerberos. To prevent intruders from resetting system clocks and using expired tickets, ticket requests from any host whose clock isn't within 300 seconds are rejected.

The mount target's LDAP Connection Errors chart and LDAP Request Errors chart can include the following error types:
- LDAP Connection Timeout
- LDAP Connection Refused/Reset
- LDAP Name Resolution Failure
- LDAP Bind Login Failed
- LDAP Certificate Validation Failure
- Lookup Username by UID
- Lookup UID by Username
- Lookup User Groups

Perform the following tasks to help troubleshoot this issue:
- Ensure that Kerberos is[enabled on the mount target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos-oci-setup.htm#enable-kerberos).
- Configure AUTH_SYS authentication on the export and try[mounting the file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingfilesystems.htm)using`-o sec=sys`in the mount command. This test can help you find whether the issue is specific to Kerberos authentication.
- Check the validity of the Kerberos ticket on the client using the`klist -A`command.
- Review the NFS client's`rpc-gssd`daemon logs for Kerberos-related issues. Increase the log verbosity of the`rpc-gssd`daemon as needed.
- Verify that the[mount command](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/mountingfilesystems.htm)uses the fully qualified domain name and includes the correct export options. For more information, see[Mounting Kerberos-enabled File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos-oci-setup-mounting.htm).
- Check the mount target's charts and logs, if logging is enabled, for errors or Kerberos Keytab Load Success messages in the[Kerberos Errors chart](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Reference/filemetrics.htm#Tips_for_Working_with_File_Storage_Metrics__mt-nfs-charts).
- If anonymous access is disabled, verify that a user entry is present under Search Base for Users with uid, uidNumber and gidNumber attributes in the LDAP server. Verify that the group for the user exists in the Search Base for Groups with gidNumber and memberUid.

Check the mount target's charts and logs, if[logging is enabled](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Concepts/logging.htm), for errors in the[LDAP Connection Errors chart or LDAP Request Errors chart](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Reference/filemetrics.htm#Tips_for_Working_with_File_Storage_Metrics__mt-nfs-charts).

For more information, see[Mount Command Fails](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/exportpaths.htm)
