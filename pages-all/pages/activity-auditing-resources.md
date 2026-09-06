# Activity Auditing Resources
- Source: https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#dcoc-content-body)

# Activity Auditing Resources

An administrator in Oracle Cloud Infrastructure Identity and Access Management (IAM) can grant permissions as needed on individual Activity Auditing resources. As an alternative to selectively granting permissions, you can grant permissions on the`data-safe-audit-family`resource in relevant compartments, which includes permissions on all Activity Auditing related resources.

## data-safe-audit-family Resource

The`data-safe-audit-family`resource includes all Oracle Data Safe resources related to Activity Auditing as well as target registration, security policies, and common resources.

Activity Auditing resources:
- 

[`data-safe-archive-retrievals`](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-2CC142FE-32FE-45FE-84B8-53AC6A891F8E)
- 

[`data-safe-audit-events`](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-BBB4A76A-F722-4F94-9AF6-F42471039F7A)
- 

[`data-safe-audit-policies`](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-AFBABF1D-B18F-41D3-93CD-3D0CA5A7AD23)
- 

[`data-safe-audit-profiles`](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-D3488419-09EB-4264-BEE0-3D20388BD3BA)
- 

[`data-safe-audit-trails`](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-8BF3F4A1-B69F-44CD-A01C-98BCB882409C)

Target registration resources:
- 

[`data-safe-private-endpoints`](https://docs.oracle.com/iaas/data-safe/doc/target-registration-resources.html#GUID-6D99DB1A-8D52-4866-8755-AD077ACA985C)
- 

[`onprem-connectors`](https://docs.oracle.com/iaas/data-safe/doc/target-registration-resources.html#GUID-01CD60B5-A7B0-478F-A9E2-30826C829591)
- 

[`target-database-group`](https://docs.oracle.com/iaas/data-safe/doc/target-registration-resources.html#GUID-96AAFA35-EC90-4F1F-B272-56C2654DE2DE)
- 

[`target-databases`](https://docs.oracle.com/iaas/data-safe/doc/target-registration-resources.html#GUID-E417AD62-B217-4505-B67F-FBE3DA7F9DAB)

Security policies resources:
- 

[`data-safe-unified-audit-policies`](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-AFBABF1D-B18F-41D3-93CD-3D0CA5A7AD23)
- 

[`data-safe-unified-audit-policy-definitions`](https://docs.oracle.com/iaas/data-safe/doc/security-policy-resources.html#GUID-05172C91-8BCB-4C05-9757-D10059F11350)
- 

[`data-safe-security-policies`](https://docs.oracle.com/iaas/data-safe/doc/security-policy-resources.html#GUID-CD78109B-E6A4-4ED6-81EE-9DAB198F7E25)
- 

[`data-safe-security-policy-configs`](https://docs.oracle.com/iaas/data-safe/doc/security-policy-resources.html#GUID-53A675BB-DA22-4F75-9EA1-4B62F26E9059)
- 

[`data-safe-security-policy-deployments`](https://docs.oracle.com/iaas/data-safe/doc/security-policy-resources.html#GUID-484F4640-FA0B-46AA-BEFC-87CD68C7D4EC)

Common resources:
- 

[`data-safe`](https://docs.oracle.com/iaas/data-safe/doc/common-resources.html#GUID-D952FF78-DE48-4CD0-8C33-AA6ECEC968BD)
- 

[`data-safe-report-definitions`](https://docs.oracle.com/iaas/data-safe/doc/common-resources.html#GUID-4269A9F3-9372-4A07-B6DE-C72C2547097E)
- 

[`data-safe-reports`](https://docs.oracle.com/iaas/data-safe/doc/common-resources.html#GUID-D595D80A-2DDD-47D1-A2A5-8A931B75D559)
- 

[`data-safe-work-requests`](https://docs.oracle.com/iaas/data-safe/doc/common-resources.html#GUID-E6B44948-81C0-4C7A-BA74-AC1C849D12BA)
- 

[`data-safe-attribute-sets`](https://docs.oracle.com/iaas/data-safe/doc/common-resources.html#GUID-B11A8CFC-B850-4C97-8129-85313C9885FC)

The following table describes the permissions that you can assign to a group for the`data-safe-audit-family`resource.

Permission Description
`inspect`The user group can list all Activity Auditing resources in a specified compartment.
`read`or`use`The user group can list and view properties for all Activity Auditing resources in a specified compartment.
`manage`The user group can do the following: 1) List, view properties for, create, update, delete, and move (to another compartment) all Activity Auditing resources in a specified compartment. 2) Inspect, read, create, update, delete, and move Oracle Data Safe private endpoints, Oracle Data Safe on-premises connectors, and Oracle Data Safe target databases. 3) Read work requests in Oracle Data Safe.

## data-safe-archive-retrievals Resource

The`data-safe-archive-retrievals`resource represents archive data retrieval objects in Activity Auditing.

The following table describes the permissions available for the`data-safe-archive-retrieval`resource.

Permission Description
`inspect`The user group can list archive data retrievals.
`read`or`use`The user group can list and view details for archive data retrievals.
`manage`The user group can list, view details for, create, update, delete, and move (to another compartment) archive data retrievals. The group can also retrieve archive audit data and return it back to the archive.

## data-safe-audit-events Resource

The`data-safe-audit-events`resource represents audit events for target databases in Activity Auditing.

The following table describes the permissions available for the`data-safe-audit-events`resource.

Permission Description
`inspect`The user group can list audit events.
`read`The user group can list and view details for audit events.

## data-safe-audit-policies Resource

The`data-safe-audit-policies`resource represents audit policies for target databases in Activity Auditing.

The following table describes the permissions available for the`data-safe-audit-policies`resource.

Permission Description
`inspect`The user group can list audit policies.
`read`or`use`The user group can list and view details for audit policies.
`manage`The user group can list, view details for, create, update, delete, and move (to another compartment) audit policies.

## data-safe-audit-profiles Resource

The`data-safe-audit-profiles`resource represents audit profiles for target databases in Activity Auditing.

The following table describes the permissions available for the`data-safe-audit-profiles`resource.

Permission Description
`inspect`The user group can list audit profiles.
`read`or`use`The user group can list and view details for audit profiles.
`manage`The user group can list, view details for, create, update, delete, and move (to another compartment) audit profiles. A user can update the online and offline retention periods and paid usage setting.

## data-safe-audit-trails Resource

The`data-safe-audit-trails`resource represents audit trails for target databases in Activity Auditing.

The following table describes the permissions available for the`data-safe-audit-trails`resource.

Permission Description
`inspect`The user group can list audit trails.
`read`or`use`The user group can list and view details for audit trails.
`manage`The user group can list, view details for, create, update, delete, and move (to another compartment) audit trails.

- [Activity Auditing Resources](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-7861386D-14BB-47D4-8410-DF5EBAC71DA0)
- [data-safe-audit-family Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-37EA9B5F-995B-4544-8C6E-D28658B2D8FE)
- [data-safe-archive-retrievals Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-2CC142FE-32FE-45FE-84B8-53AC6A891F8E)
- [data-safe-audit-events Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-BBB4A76A-F722-4F94-9AF6-F42471039F7A)
- [data-safe-audit-policies Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-AFBABF1D-B18F-41D3-93CD-3D0CA5A7AD23)
- [data-safe-audit-profiles Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-D3488419-09EB-4264-BEE0-3D20388BD3BA)
- [data-safe-audit-trails Resource](https://docs.oracle.com/iaas/data-safe/doc/activity-auditing-resources.html#GUID-8BF3F4A1-B69F-44CD-A01C-98BCB882409C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
