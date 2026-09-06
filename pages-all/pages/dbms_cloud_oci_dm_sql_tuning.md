# Database Management SQL Tuning Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#dcoc-content-body)

## Database Management SQL Tuning Functions

Package: DBMS_CLOUD_OCI_DM_SQL_TUNING

### CLONE_SQL_TUNING_TASK Function

Clones and runs a SQL tuning task in the database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`clone_sql_tuning_task_details`

(required) The detailed inputs required to clone a SQL tuning task.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SQL_TUNING_SET Function

Creates an empty Sql tuning set within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`create_sql_tuning_set_details`

(required) The details required to create a Sql tuning set.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DROP_SQL_TUNING_SET Function

Drops the Sql tuning set specified by sqlTuningSet within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_set_id`

(required) The unique identifier of the Sql tuning set. This is not OCID.

`drop_sql_tuning_set_details`

(required) The details required to drop a Sql tuning set.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DROP_SQL_TUNING_TASK Function

Drops a SQL tuning task and its related results from the database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`drop_sql_tuning_task_details`

(required) The detailed inputs required to drop a SQL tuning task.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DROP_SQLS_IN_SQL_TUNING_SET Function

Deletes the Sqls in the specified Sql tuning set that matches the filter criteria provided in the basicFilter. If basicFilter criteria is not provided, then entire Sqls in the Sql tuning set is deleted.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_set_id`

(required) The unique identifier of the Sql tuning set. This is not OCID.

`drop_sqls_in_sql_tuning_set_details`

(required) Drops the selected list of Sql statements from the current Sql tuning set.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FETCH_SQL_TUNING_SET Function

Fetch the details of Sql statements in the Sql tuning set specified by name, owner and optional filter parameters.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_set_id`

(required) The unique identifier of the Sql tuning set. This is not OCID.

`fetch_sql_tuning_set_details`

(required) The details required to fetch the Sql tuning set details.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXECUTION_PLAN_STATS_COMPARISION Function

Retrieves a comparison of the existing SQL execution plan and a new plan. A SQL tuning task may suggest a new execution plan for a SQL, and this API retrieves the comparison report of the statistics of the two plans.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_advisor_task_id`

(required) The SQL tuning task identifier. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_object_id`

(required) The SQL object ID for the SQL tuning task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`execution_id`

(required) The execution ID for an execution of a SQL tuning task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SQL_EXECUTION_PLAN Function

Retrieves a SQL execution plan for the SQL being tuned.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_advisor_task_id`

(required) The SQL tuning task identifier. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_object_id`

(required) The SQL object ID for the SQL tuning task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`attribute`

(required) The attribute of the SQL execution plan.

Allowed values are: 'ORIGINAL', 'ORIGINAL_WITH_ADJUSTED_COST', 'USING_SQL_PROFILE', 'USING_NEW_INDICES', 'USING_PARALLEL_EXECUTION'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT Function

Gets the summary report for the specified SQL Tuning Advisor task.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_advisor_task_id`

(required) The SQL tuning task identifier. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`search_period`

(optional) How far back the API will search for begin and end exec id. Unused if neither exec ids nor time filter query params are supplied. This is applicable only for Auto SQL Tuning tasks.

Allowed values are: 'LAST_24HR', 'LAST_7DAY', 'LAST_31DAY', 'SINCE_LAST', 'ALL'

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.

`begin_exec_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto SQL Tuning tasks.

`end_exec_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto SQL Tuning tasks.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_TUNING_ADVISOR_TASK_FINDINGS Function

Gets an array of the details of the findings that match specific filters.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_advisor_task_id`

(required) The SQL tuning task identifier. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`begin_exec_id`

(optional) The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task.

`end_exec_id`

(optional) The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task.

`search_period`

(optional) The search period during which the API will search for begin and end exec id, if not supplied. Unused if beginExecId and endExecId optional query params are both supplied.

Allowed values are: 'LAST_24HR', 'LAST_7DAY', 'LAST_31DAY', 'SINCE_LAST', 'ALL'

`finding_filter`

(optional) The filter used to display specific findings in the report.

Allowed values are: 'none', 'FINDINGS', 'NOFINDINGS', 'ERRORS', 'PROFILES', 'INDICES', 'STATS', 'RESTRUCTURE', 'ALTERNATIVE', 'AUTO_PROFILES', 'OTHER_PROFILES'

`stats_hash_filter`

(optional) The hash value of the object for the statistic finding search.

`index_hash_filter`

(optional) The hash value of the index table name.

`sort_by`

(optional) The possible sortBy values of an object's recommendations.

Allowed values are: 'DBTIME_BENEFIT', 'PARSING_SCHEMA', 'SQL_ID', 'STATS', 'PROFILES', 'SQL_BENEFIT', 'DATE', 'INDICES', 'RESTRUCTURE', 'ALTERNATIVE', 'MISC', 'ERROR', 'TIMEOUTS'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

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

### LIST_SQL_TUNING_ADVISOR_TASK_RECOMMENDATIONS Function

Gets the findings and possible actions for a given object in a SQL tuning task. The task ID and object ID are used to retrieve the findings and recommendations.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_advisor_task_id`

