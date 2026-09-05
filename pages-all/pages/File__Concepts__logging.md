# Logging for File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/logging.htm
- Fetched: 2026-09-05 02:02 CDT

# Logging for File Storage

Use this information to manage logs for File Storage resources.
Important  
  
Audit and mount target logs don't capture OS-level operations, such as file or folder deletion on a file system mounted on an instance.

## Audit Logs

Use audit logs to capture any of the following operations performed on a File Storage resource using the Console, CLI, or API:
- GET
- POST
- PUT
- PATCH
- DELETE

For more information, see[Audit Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm).

## Mount Target Logs

Only Kerberos-enabled mount targets use the OCI Logging service for Kerberos/LDAP related errors.

To enable logging, see[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm). No additional policies are required to enable logging. You only need to have permission to configure the mount target. For more information, see[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).

See[Details for File Storage](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_file_storage.htm)for example File Storage log entries and[Using NFS Metrics and Logs to Troubleshoot LDAP and Kerberos Issues](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Troubleshooting/using-ldap-charts-and-logs.htm)for more information about Kerberos-related error messages.
Note  
  
Logging is an option in the File Storage service. Standard limits, restrictions, and rates apply when enabling the logging features. See[Oracle Cloud Infrastructure Logging](https://www.oracle.com/devops/logging/)
