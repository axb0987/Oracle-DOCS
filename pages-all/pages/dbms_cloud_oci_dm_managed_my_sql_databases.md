# Database Management Managed MySql Databases Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#dcoc-content-body)

## Database Management Managed MySql Databases Functions

Package: DBMS_CLOUD_OCI_DM_MANAGED_MY_SQL_DATABASES

### GET_MANAGED_MY_SQL_DATABASE Function

Retrieves the general information for a specific MySQL Database.

Syntax
```

```

Parameters

Parameter Description

`managed_my_sql_database_id`

(required) The OCID of the Managed MySQL Database.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MY_SQL_FLEET_METRIC Function

Gets the health metrics for a fleet of MySQL Databases in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`start_time`

(required) The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`filter_by_my_sql_deployment_type_param`

(optional) The parameter to filter by MySQL deployment type.

Allowed values are: 'ONPREMISE', 'MDS'

`filter_by_mds_deployment_type`

(optional) The parameter to filter by MySQL Database System type.

Allowed values are: 'HA', 'HEATWAVE', 'STANDALONE'

`filter_by_my_sql_status`

(optional) The parameter to filter by MySQL Database status.

Allowed values are: 'UP', 'DOWN', 'UNKNOWN'

`filter_by_my_sql_database_version`

(optional) The parameter to filter by MySQL database version.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_MY_SQL_DATABASE_CONFIGURATION_DATA Function

Retrieves configuration data for a specific MySQL database.

Syntax
```

```

Parameters

Parameter Description

`managed_my_sql_database_id`

(required) The OCID of the Managed MySQL Database.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_MY_SQL_DATABASE_SQL_DATA Function

Retrieves the SQL performance data for a specific MySQL database.

Syntax
```

```

Parameters

Parameter Description

`managed_my_sql_database_id`

(required) The OCID of the Managed MySQL Database.

`start_time`

(required) The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`filter_column`

(optional) The parameter to filter results by key criteria which include : - SUM_TIMER_WAIT - COUNT_STAR - SUM_ERRORS - SUM_ROWS_AFFECTED - SUM_ROWS_SENT - SUM_ROWS_EXAMINED - SUM_CREATED_TMP_TABLES - SUM_NO_INDEX_USED - SUM_NO_GOOD_INDEX_USED - FIRST_SEEN - LAST_SEEN

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_MY_SQL_DATABASES Function

Gets the list of Managed MySQL Databases in a specific compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_MANAGED_MY_SQL_DATABASE_AVAILABILITY_METRICS Function

Gets the availability metrics for the MySQL Database specified by managedMySqlDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_my_sql_database_id`

(required) The OCID of the Managed MySQL Database.

`start_time`

(required) The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Database Management Managed MySql Databases Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-600DF07B-D515-45FD-9A21-447C272E6965)
- [GET_MANAGED_MY_SQL_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-B5CAA61D-7B13-45CA-B441-20AA859D2435)
- [GET_MY_SQL_FLEET_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-E76DD85A-E5EA-4039-92A6-64E8A9601213)
- [LIST_MANAGED_MY_SQL_DATABASE_CONFIGURATION_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-C1FE35F7-AE61-4C3B-B773-7BFC5B746E75)
- [LIST_MANAGED_MY_SQL_DATABASE_SQL_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-A33CBCA2-0EE7-4CED-90BB-EEE01B3627A9)
- [LIST_MANAGED_MY_SQL_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-69022547-05E8-4C7C-B34D-CE0F91465804)
- [SUMMARIZE_MANAGED_MY_SQL_DATABASE_AVAILABILITY_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_managed_my_sql_databases.html#ADSDK-GUID-FB31725F-3248-4A45-A21B-E1787EFFE931)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
