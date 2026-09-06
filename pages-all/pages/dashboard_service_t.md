# Dashboard Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#dcoc-content-body)

## Dashboard Common Types

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CHANGE_DASHBOARD_GROUP_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CHANGE_DASHBOARD_GROUP_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboardGroup into which the resource should be moved.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CREATE_DASHBOARD_DETAILS_T Type

The base schema for creating a dashboard. Derived schemas have configurations and widgets specific to the `schemaVersion`.

Syntax
```

```

Fields

Field Description

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group that the dashbaord is associated with.

`display_name`

(optional) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(optional) A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`schema_version`

(required) The schema describing how to interpret the dashboard configuration and widgets.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CREATE_DASHBOARD_GROUP_DETAILS_T Type

The data to create a new dashboard group.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(optional) A short description of the dashboard group. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the dashboard group.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CREATE_V1_DASHBOARD_DETAILS_T Type

Details for creating a version 1 dashboard. The interpretation of the `config` and `widgets` fields depends on the runtime behavior of the Oracle Cloud Infrastructure Console. The sum of the `config` and `widget` fields JSON text representation cannot exceed 200 KB.

Syntax
```

```

`dbms_cloud_oci_dashboard_service_create_v1_dashboard_details_t`is a subtype of the`dbms_cloud_oci_dashboard_service_create_dashboard_details_t`type.

Fields

Field Description

`config`

(optional) The layout and widget placement for the dashboard.

`widgets`

(required) The basic visualization building blocks of a dashboard.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_T Type

The base schema for a dashboard. Derived schemas have configurations and widgets specific to the `schemaVersion`.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard resource.

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group that the dashboard belongs to.

`display_name`

(required) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(required) A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the dashboard. A dashboard is always in the same compartment as its dashboard group.

`schema_version`

(required) The schema describing how to interpret the dashboard configuration and widgets.

Allowed values are: 'V1'

`time_created`

(required) The date and time the dashboard was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time the dashboard was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the dashboard.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_SUMMARY_T Type

Summary information about the dashboard.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard resource.

`dashboard_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group that the dashboard belongs to.

`display_name`

(required) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(required) A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the dashboard. A dashboard is always in the same compartment as its dashboard group.

`time_created`

(required) The date and time the dashboard was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z

`time_updated`

(optional) The date and time the dashboard was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the Dashboard.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dashboard_service_dashboard_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_COLLECTION_T Type

Results of a dashboard search. Contains `DashboardSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of dashboards.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_T Type

The base schema for a dashboard group.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`display_name`

(required) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(required) A short description of the dashboard group. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the dashboard group.

`time_created`

(required) The date and time the dashboard group was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(required) The date and time the dashboard group was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the `DashboardGroup` resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_SUMMARY_T Type

Summary information for the dashboard group.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the dashboard group.

`display_name`

(required) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(required) A short description of the dashboard group. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the dashboard group.

`time_created`

(required) The date and time the dashboard group was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the dashboard group was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the `DashboardGroup` resource.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dashboard_service_dashboard_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_COLLECTION_T Type

A list of dashboard groups that match filter criteria, if any. Results contain `DashboardGroupSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of dashboard groups.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_ERROR_T Type

Details about erros encountered.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_UPDATE_DASHBOARD_DETAILS_T Type

The base schema for updating a dashboard. Derived schemas have configurations and widgets specific to the `schemaVersion`.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(optional) A short description of the dashboard. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`schema_version`

(required) The schema describing how to interpret the dashboard configuration and widgets.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_UPDATE_DASHBOARD_GROUP_DETAILS_T Type

The data to update a dashboard group.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information. Leading and trailing spaces and the following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`description`

(optional) A short description of the dashboard group. It can be changed. Avoid entering confidential information. The following special characters are not allowed: &lt;&gt;()=/'\"&amp;\\

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_UPDATE_V1_DASHBOARD_DETAILS_T Type

Details for updating a version 1 dashboard. The interpretation of the `config` and `widgets` fields depends on the runtime behavior of the Oracle Cloud Infrastructure Console. The sum of the `config` and `widget` fields JSON text representation cannot exceed 200 KB.

Syntax
```

```

`dbms_cloud_oci_dashboard_service_update_v1_dashboard_details_t`is a subtype of the`dbms_cloud_oci_dashboard_service_update_dashboard_details_t`type.

Fields

Field Description

`config`

(optional) The layout and widget placement for the dashboard.

`widgets`

(optional) The basic visualization building blocks of a dashboard.

### DBMS_CLOUD_OCI_DASHBOARD_SERVICE_V1_DASHBOARD_T Type

A version 1 dashboard. The interpretation of the `config` and `widgets` fields depends on the runtime behavior of the Oracle Cloud Infrastructure Console. The sum of the `config` and `widget` fields JSON text representation cannot exceed 200 KB.

Syntax
```

```

`dbms_cloud_oci_dashboard_service_v1_dashboard_t`is a subtype of the`dbms_cloud_oci_dashboard_service_dashboard_t`type.

Fields

Field Description

`config`

(optional) The dashboard configuration. For example, the layout and widget placement.

`widgets`

(required) The visualization building blocks of the dashboard.

- [Dashboard Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-21D07152-6E8A-4F50-B151-C04C678C8F67)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-8BDE7E58-1041-47C9-AB57-F8FB42E7BBE8)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CHANGE_DASHBOARD_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-B03356C1-14DC-4A79-8CC6-AE0686875E60)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CHANGE_DASHBOARD_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-13295DD9-0DE9-49F6-A442-833550A135CD)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CREATE_DASHBOARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-FEE80B7F-F43D-44CF-84A2-AFD019304616)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CREATE_DASHBOARD_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-913D41DA-A6E8-42F9-BDB0-91B540F9D339)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-5EED0EBD-2BBF-4DB7-A56C-74F4E5DB3981)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_CREATE_V1_DASHBOARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-8AE5F51B-704C-45E3-950A-0CC14184C4E1)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-C66F5784-1D3C-4444-83C3-D7BB377C1E18)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-BFC67B4D-7FD4-4959-BAE1-0BF291946034)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-420BAEB2-DA36-4B27-AF82-3D41F645C1AF)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-52950B76-2C04-4043-A114-AFBE900C93D7)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-82321815-5EE5-408A-BF2D-20E47BD33667)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-B01F4999-BAC0-4B4C-B5E6-0781DFB9AC7B)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-A4402DEB-0255-4353-BC6E-6129343B47B7)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_DASHBOARD_GROUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-2A312B4E-0C21-485B-900F-819AE5EB8DF5)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-936A13BB-59E7-411F-AF2C-4782694EABCD)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_UPDATE_DASHBOARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-AE81ECA6-4FD4-45CD-AAFA-308319679699)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_UPDATE_DASHBOARD_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-F54D7E61-9031-4F42-863F-A5D18984D2AE)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_UPDATE_V1_DASHBOARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-41BF1FE4-2082-4154-A613-73E9A06948E2)
- [DBMS_CLOUD_OCI_DASHBOARD_SERVICE_V1_DASHBOARD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dashboard_service_t.html#ADSDK-GUID-07EBBA95-2514-4D31-95AD-4F2FC07C840D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
