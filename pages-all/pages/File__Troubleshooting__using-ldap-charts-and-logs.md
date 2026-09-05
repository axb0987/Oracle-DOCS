# Using NFS Metrics and Logs to Troubleshoot LDAP and Kerberos Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm
- Fetched: 2026-09-05 02:07 CDT

# Using NFS Metrics and Logs to Troubleshoot LDAP and Kerberos Issues

Use an outbound connector or mount target's NFS metrics and service logs to diagnose issues with file systems that use LDAP for authorization and Kerberos for authentication.

File Storage outbound connectors and mount targets that use LDAP, or use both LDAP and Kerberos, emit metrics to help you monitor connectivity, performance, and errors. The following charts are designed to capture specific errors:
- [LDAP Connection Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-connectivity)
- [LDAP Request Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-request)
- [Kerberos Errors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__kerberos)

For complete details on File Storage metrics and charts, see[File System Metrics](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Reference/filemetrics.htm).

We recommend that you[enable NFS logs](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm)for mount targets that use LDAP or Kerberos and[set alarms](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos.htm#monitoring)on errors. See[Details for File Storage](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_file_storage.htm)for more information.

## LDAP Connection Errors

The LDAP Connection Errors chart captures the following error types:
- LDAP Connection Timeout
- LDAP Connection Refused/Reset
- LDAP Name Resolution Failure
- LDAP Bind Login Failed
- LDAP Certificate Validation Failure

For "LDAP Connection Timeout" and "LDAP Connection Refused/Reset" errors:
- Verify that[VCN security rules](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)allow communication with your LDAP and DNS servers. See[Scenario D: Mount target uses LDAP for authorization](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm#Scenario_D)
- Verify that the LDAP service is running on the customer-managed LDAP server.
Tip  
  
You can test LDAP search capability using the[`ldapsearch`](https://linux.die.net/man/1/ldapsearch)command from a Linux instance in the same subnet as the mount target. See[Testing for LDAP Schema Support](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/ldap.htm#ldap-prereqs-test-queries)for more information.
- Verify that the mount target is using an outbound connector with the correct LDAP server and LDAPS port. See[Managing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managing-outbound-connectors.htm)for more information.

For "LDAP Name Resolution Failed" errors:
- Verify that[VCN security rules](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm)allow communication with your LDAP and DNS servers. See[Scenario D: Mount target uses LDAP for authorization](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm#Scenario_D)for more information.
- Ensure that the DNS zone files on the DNS server contain A and PTR records for the LDAP server.
- If the configured DNS server is customer-managed and uses[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm), verify that the DHCP options are correct and that the mount target is in the subnet which has DHCP options set.
- Verify that the name service is reachable and running on your DNS server. You can use a DNS lookup and reverse lookup from an instance in the same subnet as your mount target.

For "LDAP Bind Login Failed" errors:

Verify that the outbound connector is using the correct Bind Distinguished Name and correct password. See[Managing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managing-outbound-connectors.htm)for more information.

For "LDAP Certificate Validation Failure" errors:

Verify that the LDAP server has a valid certificate.

## LDAP Request Errors

The LDAP Request Errors chart captures the following error types:
- Lookup Username by UID
- Lookup UID by Username
- Lookup User Groups

LDAP request errors can result in[permissions issues](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/permission-denied-ldap-lookup.htm)or[errors when mounting file systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/access-denied-mounting-LDAP-or-Kerberos.htm).

You can use the[`ldapsearch`](https://linux.die.net/man/1/ldapsearch)command from a Linux instance with connectivity to the LDAP server to verify that:
- A user entry is present under Search Base for Users with uid, uidNumber and gidNumber.
- A group entry of the user is present under Search Base for Groups with memberUid attribute.

For more information, see[Testing for LDAP Schema Support](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/ldap.htm#ldap-prereqs-test-queries).

## Kerberos Errors

The Kerberos Errors chart captures the following error types:
- Kerberos no keytab
- Kerberos no key
- Kerberos key version number mismatch
- Kerberos clock skew

For "Kerberos no keytab" errors:

Verify that you've uploaded a Kerberos keytab to OCI Vault and selected the secret when[enabling Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos-oci-setup.htm).

For "Kerberos no key" errors:

There are no keys in the keytab. For more information, see[Kerberos Keytab](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos.htm#prerequisites__keytab).

For "Kerberos key version number mismatch" errors:
- Key version numbers are used to distinguish between different keys in the same domain. This error occurs when the system can't find a`kvno`in the keytab that corresponds to the ticket. The ticket might be out-of-date or expired. For more information, see[Kerberos Keytab](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos.htm#prerequisites__keytab).
- Verify that the selected keytab secret is correct. If not, extract the[correct keytab](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos.htm#prerequisites__keytab)for the mount target principal from the KDC, then re-upload the keytab as the secret and select the new secret version.

For "Kerberos clock skew" errors:
