# Database Management Diagnosability Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html#dcoc-content-body)

## Database Management Diagnosability Functions

Package: DBMS_CLOUD_OCI_DM_DIAGNOSABILITY

### LIST_ALERT_LOGS Function

Lists the alert logs for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to timestamp to filter the logs.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to timestamp to filter the logs.

`level_filter`

(optional) The optional parameter to filter the alert logs by log level.

Allowed values are: 'CRITICAL', 'SEVERE', 'IMPORTANT', 'NORMAL', 'ALL'

`type_filter`

(optional) The optional parameter to filter the attention or alert logs by type.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE', 'ALL'

`log_search_text`

(optional) The optional query parameter to filter the attention or alert logs by search text.

`is_regular_expression`

(optional) The flag to indicate whether the search text is regular expression or not.

`sort_by`

(optional) The possible sortBy values of attention logs.

Allowed values are: 'LEVEL', 'TYPE', 'MESSAGE', 'TIMESTAMP'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ATTENTION_LOGS Function

Lists the attention logs for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to timestamp to filter the logs.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to timestamp to filter the logs.

`urgency_filter`

(optional) The optional parameter to filter the attention logs by urgency.

Allowed values are: 'IMMEDIATE', 'SOON', 'DEFERRABLE', 'INFO', 'ALL'

`type_filter`

(optional) The optional parameter to filter the attention or alert logs by type.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE', 'ALL'

`log_search_text`

(optional) The optional query parameter to filter the attention or alert logs by search text.

`is_regular_expression`

(optional) The flag to indicate whether the search text is regular expression or not.

`sort_by`

(optional) The possible sortBy values of attention logs.

Allowed values are: 'URGENCY', 'TYPE', 'MESSAGE', 'TIMESTAMP', 'SCOPE', 'TARGET_USER'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ALERT_LOG_COUNTS Function

Get the counts of alert logs for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to timestamp to filter the logs.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to timestamp to filter the logs.

`level_filter`

(optional) The optional parameter to filter the alert logs by log level.

Allowed values are: 'CRITICAL', 'SEVERE', 'IMPORTANT', 'NORMAL', 'ALL'

`group_by`

(optional) The optional parameter used to group different alert logs.

Allowed values are: 'LEVEL', 'TYPE'

`type_filter`

(optional) The optional parameter to filter the attention or alert logs by type.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE', 'ALL'

`log_search_text`

(optional) The optional query parameter to filter the attention or alert logs by search text.

`is_regular_expression`

(optional) The flag to indicate whether the search text is regular expression or not.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ATTENTION_LOG_COUNTS Function

Get the counts of attention logs for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to timestamp to filter the logs.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to timestamp to filter the logs.

`urgency_filter`

(optional) The optional parameter to filter the attention logs by urgency.

Allowed values are: 'IMMEDIATE', 'SOON', 'DEFERRABLE', 'INFO', 'ALL'

`group_by`

(optional) The optional parameter used to group different attention logs.

Allowed values are: 'URGENCY', 'TYPE'

`type_filter`

(optional) The optional parameter to filter the attention or alert logs by type.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE', 'ALL'

`log_search_text`

(optional) The optional query parameter to filter the attention or alert logs by search text.

`is_regular_expression`

(optional) The flag to indicate whether the search text is regular expression or not.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Database Management Diagnosability Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html#ADSDK-GUID-8C7D0B6A-2F10-4246-8862-5BFEA78F44C5)
- [LIST_ALERT_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html#ADSDK-GUID-923B0191-7EA4-44B6-950D-7240925896F0)
- [LIST_ATTENTION_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html#ADSDK-GUID-89FFA761-8096-4EDB-B269-4EAD8A85DABE)
- [SUMMARIZE_ALERT_LOG_COUNTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html#ADSDK-GUID-BE0F6DAB-6BCE-4E90-9153-FF4D53823549)
- [SUMMARIZE_ATTENTION_LOG_COUNTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_diagnosability.html#ADSDK-GUID-70976605-9D16-44DC-BF33-87559D783806)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
