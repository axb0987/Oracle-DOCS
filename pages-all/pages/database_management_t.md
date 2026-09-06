# Database Management Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#dcoc-content-body)

## Database Management Common Types

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DIMENSION_DEFINITION_T Type

The metric dimension details.

Syntax
```

```

Fields

Field Description

`dimension_name`

(optional) The name of the dimension.

`dimension_value`

(optional) The value of the dimension.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DIMENSION_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_metric_dimension_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DATA_POINT_T Type

The metric values with dimension details.

Syntax
```

```

Fields

Field Description

`value`

(optional) The value of the metric.

`unit`

(optional) The unit of the metric value.

`dimensions`

(optional) The dimensions of the metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ACTIVITY_TIME_SERIES_METRICS_T Type

The response object representing activityMetric details for a specific Managed Database at a particular time.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(optional) The date and time the activity metric was created.

`cpu_time`

(optional)

`wait_time`

(optional)

`user_io_time`

(optional)

`cpu_count`

(optional)

`l_cluster`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_CREDENTIAL_DETAILS_T Type

The credential to connect to the database to perform tablespace administration tasks.

Syntax
```

```

Fields

Field Description

`tablespace_admin_credential_type`

(required) The type of the credential for tablespace administration tasks.

Allowed values are: 'SECRET', 'PASSWORD'

`username`

(required) The user to connect to the database.

`role`

(required) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_STORAGE_SIZE_T Type

Storage size.

Syntax
```

```

Fields

Field Description

`l_size`

(required) Storage size number in bytes, kilobytes, megabytes, gigabytes, or terabytes.

`unit`

(optional) Storage size unit: bytes, kilobytes, megabytes, gigabytes, or terabytes.

Allowed values are: 'BYTES', 'KILOBYTES', 'MEGABYTES', 'GIGABYTES', 'TERABYTES'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADD_DATA_FILES_DETAILS_T Type

The details required to add data files or temp files to the tablespace.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`file_type`

(required) Specifies whether the file is a data file or temp file.

Allowed values are: 'DATAFILE', 'TEMPFILE'

`data_files`

(optional) The list of data files or temp files added to the tablespace.

`file_count`

(optional) The number of data files or temp files to be added for the tablespace. This is for Oracle Managed Files only.

`file_size`

(optional) The size of each data file or temp file.

`is_reusable`

(optional) Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.

`is_auto_extensible`

(optional) Specifies whether the data file or temp file can be extended automatically.

`auto_extend_next_size`

(optional) The size of the next increment of disk space to be allocated automatically when more extents are required.

`auto_extend_max_size`

(optional) The maximum disk space allowed for automatic extension of the data files or temp files.

`is_max_size_unlimited`

(optional) Specifies whether the disk space of the data file or temp file can be limited.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADD_MANAGED_DATABASE_TO_MANAGED_DATABASE_GROUP_DETAILS_T Type

The Managed Database details required to add it to a Managed Database Group.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADDM_TASK_SUMMARY_T Type

The object containing the ADDM task metadata.

Syntax
```

```

Fields

Field Description

`task_name`

(optional) The name of the ADDM task.

`task_id`

(required) The ID number of the ADDM task.

`description`

(optional) The description of the ADDM task.

`db_user`

(optional) The database user who owns the ADDM task.

`status`

(optional) The status of the ADDM task.

Allowed values are: 'INITIAL', 'EXECUTING', 'INTERRUPTED', 'COMPLETED', 'ERROR'

`time_created`

(required) The creation date of the ADDM task.

`how_created`

(optional) A description of how the task was created.

Allowed values are: 'AUTO', 'MANUAL'

`start_snapshot_time`

(optional) The timestamp of the beginning AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.

`end_snapshot_time`

(optional) The timestamp of the ending AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.

`begin_snapshot_id`

(optional) The ID number of the beginning AWR snapshot.

`end_snapshot_id`

(optional) The ID number of the ending AWR snapshot.

`findings`

(optional) The number of ADDM findings.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADDM_TASK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_addm_task_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADDM_TASKS_COLLECTION_T Type

The list of ADDM task metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of ADDM task metadata.

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SCHEMA_DEFINITION_T Type

The schema object details.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the schema.

`objects`

(optional) The names of schema objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SCHEMA_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_schema_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FINDING_SCHEMA_OR_OPERATION_T Type

The findings of the Optimizer Statistics Advisor.

Syntax
```

```

Fields

Field Description

`operations`

(optional) The list of operation details.

`schemas`

(optional) The names of the impacted database schemas and their objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_EXAMPLE_LINE_T Type

An example line of the recommendation

Syntax
```

```

Fields

Field Description

`operation`

(optional) The details of the example operation.

`l_comment`

(optional) The comments about the operation.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_EXAMPLE_LINE_TBL Type

Nested table type of dbms_cloud_oci_database_management_recommendation_example_line_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_EXAMPLE_T Type

An example of the recommendation.

Syntax
```

```

Fields

Field Description

`lines`

(optional) The list of examples for the recommendation.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_RATIONALE_T Type

The details of the rationale for the recommendation.

Syntax
```

```

Fields

Field Description

`message`

(required) The message of the rationale.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_RATIONALE_TBL Type

Nested table type of dbms_cloud_oci_database_management_recommendation_rationale_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_T Type

The details of the Optimizer Statistics Advisor findings and recommendations.

Syntax
```

```

Fields

Field Description

`message`

(required) An overview of the Optimizer Statistics Advisor recommendation.

`example`

(optional)

`rationales`

(optional) The rationale of the recommendation.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FINDING_SCHEMA_OR_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_database_management_finding_schema_or_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_TBL Type

Nested table type of dbms_cloud_oci_database_management_recommendation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RULE_FINDING_T Type

The summary of the Optimizer Statistics Advisor findings and recommendations.

Syntax
```

```

Fields

Field Description

`message`

(required) A high-level overview of the findings of the Optimizer Statistics Advisor.

`details`

(required) The details of the schema or operation.

`recommendations`

(required) The list of recommendations.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RULE_FINDING_TBL Type

Nested table type of dbms_cloud_oci_database_management_rule_finding_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADVISOR_RULE_T Type

The details of the Optimizer Statistics Advisor rule.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the rule.

`description`

(required) The description of the rule.

`findings`

(required) The list of findings for the rule.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_SUMMARY_T Type

The detail for one alert log entry.

Syntax
```

```

Fields

Field Description

`message_level`

(required) The level of the alert log.

Allowed values are: 'CRITICAL', 'SEVERE', 'IMPORTANT', 'NORMAL'

`message_type`

(required) The type of alert log message.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE'

`message_content`

(optional) The contents of the alert log message.

`l_timestamp`

(optional) The date and time the alert log was created.

`supplemental_detail`

(optional) The supplemental details of the alert log.

`file_location`

(optional) The alert log file location.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_alert_log_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COLLECTION_T Type

The list of alert logs.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`items`

(required) An array of the alert logs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COUNT_SUMMARY_T Type

The details for one alert log count entry.

Syntax
```

```

Fields

Field Description

`category`

(required) The category of different alert logs.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE', 'CRITICAL', 'SEVERE', 'IMPORTANT', 'NORMAL', 'OTHER'

`l_count`

(required) The count of alert logs with specific category.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COUNT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_alert_log_count_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COUNTS_COLLECTION_T Type

The collection of the counts of different level or type of alert logs.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`items`

(required) An array of the counts of different urgency or type of alert logs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALLOWED_PARAMETER_VALUE_T Type

A valid value for a database parameter.

Syntax
```

```

Fields

Field Description

`ordinal`

(optional) The ordinal number in the list (1-based).

`value`

(optional) The parameter value at ordinal.

`is_default`

(optional) Indicates whether the given ordinal value is the default value for the parameter.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_CREDENTIALS_T Type

The credentials used to connect to the ASM instance. Currently only the `DETAILS` type is supported for creating MACS connector credentials.

Syntax
```

```

Fields

Field Description

`credential_type`

(optional) The type of credential used to connect to the ASM instance.

Allowed values are: 'NAME_REFERENCE', 'DETAILS'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_CREDENTAILS_BY_NAME_T Type

The existing named credential used to connect to the ASM instance.

Syntax
```

```

`dbms_cloud_oci_database_management_asm_connection_credentails_by_name_t`is a subtype of the`dbms_cloud_oci_database_management_asm_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(required) The name of the credential information that used to connect to the DB system resource. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_CREDENTIALS_BY_DETAILS_T Type

The credentials used to connect to the ASM instance.

Syntax
```

```

`dbms_cloud_oci_database_management_asm_connection_credentials_by_details_t`is a subtype of the`dbms_cloud_oci_database_management_asm_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(optional) The name of the credential information that used to connect to the DB system resource. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

`user_name`

(required) The user name used to connect to the ASM instance.

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

`role`

(required) The role of the user connecting to the ASM instance.

Allowed values are: 'SYSASM', 'SYSDBA', 'SYSOPER'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_STRING_T Type

The ASM instance connection string.

Syntax
```

```

Fields

Field Description

`hosts`

(required) The list of host names of the ASM instances.

`port`

(required) The port used to connect to the ASM instance.

`service`

(required) The service name of the ASM instance.

`protocol`

(required) The protocol used to connect to the ASM instance.

Allowed values are: 'TCP'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_T Type

The details of ASM properties.

Syntax
```

```

Fields

Field Description

`disk_group`

(required) The name of the disk group.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_SUMMARY_T Type

The summary of ASM properties.

Syntax
```

```

Fields

Field Description

`disk_group`

(required) The name of the disk group.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_asm_property_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_COLLECTION_T Type

A collection of ASM properties for a specific Managed Database.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of AsmPropertySummary resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_COMPONENT_T Type

The details of the associated component.

Syntax
```

```

Fields

Field Description

`component_id`

(required) The identifier of the associated component.

`component_type`

(optional) The type of associated component.

Allowed values are: 'ASM', 'ASM_INSTANCE', 'CLUSTER', 'CLUSTER_INSTANCE', 'DATABASE', 'DATABASE_INSTANCE', 'DATABASE_HOME', 'DATABASE_NODE', 'DBSYSTEM', 'LISTENER', 'PLUGGABLE_DATABASE'

`association_type`

(required) The association type.

Allowed values are: 'CONTAINS', 'USES'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_DATABASE_SUMMARY_T Type

The summary of a database currently using a Database Management private endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`name`

(required) The name of the database.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`time_registered`

(required) The time when Database Management was enabled for the database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_DATABASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_associated_database_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_DATABASE_COLLECTION_T Type

A collection of databases using a Database Management private endpoint.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of databases using a Database Management private endpoint.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_SERVICE_DETAILS_T Type

The details of the associated service that will be enabled or disabled for an external DB System.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) The status of the associated service.

`metadata`

(optional) The associated service-specific inputs in JSON string format, which Database Management can identify.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_SUMMARY_T Type

The details for one attention log entry.

Syntax
```

```

Fields

Field Description

`message_urgency`

(required) The urgency of the attention log.

Allowed values are: 'IMMEDIATE', 'SOON', 'DEFERRABLE', 'INFO'

`message_type`

(required) The type of attention log message.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE'

`message_content`

(optional) The contents of the attention log message.

`l_timestamp`

(optional) The date and time the attention log was created.

`scope`

(optional) The database scope for the attention log.

`target_user`

(optional) The user who must act on the attention log message.

`cause`

(optional) The cause of the attention log.

`action`

(optional) The recommended action to handle the attention log.

`supplemental_detail`

(optional) The supplemental details of the attention log.

`file_location`

(optional) The attention log file location.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_attention_log_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COLLECTION_T Type

The list of attention logs.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`items`

(required) An array of the attention logs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COUNT_SUMMARY_T Type

The details for one attention log count entry.

Syntax
```

```

Fields

Field Description

`category`

(required) The category of different attention logs.

Allowed values are: 'UNKNOWN', 'INCIDENT_ERROR', 'ERROR', 'WARNING', 'NOTIFICATION', 'TRACE', 'IMMEDIATE', 'SOON', 'DEFERRABLE', 'INFO', 'OTHER'

`l_count`

(required) The count of attention logs with specific category.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COUNT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_attention_log_count_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COUNTS_COLLECTION_T Type

The collection of the counts of different urgency or type of attention logs.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`items`

(required) An array of the counts of different urgency or type of attention logs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_T Type

An automatic capture filter that enables you to capture only those SQL statements that you want, and exclude noncritical statements.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the automatic capture filter. - AUTO_CAPTURE_SQL_TEXT: Search pattern to apply to SQL text. - AUTO_CAPTURE_PARSING_SCHEMA_NAME: Parsing schema to include or exclude for SQL plan management auto capture. - AUTO_CAPTURE_MODULE: Module to include or exclude for SQL plan management auto capture. - AUTO_CAPTURE_ACTION: Action to include or exclude for SQL plan management automatic capture.

Allowed values are: 'AUTO_CAPTURE_SQL_TEXT', 'AUTO_CAPTURE_PARSING_SCHEMA_NAME', 'AUTO_CAPTURE_MODULE', 'AUTO_CAPTURE_ACTION'

`values_to_include`

(optional) A list of filter values to include.

`values_to_exclude`

(optional) A list of filter values to exclude.

`time_last_modified`

(optional) The time the filter value was last updated.

`modified_by`

(optional) The database user who last updated the filter value.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_DETAILS_T Type

The details of a capture filter used to include or exclude SQL statements in the initial automatic plan capture.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the automatic capture filter. - AUTO_CAPTURE_SQL_TEXT: Search pattern to apply to SQL text. - AUTO_CAPTURE_PARSING_SCHEMA_NAME: Parsing schema to include or exclude for SQL plan management auto capture. - AUTO_CAPTURE_MODULE: Module to include or exclude for SQL plan management auto capture. - AUTO_CAPTURE_ACTION: Action to include or exclude for SQL plan management automatic capture.

Allowed values are: 'AUTO_CAPTURE_SQL_TEXT', 'AUTO_CAPTURE_PARSING_SCHEMA_NAME', 'AUTO_CAPTURE_MODULE', 'AUTO_CAPTURE_ACTION'

`values_to_include`

(optional) A list of filter values to include.

`values_to_exclude`

(optional) A list of filter values to exclude.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SUMMARY_T Type

The AWR summary for a database.

Syntax
```

```

Fields

Field Description

`awr_db_id`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`db_name`

(required) The name of the database.

`instance_list`

(optional) The database instance numbers.

`time_db_startup`

(optional) The timestamp of the database startup.

`time_first_snapshot_begin`

(optional) The start time of the earliest snapshot.

`time_latest_snapshot_end`

(optional) The end time of the latest snapshot.

`first_snapshot_id`

(optional) The ID of the earliest snapshot. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

`latest_snapshot_id`

(optional) The ID of the latest snapshot. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

`snapshot_count`

(optional) The total number of snapshots.

`snapshot_interval_in_min`

(optional) The interval time between snapshots (in minutes).

`container_id`

(optional) ID of the database container. The database container ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`db_version`

(optional) The version of the database.

`snapshot_timezone`

(optional) The time zone of the snapshot.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_QUERY_RESULT_T Type

The AWR query result.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the query result.

`version`

(optional) The version of the query result.

`query_key`

(optional) The ID assigned to the query instance.

`db_query_time_in_secs`

(optional) The time taken to query the database tier (in seconds).

`awr_result_type`

(required) The result type of AWR query.

Allowed values are: 'AWRDB_SET', 'AWRDB_SNAPSHOT_RANGE_SET', 'AWRDB_SNAPSHOT_SET', 'AWRDB_METRICS_SET', 'AWRDB_SYSSTAT_SET', 'AWRDB_TOP_EVENT_SET', 'AWRDB_EVENT_SET', 'AWRDB_EVENT_HISTOGRAM', 'AWRDB_DB_PARAMETER_SET', 'AWRDB_DB_PARAMETER_CHANGE', 'AWRDB_ASH_CPU_USAGE_SET', 'AWRDB_DB_REPORT', 'AWRDB_SQL_REPORT'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_COLLECTION_T Type

The result of AWR query.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_CPU_USAGE_SUMMARY_T Type

A summary of the AWR CPU resource limits and metrics.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(optional) The timestamp for the CPU summary data.

`avg_value`

(optional) The average CPU usage per second.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_CPU_USAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_cpu_usage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_CPU_USAGE_COLLECTION_T Type

The AWR CPU usage data.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_cpu_usage_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`num_cpu_cores`

(optional) The number of available CPU cores, which include subcores of multicore and single-core CPUs.

`cpu_count`

(optional) The number of CPUs available for the database to use.

`num_cpus`

(optional) The number of available CPUs or processors.

`items`

(optional) A list of AWR CPU usage summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_METRIC_SUMMARY_T Type

The summary of the AWR metric data for a particular metric at a specific time.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the metric.

`l_timestamp`

(optional) The time of the sampling.

`avg_value`

(optional) The average value of the sampling period.

`min_value`

(optional) The minimum value of the sampling period.

`max_value`

(optional) The maximum value of the sampling period.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_METRIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_metric_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_METRIC_COLLECTION_T Type

The AWR metrics time series summary data.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_metric_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR metric summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_CHANGE_SUMMARY_T Type

A summary of the changes made to a single AWR database parameter.

Syntax
```

```

Fields

Field Description

`time_begin`

(optional) The start time of the interval.

`time_end`

(optional) The end time of the interval.

`instance_number`

(optional) The database instance number.

`previous_value`

(optional) The previous value of the database parameter.

`value`

(optional) The current value of the database parameter.

`snapshot_id`

(required) The ID of the snapshot with the parameter value changed. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

`value_modified`

(optional) Indicates whether the parameter has been modified after instance startup: - MODIFIED - Parameter has been modified with ALTER SESSION - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions’ values to be modified) - FALSE - Parameter has not been modified after instance startup

`is_default`

(optional) Indicates whether the parameter value in the end snapshot is the default.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_CHANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_parameter_change_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_CHANGE_COLLECTION_T Type

The AWR database parameter change history.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_parameter_change_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR database parameter change summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_SUMMARY_T Type

The summary of the AWR change history data for a single database parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the parameter.

`instance_number`

(optional) The database instance number.

`begin_value`

(optional) The parameter value when the period began.

`end_value`

(optional) The parameter value when the period ended.

`is_changed`

(optional) Indicates whether the parameter value changed within the period.

`value_modified`

(optional) Indicates whether the parameter has been modified after instance startup: - MODIFIED - Parameter has been modified with ALTER SESSION - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions’ values to be modified) - FALSE - Parameter has not been modified after instance startup

`is_default`

(optional) Indicates whether the parameter value in the end snapshot is the default.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_parameter_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_COLLECTION_T Type

The AWR database parameter data.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_parameter_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR database parameter summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_REPORT_T Type

The result of the AWR report.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_report_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`content`

(optional) The content of the report.

`format`

(optional) The format of the report.

Allowed values are: 'HTML', 'TEXT', 'XML'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_SUMMARY_T Type

The AWR snapshot summary of one snapshot.

Syntax
```

```

Fields

Field Description

`awr_db_id`

(required) Internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`instance_number`

(optional) The database instance number.

`time_db_startup`

(optional) The timestamp of the database startup.

`time_begin`

(optional) The start time of the snapshot.

`time_end`

(optional) The end time of the snapshot.

`snapshot_id`

(required) The ID of the snapshot. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

`error_count`

(optional) The total number of errors.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_snapshot_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_COLLECTION_T Type

The list of AWR snapshots for one database.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_snapshot_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR snapshot summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_RANGE_SUMMARY_T Type

The summary data for a range of AWR snapshots.

Syntax
```

```

Fields

Field Description

`awr_db_id`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`db_name`

(required) The name of the database.

`instance_list`

(optional) The database instance numbers.

`time_db_startup`

(optional) The timestamp of the database startup.

`time_first_snapshot_begin`

(optional) The start time of the earliest snapshot.

`time_latest_snapshot_end`

(optional) The end time of the latest snapshot.

`first_snapshot_id`

(optional) The ID of the earliest snapshot. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

`latest_snapshot_id`

(optional) The ID of the latest snapshot. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

`snapshot_count`

(optional) The total number of snapshots.

`snapshot_interval_in_min`

(optional) The interval time between snapshots (in minutes).

`container_id`

(optional) ID of the database container. The database container ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`db_version`

(optional) The version of the database.

`snapshot_timezone`

(optional) The time zone of the snapshot.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_RANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_snapshot_range_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_RANGE_COLLECTION_T Type

The AWR snapshot range list.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_snapshot_range_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR snapshot range summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SQL_REPORT_T Type

The result of the AWR SQL report.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_sql_report_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`content`

(optional) The content of the report.

`format`

(optional) The format of the report.

Allowed values are: 'HTML', 'TEXT'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SYSSTAT_SUMMARY_T Type

The summary of the AWR SYSSTAT data.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the SYSSTAT.

`category`

(optional) The name of the SYSSTAT category.

`time_begin`

(optional) The start time of the SYSSTAT.

`time_end`

(optional) The end time of the SYSSTAT.

`avg_value`

(optional) The average value of the SYSSTAT.

`current_value`

(optional) The last value of the SYSSTAT.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SYSSTAT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_sysstat_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SYSSTAT_COLLECTION_T Type

The AWR SYSSTAT time series summary data.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_sysstat_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR SYSSTAT summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_TOP_WAIT_EVENT_SUMMARY_T Type

A summary of the AWR top wait event data for one event.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the event.

`waits_per_sec`

(optional) The wait count per second.

`avg_wait_time_per_sec`

(optional) The average wait time per second.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_TOP_WAIT_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_top_wait_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_TOP_WAIT_EVENT_COLLECTION_T Type

The AWR top wait event data.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_top_wait_event_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR top event summary data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_BUCKET_SUMMARY_T Type

A summary of the AWR wait event bucket and waits percentage.

Syntax
```

```

Fields

Field Description

`category`

(required) The name of the wait event frequency category. Normally, it is the upper range of the waits within the AWR wait event bucket.

`percentage`

(required) The percentage of waits in a wait event bucket over the total waits of the database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_BUCKET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_wait_event_bucket_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_BUCKET_COLLECTION_T Type

The percentage distribution of waits in the AWR wait event buckets.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_wait_event_bucket_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`total_waits`

(optional) The total waits of the database.

`items`

(optional) A list of AWR wait event buckets.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_SUMMARY_T Type

The summary of the AWR wait event time series data for one event.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the event.

`time_begin`

(optional) The begin time of the wait event.

`time_end`

(optional) The end time of the wait event.

`waits_per_sec`

(optional) The wait count per second.

`avg_wait_time_per_sec`

(optional) The average wait time per second.

`avg_wait_time_per_wait`

(optional) The average wait time in milliseconds per wait.

`snapshot_id`

(optional) The ID of the snapshot. The snapshot ID is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_awr_db_wait_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_COLLECTION_T Type

The AWR wait event data.

Syntax
```

```

`dbms_cloud_oci_database_management_awr_db_wait_event_collection_t`is a subtype of the`dbms_cloud_oci_database_management_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR wait events.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_T Type

The details of the preferred credential.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of preferred credential. Only 'BASIC' is supported currently.

Allowed values are: 'BASIC'

`l_credential_name`

(optional) The name of the preferred credential.

`status`

(optional) The status of the preferred credential.

Allowed values are: 'SET', 'NOT_SET'

`is_accessible`

(optional) Indicates whether the preferred credential is accessible.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_BASIC_PREFERRED_CREDENTIAL_T Type

The details of the 'BASIC' preferred credential.

Syntax
```

```

`dbms_cloud_oci_database_management_basic_preferred_credential_t`is a subtype of the`dbms_cloud_oci_database_management_preferred_credential_t`type.

Fields

Field Description

`user_name`

(optional) The user name used to connect to the database.

`role`

(optional) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Vault service secret that contains the database user password.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DATABASE_PARAMETER_DETAILS_T Type

The value of a database parameter to change.

Syntax
```

```

Fields

Field Description

`name`

(required) The parameter name.

`value`

(required) The parameter value.

`update_comment`

(optional) A comment string to associate with the change in parameter value. It cannot contain control characters or a line break.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CREDENTIALS_T Type

The database credentials used to perform management activity.

Syntax
```

```

Fields

Field Description

`user_name`

(optional) The database user name used to perform management activity.

`password`

(optional) The password for the database user name.

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

`role`

(optional) The role of the database user. Indicates whether the database user is a normal user or sysdba.

Allowed values are: 'NORMAL', 'SYSDBA'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DATABASE_PARAMETER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_management_change_database_parameter_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DATABASE_PARAMETERS_DETAILS_T Type

The details required to change database parameter values.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

`scope`

(required) The clause used to specify when the parameter change takes effect. Use `MEMORY` to make the change in memory and affect it immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.

Allowed values are: 'MEMORY', 'SPFILE', 'BOTH'

`parameters`

(required) A list of database parameters and their values.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DB_MANAGEMENT_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

The details used to move the Database Management private endpoint to another compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which the Database Management private endpoint needs to be moved.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_EXTERNAL_DB_SYSTEM_COMPARTMENT_DETAILS_T Type

The details required to change the compartment of an external DB system.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the external DB system to.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_EXTERNAL_EXADATA_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type

The details required to change the compartment of the Exadata infrastructure.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the Exadata infrastructure and related components to.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_JOB_COMPARTMENT_DETAILS_T Type

The details required to change the compartment of a job.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which the job should be moved.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_MANAGED_DATABASE_GROUP_COMPARTMENT_DETAILS_T Type

The details required to change the compartment of a Managed Database Group.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which the Managed Database Group should be moved.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_CREDENTIAL_T Type

The credential used to connect to the Managed Database and obtain the details of the optimizer statistics tasks.

Syntax
```

```

Fields

Field Description

`credential_type`

(required) Indicates the type of credential required to retrieve the details of the optimizer statistics tasks.

Allowed values are: 'SECRET', 'PASSWORD'

`username`

(required) The user name used to connect to the database.

`role`

(required) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_PLAN_RETENTION_DETAILS_T Type

The details required to change the plan retention period.

Syntax
```

```

Fields

Field Description

`retention_weeks`

(required) The retention period in weeks. It can range between 5 and 523 weeks.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_SPACE_BUDGET_DETAILS_T Type

The details required to change the disk space limit for the SQL Management Base.

Syntax
```

```

Fields

Field Description

`space_budget_percent`

(required) The maximum percent of `SYSAUX` space that the SQL Management Base can use.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_SQL_PLAN_BASELINES_ATTRIBUTES_DETAILS_T Type

The details required to change SQL plan baseline attributes.

Syntax
```

```

Fields

Field Description

`sql_handle`

(optional) The SQL statement handle. It identifies plans associated with a SQL statement for attribute changes. If `null` then `planName` must be specified.

`plan_name`

(optional) Then plan name. It identifies a specific plan. If `null' then all plans associated with a SQL statement identified by `sqlHandle' are considered for attribute changes.

`is_enabled`

(optional) Indicates whether the plan is available for use by the optimizer.

`is_fixed`

(optional) Indicates whether the plan baseline is fixed. A fixed plan takes precedence over a non-fixed plan.

`is_auto_purged`

(optional) Indicates whether the plan is purged if it is not used for a time period.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHILD_DATABASE_T Type

The child Managed Database of a Managed Database Group.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(required) The name of the Managed Database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the Managed Database resides.

`deployment_type`

(optional) The infrastructure used to deploy the Oracle Database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`time_added`

(required) The date and time the Managed Database was added to the group.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_CREDENTIAL_DETAILS_T Type

The credential used to connect to the database.

Syntax
```

```

Fields

Field Description

`sql_tuning_task_credential_type`

(required) The type of credential for the SQL tuning task.

Allowed values are: 'SECRET', 'PASSWORD'

`username`

(required) The user name used to connect to the database.

`role`

(required) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CLONE_SQL_TUNING_TASK_DETAILS_T Type

The request to clone and run a SQL tuning task. The new task uses the same inputs as the one being cloned.

Syntax
```

```

Fields

Field Description

`task_name`

(required) The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.

`original_task_id`

(required) The identifier of the SQL tuning task being cloned. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint`LIST_SQL_TUNING_ADVISOR_TASKS`Function.

`task_description`

(optional) The description of the SQL tuning task.

`credential_details`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DATA_POINT_T Type

The metric values with dimension details.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) The date and time the metric was created.

`value`

(required) The value of the metric.

`unit`

(required) The unit of the metric value.

`dimensions`

(optional) The dimensions of the metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DATA_POINT_TBL Type

Nested table type of dbms_cloud_oci_database_management_time_series_metric_data_point_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DEFINITION_T Type

The response object representing time series metric details for a specific Managed Database at a particular time.

Syntax
```

```

Fields

Field Description

`metric_name`

(required) The name of the metric the time series data corresponds to.

`datapoints`

(required) The time series metric data for the given metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_time_series_metric_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CLUSTER_CACHE_METRIC_T Type

The response containing the cluster cache metrics for the Oracle Real Application Clusters (Oracle RAC) database.

Syntax
```

```

Fields

Field Description

`cluster_cache_metrics`

(required) A list of cluster cache metrics for a specific Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_management_automatic_capture_filter_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONFIGURE_AUTOMATIC_CAPTURE_FILTERS_DETAILS_T Type

The details required to configure automatic capture filters.

Syntax
```

```

Fields

Field Description

`auto_capture_filters`

(required) The filters used in automatic initial plan capture.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SPM_EVOLVE_TASK_PARAMETERS_T Type

The set of parameters used in an SPM evolve task.

Syntax
```

```

Fields

Field Description

`alternate_plan_sources`

(optional) Determines which sources to search for additional plans.

Allowed values are: 'AUTO', 'AUTOMATIC_WORKLOAD_REPOSITORY', 'CURSOR_CACHE', 'SQL_TUNING_SET'

`alternate_plan_baselines`

(optional) Determines which alternative plans should be loaded.

Allowed values are: 'AUTO', 'EXISTING', 'NEW'

`alternate_plan_limit`

(optional) Specifies the maximum number of plans to load in total (that is, not the limit for each SQL statement). A value of zero indicates `UNLIMITED` number of plans.

`are_plans_auto_accepted`

(optional) Specifies whether to accept recommended plans automatically.

`allowed_time_limit`

(optional) The global time limit in seconds. This is the total time allowed for the task.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONFIGURE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type

The configuration details of the Automatic SPM Evolve Advisor task.

Syntax
```

```

Fields

Field Description

`task_parameters`

(required)

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONSUMER_GROUP_PRIVILEGE_SUMMARY_T Type

A summary of consumer group privileges.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the granted consumer group privilege.

`grant_option`

