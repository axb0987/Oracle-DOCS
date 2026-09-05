# Mounting a Kerberos-enabled Export Takes a Long Time to Complete
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/kerberos-enabled-mounting-slow.htm
- Fetched: 2026-09-05 02:06 CDT

# Mounting a Kerberos-enabled Export Takes a Long Time to Complete

When mounting a Kerberos-enabled export, the process takes longer than expected to complete.

Sometimes, if there are recent LDAP server related changes, it might take up to six minutes to reflect in a mount target.

This issue can also occur because of LDAP connection errors or because LDAP queries are taking a long time to complete. For more information, see[LDAP Connection Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-connectivity)and[LDAP Request Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-request)
