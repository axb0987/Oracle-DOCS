# Activity Auditing Overview
- Source: https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#dcoc-content-body)

# Activity Auditing Overview

Activity Auditing lets you collect audit data from your target databases so that you can monitor database activities.

## About Activity Auditing

You entrust your databases to your database administrators, account owners, and end users. However, it's important to monitor database activity regularly because accounts are always at risk for being compromised or misused. Activity Auditing in Oracle Data Safe helps to ensure accountability and improve regulatory compliance.

With Activity Auditing, you can collect and retain audit records per industry and regulatory compliance requirements and monitor user activities on Oracle databases. For example, you can audit access to sensitive data, security-relevant events, administrator and user activities, activities recommended by compliance regulations like the Center for Internet Security (CIS), and activities defined by your own organization. You can collect up to one million audit records per month per target database in Oracle Data Safe for free.

## Activity Auditing Landing Page

By default, the Activity Auditing landing page shows you a summary of audit events for the past one week for all target databases, in the form of charts and tables. This gives you a broad overview of audit events across all target databases monitored by Oracle Data Safe. You can modify the filters set on target databases, target database groups, and time period as needed. The charts and tables are immediately updated.

The All activity chart shows you the total count of audit events on all or selected target databases for the specified time period.

The Failed login activity chart shows you the number of failed logins on all or selected target databases for the specified time period.

The Audit trails chart shows you the number of audit trails in each state (running, stopped, not started, and needs attention) in the selected compartment.

The Admin activity chart shows you the number of database schema changes, logins, audit setting changes, and entitlement changes on all or selected target databases for the specified time period.

The Events summary tab lists the following audit event categories. For each category, you can view the number of target databases that have an audit event in each event category as well as the total number of events per category.
- 

All activity
- 

All activity by admin
- 

Audit settings changes
- 

Data access events
- 

Database Vault all violations
- 

Database Vault policy changes
- 

Entitlement changes
- 

Entitlement changes by admin
- 

Login failures
- 

Login failures by admin
- 

Schema changes
- 

Schema changes by admin

The Targets summary tab shows you various audit event counts per target database. Audit events include the number of login failures, schema changes, entitlement changes, audit settings changes, all activity (all audit events), database vault realm violations and command rule violations, and database vault policy changes. If there are no audit events for a target database, the target database isn’t listed.

## Audit Profiles, Audit Policies, Audit Trails, and Archive Data Retrievals

Activity Auditing resources that pertain to audit data collection, retention, and retrieval are audit profiles, audit policies, audit trails, and archive data retrievals.

An audit profile resource gives you the flexibility to compute how much audit data is available on the target database for each audit trail that Oracle Data Safe has not yet collected. This helps you evaluate the initial audit data volume when you configure collection in Oracle Data Safe. You can also compute how much audit data Oracle Data Safe has already collected from the target database.

An audit profile defines the online retention period, offline retention period, and the paid usage settings for a target database.

An audit policy resource represents the audit policies for the target database, their corresponding provisioning status, and which policies are enabled or disabled on the target database.

An audit trail represents audit record collection from the target database’s trail such as UNIFIED_AUDIT_TRAIL, which provides documentary evidence of the sequence of activities. Configuring audit trails in Oracle Data Safe, and enabling audit data collection on the audit trails copies the audit records from the target database’s audit trail into the Oracle Data Safe repository.

An archive data retrieval represents an archive retrieve request for audit data. You can retrieve audit data for a target database from the archive and store it online.

## Activity Auditing Reports

Oracle Data Safe generates several predefined audit reports that you can view from the Audit Reports page. The reports track general database activities, such as audited SQL statements, application access activities, and user login activities, as well as Oracle Data Safe activities.

The following table describes each report.

Report Name Description
All Activity All audited activities
Admin Activity Report tracking database activities on admin users as identified in the User Assessment feature. Please note that changes on users may not be reflected immediately in the report and might take up to 12 hours to appear.
User/Entitlement Changes User creation/deletion/privilege and role changes
Audit Policy Changes All changes in audit policies
Login Activity Database login attempts
Data Access Database query operations
Data Modification Data modification activities (DMLs)
Database Schema Changes Database schema changes (DDLs)
Data Safe Activity Activity generated by the Oracle Data Safe service
Database Vault Activity Auditable activities of enabled Oracle Database Vault policies in target databases, including mandatory Database Vault configuration changes, realm violations, and command rule violations
Common User Activity Report tracking database activities on common users as identified in the User Assessment feature.
Database Error Report tracking errors reported in database for activities that are audited.
Data Extraction Activity Report tracking DataPump and RMAN activities in database.
Sensitive Data Activity Report tracking database activities on sensitive objects as identified in the sensitive data models of the Data Discovery feature. This report will only display data if there is a Sensitive Data Model for the target database.
SQL Firewall audited violations Report tracking all SQL Firewall violations that are audited in the database.

## Prerequisites for Using Activity Auditing

These are the prerequisites for using Activity Auditing:
- 

Register the target databases that you want to use with Activity Auditing.
- 

Grant the Audit Collection and Audit Setting roles on the target database. A Database Administrator can grant these roles to the Oracle Data Safe Service Account on the target database.
- 