(optional) Indicates whether the privilege is granted with the GRANT option (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`initial_group`

(optional) Indicates whether the consumer group is designated as the default for this user or role (YES) or not (NO).

Allowed values are: 'YES', 'NO'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONSUMER_GROUP_PRIVILEGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_consumer_group_privilege_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONSUMER_GROUP_PRIVILEGE_COLLECTION_T Type

A collection of consumer group privileges granted to the current user.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of consumer group privileges.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_STATISTICS_DEFINITION_T Type

The metric statistics values with dimension details.

Syntax
```

```

Fields

Field Description

`l_min`

(optional) The minimum value of the metric.

`l_max`

(optional) The maximum value of the metric.

`median`

(optional) The median value of the metric.

`lower_quartile`

(optional) The first quartile value of the metric.

`upper_quartile`

(optional) The third quartile value of the metric.

`unit`

(optional) The unit of the metric value.

`dimensions`

(optional) The dimensions of the metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CPU_UTILIZATION_AGGREGATE_METRICS_T Type

The CPU utilization metrics for Autonomous Databases.

Syntax
```

```

Fields

Field Description

`cpu_utilization`

(optional)

`cpu_statistics`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_DB_MANAGEMENT_PRIVATE_ENDPOINT_DETAILS_T Type

The details used to create a new Database Management private endpoint.

Syntax
```

```

Fields

Field Description

`name`

(required) The display name of the Database Management private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`is_cluster`

(optional) Specifies whether the Database Management private endpoint will be used for Oracle Databases in a cluster.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`description`

(optional) The description of the private endpoint.

`nsg_ids`

(optional) The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_CONNECTOR_DETAILS_T Type

The details required to create an external DB system connector.

Syntax
```

```

Fields

Field Description

`connector_type`

(required) The type of connector.

Allowed values are: 'MACS'

`display_name`

(optional) The user-friendly name for the external connector. The name does not have to be unique.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT_CONFIG_DETAILS_T Type

The details required to enable Database Management for an external DB system.

Syntax
```

```

Fields

Field Description

`license_model`

(required) The Oracle license model that applies to the external database.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_DETAILS_T Type

The details required to create an external DB system.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the DB system. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the external DB system resides.

`db_system_discovery_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system discovery.

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_DISCOVERY_DETAILS_T Type

The details required to create an external DB system discovery resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the DB system. The name does not have to be unique.

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system discovery.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the external DB system resides.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTION_INFO_T Type

The connection details required to connect to an external DB system component.

Syntax
```

```

Fields

Field Description

`component_type`

(required) The component type.

Allowed values are: 'DATABASE', 'ASM'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_MACS_CONNECTOR_DETAILS_T Type

The details for creating an external connector that is used to connect to an external DB system component using the[Management Agent Cloud Service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html).

Syntax
```

```

`dbms_cloud_oci_database_management_create_external_db_system_macs_connector_details_t`is a subtype of the`dbms_cloud_oci_database_management_create_external_db_system_connector_details_t`type.

Fields

Field Description

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system connector.

`connection_info`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_EXADATA_INFRASTRUCTURE_DETAILS_T Type

The details required to create the external Exadata infrastructure.

Syntax
```

```

Fields

Field Description

`discovery_key`

(optional) The unique key of the discovery request.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The name of the Exadata infrastructure.

`db_system_ids`

(required) The list of DB systems in the Exadata infrastructure.

`storage_server_names`

(optional) The list of all the Exadata storage server names to be included for monitoring purposes. If not specified, all the Exadata storage servers associated with the DB systems are included.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_REST_CREDENTIAL_T Type

The user credential information.

Syntax
```

```

Fields

Field Description

`username`

(required) The name of the user.

`password`

(required) The password of the user.

`ssl_trust_store_type`

(optional) The SSL truststore type.

Allowed values are: 'JKS', 'BCFKS'

`ssl_trust_store_location`

(optional) The full path of the SSL truststore location in the agent.

`ssl_trust_store_password`

(optional) The password of the SSL truststore location in the agent.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR_DETAILS_T Type

The details required to create the connector to the Exadata storage server.

Syntax
```

```

Fields

Field Description

`storage_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the agent for the Exadata storage server.

`connector_name`

(required) The name of the Exadata storage server connector.

`connection_uri`

(required) The unique string of the connection. For example, \"https://&lt;storage-server-name&gt;/MS/RESTService/\".

`credential_info`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_RESULT_LOCATION_T Type

The location of the job execution result.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the job execution result location.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_SCHEDULE_DETAILS_T Type

The details of the job schedule.

Syntax
```

```

Fields

Field Description

`start_time`

(optional) The start time of the scheduled job in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(optional) The end time of the scheduled job in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`interval_type`

(optional) The interval type for a recurring scheduled job. For a non-recurring (one time) job, NEVER must be specified as the interval type.

Allowed values are: 'DAILY', 'HOURLY', 'WEEKLY', 'MONTHLY', 'NEVER'

`interval_value`

(optional) The value for the interval period for a recurring scheduled job.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_JOB_DETAILS_T Type

The details required to create a job.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.

`description`

(optional) The description of the job.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the job resides.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the job has to be executed.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database where the job has to be executed.

`database_sub_type`

(optional) The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`schedule_type`

(required) The schedule type of the job.

`job_type`

(required) The type of job.

Allowed values are: 'SQL'

`timeout`

(optional) The job timeout duration, which is expressed like \"1h 10m 15s\".

`result_location`

(optional)

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_MANAGED_DATABASE_GROUP_DETAILS_T Type

The details required to create a Managed Database Group.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Managed Database Group. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the Managed Database Group cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.

`description`

(optional) The information specified by the user about the Managed Database Group.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the Managed Database Group resides.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_IN_BIND_T Type

The details of the job in-bind variable.

Syntax
```

```

Fields

Field Description

`position`

(required) The position of the in-bind variable.

`data_type`

(required) The datatype of the in-bind variable.

Allowed values are: 'NUMBER', 'STRING', 'CLOB'

`l_values`

(required) The values for the in-bind variable.

`array_type_name`

(optional) The Oracle schema object name for the predefined type of array.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_IN_BIND_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_in_bind_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_IN_BINDS_DETAILS_T Type

A collection of job in-bind variables.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JobInBind objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_OUT_BIND_T Type

The details of the job out-bind variable.

Syntax
```

```

Fields

Field Description

`position`

(required) The position of the out-bind variable.

`data_type`

(required) The datatype of the out-bind variable.

Allowed values are: 'NUMBER', 'STRING', 'CLOB'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_OUT_BIND_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_out_bind_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_OUT_BINDS_DETAILS_T Type

A collection of job out-bind variables.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JobOutBind objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_SQL_JOB_DETAILS_T Type

The details specific to the SQL job request.

Syntax
```

```

`dbms_cloud_oci_database_management_create_sql_job_details_t`is a subtype of the`dbms_cloud_oci_database_management_create_job_details_t`type.

Fields

Field Description

`sql_text`

(optional) The SQL text to be executed as part of the job.

`in_binds`

(optional)

`out_binds`

(optional)

`sql_type`

(optional)

`operation_type`

(required) The SQL operation type.

`user_name`

(optional) The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group, then the user name should exist on all the databases in the group with the same password.

`password`

(optional) The password for the database user name used to execute the SQL job.

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

`role`

(optional) The role of the database user. Indicates whether the database user is a normal user or sysdba.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_CREDENTIAL_DETAILS_T Type

The credential to connect to the database to perform Sql tuning set administration tasks.

Syntax
```

```

Fields

Field Description

`sql_tuning_set_admin_credential_type`

(required) The type of the credential for Sql tuning set administration tasks.

Allowed values are: 'SECRET', 'PASSWORD'

`username`

(required) The user to connect to the database.

`role`

(required) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_SQL_TUNING_SET_DETAILS_T Type

Create an empty Sql tuning sets.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`name`

(required) A unique Sql tuning set name.

`owner`

(optional) Owner of the Sql tuning set.

`description`

(optional) The description of the Sql tuning set.

`show_sql_only`

(optional) Flag to indicate whether to create the Sql tuning set or just display the plsql used to create Sql tuning set.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_TABLESPACE_DETAILS_T Type

The details required to create a tablespace.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`name`

(required) The name of the tablespace. It must be unique within a database.

`l_type`

(optional) The type of tablespace.

Allowed values are: 'PERMANENT', 'TEMPORARY'

`is_bigfile`

(optional) Specifies whether the tablespace is a bigfile or smallfile tablespace. A bigfile tablespace contains only one data file or temp file, which can contain up to approximately 4 billion (232) blocks. A smallfile tablespace is a traditional Oracle tablespace, which can contain 1022 data files or temp files, each of which can contain up to approximately 4 million (222) blocks.

`data_files`

(optional) The list of data files or temp files created for the tablespace.

`file_count`

(optional) The number of data files or temp files created for the tablespace. This is for Oracle Managed Files only.

`file_size`

(optional) The size of each data file or temp file.

`is_reusable`

(optional) Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.

`is_auto_extensible`

(optional) Specifies whether the data file or temp file can be extended automatically.

`auto_extend_next_size`

(optional) The size of the next increment of disk space to be allocated automatically when more extents are required.

`auto_extend_max_size`

(optional) The maximum disk space allowed for automatic extension of the data files or temp files.

`is_max_size_unlimited`

(optional) Specifies whether the disk space of the data file or temp file can be limited.

`block_size_in_kilobytes`

(optional) Block size for the tablespace.

`is_encrypted`

(optional) Indicates whether the tablespace is encrypted.

`encryption_algorithm`

(optional) The name of the encryption algorithm to be used for tablespace encryption.

`default_compress`

(optional) The default compression of data for all tables created in the tablespace.

Allowed values are: 'NO_COMPRESS', 'BASIC_COMPRESS'

`status`

(optional) The status of the tablespace.

Allowed values are: 'READ_ONLY', 'READ_WRITE'

`extent_management`

(optional) Specifies how the extents of the tablespace should be managed.

Allowed values are: 'AUTOALLOCATE', 'UNIFORM'

`extent_uniform_size`

(optional) The size of the extent when the tablespace is managed with uniform extents of a specific size.

`segment_management`

(optional) Specifies whether tablespace segment management should be automatic or manual.

Allowed values are: 'AUTO', 'MANUAL'

`is_default`

(optional) Specifies whether the tablespace is the default tablespace.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CURSOR_CACHE_STATEMENT_SUMMARY_T Type

The summary of a SQL statement in the cursor cache.

Syntax
```

```

Fields

Field Description

`sql_id`

(required) The SQL statement identifier. Identifies a SQL statement in the cursor cache.

`schema`

(required) The name of the parsing schema.

`sql_text`

(required) The first thousand characters of the SQL text.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CURSOR_CACHE_STATEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_cursor_cache_statement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CURSOR_CACHE_STATEMENT_COLLECTION_T Type

The list of SQL statements in the cursor cache.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SQL statements in the cursor cache.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATA_ACCESS_CONTAINER_SUMMARY_T Type

A summary of the ContainerDataAccess user.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the container included in the attribute.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATA_ACCESS_CONTAINER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_data_access_container_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATA_ACCESS_CONTAINER_COLLECTION_T Type

A collection of specific containers for the current user. This is only applicable if ALL_CONTAINERS !='Y'.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of container resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_CREDENTIALS_T Type

The credentials used to connect to the database. Currently only the `DETAILS` type is supported for creating MACS connector credentials.

Syntax
```

```

Fields

Field Description

`credential_type`

(optional) The type of credential used to connect to the database.

Allowed values are: 'NAME_REFERENCE', 'DETAILS', 'SSL_DETAILS'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_CREDENTAILS_BY_NAME_T Type

The existing named credential used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_database_connection_credentails_by_name_t`is a subtype of the`dbms_cloud_oci_database_management_database_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(required) The name of the credential information that used to connect to the DB system resource. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_CREDENTIALS_BY_DETAILS_T Type

The credentials used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_database_connection_credentials_by_details_t`is a subtype of the`dbms_cloud_oci_database_management_database_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(optional) The name of the credential information that used to connect to the DB system resource. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

`user_name`

(required) The user name used to connect to the database.

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

`role`

(required) The role of the user connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_STRING_T Type

The Oracle Database connection string.

Syntax
```

```

Fields

Field Description

`host_name`

(required) The host name of the database or the SCAN name in case of a RAC database.

`port`

(required) The port used to connect to the database.

`service`

(required) The service name of the database.

`protocol`

(required) The protocol used to connect to the database.

Allowed values are: 'TCP', 'TCPS'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_SUMMARY_DEFINITION_T Type

A summary of the fleet metrics, which provides the metric aggregated value of the databases in the fleet.

Syntax
```

```

Fields

Field Description

`metric_name`

(optional) The name of the metric.

`baseline_value`

(optional) The metric aggregated value at the baseline date and time.

`target_value`

(optional) The metric aggregated value at the target date and time.

`unit`

(optional) The unit of the value.

`percentage_change`

(optional) The percentage change in the metric aggregated value compared to the baseline value.

`dimensions`

(optional) The unique dimension key and values of the baseline metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_STATUS_BY_CATEGORY_T Type

The number of databases in the fleet, grouped by database type and sub type.

Syntax
```

```

Fields

Field Description

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) The infrastructure used to deploy the Oracle Database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`inventory_count`

(optional) The number of databases in the fleet.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_SUMMARY_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_fleet_metric_summary_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_STATUS_BY_CATEGORY_TBL Type

Nested table type of dbms_cloud_oci_database_management_fleet_status_by_category_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_SUMMARY_T Type

A summary of the inventory count grouped by database type and subtype, and the metrics that describe the aggregated usage of CPU, storage, and so on of all the databases in the fleet.

Syntax
```

```

Fields

Field Description

`aggregated_metrics`

(optional) A list of databases present in the fleet and their usage metrics.

`inventory`

(optional) A list of the databases in the fleet, grouped by database type and subtype.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_DEFINITION_T Type

The database metric details.

Syntax
```

```

Fields

Field Description

`metric_name`

(optional) The name of the metric.

`baseline_value`

(optional) The baseline value of the metric.

`target_value`

(optional) The target value of the metric.

`unit`

(optional) The unit of the value.

`l_timestamp`

(optional) The data point date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`percentage_change`

(optional) The percentage change in the metric aggregated value compared to the baseline value.

`dimensions`

(optional) The dimensions of the metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_fleet_metric_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_USAGE_METRICS_T Type

The list of aggregated metrics for Managed Databases in the fleet.

Syntax
```

```

Fields

Field Description

`db_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the Managed Database resides.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) The infrastructure used to deploy the Oracle Database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`database_version`

(optional) The Oracle Database version.

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`database_name`

(optional) The display name of the Managed Database.

`database_container_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent Container Database, in the case of a Pluggable Database.

`metrics`

(optional) A list of the database health metrics like CPU, Storage, and Memory.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_USAGE_METRICS_TBL Type

Nested table type of dbms_cloud_oci_database_management_database_usage_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_FLEET_HEALTH_METRICS_T Type

The details of the fleet health metrics.

Syntax
```

```

Fields

Field Description

`compare_baseline_time`

(required) The baseline date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\". This is the date and time against which percentage change is calculated.

`compare_target_time`

(required) The target date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\". All the metrics are returned for the target date and time and the percentage change is calculated against the baseline date and time.

`compare_type`

(optional) The time window used for metrics comparison.

Allowed values are: 'HOUR', 'DAY', 'WEEK'

`fleet_summary`

(optional)

`fleet_databases`

(required) A list of the databases present in the fleet and their usage metrics.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_TIME_AGGREGATE_METRICS_T Type

The database time metric details.

Syntax
```

```

Fields

Field Description

`cpu_count`

(optional)

`cpu_time`

(optional)

`wait_time`

(optional)

`user_io_time`

(optional)

`l_cluster`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DATA_POINT_TBL Type

Nested table type of dbms_cloud_oci_database_management_metric_data_point_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_STATISTICS_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_metric_statistics_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_IO_AGGREGATE_METRICS_T Type

The database Input/Output metric details.

Syntax
```

```

Fields

Field Description

`iops`

(optional) The Input/Output Operations Per Second metrics grouped by IOType for a specific Managed Database.

`io_throughput`

(optional) The IOThroughput metrics grouped by IOType for a specific Managed Database.

`iops_statistics`

(optional) The Input/Output metric statistics such as min, max, mean, lowerQuartile, and upperQuartile.

`io_throughput_statistics`

(optional) The IOThroughput metric statistics such as min, max, mean, lowerQuartile, and upperQuartile.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MEMORY_AGGREGATE_METRICS_T Type

The memory aggregate metric details.

Syntax
```

```

Fields

Field Description

`memory_usage`

(optional) The Memory Usage metrics grouped by memorypool for a specific Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_STORAGE_AGGREGATE_METRICS_T Type

The database storage metric values.

Syntax
```

```

Fields

Field Description

`storage_allocated`

(optional)

`storage_used`

(optional)

`storage_used_by_table_space`

(optional) A list of the storage metrics grouped by TableSpace for a specific Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_STATEMENTS_AGGREGATE_METRICS_T Type

The queued and running statement metrics for Autonomous Databases.

Syntax
```

```

Fields

Field Description

`queued_statements`

(optional)

`running_statements`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FAILED_CONNECTIONS_AGGREGATE_METRICS_T Type

The failed connection metrics for Autonomous Databases on Shared Exadata Infrastructure.

Syntax
```

```

Fields

Field Description

`failed_connections`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ACTIVITY_TIME_SERIES_METRICS_TBL Type

Nested table type of dbms_cloud_oci_database_management_activity_time_series_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_HOME_METRIC_DEFINITION_T Type

The response containing the CPU, Storage, Wait, DB Time, and Memory metrics for a specific Managed Database.

Syntax
```

```

Fields

Field Description

`activity_time_series_metrics`

(required) A list of the active session metrics for CPU and Wait time for a specific Managed Database.

`db_time_aggregate_metrics`

(required)

`io_aggregate_metrics`

(required)

`memory_aggregate_metrics`

(required)

`db_storage_aggregate_metrics`

(required)

`cpu_utilization_aggregate_metrics`

(optional)

`statements_aggregate_metrics`

(optional)

`failed_connections_aggregate_metrics`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_INSTANCE_HOME_METRICS_DEFINITION_T Type

The response containing the CPU, Wait, DB Time, and Memory metrics for a specific Oracle Real Application Clusters (Oracle RAC) database instance.

Syntax
```

```

Fields

Field Description

`instance_name`

(required) The name of the Oracle Real Application Clusters (Oracle RAC) database instance to which the corresponding metrics belong.

`instance_number`

(required) The number of Oracle Real Application Clusters (Oracle RAC) database instance to which the corresponding metrics belong.

`activity_time_series_metrics`

(required) A list of the active session metrics for CPU and Wait time for a specific Oracle Real Application Clusters (Oracle RAC) database instance.

`db_time_aggregate_metrics`

(required)

`io_aggregate_metrics`

(required)

`memory_aggregate_metrics`

(required)

`cpu_utilization_aggregate_metrics`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_INSTANCE_HOME_METRICS_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_database_instance_home_metrics_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_HOME_METRICS_T Type

The response containing the metric collection for a specific Managed Database.

Syntax
```

```

Fields

Field Description

`database_home_metrics`

(required)

`database_instance_home_metrics`

(optional) The metrics for the RAC database instances.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_MANAGEMENT_CONFIG_T Type

The configuration of the Database Management service.

Syntax
```

```

Fields

Field Description

`database_management_status`

(required) The status of the Database Management service.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database connector.

`license_model`

(required) The Oracle license model that applies to the external database.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALLOWED_PARAMETER_VALUE_TBL Type

Nested table type of dbms_cloud_oci_database_management_allowed_parameter_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETER_SUMMARY_T Type

A summary of the database parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The parameter name.

`l_type`

(required) The parameter type.

Allowed values are: 'BOOLEAN', 'STRING', 'INTEGER', 'FILENAME', 'BIG_INTEGER', 'RESERVED'

`value`

(required) The parameter value.

`display_value`

(required) The parameter value in a user-friendly format. For example, if the `value` property shows the value 262144 for a big integer parameter, then the `displayValue` property will show the value 256K.

`l_number`

(optional) The parameter number.

`is_default`

(optional) Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`).

`is_session_modifiable`

(optional) Indicates whether the parameter can be changed with `ALTER SESSION` (`TRUE`) or not (`FALSE`)

`is_system_modifiable`

(optional) Indicates whether the parameter can be changed with `ALTER SYSTEM` and when the change takes effect: - IMMEDIATE: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect immediately. - DEFERRED: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect in subsequent sessions. - FALSE: Parameter cannot be changed with `ALTER SYSTEM` unless a server parameter file was used to start the instance. The change takes effect in subsequent instances.

Allowed values are: 'IMMEDIATE', 'DEFERRED', 'FALSE'

`is_pdb_modifiable`

(optional) Indicates whether the parameter can be modified on a per-PDB basis (`TRUE`) or not (`FALSE`). In a non-CDB, the value of this property is `null`.

`is_instance_modifiable`

(optional) For parameters that can be changed with `ALTER SYSTEM`, indicates whether the value of the parameter can be different for every instance (`TRUE`) or whether the parameter must have the same value for all Real Application Clusters instances (`FALSE`). For other parameters, this is always `FALSE`.

`is_modified`

(optional) Indicates how the parameter was modified. If an `ALTER SYSTEM` was performed, the value will be `MODIFIED`.

Allowed values are: 'MODIFIED', 'FALSE'

`is_adjusted`

(optional) Indicates whether Oracle adjusted the input value to a more suitable value.

`is_deprecated`

(optional) Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`).

`is_basic`

(optional) Indicates whether the parameter is a basic parameter (`TRUE`) or not (`FALSE`).

`description`

(optional) The description of the parameter.

`ordinal`

(optional) The position (ordinal number) of the parameter value. Useful only for parameters whose values are lists of strings.

`update_comment`

(optional) The comments associated with the most recent update.

`container_id`

(optional) The ID of the database container to which the data pertains. Possible values include: - `0`: This value is used for data that pertain to the entire CDB. This value is also used for data in non-CDBs. - `1`: This value is used for data that pertain to only the root container. - `n`: Where n is the applicable container ID for the data.

`category`

(optional) The parameter category.

`constraint`

(optional) Applicable in case of Oracle Real Application Clusters (Oracle RAC) databases. A `UNIQUE` parameter is one which is unique to each Oracle Real Application Clusters (Oracle RAC) instance. For example, the parameter `INSTANCE_NUMBER` must have different values in each instance. An `IDENTICAL` parameter must have the same value for every instance. For example, the parameter `DB_BLOCK_SIZE` must have the same value in all instances.

Allowed values are: 'UNIQUE', 'IDENTICAL', 'NONE'

`sid`

(optional) The database instance SID for which the parameter is defined.

`is_specified`

(optional) Indicates whether the parameter was specified in the server parameter file (`TRUE`) or not (`FALSE`). Applicable only when the parameter source is `SPFILE`.

`allowed_values`

(optional) A list of allowed values for this parameter.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETER_UPDATE_STATUS_T Type

The result of database parameter update.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status of the parameter update.

Allowed values are: 'SUCCEEDED', 'FAILED'

`error_code`

(optional) An error code that defines the failure or `null` if the parameter was updated successfully.

`error_message`

(optional) The error message indicating the reason for failure or `null` if the parameter was updated successfully.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_database_parameter_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETERS_COLLECTION_T Type

A collection of database parameters.

Syntax
```

```

Fields

Field Description

`database_name`

(required) The name of the Managed Database.

`database_type`

(required) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(required) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`database_version`

(required) The Oracle Database version.

`items`

(required) An array of DatabaseParameterSummary objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PLAN_DIRECTIVE_T Type

Manages resource allocation among databases. Besides the name, at least one other property must be available.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of a database or a profile.

`l_share`

(optional) The relative priority of a database in the database plan. A higher share value implies higher priority and more access to the I/O resources. Use either share or (level, allocation). All plan directives in a database plan should use the same setting. Share-based resource allocation is the recommended method for a database plan.

`l_level`

(optional) The allocation level. Valid values are from 1 to 8. Resources are allocated to level 1 first, and then remaining resources are allocated to level 2, and so on.

`allocation`

(optional) The resource allocation as a percentage (0-100) within the level.

`limit`

(optional) The maximum I/O utilization limit as a percentage of the available resources.

`is_flash_cache_on`

(optional) Controls use of Exadata Smart Flash Cache by a database. This ensures that cache space is reserved for mission-critical databases. flashcache=off is invalid in a directive that contains the flashcachemin, flashcachelimit, or flashcachesize attributes.

`is_pmem_cache_on`

(optional) Controls use of the persistent memory (PMEM) cache by a database. This ensures that cache space is reserved for mission-critical databases. pmemcache=off is invalid in a directive that contains the pmemcachemin, pmemcachelimit, or pmemcachesize attributes.

`is_flash_log_on`

(optional) Controls use of Exadata Smart Flash Log by a database. This ensures that Exadata Smart Flash Log is reserved for mission-critical databases.

`is_pmem_log_on`

(optional) Controls use of persistent memory logging (PMEM log) by a database. This ensures that PMEM log is reserved for mission-critical databases.

`flash_cache_limit`

(optional) Defines a soft limit for space usage in Exadata Smart Flash Cache. If the cache is not full, the limit can be exceeded. You specify the value for flashcachelimit in bytes. You can also use the suffixes M (megabytes), G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T. The value for flashcachelimit must be at least 4 MB. The flashcachelimit and flashcachesize attributes cannot be specified in the same directive. The value for flashcachelimit cannot be smaller than flashcachemin, if it is specified.

`flash_cache_min`

(optional) Specifies a minimum guaranteed space allocation in Exadata Smart Flash Cache. You specify the value for flashcachemin in bytes. You can also use the suffixes M (megabytes), G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T. The value for flashcachemin must be at least 4 MB. In any plan, the sum of all flashcachemin values cannot exceed the size of Exadata Smart Flash Cache. If flashcachelimit is specified, then the value for flashcachemin cannot exceed flashcachelimit. If flashcachesize is specified, then the value for flashcachemin cannot exceed flashcachesize.

`flash_cache_size`

(optional) Defines a hard limit for space usage in Exadata Smart Flash Cache. The limit cannot be exceeded, even if the cache is not full. In an IORM plan, if the size of Exadata Smart Flash Cache can accommodate all of the flashcachemin and flashcachesize allocations, then each flashcachesize definition represents a guaranteed space allocation. However, starting with Oracle Exadata System Software release 19.2.0 you can use the flashcachesize attribute to over-provision space in Exadata Smart Flash Cache. Consequently, if the size of Exadata Smart Flash Cache cannot accommodate all of the flashcachemin and flashcachesize allocations, then only flashcachemin is guaranteed.

`pmem_cache_limit`

(optional) Defines a soft limit for space usage in the persistent memory (PMEM) cache. If the cache is not full, the limit can be exceeded. You specify the value for pmemcachelimit in bytes. You can also use the suffixes M (megabytes), G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T. The value for pmemcachelimit must be at least 4 MB. The pmemcachelimit and pmemcachesize attributes cannot be specified in the same directive. The value for pmemcachelimit cannot be smaller than pmemcachemin, if it is specified.

`pmem_cache_min`

(optional) Specifies a minimum guaranteed space allocation in the persistent memory (PMEM) cache.

`pmem_cache_size`

(optional) Defines a hard limit for space usage in the persistent memory (PMEM) cache. The limit cannot be exceeded, even if the cache is not full. In an IORM plan, if the size of the PMEM cache can accommodate all of the pmemcachemin and pmemcachesize allocations, then each pmemcachesize definition represents a guaranteed space allocation. However, you can use the pmemcachesize attribute to over-provision space in the PMEM cache. Consequently, if the PMEM cache size cannot accommodate all of the pmemcachemin and pmemcachesize allocations, then only pmemcachemin is guaranteed.

`asm_cluster`

(optional) Starting with Oracle Exadata System Software release 19.1.0, you can use the asmcluster attribute to distinguish between databases with the same name running in different Oracle ASM clusters.

`l_type`

(optional) Enables you to create a profile or template, to ease management and configuration of resource plans in environments with many databases. - type=database: Specifies a directive that applies to a specific database. If type in not specified, then the directive defaults to the database type. - type=profile: Specifies a directive that applies to a profile rather than a specific database. To associate a database with an IORM profile, you must set the database initialization parameter db_performance_profile to the value of the profile name. Databases that map to a profile inherit the settings specified in the profile.

Allowed values are: 'DATABASE', 'PROFILE', 'OTHER'

`role`

(optional) Enables you to specify different plan directives based on the Oracle Data Guard database role.

Allowed values are: 'PRIMARY', 'STANDBY', 'NONE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PLAN_DIRECTIVE_TBL Type

Nested table type of dbms_cloud_oci_database_management_database_plan_directive_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PLAN_T Type

The resource allocation directives must all use the share attribute, or they must all use the level and allocation attributes. If you use the share attribute to allocate I/O resources, then the database plan can have a maximum of 1024 directives. If you use the level and allocation attributes to allocate I/O resources, then the database plan can have a maximum of 32 directives. Only one directive is allowed for each database name and each profile name.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of DatabasePlanDirectives.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_SSL_CONNECTION_CREDENTIALS_T Type

The SSL connection credential details used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_database_ssl_connection_credentials_t`is a subtype of the`dbms_cloud_oci_database_management_database_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(optional) The name of the credential information that used to connect to the DB system resource. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

`user_name`

(required) The user name used to connect to the database.

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

`role`

(required) The role of the user connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

`ssl_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the SSL keystore and truststore details.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATAFILE_T Type

The details of a data file.

Syntax
```

```

Fields

Field Description

`name`

(required) The filename (including the path) of the data file or temp file.

`status`

(optional) The status of the file. INVALID status is used when the file number is not in use, for example, a file in a tablespace that was removed.

Allowed values are: 'AVAILABLE', 'INVALID', 'OFFLINE', 'ONLINE', 'UNKNOWN'

`online_status`

(optional) The online status of the file.

Allowed values are: 'SYSOFF', 'SYSTEM', 'OFFLINE', 'ONLINE', 'RECOVER'

`is_auto_extensible`

(optional) Indicates whether the data file is auto-extensible.

`lost_write_protect`

(optional) The lost write protection status of the file.

Allowed values are: 'ENABLED', 'PROTECT_OFF', 'SUSPEND'

`shared`

(optional) Type of tablespace this file belongs to. If it's for a shared tablespace, for a local temporary tablespace for RIM (read-only) instances, or for local temporary tablespace for all instance types.

Allowed values are: 'SHARED', 'LOCAL_FOR_RIM', 'LOCAL_FOR_ALL'

`instance_id`

(optional) Instance ID of the instance to which the temp file belongs. This column has a NULL value for temp files that belong to shared tablespaces.

`max_size_kb`

(optional) The maximum file size in KB.

`allocated_size_kb`

(optional) The allocated file size in KB.

`user_size_kb`

(optional) The size of the file available for user data in KB. The actual size of the file minus the USER_BYTES value is used to store file-related metadata.

`increment_by`

(optional) The number of blocks used as auto-extension increment.

`free_space_kb`

(optional) The free space available in the data file in KB.

`used_space_kb`

(optional) The total space used in the data file in KB.

`used_percent_available`

(optional) The percentage of used space out of the maximum available space in the file.

`used_percent_allocated`

(optional) The percentage of used space out of the total allocated space in the file.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_ANALYTICS_METRIC_T Type

The metric details of a Database Management resource.

Syntax
```

```

Fields

Field Description

`metric_name`

(optional) The name of the metric.

`duration_in_seconds`

(optional) The duration of the returned aggregated data in seconds.

`metadata`

(optional) The additional information about the metric. Example: `\"unit\": \"bytes\"`

`dimensions`

(optional) The qualifiers provided in the definition of the returned metric.

`start_timestamp_in_epoch_seconds`

(optional) The start time associated with the value of the metric.

`mean`

(optional) The mean value of the metric.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_T Type

A Database Management private endpoint allows Database Management to connect to databases in a Virtual Cloud Network (VCN).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`name`

(required) The display name of the Database Management private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`is_cluster`

(optional) Specifies whether the Database Management private endpoint can be used for Oracle Databases in a cluster.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`private_ip`

(optional) The IP addresses assigned to the Database Management private endpoint.

`description`

(optional) The description of the Database Management private endpoint.

`time_created`

(optional) The date and time the Database Managament private endpoint was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current lifecycle state of the Database Management private endpoint.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`nsg_ids`

(optional) The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_SUMMARY_T Type

The summary of a Database Management private endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`name`

(required) The display name of the Database Management private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`description`

(optional) The description of the private endpoint.

`time_created`

(optional) The date and time the private endpoint was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current lifecycle state of the private endpoint.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_db_management_private_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_COLLECTION_T Type

A collection of Database Management private endpoint objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of DbManagementPrivateEndpointSummary objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DBM_RESOURCE_T Type

The base Exadata resource.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata resource.

`display_name`

(required) The name of the Exadata resource. English letters, numbers, \"-\", \"_\" and \".\" only.

`version`

(optional) The version of the Exadata resource.

`internal_id`

(optional) The internal ID of the Exadata resource.

`status`

(optional) The status of the Exadata resource.

`lifecycle_state`

(optional) The current lifecycle state of the database resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(optional) The timestamp of the creation of the Exadata resource.

`time_updated`

(optional) The timestamp of the last update of the Exadata resource.

`lifecycle_details`

(optional) The details of the lifecycle state of the Exadata resource.

`additional_details`

(optional) The additional details of the resource defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

`resource_type`

(required) The type of Exadata resource.

Allowed values are: 'INFRASTRUCTURE_SUMMARY', 'INFRASTRUCTURE', 'STORAGE_SERVER_SUMMARY', 'STORAGE_SERVER', 'STORAGE_GRID_SUMMARY', 'STORAGE_GRID', 'STORAGE_CONNECTOR_SUMMARY', 'STORAGE_CONNECTOR', 'DATABASE_SYSTEM_SUMMARY', 'DATABASE_SUMMARY'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE_DETAILS_T Type

The details required to disable automatic initial plan capture.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type

The details required to disable Automatic SPM Evolve Advisor task.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type

The details required to disable high frequency Automatic SPM Evolve Advisor task.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_SQL_PLAN_BASELINES_USAGE_DETAILS_T Type

The details required to disable SQL plan baseline usage.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVER_EXTERNAL_EXADATA_INFRASTRUCTURE_DETAILS_T Type

The connection details and the discovery options for the Exadata discovery.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`discovery_type`

(required) The type of discovery.

Allowed values are: 'NEW', 'OVERRIDE'

`db_system_ids`

(required) The list of the DB system identifiers.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure. This is applicable for rediscovery only.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_COMPONENT_TBL Type

Nested table type of dbms_cloud_oci_database_management_associated_component_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_SYSTEM_COMPONENT_T Type

The details of an external DB system component.

Syntax
```

```

Fields

Field Description

`component_id`

(required) The identifier of the discovered DB system component.

`display_name`

(required) The user-friendly name for the discovered DB system component. The name does not have to be unique.

`component_name`

(required) The name of the discovered DB system component.

`component_type`

(required) The external DB system component type.

Allowed values are: 'ASM', 'ASM_INSTANCE', 'CLUSTER', 'CLUSTER_INSTANCE', 'DATABASE', 'DATABASE_INSTANCE', 'DATABASE_HOME', 'DATABASE_NODE', 'DBSYSTEM', 'LISTENER', 'PLUGGABLE_DATABASE'

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the existing OCI resource matching the discovered DB system component.

`is_selected_for_monitoring`

(optional) Indicates whether the DB system component should be provisioned as an OCI resource or not.

`status`

(optional) The state of the discovered DB system component.

Allowed values are: 'NEW', 'EXISTING', 'MARKED_FOR_DELETION', 'UNKNOWN'

`associated_components`

(optional) The list of associated components.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_ASM_INSTANCE_T Type

The details of an ASM instance discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_asm_instance_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`host_name`

(required) The name of the host on which the ASM instance is running.

`instance_name`

(optional) The name of the ASM instance.

`adr_home_directory`

(optional) The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_CONNECTOR_T Type

The connector details used to connect to the external DB system component.

Syntax
```

```

Fields

Field Description

`connector_type`

(required) The type of connector.

Allowed values are: 'MACS'

`display_name`

(required) The user-friendly name for the external connector. The name does not have to be unique.

`connection_status`

(optional) The status of connectivity to the external DB system component.

`connection_failure_message`

(optional) The error message indicating the reason for connection failure or `null` if the connection was successful.

`time_connection_status_last_updated`

(optional) The date and time the connectionStatus of the external DB system connector was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_ASM_INSTANCE_TBL Type

Nested table type of dbms_cloud_oci_database_management_discovered_external_asm_instance_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_ASM_T Type

