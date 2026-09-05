# Generate and Download Access Governance Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/reports-overview.htm
- Fetched: 2026-09-05 03:16 CDT

# Generate and Download Access Governance Reports

Use Reports to export data across Oracle Access Governance entities for offline review, auditing, and analysis. Oracle Access Governance generates reports asynchronously. The report includes data ingested in Oracle Access Governance and are downloaded as ZIP files containing report data in CSV format.

Role : Administrator (`AG_Administrator`), Auditor (`AG_Auditor`)

You can request the following reports:
- Identities : Provides identity information, such as username, email, status, manager, and other identity attributes. You can select the identity attributes that you want to include.
```

```

- Access Bundle Assignments : Lists provisioned access bundle assignments for identities, including assignment status and validity dates.
```

```

- Accounts : Lists global identities and their accounts across orchestrated systems. Oracle Access Governance generates one report download as a ZIP file, with a separate CSV file for each orchestrated system
```

```

- Access Bundles : Lists access bundle, role and permission relationship. The report includes access bundles associated with roles and doesn't include access bundles that have no associated role. If an access bundle contains several permissions, the report represents the access bundle-to-role-to-permission relationships as separate records. Role names in this report can be system-generated.
```

```

Note  
  
CSV exports from the Identities and Enterprise-wide Browser pages export the current view or filtered results and have limits on the number of records you can export. Reports include all records returned by the report query across Oracle Access Governance entities.

## Report Retention and Limits

You can access a generated report for 30 days from the date you create it. You can request to seven reports of each report type in a service instance. This limit includes reports created by all users and failed reports.

In case a report fails, you can retry a failed report without creating a new report. A retry doesn't add another report in the seven-report limit.

### Check Report Status

Use the Reports page to check the status of the requested reports.

A report can have one of the following statuses:
- Requested : The report request is received.
- In Progress : The report generation is in progress.
- Available : The report is ready to download.
- Failed : The report generation failed. If report generation fails because of internal processing error, you can retry the failed report.

## Request a Report

Request a downloadable report that contains the Oracle Access Governance data you want to review or analyze.
You must have either Administrator (`AG_Administrator`), Auditor (`AG_Auditor`) roles. You can have only one report of the same type generating at a time in a service instance. Wait for the current report to finish before requesting another report of that type. See[Report Retention and Limits](https://docs.oracle.com/en-us/iaas/Content/access-governance/reports-overview.htm#report-limits)

- Sign in to Oracle Access Governance.
- From the navigation menu , select Reports .
- Select Request report .
- Select report type that you want to request.
- Select the attributes to include, if available.
- Select Request .

Oracle Access Governance generates the report in the background and notifies you when it's ready to download. For an Identities report, you can select supported identity attributes to include. Some attributes, such as email address, employee username, identity ID are always included.

## Download a Report

Download an available report to review its data offline.

- Go to the Reports page.
- For a report that you want to download:
- From the action menu for a report, select Download.
- Select the Download link to download the report.
The ZIP file is downloaded containing the CSV files. For the Accounts report, you request and download one report. The ZIP file contains separate CSV files for the orchestrated systems included in the report.

## Delete a Report

Delete a report when you no longer need it or to accommodate other reports. The report is automatically deleted after the retention period.

- Go to the Reports page.
- From the action menu for a report, select Delete .
- Confirm the deletion.

## Report Notification

You receive an email when the report is ready to download, fails to generate, or is scheduled for deletion.

When the report is ready, the email includes a link to the report and how long the report is available. If the report fails, the email includes a link to view the report status and failure details. If the report is scheduled for deletion, the email includes the deletion date and a link to download the report before it's permanently deleted.

## Report Detail Reference

Use this reference to understand the data included in each report and how report columns relate to information in Oracle Access Governance.

### Identities

The Identities report lists global identities and their identity attributes. You can select supported identity attributes when you request this report.

CSV column Display name Description
`identityId`Identity ID Unique identifier of the global identity.
`userName`Employee username Username associated with the identity.
`primaryEmail`Email Primary email address of the identity.
`displayName`Name Display name of the user.

### Access Bundle Assignments

The Access Bundle Assignments report lists provisioned access bundle assignments for identities.

CSV column Display name Description
`identityID`Identity ID Unique identifier of the global identity.
`userName`Employee username Username associated with the identity.
`primaryEmail`Email Primary email address of the identity.
`accessBundleName`Permission Name of the assigned access bundle
`status`Status Provisioning status of the assignment.
`validTo`Valid to Date until which the assignment is valid, when available.
`validFrom`Valid from Date from which the assignment is valid, when available.

### Accounts

The Accounts report lists global identities and their accounts across orchestrated systems.

CSV column Display name Description
`identityId`Identity ID Global identity associated with the account.
`userName`Employee username Username associated with the identity.
`primaryEmail`Email Primary email address of the identity.
`AccountId`Account ID Unique identifier of the account.
`AccountName`Account name Account name

### Access Bundles

The Access Bundles report lists role-to-access-bundle-to-permission configuration.

CSV column Display name Description
`roleId`Role ID Identifier of the role associated with the access bundle.
`roleName`Role name Name of the role associated with the access bundle. The report can be system-generated role name.
`accessBundleId`Access Bundle ID Identifier of the access bundle.
`accessBundleName`Permission Name of the access bundle.
`targetId`System ID Identifier of the associated orchestrated system.
`targetName`System name Name of the associated orchestrated system.
`permissionName`