(required) The SQL tuning task identifier. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_object_id`

(required) The SQL object ID for the SQL tuning task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`execution_id`

(required) The execution ID for an execution of a SQL tuning task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sort_by`

(optional) The possible sortBy values of an object's recommendations.

Allowed values are: 'RECOMMENDATION_TYPE', 'BENEFIT'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

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

### LIST_SQL_TUNING_ADVISOR_TASKS Function

Lists the SQL Tuning Advisor tasks for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(optional) The optional query parameter to filter the SQL Tuning Advisor task list by name.

`status`

(optional) The optional query parameter to filter the SQL Tuning Advisor task list by status.

Allowed values are: 'INITIAL', 'EXECUTING', 'INTERRUPTED', 'COMPLETED', 'ERROR'

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the SQL Tuning Advisor task summary data.

Allowed values are: 'NAME', 'START_TIME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_TUNING_SETS Function

Lists the SQL tuning sets for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`owner`

(optional) The owner of the SQL tuning set.

`name_contains`

(optional) Allow searching the name of the SQL tuning set by partial matching. The search is case insensitive.

`sort_by`

(optional) The option to sort the SQL tuning set summary data.

Allowed values are: 'NAME'

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

### LOAD_SQL_TUNING_SET Function

Load Sql statements into the Sql tuning set specified by name and optional filter parameters within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_set_id`

(required) The unique identifier of the Sql tuning set. This is not OCID.

`load_sql_tuning_set_details`

(required) The details required to load Sql statements into the Sql tuning set.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SAVE_SQL_TUNING_SET_AS Function

Saves the specified list of Sqls statements into another new Sql tuning set or loads into an existing Sql tuning set'.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_set_id`

(required) The unique identifier of the Sql tuning set. This is not OCID.

`save_sql_tuning_set_as_details`

(required) The details required to save a Sql tuning set into another Sql tuning set.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_SQL_TUNING_TASK Function

Starts a SQL tuning task for a given set of SQL statements from the active session history top SQL statements.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`start_sql_tuning_task_details`

(required) The detailed inputs required to start a SQL tuning task.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_BASIC_FILTER Function

Executes a SQL query to check whether user entered basic filter criteria is valid or not.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_tuning_set_id`

(required) The unique identifier of the Sql tuning set. This is not OCID.

`validate_basic_filter_details`

(required) Validate the basic filter criteria provided by the user.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Database Management SQL Tuning Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-359FED47-03AE-49B8-B13E-438F5FF0D4AD)
- [CLONE_SQL_TUNING_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-088BFB4C-AA41-424F-9A8B-847578FEFD40)
- [CREATE_SQL_TUNING_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-CC6F37BE-B9E7-4B55-8090-F29FA786E37F)
- [DROP_SQL_TUNING_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-35AB8238-29C0-4162-AD87-BF9415E7155A)
- [DROP_SQL_TUNING_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-01C70025-C34A-4F73-B5D0-FABF7772F883)
- [DROP_SQLS_IN_SQL_TUNING_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-409D4DA9-EB24-4DB7-83EE-0FDAE6EE3CEC)
- [FETCH_SQL_TUNING_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-EA92FF21-8A10-4EE6-8824-802B4CDF8D6E)
- [GET_EXECUTION_PLAN_STATS_COMPARISION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-B7DB2A69-9415-4DDD-AB15-2E9AF38152AB)
- [GET_SQL_EXECUTION_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-54110F45-99AE-4B6C-B180-E0242CA04ED6)
- [GET_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-C7D09A61-7982-4581-98D7-4FB192D9E458)
- [LIST_SQL_TUNING_ADVISOR_TASK_FINDINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-1F5E3F42-40B2-4621-A196-F79F238065AC)
- [LIST_SQL_TUNING_ADVISOR_TASK_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-453C33F9-1AC0-4794-9294-349448F1030E)
- [LIST_SQL_TUNING_ADVISOR_TASKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-74051DDB-A04D-487C-AA1F-A8A35A164979)
- [LIST_SQL_TUNING_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-D57E3E07-DCB0-415A-8C11-5BC9D608E96E)
- [LOAD_SQL_TUNING_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-450D08E7-DFA0-47EA-B2C8-6477DE6DCF37)
- [SAVE_SQL_TUNING_SET_AS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-B9D5A994-9BA5-4345-A195-E90A0E3F2F47)
- [START_SQL_TUNING_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-36674A24-A48A-4246-A3A5-A5DD5394BB77)
- [VALIDATE_BASIC_FILTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_sql_tuning.html#ADSDK-GUID-20AB7AD9-C6B1-43EB-A177-59FB50E71EFB)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