The details of an ASM discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_asm_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`grid_home`

(optional) The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.

`is_flex_enabled`

(optional) Indicates whether Oracle Flex ASM is enabled or not.

`version`

(optional) The ASM version.

`asm_instances`

(optional)

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_NETWORK_CONFIGURATION_T Type

The details of a network address configuration in an external cluster.

Syntax
```

```

Fields

Field Description

`network_number`

(optional) The network number.

`network_type`

(optional) The network type.

Allowed values are: 'AUTOCONFIG', 'DHCP', 'STATIC', 'MIXED'

`subnet`

(optional) The subnet for the network.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_VIP_CONFIGURATION_T Type

The details of the Virtual IP (VIP) address for a node in an external cluster.

Syntax
```

```

Fields

Field Description

`node_name`

(optional) The name of the node with the VIP.

`address`

(optional) The VIP name or IP address.

`network_number`

(optional) The network number from which VIPs are obtained.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SCAN_LISTENER_CONFIGURATION_T Type

The details of a SCAN listener in an external cluster.

Syntax
```

```

Fields

Field Description

`scan_name`

(optional) The name of the SCAN listener.

`network_number`

(optional) The network number from which SCAN VIPs are obtained.

`scan_port`

(optional) The port number of the SCAN listener.

`scan_protocol`

(optional) The protocol of the SCAN listener.

Allowed values are: 'TCP', 'TCPS'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_CLUSTER_INSTANCE_T Type

The details of an external cluster instance discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_cluster_instance_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`host_name`

(required) The name of the host on which the cluster instance is running.

`cluster_id`

(optional) The unique identifier of the Oracle cluster.

`node_role`

(optional) The role of the cluster node.

Allowed values are: 'HUB', 'LEAF'

`crs_base_directory`

(optional) The Oracle base location of Cluster Ready Services (CRS).

`adr_home_directory`

(optional) The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_NETWORK_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_cluster_network_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_VIP_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_cluster_vip_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SCAN_LISTENER_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_cluster_scan_listener_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_CLUSTER_INSTANCE_TBL Type

Nested table type of dbms_cloud_oci_database_management_discovered_external_cluster_instance_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_CLUSTER_T Type

The details of an external cluster discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_cluster_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`grid_home`

(optional) The directory in which Oracle Grid Infrastructure is installed.

`version`

(optional) The version of Oracle Clusterware running in the cluster.

`is_flex_cluster`

(optional) Indicates whether the cluster is an Oracle Flex Cluster or not.

`network_configurations`

(optional) The list of network address configurations of the external cluster.

`vip_configurations`

(optional) The list of Virtual IP (VIP) configurations of the external cluster.

`scan_configurations`

(optional) The list of Single Client Access Name (SCAN) configurations of the external cluster.

`ocr_file_location`

(optional) The location of the Oracle Cluster Registry (OCR) file.

`cluster_instances`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_PLUGGABLE_DATABASE_T Type

The details of an external Pluggable Database (PDB) discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_pluggable_database_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`container_database_id`

(required) The unique identifier of the parent Container Database (CDB).

`guid`

(optional) The unique identifier of the PDB.

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_PLUGGABLE_DATABASE_TBL Type

Nested table type of dbms_cloud_oci_database_management_discovered_external_pluggable_database_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DATABASE_T Type

The details of an external Oracle Database discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_database_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`db_unique_name`

(required) The `DB_UNIQUE_NAME` of the external database.

`db_type`

(optional) The type of Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`is_cluster`

(optional) Indicates whether the Oracle Database is part of a cluster.

`db_edition`

(optional) The Oracle Database edition.

`db_id`

(optional) The Oracle Database ID.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`db_role`

(optional) The role of the Oracle Database in Oracle Data Guard configuration.

Allowed values are: 'LOGICAL_STANDBY', 'PHYSICAL_STANDBY', 'SNAPSHOT_STANDBY', 'PRIMARY', 'FAR_SYNC'

`db_version`

(optional) The Oracle Database version.

`pluggable_databases`

(optional) The list of Pluggable Databases.

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_HOME_T Type

The details of an Oracle DB home discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_db_home_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`home_directory`

(required) The location of the DB home.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_NODE_T Type

The details of an Oracle DB node discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_db_node_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`host_name`

(required) The name of the host on which the ASM instance is running.

`cpu_core_count`

(optional) The number of CPU cores available on the DB node.

`memory_size_in_g_bs`

(optional) The total memory in gigabytes (GB) on the DB node.

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_ENDPOINT_T Type

The protocol address that an external listener is configured to listen on.

Syntax
```

```

Fields

Field Description

`protocol`

(required) The listener protocol.

Allowed values are: 'IPC', 'TCP', 'TCPS'

`services`

(optional) The list of services registered with the listener.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_ENDPOINT_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_listener_endpoint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_LISTENER_T Type

The details of an Oracle listener discovered in an external DB system discovery run.

Syntax
```

```

`dbms_cloud_oci_database_management_discovered_external_listener_t`is a subtype of the`dbms_cloud_oci_database_management_discovered_external_db_system_component_t`type.

Fields

Field Description

`db_node_name`

(optional) The name of the DB node.

`oracle_home`

(optional) The Oracle home location of the listener.

`listener_alias`

(optional) The listener alias.

`adr_home_directory`

(optional) The directory that stores tracing and logging incidents when Automatic Diagnostic Repository (ADR) is enabled.

`log_directory`

(optional) The destination directory of the listener log file.

`trace_directory`

(optional) The destination directory of the listener trace file.

`version`

(optional) The listener version.

`listener_type`

(optional) The type of listener.

Allowed values are: 'ASM', 'LOCAL', 'SCAN'

`host_name`

(optional) The name of the host on which the external listener is running.

`endpoints`

(optional) The list of protocol addresses the listener is configured to listen on.

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQL_PLAN_BASELINES_DETAILS_T Type

The details required to drop SQL plan baselines.

Syntax
```

```

Fields

Field Description

`sql_handle`

(optional) The SQL statement handle. It identifies plans associated with a SQL statement that are to be dropped. If `null` then `planName` must be specified.

`plan_name`

(optional) The plan name. It identifies a specific plan. If `null' then all plans associated with the SQL statement identified by `sqlHandle' are dropped.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQL_TUNING_SET_DETAILS_T Type

The details required to drop a Sql tuning set.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`name`

(required) A unique Sql tuning set name.

`owner`

(optional) Owner of the Sql tuning set.

`show_sql_only`

(optional) Flag to indicate whether to drop the Sql tuning set or just display the plsql used to drop Sql tuning set.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQL_TUNING_TASK_DETAILS_T Type

The request to drop a SQL tuning task.

Syntax
```

```

Fields

Field Description

`task_id`

(required) The identifier of the SQL tuning task being dropped. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint`LIST_SQL_TUNING_ADVISOR_TASKS`Function.

`credential_details`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQLS_IN_SQL_TUNING_SET_DETAILS_T Type

Drops the selected list of Sql statements from the current Sql tuning set. The basicFilter parameter specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW. If a valid filter criteria is specified, then, Sql statements matching this filter criteria will be deleted from the current Sql tuning set. If filter criteria is not specified, then, all Sql statements will be deleted from the current Sql tuning set.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`show_sql_only`

(optional) Flag to indicate whether to drop the Sql statements or just display the plsql used to drop the Sql statements.

`owner`

(optional) The owner of the Sql tuning set.

`name`

(required) The name of the Sql tuning set.

`basic_filter`

(optional) Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW. User could use any combination of the following columns with appropriate values as Sql predicate Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_TABLESPACE_DETAILS_T Type

The details required to drop a tablespace.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`is_including_contents`

(optional) Specifies whether all the contents of the tablespace being dropped should be dropped.

`is_dropping_data_files`

(optional) Specifies whether all the associated data files of the tablespace being dropped should be dropped.

`is_cascade_constraints`

(optional) Specifies whether all the constraints on the tablespace being dropped should be dropped.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE_DETAILS_T Type

The details required to enable automatic initial plan capture.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type

The details required to enable Automatic SPM Evolve Advisor task.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT_DETAILS_T Type

The details required to enable Database Management for an external DB system.

Syntax
```

```

Fields

Field Description

`license_model`

(required) The Oracle license model that applies to the external database.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_EXTERNAL_DB_SYSTEM_STACK_MONITORING_DETAILS_T Type

The details required to enable Stack Monitoring for an external DB system.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) The status of the associated service.

`metadata`

(optional) The associated service-specific inputs in JSON string format, which Database Management can identify.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_EXTERNAL_EXADATA_INFRASTRUCTURE_MANAGEMENT_DETAILS_T Type

The details required to enable Database Management on the Exadata infrastructure.

Syntax
```

```

Fields

Field Description

`license_model`

(required) The Oracle license model.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type

The details required to enable high frequency Automatic SPM Evolve Advisor task.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_SQL_PLAN_BASELINES_USAGE_DETAILS_T Type

The details required to enable SQL plan baseline usage.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENTITY_DISCOVERED_T Type

The details of the base entity discovery.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the entity discovered.

`agent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the agent used for monitoring.

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated connector.

`display_name`

(required) The name of the entity.

`version`

(optional) The version of the entity.

`internal_id`

(optional) The internal identifier of the entity.

`status`

(optional) The status of the entity.

`discover_status`

(optional) The status of the entity discovery.

Allowed values are: 'PREV_DISCOVERED', 'NEW_DISCOVERED', 'NOT_FOUND', 'DISCOVERING'

`discover_error_code`

(optional) The error code of the discovery.

`discover_error_msg`

(optional) The error message of the discovery.

`entity_type`

(required) The type of discovered entities.

Allowed values are: 'STORAGE_SERVER_DISCOVER_SUMMARY', 'STORAGE_GRID_DISCOVER_SUMMARY', 'DATABASE_SYSTEM_DISCOVER_SUMMARY', 'INFRASTRUCTURE_DISCOVER_SUMMARY', 'INFRASTRUCTURE_DISCOVER'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_PLAN_STATS_T Type

The statistics of a SQL execution plan.

Syntax
```

```

Fields

Field Description

`plan_type`

(required) The type of the original or modified plan with profile, index, and so on.

`plan_stats`

(required) A map contains the statistics for the SQL execution using the plan. The key of the map is the metric's name. The value of the map is the metric's value.

`plan_status`

(required) The status of the execution using the plan.

Allowed values are: 'COMPLETE', 'PARTIAL'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXECUTION_PLAN_STATS_COMPARISION_T Type

The comparison report of the SQL execution plan statistics in the original and modified plan.

Syntax
```

```

Fields

Field Description

`original`

(required)

`modified`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SERVICED_DATABASE_T Type

The details of a database serviced by an external ASM.

Syntax
```

```

Fields

Field Description

`disk_groups`

(optional) The list of ASM disk groups used by the database.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database.

`display_name`

(required) The user-friendly name for the database. The name does not have to be unique.

`db_unique_name`

(optional) The unique name of the external database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the external database resides.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`is_managed`

(optional) Indicates whether the database is a Managed Database or not.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SERVICED_DATABASE_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_asm_serviced_database_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_T Type

The details of an external ASM.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`display_name`

(required) The user-friendly name for the external ASM. The name does not have to be unique.

`component_name`

(required) The name of the external ASM.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the ASM is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`grid_home`

(optional) The directory in which ASM is installed. This is the same directory in which Oracle Grid Infrastructure is installed.

`is_cluster`

(optional) Indicates whether the ASM is a cluster ASM or not.

`is_flex_enabled`

(optional) Indicates whether Oracle Flex ASM is enabled or not.

`lifecycle_state`

(required) The current lifecycle state of the external ASM.

Allowed values are: 'CREATING', 'NOT_CONNECTED', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`serviced_databases`

(optional) The list of databases that are serviced by the ASM.

`additional_details`

(optional) The additional details of the external ASM defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

`time_created`

(required) The date and time the external ASM was created.

`time_updated`

(required) The date and time the external ASM was last updated.

`version`

(optional) The ASM version.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SUMMARY_T Type

The summary of an external ASM.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`display_name`

(required) The user-friendly name for the external ASM. The name does not have to be unique.

`component_name`

(required) The name of the external ASM.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the ASM is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`lifecycle_state`

(required) The current lifecycle state of the external ASM.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external ASM was created.

`time_updated`

(required) The date and time the external ASM was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_asm_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_COLLECTION_T Type

A collection of external ASMs.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external ASMs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_PARAMETERS_T Type

The initialization parameters for an ASM instance.

Syntax
```

```

Fields

Field Description

`asm_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM instance.

`asm_instance_display_name`

(required) The user-friendly name for the ASM instance. The name does not have to be unique.

`disk_discovery_path`

(required) An operating system-dependent value used to limit the set of disks considered for discovery.

`auto_mount_disk_groups`

(required) The list of disk group names that an ASM instance mounts at startup or when the `ALTER DISKGROUP ALL MOUNT` statement is issued.

`rebalance_power`

(required) The maximum power on an ASM instance for disk rebalancing.

`preferred_read_failure_groups`

(required) The list of failure groups that contain preferred read disks.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_PARAMETERS_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_asm_instance_parameters_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_CONFIGURATION_T Type

The configuration details of an ASM.

Syntax
```

```

Fields

Field Description

`init_parameters`

(required) An array of initialization parameters for the external ASM instances.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_CONNECTION_INFO_T Type

The details required to connect to an external ASM instance.

Syntax
```

```

`dbms_cloud_oci_database_management_external_asm_connection_info_t`is a subtype of the`dbms_cloud_oci_database_management_external_db_system_connection_info_t`type.

Fields

Field Description

`connection_string`

(required)

`connection_credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_DISK_GROUP_SUMMARY_T Type

The summary of an external ASM disk group.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the ASM disk group.

`mounting_instance_count`

(optional) The number of ASM instances that have the disk group in mounted state.

`dismounting_instance_count`

(optional) The number of ASM instances that have the disk group in dismounted state.

`redundancy_type`

(optional) The redundancy type of the disk group.

Allowed values are: 'EXTEND', 'EXTERN', 'FLEX', 'HIGH', 'NORMAL'

`is_sparse`

(optional) Indicates whether the disk group is a sparse disk group or not.

`databases`

(optional) The unique names of the databases using the disk group.

`total_size_in_m_bs`

(optional) The total capacity of the disk group (in megabytes).

`used_size_in_m_bs`

(optional) The used capacity of the disk group (in megabytes).

`used_percent`

(optional) The percentage of used space in the disk group.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_DISK_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_asm_disk_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_DISK_GROUP_COLLECTION_T Type

A collection of external ASM disk groups.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external ASM disk groups.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_T Type

The details of an external ASM instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM instance.

`display_name`

(required) The user-friendly name for the ASM instance. The name does not have to be unique.

`component_name`

(required) The name of the external ASM instance.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM that the ASM instance belongs to.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the ASM instance is a part of.

`external_db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node on which the ASM instance is running.

`adr_home_directory`

(optional) The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.

`host_name`

(optional) The name of the host on which the ASM instance is running.

`lifecycle_state`

(required) The current lifecycle state of the external ASM instance.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the external ASM instance was created.

`time_updated`

(optional) The date and time the external ASM instance was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_SUMMARY_T Type

The summary of an external ASM instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM instance.

`display_name`

(required) The user-friendly name for the ASM instance. The name does not have to be unique.

`component_name`

(required) The name of the external ASM instance.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM that the ASM instance belongs to.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the ASM instance is a part of.

`external_db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node on which the ASM instance is running.

`adr_home_directory`

(optional) The Automatic Diagnostic Repository (ADR) home directory for the ASM instance.

`host_name`

(optional) The name of the host on which the ASM instance is running.

`lifecycle_state`

(required) The current lifecycle state of the external ASM instance.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the external ASM instance was created.

`time_updated`

(optional) The date and time the external ASM instance was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_asm_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_COLLECTION_T Type

A collection of external ASM instances.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external ASM instances.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_USER_SUMMARY_T Type

The summary of an ASM user.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the ASM user.

`privileges`

(required) The list of privileges of the ASM user.

`asm_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_asm_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_USER_COLLECTION_T Type

A collection of external ASM users.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external ASM users.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_T Type

The details of an external cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster.

`display_name`

(required) The user-friendly name for the external cluster. The name does not have to be unique.

`component_name`

(required) The name of the external cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the cluster is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`grid_home`

(optional) The directory in which Oracle Grid Infrastructure is installed.

`is_flex_cluster`

(optional) Indicates whether the cluster is Oracle Flex Cluster or not.

`additional_details`

(optional) The additional details of the external cluster defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

`lifecycle_state`

(required) The current lifecycle state of the external cluster.

Allowed values are: 'CREATING', 'NOT_CONNECTED', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`network_configurations`

(optional) The list of network address configurations of the external cluster.

`vip_configurations`

(optional) The list of Virtual IP (VIP) configurations of the external cluster.

`scan_configurations`

(optional) The list of Single Client Access Name (SCAN) configurations of the external cluster.

`ocr_file_location`

(optional) The location of the Oracle Cluster Registry (OCR).

`time_created`

(required) The date and time the external cluster was created.

`time_updated`

(required) The date and time the external cluster was last updated.

`version`

(optional) The cluster version.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SUMMARY_T Type

The summary of an external cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster.

`display_name`

(required) The user-friendly name for the external cluster. The name does not have to be unique.

`component_name`

(required) The name of the external cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the cluster is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`lifecycle_state`

(required) The current lifecycle state of the external cluster.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external cluster was created.

`time_updated`

(required) The date and time the external cluster was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_COLLECTION_T Type

A collection of external clusters.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external clusters.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_T Type

The details of an external cluster instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster instance.

`display_name`

(required) The user-friendly name for the cluster instance. The name does not have to be unique.

`component_name`

(required) The name of the external cluster instance.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster that the cluster instance belongs to.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the cluster instance is a part of.

`external_db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`host_name`

(optional) The name of the host on which the cluster instance is running.

`node_role`

(optional) The role of the cluster node.

Allowed values are: 'HUB', 'LEAF'

`crs_base_directory`

(optional) The Oracle base location of Cluster Ready Services (CRS).

`adr_home_directory`

(optional) The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.

`lifecycle_state`

(required) The current lifecycle state of the external cluster instance.

Allowed values are: 'CREATING', 'NOT_CONNECTED', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the external cluster instance was created.

`time_updated`

(optional) The date and time the external cluster instance was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_SUMMARY_T Type

The summary of an external cluster instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster instance.

`display_name`

(required) The user-friendly name for the cluster instance. The name does not have to be unique.

`component_name`

(required) The name of the external cluster instance.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster that the cluster instance belongs to.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the cluster instance is a part of.

`external_db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`host_name`

(optional) The name of the host on which the cluster instance is running.

`node_role`

(optional) The role of the cluster node.

`crs_base_directory`

(optional) The Oracle base location of Cluster Ready Services (CRS).

`adr_home_directory`

(optional) The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.

`lifecycle_state`

(required) The current lifecycle state of the external cluster instance.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the external cluster instance was created.

`time_updated`

(optional) The date and time the external cluster instance was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_cluster_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_COLLECTION_T Type

A collection of external cluster instances.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external cluster instances.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRA_BASIC_INFO_T Type

The basic information about an external Exadata Infrastructure.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external Exadata Infrastructure.

`display_name`

(required) The user-friendly name for the Exadata Infrastructure. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_BASIC_INFO_T Type

The basic information about an external DB system.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`exadata_infra_info`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_INSTANCE_T Type

The details of an external database instance.

Syntax
```

```

Fields

Field Description

`instance_number`

(required) The instance number of the database instance.

`instance_name`

(required) The name of the database instance.

`host_name`

(required) The name of the host machine.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_INSTANCE_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_database_instance_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SUMMARY_T Type

The summary of an external database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(required) The user-friendly name for the database. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or Non-container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`external_container_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent Container Database (CDB) if this is a Pluggable Database (PDB).

`external_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB home.

`db_system_info`

(optional)

`db_management_config`

(optional)

`instance_details`

(optional) The list of database instances if the database is a RAC database.

`lifecycle_state`

(required) The current lifecycle state of the external database resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the external DB system was created.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_database_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_COLLECTION_T Type

A collection of external databases.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external databases.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_CONNECTION_INFO_T Type

The details required to connect to an external Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_management_external_database_connection_info_t`is a subtype of the`dbms_cloud_oci_database_management_external_db_system_connection_info_t`type.

Fields

Field Description

`connection_string`

(required)

`connection_credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SYSTEM_DISCOVERY_SUMMARY_T Type

The summary of the DB system discovery.

Syntax
```

```

`dbms_cloud_oci_database_management_external_database_system_discovery_summary_t`is a subtype of the`dbms_cloud_oci_database_management_entity_discovered_t`type.

Fields

Field Description

`oracle_home`

(optional) The Oracle home path.

`asm_connector_name`

(optional) The display name of the ASM connector.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_T Type

The details of an external database home.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB home.

`display_name`

(required) The user-friendly name for the external DB home. The name does not have to be unique.

`component_name`

(optional) The name of the external DB home.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the DB home is a part of.

`home_directory`

(optional) The location of the DB home.

`additional_details`

(optional) The additional details of the DB home defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

`lifecycle_state`

(required) The current lifecycle state of the external DB home.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB home was created.

`time_updated`

(required) The date and time the external DB home was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_SUMMARY_T Type

The summary of an external database home.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB home.

`display_name`

(required) The user-friendly name for the external DB home. The name does not have to be unique.

`component_name`

(optional) The name of the external DB home.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the DB home is a part of.

`home_directory`

(optional) The location of the DB home.

`lifecycle_state`

(required) The current lifecycle state of the external DB home.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB home was created.

`time_updated`

(required) The date and time the external DB home was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_db_home_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_COLLECTION_T Type

A collection of external database homes.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external DB homes.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_T Type

The details of an external database node.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node.

`display_name`

(required) The user-friendly name for the external DB node. The name does not have to be unique.

`component_name`

(required) The name of the external DB node.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the DB node is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`host_name`

(optional) The host name for the DB node.

`cpu_core_count`

(optional) The number of CPU cores available on the DB node.

`memory_size_in_g_bs`

(optional) The total memory in gigabytes (GB) on the DB node.

`additional_details`

(optional) The additional details of the external DB node defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

`lifecycle_state`

(required) The current lifecycle state of the external DB node.

Allowed values are: 'CREATING', 'NOT_CONNECTED', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`domain_name`

(optional) Name of the domain.

`time_created`

(required) The date and time the external DB node was created.

`time_updated`

(required) The date and time the external DB node was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_SUMMARY_T Type

The summary of an external database node.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node.

`display_name`

(required) The user-friendly name for the external DB node. The name does not have to be unique.

`component_name`

(required) The name of the external DB node.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the DB node is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`host_name`

(optional) The host name for the DB node.

`lifecycle_state`

(required) The current lifecycle state of the external DB node.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB node was created.

`time_updated`

(required) The date and time the external DB node was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_db_node_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_COLLECTION_T Type

A collection of external database nodes.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external DB nodes.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_STACK_MONITORING_CONFIG_DETAILS_T Type

The configuration details of Stack Monitoring for an external DB system.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) The status of the associated service.

`metadata`

(optional) The associated service-specific inputs in JSON string format, which Database Management can identify.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_T Type

The details of an external DB system.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`db_system_discovery_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system discovery.

`discovery_agent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used during the discovery of the DB system.

`is_cluster`

(optional) Indicates whether the DB system is a cluster DB system or not.

`home_directory`

(optional) The Oracle Grid home directory in case of cluster-based DB system and Oracle home directory in case of single instance-based DB system.

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

`lifecycle_state`

(required) The current lifecycle state of the external DB system resource.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'INACTIVE'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB system was created.

`time_updated`

(required) The date and time the external DB system was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_SUMMARY_T Type

The summary of an external DB system.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`home_directory`

(optional) The Oracle Grid home directory in case of cluster-based DB system and Oracle home directory in case of single instance-based DB system.

`database_management_config`

(optional)

`lifecycle_state`

(required) The current lifecycle state of the external DB system resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB system was created.

`time_updated`

(required) The date and time the external DB system was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_db_system_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_COLLECTION_T Type

A collection of external DB systems.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external DB systems.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_T Type

The details of an external DB system connector.

Syntax
```

```

Fields

Field Description

`connector_type`

(required) The type of connector.

Allowed values are: 'MACS'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system connector.

`display_name`

(required) The user-friendly name for the external connector. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the connector is a part of.

`connection_status`

(optional) The status of connectivity to the external DB system component.

`connection_failure_message`

(optional) The error message indicating the reason for connection failure or `null` if the connection was successful.

`lifecycle_state`

(required) The current lifecycle state of the external DB system connector.

Allowed values are: 'CREATING', 'NOT_CONNECTED', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_connection_status_last_updated`

(optional) The date and time the connectionStatus of the external DB system connector was last updated.

`time_created`

(required) The date and time the external DB system connector was created.

`time_updated`

(required) The date and time the external DB system connector was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_SUMMARY_T Type

The summary of an external DB system connector.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system connector.

`display_name`

(required) The user-friendly name for the external connector. The name does not have to be unique.

`connector_type`

(required) The type of connector.

Allowed values are: 'MACS'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the connector is a part of.

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system connector.

`lifecycle_state`

(required) The current lifecycle state of the external DB system connector.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB system connector was created.

`time_updated`

(required) The date and time the external DB system connector was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_db_system_connector_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_COLLECTION_T Type

A collection of external DB system connectors.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external DB system connectors.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_SYSTEM_COMPONENT_TBL Type

Nested table type of dbms_cloud_oci_database_management_discovered_external_db_system_component_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_T Type

The details of an external DB system discovery.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system discovery.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system discovery.

`grid_home`

(optional) The directory in which Oracle Grid Infrastructure is installed.

`discovered_components`

(optional) The list of DB system components that were found in the DB system discovery.

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the existing OCI resource matching the discovered DB system.

`lifecycle_state`

(required) The current lifecycle state of the external DB system discovery resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB system discovery was created.

`time_updated`

(required) The date and time the external DB system discovery was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_SUMMARY_T Type

The summary of an external DB system.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system discovery.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system discovery.

`lifecycle_state`

(required) The current lifecycle state of the external DB system discovery resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external DB system discovery was created.

`time_updated`

(required) The date and time the external DB system discovery was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_db_system_discovery_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_COLLECTION_T Type

A collection of external DB system discovery summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external DB system discoveries.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_MACS_CONNECTOR_T Type

The details of an external DB system connector that uses the[Management Agent Cloud Service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html)to connect to an external DB system component.

Syntax
```

```

`dbms_cloud_oci_database_management_external_db_system_discovery_macs_connector_t`is a subtype of the`dbms_cloud_oci_database_management_external_db_system_discovery_connector_t`type.

Fields

Field Description

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system connector.

`connection_info`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_MACS_CONNECTOR_T Type

The details of an external DB system connector that uses the[Management Agent Cloud Service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html)to connect to an external DB system component.

Syntax
```

```

`dbms_cloud_oci_database_management_external_db_system_macs_connector_t`is a subtype of the`dbms_cloud_oci_database_management_external_db_system_connector_t`type.

Fields

Field Description

`agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management agent used for the external DB system connector.

`connection_info`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_DATABASE_SYSTEM_SUMMARY_T Type

The DB systems of the Exadata infrastructure.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_database_system_summary_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_GRID_SUMMARY_T Type

The Exadata storage server grid of the Exadata infrastructure.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_storage_grid_summary_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`server_count`

(optional) The number of Exadata storage servers in the Exadata infrastructure.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_DATABASE_SYSTEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_exadata_database_system_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_T Type

The details of the Exadata infrastructure.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_infrastructure_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`rack_size`

(optional) The rack size of the Exadata infrastructure.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH'

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`storage_grid`

(optional)

`database_systems`

(optional) A list of DB systems.

`database_compartments`