Obtain permission in Oracle Cloud Infrastructure Identity and Access Management (IAM) to use the Activity Auditing feature in Oracle Data Safe. An OCI administrator can grant`view`or`manage`permission as needed on the following resources:
- 

`data-safe-work-requests`
- 

`data-safe-audit-profiles`
- 

`data-safe-audit-trails`
- 

`data-safe-audit-events`
- 

`data-safe-archive-retrievals`
- 

`data-safe-report-definitions`
- 

`data-safe-reports`
- 

`data-safe-audit-policies`

As an alternative to selectively granting permissions, you can grant permissions on`data-safe-audit-family`in the relevant compartments, which would include permissions on all of the resources above.

For additional help on establishing the prerequisites, see:
- 

[data-safe-audit-family Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html)
- 

[Grant Roles to the Oracle Data Safe Service Account on Your Target Database](https://docs.oracle.com/iaas/data-safe/doc/grant-roles-oracle-data-safe-service-account-your-target-database.html)- describes the roles required for Activity Auditing and for other Oracle Data Safe features.
- 

[OCI Resources for Oracle Data Safe](https://docs.oracle.com/iaas/data-safe/doc/oci-resources-oracle-data-safe.html)describes the permissions for each resource in Oracle Data Safe.

## Activity Auditing Workflow

The general steps for collecting and managing audit data for a target database are as follows:
- 

[Register your target database.](https://docs.oracle.com/iaas/data-safe/doc/target-database-registration.html)Oracle Data Safe creates an audit profile, creates an audit policy, and discovers the audit trails on your target database.
- 

Configure Activity Auditing. Either through the Activity Auditing wizard or manually.
- 

Activity Auditing Wizard:[Run the Configure Auditing and Alerts Wizard](https://docs.oracle.com/iaas/data-safe/doc/configure-auditing-and-alerts.html#GUID-40F6B875-C244-48FF-9098-DCC540C3B7AB)
- 

Manually configure Activity Auditing: a. Review and modify the audit profile to customize audit data retention settings and paid usage settings.
- 

[Specify if you want to collect audit data](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-audit-profiles.html#GUID-ED3ADC60-5B43-4C39-8766-EB5537E46032)for your target database after it reaches the monthly free limit.
- 

[Specify the number of months that you want to retain audit data online and archive audit data.](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-audit-profiles.html#GUID-45238E2E-C1FF-4A21-9968-E3A287DC00E9)

b. Provision audit policies for your target database using[Security Policies](https://docs.oracle.com/iaas/data-safe/doc/security-policies.html#GUID-21DB4A67-F0EA-4F06-B2FD-C26DA85BA69C).

c.[Discover additional audit trails](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-audit-trails.html#GUID-6EA9DCB4-4503-4BAE-B00B-6CF265288E88), remove audit trails, set last archive timestamp (LAT), and enable auto purge on your target database as needed.

d.[Start collecting audit data](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-audit-trails.html#GUID-E72CC85C-444E-4E72-838E-9E5B0764823B)by starting the audit trail(s) for your target database.
- 

[Monitor and analyze the audit data](https://docs.oracle.com/iaas/data-safe/doc/analyze-audit-events-activity-auditing-dashboard.html)on the Activity Auditing landing page and in audit reports.
- 

[Manage audit data collection by adjusting audit trails](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-audit-trails.html).
- 

Start, stop, and resume collecting audit data as needed.
- 

Set last archive timestamp (LAT).
- 

Enable or disable auto purge.
- 

Discover new audit trails.
- 

Delete unused audit trails.
- 

[Retrieve archived audit data when needed](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-archived-audit-data.html#GUID-A1A85A9E-AE6A-43DD-B7A3-30FD4DC2A2A3).
- You can retrieve audit data from the Oracle Data Safe archive if you have previously archived audit data for your target database.
- 

[View and Manage Audit Reports](https://docs.oracle.com/iaas/data-safe/doc/view-and-manage-audit-reports.html#GUID-364B6431-9861-4B42-B24D-103D5F43B44A).
- You can view and schedule audit reports, set filters and modify columns in audit reports, download audit reports as PDF, XLS, or JSON files, as well as create, update, and delete custom audit reports.

- [Activity Auditing Overview](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-741E8CFE-041E-46C4-9C04-D849573A4DB7)
- [About Activity Auditing](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-9D63240B-F912-4C69-A2BD-24CA6AAE3A8E)
- [Activity Auditing Landing Page](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-D61050FB-6D0C-4391-9027-92CACA95990B)
- [Audit Profiles, Audit Policies, Audit Trails, and Archive Data Retrievals](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-C4AFA1AF-648A-4030-B7C6-2A969EC0C61E)
- [Activity Auditing Reports](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-182BB6F1-931F-44C4-949A-DEE63E80ADB6)
- [Prerequisites for Using Activity Auditing](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-3E724704-CC80-4C33-8A1E-1AB0BAB1B54E)
- [Activity Auditing Workflow](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-overview.html#GUID-4A1BBE55-7779-442F-BD8C-CCE6FFB5DC57)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
