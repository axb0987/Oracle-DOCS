# Setting the Audit Retention Period
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/config-audit-retention.htm
- Fetched: 2026-09-05 02:20 CDT

# Setting the Audit Retention Period

Set the retention period for audit logs for an identity domain in IAM.

- On the Domain settings page, find the setting you want to change. If you need help finding the domain settings page, see[Listing Domain Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/list-domain-settings.htm).
- Under Audit, select Configure audit retention period . The tenancy purges the audit data for all the users, based on the interval set here.

Note  
  

As an administrator, when you delete a user, you can manually purge the audit data of that user by entering the user's OCID in Enter the OCID of the deleted user to purge audit data and then selecting Purge . All the audit data of that user is permanently deleted from the tenancy.

Audit events accessed by the AuditEvents API are available for 14 days. To see events beyond 14 days (maximum 365 days), use the OCI Audit service. See[Overview of Audit](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)and[Audit Log Retention Period](https://docs.oracle.com/iaas/Content/Audit/Tasks/settingretentionperiod.htm).
-