(optional) The list of[OCIDs]](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartments.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_SUMMARY_T Type

The Exadata infrastructure.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_infrastructure_summary_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`rack_size`

(optional) The rack size of the Exadata infrastructure.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`grid_home_path`

(optional) The Oracle grid home path.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_exadata_infrastructure_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_COLLECTION_T Type

A list of the Exadata infrastructure resources.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Exadata infrastructures.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_STORAGE_GRID_DISCOVERY_SUMMARY_T Type

The summary of the Exadata storage server grid discovery.

Syntax
```

```

`dbms_cloud_oci_database_management_external_storage_grid_discovery_summary_t`is a subtype of the`dbms_cloud_oci_database_management_entity_discovered_t`type.

Fields

Field Description

`count_of_storage_servers_discovered`

(optional) The total number of Exadata storage servers discovered.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_STORAGE_SERVER_DISCOVERY_SUMMARY_T Type

The summary of the Exadata storage server discovery.

Syntax
```

```

`dbms_cloud_oci_database_management_external_storage_server_discovery_summary_t`is a subtype of the`dbms_cloud_oci_database_management_entity_discovered_t`type.

Fields

Field Description

`ip_address`

(optional) The IP address of the Exadata storage server.

`make_model`

(optional) The make model of the Exadata storage server.

`cpu_count`

(optional) The CPU count of the Exadata storage server.

`memory_gb`

(optional) The memory size in GB of the Exadata storage server.

`connector_name`

(optional) The name of the Exadata storage server connector in case of rediscovery.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SYSTEM_DISCOVERY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_database_system_discovery_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_STORAGE_SERVER_DISCOVERY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_storage_server_discovery_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_DISCOVERY_T Type

The result of the Exadata infrastructure discovery.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_infrastructure_discovery_t`is a subtype of the`dbms_cloud_oci_database_management_entity_discovered_t`type.

Fields

Field Description

`discovery_key`

(required) The unique key of the discovery request.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`rack_size`

(optional) The size of the Exadata infrastructure.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH', 'UNKNOWN'

`grid_home_path`

(optional) The Oracle home path of the Exadata infrastructure.

`db_systems`

(optional) The list of DB systems in the Exadata infrastructure.

`storage_grid`

(optional)

`storage_servers`

(optional) The list of storage servers in the Exadata infrastructure.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_DISCOVERY_SUMMARY_T Type

The summary of the Exadata system infrastructure discovery.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_infrastructure_discovery_summary_t`is a subtype of the`dbms_cloud_oci_database_management_entity_discovered_t`type.

Fields

Field Description

`rack_size`

(optional) The size of the Exadata infrastructure.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_T Type

The details of the Exadata storage server connector.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_storage_connector_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`agent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the agent for the Exadata storage server.

`connection_uri`

(optional) The unique string of the connection. For example, \"https://&lt;storage-server-name&gt;/MS/RESTService/\".

`storage_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_SUMMARY_T Type

The connector of the Exadata storage server.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_storage_connector_summary_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`connection_uri`

(optional) The unique string of the connection. For example, \"https://&lt;storage-server-name&gt;/MS/RESTService/\".

`storage_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

`agent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the agent for the Exadata storage server.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_exadata_storage_connector_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_COLLECTION_T Type

The Exadata storage server connector list.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Exadata storage server connectors.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_STATUS_T Type

The status of an Exadata storage server connector.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server connector.

`status`

(required) The connection status of the connector.

Allowed values are: 'SUCCEEDED', 'FAILED'

`error_message`

(optional) The error message indicating the reason for failure or `null` if the connection was successful.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_SUMMARY_T Type

The Exadata storage server of the Exadata infrastructure.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_storage_server_summary_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`make_model`

(optional) The make model of the Exadata storage server.

`ip_address`

(optional) The IP address of the Exadata storage server.

`cpu_count`

(optional) The CPU count of the Exadata storage server.

`memory_gb`

(optional) The Exadata storage server memory size in GB.

`max_hard_disk_iops`

(optional) The maximum hard disk IO operations per second of the Exadata storage server.

`max_hard_disk_throughput`

(optional) The maximum hard disk IO throughput in MB/s of the Exadata storage server.

`max_flash_disk_iops`

(optional) The maximum flash disk IO operations per second of the Exadata storage server.

`max_flash_disk_throughput`

(optional) The maximum flash disk IO throughput in MB/s of the Exadata storage server.

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connector.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_exadata_storage_server_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_GRID_T Type

The details of the Exadata storage server grid.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_storage_grid_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`server_count`

(optional) The number of Exadata storage servers in the Exadata infrastructure.

`storage_servers`

(optional) A list of monitored Exadata storage servers.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_T Type

The details of the Exadata storage server.

Syntax
```

```

`dbms_cloud_oci_database_management_external_exadata_storage_server_t`is a subtype of the`dbms_cloud_oci_database_management_dbm_resource_t`type.

Fields

Field Description

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`storage_grid_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server grid.

`make_model`

(optional) The make model of the Exadata storage server.

`ip_address`

(optional) The IP address of the Exadata storage server.

`cpu_count`

(optional) The CPU count of the Exadata storage server.

`memory_gb`

(optional) The Exadata storage server memory size in GB.

`max_hard_disk_iops`

(optional) The maximum hard disk IO operations per second of the Exadata storage server.

`max_hard_disk_throughput`

(optional) The maximum hard disk IO throughput in MB/s of the Exadata storage server.

`max_flash_disk_iops`

(optional) The maximum flash disk IO operations per second of the Exadata storage server.

`max_flash_disk_throughput`

(optional) The maximum flash disk IO throughput in MB/s of the Exadata storage server.

`connector`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_COLLECTION_T Type

The Exadata storage server list.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Exadata storage servers.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICED_DATABASE_T Type

The details of a database serviced by an external listener.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database.

`display_name`

(required) The user-friendly name for the database. The name does not have to be unique.

`db_unique_name`

(optional) The unique name of the external database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the external database resides.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`is_managed`

(optional) Indicates whether the database is a Managed Database or not.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_SERVICED_ASM_T Type

The details of ASM serviced by an external listener.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`display_name`

(required) The user-friendly name for the external ASM. The name does not have to be unique.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the external ASM resides.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICED_DATABASE_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_listener_serviced_database_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_SERVICED_ASM_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_serviced_asm_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_T Type

The details of an external listener.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`display_name`

(required) The user-friendly name for the external listener. The name does not have to be unique.

`component_name`

(required) The name of the external listener.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the listener is a part of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`external_db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node.

`external_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB home.

`listener_alias`

(optional) The listener alias.

`listener_type`

(optional) The type of listener.

Allowed values are: 'ASM', 'LOCAL', 'SCAN'

`additional_details`

(optional) The additional details of the external listener defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

`lifecycle_state`

(required) The current lifecycle state of the external listener.

Allowed values are: 'CREATING', 'NOT_CONNECTED', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`listener_ora_location`

(optional) The location of the listener configuration file listener.ora.

`oracle_home`

(optional) The Oracle home location of the listener.

`host_name`

(optional) The name of the host on which the external listener is running.

`adr_home_directory`

(optional) The directory that stores tracing and logging incidents when Automatic Diagnostic Repository (ADR) is enabled.

`log_directory`

(optional) The destination directory of the listener log file.

`trace_directory`

(optional) The destination directory of the listener trace file.

`version`

(optional) The listener version.

`endpoints`

(optional) The list of protocol addresses the listener is configured to listen on.

`serviced_databases`

(optional) The list of databases that are serviced by the listener.

`serviced_asms`

(optional) The list of ASMs that are serviced by the listener.

`time_created`

(required) The date and time the external listener was created.

`time_updated`

(required) The date and time the external listener was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SUMMARY_T Type

The summary of an external listener.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`display_name`

(required) The user-friendly name for the external listener. The name does not have to be unique.

`component_name`

(required) The name of the external listener.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that the listener is a member of.

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`external_db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB node on which the listener is running.

`listener_type`

(optional) The type of listener.

`lifecycle_state`

(required) The current lifecycle state of the external listener.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external listener was created.

`time_updated`

(required) The date and time the external listener was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_listener_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_COLLECTION_T Type

A collection of external listeners.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external listeners.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_IPC_ENDPOINT_T Type

An `IPC`-based protocol address.

Syntax
```

```

`dbms_cloud_oci_database_management_external_listener_ipc_endpoint_t`is a subtype of the`dbms_cloud_oci_database_management_external_listener_endpoint_t`type.

Fields

Field Description

`key`

(required) The unique name of the service.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICE_SUMMARY_T Type

The summary of a service registered with an external listener.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the service.

`listener_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_external_listener_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICE_COLLECTION_T Type

A collection of external listener services.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of external listener services.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_TCP_ENDPOINT_T Type

A `TCP`-based protocol address.

Syntax
```

```

`dbms_cloud_oci_database_management_external_listener_tcp_endpoint_t`is a subtype of the`dbms_cloud_oci_database_management_external_listener_endpoint_t`type.

Fields

Field Description

`host`

(required) The host name or IP address.

`port`

(required) The port number.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_TCPS_ENDPOINT_T Type

A `TCPS`-based protocol address.

Syntax
```

```

`dbms_cloud_oci_database_management_external_listener_tcps_endpoint_t`is a subtype of the`dbms_cloud_oci_database_management_external_listener_endpoint_t`type.

Fields

Field Description

`host`

(required) The host name or IP address.

`port`

(required) The port number.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_SERVICED_DATABASE_T Type

The details of a database serviced by an external DB system component such as a listener or ASM.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database.

`display_name`

(required) The user-friendly name for the database. The name does not have to be unique.

`db_unique_name`

(optional) The unique name of the external database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the external database resides.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`is_managed`

(optional) Indicates whether the database is a Managed Database or not.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FETCH_SQL_TUNING_SET_DETAILS_T Type

The details required to fetch the Sql tuning set details.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`owner`

(required) The owner of the Sql tuning set.

`name`

(required) The name of the Sql tuning set.

`basic_filter`

(optional) Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW. User could use any combination of the following columns with appropriate values as Sql predicate Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C

`recursive_sql`

(optional) Specifies that the filter must include recursive Sql in the Sql tuning set.

Allowed values are: 'HAS_RECURSIVE_SQL', 'NO_RECURSIVE_SQL'

`result_percentage`

(optional) Specifies a filter that picks the top n% according to the supplied ranking measure. Note that this parameter applies only if one ranking measure is supplied.

`result_limit`

(optional) The top limit Sql from the filtered source, ranked by the ranking measure.

`ranking_measure1`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`ranking_measure2`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`ranking_measure3`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_HISTORIC_ADDM_RESULT_T Type

The details of the historic ADDM task.

Syntax
```

```

Fields

Field Description

`is_newly_created`

(optional) Specifies whether the ADDM task returned had already existed or was newly created by the api call.

`task_name`

(optional) The name of the historic ADDM task.

`task_id`

(required) The ID of the historic ADDM task.

`description`

(optional) The description of the ADDM task.

`db_user`

(optional) The database user who owns the historic ADDM task.

`status`

(optional) The status of the ADDM task.

Allowed values are: 'INITIAL', 'EXECUTING', 'INTERRUPTED', 'COMPLETED', 'ERROR'

`time_created`

(required) The creation date of the ADDM task.

`how_created`

(optional) A description of how the task was created.

Allowed values are: 'AUTO', 'MANUAL'

`start_snapshot_time`

(optional) The timestamp of the beginning AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.

`end_snapshot_time`

(optional) The timestamp of the ending AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.

`begin_snapshot_id`

(optional) The ID number of the beginning AWR snapshot.

`end_snapshot_id`

(optional) The ID number of the ending AWR snapshot.

`findings`

(optional) The number of ADDM findings.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_IMPLEMENT_OPTIMIZER_STATISTICS_ADVISOR_RECOMMENDATIONS_JOB_T Type

The job request details to implement the Optimizer Statistics Advisor task recommendations.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the job. Valid characters are uppercase or lowercase letters, numbers, and \"_\". The name of the job cannot be modified. It must be unique in the compartment and must begin with an alphabetic character.

`description`

(optional) The name of the execution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the job resides.

`result_location`

(required)

`credentials`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_IMPLEMENT_OPTIMIZER_STATISTICS_ADVISOR_RECOMMENDATIONS_DETAILS_T Type

The request details object to implement the Optimizer Statistics Advisor task recommendations.

Syntax
```

```

Fields

Field Description

`task_name`

(required) The name of the task.

`job_details`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_INSTANCE_DETAILS_T Type

The details of the Oracle Real Application Clusters (Oracle RAC) database instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the Oracle RAC database instance.

`name`

(required) The name of the Oracle RAC database instance.

`host_name`

(required) The name of the host of the Oracle RAC database instance.

`status`

(required) The status of the Oracle RAC database instance.

Allowed values are: 'UP', 'DOWN', 'UNKNOWN'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_IORM_PLAN_T Type

The IORM plan from an Exadata storage server.

Syntax
```

```

Fields

Field Description

`plan_status`

(required) The status of the IORM plan.

Allowed values are: 'ACTIVE', 'INACTIVE', 'OTHER'

`plan_objective`

(required) The objective of the IORM plan.

Allowed values are: 'AUTO', 'HIGH_THROUGHPUT', 'LOW_LATENCY', 'BALANCED', 'BASIC', 'OTHER'

`db_plan`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_DATABASE_T Type

The Managed Database on which the job is executed.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(required) The name of the Managed Database.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) A list of the supported infrastructure that can be used to deploy the database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`is_cluster`

(optional) Indicates whether the Oracle Database is part of a cluster.

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_DATABASE_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_database_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_T Type

The details of the job.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the job resides.

`name`

(required) The display name of the job.

`description`

(optional) The description of the job.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the job has to be executed.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database where the job has to be executed.

`managed_databases_details`

(optional) The details of the Managed Databases where the job has to be executed.

`database_sub_type`

(optional) The subtype of the Oracle Database where the job has to be executed. Applicable only when managedDatabaseGroupId is provided.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`schedule_type`

(required) The schedule type of the job.

Allowed values are: 'IMMEDIATE', 'LATER'

`job_type`

(required) The type of job.

Allowed values are: 'SQL'

`lifecycle_state`

(required) The lifecycle state of the job.

Allowed values are: 'ACTIVE', 'INACTIVE'

`timeout`

(optional) The job timeout duration, which is expressed like \"1h 10m 15s\".

`result_location`

(optional)

`schedule_details`

(optional)

`submission_error_message`

(optional) The error message that is returned if the job submission fails. Null is returned in all other scenarios.

`time_created`

(required) The date and time when the job was created.

`time_updated`

(required) The date and time when the job was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_SUMMARY_T Type

A summary of the job.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the job resides.

`name`

(required) The display name of the job.

`description`

(optional) The description of the job.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the job has to be executed.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database where the job has to be executed.

`database_sub_type`

(optional) The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`schedule_type`

(required) The schedule type of the job.

`schedule_details`

(optional)

`job_type`

(required) The type of job.

Allowed values are: 'SQL'

`lifecycle_state`

(required) The lifecycle state of the job.

`timeout`

(optional) The job timeout duration, which is expressed like \"1h 10m 15s\".

`submission_error_message`

(optional) The error message that is returned if the job submission fails. Null is returned in all other scenarios.

`time_created`

(required) The date and time when the job was created.

`time_updated`

(required) The date and time when the job was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_COLLECTION_T Type

A collection of job objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JobSummary objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_RESULT_DETAILS_T Type

The job execution result details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of job execution result.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_T Type

The details of a job execution.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the job execution.

`name`

(required) The name of the job execution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the parent job resides.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the parent job has to be executed.

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database associated with the job execution.

`managed_database_name`

(required) The name of the Managed Database associated with the job execution.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) A list of the supported infrastructure that can be used to deploy the database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`is_cluster`

(optional) Indicates whether the Oracle Database is part of a cluster.

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent job.

`job_name`

(required) The name of the parent job.

`job_run_id`

(required) The identifier of the associated job run.

`status`

(required) The status of the job execution.

Allowed values are: 'SUCCEEDED', 'FAILED', 'IN_PROGRESS'

`error_message`

(optional) The error message that is returned if the job execution fails. Null is returned if the job is still running or if the job execution is successful.

`result_details`

(optional)

`time_created`

(required) The date and time when the job execution was created.

`time_completed`

(optional) The date and time when the job execution completed.

`user_name`

(optional) The database user name used to execute the SQL job.

`sql_text`

(optional) The SQL text executed as part of the job.

`in_binds`

(optional)

`out_binds`

(optional)

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_SUMMARY_T Type

A summary of a job execution on a Managed Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the job execution.

`name`

(required) The name of the job execution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the parent job resides.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the parent job has to be executed.

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of Managed Database associated with the job execution.

`managed_database_name`

(required) The name of the Managed Database associated with the job execution.

`database_type`

(optional) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(optional) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) A list of the supported infrastructure that can be used to deploy the database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`is_cluster`

(optional) Indicates whether the Oracle Database is part of a cluster.

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent job.

`job_name`

(required) The name of the parent job.

`status`

(required) The status of the job execution.

`time_created`

(required) The date and time when the job execution was created.

`time_completed`

(optional) The date and time when the job execution was completed.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_execution_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_COLLECTION_T Type

A collection of job execution objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JobExecutionSummary objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTIONS_STATUS_SUMMARY_T Type

A summary of the status of the job executions.

Syntax
```

```

Fields

Field Description

`status`

(required) The status of the job execution.

Allowed values are: 'SUCCEEDED', 'FAILED', 'IN_PROGRESS'

`l_count`

(required) The number of job executions of a particular status.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTIONS_STATUS_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_executions_status_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTIONS_STATUS_SUMMARY_COLLECTION_T Type

A collection of job execution status summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JobExecutionsSummary objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_T Type

The details of a specific job run.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the job run.

`name`

(required) The name of the job run.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the parent job resides.

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent job.

`job_name`

(required) The name of the parent job.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the parent job has to be executed.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of Managed Database where the parent job has to be executed.

`run_status`

(required) The status of the job run.

Allowed values are: 'COMPLETED', 'FAILED', 'IN_PROGRESS'

`time_submitted`

(required) The date and time when the job run was submitted.

`time_updated`

(required) The date and time when the job run was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_SUMMARY_T Type

A summary of a specific job run.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the job run.

`name`

(required) The name of the job run.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the parent job resides.

`job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent job.

`job_name`

(required) The name of the parent job.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group where the parent job has to be executed.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database where the parent job has to be executed.

`run_status`

(required) The status of the job run.

`time_submitted`

(required) The date and time when the job run was submitted.

`time_updated`

(required) The date and time when the job run was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_job_run_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_COLLECTION_T Type

A collection of job run objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of JobRunSummary objects.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_LOAD_SQL_PLAN_BASELINES_FROM_AWR_DETAILS_T Type

The details required to load plans from Automatic Workload Repository (AWR).

Syntax
```

```

Fields

Field Description

`job_name`

(required) The name of the database job used for loading SQL plan baselines.

`job_description`

(optional) The description of the job.

`begin_snapshot`

(required) The begin snapshot.

`end_snapshot`

(required) The end snapshot.

`sql_text_filter`

(optional) A filter applied to AWR to select only qualifying plans to be loaded. By default all plans in AWR are selected. The filter can take the form of any `WHERE` clause predicate that can be specified against the column `DBA_HIST_SQLTEXT.SQL_TEXT`. An example is `sql_text like 'SELECT %'`.

`is_fixed`

(optional) Indicates whether the plans are loaded as fixed plans (`true`) or non-fixed plans (`false`). By default, they are loaded as non-fixed plans.

`is_enabled`

(optional) Indicates whether the loaded plans are enabled (`true`) or not (`false`). By default, they are enabled.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_LOAD_SQL_PLAN_BASELINES_FROM_CURSOR_CACHE_DETAILS_T Type

The details of SQL statements and plans to be loaded from cursor cache. You can specify the plans to load using SQL ID, plan identifier, or filterName and filterValue pair. You can also control the SQL plan baseline into which the plans are loaded using either SQL text or SQL handle.

Syntax
```

```

Fields

Field Description

`job_name`

(required) The name of the database job used for loading SQL plan baselines.

`job_description`

(optional) The description of the job.

`sql_id`

(optional) The SQL statement identifier. Identifies a SQL statement in the cursor cache.

`plan_hash`

(optional) The plan identifier. By default, all plans present in the cursor cache for the SQL statement identified by `sqlId` are captured.

`sql_text`

(optional) The SQL text to use in identifying the SQL plan baseline into which the plans are loaded. If the SQL plan baseline does not exist, it is created.

`sql_handle`

(optional) The SQL handle to use in identifying the SQL plan baseline into which the plans are loaded.

`filter_name`

(optional) The name of the filter. - SQL_TEXT: Search pattern to apply to SQL text. - PARSING_SCHEMA_NAME: Name of the parsing schema. - MODULE: Name of the module. - ACTION: Name of the action.

Allowed values are: 'SQL_TEXT', 'PARSING_SCHEMA_NAME', 'MODULE', 'ACTION'

`filter_value`

(optional) The filter value. It is upper-cased except when it is enclosed in double quotes or filter name is `SQL_TEXT`.

`is_fixed`

(optional) Indicates whether the plans are loaded as fixed plans (`true`) or non-fixed plans (`false`). By default, they are loaded as non-fixed plans.

`is_enabled`

(optional) Indicates whether the loaded plans are enabled (`true`) or not (`false`). By default, they are enabled.

`credentials`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_LOAD_SQL_TUNING_SET_DETAILS_T Type

The details required to load the Sql statements into the Sql tuning set.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`show_sql_only`

(optional) Flag to indicate whether to create the Sql tuning set or just display the plsql used to create Sql tuning set.

`owner`

(optional) The owner of the Sql tuning set.

`name`

(required) The name of the Sql tuning set.

`load_type`

(required) Specifies the loading method into the Sql tuning set.

Allowed values are: 'INCREMENTAL_CURSOR_CACHE', 'CURRENT_CURSOR_CACHE', 'AWR'

`basic_filter`

(optional) Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW. User could use any combination of the following columns with appropriate values as Sql predicate Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C

`recursive_sql`

(optional) Specifies that the filter must include recursive Sql in the Sql tuning set.

Allowed values are: 'HAS_RECURSIVE_SQL', 'NO_RECURSIVE_SQL'

`result_percentage`

(optional) Specifies a filter that picks the top n% according to the supplied ranking measure. Note that this parameter applies only if one ranking measure is supplied.

`result_limit`

(optional) The top limit Sql from the filtered source, ranked by the ranking measure.

`ranking_measure1`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`ranking_measure2`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`ranking_measure3`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`total_time_limit`

(optional) Defines the total amount of time, in seconds, to execute.

`repeat_interval`

(optional) Defines the amount of time, in seconds, to pause between sampling.

`capture_option`

(optional) Specifies whether to insert new statements, update existing statements, or both.

Allowed values are: 'INSERT', 'UPDATE', 'MERGE'

`capture_mode`

(optional) Specifies the capture mode. Note that this parameter is applicable only for UPDATE and MERGE capture options. Capture mode can take one of the following values - MODE_REPLACE_OLD_STATS Replaces statistics when the number of executions is greater than the number stored in the Sql tuning set - MODE_ACCUMULATE_STATS Adds new values to current values for Sql that is already stored. Note that this mode detects if a statement has been aged out, so the final value for a statistics is the sum of the statistics of all cursors that statement existed under.

Allowed values are: 'MODE_REPLACE_OLD_STATS', 'MODE_ACCUMULATE_STATS'

`attribute_list`

(optional) Specifies the list of Sql statement attributes to return in the result. Note that this parameter cannot be made an enum since custom value can take a list of comma separated attribute names. Attribute list can take one of the following values. TYPICAL - Specifies BASIC plus Sql plan (without row source statistics) and without object reference list (default). BASIC - Specifies all attributes (such as execution statistics and binds) except the plans. The execution context is always part of the result. ALL - Specifies all attributes. CUSTOM - Comma-separated list of the following attribute names. - EXECUTION_STATISTICS - BIND_LIST - OBJECT_LIST - SQL_PLAN - SQL_PLAN_STATISTICS Usage examples: 1. \"attributeList\": \"TYPICAL\" 2. \"attributeList\": \"ALL\" 3. \"attributeList\": \"EXECUTION_STATISTICS,OBJECT_LIST,SQL_PLAN\"

`load_option`

(optional) Specifies which statements are loaded into the Sql tuning set. The possible values are. - INSERT (default) Adds only new statements. - UPDATE Updates existing the Sql statements and ignores any new statements. - MERGE Inserts new statements and updates the information of the existing ones.

Allowed values are: 'INSERT', 'UPDATE', 'MERGE'

`update_option`

(optional) Specifies how existing Sql statements are updated. This parameter is applicable only if load_option is specified with UPDATE or MERGE as an option. Update option can take one of the following values. REPLACE (default) - Updates the statement using the new statistics, bind list, object list, and so on. ACCUMULATE - Combines attributes when possible (for example, statistics such as elapsed_time), otherwise replaces the existing values (for example, module and action) with the provided values. Following Sql statement attributes can be accumulated. elapsed_time buffer_gets direct_writes disk_reads row_processed fetches executions end_of_fetch_count stat_period active_stat_period

Allowed values are: 'REPLACE', 'ACCUMULATE'

`update_attributes`

(optional) Specifies the list of Sql statement attributes to update during a merge or update. Note that this parameter cannot be made an enum since custom value can take a list of comma separated attribute names. Update attributes can take one of the following values. NULL (default) - Specifies the content of the input cursor except the execution context. On other terms, it is equivalent to ALL without execution contexts such as module and action. BASIC - Specifies statistics and binds only. TYPICAL - Specifies BASIC with Sql plans (without row source statistics) and without an object reference list. ALL - Specifies all attributes, including the execution context attributes such as module and action. CUSTOM - List of comma separated attribute names to update EXECUTION_CONTEXT EXECUTION_STATISTICS SQL_BINDS SQL_PLAN SQL_PLAN_STATISTICS (similar to SQL_PLAN with added row source statistics) Usage examples: 1. \"updateAttributes\": \"TYPICAL\" 2. \"updateAttributes\": \"BASIC\" 3. \"updateAttributes\": \"EXECUTION_STATISTICS,SQL_PLAN_STATISTICS,SQL_PLAN\" 4. \"updateAttributes\": \"EXECUTION_STATISTICS,SQL_PLAN\"

`update_condition`

(optional) Specifies when to perform the update. The procedure only performs the update when the specified condition is satisfied. The condition can refer to either the data source or destination. The condition must use the following prefixes to refer to attributes from the source or the destination: OLD — Refers to statement attributes from the SQL tuning set (destination). NEW — Refers to statement attributes from the input statements (source). NULL — No updates are performed.

Allowed values are: 'OLD', 'NEW'

`is_ignore_null`

(optional) Specifies whether to update attributes when the new value is NULL. If TRUE, then the procedure does not update an attribute when the new value is NULL. That is, do not override with NULL values unless intentional. Possible values - true or false

`commit_rows`

(optional) Specifies whether to commit statements after DML. If a value is provided, then the load commits after each specified number of statements is inserted. If NULL is provided, then the load commits only once, at the end of the operation.

`begin_snapshot`

(optional) Defines the beginning AWR snapshot (non-inclusive).

`end_snapshot`

(optional) Defines the ending AWR snapshot (inclusive).

`baseline_name`

(optional) Specifies the name of the AWR baseline period. When loading the sql statements from AWR, following inputs has to be provided: beginSnapshot and endSnapshot OR baselineName

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PARENT_GROUP_T Type

The parent Managed Database Group of a Managed Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`name`

(required) The name of the Managed Database Group.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the Managed Database Group resides.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PDB_STATUS_DETAILS_T Type

The number and status of PDBs in a Container Database.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status of the PDBs with this count.

Allowed values are: 'UP', 'DOWN', 'UNKNOWN'

`l_count`

(optional) The number of PDBs with this status.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PARENT_GROUP_TBL Type

Nested table type of dbms_cloud_oci_database_management_parent_group_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_INSTANCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_management_instance_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PDB_STATUS_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_management_pdb_status_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_T Type

The details of a Managed Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(required) The name of the Managed Database.

`database_type`

(required) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(required) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) The infrastructure used to deploy the Oracle Database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`management_option`

(optional) The management option used when enabling Database Management.

Allowed values are: 'BASIC', 'ADVANCED'

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`is_cluster`

(required) Indicates whether the Oracle Database is part of a cluster.

`parent_container_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent Container Database if Managed Database is a Pluggable Database.

`managed_database_groups`

(optional) A list of Managed Database Groups that the Managed Database belongs to.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that this Managed Database is part of.

`storage_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the storage DB system.

`time_created`

(required) The date and time the Managed Database was created.

`database_status`

(optional) The status of the Oracle Database. Indicates whether the status of the database is UP, DOWN, or UNKNOWN at the current time.

Allowed values are: 'UP', 'DOWN', 'UNKNOWN'

`parent_container_name`

(optional) The name of the parent Container Database.

`parent_container_compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the parent Container Database resides, if the Managed Database is a Pluggable Database (PDB).

`instance_count`

(optional) The number of Oracle Real Application Clusters (Oracle RAC) database instances.

`instance_details`

(optional) The details of the Oracle Real Application Clusters (Oracle RAC) database instances.

`pdb_count`

(optional) The number of PDBs in the Container Database.

`pdb_status`

(optional) The status of the PDB in the Container Database.

`additional_details`

(optional) The additional details specific to a type of database defined in `{\"key\": \"value\"}` format. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_SUMMARY_T Type

A summary of the Managed Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(required) The name of the Managed Database.

`database_type`

(required) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`database_sub_type`

(required) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`deployment_type`

(optional) The infrastructure used to deploy the Oracle Database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`management_option`

(optional) The management option used when enabling Database Management.

Allowed values are: 'BASIC', 'ADVANCED'

`workload_type`

(optional) The workload type of the Autonomous Database.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`is_cluster`

(required) Indicates whether the Oracle Database is part of a cluster.

`parent_container_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the parent Container Database if the Managed Database is a Pluggable Database.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system that this Managed Database is part of.

`storage_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the storage DB system.

`time_created`

(required) The date and time the Managed Database was created.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_managed_database_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_COLLECTION_T Type

A collection of Managed Database objects.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of ManagedDatabaseSummary resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHILD_DATABASE_TBL Type

Nested table type of dbms_cloud_oci_database_management_child_database_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_T Type

The details of a Managed Database Group.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Managed Database Group.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`description`

(optional) The information specified by the user about the Managed Database Group.

`managed_databases`

(required) A list of Managed Databases in the Managed Database Group.

`lifecycle_state`

(required) The current lifecycle state of the Managed Database Group.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the Managed Database Group was created.

`time_updated`

(optional) The date and time the Managed Database Group was last updated.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_SUMMARY_T Type

A group of Managed Databases that will be managed together.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Managed Database Group.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`description`

(optional) The information specified by the user about the Managed Database Group.

`managed_database_count`

(required) The number of Managed Databases in the Managed Database Group.

`lifecycle_state`

(required) The current lifecycle state of the Managed Database Group.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the Managed Database Group was created.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_managed_database_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_COLLECTION_T Type

A collection of Managed Database Group resources.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of ManagedDatabaseGroupSummary resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_PASSWORD_CREDENTIAL_T Type

User provides a password to be used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_managed_database_password_credential_t`is a subtype of the`dbms_cloud_oci_database_management_managed_database_credential_t`type.

Fields

Field Description

`password`

(required) The database user's password encoded using BASE64 scheme.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_SECRET_CREDENTIAL_T Type

User provides a secret OCID, which will be used to retrieve the password to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_managed_database_secret_credential_t`is a subtype of the`dbms_cloud_oci_database_management_managed_database_credential_t`type.

Fields

Field Description

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the database password is stored.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_T Type

The details of the Managed MySQL Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Managed MySQL Database.

`compartment_id`

(required) The OCID of the compartment.

`db_name`

(required) The name of the MySQL Database.

`db_version`

(required) The version of the MySQL Database.

`time_created`

(required) The date and time the Managed MySQL Database was created.

`name`

(required) The name of the Managed MySQL Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_SUMMARY_T Type

The details of the Managed MySQL Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Managed MySQL Database.

`compartment_id`

(required) The OCID of the compartment.

`db_name`

(required) The name of the MySQL Database.

`db_version`

(required) The version of the MySQL Database.

`time_created`

(required) The date and time the Managed MySQL Database was created.

`name`

(required) The name of the Managed MySQL Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_managed_my_sql_database_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_COLLECTION_T Type

A collection of Managed MySQL Database objects.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of ManagedMySqlDatabaseSummary resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_ANALYTICS_METRIC_TBL Type

Nested table type of dbms_cloud_oci_database_management_db_management_analytics_metric_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRICS_AGGREGATION_RANGE_T Type

The set of aggregated data returned for a metric.

Syntax
```

```

Fields

Field Description

`header`

(optional)

`metrics`

(optional) The list of metrics returned for the specified request. Each of the metrics has a `metricName` and additional properties like `metadata`, `dimensions`. If a property is not set, then use the value from `header`. Suppose `m` be an item in the `metrics` array: - If `m.metricName` is not set, use `header.metricName` instead - If `m.durationInSeconds` is not set, use `header.durationInSeconds` instead - If `m.dimensions` is not set, use `header.dimensions` instead - If `m.metadata` is not set, use `header.metadata` instead

`range_start_time_in_epoch_seconds`

(optional) The beginning of the time range (inclusive) of the returned metric data.

`range_end_time_in_epoch_seconds`

(optional) The end of the time range (exclusive) of the returned metric data.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRICS_AGGREGATION_RANGE_TBL Type

Nested table type of dbms_cloud_oci_database_management_metrics_aggregation_range_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRICS_AGGREGATION_RANGE_COLLECTION_T Type

The collection of metrics.

Syntax
```

```

Fields

Field Description

`items`

(required) The metric data.

`start_time`

(optional) The beginning of the metric data query time range. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`end_time`

(optional) The end of the metric data query time range. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MODIFY_SNAPSHOT_SETTINGS_DETAILS_T Type

Details to modify the AWR snapshot settings for a database.

Syntax
```

```

Fields

Field Description

`retention`

(optional) The retention time in minutes. Acceptable values are 0, 1440 to 52596000 (inclusive), and null.

`interval`

(optional) The interval time in minutes. Acceptable values are 0, 10 to 527040 (inclusive), and null.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_CONFIGURATION_DATA_SUMMARY_T Type

The configuration variables for a MySQL Database.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the configuration variable

`value`

(required) The value of the variable.

`source`

(required) The source from which the variable was most recently set.

Allowed values are: 'COMPILED', 'GLOBAL', 'SERVER', 'EXPLICIT', 'EXTRA', 'USER', 'LOGIN', 'COMMAND_LINE', 'PERSISTED', 'DYNAMIC'

`min_value`

(required) The minimum value of the variable.

`max_value`

(required) The maximum value of the variable.

`l_type`

(required) The type of variable.

`default_value`

(required) The default value of the variable.

`time_set`

(required) The time when the value of the variable was set.

`host_set`

(required) The host from where the value of the variable was set. This is empty for a MySQL Database System.

`user_set`

(required) The user who sets the value of the variable. This is empty for a MySQL Database System.

`is_dynamic`

(required) Indicates whether the variable can be set dynamically or not.

`is_init`

(required) Indicates whether the variable is set at server startup.

`is_configurable`

(required) Indicates whether the variable is configurable.

`path`

(required) The path name of the option file (VARIABLE_PATH), if the variable was set in an option file. If the variable was not set in an

`description`

(required) The description of the variable.

`possible_values`

(required) The comma-separated list of possible values for the variable in value:valueDescription format.

`supported_versions`

(required) The comma-separated list of MySQL versions that support the variable.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_CONFIGURATION_DATA_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_configuration_data_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_CONFIGURATION_DATA_COLLECTION_T Type

The collection of configuration records for a specific MySQL Database.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of ConfigurationDataSummary records.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATA_SUMMARY_T Type

The SQL performance data record for a specific SQL query.

Syntax
```

```

Fields

Field Description

`schema_name`

(required) The name of the default schema when executing the query. If a schema is not set as the default, then the value is NULL.

`digest`

(required) The digest information of the normalized query.

`digest_text`

(required) The normalized query.

`count_star`

(required) The number Of times the query has been executed.

`sum_timer_wait`

(required) The total amount of time that has been spent executing the query.

`min_timer_wait`

(required) The fastest the query has been executed.

`avg_timer_wait`

(required) The average execution time.

`max_timer_wait`

(required) The slowest the query has been executed.

`sum_lock_time`

(required) The total amount of time that has been spent waiting for table locks.

`sum_errors`

(required) The total number of errors that have been encountered executing the query.

`sum_warnings`

(required) The total number of warnings that have been encountered executing the query.

`sum_rows_affected`

(required) The total number of rows that have been modified by the query.

`sum_rows_sent`

(required) The total number of rows that have been returned (sent) to the client.

`sum_rows_examined`

(required) The total number of rows that have been examined by the query.

`sum_created_temp_disk_tables`

(required) The total number of On-Disk internal temporary tables that have been created by the query.

`sum_created_temp_tables`

(required) The total number of internal temporary tables (in memory or on disk), which have been created by the query.

`sum_select_full_join`

(required) The total number of joins that have performed full table scans as there was no join condition or no index for the join condition. This is the same as the select_full_join status variable.

`sum_select_full_range_join`

(required) The total number of joins that use a full range search. This is the same as the select_full_range_join status variable.

`sum_select_range`

(required) The total number of times the query has used a range search. This is the same as the select_range status variable.

`sum_select_range_check`

(required) The total number of joins by the query where the join does not have an index that checks for the index usage after each row. This is the same as the select_range_check status variable.

`sum_select_scan`

(required) The total number of times the query has performed a full table scan on the first table in the join. This is the same as the select_scan status variable.

`sum_sort_merge_passes`

(required) The total number of sort merge passes that have been done to sort the result of the query. This is the same as the sort_merge_passes status variable.

`sum_sort_range`

(required) The total number of times a sort was done using ranges. This is the same as the sort_range status variable.

`sum_sort_rows`

(required) The total number of rows sorted. This is the same as the sort_rowsStatus variable.

`sum_sort_scan`

(required) The total number of times a sort was done by scanning the table. This is the same as the sort_scan status variable.

`sum_no_index_used`

(required) The total number of times no index was used to execute the query.

`sum_no_good_index_used`

(required) The total number of times no good index was used. This means that the extra column in The EXPLAIN output includes “Range Checked For Each Record.”

`first_seen`

(required) The date and time the query was first seen. If the table is truncated, the first seen value is reset.

`last_seen`

(required) The date and time the query was last seen.

`quantile95`

(required) The 95th percentile of the query latency. That is, 95% of the queries complete in the time given or in less time.

`quantile99`

(required) The 99th percentile of the query latency.

`quantile999`

(required) The 99.9th percentile of the query latency.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATA_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_data_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATA_COLLECTION_T Type

The collection of SQL performance data records for a specific Managed MySQL Database.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of SQLDataSummary records.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_DEFINITION_T Type

The list of aggregated metrics for the Managed MySQL Databases in the fleet.

Syntax
```

```

Fields

Field Description

`metric_value`

(required) The value of the metric.

`metric_name`

(required) The name of the metric.

`l_timestamp`

(required) The data point date and time in UTC in ISO-8601 format.

`dimensions`

(required) The dimensions of the metric.

`unit`

(required) The unit of the metric value.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_fleet_metric_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATABASE_USAGE_METRICS_T Type

The list of aggregated metrics for Managed MySQL Databases in the fleet.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the Managed MySQL Database resides.

`database_name`

(required) The display name of the Managed MySQL Database.

`database_type`

(required) Indicates MySQL Database type, ONPREMISE or MySQL Database System.

`mds_deployment_type`

(required) The type of MySQL Database System.

`mdslifecycle_state`

(required) The lifecycle state of the MySQL Database System.

`database_version`

(required) The version of the MySQL Database.

`db_id`

(required) The OCID of the Managed MySQL Database.

`database_status`

(required) The status of the MySQL Database. Indicates whether the status of the database is UP, DOWN, or UNKNOWN at the current time.

Allowed values are: 'UP', 'DOWN', 'UNKNOWN'

`metrics`

(required) A list of the database health metrics like CPU, Storage, and Memory.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_BY_CATEGORY_T Type

The number of MySQL Databases in the fleet, grouped by database type and sub type.

Syntax
```

```

Fields

Field Description

`database_type`

(required) The type of the MySQL Database. Indicates whether the database is on premises or Oracle Cloud. Allowed values are: MDS and ONPREMISE

`mds_deployment_type`

(required) The type of MySQL Database installation. Allowed values are: STANDALONE, HEATWAVE and HA

`inventory_count`

(required) The number of MySQL Databases.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_SUMMARY_DEFINITION_T Type

A summary of the fleet metrics, which provides the metric aggregated value of the MySQL Databases in the fleet.

Syntax
```

```

Fields

Field Description

`metric_value`

(required) The aggregated metric value.

`dimensions`

(required) The unique dimension key and values of the metric.

`metric_name`

(required) The name of the metric.

`unit`

(required) The unit of the metric value.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_SUMMARY_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_fleet_metric_summary_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_BY_CATEGORY_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_fleet_by_category_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_SUMMARY_T Type

A summary of the inventory count and the metrics that describe the aggregated usage of CPU, storage, and so on of all the MySQL Databases in the fleet.

Syntax
```

```

Fields

Field Description

`aggregated_metrics`

(required) The usage metrics for the Managed MySQL Databases in the fleet.

`inventory`

(required) A list of MySQL Databases in the fleet, grouped by database type.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATABASE_USAGE_METRICS_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_database_usage_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_my_sql_fleet_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRICS_T Type

The details of the MySQL Database fleet health metrics.

Syntax
```

```

Fields

Field Description

`start_time`

(required) The beginning of the time range during which metric data is retrieved.

`end_time`

(required) The end of the time range during which metric data is retrieved.

`fleet_databases`

(required) The list of MySQL Databases in the fleet and their usage metrics.

`fleet_summary`

(required) A summary of the inventory count and the metrics that describe the aggregated usage of CPU, storage, and so on of all the MySQL Databases in the fleet.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_PRIVILEGE_SUMMARY_T Type

A summary of object privileges.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the privilege on the object.

`schema_type`

(optional) The type of object.

`owner`

(optional) The owner of the object.

`grantor`

(optional) The name of the user who granted the object privilege.

`hierarchy`

(optional) Indicates whether the privilege is granted with the HIERARCHY OPTION (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`object`

(optional) The name of the object. The object can be any object, including tables, packages, indexes, sequences, and so on.

`grant_option`

(optional) Indicates whether the privilege is granted with the GRANT OPTION (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`common`

(optional) Indicates how the object privilege was granted. Possible values: YES if the role is granted commonly (CONTAINER=ALL is used) NO if the role is granted locally (CONTAINER=ALL is not used)

Allowed values are: 'YES', 'NO'

`inherited`

(optional) Indicates whether the granted privilege is inherited from another container (YES) or not (NO).

Allowed values are: 'YES', 'NO'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_PRIVILEGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_object_privilege_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_PRIVILEGE_COLLECTION_T Type

A collection of object privileges granted to the current user.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of object privileges.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_STORAGE_JOB_EXECUTION_RESULT_DETAILS_T Type

The details of the job execution result stored in Object Storage. The job execution result could be accessed using the Object Storage API.

Syntax
```

```

`dbms_cloud_oci_database_management_object_storage_job_execution_result_details_t`is a subtype of the`dbms_cloud_oci_database_management_job_execution_result_details_t`type.

Fields

Field Description

`namespace_name`

(optional) The Object Storage namespace used for job execution result storage.

`bucket_name`

(optional) The name of the bucket used for job execution result storage.

`object_name`

(optional) The name of the object containing the job execution result.

`row_count`

(optional) The number of rows returned in the result for the Query SqlType.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_STORAGE_JOB_EXECUTION_RESULT_LOCATION_T Type

The details about Object Storage job execution result location type.

Syntax
```

```

`dbms_cloud_oci_database_management_object_storage_job_execution_result_location_t`is a subtype of the`dbms_cloud_oci_database_management_job_execution_result_location_t`type.

Fields

Field Description

`namespace_name`

(optional) The Object Storage namespace used for job execution result storage.

`bucket_name`

(optional) The name of the bucket used for job execution result storage.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPEN_ALERT_SUMMARY_T Type

An alert from the Exadata storage server.

Syntax
```

```

Fields

Field Description

`severity`

(optional) The severity of the alert.

Allowed values are: 'CLEAR', 'INFO', 'WARNING', 'CRITICAL'

`l_type`

(optional) The type of alert.

Allowed values are: 'STATEFUL', 'STATELESS'

`time_start_at`

(optional) The start time of the alert.

`message`

(optional) The alert message.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPEN_ALERT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_open_alert_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPEN_ALERT_HISTORY_T Type

The existing open alerts in the Exadata storage server.

Syntax
```

```

Fields

Field Description

`alerts`

(required) A list of open alerts.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_DATABASE_T Type

The subset information of the Managed Database resource, which is used by Optimizer Statistics.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(required) The name of the Managed Database.

`db_type`

(required) The type of Oracle Database installation.

Allowed values are: 'EXTERNAL_SIDB', 'EXTERNAL_RAC', 'CLOUD_SIDB', 'CLOUD_RAC', 'SHARED', 'DEDICATED'

`db_sub_type`

(required) The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

Allowed values are: 'CDB', 'PDB', 'NON_CDB', 'ACD', 'ADB'

`db_deployment_type`

(required) The infrastructure used to deploy the Oracle Database.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`db_version`

(required) The version of the Oracle Database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the Managed Database resides.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADVISOR_RULE_TBL Type

Nested table type of dbms_cloud_oci_database_management_advisor_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_REPORT_T Type

A report that includes the rules, findings, recommendations, and actions discovered during the execution of the Optimizer Statistics Advisor.

Syntax
```

```

Fields

Field Description

`summary`

(required) A summary of the Optimizer Statistics Advisor execution.

`rules`

(required) The list of rules that were not adhered to by the Optimizer Statistics Collection.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_T Type

The summary of the Optimizer Statistics Advisor execution, which includes information about the Managed Database and a comprehensive execution report.

Syntax
```

```

Fields

Field Description

`database`

(optional)

`report`

(optional)

`task_name`

(required) The name of the Optimizer Statistics Advisor task.

`execution_name`

(required) The name of the Optimizer Statistics Advisor execution.

`time_start`

(required) The start time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`time_end`

(required) The end time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`status`

(required) The status of the Optimizer Statistics Advisor execution.

Allowed values are: 'EXECUTING', 'COMPLETED', 'INTERRUPTED', 'CANCELLED', 'FATAL_ERROR'

`status_message`

(optional) The Optimizer Statistics Advisor execution status message, if any.

`error_message`

(optional) The errors in the Optimizer Statistics Advisor execution, if any.

`findings`

(optional) The number of findings generated by the Optimizer Statistics Advisor execution.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SCRIPT_T Type

The Oracle system-generated script for the Optimizer Statistics Advisor execution.

Syntax
```

```

Fields

Field Description

`script`

(required) The Optimizer Statistics Advisor execution script.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SUMMARY_T Type

The summary of the Optimizer Statistics Advisor execution.

Syntax
```

```

Fields

Field Description

`task_name`

(required) The name of the Optimizer Statistics Advisor task.

`execution_name`

(required) The name of the Optimizer Statistics Advisor execution.

`time_start`

(required) The start time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`time_end`

(required) The end time of the time range to retrieve the Optimizer Statistics Advisor execution of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`status`

(required) The status of the Optimizer Statistics Advisor execution.

Allowed values are: 'EXECUTING', 'COMPLETED', 'INTERRUPTED', 'CANCELLED', 'FATAL_ERROR'

`status_message`

(optional) The Optimizer Statistics Advisor execution status message, if any.

`error_message`

(optional) The errors in the Optimizer Statistics Advisor execution, if any.

`findings`

(optional) The number of findings generated by the Optimizer Statistics Advisor execution.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_optimizer_statistics_advisor_execution_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTIONS_COLLECTION_T Type

The details of each Optimizer Statistics Advisor execution.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of Optimizer Statistics Advisor executions.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATION_SUMMARY_T Type

The summary of the Optimizer Statistics Collection, which includes the aggregated number of tasks grouped by status.

Syntax
```

```

Fields

Field Description

`group_by`

(optional) The optimizer statistics tasks grouped by type.

Allowed values are: 'TASK_STATUS', 'TASK_OBJECTS_STATUS'

`time_start`

(required) Indicates the start of the hour as the statistics are aggregated per hour.

`time_end`

(optional) Indicates the end of the hour as the statistics are aggregated per hour.

`pending`

(optional) The number of tasks or objects for which statistics are yet to be gathered.

`in_progress`

(optional) The number of tasks or objects for which statistics gathering is in progress.

`completed`

(optional) The number of tasks or objects for which statistics gathering is completed.

`failed`

(optional) The number of tasks or objects for which statistics gathering failed.

`skipped`

(optional) The number of tasks or objects for which statistics gathering was skipped.

`timed_out`

(optional) The number of tasks or objects for which statistics gathering timed out.

`unknown`

(optional) The number of tasks or objects for which the status of statistics gathering is unknown.

`total`

(optional) The total number of tasks or objects for which statistics collection is finished. This number is the sum of all the tasks or objects with various statuses: pending, inProgress, completed, failed, skipped, timedOut, and unknown.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_optimizer_statistics_collection_aggregation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATIONS_COLLECTION_T Type

The number of times optimizer statistics are collected each hour, grouped by task status.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of Optimizer Statistics Collection details.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_OPERATION_TASK_T Type

The details of the Optimizer Statistics Collection task.

Syntax
```

```

Fields

Field Description

`target`

(required) The name of the target object for which statistics are gathered.

`target_type`

(required) The type of target object.

Allowed values are: 'TABLE', 'GLOBAL_TABLE', 'COORDINATOR_TABLE', 'TABLE_PARTITION', 'TABLE_SUBPARTITION', 'INDEX', 'INDEX_PARTITION', 'INDEX_SUBPARTITION'

`time_start`

(required) The start time of the Optimizer Statistics Collection task.

`time_end`

(required) The end time of the Optimizer Statistics Collection task.

`status`

(required) The status of the Optimizer Statistics Collection task.

Allowed values are: 'PENDING', 'IN_PROGRESS', 'SKIPPED', 'TIMED_OUT', 'COMPLETED', 'FAILED'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_OPERATION_TASK_TBL Type

Nested table type of dbms_cloud_oci_database_management_optimizer_statistics_operation_task_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATION_T Type

The summary of the Optimizer Statistics Collection tasks, which includes details of the Managed Database and the execution.

Syntax
```

```

Fields

Field Description

`database`

(optional)

`tasks`

(optional) An array of Optimizer Statistics Collection task details.

`id`

(required) The ID of the operation.

`operation_name`

(required) The name of the operation.

`target`

(required) The target object type such as Table, Index, and Partition.

`job_name`

(required) The name of the job.

`status`

(required) The status of the operation such as Completed, and Failed.

Allowed values are: 'IN_PROGRESS', 'COMPLETED', 'FAILED', 'TIMED_OUT'

`start_time`

(required) The start time of the operation.

`end_time`

(required) The end time of the operation.

`duration_in_seconds`

(required) The time it takes to complete the operation (in seconds).

`completed_count`

(optional) The number of objects for which statistics collection is completed.

`in_progress_count`

(optional) The number of objects for which statistics collection is in progress.

`failed_count`

(optional) The number of objects for which statistics collection failed.

`timed_out_count`

(optional) The number of objects for which statistics collection timed out.

`total_objects_count`

(optional) The total number of objects for which statistics is collected. This number is the sum of all the objects with various statuses: completed, inProgress, failed, and timedOut.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATION_SUMMARY_T Type

The summary of the Optimizer Statistics Collection operation.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the operation.

`operation_name`

(required) The name of the operation.

`target`

(required) The target object type such as Table, Index, and Partition.

`job_name`

(required) The name of the job.

`status`

(required) The status of the operation such as Completed, and Failed.

Allowed values are: 'IN_PROGRESS', 'COMPLETED', 'FAILED', 'TIMED_OUT'

`start_time`

(required) The start time of the operation.

`end_time`

(required) The end time of the operation.

`duration_in_seconds`

(required) The time it takes to complete the operation (in seconds).

`completed_count`

(optional) The number of objects for which statistics collection is completed.

`in_progress_count`

(optional) The number of objects for which statistics collection is in progress.

`failed_count`

(optional) The number of objects for which statistics collection failed.

`timed_out_count`

(optional) The number of objects for which statistics collection timed out.

`total_objects_count`

(optional) The total number of objects for which statistics is collected. This number is the sum of all the objects with various statuses: completed, inProgress, failed, and timedOut.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_optimizer_statistics_collection_operation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATIONS_COLLECTION_T Type

The details of each statistics collection operation.

Syntax
```

```

Fields

Field Description

`items`

(required) The details of the Optimizer Statistics Collection operation.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_INSTRUCTION_T Type

A single instruction to be included as part of Patch request content.

Syntax
```

```

Fields

Field Description

`operation`

(required) The type of operation.

Allowed values are: 'MERGE'

`selection`

(required) The set of values to which the operation applies as a[JMESPath expression](https://jmespath.org/specification.html)for evaluation against the context resource. An operation fails if the selection yields an exception, except as otherwise specified. Note that comparisons involving non-primitive values (objects or arrays) are not supported and will always evaluate to false.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_INSTRUCTION_TBL Type

Nested table type of dbms_cloud_oci_database_management_patch_instruction_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_EXTERNAL_DB_SYSTEM_DISCOVERY_DETAILS_T Type

The details required to update an external DB system discovery resource.

Syntax
```

```

Fields

Field Description

`items`

(optional) A sequence of instructions to apply to the resource.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_MERGE_INSTRUCTION_T Type

An operation that recursively updates items of the selection, or adding the value if the selection is empty. If the value is not an object, it is used directly, otherwise each key-value member is used to create or update a member of the same name in the target and the same process is applied recursively for each object-typed value (similar to[RFC 7396](https://tools.ietf.org/html/rfc7396#section-2)JSON Merge Patch, except that null values are copied rather than transformed into deletions). NOT_FOUND exceptions are handled by creating the implied containing structure. To avoid referential errors if an item's descendant is also in the selection, items of the selection are processed in order of decreasing depth.

Syntax
```

```

`dbms_cloud_oci_database_management_patch_merge_instruction_t`is a subtype of the`dbms_cloud_oci_database_management_patch_instruction_t`type.

Fields

Field Description

`value`

(optional) A value to be merged into the target.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PDB_METRICS_T Type

The summary of Pluggable Databases (PDBs) and their resource usage metrics, within a specific Container Database (CDB).

Syntax
```

```

Fields

Field Description

`database_usage_metrics`

(required) A summary of PDBs and their resource usage metrics such as CPU, User I/O, and Storage, within a specific CDB.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_SUMMARY_T Type

The summary of preferred credentials.

Syntax
```

```

Fields

Field Description

`l_credential_name`

(required) The name of the preferred credential.

`status`

(required) The status of the preferred credential.

Allowed values are: 'SET', 'NOT_SET'

`is_accessible`

(required) Indicates whether the preferred credential is accessible.

`user_name`

(optional) The user name used to connect to the database.

`role`

(optional) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Vault service secret that contains the database user password.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_preferred_credential_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_COLLECTION_T Type

A collection of preferred credential attributes.

Syntax
```

```

Fields

Field Description

`items`

(required) The attributes of the preferred credential.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXIED_FOR_USER_SUMMARY_T Type

A summary of users on whose behalf the current user acts as proxy.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of a proxy user or the name of the client user.

`authentication`

(optional) Indicates whether the proxy is required to supply the client credentials (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`flags`

(optional) The flags associated with the proxy/client pair.

Allowed values are: 'PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES', 'NO_CLIENT_ROLES_MAY_BE_ACTIVATED', 'PROXY_MAY_ACTIVATE_ROLE', 'PROXY_MAY_NOT_ACTIVATE_ROLE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXIED_FOR_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_proxied_for_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXIED_FOR_USER_COLLECTION_T Type

A collection of users on whose behalf the current user acts as proxy.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of user resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXY_USER_SUMMARY_T Type

A summary of the proxy user.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of a proxy user or the name of the client user.

`authentication`

(optional) Indicates whether the proxy is required to supply the client credentials (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`flags`

(optional) The flags associated with the proxy/client pair.

Allowed values are: 'PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES', 'NO_CLIENT_ROLES_MAY_BE_ACTIVATED', 'PROXY_MAY_ACTIVATE_ROLE', 'PROXY_MAY_NOT_ACTIVATE_ROLE'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXY_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_proxy_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXY_USER_COLLECTION_T Type

A collection of proxy users for the current user.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of user resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_REMOVE_DATA_FILE_DETAILS_T Type

The details required to remove a data file or temp file from the tablespace.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`file_type`

(required) Specifies whether the file is a data file or temp file.

Allowed values are: 'DATAFILE', 'TEMPFILE'

`data_file`

(required) Name of the data file or temp file to be removed from the tablespace.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_REMOVE_MANAGED_DATABASE_FROM_MANAGED_DATABASE_GROUP_DETAILS_T Type

The Managed Database details required to remove it from a Managed Database Group.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RESET_DATABASE_PARAMETERS_DETAILS_T Type

The details required to reset database parameter values.

Syntax
```

```

Fields

Field Description

`credentials`

(required)

`scope`

(required) The clause used to specify when the parameter change takes effect. Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.

Allowed values are: 'MEMORY', 'SPFILE', 'BOTH'

`parameters`

(required) A list of database parameter names.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RESIZE_DATA_FILE_DETAILS_T Type

The details required to resize a data file or temp file within the tablespace.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`file_type`

(required) Specifies whether the file is a data file or temp file.

Allowed values are: 'DATAFILE', 'TEMPFILE'

`data_file`

(required) Name of the data file or temp file to be resized.

`file_size`

(optional) The new size of the data file or temp file.

`is_auto_extensible`

(optional) Specifies whether the data file or temp file can be extended automatically.

`auto_extend_next_size`

(optional) The size of the next increment of disk space to be allocated automatically when more extents are required.

`auto_extend_max_size`

(optional) The maximum disk space allowed for automatic extension of the data files or temp files.

`is_max_size_unlimited`

(optional) Specifies whether the disk space of the data file or temp file can be limited.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ROLE_SUMMARY_T Type

A summary of each role.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the role granted to the user.

`admin_option`

(optional) Indicates whether the role is granted with the ADMIN OPTION (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`delegate_option`

(optional) Indicates whether the role is granted with the DELEGATE OPTION (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`default_role`

(optional) Indicates whether the role is designated as a DEFAULT ROLE for the user (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`common`

(optional) Indicates how the role was granted. Possible values: YES if the role is granted commonly (CONTAINER=ALL is used) NO if the role is granted locally (CONTAINER=ALL is not used)

Allowed values are: 'YES', 'NO'

`inherited`

(optional) Indicates whether the granted role is inherited from another container (YES) or not (NO).

Allowed values are: 'YES', 'NO'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ROLE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_role_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ROLE_COLLECTION_T Type

A collection of roles granted to the current User.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of roles.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RUN_HISTORIC_ADDM_DETAILS_T Type

The details of the ADDM task, which include the beginning and ending AWR snapshot IDs.

Syntax
```

```

Fields

Field Description

`start_snapshot_id`

(required) The ID number of the beginning AWR snapshot.

`end_snapshot_id`

(required) The ID of the ending AWR snapshot.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SAVE_SQL_TUNING_SET_AS_DETAILS_T Type

Save current list of Sql statements into another Sql tuning set.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`show_sql_only`

(optional) Flag to indicate whether to save the Sql tuning set or just display the plsql used to save Sql tuning set.

`owner`

(optional) The owner of the Sql tuning set.

`name`

(required) The name of the Sql tuning set.

`destination_sql_tuning_set_name`

(required) The name of the destination Sql tuning set.

`destination_sql_tuning_set_description`

(optional) The description for the destination Sql tuning set.

`destination_sql_tuning_set_owner`

(optional) Owner of the destination Sql tuning set.

`create_new`

(required) Specifies whether to create a new Sql tuning set or not. Possible values 1 - Create a new Sql tuning set 0 - Do not create a new Sql tuning set

`basic_filter`

(optional) Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW. User could use any combination of the following columns with appropriate values as Sql predicate Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C

`plan_filter`

(optional) Specifies the plan filter. This parameter enables you to select a single plan when a statement has multiple plans. Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SQLSET.html#GUID-9D995019-91AB-4B1E-9EAF-031050789B21

Allowed values are: 'LAST_GENERATED', 'FIRST_GENERATED', 'LAST_LOADED', 'FIRST_LOADED', 'MAX_ELAPSED_TIME', 'MAX_BUFFER_GETS', 'MAX_DISK_READS', 'MAX_DIRECT_WRITES', 'MAX_OPTIMIZER_COST'

`recursive_sql`

(optional) Specifies that the filter must include recursive Sql in the Sql tuning set.

Allowed values are: 'HAS_RECURSIVE_SQL', 'NO_RECURSIVE_SQL'

`result_percentage`

(optional) Specifies a filter that picks the top n% according to the supplied ranking measure. Note that this parameter applies only if one ranking measure is supplied.

`result_limit`

(optional) The top limit Sql from the filtered source, ranked by the ranking measure.

`ranking_measure1`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`ranking_measure2`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`ranking_measure3`

(optional) Specifies an ORDER BY clause on the selected Sql. User can specify upto three ranking measures.

Allowed values are: 'ELAPSED_TIME', 'CPU_TIME', 'OPTIMIZER_COST', 'BUFFER_GETS', 'DISK_READS', 'DIRECT_WRITES'

`attribute_list`

(optional) Specifies the list of Sql statement attributes to return in the result. Note that this parameter cannot be made an enum since custom value can take a list of comma separated attribute names. Attribute list can take one of the following values. TYPICAL - Specifies BASIC plus Sql plan (without row source statistics) and without object reference list (default). BASIC - Specifies all attributes (such as execution statistics and binds) except the plans. The execution context is always part of the result. ALL - Specifies all attributes. CUSTOM - Comma-separated list of the following attribute names. - EXECUTION_STATISTICS - BIND_LIST - OBJECT_LIST - SQL_PLAN - SQL_PLAN_STATISTICS Usage examples: 1. \"attributeList\": \"TYPICAL\" 2. \"attributeList\": \"ALL\" 3. \"attributeList\": \"EXECUTION_STATISTICS,OBJECT_LIST,SQL_PLAN\"

`load_option`

(optional) Specifies which statements are loaded into the Sql tuning set. The possible values are. - INSERT (default) Adds only new statements. - UPDATE Updates existing the Sql statements and ignores any new statements. - MERGE Inserts new statements and updates the information of the existing ones.

Allowed values are: 'INSERT', 'UPDATE', 'MERGE'

`update_option`

(optional) Specifies how existing Sql statements are updated. This parameter is applicable only if load_option is specified with UPDATE or MERGE as an option. Update option can take one of the following values. REPLACE (default) - Updates the statement using the new statistics, bind list, object list, and so on. ACCUMULATE - Combines attributes when possible (for example, statistics such as elapsed_time), otherwise replaces the existing values (for example, module and action) with the provided values. Following Sql statement attributes can be accumulated. elapsed_time buffer_gets direct_writes disk_reads row_processed fetches executions end_of_fetch_count stat_period active_stat_period

Allowed values are: 'REPLACE', 'ACCUMULATE'

`update_condition`

(optional) Specifies when to perform the update. The procedure only performs the update when the specified condition is satisfied. The condition can refer to either the data source or destination. The condition must use the following prefixes to refer to attributes from the source or the destination: OLD — Refers to statement attributes from the SQL tuning set (destination). NEW — Refers to statement attributes from the input statements (source). NULL — No updates are performed.

Allowed values are: 'OLD', 'NEW'

`update_attributes`

(optional) Specifies the list of Sql statement attributes to update during a merge or update. Note that this parameter cannot be made an enum since custom value can take a list of comma separated attribute names. Update attributes can take one of the following values. NULL (default) - Specifies the content of the input cursor except the execution context. On other terms, it is equivalent to ALL without execution contexts such as module and action. BASIC - Specifies statistics and binds only. TYPICAL - Specifies BASIC with Sql plans (without row source statistics) and without an object reference list. ALL - Specifies all attributes, including the execution context attributes such as module and action. CUSTOM - List of comma separated attribute names to update EXECUTION_CONTEXT EXECUTION_STATISTICS SQL_BINDS SQL_PLAN SQL_PLAN_STATISTICS (similar to SQL_PLAN with added row source statistics) Usage examples: 1. \"updateAttributes\": \"TYPICAL\" 2. \"updateAttributes\": \"BASIC\" 3. \"updateAttributes\": \"EXECUTION_STATISTICS,SQL_PLAN_STATISTICS,SQL_PLAN\" 4. \"updateAttributes\": \"EXECUTION_STATISTICS,SQL_PLAN\"

`is_ignore_null`

(optional) Specifies whether to update attributes when the new value is NULL. If TRUE, then the procedure does not update an attribute when the new value is NULL. That is, do not override with NULL values unless intentional. Possible values - true or false

`commit_rows`

(optional) Specifies whether to commit statements after DML. If a value is provided, then the load commits after each specified number of statements is inserted. If NULL is provided, then the load commits only once, at the end of the operation.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SNAPSHOT_DETAILS_T Type

The details of the newly generated AWR snapshot.

Syntax
```

```

Fields

Field Description

`snapshot_id`

(required) The ID of the beginning AWR snapshot.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_CPU_ACTIVITY_T Type

The SQL CPU activity from the Exadata storage server.

Syntax
```

```

Fields

Field Description

`database_name`

(optional) The database name.

`sql_id`

(optional) The SQL ID.

`cpu_activity`

(optional) The CPU activity percentage.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_METRICS_T Type

Metrics of the Sql in the Sql tuning set.

Syntax
```

```

Fields

Field Description

`cpu_time`

(optional) Total CPU time consumed by the Sql.

`elapsed_time`

(optional) Elapsed time of the Sql.

`buffer_gets`

(optional) Sum total number of buffer gets.

`disk_reads`

(optional) Sum total number of disk reads.

`direct_writes`

(optional) Sum total number of direct path writes.

`executions`

(optional) Total executions of this SQL statement.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_METRICS_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_IN_SQL_TUNING_SET_T Type

Sql information in the Sql tuning set.

Syntax
```

```

Fields

Field Description

`sql_id`

(required) The unique Sql identifier.

`sql_text`

(optional) Sql text.

`container_database_id`

(optional) The unique container database identifier.

`plan_hash_value`

(required) Plan hash value of the Sql statement.

`schema`

(optional) The schema name of the Sql.

`module`

(optional) The module of the Sql.

`metrics`

(optional) A list of the Sqls associated with the Sql tuning set.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_JOB_T Type

The details of the SQL job.

Syntax
```

```

`dbms_cloud_oci_database_management_sql_job_t`is a subtype of the`dbms_cloud_oci_database_management_job_t`type.

Fields

Field Description

`sql_type`

(optional) The type of SQL. This is a mandatory field for the EXECUTE_SQL operationType.

Allowed values are: 'QUERY', 'DML', 'DDL', 'PLSQL'

`sql_text`

(optional) The SQL text to be executed in the job. This is a mandatory field for the EXECUTE_SQL operationType.

`in_binds`

(optional)

`out_binds`

(optional)

`operation_type`

(required) The SQL operation type.

Allowed values are: 'EXECUTE_SQL'

`user_name`

(optional) The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group, then the user name should exist on all the databases in the group with the same password.

`role`

(optional) The role of the database user. Indicates whether the database user is a normal user or sysdba.

Allowed values are: 'NORMAL', 'SYSDBA'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_T Type

The details of a SQL plan baseline.

Syntax
```

```

Fields

Field Description

`plan_name`

(required) The unique plan identifier.

`sql_handle`

(required) The unique SQL identifier.

`sql_text`

(required) The SQL text.

`origin`

(optional) The origin of the SQL plan baseline.

Allowed values are: 'ADDM_SQLTUNE', 'AUTO_CAPTURE', 'AUTO_SQLTUNE', 'EVOLVE_AUTO_INDEX_LOAD', 'EVOLVE_CREATE_FROM_ADAPTIVE', 'EVOLVE_LOAD_FROM_STS', 'EVOLVE_LOAD_FROM_AWR', 'EVOLVE_LOAD_FROM_CURSOR_CACHE', 'MANUAL_LOAD', 'MANUAL_LOAD_FROM_AWR', 'MANUAL_LOAD_FROM_CURSOR_CACHE', 'MANUAL_LOAD_FROM_STS', 'MANUAL_SQLTUNE', 'STORED_OUTLINE', 'UNKNOWN'

`time_created`

(required) The date and time when the plan baseline was created.

`time_last_modified`

(optional) The date and time when the plan baseline was last modified.

`time_last_executed`

(optional) The date and time when the plan baseline was last executed. **Note:** For performance reasons, database does not update this value immediately after each execution of the plan baseline. Therefore, the plan baseline may have been executed more recently than this value indicates.

`enabled`

(optional) Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).

`accepted`

(optional) Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).

`fixed`

(optional) Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).

`reproduced`

(optional) Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`). The value is set to `YES` when a plan is initially added to the plan baseline.

`auto_purge`

(optional) Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).

`adaptive`

(optional) Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not. When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` property will be marked `YES`. When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed and the final plan determined at execution will become an accepted plan if its performance is better than the existing plan baseline. At this point, the value of the `ADAPTIVE` property is set to `NO` since the plan is no longer adaptive, but resolved.

`module`

(optional) The application module name.

`action`

(optional) The application action.

`execution_plan`

(required) The execution plan for the SQL statement.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_DIMENSIONS_T Type

The details of the SQL plan baseline dimensions.

Syntax
```

```

Fields

Field Description

`attribute_name`

(required) The name of the SQL plan baseline attribute.

`attribute_value`

(required) The value of the attribute.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_AGGREGATION_T Type

A summary of SQL plan baselines.

Syntax
```

```

Fields

Field Description

`dimensions`

(required)

`l_count`

(optional) The number of SQL plan baselines matching aggregation criteria.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_plan_baseline_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_AGGREGATION_COLLECTION_T Type

A collection of SQL plan baseline aggregations.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SQL plan baseline aggregations.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_SUMMARY_T Type

The summary of a SQL plan baseline.

Syntax
```

```

Fields

Field Description

`plan_name`

(required) The unique plan identifier.

`sql_handle`

(required) The unique SQL identifier.

`sql_text`

(required) The SQL text (truncated to the first 50 characters).

`origin`

(optional) The origin of the SQL plan baseline.

Allowed values are: 'ADDM_SQLTUNE', 'AUTO_CAPTURE', 'AUTO_SQLTUNE', 'EVOLVE_AUTO_INDEX_LOAD', 'EVOLVE_CREATE_FROM_ADAPTIVE', 'EVOLVE_LOAD_FROM_STS', 'EVOLVE_LOAD_FROM_AWR', 'EVOLVE_LOAD_FROM_CURSOR_CACHE', 'MANUAL_LOAD', 'MANUAL_LOAD_FROM_AWR', 'MANUAL_LOAD_FROM_CURSOR_CACHE', 'MANUAL_LOAD_FROM_STS', 'MANUAL_SQLTUNE', 'STORED_OUTLINE', 'UNKNOWN'

`time_created`

(required) The date and time when the plan baseline was created.

`time_last_modified`

(optional) The date and time when the plan baseline was last modified.

`time_last_executed`

(optional) The date and time when the plan baseline was last executed. **Note:** For performance reasons, database does not update this value immediately after each execution of the plan baseline. Therefore, the plan baseline may have been executed more recently than this value indicates.

`enabled`

(optional) Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`).

`accepted`

(optional) Indicates whether the plan baseline is accepted (`YES`) or not (`NO`).

`fixed`

(optional) Indicates whether the plan baseline is fixed (`YES`) or not (`NO`).

`reproduced`

(optional) Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`). The value is set to `YES` when a plan is initially added to the plan baseline.

`auto_purge`

(optional) Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`).

`adaptive`

(optional) Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not. When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` property will be marked `YES`. When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed and the final plan determined at execution will become an accepted plan if its performance is better than the existing plan baseline. At this point, the value of the `ADAPTIVE` property is set to `NO` since the plan is no longer adaptive, but resolved.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_plan_baseline_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_COLLECTION_T Type

The SQL plan baseline list.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SQL plan baselines.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_TBL Type

Nested table type of dbms_cloud_oci_database_management_automatic_capture_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_CONFIGURATION_T Type

The configuration details of SQL plan baselines. The details include: - whether automatic initial plan capture is enabled or disabled - whether use of SQL plan baselines is enabled or disabled - whether Automatic SPM Evolve Advisor task is enabled or disabled - whether high-frequency Automatic SPM Evolve Advisor task is enabled or disabled - filters for the automatic initial plan capture - parameters for the Automatic SPM Evolve Advisor task - plan retention and allocated space for the plan baselines

Syntax
```

```

Fields

Field Description

`is_automatic_initial_plan_capture_enabled`

(required) Indicates whether the automatic capture of SQL plan baselines is enabled (`true`) or not (`false`).

`is_sql_plan_baselines_usage_enabled`

(required) Indicates whether the database uses SQL plan baselines (`true`) or not (`false`).

`is_auto_spm_evolve_task_enabled`

(required) Indicates whether the Automatic SPM Evolve Advisor task is enabled (`true`) or not (`false`).

`is_high_frequency_auto_spm_evolve_task_enabled`

(required) Indicates whether the high frequency Automatic SPM Evolve Advisor task is enabled (`true`) or not (`false`).

`plan_retention_weeks`

(required) The number of weeks to retain unused plans before they are purged.

`space_budget_percent`

(required) The maximum percent of `SYSAUX` space that can be used for SQL Management Base.

`space_budget_mb`

(optional) The maximum `SYSAUX` space that can be used for SQL Management Base in MB.

`space_used_mb`

(optional) The space used by SQL Management Base in MB.

`auto_capture_filters`

(optional) The capture filters used in automatic initial plan capture.

`auto_spm_evolve_task_parameters`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_T Type

The details of the database job used for loading and evolving SQL plan baselines.

Syntax
```

```

Fields

Field Description

`name`

(required) The job name.

`l_type`

(required) The job type.

Allowed values are: 'LOAD'

`status`

(required) The job status.

Allowed values are: 'SUCCEEDED', 'SCHEDULED', 'FAILED'

`time_created`

(optional) The date and time the job was created.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_SUMMARY_T Type

A summary of the database job used for loading and evolving SQL plan baselines.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the job.

`l_type`

(required) The type of the job.

Allowed values are: 'LOAD'

`status`

(required) The status of the job.

Allowed values are: 'SUCCEEDED', 'SCHEDULED', 'FAILED'

`time_created`

(optional) The date and time the job was created.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_plan_baseline_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_COLLECTION_T Type

A collection of database jobs used for loading and evolving SQL plan baselines.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SQL plan baseline jobs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_T Type

The summary of a SQL Tuning Advisor task.

Syntax
```

```

Fields

Field Description

`sql_tuning_advisor_task_id`

(required) The unique identifier of the SQL Tuning Advisor task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_id`

(optional) The instance ID of the SQL Tuning Advisor task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(optional) The name of the SQL Tuning Advisor task.

`description`

(optional) The description of the SQL Tuning Advisor task.

`owner`

(optional) The owner of the SQL Tuning Advisor task.

`time_created`

(optional) The Creation date of the SQL Tuning Advisor task.

`task_status`

(optional) The status of the SQL Tuning Advisor task.

Allowed values are: 'COMPLETED', 'INITIAL', 'EXECUTING', 'INTERRUPTED', 'ERROR'

`days_to_expire`

(optional) The number of days left before the task expires. If the value equals -1, then the task has no expiration time (UNLIMITED).

`time_execution_started`

(optional) The start time of the task execution.

`time_execution_ended`

(optional) The end time of the task execution.

`total_sql_statements`

(optional) The total number of SQL statements related to the SQL Tuning Advisor task.

`recommendation_count`

(optional) The number of recommendations provided for the SQL Tuning Advisor task.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_advisor_task_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_COLLECTION_T Type

The SQL Tuning Advisor task list.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SQL Tuning Advisor tasks.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_FINDING_SUMMARY_T Type

A summary of the findings of the objects in a tuning task that match a given filter. This includes the kind of findings that were reported, whether the benefits were analyzed, and the number of benefits obtained.

Syntax
```

```

Fields

Field Description

`sql_tuning_advisor_task_id`

(required) The unique identifier of the SQL Tuning Advisor task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_tuning_advisor_task_object_id`

(required) The key of the object to which these recommendations apply. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_tuning_advisor_task_object_execution_id`

(required) The execution id of the analyzed SQL object. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_text`

(required) The text of the SQL statement.

`parsing_schema`

(required) The parsing schema of the object.

`sql_key`

(required) The unique key of this SQL statement.

`db_time_benefit`

(optional) The time benefit (in seconds) for the highest-rated finding for this object.

`per_execution_percentage`

(optional) The per-execution percentage benefit.

`is_stats_finding_present`

(optional) Indicates whether a statistics recommendation was reported for this SQL statement.

`is_sql_profile_finding_present`

(optional) Indicates whether a SQL Profile recommendation was reported for this SQL statement.

`is_sql_profile_finding_implemented`

(optional) Indicates whether a SQL Profile recommendation has been implemented for this SQL statement.

`is_index_finding_present`

(optional) Indicates whether an index recommendation was reported for this SQL statement.

`is_restructure_sql_finding_present`

(optional) Indicates whether a restructure SQL recommendation was reported for this SQL statement.

`is_alternative_plan_finding_present`

(optional) Indicates whether an alternative execution plan was reported for this SQL statement.

`is_miscellaneous_finding_present`

(optional) Indicates whether a miscellaneous finding was reported for this SQL statement.

`is_error_finding_present`

(optional) Indicates whether there is an error in this SQL statement.

`is_timeout_finding_present`

(optional) Indicates whether the task timed out.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_FINDING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_advisor_task_finding_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_FINDING_COLLECTION_T Type

The list of findings for a SQL Tuning Advisor task.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of the findings for a tuning task.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_RECOMMENDATION_SUMMARY_T Type

A recommendation for a given object in a SQL Tuning Task.

Syntax
```

```

Fields

Field Description

`sql_tuning_advisor_task_id`

(required) The unique identifier of the task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`sql_tuning_advisor_task_object_id`

(required) The key of the object to which these recommendations apply. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`recommendation_key`

(required) The unique identifier of the recommendation in the scope of the task.

`recommendation_type`

(required) Type of recommendation.

Allowed values are: 'STATISTICS', 'INDEX', 'SQL_PROFILE', 'RESTRUCTURE_SQL', 'ALTERNATIVE_PLANS', 'ERROR', 'MISCELLANEOUS'

`finding`

(optional) Summary of the issue found in the SQL statement.

`recommendation`

(optional) The recommendation for a specific finding.

`rationale`

(optional) Describes the reasoning behind the recommendation and how it relates to the finding.

`benefit`

(optional) The percentage benefit of this implementation.

`implement_action_sql`

(optional) Action sql to be implemented based on the recommendation result.

`is_parallel_execution`

(optional) Indicates whether a SQL Profile recommendation uses parallel execution.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_RECOMMENDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_advisor_task_recommendation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_RECOMMENDATION_COLLECTION_T Type

The SQL Tuning Advisor recommendations for a given SQL statement.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SQL Tuning Advisor recommendations.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_EXECUTION_PLAN_STEP_T Type

A step in the SQL execution plan.

Syntax
```

```

Fields

Field Description

`plan_hash_value`

(optional) The numerical representation of the SQL execution plan.

`step_id`

(optional) The identification number of a step in the SQL execution plan. This is unique within the SQL execution plan. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`parent_step_id`

(optional) The ID of the next step that operates on the results of this step. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`position`

(optional) The order of processing for steps with the same parent ID.

`operation`

(optional) The name of the operation performed at this step.

`options`

(optional) The options used for the operation performed at this step.

`optimizer_mode`

(optional) The current mode of the optimizer, such as all_rows, first_rows_n (where n = 1, 10, 100, 1000, and so on).

`cost`

(optional) The cost of the current operation estimated by the cost-based optimizer (CBO).

`cardinality`

(optional) The number of rows returned by the current operation (estimated by the CBO).

`bytes`

(optional) The number of bytes returned by the current operation.

`cpu_cost`

(optional) The CPU cost of the current operation.

`io_cost`

(optional) The I/O cost of the current operation.

`temp_space`

(optional) The temporary space usage (in bytes) of the operation (sort or hash-join) as estimated by the CBO.

`time`

(optional) The elapsed time (in seconds) of the operation as estimated by the CBO.

`object_node`

(optional) The name of the database link used to reference the object.

`object_owner`

(optional) The owner of the object.

`object_name`

(optional) The name of the object.

`object_position`

(optional) The numbered position of the object name in the original SQL statement.

`object_type`

(optional) The descriptive modifier that further describes the type of object.

`partition_start`

(optional) A step may get data from a range of partitions of a partitioned object, such as table or index, based on predicates and sorting order. The partionStart is the starting partition of the range. The partitionStop is the ending partition of the range.

`partition_stop`

(optional) A step may get data from a range of partitions of a partitioned object, such as table or index, based on predicates and sorting order. The partionStart is the starting partition of the range. The partitionStop is the ending partition of the range.

`partition_id`

(optional) The ID of the step in the execution plan that has computed the pair of values of partitionStart and partitionStop.

`remarks`

(optional) The place for comments that can be added to the steps of the execution plan.

`number_of_search_column`

(optional) Number of index columns with start and stop keys (that is, the number of columns with matching predicates).

`other`

(optional) Information about parallel execution servers and parallel queries

`other_tag`

(optional) Describes the function of the SQL text in the OTHER column.

`attribute`

(optional) The text string identifying the type of execution plan.

`access_predicates`

(optional) The predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan.

`filter_predicates`

(optional) The predicates used to filter rows before producing them.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_EXECUTION_PLAN_STEP_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_task_sql_execution_plan_step_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SQL_EXECUTION_PLAN_T Type

A SQL execution plan.

Syntax
```

```

Fields

Field Description

`plan`

(required) A SQL execution plan as a list of steps.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_FINDING_BENEFITS_T Type

The benefits of the findings in the SQL Tuning Advisor summary report.

Syntax
```

```

Fields

Field Description

`db_time_before_recommended`

(required) The actual database time of the SQL statements for which SQL Tuning Advisor recommendations are not implemented.

`db_time_after_recommended`

(required) The estimated database time of the above SQL statements, if SQL Tuning Advisor recommendations are implemented.

`db_time_after_implemented`

(required) The actual database time of the SQL statements for which SQL Tuning Advisor recommendations are implemented.

`db_time_before_implemented`

(required) The actual database time of the above SQL statements, before SQL Tuning Advisor recommendations are implemented.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_FINDING_COUNTS_T Type

The number of findings in the SQL Tuning Advisor summary report.

Syntax
```

```

Fields

Field Description

`recommended_sql_profile`

(required) The number of distinct SQL statements with recommended SQL profiles.

`implemented_sql_profile`

(required) The number of distinct SQL statements with implemented SQL profiles.

`l_index`

(required) The number of distinct SQL statements with index recommendations.

`restructure`

(required) The number of distinct SQL statements with restructured SQL recommendations.

`statistics`

(required) The number of distinct SQL statements with stale or missing optimizer statistics recommendations.

`alternate_plan`

(required) The number of distinct SQL statements with alternative plan recommendations.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_TASK_INFO_T Type

The general information regarding the SQL Tuning Advisor task.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the SQL Tuning Advisor task. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(required) The name of the SQL Tuning Advisor task.

`description`

(optional) The description of the SQL Tuning Advisor task. This is not defined for Auto SQL Tuning tasks.

`owner`

(required) The owner of the SQL Tuning Advisor task.

`status`

(optional) The status of the SQL Tuning Advisor task. This is not defined for Auto SQL Tuning tasks.

Allowed values are: 'COMPLETED', 'INITIAL', 'EXECUTING', 'INTERRUPTED', 'ERROR'

`time_started`

(required) The start time of the task execution.

`time_ended`

(required) The end time of the task execution.

`running_time`

(optional) The total running time in seconds. This is not defined for Auto SQL Tuning tasks.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_STATEMENT_COUNTS_T Type

The number of statements in the SQL Tuning Advisor summary report.

Syntax
```

```

Fields

Field Description

`distinct_sql`

(required) The number of distinct SQL statements.

`total_sql`

(required) The total number of SQL statements.

`finding_count`

(required) The number of distinct SQL statements with findings.

`error_count`

(required) The number of distinct SQL statements with errors.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_STATISTICS_T Type

The statistics of the statements and findings in the SQL Tuning Advisor summary report.

Syntax
```

```

Fields

Field Description

`statement_counts`

(required)

`finding_counts`

(required)

`finding_benefits`

(required)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_OBJECT_STAT_FINDING_SUMMARY_T Type

A summary for all the statistic findings of an object in a SQL Tuning Advisor task. Includes the object's hash, name, type, schema, problem type and the object reference count.

Syntax
```

```

Fields

Field Description

`object_hash_value`

(required) Numerical representation of the object.

`object_name`

(required) Name of the object.

`object_type`

(required) Type of the object.

`schema`

(required) Schema of the object.

`problem_type`

(required) Type of statistics problem related to the object.

Allowed values are: 'MISSING', 'STALE'

`reference_count`

(required) The number of the times the object is referenced within the SQL Tuning advisor task findings.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_INDEX_FINDING_SUMMARY_T Type

A summary for all the index findings in a SQL Tuning Advisor task. Includes the index's hash value, table name, schema, index name, reference count and index columns

Syntax
```

```

Fields

Field Description

`index_hash_value`

(required) Numerical representation of the index.

`index_name`

(required) Name of the index.

`table_name`

(required) Table's name related to the index.

`schema`

(required) Schema related to the index.

`reference_count`

(required) The number of times the index is referenced within the SQL Tuning advisor task findings.

`index_columns`

(required) Columns of the index.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_OBJECT_STAT_FINDING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_advisor_task_summary_report_object_stat_finding_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_INDEX_FINDING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_advisor_task_summary_report_index_finding_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_T Type

The content of the SQL Tuning Advisor summary report.

Syntax
```

```

Fields

Field Description

`task_info`

(required)

`statistics`

(required)

`object_stat_findings`

(optional) The list of object findings related to statistics.

`index_findings`

(optional) The list of object findings related to indexes.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_IN_SQL_TUNING_SET_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_in_sql_tuning_set_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_T Type

Details of the Sql tuning set.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique Sql tuning set identifier.

`owner`

(required) The owner of the Sql tuning set.

`name`

(required) The name of the Sql tuning set.

`statement_count`

(optional) Number of statements in the Sql tuning set

`time_created`

(optional) The created time of the Sql tuning set.

`description`

(optional) The description of the Sql tuning set.

`time_last_modified`

(optional) Last modified time of the Sql tuning set.

`status`

(optional) Current status of the Sql tuning set.

Allowed values are: 'DISABLED', 'RETRY_SCHEDULED', 'SCHEDULED', 'BLOCKED', 'RUNNING', 'COMPLETED', 'BROKEN', 'FAILED', 'REMOTE', 'RESOURCE_UNAVAILABLE', 'SUCCEEDED', 'CHAIN_STALLED'

`scheduled_job_name`

(optional) Name of the Sql tuning set scheduler job.

`error_message`

(optional) Latest execution error of the plsql that was submitted as a scheduler job.

`all_sql_statements_fetched`

(optional) In OCI database management, there is a limit to fetch only 2000 rows. This flag indicates whether all Sql statements of this Sql tuning set matching the filter criteria are fetched or not. Possible values are 'Yes' or 'No' - Yes - All Sql statements matching the filter criteria are fetched. - No - There are more Sql statements matching the fitler criteria. User should fine tune the filter criteria to narrow down the result set.

`sql_list`

(optional) A list of the Sqls associated with the Sql tuning set.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_ACTION_STATUS_T Type

The status of a Sql tuning set admin action.

Syntax
```

```

Fields

Field Description

`status`

(required) The status of a Sql tuning set admin action.

Allowed values are: 'SUCCEEDED', 'FAILED'

`success_message`

(optional) The success message of the Sql tuning set admin action. The success message is \"null\" if the admin action is non successful.

`error_code`

(optional) The error code that denotes failure if the Sql tuning set admin action is not successful. The error code is \"null\" if the admin action is successful.

`error_message`

(optional) The error message that indicates the reason for failure if the Sql tuning set admin action is not successful. The error message is \"null\" if the admin action is successful.

`show_sql_only`

(optional) Flag to indicate whether to create the Sql tuning set or just display the plsql used for the selected user action.

`sql_statement`

(optional) When showSqlOnly is set to 1, this attribute displays the plsql generated for the selected user action. When showSqlOnly is set to 0, this attribute will not be returned.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_PASSWORD_CREDENTIAL_DETAILS_T Type

User provides a password to be used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_sql_tuning_set_admin_password_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_sql_tuning_set_admin_credential_details_t`type.

Fields

Field Description

`password`

(required) The database user's password encoded using BASE64 scheme.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_SECRET_CREDENTIAL_DETAILS_T Type

User provides a secret OCID, which will be used to retrieve the password to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_sql_tuning_set_admin_secret_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_sql_tuning_set_admin_credential_details_t`type.

Fields

Field Description

`secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the database password is stored.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_SUMMARY_T Type

The summary information of a SQL tuning set.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the SQL tuning set.

`owner`

(required) The owner of the SQL tuning set.

`description`

(optional) The description of the SQL tuning set.

`statement_counts`

(optional) The number of SQL statements in the SQL tuning set.

`id`

(optional) The unique Sql tuning set identifier. This is not OCID.

`time_created`

(optional) The created time of the Sql tuning set.

`time_last_modified`

(optional) Last modified time of the Sql tuning set.

`status`

(optional) Current status of the Sql tuning set.

Allowed values are: 'DISABLED', 'RETRY_SCHEDULED', 'SCHEDULED', 'BLOCKED', 'RUNNING', 'COMPLETED', 'BROKEN', 'FAILED', 'REMOTE', 'RESOURCE_UNAVAILABLE', 'SUCCEEDED', 'CHAIN_STALLED'

`scheduled_job_name`

(optional) Name of the Sql tuning set scheduler job.

`error_message`

(optional) Latest execution error of the plsql that was submitted as a scheduler job.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_set_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_COLLECTION_T Type

The details in the SQL tuning set summary.

Syntax
```

```

Fields

Field Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`items`

(required) The details in the SQL tuning set summary.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_INPUT_T Type

The SQL tuning set for a SQL tuning task.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the SQL tuning set.

`owner`

(required) The owner of the SQL tuning set.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_PASSWORD_CREDENTIAL_DETAILS_T Type

The password provided by the user to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_sql_tuning_task_password_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_sql_tuning_task_credential_details_t`type.

Fields

Field Description

`password`

(required) The database user's password encoded using BASE64 scheme.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_RETURN_T Type

The returned object for starting or cloning a SQL tuning advisor task.

Syntax
```

```

Fields

Field Description

`sql_tuning_task_id`

(required) The identifier of the task being started or cloned. This is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint`LIST_SQL_TUNING_ADVISOR_TASKS`Function.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SECRET_CREDENTIAL_DETAILS_T Type

The OCID of the Secret provided by the user to retrieve the password to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_sql_tuning_task_secret_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_sql_tuning_task_credential_details_t`type.

Fields

Field Description

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the database password is stored.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_DETAIL_T Type

The details of the SQL statements on which SQL tuning is performed.

Syntax
```

```

Fields

Field Description

`sql_id`

(required) The identifier of a SQL statement.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_tuning_task_sql_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_START_SQL_TUNING_TASK_DETAILS_T Type

The request to start a SQL tuning task.

Syntax
```

```

Fields

Field Description

`task_name`

(required) The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.

`task_description`

(optional) The description of the SQL tuning task.

`credential_details`

(required)

`total_time_limit_in_minutes`

(required) The time limit for running the SQL tuning task.

`scope`

(required) The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation is included.

Allowed values are: 'LIMITED', 'COMPREHENSIVE'

`statement_time_limit_in_minutes`

(optional) The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope. The time limit per SQL statement should not be more than the total time limit.

`sql_tuning_set`

(optional)

`sql_details`

(optional) The details of the SQL statement on which tuning is performed. To obtain the details of the SQL statement, you must provide either the sqlTuningSet or the tuple of sqlDetails/timeStarted/timeEnded.

`time_started`

(optional) The start time of the period in which SQL statements are running.

`time_ended`

(optional) The end time of the period in which SQL statements are running.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SYSTEM_PRIVILEGE_SUMMARY_T Type

A Summary of system privileges.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of a system privilege.

`admin_option`

(optional) Indicates whether the system privilege is granted with the ADMIN option (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`common`

(optional) Indicates how the system privilege was granted. Possible values: YES if the system privilege is granted commonly (CONTAINER=ALL is used) NO if the system privilege is granted locally (CONTAINER=ALL is not used)

Allowed values are: 'YES', 'NO'

`inherited`

(optional) Indicates whether the granted system privilege is inherited from another container (YES) or not (NO).

Allowed values are: 'YES', 'NO'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SYSTEM_PRIVILEGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_system_privilege_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SYSTEM_PRIVILEGE_COLLECTION_T Type

A collection of system privileges granted to the current user.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of system privileges.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLE_STATISTIC_SUMMARY_T Type

The summary of table statistics statuses, which includes status categories such as Stale, Not Stale, and No Stats, the number of table statistics grouped by status category, and the percentage of objects with a particular status.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The valid status categories of table statistics.

Allowed values are: 'NO_STATS', 'STALE', 'NOT_STALE'

`l_count`

(required) The number of objects aggregated by status category.

`percentage`

(required) The percentage of objects with a particular status.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLE_STATISTIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_table_statistic_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLE_STATISTICS_COLLECTION_T Type

A collection of table statistics, which are grouped by status.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of table statistics statuses.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATAFILE_TBL Type

Nested table type of dbms_cloud_oci_database_management_datafile_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_T Type

The details of a tablespace.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the tablespace.

`l_type`

(required) The type of tablespace.

Allowed values are: 'UNDO', 'LOST_WRITE_PROTECTION', 'PERMANENT', 'TEMPORARY'

`status`

(optional) The status of the tablespace.

Allowed values are: 'ONLINE', 'OFFLINE', 'READ_ONLY'

`block_size_bytes`

(optional) The tablespace block size.

`logging`

(optional) The default logging attribute.

Allowed values are: 'LOGGING', 'NOLOGGING'

`is_force_logging`

(optional) Indicates whether the tablespace is under Force Logging mode.

`extent_management`

(optional) Indicates whether the extents in the tablespace are Locally managed or Dictionary managed.

Allowed values are: 'LOCAL', 'DICTIONARY'

`allocation_type`

(optional) The type of extent allocation in effect for the tablespace.

Allowed values are: 'SYSTEM', 'UNIFORM', 'USER'

`is_plugged_in`

(optional) Indicates whether the tablespace is plugged in.

`segment_space_management`

(optional) Indicates whether the free and used segment space in the tablespace is managed using free lists (MANUAL) or bitmaps (AUTO).

Allowed values are: 'MANUAL', 'AUTO'

`default_table_compression`

(optional) Indicates whether default table compression is enabled or disabled.

Allowed values are: 'ENABLED', 'DISABLED'

`retention`

(optional) Indicates whether undo retention guarantee is enabled for the tablespace.

Allowed values are: 'GUARANTEE', 'NOGUARANTEE', 'NOT_APPLY'

`is_bigfile`

(optional) Indicates whether the tablespace is a Bigfile tablespace or a Smallfile tablespace.

`predicate_evaluation`

(optional) Indicates whether predicates are evaluated by Host or by Storage.

Allowed values are: 'HOST', 'STORAGE'

`is_encrypted`

(optional) Indicates whether the tablespace is encrypted.

`compress_for`

(optional) The operation type for which default compression is enabled.

Allowed values are: 'BASIC', 'ADVANCED', 'QUERY_LOW', 'QUERY_HIGH', 'ARCHIVE_LOW', 'ARCHIVE_HIGH', 'DIRECT_LOAD_ONLY', 'FOR_ALL_OPERATIONS'

`default_in_memory`

(optional) Indicates whether the In-Memory Column Store (IM column store) is by default enabled or disabled for tables in the tablespace.

Allowed values are: 'ENABLED', 'DISABLED'

`default_in_memory_priority`

(optional) Indicates the default priority for In-Memory Column Store (IM column store) population for the tablespace.

Allowed values are: 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL', 'NONE'

`default_in_memory_distribute`

(optional) Indicates how the IM column store is distributed by default for the tablespace in an Oracle Real Application Clusters (Oracle RAC) environment.

Allowed values are: 'AUTO', 'BY_ROWID_RANGE', 'BY_PARTITION', 'BY_SUBPARTITION'

`default_in_memory_compression`

(optional) Indicates the default compression level for the IM column store for the tablespace.

Allowed values are: 'NO_MEMCOMPRESS', 'FOR_DML', 'FOR_QUERY_LOW', 'FOR_QUERY_HIGH', 'FOR_CAPACITY_LOW', 'FOR_CAPACITY_HIGH'

`default_in_memory_duplicate`

(optional) Indicates the duplicate setting for the IM column store in an Oracle RAC environment.

Allowed values are: 'NO_DUPLICATE', 'DUPLICATE', 'DUPLICATE_ALL'

`shared`

(optional) Indicates whether the tablespace is for shared tablespace, or for local temporary tablespace for leaf (read-only) instances, or for local temporary tablespace for all instance types.

Allowed values are: 'SHARED', 'LOCAL_ON_LEAF', 'LOCAL_ON_ALL'

`default_index_compression`

(optional) Indicates whether default index compression is enabled or disabled.

Allowed values are: 'ENABLED', 'DISABLED'

`index_compress_for`

(optional) The operation type for which default index compression is enabled.

Allowed values are: 'ADVANCED_LOW', 'ADVANCED_HIGH', 'NONE'

`default_cell_memory`

(optional) This specifies the default value for the CELLMEMORY attribute that tables created in the tablespace will inherit unless the behavior is overridden explicitly. This column is intended for use with Oracle Exadata.

`default_in_memory_service`

(optional) Indicates how the IM column store is populated on various instances by default for the tablespace.

Allowed values are: 'DEFAULT', 'NONE', 'ALL', 'USER_DEFINED'

`default_in_memory_service_name`

(optional) Indicates the service name for the service on which the IM column store should be populated by default for the tablespace. This column has a value only when the corresponding DEF_INMEMORY_SERVICE is USER_DEFINED. In all other cases, this column is null.

`lost_write_protect`

(optional) The lost write protection setting for the tablespace.

Allowed values are: 'ENABLED', 'PROTECT_OFF', 'SUSPEND'

`is_chunk_tablespace`

(optional) Indicates whether this is a chunk tablespace.

`temp_group`

(optional) The temporary tablespace group.

`max_size_kb`

(optional) The maximum tablespace size in KB. If the tablespace contains any data files with Autoextend enabled, then this column displays the amount of underlying free storage space for the tablespace. For example, if the current tablespace size is 1 GB, the combined maximum size of all its data files is 32 GB, and its underlying storage (for example, ASM or file system storage) has 20 GB of free space, then this column will have a value of approximately 20 GB. If the tablespace contains only data files with autoextend disabled, then this column displays the allocated space for the entire tablespace, that is, the combined size of all data files in the tablespace.

`allocated_size_kb`

(optional) The allocated tablespace size in KB.

`user_size_kb`

(optional) The size of the tablespace available for user data in KB. The difference between tablespace size and user data size is used for storing metadata.

`free_space_kb`

(optional) The free space available in the tablespace in KB.

`used_space_kb`

(optional) The total space used by the tablespace in KB.

`used_percent_available`

(optional) The percentage of used space out of the maximum available space in the tablespace.

`used_percent_allocated`

(optional) The percentage of used space out of the total allocated space in the tablespace.

`is_default`

(optional) Indicates whether this is the default tablespace.

`datafiles`

(optional) A list of the data files associated with the tablespace.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_PASSWORD_CREDENTIAL_DETAILS_T Type

User provides a password to be used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_tablespace_admin_password_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_tablespace_admin_credential_details_t`type.

Fields

Field Description

`password`

(required) The database user's password encoded using BASE64 scheme.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_SECRET_CREDENTIAL_DETAILS_T Type

User provides a secret OCID, which will be used to retrieve the password to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_management_tablespace_admin_secret_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_tablespace_admin_credential_details_t`type.

Fields

Field Description

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the database password is stored.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_STATUS_T Type

The status of a tablespace admin action.

Syntax
```

```

Fields

Field Description

`status`

(required) The status of a tablespace admin action.

Allowed values are: 'SUCCEEDED', 'FAILED'

`error_code`

(optional) The error code that denotes failure if the tablespace admin action is not successful. The error code is \"null\" if the admin action is successful.

`error_message`

(optional) The error message that indicates the reason for failure if the tablespace admin action is not successful. The error message is \"null\" if the admin action is successful.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_SUMMARY_T Type

The summary of a tablespace.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the tablespace.

`l_type`

(required) The type of tablespace.

Allowed values are: 'UNDO', 'LOST_WRITE_PROTECTION', 'PERMANENT', 'TEMPORARY'

`status`

(optional) The status of the tablespace.

Allowed values are: 'ONLINE', 'OFFLINE', 'READ_ONLY'

`block_size_bytes`

(optional) The tablespace block size.

`logging`

(optional) The default logging attribute.

Allowed values are: 'LOGGING', 'NOLOGGING'

`is_force_logging`

(optional) Indicates whether the tablespace is under Force Logging mode.

`extent_management`

(optional) Indicates whether the extents in the tablespace are Locally managed or Dictionary managed.

Allowed values are: 'LOCAL', 'DICTIONARY'

`allocation_type`

(optional) The type of extent allocation in effect for the tablespace.

Allowed values are: 'SYSTEM', 'UNIFORM', 'USER'

`is_plugged_in`

(optional) Indicates whether the tablespace is plugged in.

`segment_space_management`

(optional) Indicates whether the free and used segment space in the tablespace is managed using free lists (MANUAL) or bitmaps (AUTO).

Allowed values are: 'MANUAL', 'AUTO'

`default_table_compression`

(optional) Indicates whether default table compression is enabled or disabled.

Allowed values are: 'ENABLED', 'DISABLED'

`retention`

(optional) Indicates whether undo retention guarantee is enabled for the tablespace.

Allowed values are: 'GUARANTEE', 'NOGUARANTEE', 'NOT_APPLY'

`is_bigfile`

(optional) Indicates whether the tablespace is a Bigfile tablespace or a Smallfile tablespace.

`predicate_evaluation`

(optional) Indicates whether predicates are evaluated by Host or by Storage.

Allowed values are: 'HOST', 'STORAGE'

`is_encrypted`

(optional) Indicates whether the tablespace is encrypted.

`compress_for`

(optional) The operation type for which default compression is enabled.

Allowed values are: 'BASIC', 'ADVANCED', 'QUERY_LOW', 'QUERY_HIGH', 'ARCHIVE_LOW', 'ARCHIVE_HIGH', 'DIRECT_LOAD_ONLY', 'FOR_ALL_OPERATIONS'

`default_in_memory`

(optional) Indicates whether the In-Memory Column Store (IM column store) is by default enabled or disabled for tables in the tablespace.

Allowed values are: 'ENABLED', 'DISABLED'

`default_in_memory_priority`

(optional) Indicates the default priority for In-Memory Column Store (IM column store) population for the tablespace.

Allowed values are: 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL', 'NONE'

`default_in_memory_distribute`

(optional) Indicates how the IM column store is distributed by default for the tablespace in an Oracle Real Application Clusters (Oracle RAC) environment.

Allowed values are: 'AUTO', 'BY_ROWID_RANGE', 'BY_PARTITION', 'BY_SUBPARTITION'

`default_in_memory_compression`

(optional) Indicates the default compression level for the IM column store for the tablespace.

Allowed values are: 'NO_MEMCOMPRESS', 'FOR_DML', 'FOR_QUERY_LOW', 'FOR_QUERY_HIGH', 'FOR_CAPACITY_LOW', 'FOR_CAPACITY_HIGH'

`default_in_memory_duplicate`

(optional) Indicates the duplicate setting for the IM column store in an Oracle RAC environment.

Allowed values are: 'NO_DUPLICATE', 'DUPLICATE', 'DUPLICATE_ALL'

`shared`

(optional) Indicates whether the tablespace is for shared tablespace, or for local temporary tablespace for leaf (read-only) instances, or for local temporary tablespace for all instance types.

Allowed values are: 'SHARED', 'LOCAL_ON_LEAF', 'LOCAL_ON_ALL'

`default_index_compression`

(optional) Indicates whether default index compression is enabled or disabled.

Allowed values are: 'ENABLED', 'DISABLED'

`index_compress_for`

(optional) The operation type for which default index compression is enabled.

Allowed values are: 'ADVANCED_LOW', 'ADVANCED_HIGH', 'NONE'

`default_cell_memory`

(optional) This specifies the default value for the CELLMEMORY attribute that tables created in the tablespace will inherit unless the behavior is overridden explicitly. This column is intended for use with Oracle Exadata.

`default_in_memory_service`

(optional) Indicates how the IM column store is populated on various instances by default for the tablespace.

Allowed values are: 'DEFAULT', 'NONE', 'ALL', 'USER_DEFINED'

`default_in_memory_service_name`

(optional) Indicates the service name for the service on which the IM column store should be populated by default for the tablespace. This column has a value only when the corresponding DEF_INMEMORY_SERVICE is USER_DEFINED. In all other cases, this column is null.

`lost_write_protect`

(optional) The lost write protection setting for the tablespace.

Allowed values are: 'ENABLED', 'PROTECT_OFF', 'SUSPEND'

`is_chunk_tablespace`

(optional) Indicates whether this is a chunk tablespace.

`temp_group`

(optional) The temporary tablespace group.

`max_size_kb`

(optional) The maximum tablespace size in KB. If the tablespace contains any data files with Autoextend enabled, then this column displays the amount of underlying free storage space for the tablespace. For example, if the current tablespace size is 1 GB, the combined maximum size of all its data files is 32 GB, and its underlying storage (for example, ASM or file system storage) has 20 GB of free space, then this column will have a value of approximately 20 GB. If the tablespace contains only data files with autoextend disabled, then this column displays the allocated space for the entire tablespace, that is, the combined size of all data files in the tablespace.

`allocated_size_kb`

(optional) The allocated tablespace size in KB.

`user_size_kb`

(optional) The size of the tablespace available for user data in KB. The difference between tablespace size and user data size is used for storing metadata.

`free_space_kb`

(optional) The free space available in the tablespace in KB.

`used_space_kb`

(optional) The total space used by the tablespace in KB.

`used_percent_available`

(optional) The percentage of used space out of the maximum available space in the tablespace.

`used_percent_allocated`

(optional) The percentage of used space out of the total allocated space in the tablespace.

`is_default`

(optional) Indicates whether this is the default tablespace.

`datafiles`

(optional) A list of the data files associated with the tablespace.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_tablespace_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_COLLECTION_T Type

A collection of tablespaces for a specific Managed Database.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of TablespaceSummary resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TEST_PREFERRED_CREDENTIAL_DETAILS_T Type

The status of the preferred credential test. The status is 'SUCCEEDED' if the preferred credential is working else the status is 'FAILED'.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of preferred credential. Only 'BASIC' is supported currently.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TEST_BASIC_PREFERRED_CREDENTIAL_DETAILS_T Type

The details of the 'BASIC' preferred credential.

Syntax
```

```

`dbms_cloud_oci_database_management_test_basic_preferred_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_test_preferred_credential_details_t`type.

Fields

Field Description

`user_name`

(optional) The user name used to connect to the database.

`role`

(optional) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Vault service secret that contains the database user password.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TEST_PREFERRED_CREDENTIAL_STATUS_T Type

The status of the preferred credential test. The status is 'SUCCEEDED' if the preferred credential is working else the status is 'FAILED'.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status of the preferred credential test. The status is 'SUCCEEDED' if the preferred credential is working else the status is 'FAILED'.

Allowed values are: 'SUCCEEDED', 'FAILED'

`error_code`

(optional) An error code that defines the failure of the preferred credential test. The response is 'null' if the preferred credential test was successful.

`error_message`

(optional) The error message that indicates the reason for the failure of the preferred credential test. The response is 'null' if the preferred credential test was successful.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_CPU_ACTIVITY_TBL Type

Nested table type of dbms_cloud_oci_database_management_sql_cpu_activity_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TOP_SQL_CPU_ACTIVITY_T Type

A list of SQL IDs with most CPU activity.

Syntax
```

```

Fields

Field Description

`activity`

(required) A list of sql CPU activity.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_PREFERRED_CREDENTIAL_DETAILS_T Type

The details required to update the preferred credential.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of preferred credential.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_BASIC_PREFERRED_CREDENTIAL_DETAILS_T Type

The details of the 'BASIC' preferred credential.

Syntax
```

```

`dbms_cloud_oci_database_management_update_basic_preferred_credential_details_t`is a subtype of the`dbms_cloud_oci_database_management_update_preferred_credential_details_t`type.

Fields

Field Description

`user_name`

(optional) The user name used to connect to the database.

`role`

(optional) The role of the database user.

Allowed values are: 'NORMAL', 'SYSDBA'

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Vault service secret that contains the database user password.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_DATABASE_PARAMETERS_RESULT_T Type

The results of database parameter update.

Syntax
```

```

Fields

Field Description

`status`

(required) A map with the parameter name as key and its update status as value.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_DB_MANAGEMENT_PRIVATE_ENDPOINT_DETAILS_T Type

The details used to update a Database Management private endpoint.

Syntax
```

```

Fields

Field Description

`name`

(optional) The display name of the private endpoint.

`description`

(optional) The description of the private endpoint.

`nsg_ids`

(optional) The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_ASM_DETAILS_T Type

The details required to update an external ASM.

Syntax
```

```

Fields

Field Description

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_CLUSTER_DETAILS_T Type

The details required to update an external cluster.

Syntax
```

```

Fields

Field Description

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_CLUSTER_INSTANCE_DETAILS_T Type

The details required to update an external cluster instance.

Syntax
```

```

Fields

Field Description

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_NODE_DETAILS_T Type

The details required to update an external DB node.

Syntax
```

```

Fields

Field Description

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_CONNECTOR_DETAILS_T Type

The details required to update an external DB system connector.

Syntax
```

```

Fields

Field Description

`connector_type`

(required) The type of connector.

Allowed values are: 'MACS'

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_DETAILS_T Type

The details required to update an external DB system.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the DB system. The name does not have to be unique.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_DISCOVERY_DETAILS_T Type

The details required to update an external DB system discovery resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the DB system. The name does not have to be unique.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_MACS_CONNECTOR_DETAILS_T Type

The details for updating the external[Management Agent Cloud Service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html)connector used to connect to an external DB system component.

Syntax
```

```

`dbms_cloud_oci_database_management_update_external_db_system_macs_connector_details_t`is a subtype of the`dbms_cloud_oci_database_management_update_external_db_system_connector_details_t`type.

Fields

Field Description

`connection_info`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_EXADATA_INFRASTRUCTURE_DETAILS_T Type

The details required to update the external Exadata infrastructure.

Syntax
```

```

Fields

Field Description

`discovery_key`

(optional) The unique key of the discovery request.

`license_model`

(optional) The Oracle license model that applies to the database management resources.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) The name of the Exadata infrastructure.

`db_system_ids`

(optional) The list of all the DB systems OCIDs.

`storage_server_names`

(optional) The list of the names of Exadata storage servers to be monitored. If not specified, it includes all Exadata storage servers associated with the monitored DB systems.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR_DETAILS_T Type

The connector details of the Exadata storage server to be updated.

Syntax
```

```

Fields

Field Description

`connector_name`

(optional) The name of the Exadata storage server connector.

`connection_uri`

(optional) The unique string of the connection. For example, \"https://&lt;storage-server-name&gt;/MS/RESTService/\".

`credential_info`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_LISTENER_DETAILS_T Type

The details required to update an external listener.

Syntax
```

```

Fields

Field Description

`external_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_JOB_DETAILS_T Type

The details required to update a job.

Syntax
```

```

Fields

Field Description

`description`

(optional) The description of the job.

`job_type`

(optional) The type of job.

Allowed values are: 'SQL'

`timeout`

(optional) The job timeout duration, which is expressed like \"1h 10m 15s\".

`result_location`

(optional)

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_MANAGED_DATABASE_GROUP_DETAILS_T Type

The details required to update a Managed Database Group.

Syntax
```

```

Fields

Field Description

`description`

(optional) The information specified by the user about the Managed Database Group.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_SQL_JOB_DETAILS_T Type

The details specific to the SQL job request.

Syntax
```

```

`dbms_cloud_oci_database_management_update_sql_job_details_t`is a subtype of the`dbms_cloud_oci_database_management_update_job_details_t`type.

Fields

Field Description

`sql_text`

(optional) The SQL text to be executed as part of the job.

`in_binds`

(optional)

`out_binds`

(optional)

`sql_type`

(optional)

`user_name`

(optional) The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group, then the user name should exist on all the databases in the group with the same password.

`password`

(optional) The password for the database user name used to execute the SQL job.

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

`role`

(optional) The role of the database user. Indicates whether the database user is a normal user or sysdba.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_TABLESPACE_DETAILS_T Type

The details required to update a tablespace.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`name`

(optional) The name of the tablespace. It must be unique within a database.

`l_type`

(optional) The type of tablespace.

Allowed values are: 'PERMANENT', 'TEMPORARY'

`file_size`

(optional) The size of each data file or temp file.

`status`

(optional) The status of the tablespace.

Allowed values are: 'READ_ONLY', 'READ_WRITE'

`is_auto_extensible`

(optional) Specifies whether the data file or temp file can be extended automatically.

`auto_extend_next_size`

(optional) The size of the next increment of disk space to be allocated automatically when more extents are required.

`auto_extend_max_size`

(optional) The maximum disk space allowed for automatic extension of the data files or temp files.

`is_max_size_unlimited`

(optional) Specifies whether the disk space of the data file or temp file can be limited.

`is_default`

(optional) Specifies whether the tablespace is the default tablespace.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_T Type

The summary of a specific user resource.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the User.

`status`

(required) The status of the user account.

Allowed values are: 'OPEN', 'EXPIRED', 'EXPIRED_GRACE', 'LOCKED', 'LOCKED_TIMED', 'EXPIRED_AND_LOCKED', 'EXPIRED_GRACE_AND_LOCKED', 'EXPIRED_AND_LOCKED_TIMED', 'EXPIRED_GRACE_AND_LOCKED_TIMED', 'OPEN_AND_IN_ROLLOVER', 'EXPIRED_AND_IN_ROLLOVER', 'LOCKED_AND_IN_ROLLOVER', 'EXPIRED_AND_LOCKED_AND_IN_ROLLOVER', 'LOCKED_TIMED_AND_IN_ROLLOVER', 'EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL'

`time_locked`

(optional) The date the account was locked, if the status of the account is LOCKED.

`time_expiring`

(optional) The date and time of the expiration of the user account.

`default_tablespace`

(required) The default tablespace for data.

`temp_tablespace`

(required) The name of the default tablespace for temporary tables or the name of a tablespace group.

`local_temp_tablespace`

(optional) The default local temporary tablespace for the user.

`time_created`

(required) The date and time the user was created.

`profile`

(required) The profile name of the user.

`consumer_group`

(optional) The initial resource consumer group for the User.

`external_name`

(optional) The external name of the user.

`password_versions`

(optional) The list of existing versions of the password hashes (also known as \"verifiers\") for the account.

`editions_enabled`

(optional) Indicates whether editions have been enabled for the corresponding user (Y) or not (N).

Allowed values are: 'YES', 'NO'

`authentication`

(optional) The authentication mechanism for the user.

Allowed values are: 'NONE', 'EXTERNAL', 'GLOBAL', 'PASSWORD'

`proxy_connect`

(optional) Indicates whether a user can connect directly (N) or whether the account can only be proxied (Y) by users who have proxy privileges for this account (that is, by users who have been granted the \"connect through\" privilege for this account).

Allowed values are: 'YES', 'NO'

`common`

(optional) Indicates whether a given user is common(Y) or local(N).

Allowed values are: 'YES', 'NO'

`time_last_login`

(optional) The date and time of the last user login. This column is not populated when a user connects to the database with administrative privileges, that is, AS { SYSASM | SYSBACKUP | SYSDBA | SYSDG | SYSOPER | SYSRAC | SYSKM }.

`oracle_maintained`

(optional) Indicates whether the user was created and is maintained by Oracle-supplied scripts (such as catalog.sql or catproc.sql).

Allowed values are: 'YES', 'NO'

`inherited`

(optional) Indicates whether the user definition is inherited from another container (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`default_collation`

(optional) The default collation for the user schema.

`implicit`

(optional) Indicates whether the user is a common user created by an implicit application (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`all_shared`

(optional) In a sharded database, indicates whether the user is created with shard DDL enabled (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`external_shared`

(optional) In a federated sharded database, indicates whether the user is an external shard user (YES) or not (NO).

Allowed values are: 'YES', 'NO'

`time_password_changed`

(optional) The date and time when the user password was last set. This column is populated only when the value of the AUTHENTICATION_TYPE column is PASSWORD. Otherwise, this column is null.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_SUMMARY_T Type

The summary of a specific User.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the User.

`status`

(required) The status of the user account.

Allowed values are: 'OPEN', 'EXPIRED', 'EXPIRED_GRACE', 'LOCKED', 'LOCKED_TIMED', 'EXPIRED_AND_LOCKED', 'EXPIRED_GRACE_AND_LOCKED', 'EXPIRED_AND_LOCKED_TIMED', 'EXPIRED_GRACE_AND_LOCKED_TIMED', 'OPEN_AND_IN_ROLLOVER', 'EXPIRED_AND_IN_ROLLOVER', 'LOCKED_AND_IN_ROLLOVER', 'EXPIRED_AND_LOCKED_AND_IN_ROLLOVER', 'LOCKED_TIMED_AND_IN_ROLLOVER', 'EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL'

`time_expiring`

(optional) The date and time of the expiration of the user account.

`default_tablespace`

(required) The default tablespace for data.

`temp_tablespace`

(required) The name of the default tablespace for temporary tables or the name of a tablespace group.

`time_created`

(required) The date and time the user was created.

`time_locked`

(optional) The date the account was locked, if the status of the account is LOCKED.

`profile`

(required) The profile name of the user.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_COLLECTION_T Type

A collection of users for a specific Managed Database.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of User resources.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_VALIDATE_BASIC_FILTER_DETAILS_T Type

Validate the basic filter criteria provided by the user.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`owner`

(required) The owner of the Sql tuning set.

`name`

(required) The name of the Sql tuning set.

`basic_filter`

(required) Specifies the Sql predicate to filter the Sql from the Sql tuning set defined on attributes of the SQLSET_ROW. User could use any combination of the following columns with appropriate values as Sql predicate Refer to the documentation https://docs.oracle.com/en/database/oracle/oracle-database/18/arpls/DBMS_SQLTUNE.html#GUID-1F4AFB03-7B29-46FC-B3F2-CB01EC36326C

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUB_RESOURCE_T Type

The resource that is created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_name`

(required) The name of the subresource entity.

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED', 'ACCEPTED', 'ENABLED', 'DISABLED'

`identifier`

(optional) The OCID or other unique identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that is used in a GET request to access the resource metadata.

`description`

(optional) Description of the entity

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUB_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_database_management_work_request_sub_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_RESOURCE_T Type

The resource that is created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED', 'ACCEPTED', 'ENABLED', 'DISABLED'

`identifier`

(required) The OCID or other unique identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that is used in a GET request to access the resource metadata.

`entity_name`

(optional) The name of the WorkRequest resource entity.

`entity_dependencies`

(optional) The dependent resources of this work request resource, these can only be provisioned when primary resource successfully completes.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_database_management_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_T Type

A description of the work request status.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources that are not in the same compartment, then the system picks the primary resource whose compartment should be used.

`operation_type`

(required) The type of work request.

Allowed values are: 'CREATE_DB_MANAGEMENT_PRIVATE_ENDPOINT', 'DELETE_DB_MANAGEMENT_PRIVATE_ENDPOINT', 'CREATE_DB_SYSTEM_DISCOVERY', 'CREATE_DB_SYSTEM', 'UPDATE_DB_SYSTEM', 'DB_SYSTEM_ENABLE_DBMGMT', 'DB_SYSTEM_DISABLE_DBMGMT', 'DELETE_DB_SYSTEM', 'UPDATE_EXTERNAL_DB_SYSTEM_CONNECTOR', 'CHANGE_EXTERNAL_DB_SYSTEM_COMPARTMENT', 'DISABLE_EXADATA_INFRASTURCTURE', 'ENABLE_EXADATA_INFRASTRUCTURE', 'DELETE_EXADATA_INFRASTRUCTURE', 'CHANGE_EXADATA_COMPARTMENT'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`percent_complete`

(required) The completed percentage of the operation tracked by the work request.

`time_accepted`

(required) The date and time the work request was accepted, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for this time object in milliseconds.

`time_started`

(optional) The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for this time object is in milliseconds.

`time_finished`

(optional) The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for this time object is in milliseconds.

`resources`

(required) The resources affected by this work request.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUMMARY_T Type

A Summary of the work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of work request.

Allowed values are: 'CREATE_DB_MANAGEMENT_PRIVATE_ENDPOINT', 'DELETE_DB_MANAGEMENT_PRIVATE_ENDPOINT', 'CREATE_DB_SYSTEM_DISCOVERY', 'CREATE_DB_SYSTEM', 'UPDATE_DB_SYSTEM', 'DB_SYSTEM_ENABLE_DBMGMT', 'DB_SYSTEM_DISABLE_DBMGMT', 'DELETE_DB_SYSTEM', 'UPDATE_EXTERNAL_DB_SYSTEM_CONNECTOR', 'CHANGE_EXTERNAL_DB_SYSTEM_COMPARTMENT', 'DISABLE_EXADATA_INFRASTURCTURE', 'ENABLE_EXADATA_INFRASTRUCTURE', 'DELETE_EXADATA_INFRASTRUCTURE', 'CHANGE_EXADATA_COMPARTMENT'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources that are not in the same compartment then the system picks the primary resource whose compartment should be used.

`percent_complete`

(required) The completed percentage of the operation tracked by the work request.

`time_accepted`

(required) The date and time the work request was accepted, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for this time object is in milliseconds.

`time_started`

(optional) The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for this time object is in milliseconds.

`time_finished`

(optional) The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for this time object is in milliseconds.

`resources`

(required) The resources affected by this work request.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_management_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_COLLECTION_T Type

Lists all work requests in a specific compartment. This contains WorkRequestSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work requests.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the work request error.

`work_request_id`

(required) The OCID of the work request.

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed on (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm).

`message`

(required) A human-readable description of the issue that occurred.

`is_retryable`

(optional) Determines if the work request error can be reproduced and tried again.

`l_timestamp`

(required) The date and time the error occurred as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for the time object is in milliseconds.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_database_management_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_ERROR_COLLECTION_T Type

The results of a work request error search. This contains WorkRequestError items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request errors.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the work request log.

`work_request_id`

(required) The OCID of the work request.

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written, described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). The precision for the time object is in milliseconds.

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_database_management_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

The results of a work request log search. This contains WorkRequestLog items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) A collection of work request logs.

- [Database Management Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A60F666A-6BF5-4E0A-9017-5983376C7600)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FDABD16A-8BA4-46C1-998A-1835FD149641)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DIMENSION_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-59F30803-44AB-4E97-9122-AD1FFF77ACDD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DIMENSION_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E360E38B-D4BB-4A00-8D37-ED0FB98E201C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DATA_POINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C546B085-B7D3-430E-AA1F-A0154AAB2D24)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ACTIVITY_TIME_SERIES_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A88FDB6D-24DF-4648-8B32-9EFEB2AF8EF4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F1C7F205-2952-42AB-8D33-14102E699DFF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_STORAGE_SIZE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1CF25605-ABC8-446F-8E4B-052B19184128)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADD_DATA_FILES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3D903654-6F39-491A-908B-2AB869390E87)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADD_MANAGED_DATABASE_TO_MANAGED_DATABASE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9DC22F09-C95D-4EBB-AAB3-B9EA0A454ACF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADDM_TASK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1A741219-AEB6-4051-8ED8-E5B22607E5BC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADDM_TASK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1286190E-97F0-404B-BE68-9F760BA32A33)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADDM_TASKS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1BC57962-A4F5-45B5-B76D-F8B6D1D92739)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SCHEMA_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-34DFA67D-0F67-48F4-BF07-B5D8D6C2F344)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SCHEMA_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DFF30D41-4879-45F2-B3C3-659CDF6468FB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FINDING_SCHEMA_OR_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CA6418EC-6D56-4538-9006-87C47E4186EE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_EXAMPLE_LINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-93F35168-72A8-485C-B2F1-A8B14E84F9D2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_EXAMPLE_LINE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A64F84A4-1710-4E42-8A4B-993CD3E460C3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_EXAMPLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C4AB708F-1608-4C43-8D08-521F06B3D5E4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_RATIONALE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-14995770-706E-4247-8F89-C5A639FBBA96)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_RATIONALE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-643732EE-4CE0-41E7-A6BB-1348167CD7BB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C6F17D50-8234-400E-894A-C335C5D1DB41)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FINDING_SCHEMA_OR_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5507EA9D-9618-4032-890E-94FF1EA67FEA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RECOMMENDATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-835E9B08-A626-47AB-A2C7-EC4A7FC3A89F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RULE_FINDING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1147FB43-6BB5-4CD8-B1CC-35F984D1F664)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RULE_FINDING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E3B60316-D8C8-4FB7-9812-3C12C3607E12)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADVISOR_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-17020F86-79A4-47AD-8E9E-4C6F2F027D50)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6EBBE082-F7A7-4697-ABA0-5E4C3CC5A069)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A6C30883-C4BE-43D1-A747-70F9C17D7F56)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9A44377A-8B21-4FF3-BFDA-17CC3020CD1E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COUNT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E7899096-419E-4616-BA01-FBD8955383CF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COUNT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-27C38BB4-BA70-4BF5-95C5-6817C252BC4E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALERT_LOG_COUNTS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9F9011F9-7E81-4901-8CD2-128A125D6E24)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALLOWED_PARAMETER_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6D14D680-DD4C-4647-80B7-D554DB3F5DE7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-65DA5F49-9B84-4A29-AF83-508B376AC880)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_CREDENTAILS_BY_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BE931953-32FC-4AC5-8D91-F450ED6C8C52)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_CREDENTIALS_BY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F3F268F3-BF26-4F31-83F6-E42CFE72EB73)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_CONNECTION_STRING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-27DD949D-32F2-4F5F-8F1D-0898FDD0A0E9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B2E92EDE-C2B5-43BD-87C9-E102E387F6DA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FA5476B4-D8C4-4F72-9593-35DFF4A0BF16)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3E5EC320-7AE2-4612-8F2C-C3A4218F5640)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASM_PROPERTY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C8207036-7F52-4191-A384-AC0D9015D3E4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_COMPONENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D67C3917-359B-47B7-AAF1-6216586C8A52)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-527F0BB9-1285-4BE5-8E5B-EC5DCB4FFFD5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_DATABASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-748B1A45-261D-4B8D-99D6-C3C815DC9488)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_DATABASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8A60C655-1837-43B1-BC3E-43912607FC38)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D3AA1B26-10EB-4B62-B617-EA5ED7F3E2B0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-19162119-C6A0-401E-8C5C-556C32900741)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-34BF6454-1036-47F9-8C61-6D73486DBA5D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D5B8B031-04C0-4677-A38A-693FCE77BBDB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COUNT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9D63976C-5983-4219-9923-8763AE356F18)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COUNT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-909B7FEA-4F4B-4FC3-9CEA-ED45166F5BC7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ATTENTION_LOG_COUNTS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A0159945-9E4A-405F-852A-E25743E793DD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-64ACF1CC-37E3-4452-9E01-EBA87597855E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4FB0166C-04FD-4C7B-BF57-409515AE29BB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-886C9CA0-2B59-40F7-93D7-CFD6929E0CE8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5A5E7C0B-CB20-4BE0-999E-C6A0A622AC8E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_QUERY_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-15B2E75A-2A0B-4F86-903D-58439F667E11)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-327F91CE-8D5F-4F9C-B673-2DABAB6F0B0C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1360B5A4-BB54-449C-A68D-CC360926D1B3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_CPU_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B4157EB1-75A3-4645-9FCF-53F41C848060)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_CPU_USAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-655EFBDE-E337-4D28-8052-398073F2436D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_CPU_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-79A26423-B6B2-482F-AE56-EA9AD475FA23)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_METRIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-00526F99-D5B2-4389-8C78-49817430E63E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_METRIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D75066C2-044E-47A5-9B9E-CC4DB8E7A540)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_METRIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2989083F-42DF-47D5-BB4D-FA4960B78E0F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_CHANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B85BE07E-54A7-4A6D-82B5-D0C3EFC870D9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_CHANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4545381B-239C-4F7B-95E6-6D0C0C07DBA6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_CHANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8E1134E4-17A5-4601-B52D-F9217914ED2C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7598F7AC-0A08-4A73-A0DD-6202E0A37B58)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C97A81D2-E787-405F-94F1-2EEB3F332142)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_PARAMETER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6BC4D36B-0777-4AF2-A860-5999C2BFB763)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AFC3E6D1-9E50-4111-B94D-48B966D2F277)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8A0D19A9-36D2-4431-8341-1517A1B15E66)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B519C408-6623-4F72-9231-A778F2D81FA4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-028068CE-898E-413A-9807-C2587C65DDFB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_RANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EBF0AAAC-1E44-45F8-A390-161BB49D6317)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_RANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9F79A6B6-75B7-4141-975E-DAA504F3A91E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SNAPSHOT_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3494B11E-9CE0-49CB-A539-D835AC93F809)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SQL_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-82205C39-99FA-414E-9DA4-ED6EA49BBEA6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SYSSTAT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-42017C62-E13C-4FEF-B5DB-D7186936EFED)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SYSSTAT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3FC03969-7730-48BD-B1B2-73BC0FE20033)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_SYSSTAT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AC73F56C-244A-42C1-91F6-C0805A20FBB9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_TOP_WAIT_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7423C3D1-EBEC-4D89-8166-4469C984C5F1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_TOP_WAIT_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-62ABCE50-8D4B-4EAA-9B74-97B0A295AC18)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_TOP_WAIT_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D79A949A-9EE3-4C49-9C82-0C32FF932F2D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_BUCKET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-72B523FA-7227-4564-A8A2-E69678FC5450)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_BUCKET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1F3518F3-4F78-4F45-ACD9-C4161539817A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_BUCKET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-52538BBE-7E62-4ADA-93F5-D79DA53E5D46)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C1536D49-B7F1-474B-BFDB-11ABD92F6A17)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F16A77E6-2011-40D9-883E-4C5BF4A4642F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AWR_DB_WAIT_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-93BED6EC-DFE0-4212-8982-708D9746447A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0AD11BA7-D479-48B3-92F7-805A8C3F01E5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_BASIC_PREFERRED_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-69EDFA9A-D43D-4997-AE8A-EB3DA8E286CA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DATABASE_PARAMETER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4747426B-0485-4186-96F6-C33A2EDB3DA9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F044FC54-ADF4-44D7-B9D5-38A2879225D2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DATABASE_PARAMETER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E3469DB6-6CC8-484B-900D-CD16A0EECFE6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DATABASE_PARAMETERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4918A6DD-7B81-4C35-8E6B-F072FAA3448A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_DB_MANAGEMENT_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-35965373-098B-4109-AB08-E40CDF08F0D5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_EXTERNAL_DB_SYSTEM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A6A67A45-22FE-4070-81D1-A51F69148FA6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_EXTERNAL_EXADATA_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F6A8254E-A969-4A3B-A1DC-D076440F8042)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_JOB_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-730ACB50-EB5A-431A-88FB-A7FE8A937CB0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_MANAGED_DATABASE_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1D8C9D01-5F72-422E-8214-5C5E7ED7298F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AC7A61D7-2DB6-46D6-92EC-278EFDEB3776)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_PLAN_RETENTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-77823EDD-D082-45BF-8189-2CF846C595DC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_SPACE_BUDGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-19F85EF3-4A5A-41B3-BBFD-F94620F9940A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHANGE_SQL_PLAN_BASELINES_ATTRIBUTES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A1EDC912-1289-4D78-8C83-F65350C120A6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHILD_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-01F97E6A-4FC3-43CB-B3ED-656D34FC978F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2AABA97F-9D1D-4BEB-AE9D-B564E790B4E9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CLONE_SQL_TUNING_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A414770C-39A2-44AA-A809-ED60AB8ADD2C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DATA_POINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8E080958-B0D0-42ED-9258-4B5811F4746F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DATA_POINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AB1B0060-C1B3-4079-9A37-4210DE2B8A55)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FA088AC0-F9D5-4D2C-B81D-C53FD4B27763)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TIME_SERIES_METRIC_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AC57887D-A2AE-4420-B241-A5B935809FCA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CLUSTER_CACHE_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EFD9C473-9938-48D7-9ADA-65E35CF3C739)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-10252FCB-43CB-48DD-B20B-2394171806B8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONFIGURE_AUTOMATIC_CAPTURE_FILTERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-54C9805A-3732-4D4E-80FC-183CD448BD1A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SPM_EVOLVE_TASK_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CEBA4E00-5409-4610-8411-C83B0D3CB61B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONFIGURE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8C3191DE-9BB2-4A34-B1DC-956D8783516D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONSUMER_GROUP_PRIVILEGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-58761F57-2CD8-4341-8845-91188E1425B2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONSUMER_GROUP_PRIVILEGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9CDCB3B2-AA7D-4710-AE77-25BCA3DE49FF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CONSUMER_GROUP_PRIVILEGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B08A6B71-8083-4B70-9058-9914E66BCE5C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_STATISTICS_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-44A925FC-21E9-4E40-8EC4-3911DC7E6EEF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CPU_UTILIZATION_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-72849568-326E-4CC0-850E-AC5D26FC0504)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_DB_MANAGEMENT_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A68E00C9-F52B-4DB2-A7DE-DE2A2E8A4C90)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DE495BA7-BC07-4BAE-A850-751715610BC4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E2369606-66BC-41C3-B24C-D9526EA30578)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-72FE68E5-6B33-40CC-8F07-FE171E6BA8A3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6FF0169D-D5DE-45E2-B893-D6874E33CE5E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-306047E5-8C48-4041-8AA0-D36C52786BBE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_DB_SYSTEM_MACS_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-85347A26-F111-4CE6-8A4B-E06127B6C23A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AD372F76-3D93-4214-8950-E3C2E534CED0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_REST_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F9D97AC8-0805-4E31-9C1D-1614A9EBC6F9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-400AB3FA-7733-40F2-8656-F5D1C5C0051D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_RESULT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4E5E4090-5660-4B71-9D6D-2AF0987CC8DC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FB19C807-68F2-4592-A400-B0948C22AB62)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F02A76C8-E185-4E02-AB00-0707B15B4A07)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_MANAGED_DATABASE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0633513B-0484-4690-AC3C-3C988E4E9CFF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_IN_BIND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FCA7E7A3-8C5C-4461-B0EA-B13421937668)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_IN_BIND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BA9725D3-DE6D-4182-A9D7-B6A6A866351E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_IN_BINDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F5257644-521F-44DA-AF35-5A14234AA970)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_OUT_BIND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F4341C60-F34D-4C5A-8DF1-07B0CFE5B49B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_OUT_BIND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-733427F6-0D82-4112-B7A8-82929E444AE9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_OUT_BINDS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B9DD13C9-C4FB-4588-B712-FD151A8E0B43)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_SQL_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5C62F765-A183-4618-89E0-C405987EF5F3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-89BA9921-EA5E-476E-9D34-5A16DCD70C71)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_SQL_TUNING_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D6DEA7B5-7C46-400C-BB39-1200BACB7D68)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DD041218-751D-41BF-B2D9-8695B46D39A8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CURSOR_CACHE_STATEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EF602C31-2966-4DA5-B2B8-8F1EEB865225)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CURSOR_CACHE_STATEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EAFFF168-CDA0-4522-8DAB-744B14D263C9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CURSOR_CACHE_STATEMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D49A04B2-670B-4603-8929-EB4231D1C723)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATA_ACCESS_CONTAINER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8802433A-8116-4D42-B4A8-D2C1B0DD9E0B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATA_ACCESS_CONTAINER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7F04CF78-4440-45EA-A2B7-55FD4CC9E99F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATA_ACCESS_CONTAINER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A4B5CDE4-D42F-4C5E-B907-95CB87D96DCF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DAAA27E9-7D6E-4399-A924-3155ED972A8F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_CREDENTAILS_BY_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E7F59F0C-67B5-4539-ADF5-C0477F2A5FE4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_CREDENTIALS_BY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4C36EC26-C664-4B69-99C9-053C7F42D0FB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_CONNECTION_STRING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4E0F1A93-ADCD-4D32-9AC7-D87DFA184E6A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_SUMMARY_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7C62C80F-6309-46A4-B696-65A35369EB5D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_STATUS_BY_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C3E3FE3B-4094-4127-ABB4-729B473AC27B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_SUMMARY_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6812A9DE-A4F7-45F2-A09D-44B0A1FFF753)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_STATUS_BY_CATEGORY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3D5A8B3B-F318-4919-9126-7F74D3069524)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F8DA32F7-7F8C-458F-95C0-BCE40F953AAC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F041184E-DDE7-4E9B-8BB5-89B4B64E2FF3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FLEET_METRIC_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8B6EC141-E2ED-4415-A4DF-43713741C03A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_USAGE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-79AB822B-767A-460D-B662-48C01B3F78B0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_USAGE_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8509C25C-2500-4D2F-9262-C837FDFFC55D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_FLEET_HEALTH_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6933DE47-DE19-4647-A9BB-2433AB462C9A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_TIME_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D4C7AA0D-2E2F-4DDF-9589-2E532523DFF1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_DATA_POINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5EDC22A0-112E-4C8B-B5A6-BA5ACF92FC94)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRIC_STATISTICS_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B68517BB-BD4D-4D87-8F68-7B47DDD05A96)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_IO_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BC706C42-F339-412E-81CD-4CD4037533B4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MEMORY_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E28DC291-5021-40B4-B72F-AA84A28E0501)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_STORAGE_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3D7789DE-8061-458E-8760-39C6987E3AC4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_STATEMENTS_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E04C1B4F-5943-432B-B5E1-97000948D0B1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FAILED_CONNECTIONS_AGGREGATE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9826F4C2-547D-454A-B5BB-5EAAD5EFAB09)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ACTIVITY_TIME_SERIES_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5E09A77E-3F63-4071-A881-9A6EB6F44AC9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_HOME_METRIC_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4F0713B9-0C5F-495D-B19E-A2820A6C3865)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_INSTANCE_HOME_METRICS_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9DA79819-3FC2-4168-8C29-EF902410E920)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_INSTANCE_HOME_METRICS_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2BEA0033-A849-4A29-AC0F-3CC40D5682FB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_HOME_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A9E9525C-0CA3-42A7-9987-71108310BD68)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_MANAGEMENT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-537F2097-6CCC-4E56-A824-44D70D522795)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ALLOWED_PARAMETER_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-142430EC-2C10-496E-A61E-E036776C5A16)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1FC0DF9B-027A-4A89-AF19-0985A28CBB17)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETER_UPDATE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3987B176-E62C-4976-A8DE-6D4FEBE54FD4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-844127F2-C684-4046-9BD6-BB5DE3D28E2C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PARAMETERS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E27B0C4C-10AE-4B0B-BAE0-97FD447C1163)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PLAN_DIRECTIVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-075F5246-A688-44FB-AB4E-D955A9A80E40)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PLAN_DIRECTIVE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7AAFC557-9E16-499F-8DFD-79B12561994A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_PLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CFC871A0-DB1B-498A-830E-4B4E178A127A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATABASE_SSL_CONNECTION_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D0903647-7099-4571-9158-6FB3716D704C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATAFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2C61A640-F094-4CFF-BB77-E49C2C606B5A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_ANALYTICS_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-ED5DEC0E-1BF4-4163-921C-E7E9934CD0B9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F1227746-34F9-4DB7-B0FC-CB76EB8620CD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7ABFD9E3-D865-4C57-BEEF-93CFF0AEE614)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-99FD7004-F112-4FBC-9CDE-6E1DFE07748F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_PRIVATE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1DE611E9-C268-4C8B-93F6-3225236A0033)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DBM_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-732A07F9-AA96-4294-AE64-8FA35F3AD92E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4A459E4D-F5EA-4FFC-B458-37E33D72A9B8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E5FB7C38-70C2-49A9-9D39-5F75C9F47B57)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-00A30ABA-3810-443C-BE05-E4451993BBA1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISABLE_SQL_PLAN_BASELINES_USAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-162FC3D0-6145-4885-8C30-E2AD9DC7887F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVER_EXTERNAL_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E362A9FA-869E-4C15-B7A2-73293F989B60)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ASSOCIATED_COMPONENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7F6ADE4E-A70A-4A7D-A4C0-C19DF00712E1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_SYSTEM_COMPONENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-11AE69A4-3E5C-4F7D-BC8C-10DBDB7031E3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_ASM_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-29EFF635-95EE-4A48-88FB-83BB02BBECD0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D0934371-BA2D-4067-AB31-A69A48E470EF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_ASM_INSTANCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6DF102DD-311C-47C5-8002-591CF8492258)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_ASM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A0EE4261-B3FF-480F-9A13-FD147402FCFB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_NETWORK_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E40B57C8-E025-4F97-B373-031437986DD4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_VIP_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E9F04FE7-F303-4E63-96F2-6CF02A1AD535)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SCAN_LISTENER_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7466F917-0D78-4CC9-8E19-9B1CABF3AA2F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_CLUSTER_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4C37CC85-07AA-4C9D-A702-5F445DD56E36)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_NETWORK_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-ED563B10-9F6C-433B-9E6C-CC2CA89FAD04)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_VIP_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-551C6C86-6622-42C3-80B3-E3C84B5520BE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SCAN_LISTENER_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EE86332F-454C-43C6-8D0B-2D9D58E6A2AB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_CLUSTER_INSTANCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4D92E3A7-80AD-489E-BAA6-554D4D00363C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BA1DDCFC-DF5C-4176-A916-53C4FC528491)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_PLUGGABLE_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A0DBFC61-FDE4-4967-99EF-4074757F1F5C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_PLUGGABLE_DATABASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5B5FB035-EF39-4B6D-9037-32811022BE34)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BF72ABC8-10EB-4513-8B5A-1604C1B7C0F0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_HOME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9DD41130-796D-403F-9CC9-A9BB3F6C5A3D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CC3A2BB7-AB63-4017-82F7-36F3980DCE08)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3689B4D5-F8E6-4889-AA98-9083088D367C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_ENDPOINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2760529E-DA11-44C5-99A8-EA09808F37E2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_LISTENER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0DDB5E35-9726-4D16-BFF7-FB677BD3F023)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQL_PLAN_BASELINES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EE3C8178-F85D-42BA-9A75-ACDDA8E87FB5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQL_TUNING_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BF7AECF7-2BD2-481B-8F1C-A19DA5105ECC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQL_TUNING_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-49DA80DB-E94C-426A-ADE4-CA47628BD77F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_SQLS_IN_SQL_TUNING_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9FD1619B-BE35-4F90-95D8-7FCA0DA49935)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DROP_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-90F6FC30-5EF9-4F51-826D-38D7324F4338)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AF0CC813-104C-4ED7-8245-F6DB5C664E0C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AAEBE050-E34A-4C4D-97EE-C7472140CF30)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A731BA1E-50D9-4FCA-845D-933BB88AE8A0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_EXTERNAL_DB_SYSTEM_STACK_MONITORING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CEFAABF1-73E8-43F6-A7C3-6061DBB3678F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_EXTERNAL_EXADATA_INFRASTRUCTURE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DED4BA85-9F4D-45BE-8C35-A67334D06C9B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-99F05494-1541-4315-962B-B2B70F9FA663)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENABLE_SQL_PLAN_BASELINES_USAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C5D22C37-F7B3-4E17-852C-6B4C7A62EEE7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ENTITY_DISCOVERED_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B617DB70-A1EC-4B91-9A09-93B56533F8D5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-44AA86ED-EFE7-4A22-88C5-0F0FEC4A8265)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_PLAN_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F8AD2A4F-9B84-4A52-A8D2-771C1729A5D9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXECUTION_PLAN_STATS_COMPARISION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-834B8A30-1BC1-4F4F-B4DF-BE51EC8B2605)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SERVICED_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-448B22AD-E033-495D-BAE4-FCCFE57B1A86)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SERVICED_DATABASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0B1A7E6E-9FBC-4E06-B4E1-78DE0126C29A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6874D62A-1003-4D6E-BB9E-56D46E8761AE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B02FD842-D8A6-4BF0-BBC5-6ACC1644AC8A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C0B4B38A-7F39-4414-A533-3D6ED8ACB696)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6E96E480-92C5-479A-A6E1-A5BB3D7678E5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D0FEF6FA-8490-448F-A5E1-1A6C2105D2D9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_PARAMETERS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2BDFA645-44C5-490D-907D-AEE344ED2072)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FC1D64A0-6A6C-4F54-BD1D-D651E0A7B102)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_CONNECTION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3F9BDD23-B97D-4B53-8553-095238F1ACAE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_DISK_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CE2FF17B-A3CE-44BB-B67B-193CDA63EE7F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_DISK_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-74311B1F-1F0F-48C6-892A-19D27A9B7F6F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_DISK_GROUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0D1E402F-444B-47A9-8F41-7FE2C6BB0FB6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B7EB69FC-91A7-425B-AFDC-AE542F5B898A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E9C6EDD8-4E35-461D-8057-473C8AB10BBB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FBA2D94E-32A3-4DE8-9411-2BAF1C1C3390)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0D35C7CF-276A-4244-8204-782B4208A295)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DA4E812E-F638-4696-BE23-DD466C21A3D8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7C0C052A-1C34-450C-8A79-1FFE2FB78061)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_ASM_USER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C6D51381-A646-4AC7-8A4E-624894756DB9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E2848A20-F929-413B-856E-9135F07F5C80)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B29911EC-E7CF-4C53-BF75-B5DDBCC0D907)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-15E27680-8E73-4D4E-8EAB-0866F9547A7B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-430B01B8-D960-45E8-951C-53D55B4D6920)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-53D2E32D-C824-4203-A48C-B17E3932264D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D9FEDCFF-515B-454B-86F5-4B160B7B7C51)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7BDAF825-3629-458B-87DD-F98FB4E8D930)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_CLUSTER_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A810F513-07BE-4751-B376-4A4FA5AC50F2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRA_BASIC_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CF621F11-A795-403B-AE5D-70356DD82595)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_BASIC_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BD42D85C-2F57-46A3-8A60-83A49E0C68EB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9C117EE9-1137-4F3A-BDCD-3C985B3C1B61)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_INSTANCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FC098E6C-30F7-4BB6-984D-03E8A82C40CD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8070C758-3A56-44B2-8F6A-B839A46DCFBB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-76C30DEE-47F1-44C0-AA21-6D4C0874001E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E6494184-57CD-4F9F-B90B-DA2D5BE04977)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_CONNECTION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-49A9A046-C6E0-44FD-8939-26E5679088FF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SYSTEM_DISCOVERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B88D4716-EBC9-40D3-B6AA-CE31428834F5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7B87F484-7DFA-4698-9EC1-DEF0FFF1E788)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F87C9F4F-1249-4403-83F5-6DCF991D7DB9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7A4A6E67-B392-45E4-964A-9E7B828E64DF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_HOME_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3C2E23FB-0FA6-42A1-929F-96106DBEEFA8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3FEC545B-6B10-4D1C-A74F-6323CB5775A9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A795CAE7-2177-47D3-B4D8-8D5944274EAD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-563A7D5A-B18C-43AE-872A-E8A37A300ABD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_NODE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B2F5862B-E8F7-4A33-8925-63AD2D584A18)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_STACK_MONITORING_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9CE75A57-0A7D-4491-A56E-B52DCDCF4DF0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-26EC6DF9-88C7-436F-80BF-676AC99F5035)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BF58EE79-9481-4DCD-A105-7D74E91F3CB2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2CF29C69-5AEE-4AFE-8AA6-CEE5D2A118A1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-86CF86FD-2E2F-41EA-81B1-22E00B2CB029)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8B67913E-B80F-457B-886A-694019683117)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F4CC0417-AFD3-437C-A29A-D3CB4B5D850E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EBC5BC11-8113-451D-8F2C-8A695FB042B0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_CONNECTOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A90FCBE0-D8F1-4BC7-92CE-5A93EA9D1331)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DISCOVERED_EXTERNAL_DB_SYSTEM_COMPONENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DED84293-1160-4E0B-935F-112C1975650F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F83B6CDD-CED6-456F-A113-80F33AC815CB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CCECA9E0-F395-4075-A93B-C5C60539DB29)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-ADC6234B-564B-46D2-9028-C9A015A2DB12)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D21E920B-9526-42B6-AF9F-B73433CDE182)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_DISCOVERY_MACS_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-00477AD8-308C-4918-832E-4074808C54D8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DB_SYSTEM_MACS_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6CF6543D-D080-4B41-A9E2-4EA60057E10D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_DATABASE_SYSTEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A37F7C19-52F1-431E-AC98-3CB05877747F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_GRID_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-18EC1BBE-2038-4E00-BEDE-B292548E5645)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_DATABASE_SYSTEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-32CE49B2-1917-438F-A7FC-F5A51922F26A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CF56662D-7092-4501-BDBC-1FC5C84B7DF8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9616F98E-CC49-4828-B102-FF5638B7A2BD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E869B63B-9D09-47B2-817A-568F3A1E8110)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CC9D3E27-87FE-4C45-B291-CF59E28C220B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_STORAGE_GRID_DISCOVERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-43F3541F-2E0B-4E0C-B04E-78D3C6DA11AD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_STORAGE_SERVER_DISCOVERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8B87E545-85D8-4042-98EA-CC8A0EBEC25C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_DATABASE_SYSTEM_DISCOVERY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0DC95A28-3CDA-4760-AF1D-12594C51D01C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_STORAGE_SERVER_DISCOVERY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C7844092-79E9-4616-9D54-BD721E99B72D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FCA734BD-7EA4-4DB2-941D-2567CFE14B56)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_INFRASTRUCTURE_DISCOVERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-43886A58-07A6-4D53-AE00-25CDFA1F8C8F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2218F49D-B434-4428-851F-458819D50F29)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AEE6745C-31E2-4960-B055-1E9D20588698)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C5689DD9-DC72-4CD7-89F7-805D3A8C387F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4F0DC454-6598-457C-8DEC-2AA16D19729D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_CONNECTOR_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F0826427-6A22-4161-903C-1472940A027D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C1A2D6A5-01C1-475D-9319-C9E3316AAB3D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DBFAC768-2B95-452F-AE44-EF3E6DB1C5E3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_GRID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-94837206-9BE7-4679-8F6D-170DE2FF22AA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-191D57C6-1C99-40D9-BCE5-D5CE2D36BC1C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_EXADATA_STORAGE_SERVER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5B2D72C0-9771-4680-A871-9CBF73E4DCA1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICED_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5638D11F-E8C8-45BE-A537-3B6F771A7532)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_SERVICED_ASM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BDCEF398-4594-4152-8EEE-8FEDF6045A0F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICED_DATABASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1DF2A416-58B5-4D2B-B725-E09B301CBF4C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_SERVICED_ASM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1CC78ADB-184A-4392-B37E-8C14530A613D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-71E1487A-B270-4F7E-AAB0-360D1E3E0CF8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BDD56AD4-BFD7-46B3-B0C3-3B446E44336F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D1B36A7D-6214-4D53-9B9E-CB65C0F3E8EB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B1D640BF-7459-4158-805A-F801E63F8F9C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_IPC_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9C74CCFE-CB86-4307-9950-9907B80F5C11)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-51F59C14-9550-4DFE-972F-0A913ABED323)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-96813BD1-C7B3-4493-957C-B7D3B55C1A6C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_SERVICE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-28F0189F-E4D6-4C9F-9494-E80D22F8FADE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_TCP_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-95D4121C-9C73-4803-A880-6580EA18829E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_LISTENER_TCPS_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C0AC5A52-D1E2-4A75-AB44-E32B84D8E12F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_EXTERNAL_SERVICED_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-634D36A8-2338-4766-AEA8-0B286FE056A7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_FETCH_SQL_TUNING_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-362B4CF6-1462-4DDE-8148-FB8315657179)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_HISTORIC_ADDM_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CF90B354-A889-44DC-BD10-DD9339027E61)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_IMPLEMENT_OPTIMIZER_STATISTICS_ADVISOR_RECOMMENDATIONS_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0E17A1FD-8CF2-4EAD-B185-61D215E31193)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_IMPLEMENT_OPTIMIZER_STATISTICS_ADVISOR_RECOMMENDATIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-06CAE00E-71B6-4CFB-94D4-E809286E437B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F51F3EA7-5C40-4FE4-AFBC-357C47258655)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_IORM_PLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A97F6F80-9A7B-447A-AC15-BD91D71665F3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AF59491D-753E-49AB-8514-287B4E83934E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_DATABASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3451FB00-0147-4AF8-B5B8-2119007C39BF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C0181054-94DD-45F8-9CD6-DBAAF944F68E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6DA2CF49-0B0C-4A7F-996F-455622C969BC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F558E1E6-5C55-488D-971D-029242E52543)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-09A0EE4F-193F-4786-A937-7EF50F73E5BC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_RESULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5A631FF7-1A06-4FAF-90BD-D0D0EA4AED35)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-91D9D0BF-1560-4277-84F6-58F6880827C2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B9A0930B-9D70-409D-A01A-C4DB45CB5054)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AC5AB6A3-68A0-412F-B940-D3EE8E4AAD5C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F696275F-5EC1-4CCA-BFCB-08B8AD16099D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTIONS_STATUS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0830CFC9-8530-44A8-BDCF-B940EE298D71)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTIONS_STATUS_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-76F70C1A-A330-4C06-82A1-9F08BAB80F97)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_EXECUTIONS_STATUS_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E9D4E8DD-744E-46AF-BD77-14BE3781AAC6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-96029DE9-1E82-4FC7-9879-C6062BCEBF63)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F65DAE81-C33E-4342-A0CA-E8F8EE954883)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-63078C54-EFF9-4C19-B6D2-62DD28AA3832)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_JOB_RUN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8485832F-CA3C-4E30-AF6E-E2FB0B8E54EA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_LOAD_SQL_PLAN_BASELINES_FROM_AWR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F54C8428-3E1D-4A53-B567-4D1C3C0A0ABB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_LOAD_SQL_PLAN_BASELINES_FROM_CURSOR_CACHE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-845E13E9-4D29-463F-8003-084E91A038B9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_LOAD_SQL_TUNING_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F8BF7086-3086-40E5-9334-CF46215E45D7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PARENT_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E243803B-7459-47C1-A8EF-B2A4AB8E2B5F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PDB_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D1566240-71B6-4F83-9E31-D5EFB25567AB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PARENT_GROUP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C1A39BBC-994D-40E9-B18D-1389CBF27787)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_INSTANCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E2B4EEBA-6597-49E3-92ED-024FF46D721C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PDB_STATUS_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A915D478-1FC7-4BE5-84FF-2555B5AF9002)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-735C94A6-BB18-48E5-BA50-0E26DC98458C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DDC03EE7-47F7-4462-B370-D73D347DCCED)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FEB9AB43-1A8F-4209-8985-77277728BFD3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-30B477DB-A43E-4EE9-92D7-C634486311E2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_CHILD_DATABASE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E3B43F0A-FF37-4699-80D1-B1D48D9EFCE6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-09613014-88BE-4A02-A82B-A14A0693E4D8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6AC0DD50-0E6B-4F64-91B0-AC589A01502E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1C07285F-BB54-4CC4-93BB-263855732524)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_GROUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F5CA7F2C-7A02-4400-8F00-D1A21CDA4F3A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_PASSWORD_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CC180AA3-190A-4FDD-A4DE-0E531C467E93)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_DATABASE_SECRET_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E3714494-32E5-47A6-9AB2-022A968A5DC0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1164DB4C-A8A3-43FF-B823-42E2213EF3F6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-54CC59CB-AE2D-45DB-B254-0186070BAB61)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F4560FE6-6978-4A43-8222-B65CB594A2A6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MANAGED_MY_SQL_DATABASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-27081292-3BE9-42FB-8852-407EF1C6A26A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DB_MANAGEMENT_ANALYTICS_METRIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9EB480ED-E72F-4E09-924B-F0517362E118)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRICS_AGGREGATION_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D7305246-EAE9-412F-924A-E921535D6CDF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRICS_AGGREGATION_RANGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B312E24A-385C-440F-8803-D2869E7BF026)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_METRICS_AGGREGATION_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5D164020-7423-4C98-8469-78E644F113F4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MODIFY_SNAPSHOT_SETTINGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2FFEC421-C8B2-474A-82F1-2DB63F2C1871)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_CONFIGURATION_DATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9411831E-F1B0-461C-8A19-10769A127747)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_CONFIGURATION_DATA_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-37BE4653-907A-4975-9889-3689F67E7F0A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_CONFIGURATION_DATA_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C2A63F86-5AAD-4A83-986C-F4FF6908EFCD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7224900D-C99B-4188-A385-9EF0333B001B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATA_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A1788700-B22F-4835-87CF-23AF7AE1C26E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATA_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1F1E7896-09A7-4EE5-A85C-FE72428499AD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9DB2A99E-DF99-4BB3-A31A-507D12576548)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AA76D7E7-6A61-4DCF-BFA9-927670AE16C3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATABASE_USAGE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7AC5EE12-A9C1-47D8-AEA1-C462117C0636)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_BY_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AFAEAB1C-13DD-4314-9524-DB5FB11B377F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_SUMMARY_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7E24F64B-9C69-480F-B5D4-45FFCFEC667E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRIC_SUMMARY_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1F8EF818-173A-416F-908B-804E9EB5462A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_BY_CATEGORY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-464DB8CE-7692-499B-8D9F-3BE12D90E8EA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B756EF8C-AA78-4CD2-98ED-557B31372CB9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_DATABASE_USAGE_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A13B3F43-68E9-4E6A-8BCA-492C1D036260)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3D6612FA-F39F-4D0C-90D8-3FAFE4E10549)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_MY_SQL_FLEET_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-368AD811-701E-41D1-8E6B-6461F4C87AAC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_PRIVILEGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-41D928AA-FBDD-4D06-B4BE-04F9274D9E91)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_PRIVILEGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6071F1AF-5F90-43A9-9364-ADAC20FBEE32)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_PRIVILEGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9A866371-38AB-49F6-8901-C535EB523DEF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_STORAGE_JOB_EXECUTION_RESULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A2143DA8-D543-43D4-B1D0-146306FB9351)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OBJECT_STORAGE_JOB_EXECUTION_RESULT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3829407E-4118-4BA1-A25B-0378B5F2604A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPEN_ALERT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4FBAA415-C6A2-45BC-B415-C397DC8D54C1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPEN_ALERT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-47561668-5C16-4722-AE15-51120FF2A0FF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPEN_ALERT_HISTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-66F7563E-FE4B-4337-BD88-DB7223931A45)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8F81AFEF-AEBA-46FB-88C6-B2A4D4837067)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ADVISOR_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4D44FEAB-DB6F-4865-B472-FE59AF198CD8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A796B287-7D15-43FD-9081-9D056CE70726)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FC7C9B8A-3F7F-4DB6-AA66-122A14138882)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SCRIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4EF5ACFD-B52F-4B35-8F24-E888E340BB52)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5F8A06EA-F95D-4FAE-B1BD-4B3E05F0B8F1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5C20EFB4-35BC-4311-B0F3-948842747ED7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_ADVISOR_EXECUTIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AE5DA99B-BA2A-4FA9-AFC6-A2B2FF8484FD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4B292FE1-3EF8-4FE9-86B6-1D36F7E19DE4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E5D8FDCE-3885-421D-80F6-8E77F4545AC5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-99B55F03-BAF7-4048-9103-818D229DC9D3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_OPERATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-43DBB16B-55B2-4B9D-908C-4515BA57D460)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_OPERATION_TASK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6785D942-D08F-4128-B111-0A69040CC52D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2503BA4F-B514-470D-8B82-DCE593FFB7F2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DC58B3F8-0111-4AE0-BE47-4DE0EE2B0ED8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4E0A2E07-F6F7-4481-977C-67B73DBCEE6F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_OPTIMIZER_STATISTICS_COLLECTION_OPERATIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-FE4455A5-6731-476C-89DE-C2049480ED82)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-964518CC-A8D6-4E06-AB20-89D5771437BB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_INSTRUCTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-505A6F65-1577-4F0F-A1B9-C9262B638DBD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_EXTERNAL_DB_SYSTEM_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4B391602-2FB5-4D87-B0D2-14D974B68551)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PATCH_MERGE_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9BF46B75-6D8E-4FFE-9B34-73861D9321EF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PDB_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0CEA3EA2-B7F8-4EF4-9280-A37CF75524AF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A25F3E49-FE98-47D0-B75E-96EFC436D858)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-30E7F3B8-9DE2-461D-A9B7-B49BCE881C80)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PREFERRED_CREDENTIAL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DFC30C06-964A-4EE2-9F8D-81A8CCA214D6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXIED_FOR_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3024C79F-A98E-4CB2-A1D2-CBFB16DA93BD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXIED_FOR_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CEECCC5C-1047-4DED-9D45-76ACCE114D89)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXIED_FOR_USER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-05A662EB-0B1A-4150-ACB5-F3CB0216D3B2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXY_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C03E730E-3E08-4C91-94CD-2F6FC8D2901E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXY_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DABB31F2-C99C-4E39-83A1-D778FC4253AA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_PROXY_USER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5263EEC9-5572-492E-9315-C3EAFFE977A4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_REMOVE_DATA_FILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E036712E-D18A-4971-99D1-57A2AF5FBC16)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_REMOVE_MANAGED_DATABASE_FROM_MANAGED_DATABASE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E3D2E76F-BE75-4FC1-A1F9-0C6FA049D69C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RESET_DATABASE_PARAMETERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0D3E0665-EE46-455B-A5C2-51DB7F50F3F2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RESIZE_DATA_FILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F801EEDC-D762-4E2D-8C3D-60B774BC915A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ROLE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D9C549A4-9B3C-4584-8A0E-D01C70A3C1A7)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ROLE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-42E60E7B-6427-4C3F-91AE-F93952999F69)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_ROLE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-73A268F3-A016-4E42-B369-A2776B50C9B9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_RUN_HISTORIC_ADDM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3FB666C0-E748-49D6-811D-FB4C5BFA0A45)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SAVE_SQL_TUNING_SET_AS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E996673E-2211-473B-85B9-779167D07645)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SNAPSHOT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EE9B5AE0-FEC2-4CA8-8B3F-5A2A3BC7D63E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_CPU_ACTIVITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7E258E28-2014-4A72-9932-49FF517B89CD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5D0E54BA-B022-4D4E-9C90-181B0EB53E2D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8820583F-0EEC-4911-8F86-B354D306DD13)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_IN_SQL_TUNING_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-35890EBC-7A55-4BD3-AE5E-D5B6BBC2281A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-92BA4C97-32D9-450B-881D-2E666245D4A2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C089E599-B401-485C-92B5-7026960A03BE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_DIMENSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EA5B80B1-C19E-495A-9E15-DE080A32F23B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7CB5A4C7-D479-46B7-8D01-8E5960FD72EF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A025B613-E243-42A2-B7B3-AE37614A0AF6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-69DC8EF8-D5D9-44B1-B5BA-F505D640D2FF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-818776BF-D6A9-4374-BB16-985E5F9B3F08)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-63B203C0-CA89-45F4-B3EA-CA8EFB6E1D33)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A9E5EEAE-C1E6-4FDF-8EE6-BBD06CB73D56)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_AUTOMATIC_CAPTURE_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7272EE18-9A6B-4E10-8F2F-0852D15959F4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B3ED30B9-83D3-4350-BA50-325AB96D9F40)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-64EF5351-79BF-465C-86C0-DE7D5426A7C1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1874EB7C-B575-45E3-8721-027BD6B764C3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F70A5757-8BC8-4F3B-ACAE-94AD905E529A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_PLAN_BASELINE_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BCA9E761-E94E-488E-AF13-41214B674E7F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8E7DA757-FC32-48BE-BF94-917A92F206F1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-28244F45-25C2-4FA5-B657-B05BF33F535F)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-635D41DE-25B3-4035-9773-9E1AA82DB6DE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_FINDING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C9454320-493A-4F8C-ACD9-8D6D0318848E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_FINDING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-498E05F5-C749-4DD2-B177-3919202197BF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_FINDING_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7079AC42-D65A-4CEE-B930-26B797F2A8BB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_RECOMMENDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1083CDBF-9CFC-4E06-B06E-5D0658C536D9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_RECOMMENDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5E07F542-78CA-4607-8C4E-649678F212F1)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_RECOMMENDATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C4FA72FD-4AFB-41FA-BB40-A2EC769C25E6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_EXECUTION_PLAN_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D64A3D84-69B4-47FB-9E65-4E1047A0D784)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_EXECUTION_PLAN_STEP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F82CAD41-FCE6-4C80-ACA8-DB963252BEBD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SQL_EXECUTION_PLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9A27F130-181C-449C-B142-D921B3DBA184)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_FINDING_BENEFITS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-14690558-91E3-4CA8-9259-DD582496AA85)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_FINDING_COUNTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0BE8D745-782A-456E-8BDD-447B3441544E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_TASK_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A947AA6C-D1AC-4B16-A009-5A324115430E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_STATEMENT_COUNTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-04D0A5D9-F1B6-4EB0-A7E2-9ABDCE2886D2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-61B6F65D-2711-4599-A64D-1592A6E63ABF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_OBJECT_STAT_FINDING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-293105DB-E089-4CC0-B80A-4BDA8C9AF804)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_INDEX_FINDING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-75A25F50-1B5A-473D-A364-7731F6D0A903)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_OBJECT_STAT_FINDING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-4DD79F7E-3D43-4487-B5C8-D6CF7FA069FB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_INDEX_FINDING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E966C71C-8E64-4110-AF12-B59E132C30E8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_ADVISOR_TASK_SUMMARY_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-442EE76D-0C34-40B7-A631-39481383ECC9)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_IN_SQL_TUNING_SET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-31716075-D274-43DD-9D2A-C611A47DDCA6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A3F3E024-01DF-4DE7-918A-3A1808D7E173)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_ACTION_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-05A21E9A-7586-4AE9-98C1-C5D3FECD3B3B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_PASSWORD_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E266195F-4C43-49E2-80AC-9FB68D7C2CF8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_ADMIN_SECRET_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5D0DAEEA-6DA9-4D93-BB38-E7985CFA61A4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3528666A-C96F-4B25-AD43-26E4E6A84728)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8E8B7384-E011-4FE6-8E1C-DDC41FB26710)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8ED6244C-C379-431C-844A-3D2D3D5EEB92)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_SET_INPUT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1B4E9A7D-4D8E-4E8A-A8E5-7FC4962E51C6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_PASSWORD_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-291E1554-9A43-4E79-B319-50B2F944F92E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_RETURN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-75E3D24B-BEFC-42D9-8E30-67A2ADEA2D75)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SECRET_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DB01FB88-9153-48CA-A7D7-B2559CD54684)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-BB5317D6-D077-4B12-A208-3C5F68CA1423)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_TUNING_TASK_SQL_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-97CB198B-3D8E-417F-B8C0-2A34C3953DBC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_START_SQL_TUNING_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B1554CCC-8491-436C-AFCA-B557B69D88B4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SYSTEM_PRIVILEGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8A9AEA82-D26D-4F9C-9A0E-EB15C7448FBE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SYSTEM_PRIVILEGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-106F9EEF-1544-4637-85AD-A908A659FA9C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SYSTEM_PRIVILEGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6AA5FABB-A276-41D3-90BF-E95661790D10)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLE_STATISTIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DCF14C51-8B8A-4629-A356-F09450F8DF67)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLE_STATISTIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-EE92088E-4D77-4ED2-A8E4-B716833758B5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLE_STATISTICS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-AF169165-05E6-4634-80A1-6DC76680FD06)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_DATAFILE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3520A0DA-DD14-42D7-A40A-3C5EC53DAE98)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-69C6FE73-4E07-47CC-BC88-473DC98F18CD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_PASSWORD_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-20EF4582-8D33-49A3-9C9F-6DE74D61A65B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_SECRET_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-43BE7C81-3C88-4939-A7E2-B96585E9B1EB)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_ADMIN_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6176BED0-393E-4B27-A880-B28D7A17688B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7C06435E-654A-4DB0-9B7A-8F73A3F4D1AE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-873E234E-0217-41E2-B269-57721AAC4EA2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TABLESPACE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-34B14ABF-C432-4882-9042-F67241B45C28)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TEST_PREFERRED_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E8500C8B-FC16-452A-897B-EAC82822D38D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TEST_BASIC_PREFERRED_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5C366167-C303-4FEF-92FD-E278C146CAA3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TEST_PREFERRED_CREDENTIAL_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0B7180AB-188F-4B61-95FD-5FEB782F1CAE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_SQL_CPU_ACTIVITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C0D6E8D0-B197-4549-ADC7-3E1693A8BAB4)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_TOP_SQL_CPU_ACTIVITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-5AAB4348-C7E9-406B-8522-714C66D01BFD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_PREFERRED_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-6B0DE808-E658-4EF2-BDAF-EAA2C94C0999)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_BASIC_PREFERRED_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-F156C006-0C59-42E4-8555-9B42A937010E)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_DATABASE_PARAMETERS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3B9D2B92-AB52-45B5-A785-B01888072578)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_DB_MANAGEMENT_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7626007D-7DEA-4F3B-B278-9C45476035ED)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_ASM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0C28762D-EDE7-43EF-9B6B-D8996C2AA215)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D6423470-5C00-483C-B50D-D6B0C16DA0E6)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_CLUSTER_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-09A59706-1FEE-47DA-89DF-02997956C946)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-806E2C85-BD02-4AE7-97B7-579A4831B0CE)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9D2552B9-DC13-4F59-A95F-687869A0867C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1CB5ED65-42EB-4AEC-80DB-1B34BA7BF266)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-05510834-BA8D-419E-98E1-44B051E02ED5)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_DB_SYSTEM_MACS_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8F586E81-E899-4F59-AC41-FA32AFDBE268)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-C0CDB8C8-FBA3-4871-8074-12902FD75A47)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DF15014C-4765-4F45-951A-27A744331118)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_EXTERNAL_LISTENER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-CFAA8538-A6DE-4F4F-8613-E32F58C9D2F2)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-E46E4B42-40CF-445A-B2B5-27DFA9990423)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_MANAGED_DATABASE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B6F67F68-CC4E-4DA6-8E2D-972FA50E6F73)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_SQL_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-114CB601-0F1B-461A-AEE6-A7B638EE2712)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_UPDATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-81E8F36F-2FCD-40B5-8543-3900BD1B0BEC)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-D59E58B4-35D3-426F-98B6-1ED433BDB5A0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-7EF64E6C-1A5E-4861-8FC9-E4E6FE9C73E0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9B7FD933-2921-4E76-A022-976AD577408A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_USER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-A7EBB545-5838-47D6-BF9B-55C53E8A447D)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_VALIDATE_BASIC_FILTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-9E85FF3C-3511-40B5-9286-E90C25B30206)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUB_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-67DF49B5-11A5-444A-A9E1-8DCEE34B2991)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUB_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-2AC2915A-33FD-43B7-939B-7A7F2C98C17B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-8C43527F-665E-450D-9772-7C8CA89E85D0)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-3ED99CAE-8E6D-41FC-A55A-A7552E725861)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-B2049426-3FB1-4DCA-B7AA-B8CE638982F8)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DFA733B8-12C0-48E1-A23E-57396D3BB5AF)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-49641C74-75DA-4C1A-B43E-2DD6D69B311A)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-DD341DA2-E8DD-4F9C-A027-BEE705BEA1A3)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-01ED538C-4E04-489B-B1D9-3F89AA616A96)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-524D0C69-22D7-4EF8-B25E-36CFD60C430B)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-74F88BAC-6140-4E42-BBE2-A1EC6B1DCD2C)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-1D45A12A-1647-4F56-8791-798FB35928AA)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-0E881715-3644-41FE-9CC0-D3B1733D15BD)
- [DBMS_CLOUD_OCI_DATABASE_MANAGEMENT_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_management_t.html#ADSDK-GUID-644AFC16-D4AD-400E-AC84-B49BD23CCEEE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
