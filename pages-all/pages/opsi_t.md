# OPSI Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#dcoc-content-body)

## OPSI Common Types

### DBMS_CLOUD_OCI_OPSI_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_EXADATA_MEMBER_ENTITY_DETAILS_T Type

Compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Enterprise Manager member entity (e.g. databases and hosts) associated with an Exadata system.

Syntax
```

```

Fields

Field Description

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_OPSI_ADD_EXADATA_INSIGHT_MEMBERS_DETAILS_T Type

The information about the members of Exadata system to be added.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the Exadata system.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

### DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_EXADATA_MEMBER_ENTITY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_create_em_managed_external_exadata_member_entity_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADD_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_MEMBERS_DETAILS_T Type

The information about the members of Exadata system to be added. If memberEntityDetails is not specified, the the Enterprise Manager entity (e.g. databases and hosts) associated with an Exadata system will be placed in the same compartment as the Exadata system.

Syntax
```

```

`dbms_cloud_oci_opsi_add_em_managed_external_exadata_insight_members_details_t`is a subtype of the`dbms_cloud_oci_opsi_add_exadata_insight_members_details_t`type.

Fields

Field Description

`member_entity_details`

(optional)

### DBMS_CLOUD_OCI_OPSI_CREDENTIAL_DETAILS_T Type

User credential details to connect to the database. This is supplied via the External Database Service.

Syntax
```

```

Fields

Field Description

`credential_source_name`

(required) Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.

`credential_type`

(required) Credential type.

Allowed values are: 'CREDENTIALS_BY_SOURCE', 'CREDENTIALS_BY_VAULT'

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_HOST_DETAILS_T Type

Input Host Details used for connection requests for private endpoint accessed db resource.

Syntax
```

```

Fields

Field Description

`host_ip`

(optional) Host IP used for connection requests for Cloud DB resource.

`port`

(optional) Listener port number used for connection requests for rivate endpoint accessed db resource.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_HOST_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_pe_comanaged_database_host_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_CONNECTION_DETAILS_T Type

Connection details of the private endpoints.

Syntax
```

```

Fields

Field Description

`hosts`

(required) List of hosts and port for private endpoint accessed database resource.

`protocol`

(optional) Protocol used for connection requests for private endpoint accssed database resource.

Allowed values are: 'TCP', 'TCPS'

`service_name`

(optional) Database service name used for connection requests.

### DBMS_CLOUD_OCI_OPSI_CREATE_DATABASE_INSIGHT_DETAILS_T Type

The information about database to be analyzed.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the database entity.

Allowed values are: 'EM_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE'

`compartment_id`

(required) Compartment Identifier of database

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type

The information about database to be analyzed. Either an opsiPrivateEndpointId or dbmPrivateEndpointId must be specified. If the dbmPrivateEndpointId is specified, a new Operations Insights private endpoint will be created.

Syntax
```

```

`dbms_cloud_oci_opsi_create_pe_comanaged_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_database_insight_details_t`type.

Fields

Field Description

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`database_resource_type`

(required) OCI database resource type

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`dbm_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint

`service_name`

(required) Database service name used for connection requests.

`credential_details`

(required)

`connection_details`

(optional)

`deployment_type`

(required) Database Deployment Type

Allowed values are: 'VIRTUAL_MACHINE', 'BARE_METAL', 'EXACS'

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_create_pe_comanaged_database_insight_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_EXADATA_VMCLUSTER_DETAILS_T Type

The information of the VM Cluster which contains databases. Either an opsiPrivateEndpointId or dbmPrivateEndpointId must be specified. If the dbmPrivateEndpointId is specified, a new Operations Insights private endpoint will be created.

Syntax
```

```

Fields

Field Description

`vmcluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Cluster.

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`dbm_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint

`member_database_details`

(optional) The databases that belong to the VM Cluster

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_EXADATA_VMCLUSTER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_create_pe_comanaged_exadata_vmcluster_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADD_PE_COMANAGED_EXADATA_INSIGHT_MEMBERS_DETAILS_T Type

The information about the members of Exadata system to be added.

Syntax
```

```

`dbms_cloud_oci_opsi_add_pe_comanaged_exadata_insight_members_details_t`is a subtype of the`dbms_cloud_oci_opsi_add_exadata_insight_members_details_t`type.

Fields

Field Description

`member_entity_details`

(optional)

### DBMS_CLOUD_OCI_OPSI_HOST_INSTANCE_MAP_T Type

Object containing hostname and instance name mapping.

Syntax
```

```

Fields

Field Description

`host_name`

(required) The hostname of the database insight resource.

`instance_name`

(required) The instance name of the database insight resource.

### DBMS_CLOUD_OCI_OPSI_HOST_INSTANCE_MAP_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_instance_map_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_DATABASE_DETAILS_T Type

Partial information about the database which includes id, name, type.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_name`

(required) The database name. The database name is unique within the tenancy.

`database_display_name`

(optional) The user-friendly name for the database. The name does not have to be unique.

`database_type`

(required) Operations Insights internal representation of the database type.

`database_version`

(optional) The version of the database.

`instances`

(optional) Array of hostname and instance name.

`cdb_name`

(optional) Name of the CDB.Only applies to PDB.

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SUMMARY_T Type

ADDM summary for a database

Syntax
```

```

Fields

Field Description

`database_details`

(required)

`number_of_findings`

(optional) Number of ADDM findings

`number_of_addm_tasks`

(optional) Number of ADDM tasks

`time_first_snapshot_begin`

(optional) The start timestamp that was passed into the request.

`time_latest_snapshot_end`

(optional) The end timestamp that was passed into the request.

`snapshot_interval_start`

(optional) AWR snapshot id.

`snapshot_interval_end`

(optional) AWR snapshot id.

`max_overall_impact`

(optional) Maximum overall impact in terms of percentage of total activity

`most_frequent_category_name`

(optional) Category name

`most_frequent_category_display_name`

(optional) Category display name

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_COLLECTION_T Type

The result of ADDM databases

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) List of ADDM database summary data

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_AGGREGATION_T Type

Summarizes a specific ADDM finding

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`finding_id`

(required) Unique finding id

`category_name`

(required) Category name

`category_display_name`

(required) Category display name

`name`

(required) Finding name

`message`

(required) Finding message

`impact_overall_percent`

(required) Overall impact in terms of percentage of total activity

`impact_max_percent`

(required) Maximum impact in terms of percentage of total activity

`impact_avg_active_sessions`

(optional) Impact in terms of average active sessions

`frequency_count`

(required) Number of occurrences for this finding

`recommendation_count`

(required) Number of recommendations for this finding

### DBMS_CLOUD_OCI_OPSI_DATABASE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_database_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_finding_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_AGGREGATION_COLLECTION_T Type

Summarizes ADDM findings over specified time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of ADDM finding summaries

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_CATEGORY_SUMMARY_T Type

Finding category summary

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`name`

(required) Name of finding category

`display_name`

(required) Display name of finding category

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_CATEGORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_finding_category_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_CATEGORY_COLLECTION_T Type

List of finding categories

Syntax
```

```

Fields

Field Description

`database_details_items`

(required) List of database details data

`items`

(required) List of finding categories

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDINGS_TIME_SERIES_SUMMARY_T Type

ADDM findings time series data

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`task_id`

(required) Unique ADDM task id

`task_name`

(required) ADDM task name

`finding_id`

(required) Unique finding id

`l_timestamp`

(required) Timestamp when finding was generated

`time_analysis_started`

(optional) Start Timestamp of snapshot

`time_analysis_ended`

(optional) End Timestamp of snapshot

`category_name`

(required) Category name

`category_display_name`

(required) Category display name

`name`

(required) Finding name

`message`

(required) Finding message

`analysis_db_time_in_secs`

(optional) DB time in seconds for the snapshot

`analysis_avg_active_sessions`

(optional) DB avg active sessions for the snapshot

`impact_db_time_in_secs`

(optional) Impact in seconds

`impact_percent`

(required) Impact in terms of percentage of total activity

`impact_avg_active_sessions`

(required) Impact in terms of average active sessions

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDINGS_TIME_SERIES_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_findings_time_series_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDINGS_TIME_SERIES_COLLECTION_T Type

ADDM findings time series response.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of ADDM finding time series data

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_AGGREGATION_T Type

Summarizes change history for specific database parameter

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`name`

(required) Name of parameter

`inst_num`

(optional) Number of database instance

`default_value`

(optional) Parameter default value

`begin_value`

(optional) Parameter value when time period began

`end_value`

(optional) Parameter value when time period ended

`is_changed`

(required) Indicates whether the parameter's value changed during the selected time range (TRUE) or did not change during the selected time range (FALSE)

`is_default`

(optional) Indicates whether the parameter's end value was set to the default value (TRUE) or was specified in the parameter file (FALSE)

`value_modified`

(optional) Indicates whether the parameter has been modified after instance starup MODIFIED - Parameter has been modified with ALTER SESSION SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM FALSE - Parameter has not been modified after instance starup

`is_high_impact`

(optional) Indicates whether the parameter is a high impact parameter (TRUE) or not (FALSE)

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_parameter_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_AGGREGATION_COLLECTION_T Type

Summarizes AWR parameter change history over specified time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of AWR parameter change summaries

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CATEGORY_SUMMARY_T Type

Database parameter category summary

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`name`

(required) Name of database parameter category

`display_name`

(required) Display name of database parameter category

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CATEGORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_parameter_category_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CATEGORY_COLLECTION_T Type

List of database parameter categories

Syntax
```

```

Fields

Field Description

`database_details_items`

(required) List of database details data

`items`

(required) List of database parameter categories

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CHANGE_AGGREGATION_T Type

Change record for AWR database parameter

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`time_begin`

(required) Begin time of interval which includes change

`time_end`

(required) End time of interval which includes change

`inst_num`

(required) Instance number

`previous_value`

(optional) Previous value

`value`

(optional) Current value

`snapshot_id`

(required) AWR snapshot id which includes the parameter value change

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CHANGE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_parameter_change_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CHANGE_AGGREGATION_COLLECTION_T Type

Summarizes AWR parameter change history over specified time period for specified parameter

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of AWR parameter changes

### DBMS_CLOUD_OCI_OPSI_RELATED_OBJECT_TYPE_DETAILS_T Type

Related object details

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of related object

Allowed values are: 'SCHEMA_OBJECT', 'SQL', 'DATABASE_PARAMETER'

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_AGGREGATION_T Type

Summarizes a specific ADDM recommendation

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`l_type`

(optional) Type of recommendation

`message`

(required) Recommendation message

`requires_db_restart`

(optional) Indicates implementation of the recommended action requires a database restart in order for it to take effect. Possible values \"Y\", \"N\" and null.

`implement_actions`

(optional) Actions that can be performed to implement the recommendation (such as 'ALTER PARAMETER', 'RUN SQL TUNING ADVISOR')

`rationale`

(optional) Recommendation message

`max_benefit_percent`

(optional) Maximum estimated benefit in terms of percentage of total activity

`overall_benefit_percent`

(optional) Overall estimated benefit in terms of percentage of total activity

`max_benefit_avg_active_sessions`

(optional) Maximum estimated benefit in terms of average active sessions

`frequency_count`

(optional) Number of occurrences for this recommendation

`related_object`

(optional)

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_recommendation_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_AGGREGATION_COLLECTION_T Type

Summarizes ADDM recommendations over specified time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of ADDM recommendation summaries

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_CATEGORY_SUMMARY_T Type

Recommendation category summary

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`name`

(required) Name of recommendation category

`display_name`

(required) Display name of recommendation category

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_CATEGORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_recommendation_category_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_CATEGORY_COLLECTION_T Type

List of recommendation categories

Syntax
```

```

Fields

Field Description

`database_details_items`

(required) List of database details data

`items`

(required) List of recommendation categories

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATIONS_TIME_SERIES_SUMMARY_T Type

ADDM recommendation

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`task_id`

(required) Unique ADDM task id

`task_name`

(required) ADDM task name

`l_timestamp`

(required) Timestamp when recommendation was generated

`time_analysis_started`

(optional) Start Timestamp of snapshot

`time_analysis_ended`

(optional) End Timestamp of snapshot

`l_type`

(optional) Type of recommendation

`analysis_db_time_in_secs`

(optional) DB time in seconds for the snapshot

`analysis_avg_active_sessions`

(optional) DB avg active sessions for the snapshot

`max_benefit_percent`

(optional) Maximum estimated benefit in terms of percentage of total activity

`max_benefit_db_time_in_secs`

(optional) Maximum estimated benefit in terms of seconds

`max_benefit_avg_active_sessions`

(optional) Maximum estimated benefit in terms of average active sessions

`related_object`

(optional)

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATIONS_TIME_SERIES_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_recommendations_time_series_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATIONS_TIME_SERIES_COLLECTION_T Type

ADDM recommendations time series

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of ADDM recommendations time series data

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SCHEMA_OBJECT_SUMMARY_T Type

Details for a given object id

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`object_identifier`

(required) Object id (from RDBMS)

`owner`

(required) Owner of object

`object_name`

(required) Name of object

`sub_object_name`

(optional) Subobject name; for example, partition name

`object_type`

(required) Type of the object (such as TABLE, INDEX)

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SCHEMA_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_schema_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SCHEMA_OBJECT_COLLECTION_T Type

Summarizes Schema Objects over specified time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of Schema Objects

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SQL_STATEMENT_SUMMARY_T Type

Details for a given SQL ID

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database insight.

`sql_identifier`

(required) SQL identifier

`sql_text`

(required) First 3800 characters of the SQL text

`is_sql_text_truncated`

(required) SQL identifier

`sql_command`

(required) SQL command name (such as SELECT, INSERT)

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SQL_STATEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_db_sql_statement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ADDM_DB_SQL_STATEMENT_COLLECTION_T Type

Summarizes SQL statements over specified time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`database_details_items`

(required) List of database details data

`items`

(required) List of SQL statements

### DBMS_CLOUD_OCI_OPSI_ADDM_REPORT_T Type

ADDM Tasks.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`task_identifier`

(required) TASK_ID in the oracle database view DBA_ADDM_TASKS

`database_identifier`

(required) Internal id of the database.

`snapshot_interval_start`

(required) AWR snapshot id.

`snapshot_interval_end`

(required) AWR snapshot id.

`addm_report`

(required) The complete ADDM report

### DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_SUMMARY_T Type

Summary of a database configuration for a resource.

Syntax
```

```

Fields

Field Description

`database_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`entity_source`

(required) Source of the database entity.

Allowed values are: 'AUTONOMOUS_DATABASE', 'EM_MANAGED_EXTERNAL_DATABASE', 'MACS_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_name`

(required) The database name. The database name is unique within the tenancy.

`database_display_name`

(required) The user-friendly name for the database. The name does not have to be unique.

`database_type`

(required) Operations Insights internal representation of the database type.

`database_version`

(required) The version of the database.

`cdb_name`

(required) Name of the CDB.Only applies to PDB.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`processor_count`

(optional) Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.

### DBMS_CLOUD_OCI_OPSI_AUTONOMOUS_DATABASE_CONFIGURATION_SUMMARY_T Type

Configuration Summary of autonomous database.

Syntax
```

```

`dbms_cloud_oci_opsi_autonomous_database_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_summary_t`type.

Fields

Field Description

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

### DBMS_CLOUD_OCI_OPSI_CONNECTION_DETAILS_T Type

Connection details to connect to the database. HostName, protocol, and port should be specified.

Syntax
```

```

Fields

Field Description

`host_name`

(required) Name of the listener host that will be used to create the connect string to the database.

`protocol`

(required) Protocol used for connection requests.

Allowed values are: 'TCP', 'TCPS'

`port`

(required) Listener port number used for connection requests.

`service_name`

(required) Database service name used for connection requests.

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHT_T Type

Database insight resource.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the database entity.

Allowed values are: 'AUTONOMOUS_DATABASE', 'EM_MANAGED_EXTERNAL_DATABASE', 'MACS_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE'

`id`

(required) Database insight identifier

`compartment_id`

(required) Compartment identifier of the database

`status`

(required) Indicates the status of a database insight in Operations Insights

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`database_type`

(optional) Operations Insights internal representation of the database type.

`database_version`

(optional) The version of the database.

`processor_count`

(optional) Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time the the database insight was first enabled. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the database insight was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the database.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`database_connection_status_details`

(optional) A message describing the status of the database connection of this resource. For example, it can be used to provide actionable information about the permission and content validity of the database connection.

### DBMS_CLOUD_OCI_OPSI_AUTONOMOUS_DATABASE_INSIGHT_T Type

Database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_autonomous_database_insight_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_t`type.

Fields

Field Description

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`database_name`

(required) Name of database

`database_display_name`

(optional) Display name of database

`database_resource_type`

(required) OCI database resource type

`db_additional_details`

(optional) Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty string. Note that this string needs to be escaped when specified in the curl command.

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`is_advanced_features_enabled`

(optional) Flag is to identify if advanced features for autonomous database is enabled or not

`connection_details`

(optional)

`credential_details`

(optional)

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHT_SUMMARY_T Type

Summary of a database insight resource.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_name`

(optional) The database name. The database name is unique within the tenancy.

`database_display_name`

(optional) The user-friendly name for the database. The name does not have to be unique.

`database_type`

(optional) Operations Insights internal representation of the database type.

`database_version`

(optional) The version of the database.

`database_host_names`

(optional) The hostnames for the database.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`entity_source`

(required) Source of the database entity.

Allowed values are: 'AUTONOMOUS_DATABASE', 'EM_MANAGED_EXTERNAL_DATABASE', 'MACS_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE'

`processor_count`

(optional) Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.

`status`

(optional) Indicates the status of a database insight in Operations Insights

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`time_created`

(optional) The time the the database insight was first enabled. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the database insight was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the database.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`database_connection_status_details`

(optional) A message describing the status of the database connection of this resource. For example, it can be used to provide actionable information about the permission and content validity of the database connection.

### DBMS_CLOUD_OCI_OPSI_AUTONOMOUS_DATABASE_INSIGHT_SUMMARY_T Type

Summary of a database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_autonomous_database_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_summary_t`type.

Fields

Field Description

`database_resource_type`

(optional) OCI database resource type

`is_advanced_features_enabled`

(optional) Flag is to identify if advanced features for autonomous database is enabled or not

### DBMS_CLOUD_OCI_OPSI_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SUMMARY_T Type

The AWR summary for a database.

Syntax
```

```

Fields

Field Description

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

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

`first_snapshot_identifier`

(optional) The ID of the earliest snapshot. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabaseSnapshots

`latest_snapshot_identifier`

(optional) The ID of the latest snapshot. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabaseSnapshots

`snapshot_count`

(optional) The total number of snapshots.

`snapshot_interval_in_min`

(optional) The interval time between snapshots (in minutes).

`db_version`

(optional) The version of the database.

`snapshot_timezone`

(optional) The time zone of the snapshot. sample - snapshotTimezone=+0 00:00:00

### DBMS_CLOUD_OCI_OPSI_AWR_QUERY_RESULT_T Type

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

`db_query_time_in_secs`

(optional) The time taken to query the database tier (in seconds).

`awr_result_type`

(required) The result type of AWR query.

Allowed values are: 'AWRDB_SET', 'AWRDB_SNAPSHOT_RANGE_SET', 'AWRDB_SNAPSHOT_SET', 'AWRDB_METRICS_SET', 'AWRDB_SYSSTAT_SET', 'AWRDB_TOP_EVENT_SET', 'AWRDB_EVENT_SET', 'AWRDB_EVENT_HISTOGRAM', 'AWRDB_DB_PARAMETER_SET', 'AWRDB_DB_PARAMETER_CHANGE', 'AWRDB_ASH_CPU_USAGE_SET', 'AWRDB_DB_REPORT', 'AWRDB_SQL_REPORT'

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_COLLECTION_T Type

The result of AWR query.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_CPU_USAGE_SUMMARY_T Type

A summary of the AWR CPU resource limits and metrics.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(optional) The timestamp for the CPU summary data.

`avg_usage_in_secs`

(optional) The average CPU usage per second.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_CPU_USAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_cpu_usage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_CPU_USAGE_COLLECTION_T Type

The AWR CPU usage data.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_cpu_usage_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`num_cpu_cores`

(optional) The number of available CPU cores, which include subcores of multicore and single-core CPUs.

`database_cpu_count`

(optional) The number of CPUs available for the database to use.

`host_cpu_count`

(optional) The number of available CPUs or processors.

`items`

(optional) A list of AWR CPU usage summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_METRIC_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_METRIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_metric_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_METRIC_COLLECTION_T Type

The AWR metrics time series summary data.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_metric_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR metric summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_CHANGE_SUMMARY_T Type

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

`snapshot_identifier`

(required) The ID of the snapshot with the parameter value changed. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabaseSnapshots

`value_modified`

(optional) Indicates whether the parameter has been modified after instance startup: - MODIFIED - Parameter has been modified with ALTER SESSION - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions values to be modified) - FALSE - Parameter has not been modified after instance startup

`is_default`

(optional) Indicates whether the parameter value in the end snapshot is the default.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_CHANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_parameter_change_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_CHANGE_COLLECTION_T Type

The AWR database parameter change history.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_parameter_change_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR database parameter change summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_SUMMARY_T Type

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

(optional) Indicates whether the parameter has been modified after instance startup: - MODIFIED - Parameter has been modified with ALTER SESSION - SYSTEM_MOD - Parameter has been modified with ALTER SYSTEM (which causes all the currently logged in sessions values to be modified) - FALSE - Parameter has not been modified after instance startup

`is_default`

(optional) Indicates whether the parameter value in the end snapshot is the default.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_parameter_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_COLLECTION_T Type

The AWR database parameter data.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_parameter_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR database parameter summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_REPORT_T Type

The result of the AWR report.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_report_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`content`

(optional) The content of the report.

`format`

(optional) The format of the report.

Allowed values are: 'HTML', 'TEXT', 'XML'

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_SUMMARY_T Type

The AWR snapshot summary of one snapshot.

Syntax
```

```

Fields

Field Description

`awr_source_database_identifier`

(required) Internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The database instance number.

`time_db_startup`

(optional) The timestamp of the database startup.

`time_begin`

(optional) The start time of the snapshot.

`time_end`

(optional) The end time of the snapshot.

`snapshot_identifier`

(required) The ID of the snapshot. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDbSnapshots

`error_count`

(optional) The total number of errors.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_snapshot_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_COLLECTION_T Type

The list of AWR snapshots for one database.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_snapshot_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR snapshot summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_RANGE_SUMMARY_T Type

The summary data for a range of AWR snapshots.

Syntax
```

```

Fields

Field Description

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

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

`first_snapshot_identifier`

(optional) The ID of the earliest snapshot. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabaseSnapshots

`latest_snapshot_identifier`

(optional) The ID of the latest snapshot. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabaseSnapshots

`snapshot_count`

(optional) The total number of snapshots.

`snapshot_interval_in_min`

(optional) The interval time between snapshots (in minutes).

`db_version`

(optional) The version of the database.

`snapshot_timezone`

(optional) The time zone of the snapshot. sample - snapshotTimezone=+0 00:00:00

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_RANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_snapshot_range_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_RANGE_COLLECTION_T Type

The AWR snapshot range list.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_snapshot_range_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR snapshot range summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SQL_REPORT_T Type

The result of the AWR SQL report.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_sql_report_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`content`

(optional) The content of the report.

`format`

(optional) The format of the report.

Allowed values are: 'HTML', 'TEXT'

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SYSSTAT_SUMMARY_T Type

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

(optional) The average value of the SYSSTAT. The units are stats name/val per the time period {timeBegin - timeEnd}.

`current_value`

(optional) The last value of the SYSSTAT. The units are stats name/val per the time period {timeBegin - timeEnd}.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SYSSTAT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_sysstat_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SYSSTAT_COLLECTION_T Type

The AWR SYSSTAT time series summary data.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_sysstat_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR SYSSTAT summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_TOP_WAIT_EVENT_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_TOP_WAIT_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_top_wait_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_TOP_WAIT_EVENT_COLLECTION_T Type

The AWR top wait event data.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_top_wait_event_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR top event summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_BUCKET_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_BUCKET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_wait_event_bucket_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_BUCKET_COLLECTION_T Type

The percentage distribution of waits in the AWR wait event buckets.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_wait_event_bucket_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`total_waits`

(optional) The total waits of the database.

`items`

(optional) A list of AWR wait event buckets.

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_SUMMARY_T Type

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

`snapshot_identifier`

(optional) The ID of the snapshot. The snapshot identifier is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabaseSnapshots

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_database_wait_event_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_COLLECTION_T Type

The AWR wait event data.

Syntax
```

```

`dbms_cloud_oci_opsi_awr_database_wait_event_collection_t`is a subtype of the`dbms_cloud_oci_opsi_awr_query_result_t`type.

Fields

Field Description

`items`

(optional) A list of AWR wait events.

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_T Type

Awr Hub resource.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) OPSI Warehouse OCID

`id`

(required) AWR Hub OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) User-friedly name of AWR Hub that does not have to be unique.

`object_storage_bucket_name`

(required) Object Storage Bucket Name

`awr_mailbox_url`

(optional) Mailbox URL required for AWR hub and AWR source setup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`hub_dst_timezone_version`

(optional) Dst Time Zone Version of the AWR Hub

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_OBJECTS_T Type

Logical grouping used for Awr Hub Object operations.

Syntax
```

```

Fields

Field Description

`awr_snapshots`

(optional) Awr Hub Object.

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_T Type

Awr hub source object

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Awr Hub source database.

`awr_hub_id`

(required) AWR Hub OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`l_type`

(required) source type of the database

Allowed values are: 'ADW_S', 'ATP_S', 'ADW_D', 'ATP_D', 'EXTERNAL_PDB', 'EXTERNAL_NONCDB', 'COMANAGED_VM_CDB', 'COMANAGED_VM_PDB', 'COMANAGED_VM_NONCDB', 'COMANAGED_BM_CDB', 'COMANAGED_BM_PDB', 'COMANAGED_BM_NONCDB', 'COMANAGED_EXACS_CDB', 'COMANAGED_EXACS_PDB', 'COMANAGED_EXACS_NONCDB', 'UNDEFINED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Awr Hub source database.

`awr_hub_opsi_source_id`

(required) The shorted string of the Awr Hub source database identifier.

`source_mail_box_url`

(required) Opsi Mailbox URL based on the Awr Hub and Awr Hub source.

`associated_resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database id.

`associated_opsi_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database id.

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`is_registered_with_awr_hub`

(optional) This is `true` if the source databse is registered with a Awr Hub, otherwise `false`

`awr_source_database_id`

(optional) DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.

`min_snapshot_identifier`

(optional) The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.

`max_snapshot_identifier`

(optional) The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.

`time_first_snapshot_generated`

(optional) The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string

`time_last_snapshot_generated`

(optional) The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string

`hours_since_last_import`

(optional) Number of hours since last AWR snapshots import happened from the Source database.

`lifecycle_state`

(required) the current state of the source database

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`status`

(required) Indicates the status of a source database in Operations Insights

Allowed values are: 'ACCEPTING', 'NOT_ACCEPTING', 'NOT_REGISTERED', 'TERMINATED'

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_SUMMARY_T Type

Awr hub source object

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Awr Hub source database.

`awr_hub_id`

(required) AWR Hub OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`l_type`

(required) source type of the database

Allowed values are: 'ADW_S', 'ATP_S', 'ADW_D', 'ATP_D', 'EXTERNAL_PDB', 'EXTERNAL_NONCDB', 'COMANAGED_VM_CDB', 'COMANAGED_VM_PDB', 'COMANAGED_VM_NONCDB', 'COMANAGED_BM_CDB', 'COMANAGED_BM_PDB', 'COMANAGED_BM_NONCDB', 'COMANAGED_EXACS_CDB', 'COMANAGED_EXACS_PDB', 'COMANAGED_EXACS_NONCDB', 'UNDEFINED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Awr Hub source database.

`awr_hub_opsi_source_id`

(required) The shorted string of the Awr Hub source database identifier.

`source_mail_box_url`

(required) Opsi Mailbox URL based on the Awr Hub and Awr Hub source.

`associated_resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database id.

`associated_opsi_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database id.

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`is_registered_with_awr_hub`

(optional) This is `true` if the source databse is registered with a Awr Hub, otherwise `false`

`awr_source_database_id`

(optional) DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.

`min_snapshot_identifier`

(optional) The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.

`max_snapshot_identifier`

(optional) The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.

`time_first_snapshot_generated`

(optional) The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string

`time_last_snapshot_generated`

(optional) The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string

`hours_since_last_import`

(optional) Number of hours since last AWR snapshots import happened from the Source database.

`lifecycle_state`

(required) the current state of the source database

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`status`

(required) Indicates the status of a source database in Operations Insights

Allowed values are: 'ACCEPTING', 'NOT_ACCEPTING', 'NOT_REGISTERED', 'TERMINATED'

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_hub_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_SUMMARY_COLLECTION_T Type

Collection of Awr Hub sources.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Awr Hub source objects.

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCES_T Type

Logical grouping used for Awr Hub Source operations.

Syntax
```

```

Fields

Field Description

`awr_hub_sources`

(optional) Awr Hub Source Object.

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SUMMARY_T Type

Summary Hub resource.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) OPSI Warehouse OCID

`id`

(required) AWR Hub OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) User-friedly name of AWR Hub that does not have to be unique.

`object_storage_bucket_name`

(required) Object Storage Bucket Name

`awr_mailbox_url`

(optional) Mailbox URL required for AWR hub and AWR source setup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_hub_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_HUB_SUMMARY_COLLECTION_T Type

Collection of Hub resources.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Hub summary objects.

### DBMS_CLOUD_OCI_OPSI_AWR_HUBS_T Type

Logical grouping used for Awr Hub operations.

Syntax
```

```

Fields

Field Description

`awr_hubs`

(optional) Awr Hub Object.

### DBMS_CLOUD_OCI_OPSI_AWR_REPORT_T Type

The result of the AWR report.

Syntax
```

```

Fields

Field Description

`content`

(optional) The content of the report.

`format`

(required) The format of the report.

Allowed values are: 'HTML', 'TEXT'

### DBMS_CLOUD_OCI_OPSI_AWR_SNAPSHOT_SUMMARY_T Type

The AWR snapshot summary of one snapshot.

Syntax
```

```

Fields

Field Description

`awr_source_database_id`

(required) DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.

`instance_number`

(optional) The database instance number.

`time_db_startup`

(optional) The timestamp of the database startup.

`time_snapshot_begin`

(optional) The start time of the snapshot.

`time_snapshot_end`

(optional) The end time of the snapshot.

`snapshot_identifier`

(required) The identifier of the snapshot.

`error_count`

(optional) The total number of errors.

### DBMS_CLOUD_OCI_OPSI_AWR_SNAPSHOT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_snapshot_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_AWR_SNAPSHOT_COLLECTION_T Type

The list of AWR snapshots for one database.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of AWR snapshot summary data.

### DBMS_CLOUD_OCI_OPSI_AWR_SOURCE_SUMMARY_T Type

Summary of an AwrSource.

Syntax
```

```

Fields

Field Description

`awr_hub_id`

(required) AWR Hub OCID

`name`

(required) Database name of the Source database for which AWR Data will be uploaded to AWR Hub.

`awr_source_database_id`

(required) DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.

`snapshots_uploaded`

(required) Number of AWR snapshots uploaded from the Source database.

`min_snapshot_identifier`

(required) The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.

`max_snapshot_identifier`

(required) The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.

`time_first_snapshot_generated`

(required) The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string

`time_last_snapshot_generated`

(required) The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string

`hours_since_last_import`

(required) Number of hours since last AWR snapshots import happened from the Source database.

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_UNIT_DETAILS_T Type

Unit details of configuration item.

Syntax
```

```

Fields

Field Description

`unit`

(optional) Unit of configuration item.

`display_name`

(optional) User-friendly display name for the configuration item unit.

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_ALLOWED_VALUE_DETAILS_T Type

Allowed value details of configuration item, to validate what value can be assigned to a configuration item.

Syntax
```

```

Fields

Field Description

`allowed_value_type`

(required) Allowed value type of configuration item.

Allowed values are: 'LIMIT', 'PICK', 'FREE_TEXT'

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_METADATA_T Type

Configuration item metadata.

Syntax
```

```

Fields

Field Description

`config_item_type`

(required) Type of configuration item.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_OPSI_BASIC_CONFIGURATION_ITEM_METADATA_T Type

Basic configuration item metadata.

Syntax
```

```

`dbms_cloud_oci_opsi_basic_configuration_item_metadata_t`is a subtype of the`dbms_cloud_oci_opsi_configuration_item_metadata_t`type.

Fields

Field Description

`display_name`

(optional) User-friendly display name for the configuration item.

`description`

(optional) Description of configuration item .

`data_type`

(optional) Data type of configuration item. Examples: STRING, BOOLEAN, NUMBER

`unit_details`

(optional)

`value_input_details`

(optional)

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_SUMMARY_T Type

Configuration item summary.

Syntax
```

```

Fields

Field Description

`config_item_type`

(required) Type of configuration item.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_OPSI_BASIC_CONFIGURATION_ITEM_SUMMARY_T Type

Basic configuration item summary. Value field contain the most preferred value for the specified scope (compartmentId), which could be from any of the ConfigurationItemValueSourceConfigurationType. Default value field contains the default value from Operations Insights.

Syntax
```

```

`dbms_cloud_oci_opsi_basic_configuration_item_summary_t`is a subtype of the`dbms_cloud_oci_opsi_configuration_item_summary_t`type.

Fields

Field Description

`name`

(optional) Name of configuration item.

`value`

(optional) Value of configuration item.

`value_source_config`

(optional) Source configuration from where the value is taken for a configuration item.

Allowed values are: 'DEFAULT', 'TENANT', 'COMPARTMENT'

`default_value`

(optional) Value of configuration item.

`applicable_contexts`

(optional) List of contexts in Operations Insights where this configuration item is applicable.

`metadata`

(optional)

### DBMS_CLOUD_OCI_OPSI_CHANGE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES_DETAILS_T Type

Advanced feature details of autonomous database insight.

Syntax
```

```

Fields

Field Description

`connection_details`

(required)

`credential_details`

(required)

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

### DBMS_CLOUD_OCI_OPSI_CHANGE_AWR_HUB_SOURCE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_DATABASE_INSIGHT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_ENTERPRISE_MANAGER_BRIDGE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_EXADATA_INSIGHT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_HOST_INSIGHT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_NEWS_REPORT_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource will be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

The details used to change the compartment of a Operation Insights private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The new compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Private service accessed database.

### DBMS_CLOUD_OCI_OPSI_CHANGE_OPERATIONS_INSIGHTS_WAREHOUSE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_OPSI_CHANGE_OPSI_CONFIGURATION_COMPARTMENT_DETAILS_T Type

The information used to change the compartment of an OPSI configuration resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_OPSI_CHANGE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type

Details of a Private Endpoint co-managed database insight.

Syntax
```

```

Fields

Field Description

`service_name`

(required) Database service name used for connection requests.

`credential_details`

(required)

`connection_details`

(optional)

`opsi_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_T Type

A compute entity that can be imported into Operations Insights.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the importable agent entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST'

`compute_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Compute Instance

`compute_display_name`

(required) The[Display Name](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display)of the Compute Instance

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_OPSI_CLOUD_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_T Type

A compute host entity that can be imported into Operations Insights.

Syntax
```

```

`dbms_cloud_oci_opsi_cloud_importable_compute_entity_summary_t`is a subtype of the`dbms_cloud_oci_opsi_importable_compute_entity_summary_t`type.

Fields

Field Description

`host_name`

(required) The host name. The host name is unique amongst the hosts managed by the same management agent.

`platform_type`

(required) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_FREE_TEXT_ALLOWED_VALUE_DETAILS_T Type

Allowed value details of configuration item for FREE_TEXT type.

Syntax
```

```

`dbms_cloud_oci_opsi_configuration_item_free_text_allowed_value_details_t`is a subtype of the`dbms_cloud_oci_opsi_configuration_item_allowed_value_details_t`type.

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_LIMIT_ALLOWED_VALUE_DETAILS_T Type

Allowed value details of configuration item for LIMIT type. Value has to be between minValue and maxValue.

Syntax
```

```

`dbms_cloud_oci_opsi_configuration_item_limit_allowed_value_details_t`is a subtype of the`dbms_cloud_oci_opsi_configuration_item_allowed_value_details_t`type.

Fields

Field Description

`min_value`

(optional) Minimum value limit for the configuration item.

`max_value`

(optional) Maximum value limit for the configuration item.

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_PICK_ALLOWED_VALUE_DETAILS_T Type

Allowed value details of configuration item for PICK type. Value has to be from one of the possibleValues.

Syntax
```

```

`dbms_cloud_oci_opsi_configuration_item_pick_allowed_value_details_t`is a subtype of the`dbms_cloud_oci_opsi_configuration_item_allowed_value_details_t`type.

Fields

Field Description

`possible_values`

(optional) Allowed values to pick for the configuration item.

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_configuration_item_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEMS_COLLECTION_T Type

Collection of configuration item summary objects.

Syntax
```

```

Fields

Field Description

`opsi_config_type`

(required) OPSI configuration type.

Allowed values are: 'UX_CONFIGURATION'

`config_items`

(optional) Array of configuration item summary objects.

### DBMS_CLOUD_OCI_OPSI_CREATE_AWR_HUB_DETAILS_T Type

The information about Hub to be analyzed. Input compartmentId MUST be the root compartment.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) OPSI Warehouse OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) User-friedly name of AWR Hub that does not have to be unique.

`object_storage_bucket_name`

(optional) Object Storage Bucket Name

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_AWR_HUB_SOURCE_DETAILS_T Type

payload to register Awr Hub source

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Awr Hub source database.

`awr_hub_id`

(required) AWR Hub OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`associated_resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database id.

`associated_opsi_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database id.

`l_type`

(required) source type of the database

Allowed values are: 'ADW_S', 'ATP_S', 'ADW_D', 'ATP_D', 'EXTERNAL_PDB', 'EXTERNAL_NONCDB', 'COMANAGED_VM_CDB', 'COMANAGED_VM_PDB', 'COMANAGED_VM_NONCDB', 'COMANAGED_BM_CDB', 'COMANAGED_BM_PDB', 'COMANAGED_BM_NONCDB', 'COMANAGED_EXACS_CDB', 'COMANAGED_EXACS_PDB', 'COMANAGED_EXACS_NONCDB', 'UNDEFINED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_CONFIGURATION_ITEM_DETAILS_T Type

Configuration item details for OPSI configuration creation.

Syntax
```

```

Fields

Field Description

`config_item_type`

(required) Type of configuration item.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_OPSI_CREATE_BASIC_CONFIGURATION_ITEM_DETAILS_T Type

Basic configuration item details for OPSI configuration creation.

Syntax
```

```

`dbms_cloud_oci_opsi_create_basic_configuration_item_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_configuration_item_details_t`type.

Fields

Field Description

`name`

(optional) Name of configuration item.

`value`

(optional) Value of configuration item.

### DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type

The information about database to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_create_em_managed_external_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_database_insight_details_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`exadata_insight_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

### DBMS_CLOUD_OCI_OPSI_CREATE_EXADATA_INSIGHT_DETAILS_T Type

The information about the Exadata system to be analyzed.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the Exadata system.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

`compartment_id`

(required) Compartment Identifier of Exadata insight

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_DETAILS_T Type

The information about the Exadata system to be analyzed. If memberEntityDetails is not specified, the the Enterprise Manager entity (e.g. databases and hosts) associated with an Exadata system will be placed in the same compartment as the Exadata system.

Syntax
```

```

`dbms_cloud_oci_opsi_create_em_managed_external_exadata_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_exadata_insight_details_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`member_entity_details`

(optional)

`is_auto_sync_enabled`

(optional) Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.

### DBMS_CLOUD_OCI_OPSI_CREATE_HOST_INSIGHT_DETAILS_T Type

The information about the host to be analyzed.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the host entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'EM_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST', 'PE_COMANAGED_HOST'

`compartment_id`

(required) Compartment Identifier of host

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type

The information about the EM-managed external host to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_create_em_managed_external_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_host_insight_details_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`exadata_insight_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

### DBMS_CLOUD_OCI_OPSI_CREATE_ENTERPRISE_MANAGER_BRIDGE_DETAILS_T Type

The information about a Enterprise Manager bridge resource to be created

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment identifier of the Enterprise Manager bridge

`display_name`

(required) User-friedly name of Enterprise Manager Bridge that does not have to be unique.

`description`

(optional) Description of Enterprise Manager Bridge

`object_storage_bucket_name`

(required) Object Storage Bucket Name

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_MACS_MANAGED_CLOUD_HOST_INSIGHT_DETAILS_T Type

The information about the Compute Instance host to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_create_macs_managed_cloud_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_host_insight_details_t`type.

Fields

Field Description

`compute_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Compute Instance

### DBMS_CLOUD_OCI_OPSI_CREATE_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type

The information about the MACS-managed external host to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_create_macs_managed_external_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_host_insight_details_t`type.

Fields

Field Description

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

### DBMS_CLOUD_OCI_OPSI_NEWS_CONTENT_TYPES_T Type

Content types that the news report can handle.

Syntax
```

```

Fields

Field Description

`capacity_planning_resources`

(required) Supported resources for capacity planning content type.

### DBMS_CLOUD_OCI_OPSI_CREATE_NEWS_REPORT_DETAILS_T Type

The information about the news report to be created.

Syntax
```

```

Fields

Field Description

`name`

(required) The news report name.

`news_frequency`

(required) News report frequency.

Allowed values are: 'WEEKLY'

`description`

(required) The description of the news report.

`ons_topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ONS topic.

`compartment_id`

(required) Compartment Identifier where the news report will be created.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`content_types`

(required)

`locale`

(required) Language of the news report.

Allowed values are: 'EN'

`status`

(optional) Defines if the news report will be enabled or disabled.

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

### DBMS_CLOUD_OCI_OPSI_CREATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_DETAILS_T Type

The details used to create a new Operation Insights private endpoint.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The display name for the private endpoint. It is changeable.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Private service accessed database.

`vcn_id`

(required) The VCN[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Private service accessed database.

`subnet_id`

(required) The Subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Private service accessed database.

`is_used_for_rac_dbs`

(required) The flag to identify if private endpoint is used for rac database or not

`description`

(optional) The description of the private endpoint.

`nsg_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups that the private endpoint belongs to.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_OPERATIONS_INSIGHTS_WAREHOUSE_DETAILS_T Type

The information about a Operations Insights Warehouse resource to be created. Input compartmentId MUST be the root compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) User-friedly name of Operations Insights Warehouse that does not have to be unique.

`cpu_allocated`

(required) Number of OCPUs allocated to OPSI Warehouse ADW.

`storage_allocated_in_g_bs`

(optional) Storage allocated to OPSI Warehouse ADW.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER_DETAILS_T Type

The information about a Operations Insights Warehouse User to be created. Input compartmentId MUST be the root compartment.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) OPSI Warehouse OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(required) Username for schema which would have access to AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`connection_password`

(required) User provided connection password for the AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`is_awr_data_access`

(required) Indicate whether user has access to AWR data.

`is_em_data_access`

(optional) Indicate whether user has access to EM data.

`is_opsi_data_access`

(optional) Indicate whether user has access to OPSI data.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_CREATE_CONFIGURATION_ITEM_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_create_configuration_item_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_CREATE_OPSI_CONFIGURATION_DETAILS_T Type

Information about OPSI configuration to be created.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opsi_config_type`

(required) OPSI configuration type.

Allowed values are: 'UX_CONFIGURATION'

`display_name`

(optional) User-friendly display name for the OPSI configuration. The name does not have to be unique.

`description`

(optional) Description of OPSI configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`config_items`

(optional) Array of configuration items with custom values. All and only configuration items requiring custom values should be part of this array.

### DBMS_CLOUD_OCI_OPSI_CREATE_OPSI_UX_CONFIGURATION_DETAILS_T Type

Information about OPSI UX configuration to be created.

Syntax
```

```

`dbms_cloud_oci_opsi_create_opsi_ux_configuration_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_opsi_configuration_details_t`type.

### DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_EXADATA_INSIGHT_DETAILS_T Type

The information about the Exadata system to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_create_pe_comanaged_exadata_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_create_exadata_insight_details_t`type.

Fields

Field Description

`exadata_infra_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata Infrastructure.

`member_vm_cluster_details`

(optional)

### DBMS_CLOUD_OCI_OPSI_CREDENTIAL_BY_VAULT_T Type

Vault Credential Details to connect to the database.

Syntax
```

```

`dbms_cloud_oci_opsi_credential_by_vault_t`is a subtype of the`dbms_cloud_oci_opsi_credential_details_t`type.

Fields

Field Description

`user_name`

(optional) database user name.

`password_secret_id`

(optional) The secret[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)mapping to the database credentials.

`wallet_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the database keystore contents are stored. This is used for TCPS support in BM/VM/ExaCS cases.

`role`

(optional) database user role.

Allowed values are: 'NORMAL'

### DBMS_CLOUD_OCI_OPSI_CREDENTIALS_BY_SOURCE_T Type

Credential Source to connect to the database.

Syntax
```

```

`dbms_cloud_oci_opsi_credentials_by_source_t`is a subtype of the`dbms_cloud_oci_opsi_credential_details_t`type.

### DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_METRIC_GROUP_T Type

Supported configuration metric groups for database capacity planning service.

Syntax
```

```

Fields

Field Description

`metric_name`

(required) Name of the metric group.

Allowed values are: 'DB_EXTERNAL_PROPERTIES', 'DB_EXTERNAL_INSTANCE', 'DB_OS_CONFIG_INSTANCE', 'DB_PARAMETERS'

`time_collected`

(optional) Collection timestamp Example: `\"2020-05-06T00:00:00.000Z\"`

### DBMS_CLOUD_OCI_OPSI_DB_EXTERNAL_INSTANCE_T Type

Configuration parameters defined for external databases instance level.

Syntax
```

```

`dbms_cloud_oci_opsi_db_external_instance_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_metric_group_t`type.

Fields

Field Description

`instance_name`

(required) Name of the database instance.

`host_name`

(required) Host name of the database instance.

`cpu_count`

(optional) Total number of CPUs allocated for the host.

`host_memory_capacity`

(optional) Total amount of usable Physical RAM Memory available in gigabytes.

`version`

(optional) Database version.

`parallel`

(optional) Indicates whether the instance is mounted in cluster database mode (YES) or not (NO).

`instance_role`

(optional) Role (permissions) of the database instance.

`logins`

(optional) Indicates if logins are allowed or restricted.

`database_status`

(optional) Status of the database.

`status`

(optional) Status of the instance.

`edition`

(optional) The edition of the database.

`startup_time`

(optional) Start up time of the database instance.

### DBMS_CLOUD_OCI_OPSI_DB_EXTERNAL_PROPERTIES_T Type

Configuration parameters defined for external databases.

Syntax
```

```

`dbms_cloud_oci_opsi_db_external_properties_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_metric_group_t`type.

Fields

Field Description

`name`

(optional) Name of the database.

`log_mode`

(optional) Archive log mode.

`cdb`

(optional) Indicates if it is a CDB or not. This would be 'yes' or 'no'.

`open_mode`

(optional) Open mode information.

`database_role`

(optional) Current role of the database.

`guard_status`

(optional) Data protection policy.

`platform_name`

(optional) Platform name of the database, OS with architecture.

`control_file_type`

(optional) Type of control file.

`switchover_status`

(optional) Indicates whether switchover is allowed.

`created`

(optional) Creation time.

### DBMS_CLOUD_OCI_OPSI_DBOS_CONFIG_INSTANCE_T Type

Configuration parameters defined for external databases instance level.

Syntax
```

```

`dbms_cloud_oci_opsi_dbos_config_instance_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_metric_group_t`type.

Fields

Field Description

`instance_name`

(required) Name of the database instance.

`host_name`

(required) Host name of the database instance.

`num_cp_us`

(optional) Total number of CPUs available.

`num_cpu_cores`

(optional) Number of CPU cores available (includes subcores of multicore CPUs as well as single-core CPUs).

`num_cpu_sockets`

(optional) Number of CPU Sockets available.

`physical_memory_bytes`

(optional) Total number of bytes of physical memory.

### DBMS_CLOUD_OCI_OPSI_DB_PARAMETERS_T Type

Initialization parameters for a database.

Syntax
```

```

`dbms_cloud_oci_opsi_db_parameters_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_metric_group_t`type.

Fields

Field Description

`instance_number`

(required) Database instance number.

`parameter_name`

(required) Database parameter name.

`parameter_value`

(required) Database parameter value.

`snapshot_id`

(optional) AWR snapshot id for the parameter value

`is_changed`

(optional) Indicates whether the parameter's value changed in given snapshot or not.

`is_default`

(optional) Indicates whether this value is the default value or not.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_BIND_PARAMETER_T Type

Details for a bind parameter used in data object query.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the bind parameter.

`value`

(required) Value for the bind parameter.

`data_type`

(required) Data type of the bind parameter.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_COLUMN_UNIT_T Type

Unit details of a data object column.

Syntax
```

```

Fields

Field Description

`unit_category`

(required) Category of the column's unit.

Allowed values are: 'DATA_SIZE', 'TIME', 'POWER', 'TEMPERATURE', 'CORE', 'RATE', 'FREQUENCY', 'OTHER_STANDARD', 'CUSTOM'

`display_name`

(optional) Display name of the column's unit.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_COLUMN_METADATA_T Type

Metadata of a column in a data object resultset.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the column.

`category`

(optional) Category of the column.

Allowed values are: 'DIMENSION', 'METRIC', 'TIME_DIMENSION', 'UNKNOWN'

`data_type`

(optional) Type of a data object column.

`data_type_name`

(optional) Type name of a data object column.

Allowed values are: 'NUMBER', 'TIMESTAMP', 'VARCHAR2', 'OTHER'

`display_name`

(optional) Display name of the column.

`description`

(optional) Description of the column.

`group_name`

(optional) Group name of the column.

`unit_details`

(optional)

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_CORE_COLUMN_UNIT_T Type

Unit details of a data object column of CORE unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_core_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Core unit.

Allowed values are: 'CORE', 'MILLI_CORE'

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_CUSTOM_COLUMN_UNIT_T Type

Unit details of a data object column of CUSTOM unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_custom_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Custom column unit.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_DATA_SIZE_COLUMN_UNIT_T Type

Unit details of a data object column of DATA_SIZE unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_data_size_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Data size unit.

Allowed values are: 'CHARACTER', 'BLOCK', 'BIT', 'BYTE', 'KILO_BYTE', 'MEGA_BYTE', 'GIGA_BYTE', 'TERA_BYTE', 'PETA_BYTE', 'EXA_BYTE', 'ZETTA_BYTE', 'YOTTA_BYTE'

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_FREQUENCY_COLUMN_UNIT_T Type

Unit details of a data object column of FREQEUENCY unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_frequency_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Frequency unit.

Allowed values are: 'HERTZ', 'KILO_HERTZ', 'MEGA_HERTZ', 'GIGA_HERTZ', 'TERA_HERTZ'

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_OTHER_STANDARD_COLUMN_UNIT_T Type

Unit details of a data object column of OTHER_STANDARD unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_other_standard_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Other standard column unit.

Allowed values are: 'PERCENTAGE', 'COUNT', 'IO', 'BOOLEAN', 'OPERATION', 'TRANSACTION', 'CONNECTION', 'ACCESS', 'REQUEST', 'MESSAGE', 'EXECUTION', 'LOGONS', 'THREAD', 'ERROR'

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_POWER_COLUMN_UNIT_T Type

Unit details of a data object column of POWER unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_power_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Power unit.

Allowed values are: 'AMP', 'WATT', 'KILO_WATT', 'MEGA_WATT', 'GIGA_WATT'

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_BIND_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_opsi_data_object_bind_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_QUERY_T Type

Information required to form and execute query on a data object.

Syntax
```

```

Fields

Field Description

`query_type`

(required) Type of Query

Allowed values are: 'TEMPLATIZED_QUERY', 'STANDARD_QUERY'

`bind_params`

(optional) List of bind parameters to be applied in the query.

`query_execution_timeout_in_seconds`

(optional) Timeout (in seconds) to be set for the data object query execution.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_QUERY_TIME_FILTERS_T Type

Time filters to be applied in the data object query.

Syntax
```

```

Fields

Field Description

`time_period`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timePeriod is specified, then timeStart and timeEnd will be ignored. Examples: P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months).

`time_start`

(optional) Start time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z. timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored.

`time_end`

(optional) End time in UTC in RFC3339 formatted datetime string. Example: 2021-10-30T00:00:00.000Z. timeStart and timeEnd are used together. If timePeriod is specified, this parameter is ignored. If timeEnd is not specified, current time is used as timeEnd.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_RATE_COLUMN_UNIT_T Type

Unit details of a data object column of RATE unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_rate_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`numerator`

(optional)

`denominator`

(optional)

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_STANDARD_QUERY_T Type

Information required to execute query on data objects. Query is given in standard SQL syntax providing flexibility to form complex queries such as queries with joins and nested queries.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_standard_query_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_query_t`type.

Fields

Field Description

`statement`

(optional) SQL query statement with standard Oracle supported SQL syntax. - When Warehouse (e.g: Awr hub) data objects are queried, use the actual names of underlying data objects (e.g: tables, views) in the query. The same query that works through JDBC connection with the OperationsInsightsWarehouseUsers credentials will work here and vice-versa. SCHEMA.VIEW syntax can also be used here. - When OPSI data objects are queried, use name of the respective OPSI data object, just like how views are used in a query. Identifier of the OPSI data object cannot be used in the query.

`time_filters`

(optional)

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_TEMPERATURE_COLUMN_UNIT_T Type

Unit details of a data object column of TEMPERATURE unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_temperature_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Temparature unit.

Allowed values are: 'CELSIUS', 'FAHRENHEIT'

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_TEMPLATIZED_QUERY_T Type

Information required in a structured template to form and execute query on a data object.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_templatized_query_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_query_t`type.

Fields

Field Description

`select_list`

(optional) List of items to be added into the SELECT clause of the query; items will be added with comma separation.

`from_clause`

(optional) Unique data object name that will be added into the FROM clause of the query, just like a view name in FROM clause. - Use actual name of the data objects (e.g: tables, views) in case of Warehouse (e.g: Awr hub) data objects query. SCHEMA.VIEW name syntax can also be used here. e.g: SYS.DBA_HIST_SNAPSHOT or DBA_HIST_SNAPSHOT - Use name of the data object (e.g: SQL_STATS_DO) in case of OPSI data objects. Identifier of the OPSI data object cannot be used here.

`where_conditions_list`

(optional) List of items to be added into the WHERE clause of the query; items will be added with AND separation. Item can contain a single condition or multiple conditions. Single condition e.g: \"optimizer_mode='mode1'\" Multiple conditions e.g: (module='module1' OR module='module2')

`group_by_list`

(optional) List of items to be added into the GROUP BY clause of the query; items will be added with comma separation.

`having_conditions_list`

(optional) List of items to be added into the HAVING clause of the query; items will be added with AND separation.

`order_by_list`

(optional) List of items to be added into the ORDER BY clause of the query; items will be added with comma separation.

`time_filters`

(optional)

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_TIME_COLUMN_UNIT_T Type

Unit details of a data object column of TIME unit category.

Syntax
```

```

`dbms_cloud_oci_opsi_data_object_time_column_unit_t`is a subtype of the`dbms_cloud_oci_opsi_data_object_column_unit_t`type.

Fields

Field Description

`unit`

(optional) Time unit.

Allowed values are: 'NANO_SECOND', 'MICRO_SECOND', 'MILLI_SECOND', 'CENTI_SECOND', 'SECOND', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR', 'MINUTE'

### DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_database_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_COLLECTION_T Type

Collection of database insight configuration summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of database insight configurations summary objects.

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_T Type

Logical grouping used for Operations Insights database-targeted operations.

Syntax
```

```

Fields

Field Description

`database_insights`

(optional) Database Insights Object.

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_database_insight_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_COLLECTION_T Type

Collection of database insight summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of database insight summary objects.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUPPORTED_QUERY_PARAM_T Type

Details of query parameter supported by an OPSI data object.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the query parameter.

`description`

(optional) Description of the query parameter.

`data_type`

(optional) Data type of the for the query parameter.

### DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_COLUMN_METADATA_TBL Type

Nested table type of dbms_cloud_oci_opsi_data_object_column_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUPPORTED_QUERY_PARAM_TBL Type

Nested table type of dbms_cloud_oci_opsi_opsi_data_object_supported_query_param_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_T Type

OPSI data object.

Syntax
```

```

Fields

Field Description

`identifier`

(required) Unique identifier of OPSI data object.

`data_object_type`

(required) Type of OPSI data object.

Allowed values are: 'DATABASE_INSIGHTS_DATA_OBJECT', 'HOST_INSIGHTS_DATA_OBJECT', 'EXADATA_INSIGHTS_DATA_OBJECT'

`display_name`

(required) User-friendly name of OPSI data object.

`description`

(optional) Description of OPSI data object.

`name`

(optional) Name of the data object, which can be used in data object queries just like how view names are used in a query.

`group_names`

(optional) Names of all the groups to which the data object belongs to.

`supported_query_time_period`

(optional) Time period supported by the data object for quering data. Time period is in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. Examples: P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months).

`columns_metadata`

(required) Metadata of columns in a data object.

`supported_query_params`

(optional) Supported query parameters by this OPSI data object that can be configured while a data object query involving this data object is executed.

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_DATA_OBJECT_T Type

Database insights data object.

Syntax
```

```

`dbms_cloud_oci_opsi_database_insights_data_object_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_t`type.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUMMARY_T Type

Summary of an OPSI data object.

Syntax
```

```

Fields

Field Description

`identifier`

(required) Unique identifier of OPSI data object.

`data_object_type`

(required) Type of OPSI data object.

Allowed values are: 'DATABASE_INSIGHTS_DATA_OBJECT', 'HOST_INSIGHTS_DATA_OBJECT', 'EXADATA_INSIGHTS_DATA_OBJECT'

`display_name`

(required) User-friendly name of OPSI data object.

`description`

(optional) Description of OPSI data object.

`name`

(optional) Name of the data object, which can be used in data object queries just like how view names are used in a query.

`group_names`

(optional) Names of all the groups to which the data object belongs to.

### DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_DATA_OBJECT_SUMMARY_T Type

Summary of a database insights data object.

Syntax
```

```

`dbms_cloud_oci_opsi_database_insights_data_object_summary_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_summary_t`type.

### DBMS_CLOUD_OCI_OPSI_DATABASE_PARAMETER_TYPE_DETAILS_T Type

Database parameter details

Syntax
```

```

`dbms_cloud_oci_opsi_database_parameter_type_details_t`is a subtype of the`dbms_cloud_oci_opsi_related_object_type_details_t`type.

Fields

Field Description

`name`

(required) Name of database parameter

### DBMS_CLOUD_OCI_OPSI_DISK_GROUP_DETAILS_T Type

Information about a diskgroup which includes diskgroup name and ASM name.

Syntax
```

```

Fields

Field Description

`diskgroup_name`

(required) The diskgroup name.

`asm_name`

(required) The ASM name.

### DBMS_CLOUD_OCI_OPSI_DISK_STATISTICS_T Type

Aggregated data per disk.

Syntax
```

```

Fields

Field Description

`disk_name`

(required) Name of the disk.

`disk_unallocated_in_g_bs`

(required) Value for unallocated space in a disk.

`disk_usage_in_g_bs`

(required) Disk usage.

`disk_size_in_g_bs`

(required) Size of the disk.

### DBMS_CLOUD_OCI_OPSI_DOWNLOAD_OPERATIONS_INSIGHTS_WAREHOUSE_WALLET_DETAILS_T Type

Download Wallet details.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_wallet_password`

(required) User provided ADW wallet password for the Operations Insights Warehouse.

### DBMS_CLOUD_OCI_OPSI_EXADATA_DETAILS_T Type

Partial information about the exadata which includes id, name and vmclusterNames.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`name`

(required) Name of exadata insight resource.

`vmcluster_names`

(optional) Array of vm cluster names. Applicable for ExaCC and ExaCS.

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_DATABASE_CONFIGURATION_SUMMARY_T Type

Configuration summary of a EM Managed External database.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_database_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_summary_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`instances`

(required) Array of hostname and instance name.

`exadata_details`

(required)

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_T Type

Database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_database_insight_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`enterprise_manager_entity_display_name`

(optional) Enterprise Manager Entity Display Name

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`exadata_insight_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_SUMMARY_T Type

Summary of a database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_database_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_summary_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`enterprise_manager_entity_display_name`

(optional) Enterprise Manager Entity Display Name

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`exadata_insight_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_T Type

Exadata insight resource.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the Exadata system.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

`id`

(required) Exadata insight identifier

`compartment_id`

(required) Compartment identifier of the Exadata insight resource

`exadata_name`

(required) The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.

`exadata_display_name`

(optional) The user-friendly name for the Exadata system. The name does not have to be unique.

`exadata_type`

(optional) Operations Insights internal representation of the the Exadata system type.

Allowed values are: 'DBMACHINE', 'EXACS', 'EXACC'

`exadata_rack_type`

(optional) Exadata rack type.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH', 'FLEX'

`is_virtualized_exadata`

(optional) true if virtualization is used in the Exadata system

`status`

(required) Indicates the status of an Exadata insight in Operations Insights

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time the the Exadata insight was first enabled. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Exadata insight was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Exadata insight.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_T Type

EM-managed Exadata insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_exadata_insight_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`enterprise_manager_entity_display_name`

(optional) Enterprise Manager Entity Display Name

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`is_auto_sync_enabled`

(optional) Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_SUMMARY_T Type

Summary of an Exadata insight resource.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the Exadata system.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`exadata_name`

(required) The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.

`exadata_display_name`

(optional) The user-friendly name for the Exadata system. The name does not have to be unique.

`exadata_type`

(optional) Operations Insights internal representation of the the Exadata system type.

Allowed values are: 'DBMACHINE', 'EXACS', 'EXACC'

`exadata_rack_type`

(optional) Operations Insights internal representation of the the Exadata system rack type.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH', 'FLEX'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`status`

(required) Indicates the status of an Exadata insight in Operations Insights

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`time_created`

(required) The time the the Exadata insight was first enabled. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Exadata insight was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Exadata insight.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_SUMMARY_T Type

Summary of an Exadata insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_exadata_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_summary_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`enterprise_manager_entity_display_name`

(optional) Enterprise Manager Entity Display Name

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

### DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_SUMMARY_T Type

Summary of a host configuration for a resource.

Syntax
```

```

Fields

Field Description

`host_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`entity_source`

(required) Source of the host entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'EM_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST', 'PE_COMANAGED_HOST'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`host_name`

(required) The host name. The host name is unique amongst the hosts managed by the same management agent.

`platform_type`

(required) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`platform_version`

(required) Platform version.

`platform_vendor`

(required) Platform vendor.

`total_cpus`

(required) Total CPU on this host.

`total_memory_in_g_bs`

(required) Total amount of usable physical memory in gibabytes

`cpu_architecture`

(required) CPU architechure

`cpu_cache_in_m_bs`

(required) Size of cache memory in megabytes.

`cpu_vendor`

(required) Name of the CPU vendor.

`cpu_frequency_in_mhz`

(required) Clock frequency of the processor in megahertz.

`cpu_implementation`

(required) Model name of processor.

`cores_per_socket`

(required) Number of cores per socket.

`total_sockets`

(required) Number of total sockets.

`threads_per_socket`

(required) Number of threads per socket.

`is_hyper_threading_enabled`

(required) Indicates if hyper-threading is enabled or not

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_HOST_CONFIGURATION_SUMMARY_T Type

Configuration summary of a EM Managed External host.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_host_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_summary_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`exadata_details`

(required)

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_T Type

Host insight resource.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the host entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'EM_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST', 'PE_COMANAGED_HOST'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`host_name`

(required) The host name. The host name is unique amongst the hosts managed by the same management agent.

`host_display_name`

(optional) The user-friendly name for the host. The name does not have to be unique.

`host_type`

(optional) Operations Insights internal representation of the host type. Possible value is EXTERNAL-HOST.

`processor_count`

(optional) Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`status`

(required) Indicates the status of a host insight in Operations Insights

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`time_created`

(required) The time the the host insight was first enabled. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the host insight was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the host.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_HOST_INSIGHT_T Type

EM-managed external host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_host_insight_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`enterprise_manager_entity_display_name`

(optional) Enterprise Manager Entity Display Name

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`platform_name`

(optional) Platform name.

`platform_version`

(optional) Platform version.

`exadata_insight_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_SUMMARY_T Type

Summary of a host insight resource.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the host entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'EM_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST', 'PE_COMANAGED_HOST'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`host_name`

(required) The host name. The host name is unique amongst the hosts managed by the same management agent.

`host_display_name`

(optional) The user-friendly name for the host. The name does not have to be unique.

`host_type`

(optional) Operations Insights internal representation of the host type. Possible value is EXTERNAL-HOST.

`processor_count`

(optional) Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`status`

(optional) Indicates the status of a host insight in Operations Insights

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`time_created`

(optional) The time the the host insight was first enabled. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the host insight was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the host.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_HOST_INSIGHT_SUMMARY_T Type

Summary of an EM-managed external host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_em_managed_external_host_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_summary_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`enterprise_manager_entity_display_name`

(optional) Enterprise Manager Entity Display Name

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`exadata_insight_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

### DBMS_CLOUD_OCI_OPSI_ENABLE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES_DETAILS_T Type

The advanced feature details for autonomous database to be enabled.

Syntax
```

```

Fields

Field Description

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`connection_details`

(required)

`credential_details`

(required)

### DBMS_CLOUD_OCI_OPSI_ENABLE_DATABASE_INSIGHT_DETAILS_T Type

The information about database to be analyzed.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the database entity.

Allowed values are: 'EM_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE'

### DBMS_CLOUD_OCI_OPSI_ENABLE_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type

The information about database to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_enable_em_managed_external_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_database_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_ENABLE_EXADATA_INSIGHT_DETAILS_T Type

The information about the Exadata system to be analyzed.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the Exadata system.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

### DBMS_CLOUD_OCI_OPSI_ENABLE_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_DETAILS_T Type

The information about the Exadata system to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_enable_em_managed_external_exadata_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_exadata_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_ENABLE_HOST_INSIGHT_DETAILS_T Type

The information about the host to be analyzed.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the host entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'EM_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST', 'PE_COMANAGED_HOST'

### DBMS_CLOUD_OCI_OPSI_ENABLE_EM_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type

The information about the EM-managed external host to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_enable_em_managed_external_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_host_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_ENABLE_MACS_MANAGED_CLOUD_HOST_INSIGHT_DETAILS_T Type

The information about the MACS-managed external host to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_enable_macs_managed_cloud_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_host_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_ENABLE_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type

The information about the MACS-managed external host to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_enable_macs_managed_external_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_host_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_ENABLE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type

The information about database to be analyzed.

Syntax
```

```

`dbms_cloud_oci_opsi_enable_pe_comanaged_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_database_insight_details_t`type.

Fields

Field Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Private service accessed database.

`opsi_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`service_name`

(required) Database service name used for connection requests.

`credential_details`

(required)

`connection_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPSI_ENABLE_PE_COMANAGED_EXADATA_INSIGHT_DETAILS_T Type

The information about the Exadata system to be analyzed. (ExaCS)

Syntax
```

```

`dbms_cloud_oci_opsi_enable_pe_comanaged_exadata_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_enable_exadata_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_T Type

Enterprise Manager bridge resource.

Syntax
```

```

Fields

Field Description

`id`

(required) Enterprise Manager bridge identifier

`compartment_id`

(required) Compartment identifier of the Enterprise Manager bridge

`display_name`

(required) User-friedly name of Enterprise Manager Bridge that does not have to be unique.

`description`

(optional) Description of Enterprise Manager Bridge

`object_storage_namespace_name`

(required) Object Storage Namespace Name

`object_storage_bucket_name`

(required) Object Storage Bucket Name

`object_storage_bucket_status_details`

(optional) A message describing status of the object storage bucket of this resource. For example, it can be used to provide actionable information about the permission and content validity of the bucket.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time the the Enterprise Manager bridge was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Enterprise Manager bridge was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Enterprise Manager bridge.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_SUMMARY_T Type

Summary of a Enterprise Manager bridge resource.

Syntax
```

```

Fields

Field Description

`id`

(required) Enterprise Manager bridge identifier

`compartment_id`

(required) Compartment identifier of the Enterprise Manager bridge

`display_name`

(required) User-friedly name of Enterprise Manager Bridge that does not have to be unique.

`object_storage_namespace_name`

(required) Object Storage Namespace Name

`object_storage_bucket_name`

(required) Object Storage Bucket Name

`object_storage_bucket_status_details`

(optional) A message describing status of the object storage bucket of this resource. For example, it can be used to provide actionable information about the permission and content validity of the bucket.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time the the Enterprise Manager bridge was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Enterprise Manager bridge was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Enterprise Manager bridge.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_enterprise_manager_bridge_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_COLLECTION_T Type

Collection of Enterprose Manager bridge summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Enterprose Manager bridge summary objects.

### DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGES_T Type

Logical grouping used for Operations Insights Enterprise Manager Bridge operations.

Syntax
```

```

Fields

Field Description

`enterprise_manager_bridges`

(optional) Enterprise Manager Bridge Object.

### DBMS_CLOUD_OCI_OPSI_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OPSI_VM_CLUSTER_SUMMARY_T Type

Partial information about the VM Cluster which includes name, memory allocated etc.

Syntax
```

```

Fields

Field Description

`vmcluster_name`

(required) The name of the vm cluster.

`memory_allocated_in_g_bs`

(optional) The memory allocated on a vm cluster.

`cpu_allocated`

(optional) The cpu allocated on a vm cluster.

`db_nodes_count`

(optional) The number of DB nodes on a vm cluster.

### DBMS_CLOUD_OCI_OPSI_VM_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_vm_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_CONFIGURATION_SUMMARY_T Type

Summary of a exadata configuration for a resource.

Syntax
```

```

Fields

Field Description

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`entity_source`

(required) Source of the exadata entity.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`exadata_name`

(required) The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.

`exadata_display_name`

(required) The user-friendly name for the Exadata system. The name does not have to be unique.

`exadata_type`

(required) Operations Insights internal representation of the the Exadata system type.

Allowed values are: 'DBMACHINE', 'EXACS', 'EXACC'

`exadata_rack_type`

(required) Exadata rack type.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH', 'FLEX'

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`vmcluster_details`

(optional) Array of objects containing VM cluster information.

### DBMS_CLOUD_OCI_OPSI_EXADATA_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_CONFIGURATION_COLLECTION_T Type

Collection of exadata insight configuration summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of exadata insight configurations summary objects.

### DBMS_CLOUD_OCI_OPSI_EXADATA_DATABASE_MACHINE_CONFIGURATION_SUMMARY_T Type

Configuration summary of a database machine.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_database_machine_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_configuration_summary_t`type.

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_bridge_id`

(required) OPSI Enterprise Manager Bridge OCID

### DBMS_CLOUD_OCI_OPSI_INSTANCE_METRICS_T Type

Object containing instance metrics.

Syntax
```

```

Fields

Field Description

`host_name`

(optional) The hostname of the database insight resource.

`instance_name`

(optional) The instance name of the database insight resource.

`usage`

(optional) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(optional) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

`utilization_percent`

(optional) Resource utilization in percentage

`usage_change_percent`

(optional) Change in resource utilization in percentage

### DBMS_CLOUD_OCI_OPSI_INSTANCE_METRICS_TBL Type

Nested table type of dbms_cloud_oci_opsi_instance_metrics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_T Type

Contains resource statistics with usage unit

Syntax
```

```

Fields

Field Description

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

`utilization_percent`

(required) Resource utilization in percentage

`usage_change_percent`

(required) Change in resource utilization in percentage

`instance_metrics`

(optional) Array of instance metrics

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_T Type

Contains resource details and current statistics

Syntax
```

```

Fields

Field Description

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

### DBMS_CLOUD_OCI_OPSI_EXADATA_DATABASE_STATISTICS_SUMMARY_T Type

Database details and statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_database_statistics_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_resource_statistics_aggregation_t`type.

Fields

Field Description

`resource_details`

(required)

`current_statistics`

(required)

### DBMS_CLOUD_OCI_OPSI_EXADATA_DISKGROUP_STATISTICS_SUMMARY_T Type

Diskgroup details and statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_diskgroup_statistics_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_resource_statistics_aggregation_t`type.

Fields

Field Description

`resource_details`

(required)

`current_statistics`

(required)

### DBMS_CLOUD_OCI_OPSI_EXADATA_EXACS_CONFIGURATION_SUMMARY_T Type

Configuration summary of a Exacs exadata machine.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_exacs_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_configuration_summary_t`type.

Fields

Field Description

`opsi_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`parent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

### DBMS_CLOUD_OCI_OPSI_HOST_DETAILS_T Type

Partial information about a host which includes id, name, type.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`host_name`

(required) The host name. The host name is unique amongst the hosts managed by the same management agent.

`host_display_name`

(optional) The user-friendly name for the host. The name does not have to be unique.

`platform_type`

(required) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`agent_identifier`

(required) The identifier of the agent.

### DBMS_CLOUD_OCI_OPSI_EXADATA_HOST_STATISTICS_SUMMARY_T Type

Host details and statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_host_statistics_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_resource_statistics_aggregation_t`type.

Fields

Field Description

`resource_details`

(required)

`current_statistics`

(required)

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type

Resource Capacity samples

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_insight_resource_capacity_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_SUMMARY_T Type

List of resource id, name , capacity time series data

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`name`

(required) The name of the resource.

`capacity_data`

(required) Time series data for capacity

### DBMS_CLOUD_OCI_OPSI_HISTORICAL_DATA_ITEM_T Type

The historical timestamp and the corresponding resource value.

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

### DBMS_CLOUD_OCI_OPSI_PROJECTED_DATA_ITEM_T Type

The timestamp of the projected event and their corresponding resource value. `highValue` and `lowValue` are the uncertainty bounds of the corresponding value.

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`high_value`

(required) Upper uncertainty bound of the current usage value.

`low_value`

(required) Lower uncertainty bound of the current usage value.

### DBMS_CLOUD_OCI_OPSI_HISTORICAL_DATA_ITEM_TBL Type

Nested table type of dbms_cloud_oci_opsi_historical_data_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_PROJECTED_DATA_ITEM_TBL Type

Nested table type of dbms_cloud_oci_opsi_projected_data_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_SUMMARY_T Type

List of resource id, name , capacity insight value, pattern, historical usage and projected data.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`name`

(required) The name of the resource.

`days_to_reach_capacity`

(required) Days to reach capacity for a storage server

`selected_forecast_algorithm`

(optional) Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.

`pattern`

(required) Time series patterns used in the forecasting.

Allowed values are: 'LINEAR', 'MONTHLY_SEASONS', 'MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_SEASONS', 'WEEKLY_AND_MONTHLY_SEASONS', 'WEEKLY_MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_AND_YEARLY_SEASONS', 'YEARLY_SEASONS'

`historical_data`

(required) Time series data used for the forecast analysis.

`projected_data`

(required) Time series data result of the forecasting analysis.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_INSIGHT_UTILIZATION_ITEM_T Type

Object containing current utilization, projected utilization, id and daysToReach high and low utilization value.

Syntax
```

```

Fields

Field Description

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`exadata_display_name`

(optional) The user-friendly name for the Exadata system. The name does not have to be unique.

`current_utilization`

(required) Current utilization

`projected_utilization`

(required) Projected utilization

`days_to_reach_high_utilization`

(required) Days to reach projected high utilization

`days_to_reach_low_utilization`

(required) Days to reach projected low utilization

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_insight_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_SUMMARY_COLLECTION_T Type

Collection of Exadata insight summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Exadata insight summary objects.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHTS_T Type

Logical grouping used for Operations Insights Exadata related operations.

Syntax
```

```

Fields

Field Description

`exadata_insights`

(optional) Exadata Insights Object.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHTS_DATA_OBJECT_T Type

Exadata insights data object.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_insights_data_object_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_t`type.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHTS_DATA_OBJECT_SUMMARY_T Type

Summary of an exadata insights data object.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_insights_data_object_summary_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_summary_t`type.

### DBMS_CLOUD_OCI_OPSI_EXADATA_MEMBER_SUMMARY_T Type

Lists name, display name and type of exadata member.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of exadata member target

`display_name`

(required) Display Name of exadata member target

`entity_type`

(required) Entity type of exadata member target

Allowed values are: 'DATABASE', 'ILOM_SERVER', 'PDU', 'STORAGE_SERVER', 'CLUSTER_ASM', 'INFINIBAND_SWITCH', 'ETHERNET_SWITCH', 'HOST', 'VM_CLUSTER'

### DBMS_CLOUD_OCI_OPSI_EXADATA_MEMBER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_member_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_EXADATA_MEMBER_COLLECTION_T Type

Partial definition of the exadata insight resource.

Syntax
```

```

Fields

Field Description

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`exadata_name`

(required) The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.

`exadata_display_name`

(required) The user-friendly name for the Exadata system. The name does not have to be unique.

`exadata_type`

(required) Operations Insights internal representation of the the Exadata system type.

Allowed values are: 'DBMACHINE', 'EXACS', 'EXACC'

`exadata_rack_type`

(required) Exadata rack type.

Allowed values are: 'FULL', 'HALF', 'QUARTER', 'EIGHTH', 'FLEX'

`items`

(required) Collection of Exadata members

### DBMS_CLOUD_OCI_OPSI_STORAGE_SERVER_DETAILS_T Type

Partial information about a storage server which includes name and displayName.

Syntax
```

```

Fields

Field Description

`storage_server_name`

(required) The storage server name.

`storage_server_display_name`

(required) The user-friendly name for the storage server. The name does not have to be unique.

### DBMS_CLOUD_OCI_OPSI_EXADATA_STORAGE_SERVER_STATISTICS_SUMMARY_T Type

Storage server details and statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_exadata_storage_server_statistics_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_resource_statistics_aggregation_t`type.

Fields

Field Description

`resource_details`

(required)

`current_statistics`

(required)

### DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_COLLECTION_T Type

Collection of host insight configuration summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of host insight configurations summary objects.

### DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_METRIC_GROUP_T Type

Base Metric Group for Host configuration metrics

Syntax
```

```

Fields

Field Description

`metric_name`

(required) Name of the metric group

Allowed values are: 'HOST_PRODUCT', 'HOST_RESOURCE_ALLOCATION', 'HOST_MEMORY_CONFIGURATION', 'HOST_HARDWARE_CONFIGURATION', 'HOST_CPU_HARDWARE_CONFIGURATION', 'HOST_NETWORK_CONFIGURATION', 'HOST_ENTITES', 'HOST_FILESYSTEM_CONFIGURATION'

`time_collected`

(required) Collection timestamp Example: `\"2020-05-06T00:00:00.000Z\"`

### DBMS_CLOUD_OCI_OPSI_HOST_CPU_HARDWARE_CONFIGURATION_T Type

CPU Hardware Configuration metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_cpu_hardware_configuration_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`total_sockets`

(optional) Total number of CPU Sockets

`vendor_name`

(optional) Name of the CPU vendor

`frequency_in_mhz`

(optional) Clock frequency of the processor in megahertz

`cache_in_mb`

(optional) Size of cache memory in megabytes

`cpu_implementation`

(optional) Model name of processor

`model`

(optional) CPU model

`cpu_family`

(optional) Type of processor in the system

`cores_per_socket`

(optional) Number of cores per socket

`threads_per_socket`

(optional) Number of threads per socket

`hyper_threading_enabled`

(optional) Indicates if hyper-threading is enabled or not

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_HOST_RECOMMENDATIONS_T Type

Contains recommendations depending of resource metric received.

Syntax
```

```

Fields

Field Description

`metric_recommendation_name`

(required) Name of recommendations depending of resource metric received.

Allowed values are: 'HOST_CPU_RECOMMENDATIONS'

### DBMS_CLOUD_OCI_OPSI_HOST_CPU_RECOMMENDATIONS_T Type

Contains CPU recommendation.

Syntax
```

```

`dbms_cloud_oci_opsi_host_cpu_recommendations_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_host_recommendations_t`type.

Fields

Field Description

`burstable`

(optional) Show if OPSI recommend to convert an instance to a burstable instance and show recommended cpu baseline if positive recommendation.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'NO_RECOMMENDATION', 'DISABLE_BURSTABLE'

### DBMS_CLOUD_OCI_OPSI_SUMMARY_STATISTICS_T Type

Contains common summary statistics.

Syntax
```

```

Fields

Field Description

`minimum`

(required) The smallest number in the data set.

`maximum`

(required) The largest number in the data set.

`average`

(required) The average number in the data set.

`median`

(required) The middle number in the data set.

`lower_quartile`

(required) The middle number between the smallest number and the median of the data set. It's also known as the 25th quartile.

`upper_quartile`

(required) The middle number between the median and the largest number of the data set. It's also known as the 75th quartile.

### DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_STATISTICS_T Type

Contains host resource base statistics.

Syntax
```

```

Fields

Field Description

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`utilization_percent`

(required) Resource utilization in percentage.

`usage_change_percent`

(required) Change in resource utilization in percentage

`resource_name`

(required) Name of resource for host

Allowed values are: 'HOST_CPU_STATISTICS', 'HOST_MEMORY_STATISTICS', 'HOST_STORAGE_STATISTICS', 'HOST_NETWORK_STATISTICS'

### DBMS_CLOUD_OCI_OPSI_HOST_CPU_STATISTICS_T Type

Contains CPU statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_host_cpu_statistics_t`is a subtype of the`dbms_cloud_oci_opsi_host_resource_statistics_t`type.

Fields

Field Description

`cpu_baseline`

(optional) The baseline utilization is a fraction of each CPU core expressed in percentages, either 12.5% or 50%. The baseline provides the minimum CPUs that can be used constantly.

`load`

(optional)

### DBMS_CLOUD_OCI_OPSI_HOST_PERFORMANCE_METRIC_GROUP_T Type

Base Metric Group for Host performance metrics

Syntax
```

```

Fields

Field Description

`metric_name`

(required) Name of the metric group

Allowed values are: 'HOST_CPU_USAGE', 'HOST_MEMORY_USAGE', 'HOST_NETWORK_ACTIVITY_SUMMARY', 'HOST_TOP_PROCESSES', 'HOST_FILESYSTEM_USAGE'

`time_collected`

(required) Collection timestamp Example: `\"2020-05-06T00:00:00.000Z\"`

### DBMS_CLOUD_OCI_OPSI_HOST_CPU_USAGE_T Type

CPU Usage metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_cpu_usage_t`is a subtype of the`dbms_cloud_oci_opsi_host_performance_metric_group_t`type.

Fields

Field Description

`cpu_user_mode_in_percent`

(optional) Percentage of CPU time spent in user mode

`cpu_system_mode_in_percent`

(optional) Percentage of CPU time spent in system mode

`cpu_usage_in_sec`

(optional) Amount of CPU Time spent in seconds

`cpu_utilization_in_percent`

(optional) Amount of CPU Time spent in percentage

`cpu_stolen_in_percent`

(optional) Amount of CPU time stolen in percentage

`cpu_idle_in_percent`

(optional) Amount of CPU idle time in percentage

`cpu_load1min`

(optional) Load average in the last 1 minute

`cpu_load5min`

(optional) Load average in the last 5 minutes

`cpu_load15min`

(optional) Load average in the last 15 minutes

### DBMS_CLOUD_OCI_OPSI_HOST_ENTITIES_T Type

Database entities running on the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_entities_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`entity_name`

(required) Name of the database entity

`entity_type`

(required) Type of the database entity

### DBMS_CLOUD_OCI_OPSI_HOST_FILESYSTEM_CONFIGURATION_T Type

Filesystem Configuration metric for the host.

Syntax
```

```

`dbms_cloud_oci_opsi_host_filesystem_configuration_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`file_system_name`

(required) Name of filesystem

`mount_point`

(required) Mount points are specialized NTFS filesystem objects

`file_system_size_in_gb`

(required) Size of filesystem

### DBMS_CLOUD_OCI_OPSI_HOST_FILESYSTEM_USAGE_T Type

Filesystem Usage metric for the host.

Syntax
```

```

`dbms_cloud_oci_opsi_host_filesystem_usage_t`is a subtype of the`dbms_cloud_oci_opsi_host_performance_metric_group_t`type.

Fields

Field Description

`mount_point`

(optional) Mount points are specialized NTFS filesystem objects

`file_system_usage_in_gb`

(optional)

`file_system_avail_in_percent`

(optional)

### DBMS_CLOUD_OCI_OPSI_HOST_HARDWARE_CONFIGURATION_T Type

Hardware Configuration metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_hardware_configuration_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`cpu_architecture`

(required) Processor architecture used by the platform

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_AGENT_ENTITY_SUMMARY_T Type

An agent entity that can be imported into Operations Insights.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the importable agent entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST'

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`management_agent_display_name`

(required) The[Display Name](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display)of the Management Agent

### DBMS_CLOUD_OCI_OPSI_HOST_IMPORTABLE_AGENT_ENTITY_SUMMARY_T Type

An agent host entity that can be imported into Operations Insights.

Syntax
```

```

`dbms_cloud_oci_opsi_host_importable_agent_entity_summary_t`is a subtype of the`dbms_cloud_oci_opsi_importable_agent_entity_summary_t`type.

Fields

Field Description

`host_name`

(required) The host name. The host name is unique amongst the hosts managed by the same management agent.

`platform_type`

(required) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_T Type

Contains host details and resource statistics.

Syntax
```

```

Fields

Field Description

`host_details`

(required)

`current_statistics`

(required)

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_insight_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_SUMMARY_COLLECTION_T Type

Collection of host insight summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of host insight summary objects.

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHTS_T Type

Logical grouping used for Operations Insights host related operations.

Syntax
```

```

Fields

Field Description

`host_insights`

(optional) Host Insights Object.

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHTS_DATA_OBJECT_T Type

Host insights data object.

Syntax
```

```

`dbms_cloud_oci_opsi_host_insights_data_object_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_t`type.

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHTS_DATA_OBJECT_SUMMARY_T Type

Summary of a host insights data object.

Syntax
```

```

`dbms_cloud_oci_opsi_host_insights_data_object_summary_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_summary_t`type.

### DBMS_CLOUD_OCI_OPSI_HOST_MEMORY_CONFIGURATION_T Type

Memory Configuration metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_memory_configuration_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`page_size_in_kb`

(optional) Page size in kilobytes

`page_tables_in_kb`

(optional) Amount of memory used for page tables in kilobytes

`swap_total_in_kb`

(optional) Amount of total swap space in kilobytes

`huge_page_size_in_kb`

(optional) Size of huge pages in kilobytes

`huge_pages_total`

(optional) Total number of huge pages

### DBMS_CLOUD_OCI_OPSI_HOST_MEMORY_STATISTICS_T Type

Contains memory statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_host_memory_statistics_t`is a subtype of the`dbms_cloud_oci_opsi_host_resource_statistics_t`type.

Fields

Field Description

`free_memory`

(optional)

`available_memory`

(optional)

`huge_pages_total`

(optional) Total number of huge pages.

`huge_page_size_in_mb`

(optional) Size of huge pages in megabytes.

`huge_pages_free`

(optional) Total number of available huge pages.

`huge_pages_reserved`

(optional) Total number of huge pages which are used or reserved.

`load`

(optional)

### DBMS_CLOUD_OCI_OPSI_HOST_MEMORY_USAGE_T Type

Memory usage metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_memory_usage_t`is a subtype of the`dbms_cloud_oci_opsi_host_performance_metric_group_t`type.

Fields

Field Description

`memory_used_in_gb`

(optional) Amount of physical memory used in gigabytes

`memory_utilization_in_percent`

(optional) Amount of physical memory used in percentage

`memory_load_in_gb`

(optional) Load on memory in gigabytes

`real_memory_in_kb`

(optional) Amount of usable physical memory in kilobytes

`free_memory_in_kb`

(optional) Amount of available physical memory in kilobytes

`logical_memory_used_in_gb`

(optional) Memory used excluding buffers and cache in gigabytes

`logical_memory_utilization_in_percent`

(optional) Amount of logical memory used in percentage

`free_logical_memory_in_kb`

(optional) Amount of avaiable virtual memory in kilobytes

`major_page_faults`

(optional) Number of major page faults

`swap_free_in_kb`

(optional) Amount of available swap space in kilobytes

`anon_huge_pages_in_kb`

(optional) Amount of memory used for anon huge pages in kilobytes

`huge_pages_free`

(optional) Number of available huge pages

`huge_pages_reserved`

(optional) Number of reserved huge pages

`huge_pages_surplus`

(optional) Number of surplus huge pages

### DBMS_CLOUD_OCI_OPSI_HOST_NETWORK_ACTIVITY_SUMMARY_T Type

Network Activity Summary metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_network_activity_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_performance_metric_group_t`type.

Fields

Field Description

`interface_name`

(optional) Name of the network interface

`all_network_read_in_mbps`

(optional) All network interfaces read rate in Mbps

`all_network_write_in_mbps`

(optional) All network interfaces write rate in Mbps

`all_network_io_in_mbps`

(optional) All network interfaces IO rate in Mbps

### DBMS_CLOUD_OCI_OPSI_HOST_NETWORK_CONFIGURATION_T Type

Network Configuration metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_network_configuration_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`interface_name`

(required) Name of the network interface

`ip_address`

(required) IP address (IPv4 or IPv6) of the network interface

`mac_address`

(optional) MAC address of the network interface. MAC address is a 12-digit hexadecimal number separated by colons or dashes or dots. Following formats are accepted: MM:MM:MM:SS:SS:SS, MM-MM-MM-SS-SS-SS, MM.MM.MM.SS.SS.SS, MMM:MMM:SSS:SSS, MMM-MMM-SSS-SSS, MMM.MMM.SSS.SSS, MMMM:MMSS:SSSS, MMMM-MMSS-SSSS, MMMM.MMSS.SSSS

### DBMS_CLOUD_OCI_OPSI_HOST_NETWORK_STATISTICS_T Type

Contains network statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_host_network_statistics_t`is a subtype of the`dbms_cloud_oci_opsi_host_resource_statistics_t`type.

Fields

Field Description

`network_read_in_m_bs`

(optional)

`network_write_in_m_bs`

(optional)

### DBMS_CLOUD_OCI_OPSI_HOST_PRODUCT_T Type

Product metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_product_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`vendor`

(optional) Vendor of the product

`name`

(optional) Name of the product

`version`

(optional) Version of the product

### DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_ALLOCATION_T Type

Resource Allocation metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_resource_allocation_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_metric_group_t`type.

Fields

Field Description

`total_cpus`

(optional) Total number of CPUs available

`total_memory_in_gb`

(optional) Total amount of usable physical memory in gibabytes

### DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type

Host Resource Capacity samples

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

### DBMS_CLOUD_OCI_OPSI_HOST_STORAGE_STATISTICS_T Type

Contains storage statistics.

Syntax
```

```

`dbms_cloud_oci_opsi_host_storage_statistics_t`is a subtype of the`dbms_cloud_oci_opsi_host_resource_statistics_t`type.

Fields

Field Description

`filesystem_available_in_percent`

(optional)

### DBMS_CLOUD_OCI_OPSI_HOST_TOP_PROCESSES_T Type

Top Processes metric for the host

Syntax
```

```

`dbms_cloud_oci_opsi_host_top_processes_t`is a subtype of the`dbms_cloud_oci_opsi_host_performance_metric_group_t`type.

Fields

Field Description

`pid`

(optional) process id

`user_name`

(optional) User that started the process

`memory_utilization_percent`

(optional) Memory utilization percentage

`cpu_utilization_percent`

(optional) CPU utilization percentage

`cpu_usage_in_seconds`

(optional) CPU usage in seconds

`command`

(optional) Command line executed for the process

`virtual_memory_in_m_bs`

(optional) Virtual memory in megabytes

`physical_memory_in_m_bs`

(optional) Physical memory in megabytes

`start_time`

(optional) Process Start Time Example: `\"2020-03-31T00:00:00.000Z\"`

`total_processes`

(optional) Number of processes running at the time of collection

### DBMS_CLOUD_OCI_OPSI_HOSTED_ENTITY_SUMMARY_T Type

Information about a hosted entity which includes identifier, name, and type.

Syntax
```

```

Fields

Field Description

`entity_identifier`

(required) The identifier of the entity.

`entity_name`

(required) The entity name.

`entity_type`

(required) The entity type.

### DBMS_CLOUD_OCI_OPSI_HOSTED_ENTITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_hosted_entity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_HOSTED_ENTITY_COLLECTION_T Type

Returns a list of hosted entities for the specific host.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) List of hosted entities details.

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_AGENT_ENTITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_importable_agent_entity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_AGENT_ENTITY_SUMMARY_COLLECTION_T Type

Collection of importable agent entity objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of importable agent entity objects.

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_importable_compute_entity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_COLLECTION_T Type

Collection of importable compute entity objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of importable compute entity objects.

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_ENTERPRISE_MANAGER_ENTITY_T Type

An Enterprise Manager entity that can be imported into Operations Insights.

Syntax
```

```

Fields

Field Description

`enterprise_manager_identifier`

(required) Enterprise Manager Unique Identifier

`enterprise_manager_entity_name`

(required) Enterprise Manager Entity Name

`enterprise_manager_entity_type`

(required) Enterprise Manager Entity Type

`enterprise_manager_entity_identifier`

(required) Enterprise Manager Entity Unique Identifier

`opsi_entity_type`

(optional) Operations Insights internal representation of the resource type.

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_ENTERPRISE_MANAGER_ENTITY_TBL Type

Nested table type of dbms_cloud_oci_opsi_importable_enterprise_manager_entity_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_IMPORTABLE_ENTERPRISE_MANAGER_ENTITY_COLLECTION_T Type

Collection of importable Enterprise Manager entity objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of importable Enterprise Manager entity objects.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_QUERY_PARAM_T Type

Details for a query parameter to be applied on an OPSI data object, when a data object query is executed.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the query parameter.

`value`

(required) Value for the query parameter.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_QUERY_PARAM_TBL Type

Nested table type of dbms_cloud_oci_opsi_opsi_data_object_query_param_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_T Type

Details for OPSI data object used in a data object query.

Syntax
```

```

Fields

Field Description

`data_object_details_target`

(required) Data objects to which this OpsiDataObjectDetailsInQuery is applicable.

Allowed values are: 'INDIVIDUAL_OPSIDATAOBJECT', 'OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS'

`query_params`

(optional) An array of query parameters to be applied, for the OPSI data objects targetted by dataObjectDetailsTarget, before executing the query. Refer to supportedQueryParams of OpsiDataObject for the supported query parameters.

### DBMS_CLOUD_OCI_OPSI_INDIVIDUAL_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_T Type

Details applicable for an individual OPSI data object used in a data object query.

Syntax
```

```

`dbms_cloud_oci_opsi_individual_opsi_data_object_details_in_query_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_details_in_query_t`type.

Fields

Field Description

`data_object_identifier`

(required) Unique OPSI data object identifier.

### DBMS_CLOUD_OCI_OPSI_ADDM_REPORT_TBL Type

Nested table type of dbms_cloud_oci_opsi_addm_report_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_ADDM_REPORTS_DETAILS_T Type

Collection of Addm reports

Syntax
```

```

Fields

Field Description

`items`

(required) List of Addm reports

### DBMS_CLOUD_OCI_OPSI_INGEST_ADDM_REPORTS_RESPONSE_DETAILS_T Type

The response object returned from IngestAddmReports operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_METRIC_GROUP_TBL Type

Nested table type of dbms_cloud_oci_opsi_database_configuration_metric_group_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_DATABASE_CONFIGURATION_DETAILS_T Type

Database Configuration Metrics details.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of one or more database configuration metrics objects.

### DBMS_CLOUD_OCI_OPSI_INGEST_DATABASE_CONFIGURATION_RESPONSE_DETAILS_T Type

The response object returned from IngestDatabaseConfiguration operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_METRIC_GROUP_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_configuration_metric_group_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_HOST_CONFIGURATION_DETAILS_T Type

Contains the data to ingest for one or more host configuration metrics

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of one or more host configuration metric data points

### DBMS_CLOUD_OCI_OPSI_INGEST_HOST_CONFIGURATION_RESPONSE_DETAILS_T Type

The response object returned from IngestHostConfiguration operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_HOST_PERFORMANCE_METRIC_GROUP_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_performance_metric_group_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_HOST_METRICS_DETAILS_T Type

Contains the data to ingest for one or more host performance metrics

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of one or more host performance metric data points

### DBMS_CLOUD_OCI_OPSI_INGEST_HOST_METRICS_RESPONSE_DETAILS_T Type

The response object returned from IngestHostMetrics operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_MY_SQL_SQL_TEXT_T Type

MySql SQL Text type object.

Syntax
```

```

Fields

Field Description

`schema_name`

(optional) Name of Database Schema. Example: `\"performance_schema\"`

`digest`

(required) digest Example: `\"323k3k99ua09a90adf\"`

`time_collected`

(required) Collection timestamp. Example: `\"2020-05-06T00:00:00.000Z\"`

`command_type`

(optional) SQL event name Example: `\"SELECT\"`

`digest_text`

(required) The normalized statement string. Example: `\"SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users\"`

### DBMS_CLOUD_OCI_OPSI_MY_SQL_SQL_TEXT_TBL Type

Nested table type of dbms_cloud_oci_opsi_my_sql_sql_text_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_MY_SQL_SQL_TEXT_DETAILS_T Type

Collection of SQL Text Entries

Syntax
```

```

Fields

Field Description

`items`

(optional) List of SQL Text Entries.

### DBMS_CLOUD_OCI_OPSI_INGEST_MY_SQL_SQL_TEXT_RESPONSE_DETAILS_T Type

The response object returned from IngestMySqlSqlTextDetails operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_SQL_BUCKET_T Type

Sql bucket type object.

Syntax
```

```

Fields

Field Description

`version`

(optional) Version Example: `1`

`database_type`

(optional) Operations Insights internal representation of the database type.

`time_collected`

(required) Collection timestamp Example: `\"2020-03-31T00:00:00.000Z\"`

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`plan_hash`

(required) Plan hash value for the SQL Execution Plan

`bucket_id`

(required) SQL Bucket ID, examples &lt;= 3 secs, 3-10 secs, 10-60 secs, 1-5 min, &gt; 5 min Example: `\"&lt;= 3 secs\"`

`executions_count`

(optional) Total number of executions Example: `60`

`cpu_time_in_sec`

(optional) Total CPU time Example: `1046`

`io_time_in_sec`

(optional) Total IO time Example: `5810`

`other_wait_time_in_sec`

(optional) Total other wait time Example: `24061`

`total_time_in_sec`

(optional) Total time Example: `30917`

### DBMS_CLOUD_OCI_OPSI_SQL_BUCKET_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_bucket_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_BUCKET_DETAILS_T Type

Collection of SQL Bucket Metric Entries

Syntax
```

```

Fields

Field Description

`items`

(optional) List of SQL Bucket Metric Entries.

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_BUCKET_RESPONSE_DETAILS_T Type

The response object returned from IngestSqlBucketDetails operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_LINE_T Type

SQL Plan Line type object.

Syntax
```

```

Fields

Field Description

`version`

(optional) Version Example: `1`

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`plan_hash`

(required) Plan hash value for the SQL Execution Plan

`time_collected`

(required) Collection time stamp Example: `\"2020-05-06T00:00:00.000Z\"`

`operation`

(required) Operation Example: `\"SELECT STATEMENT\"`

`remark`

(optional) Remark Example: `\"\"`

`options`

(optional) Options Example: `\"RANGE SCAN\"`

`object_node`

(optional) Object Node Example: `\"Q4000\"`

`object_owner`

(optional) Object Owner Example: `\"TENANT_A#SCHEMA\"`

`object_name`

(optional) Object Name Example: `\"PLAN_LINES_PK\"`

`object_alias`

(optional) Object Alias Example: `\"PLAN_LINES@SEL$1\"`

`object_instance`

(optional) Object Instance Example: `37472`

`object_type`

(optional) Object Type Example: `\"INDEX (UNIQUE)\"`

`optimizer`

(optional) Optimizer Example: `\"CLUSTER\"`

`search_columns`

(optional) Search Columns Example: `3`

`identifier`

(required) Identifier Example: `3`

`parent_identifier`

(optional) Parent Identifier Example: `2`

`depth`

(optional) Depth Example: `3`

`position`

(optional) Position Example: `1`

`cost`

(optional) Cost Example: `1`

`cardinality`

(optional) Cardinality Example: `1`

`bytes`

(optional) Bytes Example: `150`

`other`

(optional) Other Example: ``

`other_tag`

(optional) Other Tag Example: `\"PARALLEL_COMBINED_WITH_PARENT\"`

`partition_start`

(optional) Partition start Example: `1`

`partition_stop`

(optional) Partition stop Example: `2`

`partition_identifier`

(optional) Partition identifier Example: `8`

`distribution`

(optional) Distribution Example: `\"QC (RANDOM)\"`

`cpu_cost`

(optional) CPU cost Example: `7321`

`io_cost`

(optional) IO cost Example: `1`

`temp_space`

(optional) Time space Example: `15614000`

`access_predicates`

(optional) Access predicates Example: `\"\\\"RESOURCE_ID\\\"=:1 AND \\\"QUERY_ID\\\"=:2\"`

`filter_predicates`

(optional) Filter predicates Example: `\"(INTERNAL_FUNCTION(\\\"J\\\".\\\"DATABASE_ROLE\\\") OR (\\\"J\\\".\\\"DATABASE_ROLE\\\" IS NULL AND SYS_CONTEXT('userenv','database_role')='PRIMARY'))\"`

`projection`

(optional) Projection Example: `\"COUNT(*)[22]\"`

`qblock_name`

(optional) Qblock Name Example: `\"SEL$1\"`

`elapsed_time_in_sec`

(optional) Total elapsed time Example: `1.2`

`other_xml`

(optional) Other SQL Example: `\"&lt;other_xml&gt;&lt;info type=\\\"db_version\\\"&gt;18.0.0.0&lt;/info&gt;&lt;info type=\\\"parse_schema\\\"&gt;&lt;[CDATA[\\\"SYS\\\"]]&gt;&lt;/info&gt;&lt;info type=\\\"plan_hash_full\\\"&gt;483892784&lt;/info&gt;&lt;info type=\\\"plan_hash\\\"&gt;2709293936&lt;/info&gt;&lt;info type=\\\"plan_hash_2\\\"&gt;483892784&lt;/info&gt;&lt;outline_data&gt;&lt;hint&gt;&lt;[CDATA[IGNORE_OPTIM_EMBEDDED_HINTS]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[OPTIMIZER_FEATURES_ENABLE('18.1.0')]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[DB_VERSION('18.1.0')]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[OPT_PARAM('_b_tree_bitmap_plans' 'false')]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[OPT_PARAM('_optim_peek_user_binds' 'false')]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[OPT_PARAM('result_cache_mode' 'FORCE')]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[OPT_PARAM('_fix_control' '20648883:0 27745220:1 30001331:1 30142527:1 30539126:1')]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[OUTLINE_LEAF(@\\\"SEL$1\\\")]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;[CDATA[INDEX(@\\\"SEL$1\\\" \\\"USER$\\\"@\\\"SEL$1\\\" \\\"I_USER#\\\")]]&gt;&lt;/hint&gt;&lt;/outline_data&gt;&lt;/other_xml&gt;\"`

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_LINE_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_plan_line_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_PLAN_LINES_DETAILS_T Type

Collection of SQL Plan Line Entries

Syntax
```

```

Fields

Field Description

`items`

(optional) List of SQL Plan Line Entries.

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_PLAN_LINES_RESPONSE_DETAILS_T Type

The response object returned from IngestSqlPlanLines operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_SQL_STATS_T Type

Sql Stats type object.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`plan_hash_value`

(required) Plan hash value for the SQL Execution Plan

`time_collected`

(required) Collection timestamp Example: `\"2020-03-31T00:00:00.000Z\"`

`instance_name`

(required) Name of Database Instance Example: `\"DB10902_1\"`

`last_active_time`

(optional) last_active_time Example: `\"0000000099CCE300\"`

`parse_calls`

(optional) Total integer of parse calls Example: `60`

`disk_reads`

(optional) Number of disk reads

`direct_reads`

(optional) Number of direct reads

`direct_writes`

(optional) Number of Direct writes

`buffer_gets`

(optional) Number of Buffer Gets

`rows_processed`

(optional) Number of row processed

`serializable_aborts`

(optional) Number of serializable aborts

`fetches`

(optional) Number of fetches

`executions`

(optional) Number of executions

`avoided_executions`

(optional) Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine

`end_of_fetch_count`

(optional) Number of times this cursor was fully executed since the cursor was brought into the library cache

`loads`

(optional) Number of times the object was either loaded or reloaded

`version_count`

(optional) Number of cursors present in the cache with this SQL text and plan

`invalidations`

(optional) Number of times this child cursor has been invalidated

`obsolete_count`

(optional) Number of times that a parent cursor became obsolete

`px_servers_executions`

(optional) Total number of executions performed by parallel execution servers (0 when the statement has never been executed in parallel)

`cpu_time_in_us`

(optional) CPU time (in microseconds) used by this cursor for parsing, executing, and fetching

`elapsed_time_in_us`

(optional) Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching.

`avg_hard_parse_time_in_us`

(optional) Average hard parse time (in microseconds) used by this cursor

`concurrency_wait_time_in_us`

(optional) Concurrency wait time (in microseconds)

`application_wait_time_in_us`

(optional) Application wait time (in microseconds)

`cluster_wait_time_in_us`

(optional) Cluster wait time (in microseconds). This value is specific to Oracle RAC

`user_io_wait_time_in_us`

(optional) User I/O wait time (in microseconds)

`plsql_exec_time_in_us`

(optional) PL/SQL execution time (in microseconds)

`java_exec_time_in_us`

(optional) Java execution time (in microseconds)

`sorts`

(optional) Number of sorts that were done for the child cursor

`sharable_mem`

(optional) Total shared memory (in bytes) currently occupied by all cursors with this SQL text and plan

`total_sharable_mem`

(optional) Total shared memory (in bytes) occupied by all cursors with this SQL text and plan if they were to be fully loaded in the shared pool (that is, cursor size)

`type_check_mem`

(optional) Typecheck memory

`io_cell_offload_eligible_bytes`

(optional) Number of I/O bytes which can be filtered by the Exadata storage system

`io_interconnect_bytes`

(optional) Number of I/O bytes exchanged between Oracle Database and the storage system. Typically used for Cache Fusion or parallel queries

`physical_read_requests`

(optional) Number of physical read I/O requests issued by the monitored SQL. The requests may not be disk reads

`physical_read_bytes`

(optional) Number of bytes read from disks by the monitored SQL

`physical_write_requests`

(optional) Number of physical write I/O requests issued by the monitored SQL

`physical_write_bytes`

(optional) Number of bytes written to disks by the monitored SQL

`exact_matching_signature`

(optional) exact_matching_signature Example: `\"18067345456756876713\"`

`force_matching_signature`

(optional) force_matching_signature Example: `\"18067345456756876713\"`

`io_cell_uncompressed_bytes`

(optional) Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells

`io_cell_offload_returned_bytes`

(optional) Number of bytes that are returned by Exadata cell through the regular I/O path

`child_number`

(optional) Number of this child cursor

`command_type`

(optional) Oracle command type definition

`users_opening`

(optional) Number of users that have any of the child cursors open

`users_executing`

(optional) Number of users executing the statement

`optimizer_cost`

(optional) Cost of this query given by the optimizer

`full_plan_hash_value`

(optional) Total Number of rows in SQLStats table

`module`

(optional) Module name

`service`

(optional) Service name

`action`

(optional) Contains the name of the action that was executing when the SQL statement was first parsed, which is set by calling DBMS_APPLICATION_INFO.SET_ACTION

`sql_profile`

(optional) SQL profile used for this statement, if any

`sql_patch`

(optional) SQL patch used for this statement, if any

`sql_plan_baseline`

(optional) SQL plan baseline used for this statement, if any

`delta_execution_count`

(optional) Number of executions for the cursor since the last AWR snapshot

`delta_cpu_time`

(optional) CPU time (in microseconds) for the cursor since the last AWR snapshot

`delta_io_bytes`

(optional) Number of I/O bytes exchanged between the Oracle database and the storage system for the cursor since the last AWR snapshot

`delta_cpu_rank`

(optional) Rank based on CPU Consumption

`delta_execs_rank`

(optional) Rank based on number of execution

`sharable_mem_rank`

(optional) Rank based on sharable memory

`delta_io_rank`

(optional) Rank based on I/O Consumption

`harmonic_sum`

(optional) Harmonic sum based on ranking parameters

`wt_harmonic_sum`

(optional) Weight based harmonic sum of ranking parameters

`total_sql_count`

(optional) Total number of rows in SQLStats table

### DBMS_CLOUD_OCI_OPSI_SQL_STATS_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_stats_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_STATS_DETAILS_T Type

Collection of SQL Stats Metric Entries

Syntax
```

```

Fields

Field Description

`items`

(optional) List of SQL Stats Metric Entries.

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_STATS_RESPONSE_DETAILS_T Type

The response object returned from IngestSqlStats operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_SQL_TEXT_T Type

SQL Text type object.

Syntax
```

```

Fields

Field Description

`version`

(optional) Version Example: `1`

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`time_collected`

(required) Collection timestamp Example: `\"2020-05-06T00:00:00.000Z\"`

`sql_command`

(required) SQL command Example: `\"SELECT\"`

`exact_matching_signature`

(optional) Exact matching signature Example: `\"18067345456756876713\"`

`force_matching_signature`

(optional) Force matching signature Example: `\"18067345456756876713\"`

`sql_full_text`

(required) Full SQL Text Example: `\"SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users\"` Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.

### DBMS_CLOUD_OCI_OPSI_SQL_TEXT_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_text_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_TEXT_DETAILS_T Type

Collection of SQL Text Entries

Syntax
```

```

Fields

Field Description

`items`

(optional) List of SQL Text Entries.

### DBMS_CLOUD_OCI_OPSI_INGEST_SQL_TEXT_RESPONSE_DETAILS_T Type

The response object returned from IngestSqlTextDetails operation.

Syntax
```

```

Fields

Field Description

`message`

(required) Success message returned as a result of the upload.

### DBMS_CLOUD_OCI_OPSI_OBJECT_SUMMARY_T Type

Summary resource object.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the Awr Hub object.

`l_size`

(optional) Size of the Awr Hub object in bytes.

`md5`

(optional) Base64-encoded MD5 hash of the Awr Hub object data.

`time_created`

(optional) The time at which the resource was first created. An RFC3339 formatted datetime string

`etag`

(optional) For optimistic concurrency control. See `if-match`.

`storage_tier`

(optional) The object's storage tier.

Allowed values are: 'STANDARD', 'INFREQUENTACCESS', 'ARCHIVE'

`archival_state`

(optional) Archival state of an object for those in the archival tier.

Allowed values are: 'ARCHIVED', 'RESTORING', 'RESTORED'

`time_modified`

(optional) The date and time the Awr Hub object was modified

### DBMS_CLOUD_OCI_OPSI_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_LIST_OBJECTS_T Type

List of the objects.

Syntax
```

```

Fields

Field Description

`prefixes`

(optional) Array comprising of all the prefixes.

`next_start_with`

(optional) Object names returned by a list query must be greater or equal to this parameter.

`objects`

(required) List of the object summary data.

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_CLOUD_HOST_CONFIGURATION_SUMMARY_T Type

Configuration Summary of a Macs Managed Cloud host.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_cloud_host_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_summary_t`type.

Fields

Field Description

`compute_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Compute Instance

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of External Database Connector

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_CLOUD_HOST_INSIGHT_T Type

MACS-managed OCI Compute host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_cloud_host_insight_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_t`type.

Fields

Field Description

`compute_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Compute Instance

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`platform_name`

(optional) Platform name.

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`platform_version`

(optional) Platform version.

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_CLOUD_HOST_INSIGHT_SUMMARY_T Type

Summary of a MACS-managed cloud host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_cloud_host_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_summary_t`type.

Fields

Field Description

`compute_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Compute Instance

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_DATABASE_CONFIGURATION_SUMMARY_T Type

Configuration Summary of a Macs Managed External database.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_external_database_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_summary_t`type.

Fields

Field Description

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of External Database Connector

`instances`

(required) Array of hostname and instance name.

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_DATABASE_INSIGHT_T Type

Database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_external_database_insight_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_t`type.

Fields

Field Description

`management_agent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of External Database Connector

`connection_details`

(optional)

`connection_credential_details`

(optional)

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`database_name`

(required) Name of database

`database_display_name`

(optional) Display name of database

`database_resource_type`

(required) OCI database resource type

`db_additional_details`

(optional) Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty string. Note that this string needs to be escaped when specified in the curl command.

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_DATABASE_INSIGHT_SUMMARY_T Type

Summary of a database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_external_database_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_summary_t`type.

Fields

Field Description

`database_resource_type`

(optional) OCI database resource type

`management_agent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of External Database Connector

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_HOST_CONFIGURATION_SUMMARY_T Type

Configuration Summary of a Macs Managed External host.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_external_host_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_summary_t`type.

Fields

Field Description

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of External Database Connector

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_T Type

MACS-managed external host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_external_host_insight_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_t`type.

Fields

Field Description

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`platform_name`

(optional) Platform name.

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`platform_version`

(optional) Platform version.

### DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_SUMMARY_T Type

Summary of a MACS-managed external host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_macs_managed_external_host_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_summary_t`type.

Fields

Field Description

`management_agent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Management Agent

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

### DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_T Type

Usage data samples.

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`all_network_read_in_mbps`

(required) Network read in Mbps.

`all_network_write_in_mbps`

(required) Network write in Mbps.

`all_network_io_in_mbps`

(required) Network input/output in Mbps.

### DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_TBL Type

Nested table type of dbms_cloud_oci_opsi_network_usage_trend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_AGGREGATION_T Type

Usage data per network interface.

Syntax
```

```

Fields

Field Description

`interface_name`

(required) Name of interface.

`ip_address`

(required) Address that is connected to a computer network that uses the Internet Protocol for communication.

`mac_address`

(required) Unique identifier assigned to a network interface.

`usage_data`

(required) List of usage data samples for a network interface.

### DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_T Type

News report resource.

Syntax
```

```

Fields

Field Description

`news_frequency`

(required) News report frequency.

Allowed values are: 'WEEKLY'

`content_types`

(required)

`locale`

(optional) Language of the news report.

Allowed values are: 'EN'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the news report resource.

`description`

(optional) The description of the news report.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(optional) The news report name.

`ons_topic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ONS topic.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`status`

(optional) Indicates the status of a news report in Operations Insights.

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`time_created`

(optional) The time the the news report was first enabled. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the news report was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the news report.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_SUMMARY_T Type

Summary of a news report resource.

Syntax
```

```

Fields

Field Description

`news_frequency`

(required) News report frequency.

Allowed values are: 'WEEKLY'

`content_types`

(required)

`locale`

(optional) Language of the news report.

Allowed values are: 'EN'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the news report resource.

`description`

(optional) The description of the news report.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(optional) The news report name.

`ons_topic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ONS topic.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`status`

(optional) Indicates the status of a news report in Operations Insights.

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`time_created`

(optional) The time the the news report was first enabled. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the news report was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the news report.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_news_report_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_COLLECTION_T Type

Collection of news reports summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of news reports summary objects.

### DBMS_CLOUD_OCI_OPSI_NEWS_REPORTS_T Type

Logical grouping used for Operations Insights news reports related operations.

Syntax
```

```

Fields

Field Description

`news_reports`

(optional) News report object.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_T Type

A private endpoint that allows Operation Insights services to connect to databases in a customer's virtual cloud network (VCN).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Private service accessed database.

`display_name`

(required) The display name of the private endpoint.

`compartment_id`

(required) The compartment OCID of the Private service accessed database.

`vcn_id`

(required) The OCID of the VCN.

`subnet_id`

(required) The OCID of the subnet.

`private_ip`

(optional) The private IP addresses assigned to the private endpoint. All IP addresses will be concatenated if it is RAC DBs.

`description`

(optional) The description of the private endpoint.

`time_created`

(optional) The date and time the private endpoint was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(required) The current state of the private endpoint.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`private_endpoint_status_details`

(optional) A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable information about the validity of the private endpoint connection.

`is_used_for_rac_dbs`

(optional) The flag is to identify if private endpoint is used for rac database or not

`nsg_ids`

(optional) The OCIDs of the network security groups that the private endpoint belongs to.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_SUMMARY_T Type

Summary of a Operation Insights private endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Private service accessed database.

`display_name`

(required) The display name of the private endpoint.

`compartment_id`

(required) The compartment OCID of the Private service accessed database.

`vcn_id`

(required) The OCID of the VCN.

`subnet_id`

(required) The OCID of the subnet.

`is_used_for_rac_dbs`

(optional) The flag to identify if private endpoint is used for rac database or not

`description`

(optional) The description of the private endpoint.

`time_created`

(required) The date and time the private endpoint was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`lifecycle_state`

(required) Private endpoint lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`private_endpoint_status_details`

(optional) A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable information about the validity of the private endpoint connection.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_operations_insights_private_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_COLLECTION_T Type

A collection of Operation Insights private endpoint objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of OperationsInsightsPrivateEndpointSummary objects.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_T Type

OPSI warehouse resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OPSI Warehouse OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) User-friedly name of Operations Insights Warehouse that does not have to be unique.

`cpu_allocated`

(required) Number of OCPUs allocated to OPSI Warehouse ADW.

`cpu_used`

(optional) Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.

`storage_allocated_in_g_bs`

(optional) Storage allocated to OPSI Warehouse ADW.

`storage_used_in_g_bs`

(optional) Storage by OPSI Warehouse ADW in GB.

`dynamic_group_id`

(optional) OCID of the dynamic group created for the warehouse

`operations_insights_tenancy_id`

(optional) Tenancy Identifier of Operations Insights service

`time_last_wallet_rotated`

(optional) The time at which the ADW wallet was last rotated for the Operations Insights Warehouse. An RFC3339 formatted datetime string

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_SUMMARY_T Type

Summary of a Operations Insights Warehouse resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OPSI Warehouse OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) User-friedly name of Operations Insights Warehouse that does not have to be unique.

`cpu_allocated`

(required) Number of OCPUs allocated to OPSI Warehouse ADW.

`cpu_used`

(optional) Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.

`storage_allocated_in_g_bs`

(optional) Storage allocated to OPSI Warehouse ADW.

`storage_used_in_g_bs`

(optional) Storage by OPSI Warehouse ADW in GB.

`dynamic_group_id`

(optional) OCID of the dynamic group created for the warehouse

`operations_insights_tenancy_id`

(optional) Tenancy Identifier of Operations Insights service

`time_last_wallet_rotated`

(optional) The time at which the ADW wallet was last rotated for the Operations Insights Warehouse. An RFC3339 formatted datetime string

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(required) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_operations_insights_warehouse_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_SUMMARY_COLLECTION_T Type

Collection of Operations Insights Warehouse summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Operations Insights Warehouse summary objects.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_T Type

OPSI warehouse User.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) OPSI Warehouse OCID

`id`

(required) Hub User OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(required) Username for schema which would have access to AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`connection_password`

(optional) User provided connection password for the AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`is_awr_data_access`

(required) Indicate whether user has access to AWR data.

`is_em_data_access`

(optional) Indicate whether user has access to EM data.

`is_opsi_data_access`

(optional) Indicate whether user has access to OPSI data.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_SUMMARY_T Type

Summary of a Operations Insights Warehouse User.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_id`

(required) OPSI Warehouse OCID

`id`

(required) Hub User OCID

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(required) Username for schema which would have access to AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`connection_password`

(optional) User provided connection password for the AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`is_awr_data_access`

(required) Indicate whether user has access to AWR data.

`is_em_data_access`

(optional) Indicate whether user has access to EM data.

`is_opsi_data_access`

(optional) Indicate whether user has access to OPSI data.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_operations_insights_warehouse_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_SUMMARY_COLLECTION_T Type

Collection of Operations Insights Warehouse User summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Operations Insights Warehouse user summary objects.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USERS_T Type

Logical grouping used for Operations Insights Warehouse User operations.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouse_users`

(optional) Operations Insights Warehouse User Object.

### DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSES_T Type

Logical grouping used for Operations Insights Warehouse operations.

Syntax
```

```

Fields

Field Description

`operations_insights_warehouses`

(optional) Operations Insights Warehouse Object.

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_CONFIGURATION_ITEM_SUMMARY_T Type

Configuration item summary.

Syntax
```

```

Fields

Field Description

`config_item_type`

(required) Type of configuration item.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_CONFIGURATION_ITEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_opsi_configuration_configuration_item_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_T Type

OPSI configuration.

Syntax
```

```

Fields

Field Description

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of OPSI configuration resource.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opsi_config_type`

(required) OPSI configuration type.

Allowed values are: 'UX_CONFIGURATION'

`display_name`

(optional) User-friendly display name for the OPSI configuration. The name does not have to be unique.

`description`

(optional) Description of OPSI configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(optional) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) OPSI configuration resource lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`config_items`

(optional) Array of configuration item summary objects.

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_BASIC_CONFIGURATION_ITEM_SUMMARY_T Type

Basic configuration item summary. Value and defaultValue fields will contain the custom value stored in the resource and default value from Operations Insights respectively.

Syntax
```

```

`dbms_cloud_oci_opsi_opsi_configuration_basic_configuration_item_summary_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_configuration_configuration_item_summary_t`type.

Fields

Field Description

`name`

(optional) Name of configuration item.

`value`

(optional) Value of configuration item.

`default_value`

(optional) Value of configuration item.

`applicable_contexts`

(optional) List of contexts in Operations Insights where this configuration item is applicable.

`metadata`

(optional)

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_SUMMARY_T Type

OPSI configuration summary.

Syntax
```

```

Fields

Field Description

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of OPSI configuration resource.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opsi_config_type`

(required) OPSI configuration type.

Allowed values are: 'UX_CONFIGURATION'

`display_name`

(optional) User-friendly display name for the OPSI configuration. The name does not have to be unique.

`description`

(optional) Description of OPSI configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(optional) The time at which the resource was first created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time at which the resource was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) OPSI configuration resource lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATIONS_T Type

An OPSI configuration resource is a container for storing custom values for customizable configuration items exposed by Operations Insights. Operations Insights exposes different sets of customizable configuration items through different OPSI configuration types. UX_CONFIGURATION: OPSI configuration resource of this type can be created only once in each compartment. It is a compartment level singleton resource. When configuration values, for an OPSI configuration type that supports compartment level singleton (e.g: UX_CONFIGURATION) resource, are queried for a compartment, following will be the order of preference. 1. If the specified compartment has an OPSI configuration resource, first preference will be given to the custom values inside that. 2. If the root compartment has an OPSI configuration resource, it will be considered as applicable to all compartments of that tenency, hence second preference will be given to the custom values inside that. 3. Default configuration will be considered as a final fallback option.

Syntax
```

```

Fields

Field Description

`opsi_configurations`

(optional) OPSI Configuration Object.

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_opsi_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATIONS_COLLECTION_T Type

Collection of OPSI configuration summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of OPSI configuration summary objects.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_TYPE_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_T Type

Details applicable for all OPSI data objects of a specific OpsiDataObjectType used in a data object query.

Syntax
```

```

`dbms_cloud_oci_opsi_opsi_data_object_type_opsi_data_object_details_in_query_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_data_object_details_in_query_t`type.

Fields

Field Description

`data_object_type`

(required) Type of OPSI data object.

Allowed values are: 'DATABASE_INSIGHTS_DATA_OBJECT', 'HOST_INSIGHTS_DATA_OBJECT', 'EXADATA_INSIGHTS_DATA_OBJECT'

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECTS_T Type

Logical grouping used for OPSI data object targeted operations.

Syntax
```

```

Fields

Field Description

`opsi_data_objects`

(optional) OPSI Data Object.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_opsi_data_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECTS_COLLECTION_T Type

Collection of OPSI data object summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of OPSI data object summary objects.

### DBMS_CLOUD_OCI_OPSI_OPSI_UX_CONFIGURATION_T Type

OPSI UX configuration.

Syntax
```

```

`dbms_cloud_oci_opsi_opsi_ux_configuration_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_configuration_t`type.

### DBMS_CLOUD_OCI_OPSI_OPSI_UX_CONFIGURATION_SUMMARY_T Type

OPSI UX configuration summary.

Syntax
```

```

`dbms_cloud_oci_opsi_opsi_ux_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_opsi_configuration_summary_t`type.

### DBMS_CLOUD_OCI_OPSI_OPSI_WAREHOUSE_DATA_OBJECTS_T Type

Logical grouping used for Operations Insights Warehouse data objects operations.

Syntax
```

```

Fields

Field Description

`opsi_warehouse_data_objects`

(optional) Operations Insights Warehouse Data Object.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_INSIGHT_T Type

Database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_database_insight_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_t`type.

Fields

Field Description

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`connection_details`

(optional)

`credential_details`

(optional)

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`database_name`

(required) Name of database

`database_display_name`

(optional) Display name of database

`database_resource_type`

(required) OCI database resource type

`parent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

`root_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata Infrastructure.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_INSIGHT_SUMMARY_T Type

Summary of a database insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_database_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_insight_summary_t`type.

Fields

Field Description

`database_resource_type`

(optional) OCI database resource type

`opsi_private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`parent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

`root_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the root resource for a composite target. e.g. for ExaCS members the rootId will be the OCID of the Exadata Infrastructure resource.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_EXADATA_INSIGHT_T Type

Private endpoint managed Exadata insight resource (ExaCS).

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_exadata_insight_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_t`type.

Fields

Field Description

`exadata_infra_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata Infrastructure.

`exadata_infra_resource_type`

(required) OCI exadata infrastructure resource type

Allowed values are: 'cloudExadataInfrastructure'

`exadata_shape`

(required) The shape of the Exadata Infrastructure.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_EXADATA_INSIGHT_SUMMARY_T Type

Summary of a Private endpoint managed Exadata insight resource (ExaCS).

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_exadata_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_exadata_insight_summary_t`type.

Fields

Field Description

`exadata_infra_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata Infrastructure.

`exadata_infra_resource_type`

(required) OCI exadata infrastructure resource type

Allowed values are: 'cloudExadataInfrastructure'

`exadata_shape`

(required) The shape of the Exadata Infrastructure.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_HOST_CONFIGURATION_SUMMARY_T Type

Configuration Summary of a PeComanaged host.

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_host_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_configuration_summary_t`type.

Fields

Field Description

`opsi_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`parent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`exadata_details`

(required)

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_HOST_INSIGHT_T Type

Private Endpoint host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_host_insight_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_t`type.

Fields

Field Description

`opsi_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`parent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

`root_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata Infrastructure.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_HOST_INSIGHT_SUMMARY_T Type

Summary of a Private Endpoint host insight resource.

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_host_insight_summary_t`is a subtype of the`dbms_cloud_oci_opsi_host_insight_summary_t`type.

Fields

Field Description

`platform_type`

(optional) Platform type. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`parent_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

`root_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata Infrastructure.

### DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_MANAGED_EXTERNAL_DATABASE_CONFIGURATION_SUMMARY_T Type

Configuration Summary of a Private Endpoint Co-managed External database.

Syntax
```

```

`dbms_cloud_oci_opsi_pe_comanaged_managed_external_database_configuration_summary_t`is a subtype of the`dbms_cloud_oci_opsi_database_configuration_summary_t`type.

Fields

Field Description

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`parent_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`opsi_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OPSI private endpoint

`instances`

(required) Array of hostname and instance name.

`exadata_details`

(required)

### DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_RESULT_SET_COLUMN_METADATA_T Type

Metadata of a column in a data object query result set.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the column in a data object query result set.

`data_type`

(optional) Type of the column in a data object query result.

`data_type_name`

(optional) Type name of the column in a data object query result set.

Allowed values are: 'NUMBER', 'TIMESTAMP', 'VARCHAR2', 'OTHER'

### DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_RESULT_SET_ROWS_COLLECTION_T Type

Collection of result set rows from the data object query.

Syntax
```

```

Fields

Field Description

`format`

(required) Format type of data object query result set.

Allowed values are: 'JSON'

### DBMS_CLOUD_OCI_OPSI_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_RESULT_SET_COLUMN_METADATA_TBL Type

Nested table type of dbms_cloud_oci_opsi_query_data_object_result_set_column_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_JSON_RESULT_SET_ROWS_COLLECTION_T Type

Collection of result set rows from the data object query.

Syntax
```

```

`dbms_cloud_oci_opsi_query_data_object_json_result_set_rows_collection_t`is a subtype of the`dbms_cloud_oci_opsi_query_data_object_result_set_rows_collection_t`type.

Fields

Field Description

`items`

(required) Array of result set rows.

`items_metadata`

(required) Array of QueryDataObjectResultSetColumnMetadata objects that describe the result set columns.

`query_execution_time_in_seconds`

(optional) Time taken for executing the data object query (in seconds). Consider optimizing the query or reducing the target data range, if query execution time is longer.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_FILTERS_T Type

Information to filter the actual target resources in an operation. e.g: While querying a DATABASE_INSIGHTS_DATA_OBJECT using /opsiDataObjects/actions/queryData API, if resourceFilters is set with valid value for definedTagEquals field, only data of the database insights resources for which the specified freeform tags exist will be considered for the actual query scope.

Syntax
```

```

Fields

Field Description

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be considered. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be considered. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be considered. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist will be considered. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to consider all resources within a given compartment and all sub-compartments.

### DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_TBL Type

Nested table type of dbms_cloud_oci_opsi_opsi_data_object_details_in_query_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_QUERY_OPSI_DATA_OBJECT_DATA_DETAILS_T Type

Information required to form and execute query on an OPSI data object.

Syntax
```

```

Fields

Field Description

`data_object_identifier`

(optional) Unique OPSI data object identifier.

`data_objects`

(optional) Details of OPSI data objects used in the query.

`query`

(required)

`resource_filters`

(optional)

### DBMS_CLOUD_OCI_OPSI_QUERY_WAREHOUSE_DATA_OBJECT_DATA_DETAILS_T Type

Information required to form and execute Operations Insights Warehouse data objects query.

Syntax
```

```

Fields

Field Description

`query`

(required)

### DBMS_CLOUD_OCI_OPSI_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type

Resource Capacity samples

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`base_capacity`

(required) The base allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_CURRENT_UTILIZATION_T Type

Current utilization(High/low) for cpu or storage

Syntax
```

```

Fields

Field Description

`low`

(optional) List of db ids with low usage

`high`

(optional) List of db ids with high usage

### DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_PROJECTED_UTILIZATION_ITEM_T Type

Projected utilization object containing dbid and daysToReach value

Syntax
```

```

Fields

Field Description

`id`

(required) Db id

`days_to_reach`

(required) Days to reach projected utilization

### DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_PROJECTED_UTILIZATION_ITEM_TBL Type

Nested table type of dbms_cloud_oci_opsi_resource_insight_projected_utilization_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_PROJECTED_UTILIZATION_T Type

Projected utilization(High/low) for cpu or storage

Syntax
```

```

Fields

Field Description

`low`

(required) List of db ids with low usage

`high`

(required) List of db ids with high usage

### DBMS_CLOUD_OCI_OPSI_RESOURCE_STATISTICS_T Type

Contains resource statistics with usage unit

Syntax
```

```

Fields

Field Description

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`base_capacity`

(optional) The base allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`is_auto_scaling_enabled`

(optional) Indicates if auto scaling feature is enabled or disabled on a database. It will be false for all metrics other than CPU.

`utilization_percent`

(required) Resource utilization in percentage

`usage_change_percent`

(required) Change in resource utilization in percentage

`instance_metrics`

(optional) Array of instance metrics

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_STATISTICS_AGGREGATION_T Type

Contains database details and resource statistics

Syntax
```

```

Fields

Field Description

`database_details`

(optional)

`current_statistics`

(optional)

### DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_SUMMARY_T Type

Contains resource usage summary

Syntax
```

```

Fields

Field Description

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`exadata_display_name`

(optional) The user-friendly name for the Exadata system. The name does not have to be unique.

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`utilization_percent`

(required) Resource utilization in percentage

`usage_change_percent`

(required) Change in resource utilization in percentage

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_TREND_AGGREGATION_T Type

Aggregate usage samples

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_SCHEMA_OBJECT_TYPE_DETAILS_T Type

Schema object details

Syntax
```

```

`dbms_cloud_oci_opsi_schema_object_type_details_t`is a subtype of the`dbms_cloud_oci_opsi_related_object_type_details_t`type.

Fields

Field Description

`object_id`

(required) Object id (from RDBMS)

`owner`

(required) Owner of object

`object_name`

(required) Name of object

`sub_object_name`

(optional) Subobject name; for example, partition name

`object_type`

(required) Type of the object (such as TABLE, INDEX)

### DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_AGGREGATION_T Type

Represents a SQL Insight.

Syntax
```

```

Fields

Field Description

`text`

(required) Insight text. For example `Degrading SQLs`, `Variant SQLs`, `Inefficient SQLs`, `Improving SQLs`, `SQLs with Plan Changes`, `Degrading SQLs have increasing IO Time above 50%`, `Degrading SQLs are variant`, `2 of the 2 variant SQLs have plan changes`, `Inefficient SQLs have increasing CPU Time above 50%

`l_values`

(required) SQL counts for a given insight. For example insight text `2 of 10 SQLs have degrading response time` will have values as [2,10]\"

`category`

(required) Insight category. It would be one of the following DEGRADING, VARIANT, INEFFICIENT, CHANGING_PLANS, IMPROVING, DEGRADING_VARIANT, DEGRADING_INEFFICIENT, DEGRADING_CHANGING_PLANS, DEGRADING_INCREASING_IO, DEGRADING_INCREASING_CPU, DEGRADING_INCREASING_INEFFICIENT_WAIT, DEGRADING_CHANGING_PLANS_AND_INCREASING_IO, DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU, DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,VARIANT_INEFFICIENT, VARIANT_CHANGING_PLANS, VARIANT_INCREASING_IO, VARIANT_INCREASING_CPU, VARIANT_INCREASING_INEFFICIENT_WAIT, VARIANT_CHANGING_PLANS_AND_INCREASING_IO, VARIANT_CHANGING_PLANS_AND_INCREASING_CPU, VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT, INEFFICIENT_CHANGING_PLANS, INEFFICIENT_INCREASING_INEFFICIENT_WAIT, INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT

### DBMS_CLOUD_OCI_OPSI_SQL_INVENTORY_T Type

Inventory details.

Syntax
```

```

Fields

Field Description

`total_sqls`

(required) Total number of sqls. Example `2000`

`total_databases`

(required) Total number of Databases. Example `400`

`sqls_analyzed`

(required) Total number of sqls analyzed by the query. Example `120`

### DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_THRESHOLDS_T Type

Inventory details.

Syntax
```

```

Fields

Field Description

`degradation_in_pct`

(required) Degradation Percent Threshold is used to derive degrading SQLs.

`variability`

(required) Variability Percent Threshold is used to derive variant SQLs.

`inefficiency_in_pct`

(required) Inefficiency Percent Threshold is used to derive inefficient SQLs.

`increase_in_io_in_pct`

(required) PctIncreaseInIO is used for deriving insights for SQLs which are degrading or variant or inefficient. And these SQLs should also have increasing change in IO Time beyond threshold. Insights are derived using linear regression.

`increase_in_cpu_in_pct`

(required) PctIncreaseInCPU is used for deriving insights for SQLs which are degrading or variant or inefficient. And these SQLs should also have increasing change in CPU Time beyond threshold. Insights are derived using linear regression.

`increase_in_inefficient_wait_in_pct`

(required) PctIncreaseInIO is used for deriving insights for SQLs which are degrading or variant or inefficient. And these SQLs should also have increasing change in Other Wait Time beyond threshold. Insights are derived using linear regression.

`improved_in_pct`

(required) Improved Percent Threshold is used to derive improving SQLs.

### DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_insight_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_AGGREGATION_COLLECTION_T Type

SQL Insights response.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`inventory`

(required)

`items`

(required) List of insights.

`thresholds`

(required)

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_SUMMARY_T Type

SQL Plan details

Syntax
```

```

Fields

Field Description

`plan_hash`

(required) Plan hash value for the SQL Execution Plan

`plan_content`

(required) Plan XML Content

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_plan_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_COLLECTION_T Type

SQL Plans for the particular SQL.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`items`

(required) array of SQL Plans.

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHT_AGGREGATION_T Type

SQL execution plan Performance statistics.

Syntax
```

```

Fields

Field Description

`plan_hash`

(required) Plan hash value for the SQL Execution Plan

`io_time_in_sec`

(required) IO Time in seconds

`cpu_time_in_sec`

(required) CPU Time in seconds

`inefficient_wait_time_in_sec`

(required) Inefficient Wait Time in seconds

`executions_count`

(required) Total number of executions

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHTS_T Type

Represents collection of SQL Plan Insights.

Syntax
```

```

Fields

Field Description

`text`

(required) SQL Plan Insight text. For example `Number of Plans Used`, `Most Executed Plan`, `Best Performing Plan`, `Worst Performing Plan`, `Plan With Most IO`, `Plan with Most CPU`

`value`

(required) SQL execution plan hash value for a given insight. For example `Most Executed Plan` insight will have value as \"3975467901\"

`category`

(required) SQL Insight category. For example PLANS_USED, MOST_EXECUTED, BEST_PERFORMER, WORST_PERFORMER, MOST_CPU or MOST_IO.

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHTS_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_plan_insights_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHT_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_plan_insight_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHT_AGGREGATION_COLLECTION_T Type

SQL plan insights response.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`insights`

(required) List of SQL plan insights.

`items`

(required) List of SQL plan statistics.

### DBMS_CLOUD_OCI_OPSI_SQL_RESPONSE_TIME_DISTRIBUTION_AGGREGATION_T Type

SQL Response time distribution entry.

Syntax
```

```

Fields

Field Description

`bucket_id`

(required) Response time bucket id

`executions_count`

(required) Total number of SQL executions

### DBMS_CLOUD_OCI_OPSI_SQL_RESPONSE_TIME_DISTRIBUTION_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_response_time_distribution_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_RESPONSE_TIME_DISTRIBUTION_AGGREGATION_COLLECTION_T Type

SQL response time distribution over the selected time window.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) Array of pre defined SQL response time bucket id and SQL executions count.

### DBMS_CLOUD_OCI_OPSI_SQL_SEARCH_SUMMARY_T Type

Database summary object resulting from a sql search operation.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_name`

(required) The database name. The database name is unique within the tenancy.

`database_display_name`

(required) The user-friendly name for the database. The name does not have to be unique.

`database_type`

(required) Operations Insights internal representation of the database type.

`database_version`

(required) The version of the database.

### DBMS_CLOUD_OCI_OPSI_SQL_SEARCH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_search_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_SEARCH_COLLECTION_T Type

Search SQL response.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(optional) Unique SQL_ID for a SQL Statement.

`sql_text`

(optional) SQL Statement Text

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) List of Databases executing the sql.

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_T Type

Performance statistics for the SQL.

Syntax
```

```

Fields

Field Description

`database_time_in_sec`

(required) Database Time in seconds

`executions_per_hour`

(required) Number of executions per hour

`executions_count`

(required) Total number of executions

`cpu_time_in_sec`

(required) CPU Time in seconds

`io_time_in_sec`

(required) I/O Time in seconds

`inefficient_wait_time_in_sec`

(required) Inefficient Wait Time in seconds

`response_time_in_sec`

(required) Response time is the average elaspsed time per execution. It is the ratio of Total Database Time to the number of executions

`plan_count`

(required) Number of SQL execution plans used by the SQL

`variability`

(required) Variability is the ratio of the standard deviation in response time to the mean of response time of the SQL

`average_active_sessions`

(required) Average Active Sessions represent the average active sessions at a point in time. It is the number of sessions that are either working or waiting.

`database_time_pct`

(required) Percentage of Database Time

`inefficiency_in_pct`

(required) Percentage of Inefficiency. It is calculated by Total Database Time divided by Total Wait Time

`change_in_cpu_time_in_pct`

(required) Percent change in CPU Time based on linear regression

`change_in_io_time_in_pct`

(required) Percent change in IO Time based on linear regression

`change_in_inefficient_wait_time_in_pct`

(required) Percent change in Inefficient Wait Time based on linear regression

`change_in_response_time_in_pct`

(required) Percent change in Response Time based on linear regression

`change_in_average_active_sessions_in_pct`

(required) Percent change in Average Active Sessions based on linear regression

`change_in_executions_per_hour_in_pct`

(required) Percent change in Executions per hour based on linear regression

`change_in_inefficiency_in_pct`

(required) Percent change in Inefficiency based on linear regression

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTIC_AGGREGATION_T Type

SQL Statistics

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`database_details`

(required)

`category`

(required) SQL belongs to one or more categories based on the insights.

`statistics`

(optional)

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTIC_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_statistic_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTIC_AGGREGATION_COLLECTION_T Type

SQL statistics response.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) Array of SQLs along with its statistics statisfying the query criteria.

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_T Type

SQL performance statistics per database

Syntax
```

```

Fields

Field Description

`name`

(required) SQL performance statistic name

`l_values`

(required) SQL performance statistic value

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_statistics_time_series_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_AGGREGATION_T Type

Database details and SQL performance statistics for a given database

Syntax
```

```

Fields

Field Description

`database_details`

(required)

`statistics`

(required) SQL performance statistics for a given database

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_statistics_time_series_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_AGGREGATION_COLLECTION_T Type

SQL performance statistics over the selected time window.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`end_timestamps`

(optional) Array comprising of all the sampling period end timestamps in RFC 3339 format.

`items`

(required) Array of SQL performance statistics across databases.

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_BY_PLAN_AGGREGATION_T Type

SQL performance statistics for a given plan

Syntax
```

```

Fields

Field Description

`plan_hash`

(required) Plan hash value for the SQL Execution Plan

`statistics`

(required) SQL performance statistics for a given plan

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_BY_PLAN_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_statistics_time_series_by_plan_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_BY_PLAN_AGGREGATION_COLLECTION_T Type

SQL performance statistics by plan over the selected time window.

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`end_timestamps`

(required) Array comprising of all the sampling period end timestamps in RFC 3339 format.

`items`

(required) array of SQL performance statistics by plans

### DBMS_CLOUD_OCI_OPSI_SQL_TEXT_SUMMARY_T Type

SQL Text details

Syntax
```

```

Fields

Field Description

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_text`

(required) SQL Text

### DBMS_CLOUD_OCI_OPSI_SQL_TEXT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_sql_text_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SQL_TEXT_COLLECTION_T Type

SQL Text for the particular SQL.

Syntax
```

```

Fields

Field Description

`items`

(required) array of SQL Texts.

### DBMS_CLOUD_OCI_OPSI_SQL_TYPE_DETAILS_T Type

SQL details

Syntax
```

```

`dbms_cloud_oci_opsi_sql_type_details_t`is a subtype of the`dbms_cloud_oci_opsi_related_object_type_details_t`type.

Fields

Field Description

`sql_id`

(required) SQL identifier

`sql_text`

(required) First 3800 characters of the SQL text

`is_sql_text_truncated`

(required) SQL identifier

`sql_command`

(required) SQL command name (such as SELECT, INSERT)

### DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_T Type

Usage data samples.

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`file_system_usage_in_g_bs`

(required) Filesystem usage in GB.

`file_system_avail_in_percent`

(required) Filesystem available in percent.

### DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_TBL Type

Nested table type of dbms_cloud_oci_opsi_storage_usage_trend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_AGGREGATION_T Type

Usage data per filesystem.

Syntax
```

```

Fields

Field Description

`file_system_name`

(required) Name of filesystem.

`mount_point`

(required) Mount points are specialized NTFS filesystem objects.

`file_system_size_in_g_bs`

(required) Size of filesystem.

`usage_data`

(required) List of usage data samples for a filesystem.

### DBMS_CLOUD_OCI_OPSI_AWR_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_awr_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_AWR_SOURCES_SUMMARIES_COLLECTION_T Type

Collection of AwrSource summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of AwrSource summary objects.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_CAPACITY_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_resource_capacity_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_COLLECTION_T Type

Collection of resource capacity trend.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'MEMORY_PGA', 'MEMORY_SGA'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`capacity_data`

(required) Capacity Data with time interval

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATION_T Type

Forecast results from the selected time period.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'MEMORY_PGA', 'MEMORY_SGA'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`selected_forecast_algorithm`

(optional) Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.

`pattern`

(required) Time series patterns used in the forecasting.

Allowed values are: 'LINEAR', 'MONTHLY_SEASONS', 'MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_SEASONS', 'WEEKLY_AND_MONTHLY_SEASONS', 'WEEKLY_MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_AND_YEARLY_SEASONS', 'YEARLY_SEASONS'

`tablespace_name`

(required) The name of tablespace.

`historical_data`

(required) Time series data used for the forecast analysis.

`projected_data`

(required) Time series data result of the forecasting analysis.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_STATISTICS_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_resource_statistics_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_COLLECTION_T Type

Returns list of the Databases with resource statistics like usage, capacity, utilization and usage change percent.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'MEMORY_PGA', 'MEMORY_SGA'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`items`

(required) Collection of Resource Statistics items

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE_AGGREGATION_T Type

Resource usage summation for the current time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`resource_metric`

(required) Defines the type of resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'MEMORY_PGA', 'MEMORY_SGA'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`usage_change_percent`

(required) Percentage change in resource usage during the current period calculated using linear regression functions

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_resource_usage_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE_TREND_AGGREGATION_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`resource_metric`

(required) Defines the type of resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'MEMORY_PGA', 'MEMORY_SGA'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`usage_data`

(required) Usage Data with time stamps

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_AGGREGATION_T Type

Insights response containing current/projected groups for storage or CPU.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'MEMORY_PGA', 'MEMORY_SGA'

`projected_utilization`

(required)

`current_utilization`

(required)

### DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_T Type

Usage data samples

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

### DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_TBL Type

Nested table type of dbms_cloud_oci_opsi_tablespace_usage_trend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_AGGREGATION_T Type

Usage data per tablespace for a Pluggable database

Syntax
```

```

Fields

Field Description

`tablespace_name`

(required) The name of tablespace.

`tablespace_type`

(required) Type of tablespace

`usage_data`

(required) List of usage data samples for a tablespace

### DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_tablespace_usage_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_TABLESPACE_USAGE_TREND_AGGREGATION_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`items`

(required) Collection of Usage Data with time stamps for top five tablespace

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type

Collection of resource capacity trend.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`capacity_data`

(required) Capacity Data with time interval

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_insight_resource_capacity_trend_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_COLLECTION_T Type

capacity results with breakdown by databases, hosts, storage servers or diskgroup.

Syntax
```

```

Fields

Field Description

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`items`

(required) Capacity Data with time interval

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATION_T Type

Usage and Forecast results from the selected time period.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`selected_forecast_algorithm`

(optional) Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.

`pattern`

(required) Time series patterns used in the forecasting.

Allowed values are: 'LINEAR', 'MONTHLY_SEASONS', 'MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_SEASONS', 'WEEKLY_AND_MONTHLY_SEASONS', 'WEEKLY_MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_AND_YEARLY_SEASONS', 'YEARLY_SEASONS'

`days_to_reach_capacity`

(required) Days to reach capacity for a storage server

`historical_data`

(required) Time series data used for the forecast analysis.

`projected_data`

(required) Time series data result of the forecasting analysis.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_insight_resource_forecast_trend_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_COLLECTION_T Type

Usage and Forecast results with breakdown by databases, hosts or storage servers.

Syntax
```

```

Fields

Field Description

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`items`

(required) Collection of id, name , daysToReach Capacity, historical usage and projected usage forecast.

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_insight_resource_statistics_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_COLLECTION_T Type

Returns list of the resources with resource statistics like usage,capacity,utilization and usage change percent.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) Collection of Resource Statistics items

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`exadata_insight_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata insight.

`exadata_display_name`

(optional) The user-friendly name for the Exadata system. The name does not have to be unique.

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE_AGGREGATION_T Type

Resource usage summation for the current time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`usage_change_percent`

(required) Percentage change in resource usage during the current period calculated using linear regression functions

`total_host_capacity`

(optional) The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.

### DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_resource_usage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE_COLLECTION_T Type

Resource usage , allocation, utilization and usage ChangePercent for the current time period

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`items`

(required) Collection of Resource Usage Summary items

### DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_INSIGHT_UTILIZATION_ITEM_TBL Type

Nested table type of dbms_cloud_oci_opsi_exadata_insight_resource_insight_utilization_item_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_AGGREGATION_T Type

Insights response containing utilization values for exadata systems.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`exadata_resource_metric`

(required) Defines the type of exadata resource metric (example: CPU, STORAGE)

Allowed values are: 'CPU', 'STORAGE', 'IO', 'MEMORY', 'IOPS', 'THROUGHPUT'

`exadata_resource_type`

(required) Defines the resource type for an exadata (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

Allowed values are: 'DATABASE', 'HOST', 'STORAGE_SERVER', 'DISKGROUP'

`utilization`

(required) Collection of Exadata system utilization

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_HOST_RECOMMENDATION_AGGREGATION_T Type

Returns list of hosts with resource statistics like usage, capacity, utilization, usage change percent and load.

Syntax
```

```

Fields

Field Description

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`details`

(optional)

### DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_network_usage_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_NETWORK_USAGE_TREND_AGGREGATION_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`items`

(required) Collection of Usage Data with time stamps for all network interfaces.

### DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_CAPACITY_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_resource_capacity_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`capacity_data`

(required) Capacity Data with timestamp.

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATION_T Type

Forecast results from the selected time period.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`selected_forecast_algorithm`

(optional) Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.

`pattern`

(required) Time series patterns used in the forecasting.

Allowed values are: 'LINEAR', 'MONTHLY_SEASONS', 'MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_SEASONS', 'WEEKLY_AND_MONTHLY_SEASONS', 'WEEKLY_MONTHLY_AND_YEARLY_SEASONS', 'WEEKLY_AND_YEARLY_SEASONS', 'YEARLY_SEASONS'

`historical_data`

(required) Time series data used for the forecast analysis.

`projected_data`

(required) Time series data result of the forecasting analysis.

### DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_host_insight_resource_statistics_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_COLLECTION_T Type

Returns list of hosts with resource statistics like usage, capacity, utilization, usage change percent and load.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`items`

(required) Collection of Resource Statistics items

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE_AGGREGATION_T Type

Resource usage summation for the current time period.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`usage`

(required) Total amount used of the resource metric type (CPU, STORAGE).

`l_capacity`

(required) The maximum allocated amount of the resource metric type (CPU, STORAGE) for a set of databases.

`usage_change_percent`

(required) Percentage change in resource usage during the current period calculated using linear regression functions

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE_TREND_AGGREGATION_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`usage_data`

(required) Usage Data with timestamp.

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_AGGREGATION_T Type

Insights response containing current/projected groups for CPU or memory.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`high_utilization_threshold`

(required) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(required) Percent value in which a resource metric is considered lowly utilized.

`resource_metric`

(required) Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

Allowed values are: 'CPU', 'MEMORY', 'LOGICAL_MEMORY', 'STORAGE', 'NETWORK'

`projected_utilization`

(required)

`current_utilization`

(required)

### DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_storage_usage_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_STORAGE_USAGE_TREND_AGGREGATION_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`items`

(required) Collection of Usage Data with time stamps for all filesystems.

### DBMS_CLOUD_OCI_OPSI_DISK_STATISTICS_TBL Type

Nested table type of dbms_cloud_oci_opsi_disk_statistics_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHTS_DISK_STATISTICS_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`usage_unit`

(required) Displays usage unit ( CORES, GB , PERCENT, MBPS)

Allowed values are: 'CORES', 'GB', 'MBPS', 'IOPS', 'PERCENT'

`item_duration_in_ms`

(required) Time duration in milliseconds between data points (one hour or one day).

`items`

(required) Collection of Data for all disks in a host.

### DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_T Type

Aggregated data for top processes on a specific date.

Syntax
```

```

Fields

Field Description

`command`

(required) Command line and arguments used to launch process.

`process_hash`

(required) Unique identifier for a process.

`cpu_usage`

(required) Process CPU usage.

`cpu_utilization`

(required) Process CPU utilization percentage.

`memory_utilization`

(required) Process memory utilization percentage.

`virtual_memory_in_m_bs`

(required) Process virtual memory in Megabytes.

`physical_memory_in_m_bs`

(required) Procress physical memory in Megabytes.

`max_process_count`

(required) Maximum number of processes running at time of collection.

### DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TBL Type

Nested table type of dbms_cloud_oci_opsi_top_processes_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHTS_TOP_PROCESSES_USAGE_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) The start timestamp that was passed into the request.

`items`

(required) List of usage data samples for a top process on a specific date.

### DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_T Type

Aggregated data for top processes

Syntax
```

```

Fields

Field Description

`end_timestamp`

(required) The timestamp in which the current sampling period ends in RFC 3339 format.

`cpu_usage`

(required) Process CPU usage.

`cpu_utilization`

(required) Process CPU utilization percentage

`memory_utilization`

(required) Process memory utilization percentage

`virtual_memory_in_m_bs`

(required) Process virtual memory in Megabytes

`physical_memory_in_m_bs`

(required) Procress physical memory in Megabytes

`max_process_count`

(required) Maximum number of processes running at time of collection

### DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_TBL Type

Nested table type of dbms_cloud_oci_opsi_top_processes_usage_trend_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_AGGREGATION_T Type

Usage data per host top process

Syntax
```

```

Fields

Field Description

`command`

(required) Command line and arguments used to launch process

`usage_data`

(required) List of usage data samples for a top process

### DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_opsi_top_processes_usage_trend_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHTS_TOP_PROCESSES_USAGE_TREND_COLLECTION_T Type

Top level response object.

Syntax
```

```

Fields

Field Description

`time_interval_start`

(required) The start timestamp that was passed into the request.

`time_interval_end`

(required) The end timestamp that was passed into the request.

`items`

(required) Collection of Usage Data with time stamps for top processes

### DBMS_CLOUD_OCI_OPSI_SUMMARIZE_OPERATIONS_INSIGHTS_WAREHOUSE_RESOURCE_USAGE_AGGREGATION_T Type

Details of resource usage by an Operations Insights Warehouse resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OPSI Warehouse OCID

`cpu_used`

(optional) Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.

`storage_used_in_g_bs`

(optional) Storage by OPSI Warehouse ADW in GB.

`lifecycle_state`

(required) Possible lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_OPSI_UPDATE_DATABASE_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the database entity.

Allowed values are: 'AUTONOMOUS_DATABASE', 'EM_MANAGED_EXTERNAL_DATABASE', 'MACS_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_AUTONOMOUS_DATABASE_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_autonomous_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_database_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_AWR_HUB_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-friedly name of AWR Hub that does not have to be unique.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_AWR_HUB_SOURCE_DETAILS_T Type

Awr hub source update object information

Syntax
```

```

Fields

Field Description

`l_type`

(optional) source type of the database

Allowed values are: 'ADW_S', 'ATP_S', 'ADW_D', 'ATP_D', 'EXTERNAL_PDB', 'EXTERNAL_NONCDB', 'COMANAGED_VM_CDB', 'COMANAGED_VM_PDB', 'COMANAGED_VM_NONCDB', 'COMANAGED_BM_CDB', 'COMANAGED_BM_PDB', 'COMANAGED_BM_NONCDB', 'COMANAGED_EXACS_CDB', 'COMANAGED_EXACS_PDB', 'COMANAGED_EXACS_NONCDB', 'UNDEFINED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_CONFIGURATION_ITEM_DETAILS_T Type

Configuration item details for OPSI configuration update.

Syntax
```

```

Fields

Field Description

`config_item_type`

(required) Type of configuration item.

Allowed values are: 'BASIC'

### DBMS_CLOUD_OCI_OPSI_UPDATE_BASIC_CONFIGURATION_ITEM_DETAILS_T Type

Configuration item details for OPSI configuration update.

Syntax
```

```

`dbms_cloud_oci_opsi_update_basic_configuration_item_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_configuration_item_details_t`type.

Fields

Field Description

`name`

(optional) Name of configuration item.

`value`

(optional) Value of configuration item.

### DBMS_CLOUD_OCI_OPSI_UPDATE_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_em_managed_external_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_database_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_EXADATA_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the Exadata system.

Allowed values are: 'EM_MANAGED_EXTERNAL_EXADATA', 'PE_COMANAGED_EXADATA'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_em_managed_external_exadata_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_exadata_insight_details_t`type.

Fields

Field Description

`is_auto_sync_enabled`

(optional) Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.

### DBMS_CLOUD_OCI_OPSI_UPDATE_HOST_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`entity_source`

(required) Source of the host entity.

Allowed values are: 'MACS_MANAGED_EXTERNAL_HOST', 'EM_MANAGED_EXTERNAL_HOST', 'MACS_MANAGED_CLOUD_HOST', 'PE_COMANAGED_HOST'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_EM_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_em_managed_external_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_host_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_ENTERPRISE_MANAGER_BRIDGE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-friedly name of Enterprise Manager Bridge that does not have to be unique.

`description`

(optional) Description of Enterprise Manager Bridge

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_MACS_MANAGED_CLOUD_HOST_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_macs_managed_cloud_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_host_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_MACS_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_macs_managed_external_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_database_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_macs_managed_external_host_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_host_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_NEWS_REPORT_DETAILS_T Type

The information about the news report to be updated.

Syntax
```

```

Fields

Field Description

`status`

(optional) Defines if the news report will be enabled or disabled.

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`news_frequency`

(optional) News report frequency.

Allowed values are: 'WEEKLY'

`locale`

(optional) Language of the news report.

Allowed values are: 'EN'

`content_types`

(optional)

`ons_topic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ONS topic.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_DETAILS_T Type

The details used to update a Operation Insights private endpoint.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the private endpoint.

`description`

(optional) The description of the private endpoint.

`nsg_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups that the Private service accessed the database.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-friedly name of Operations Insights Warehouse that does not have to be unique.

`cpu_allocated`

(optional) Number of OCPUs allocated to OPSI Warehouse ADW.

`storage_allocated_in_g_bs`

(optional) Storage allocated to OPSI Warehouse ADW.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`connection_password`

(optional) User provided connection password for the AWR Data, Enterprise Manager Data and Operations Insights OPSI Hub.

`is_awr_data_access`

(optional) Indicate whether user has access to AWR data.

`is_em_data_access`

(optional) Indicate whether user has access to EM data.

`is_opsi_data_access`

(optional) Indicate whether user has access to OPSI data.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OPSI_UPDATE_CONFIGURATION_ITEM_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_opsi_update_configuration_item_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_UPDATE_OPSI_CONFIGURATION_DETAILS_T Type

Information to be updated in OPSI configuration resource.

Syntax
```

```

Fields

Field Description

`opsi_config_type`

(required) OPSI configuration type.

Allowed values are: 'UX_CONFIGURATION'

`display_name`

(optional) User-friendly display name for the OPSI configuration. The name does not have to be unique.

`description`

(optional) Description of OPSI configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`config_items`

(optional) Array of configuration items with custom values. All and only configuration items requiring custom values should be part of this array. This array overwrites the existing custom configuration items array for this resource.

### DBMS_CLOUD_OCI_OPSI_UPDATE_OPSI_UX_CONFIGURATION_DETAILS_T Type

Information to be updated in OPSI UX configuration.

Syntax
```

```

`dbms_cloud_oci_opsi_update_opsi_ux_configuration_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_opsi_configuration_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_pe_comanaged_database_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_database_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UPDATE_PE_COMANAGED_EXADATA_INSIGHT_DETAILS_T Type

The information to be updated.

Syntax
```

```

`dbms_cloud_oci_opsi_update_pe_comanaged_exadata_insight_details_t`is a subtype of the`dbms_cloud_oci_opsi_update_exadata_insight_details_t`type.

### DBMS_CLOUD_OCI_OPSI_UX_CONFIGURATION_ITEMS_COLLECTION_T Type

Collection of ux configuration item summary objects.

Syntax
```

```

`dbms_cloud_oci_opsi_ux_configuration_items_collection_t`is a subtype of the`dbms_cloud_oci_opsi_configuration_items_collection_t`type.

### DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_DETAILS_T Type

Warehouse data object details.

Syntax
```

```

Fields

Field Description

`data_object_type`

(required) Type of the data object.

Allowed values are: 'VIEW', 'TABLE'

### DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_SUMMARY_T Type

Summary of a Warehouse data object.

Syntax
```

```

Fields

Field Description

`data_object_type`

(required) Type of the data object.

Allowed values are: 'VIEW', 'TABLE'

`name`

(optional) Name of the data object, which can be used in data object queries just like how view names are used in a query.

`owner`

(optional) Owner of the data object, which can be used in data object queries in front of data object names just like SCHEMA.VIEW notation in queries.

`details`

(optional)

### DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_opsi_warehouse_data_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_COLLECTION_T Type

Collection of Warehouse data object summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Warehouse data object summary objects.

### DBMS_CLOUD_OCI_OPSI_WAREHOUSE_TABLE_DATA_OBJECT_DETAILS_T Type

Details of a TABLE type data object in a Warehouse.

Syntax
```

```

`dbms_cloud_oci_opsi_warehouse_table_data_object_details_t`is a subtype of the`dbms_cloud_oci_opsi_warehouse_data_object_details_t`type.

Fields

Field Description

`columns_metadata`

(optional) Metadata of columns in the data object.

### DBMS_CLOUD_OCI_OPSI_WAREHOUSE_VIEW_DATA_OBJECT_DETAILS_T Type

Details of a VIEW type data object in a Warehouse.

Syntax
```

```

`dbms_cloud_oci_opsi_warehouse_view_data_object_details_t`is a subtype of the`dbms_cloud_oci_opsi_warehouse_data_object_details_t`type.

Fields

Field Description

`columns_metadata`

(optional) Metadata of columns in the data object.

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_opsi_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'ENABLE_DATABASE_INSIGHT', 'DISABLE_DATABASE_INSIGHT', 'UPDATE_DATABASE_INSIGHT', 'CREATE_DATABASE_INSIGHT', 'MOVE_DATABASE_INSIGHT', 'DELETE_DATABASE_INSIGHT', 'CREATE_ENTERPRISE_MANAGER_BRIDGE', 'UDPATE_ENTERPRISE_MANAGER_BRIDGE', 'MOVE_ENTERPRISE_MANAGER_BRIDGE', 'DELETE_ENTERPRISE_MANAGER_BRIDGE', 'ENABLE_HOST_INSIGHT', 'DISABLE_HOST_INSIGHT', 'UPDATE_HOST_INSIGHT', 'CREATE_HOST_INSIGHT', 'MOVE_HOST_INSIGHT', 'DELETE_HOST_INSIGHT', 'CREATE_EXADATA_INSIGHT', 'ENABLE_EXADATA_INSIGHT', 'DISABLE_EXADATA_INSIGHT', 'UPDATE_EXADATA_INSIGHT', 'MOVE_EXADATA_INSIGHT', 'DELETE_EXADATA_INSIGHT', 'ADD_EXADATA_INSIGHT_MEMBERS', 'EXADATA_AUTO_SYNC', 'UPDATE_OPSI_WAREHOUSE', 'CREATE_OPSI_WAREHOUSE', 'MOVE_OPSI_WAREHOUSE', 'DELETE_OPSI_WAREHOUSE', 'ROTATE_OPSI_WAREHOUSE_WALLET', 'UPDATE_OPSI_WAREHOUSE_USER', 'CREATE_OPSI_WAREHOUSE_USER', 'MOVE_OPSI_WAREHOUSE_USER', 'DELETE_OPSI_WAREHOUSE_USER', 'UPDATE_AWRHUB', 'CREATE_AWRHUB', 'MOVE_AWRHUB', 'DELETE_AWRHUB', 'UPDATE_PRIVATE_ENDPOINT', 'CREATE_PRIVATE_ENDPOINT', 'MOVE_PRIVATE_ENDPOINT', 'DELETE_PRIVATE_ENDPOINT', 'CHANGE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS', 'UPDATE_OPSI_CONFIGURATION', 'CREATE_OPSI_CONFIGURATION', 'MOVE_OPSI_CONFIGURATION', 'DELETE_OPSI_CONFIGURATION', 'ENABLE_ADB_ADVANCED_FEATURES', 'DISABLE_ADB_ADVANCED_FEATURES', 'UPDATE_ADB_ADVANCED_FEATURES', 'CREATE_NEWS_REPORT', 'ENABLE_NEWS_REPORT', 'DISABLE_NEWS_REPORT', 'UPDATE_NEWS_REPORT', 'MOVE_NEWS_REPORT', 'DELETE_NEWS_REPORT', 'CREATE_AWRHUB_SOURCE', 'DELETE_AWRHUB_SOURCE', 'UPDATE_AWRHUB_SOURCE', 'MOVE_AWRHUB_SOURCE', 'ENABLE_AWRHUB_SOURCE', 'DISABLE_AWRHUB_SOURCE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_opsi_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequests.

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_opsi_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_opsi_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_OPSI_WORK_REQUESTS_T Type

Logical grouping used for Operations Insights Work Request operations.

Syntax
```

```

Fields

Field Description

`work_requests`

(optional) OPSI Work Request Object.

- [OPSI Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-60E792A3-8CCC-4946-A1A2-525A6189BBE9)
- [DBMS_CLOUD_OCI_OPSI_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9FA6505D-05CC-45DF-974B-85E07A595A66)
- [DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_EXADATA_MEMBER_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7E1A820B-854B-4D69-AF91-A8501698AD57)
- [DBMS_CLOUD_OCI_OPSI_ADD_EXADATA_INSIGHT_MEMBERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-016E5F60-0DF8-4491-9A8F-63CA1823F65A)
- [DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_EXADATA_MEMBER_ENTITY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E3284B3F-0130-4094-AA46-D3BB95AF58E8)
- [DBMS_CLOUD_OCI_OPSI_ADD_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_MEMBERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-21DE8BD6-0EAA-477A-A071-DBE7A72C5B95)
- [DBMS_CLOUD_OCI_OPSI_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6CC2CDC8-7CFA-453E-83D5-FAC9C2188F7C)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BB83F06F-580A-46BE-AF37-B0B6F9CA6DCF)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_HOST_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1FE280B5-BDDB-449E-BCB1-70A8CAF8F2BA)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0CCF8D83-5B84-4EB0-98D8-145D3ACE3ABB)
- [DBMS_CLOUD_OCI_OPSI_CREATE_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EF74D908-A6CE-4F08-9EF3-088BCF2260C6)
- [DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-716C8C15-0437-4338-BC5C-29FFB6512B67)
- [DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-54D3A372-30A8-4DC7-B13D-08DFFAF277A3)
- [DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_EXADATA_VMCLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6053C28F-51AC-4DED-B18C-B6AF33F7D3EF)
- [DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_EXADATA_VMCLUSTER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2F0E4B35-54F7-4520-8DC6-C26F0D021CEB)
- [DBMS_CLOUD_OCI_OPSI_ADD_PE_COMANAGED_EXADATA_INSIGHT_MEMBERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AC3AA973-CA6F-4F71-9B7A-D0AFB32B44B1)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSTANCE_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A8FC55C9-CD46-4FF9-A8E8-14F0A941F35D)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSTANCE_MAP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F795C0B7-784F-47EE-8D0F-3CC479DC8DD0)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DCD50F12-C21D-49D5-A83B-08EF81490D3B)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-89C18AA7-BA07-4787-8BF0-181F67A6BDCD)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D8228379-7308-4AA7-9EA1-994F1542696B)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-90693BD5-C2A5-475E-874B-124AFBA30B5B)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E44A67E6-DD3A-483E-A40C-E655A65FD3F6)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8D883F00-8963-4A99-86AB-E95ACDC26978)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F8487331-4E4B-4628-ADD9-E5865CFF2BEE)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8E178B3A-A401-465F-AF86-048CE4F79AA1)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8FB316EA-91FD-40B1-9A24-48CAD1AC6341)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_CATEGORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3596073A-0AB7-4FA1-A025-E47308338DCA)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDING_CATEGORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-77084D12-222F-4A6E-B377-83110E4CA01C)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDINGS_TIME_SERIES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-18025B51-B0D2-47C8-9ACF-0B58C168E469)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDINGS_TIME_SERIES_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C7C3D83C-2024-4C20-9352-53819C625369)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_FINDINGS_TIME_SERIES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6082EF77-B47D-4B10-93D0-CA5BC5E8756C)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1C5808D6-5C17-421D-AFC5-917F0C6C9C3D)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-87FFFA92-5484-47C5-8F11-827403D768F1)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5FAAFAE7-5048-403D-8F90-AC420B5136AE)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8DA4E551-8128-4EA1-98E7-F6DDC1F29511)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CATEGORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-46B39B50-A353-44BA-8811-29F878D7AE96)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CATEGORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-259EE9C9-BB98-4749-BED7-DF616F38DBDE)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CHANGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-449FD1BB-520A-43D4-942A-839C91BF5D0F)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CHANGE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-294737B2-1BD7-457F-B099-2FCFAF262B8F)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_PARAMETER_CHANGE_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-63F27035-6432-468F-B051-BAE8BFA8DFEF)
- [DBMS_CLOUD_OCI_OPSI_RELATED_OBJECT_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E7289F7E-BFB9-44BF-B8B6-2F568C624174)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5561F05F-C4E1-4225-8976-A540F85A3FAE)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0B83EECF-53BD-4B73-A13E-CFCBE8831DD4)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B2BE76D5-6A99-459A-AD10-246FA895B8A7)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F81C78B1-BF7F-4984-9AAE-A5A022242247)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_CATEGORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5865911E-D57E-4DED-81E2-7CE5EFDB28D1)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATION_CATEGORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-790F1E21-FD72-47F4-82B7-E57973227712)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATIONS_TIME_SERIES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-86CAB21A-1467-4835-8FC4-C310D3A40A43)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATIONS_TIME_SERIES_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0B804778-8DA2-44B6-85B6-2DDE4CC137ED)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_RECOMMENDATIONS_TIME_SERIES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AED2C96C-1CC6-40B4-ACAC-80F44090A902)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SCHEMA_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8B64CB4A-9B37-47BE-B7E0-39FC7BB40B39)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SCHEMA_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-709C1DC7-3CA1-40CC-B697-9411AAA25957)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SCHEMA_OBJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-253A5FF8-C5A3-45DD-AAA7-9C6E11908F63)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SQL_STATEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B1A50C24-9B05-4852-A75D-AC01E5B00C28)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SQL_STATEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E22CFAC1-E09F-4F98-A9A0-93A0076D7A22)
- [DBMS_CLOUD_OCI_OPSI_ADDM_DB_SQL_STATEMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-777E4EA7-38C8-4696-A1C9-105E6D455E29)
- [DBMS_CLOUD_OCI_OPSI_ADDM_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BFB544C8-5098-4574-B625-28ED63DABCEB)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-297A9322-ECEC-4401-B26A-DE64CADE3226)
- [DBMS_CLOUD_OCI_OPSI_AUTONOMOUS_DATABASE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5BBFA0D7-649D-4AB1-9FAF-9ADDD5773823)
- [DBMS_CLOUD_OCI_OPSI_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CAA324D6-BBEA-4AFB-967F-F060FC0D289E)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-614BEEC1-F30D-4A7D-AAB9-9289DC84D6D1)
- [DBMS_CLOUD_OCI_OPSI_AUTONOMOUS_DATABASE_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0F70A509-A9C2-4A20-8B7B-EE2F7D309950)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DA736871-31FB-4EDB-A5C8-E52007C3B9AB)
- [DBMS_CLOUD_OCI_OPSI_AUTONOMOUS_DATABASE_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-12313EFF-9F5C-48E7-9C44-8E547B396FC4)
- [DBMS_CLOUD_OCI_OPSI_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1750D82E-4E11-40CE-A9C0-DD2FC15220D8)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8C14187C-6D39-4E1A-BF87-623D58AFC283)
- [DBMS_CLOUD_OCI_OPSI_AWR_QUERY_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-31327018-EB2E-4666-B1B2-05A3F233BCB0)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5179984D-FE84-40DB-BD5F-9AF0CF0B99C3)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BC657C8E-360D-483F-8090-0E4ABFCD1A31)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_CPU_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EDB77AAD-30A7-4AA5-A5DC-4D577CB14CD9)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_CPU_USAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A0C14BFC-AB14-4CAC-89F8-C0D4C728B36F)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_CPU_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-00505FE1-F5EB-4DC7-A449-33B42406885C)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_METRIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-26B4CE97-544B-4BC9-B16E-37814B97F133)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_METRIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EE3DCBF8-92BB-4934-91C1-0BBE18974605)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_METRIC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E7E244EA-A65A-42DF-8865-3BA0FE7F97D8)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_CHANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6E1D5BDA-ED1B-4C11-A4EB-238060EF8F90)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_CHANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-54E54D04-B98B-4CE2-B338-3410380A69B4)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_CHANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CBDF5F26-4A1A-4B5F-8CD4-2CB68A666D8F)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6969001F-D5A7-45E3-B460-7B115AC46120)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6991E3C0-8058-40D6-BE99-7F842782415D)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_PARAMETER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1E8411CA-F799-4BB8-B296-087F483E139A)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C119C3E5-A600-4BD3-A288-919058B88655)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C109E311-94AE-453A-A1E2-9AA33536283A)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1651A120-6800-42B0-98FA-FEB7C88C745B)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A48116EA-6141-43EA-BF0E-7F99972D8CC8)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_RANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6A8C6AB1-23D2-4E79-839F-3F493407BF87)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_RANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C8EA43FF-2B4B-4D5F-8EA0-79AD3A4B1A5B)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SNAPSHOT_RANGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-070385B2-5113-44FB-8D10-19ABEB8BC6DB)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SQL_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-69B1C18C-B371-41E9-830B-A740069A5580)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SYSSTAT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-115312C0-2B87-4BCB-8716-A2CE1ADEC6AB)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SYSSTAT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-42B825AA-1409-408C-9B37-A31C3B788C99)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_SYSSTAT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CFF3A859-9A73-4FE0-89AE-BEBBCD152E8F)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_TOP_WAIT_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B7801BD2-E2E7-43DD-AE07-90EB956FB35A)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_TOP_WAIT_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-92F148AA-E794-4655-A04E-8AB7F515CEB6)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_TOP_WAIT_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2A010C95-D6BE-4C84-B71F-64DC60DC008D)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_BUCKET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-517CA357-3ED3-4CBC-A4ED-76CF9A4432FF)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_BUCKET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-52E7CAFF-B901-44FE-917C-8DC06729EDFB)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_BUCKET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BE18CE6C-C03B-4468-A270-869C998F5038)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-06FC1523-B094-4160-8B6F-40A9F5618364)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2A9B1890-37B6-43F5-81EF-83F77F9A0F85)
- [DBMS_CLOUD_OCI_OPSI_AWR_DATABASE_WAIT_EVENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-02058218-DAAA-4F46-8557-583D93DAAEBC)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C53B74AC-1CF1-48C4-9F3E-9CEC48DF50D8)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_OBJECTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3FCB4F06-20A1-46FB-9916-D86F3DE5574F)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EB27C273-4E7B-423D-BD11-0F2022EC30DF)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BF485115-2713-4BA9-94F5-1C2926DE4196)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-21F47588-462B-4025-B63F-77F1FBBB3E3D)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8C49D6A8-8CD1-4EF2-95F0-E8D4952530FD)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SOURCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DB140685-9B84-4965-8435-0BB20991AF41)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-19B16231-D136-4DBA-A390-4466DD9982CD)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-863097C8-A527-441C-AE45-0A06692EE325)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUB_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2245CF07-12DF-4BBE-A0C0-1A71575931BB)
- [DBMS_CLOUD_OCI_OPSI_AWR_HUBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EDFCE046-DFF2-4E13-AB9A-C04283B17879)
- [DBMS_CLOUD_OCI_OPSI_AWR_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-342A3961-BCBA-460C-8523-F89BCC2E5271)
- [DBMS_CLOUD_OCI_OPSI_AWR_SNAPSHOT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8F41EA40-D489-4399-9635-A7451D0FA518)
- [DBMS_CLOUD_OCI_OPSI_AWR_SNAPSHOT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-35448AC5-79FD-499E-88DC-6501CA81A1E6)
- [DBMS_CLOUD_OCI_OPSI_AWR_SNAPSHOT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-24562EF5-1048-4A93-815E-96E99B794BE7)
- [DBMS_CLOUD_OCI_OPSI_AWR_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0DF337D2-788D-4AA2-962A-5475F8EF495A)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_UNIT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BAAE51B5-AC58-441C-98FB-68D8ED5C8D8B)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_ALLOWED_VALUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4370030F-3E4F-4C6C-B604-0D0978286457)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D36A39C2-86A3-4E29-8D87-712466F57BBA)
- [DBMS_CLOUD_OCI_OPSI_BASIC_CONFIGURATION_ITEM_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-166467C4-1E33-4C30-8A93-9D591A2ADDDF)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-91103A35-EAF1-4AB2-9B91-6DEAB927D6B9)
- [DBMS_CLOUD_OCI_OPSI_BASIC_CONFIGURATION_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D5DEE8BB-BF4E-457F-B70B-FB322CA7E6F6)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8C0389DB-0729-43BB-84D3-5E17BC9AA631)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_AWR_HUB_SOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C255E8D7-A475-413B-96A5-6D3814B9E2A7)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_DATABASE_INSIGHT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1EAC4949-4E35-4FDE-A0BE-9006048E096F)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_ENTERPRISE_MANAGER_BRIDGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-351086DB-4B5A-431E-8D0A-42A12AF0A4D3)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_EXADATA_INSIGHT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9D5AE836-DB94-410C-9516-35A3FCD56E3B)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_HOST_INSIGHT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7732923D-7C15-4D5F-9DF6-EDF4BC49F741)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_NEWS_REPORT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CC1D998D-F6AD-4B4D-9D65-A01166E334A6)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-43D9EC77-067C-4028-BAB0-C659047E07F8)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_OPERATIONS_INSIGHTS_WAREHOUSE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-42AF60A3-18FB-43CB-B754-46C2EEDD8C2C)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_OPSI_CONFIGURATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C06D7B18-E9E8-4BA1-8AFE-49C729BA6B93)
- [DBMS_CLOUD_OCI_OPSI_CHANGE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8D408396-67B1-4EDB-B8CB-82434C9A40B3)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A320BC0D-C7F2-4FC3-9ED1-986663C13FAC)
- [DBMS_CLOUD_OCI_OPSI_CLOUD_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-80D0D668-76F9-481E-9484-0787C611DCDB)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_FREE_TEXT_ALLOWED_VALUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A23E014C-2596-4CF7-A69E-40B42CDDCDA1)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_LIMIT_ALLOWED_VALUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F22261E8-CCB5-45DB-9E97-02F331BA1E08)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_PICK_ALLOWED_VALUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EECEDE83-4371-4C77-8A76-1F5203BA9FFE)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9F98F30F-8BA0-4946-956E-EFEC4BB05125)
- [DBMS_CLOUD_OCI_OPSI_CONFIGURATION_ITEMS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A8B5DD31-3024-4A1F-A0DF-F90FAF120C95)
- [DBMS_CLOUD_OCI_OPSI_CREATE_AWR_HUB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D9DAEE1A-FE7C-4FC8-9E77-AACD48D500D3)
- [DBMS_CLOUD_OCI_OPSI_CREATE_AWR_HUB_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-39CD09D7-B5A4-4EF1-A10A-7BA1A0BAE2EF)
- [DBMS_CLOUD_OCI_OPSI_CREATE_CONFIGURATION_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-89A043B6-3B1B-450A-A4E5-C4354EF69F77)
- [DBMS_CLOUD_OCI_OPSI_CREATE_BASIC_CONFIGURATION_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5C45C077-CA88-4297-BD2A-5DA0D14E46E0)
- [DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-85A1EC62-95FB-4089-AE5F-045BDA22D2AF)
- [DBMS_CLOUD_OCI_OPSI_CREATE_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4965398D-8925-4885-B518-20FB2A63B58B)
- [DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-34516DBC-605A-41B3-8207-6CAC2D44CD20)
- [DBMS_CLOUD_OCI_OPSI_CREATE_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A4E66283-0760-43FB-A223-ED0312ED0826)
- [DBMS_CLOUD_OCI_OPSI_CREATE_EM_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0F2DA250-4FB6-45A2-B944-39B62A5B09E8)
- [DBMS_CLOUD_OCI_OPSI_CREATE_ENTERPRISE_MANAGER_BRIDGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-51C49CBB-9D98-46E9-98F6-64E6FFE900E0)
- [DBMS_CLOUD_OCI_OPSI_CREATE_MACS_MANAGED_CLOUD_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9CC68E6A-2082-430F-9335-28B3EC1D9FFA)
- [DBMS_CLOUD_OCI_OPSI_CREATE_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-981B2DFE-B9B4-48A0-A572-C30B424FD6DF)
- [DBMS_CLOUD_OCI_OPSI_NEWS_CONTENT_TYPES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F744DE2C-DE03-4232-9687-A4ACE3245B24)
- [DBMS_CLOUD_OCI_OPSI_CREATE_NEWS_REPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-67CFCCF2-4845-4BF1-BBBA-FCDBCF8A3E51)
- [DBMS_CLOUD_OCI_OPSI_CREATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F99EAA3A-30F2-4C7B-8DB3-DEBCC98F11F6)
- [DBMS_CLOUD_OCI_OPSI_CREATE_OPERATIONS_INSIGHTS_WAREHOUSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8D6E8F0D-6008-494F-94D6-5129B6BEC738)
- [DBMS_CLOUD_OCI_OPSI_CREATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7EB2D46D-8FCA-4031-B5DF-EDC19BD71629)
- [DBMS_CLOUD_OCI_OPSI_CREATE_CONFIGURATION_ITEM_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-73FA5840-2907-4884-82E6-4AC125292AAE)
- [DBMS_CLOUD_OCI_OPSI_CREATE_OPSI_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D481274E-147A-4BFA-B5AF-7A7A76F673AD)
- [DBMS_CLOUD_OCI_OPSI_CREATE_OPSI_UX_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-87631828-FA04-4569-B5FF-B4EDF9ED85B5)
- [DBMS_CLOUD_OCI_OPSI_CREATE_PE_COMANAGED_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-60DCFD41-85CD-4C02-B940-B6B5ACE01836)
- [DBMS_CLOUD_OCI_OPSI_CREDENTIAL_BY_VAULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-603976F6-C25A-46F6-BCD4-AB893D9AD6FE)
- [DBMS_CLOUD_OCI_OPSI_CREDENTIALS_BY_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3AEB498A-5D1B-43BA-B61D-B86028F4C996)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_METRIC_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8DA9638F-9DC5-469E-8344-73C532D2AEDA)
- [DBMS_CLOUD_OCI_OPSI_DB_EXTERNAL_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E0772004-6755-4816-93E5-116C6E25644B)
- [DBMS_CLOUD_OCI_OPSI_DB_EXTERNAL_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C5D6624D-A220-4D1A-B603-8B507976D855)
- [DBMS_CLOUD_OCI_OPSI_DBOS_CONFIG_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AB9569E8-09FF-44FE-B006-79C8981FD67E)
- [DBMS_CLOUD_OCI_OPSI_DB_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0C1C5F4B-EE85-4C18-AB82-C480419FC94A)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_BIND_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BA1A3C2D-E644-4C48-B8A3-B3A439BAC9E8)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6D2E6BC6-C662-4382-B830-FE1FAB894570)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_COLUMN_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BBF4E40A-5E78-44A5-895E-A233BA416EEB)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_CORE_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-180BC494-5DEB-4237-8E73-7F005E364A60)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_CUSTOM_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3C4E7A9D-22B5-45D4-98B9-6D465DB8E1C8)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_DATA_SIZE_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6DF30876-6F97-4E29-AF20-36FF19036194)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_FREQUENCY_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-69EF1FF3-4FA2-412D-BCF6-FEF121FAD9B3)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_OTHER_STANDARD_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-61D99B4F-C3E9-4B19-A68D-738485885E74)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_POWER_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6EEBCEF7-F609-4DB9-BBAC-2350FEE39040)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_BIND_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-743E0B40-D863-40EE-9551-B53797C46669)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E1E60F23-1DAB-48F5-BBE9-4115376B8BFE)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_QUERY_TIME_FILTERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F00D0B7A-D146-479A-85C1-CBC2A5953CAB)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_RATE_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-28C6DE10-CB0F-4FB6-BBA2-F80A5B18AF02)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_STANDARD_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1B3EAC76-3F19-42C4-8B17-5BDAEB7DCEF0)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_TEMPERATURE_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-71A1DA0D-9335-44B5-A2F8-7B72BBE8A01D)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_TEMPLATIZED_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D3422EF8-83F8-4D50-99BA-F545972EFC48)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_TIME_COLUMN_UNIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C76A2AC6-F892-4021-AD48-21B53F739569)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-08C0DB5D-5EE9-4C4E-AFB9-382960CBCB4B)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B01EA8D5-CCC4-4927-BAD7-7E0BD69A3583)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7791D737-2AAE-4B8F-BF60-6A28F0E8B164)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DEA9D785-B77E-4DA9-8F6A-8BFB452F8ACC)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-49923972-3D33-4483-A1BE-65E9E543601A)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUPPORTED_QUERY_PARAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3FBF00C1-BB27-44BE-B192-DBB815446024)
- [DBMS_CLOUD_OCI_OPSI_DATA_OBJECT_COLUMN_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-16663E8A-3F92-487E-AE6C-7F0E94489427)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUPPORTED_QUERY_PARAM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E557C6DE-6179-435F-9D44-CD2AC73882AE)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D78879C4-A157-4F0C-9DEA-998C18222853)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_DATA_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-099FBFDC-81D3-4E3B-8BC0-2ABA4BA16259)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EDCFF49E-7053-493F-9B5B-BF362E5A9A55)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_INSIGHTS_DATA_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D0E88379-AD3B-4BA6-BBF1-09243D46B37F)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_PARAMETER_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D4F26A0A-35CC-4E51-B4B3-DDD267A28338)
- [DBMS_CLOUD_OCI_OPSI_DISK_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B5641796-FB71-43FE-88E9-5AE265BBEBE0)
- [DBMS_CLOUD_OCI_OPSI_DISK_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4B977377-6D05-45F8-B16F-DF36C6FE6688)
- [DBMS_CLOUD_OCI_OPSI_DOWNLOAD_OPERATIONS_INSIGHTS_WAREHOUSE_WALLET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-64DC653D-0642-490A-AC4B-85D70A766FCF)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-09AF9C29-9CBD-4E74-87E6-BAFE63942080)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_DATABASE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B51FFBAC-CB2C-4995-970C-A2C4325F9C84)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-25CF1074-13B3-42EB-B070-E0B375F13DCC)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F5FE7EC2-5D13-48B7-B97E-3CBDC633C2DC)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-76563897-F55D-4688-9361-0BB218F25280)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9FD151B4-6B0E-4CE2-A5AA-C0BD8D48FEDA)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E82F7C27-53A9-4F11-AB4E-7DB64CD4D018)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4DE7800C-3D82-461B-86F1-EDBBC9C4EAAD)
- [DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-56050838-B96C-459A-977A-602B85470BB1)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_HOST_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-29AC9BED-3933-4398-A115-608A222CD3A4)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DCD2408F-DCA7-4A7A-AD35-3D014540E1B1)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_HOST_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6E3C3069-23B8-4AA3-865A-CF15D0915250)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-16E33E79-DE31-4086-833D-672489A4231A)
- [DBMS_CLOUD_OCI_OPSI_EM_MANAGED_EXTERNAL_HOST_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-72E9CBC3-E830-471E-B515-103F491A3513)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7EB6DEED-4E3D-4F50-8D4D-D7FAA7D7720F)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-70001866-27C6-4501-845B-94E1E7E62E2B)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4A9E5F68-6701-4B02-B4ED-E2DA69726171)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8142F99E-5B01-40D1-8A18-8F4259FBD113)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-47AE6F5B-6547-4532-8361-F979C210BAA0)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0A8872E1-7CA0-4907-8957-1E65F64BCE9A)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_EM_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AAA3C1A3-33D4-415F-963F-6015F4F16A8B)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_MACS_MANAGED_CLOUD_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-392436A8-FF90-4664-BE08-3AE53D405DA8)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CE02FD23-6B7A-4CE1-BC9B-13321C5AF58C)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-205341B1-B7CB-4DD8-933D-325A99BD5B3D)
- [DBMS_CLOUD_OCI_OPSI_ENABLE_PE_COMANAGED_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F16538EF-FA01-4139-AE5C-35B85B31D62F)
- [DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-68561655-115C-477B-8E69-057ABD1EC576)
- [DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-10B8A7F1-7756-403E-8F96-B95D2CCC7E03)
- [DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5B2566F9-45CC-4495-A204-6C5E8A9F9672)
- [DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2A34B4C9-351F-47F7-8B42-B023A3438CAA)
- [DBMS_CLOUD_OCI_OPSI_ENTERPRISE_MANAGER_BRIDGES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7B8732A4-05AB-428A-B394-BBC0B45C99A5)
- [DBMS_CLOUD_OCI_OPSI_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-12FF3935-97B2-4AC9-AC29-4E7080EB03FA)
- [DBMS_CLOUD_OCI_OPSI_VM_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F8D3A91B-FA43-41FA-A97B-83F10D9D233B)
- [DBMS_CLOUD_OCI_OPSI_VM_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-59EC6210-88D2-4173-9D51-F8094B3B7A5D)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3AA467F2-5DE7-42FC-9F1F-DBE742706226)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1359BF62-D427-475B-A141-E991BD6411A6)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C5189C88-0152-4C74-9E09-AF4BFEC1DA04)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_DATABASE_MACHINE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C765D275-D6A7-4A1E-B6D3-BDC94D3C344A)
- [DBMS_CLOUD_OCI_OPSI_INSTANCE_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-09F8AB1B-03A5-4E93-963E-58CBAEBAA251)
- [DBMS_CLOUD_OCI_OPSI_INSTANCE_METRICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1341AF1F-FA16-4AE7-9504-49B33E8EBFA9)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3E9C9723-123F-4E93-8617-D99FEFCD9044)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C229D338-EC14-4BAB-8D83-1A5060871BF1)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_DATABASE_STATISTICS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-285B5976-43A8-4F43-81B5-2DD7AC0B69DB)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_DISKGROUP_STATISTICS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-409B8ADB-E0E4-4A30-B272-AD1F2181E366)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_EXACS_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9774E3AF-66CB-476A-AFD8-7B93DFD0C146)
- [DBMS_CLOUD_OCI_OPSI_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2CB44126-3DB7-4179-9401-C598293D6458)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_HOST_STATISTICS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-29C6BFE7-0C58-4D05-958A-4988048931C9)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A7E57157-A77F-49EA-84D1-9FB2F203EB4E)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-28BCB913-5027-4969-8462-3AF7443C33AC)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1BE8DDF1-FD2B-48C4-907E-FC4F66829F70)
- [DBMS_CLOUD_OCI_OPSI_HISTORICAL_DATA_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-03D466CE-4881-42A9-BE68-FC4033796DB3)
- [DBMS_CLOUD_OCI_OPSI_PROJECTED_DATA_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-339D5779-9644-4153-8091-714C04E6C81A)
- [DBMS_CLOUD_OCI_OPSI_HISTORICAL_DATA_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-403743AF-8B05-4243-B747-554ECE81A4DA)
- [DBMS_CLOUD_OCI_OPSI_PROJECTED_DATA_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-96605CA2-7DAB-475E-ACBF-CA837BB597C5)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BEFD581D-E8F0-4D84-A5F5-90D69DE4E374)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_INSIGHT_UTILIZATION_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3D6A1144-C6E7-40BB-939A-8D21A8D61BD2)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-98F4FBF7-E964-4992-9B9A-859BA5F09D5C)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D736A324-E0B4-454D-A310-FFB21E09BE89)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2428B43A-ED7B-4743-9DF7-59BC73DAE619)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHTS_DATA_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6BD4BCE3-DDF4-4372-9FF1-3ABF4436978B)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHTS_DATA_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-50788522-3679-4CF2-BBA6-B691C7574FC5)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_MEMBER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4CD669D4-BBED-44C0-A398-90C9C25F1452)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_MEMBER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-145213B3-0683-4EC9-8438-817BCDD304E5)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_MEMBER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A6585901-A266-436F-B340-BFA54FB3AE27)
- [DBMS_CLOUD_OCI_OPSI_STORAGE_SERVER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CC617CF2-98A9-47F7-9F85-68E308612E54)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_STORAGE_SERVER_STATISTICS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F53FFCA9-5F2F-4D1F-8B4F-B1F4CCD9E9EA)
- [DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B8443578-342F-4D7F-B1F1-C02565E8313B)
- [DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-115CE178-0C47-4A9B-8570-E377B99E7FAB)
- [DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_METRIC_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-58D0CCD8-F8C4-4C49-A14F-0149DE86F25A)
- [DBMS_CLOUD_OCI_OPSI_HOST_CPU_HARDWARE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4AE96E92-C5CE-4726-80C0-D8B6EB7CA8E4)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_HOST_RECOMMENDATIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-32B752DE-7534-4724-B211-971D07BA3C17)
- [DBMS_CLOUD_OCI_OPSI_HOST_CPU_RECOMMENDATIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BF21A72E-A62D-406D-A515-EF369AC81B1A)
- [DBMS_CLOUD_OCI_OPSI_SUMMARY_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0929756B-51B9-4772-8CB0-3EE79BBC4E14)
- [DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1FEEA993-8570-465A-B419-14068D8E6183)
- [DBMS_CLOUD_OCI_OPSI_HOST_CPU_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A3B620B9-55FB-4639-9341-DD8DC2B7D918)
- [DBMS_CLOUD_OCI_OPSI_HOST_PERFORMANCE_METRIC_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7F0C418D-75D1-4D00-A67F-82B95DD721DC)
- [DBMS_CLOUD_OCI_OPSI_HOST_CPU_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4D41AA00-883E-410B-ACDC-949536EB825F)
- [DBMS_CLOUD_OCI_OPSI_HOST_ENTITIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C1C077F6-2ED2-43C7-815B-FC59AE5510CC)
- [DBMS_CLOUD_OCI_OPSI_HOST_FILESYSTEM_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-21BA938B-1627-416B-8932-9AE604CB8526)
- [DBMS_CLOUD_OCI_OPSI_HOST_FILESYSTEM_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D4521FA7-E62D-48A4-9518-A59BEBCE093D)
- [DBMS_CLOUD_OCI_OPSI_HOST_HARDWARE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E677CF62-78D6-4B92-AA47-65DCA10CF580)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_AGENT_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-ED4DEC72-67B9-468C-A13E-63E572A6EA64)
- [DBMS_CLOUD_OCI_OPSI_HOST_IMPORTABLE_AGENT_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B96FBD42-96ED-4EFD-BEC8-1184B18594C3)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-970F9422-3BB5-4806-858F-2784BD20E3AB)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-713907A5-BE40-40F4-B0B0-31240D4699D0)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B4621904-314B-4A49-9501-FEFA4D59F365)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F0AC57E9-2EC2-473A-83A6-18DB38DEA379)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHTS_DATA_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5C5EC37E-1071-4912-9274-E6A368D33EEB)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHTS_DATA_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6E2650A7-2959-44E7-9D2D-37DF3779231C)
- [DBMS_CLOUD_OCI_OPSI_HOST_MEMORY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-802E7CCB-44CF-4082-92B1-70D935D738BC)
- [DBMS_CLOUD_OCI_OPSI_HOST_MEMORY_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0A2A0604-AF4E-4DF8-92AC-0D0552F33074)
- [DBMS_CLOUD_OCI_OPSI_HOST_MEMORY_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-87E2B59A-2ADF-42A4-9BA2-A01125C274CA)
- [DBMS_CLOUD_OCI_OPSI_HOST_NETWORK_ACTIVITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-430FFB12-75C6-4B9A-834B-0FF3937B3ECE)
- [DBMS_CLOUD_OCI_OPSI_HOST_NETWORK_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B50D3045-49CA-4E71-8E76-A68A7F20E111)
- [DBMS_CLOUD_OCI_OPSI_HOST_NETWORK_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8BC580E0-BBBC-49F5-B3EE-F2205C9B1209)
- [DBMS_CLOUD_OCI_OPSI_HOST_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-162A1BD1-08FD-4138-A1BE-A1588343933C)
- [DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_ALLOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-85F26C37-32D5-4601-B3FC-E5C601F19340)
- [DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A393E7F1-0A30-456F-9A8B-C05E8E6CA22C)
- [DBMS_CLOUD_OCI_OPSI_HOST_STORAGE_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2A8E412F-8359-4F29-BE71-710B49310D89)
- [DBMS_CLOUD_OCI_OPSI_HOST_TOP_PROCESSES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9A5CFCBD-4271-45C6-BB80-04C8D0C35B6E)
- [DBMS_CLOUD_OCI_OPSI_HOSTED_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5EF2D2E8-E7BD-4503-BE1C-69325897AAC5)
- [DBMS_CLOUD_OCI_OPSI_HOSTED_ENTITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8A229AB3-CF01-44B9-9474-3400D51178B7)
- [DBMS_CLOUD_OCI_OPSI_HOSTED_ENTITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-86C7F201-60FD-4681-962D-90227AB2EFD2)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_AGENT_ENTITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-95F99856-BBBA-44AD-BFDA-3ECD9F58AAA2)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_AGENT_ENTITY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BD6B8D15-CD4E-4B94-B231-78F6DB0977D4)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E8AE1C5E-4E8B-42A2-9FA5-9315FA63917C)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_COMPUTE_ENTITY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B33CB710-2929-4F08-BF6C-C18AF761FBAF)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_ENTERPRISE_MANAGER_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-451422DB-EBC9-40FA-8643-A89B3931E7C2)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_ENTERPRISE_MANAGER_ENTITY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-57C6DFEF-4E39-4619-8D43-5E16E220E82D)
- [DBMS_CLOUD_OCI_OPSI_IMPORTABLE_ENTERPRISE_MANAGER_ENTITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5CBBB4A8-CB95-420E-8C8F-28F5B78161ED)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_QUERY_PARAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8A1CA5D4-BE5A-4F8A-9C49-7B9FEA14C7FC)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_QUERY_PARAM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E990203A-8D7A-4D4D-872D-BA502644EEE3)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-94F2D2FD-156B-4579-940B-EBF03A1BBD39)
- [DBMS_CLOUD_OCI_OPSI_INDIVIDUAL_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EBD93E52-1AD1-4AF9-9E39-1AD62D6C9F68)
- [DBMS_CLOUD_OCI_OPSI_ADDM_REPORT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A6478783-9F81-4B57-BAFA-EC113D95A0DB)
- [DBMS_CLOUD_OCI_OPSI_INGEST_ADDM_REPORTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-97A18E5C-26F7-4C2E-AA14-32F48367C654)
- [DBMS_CLOUD_OCI_OPSI_INGEST_ADDM_REPORTS_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1D8E6DCD-11C5-4F9C-B4C9-71395DA7D109)
- [DBMS_CLOUD_OCI_OPSI_DATABASE_CONFIGURATION_METRIC_GROUP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-920947F9-438D-4C3F-AF51-37F879FBAF3C)
- [DBMS_CLOUD_OCI_OPSI_INGEST_DATABASE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3089F7F0-968C-4E4C-88E1-56D214E3C12E)
- [DBMS_CLOUD_OCI_OPSI_INGEST_DATABASE_CONFIGURATION_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3FFFCE9C-1E8F-4AA2-BDE8-E74CC78B14A1)
- [DBMS_CLOUD_OCI_OPSI_HOST_CONFIGURATION_METRIC_GROUP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C6E44D6C-5D9C-43CC-B6BC-3943FFC867F9)
- [DBMS_CLOUD_OCI_OPSI_INGEST_HOST_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1B5BEFE4-F71D-479B-8CB8-EEDBD40BAE26)
- [DBMS_CLOUD_OCI_OPSI_INGEST_HOST_CONFIGURATION_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-55A1099F-A66C-4F6B-9EDE-6114B6C67056)
- [DBMS_CLOUD_OCI_OPSI_HOST_PERFORMANCE_METRIC_GROUP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-44A31B6A-126A-4C2A-B7C3-B220090462BF)
- [DBMS_CLOUD_OCI_OPSI_INGEST_HOST_METRICS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-ABB147F9-E4B0-4761-BF0F-7FC541E59497)
- [DBMS_CLOUD_OCI_OPSI_INGEST_HOST_METRICS_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-132796B5-7C98-4B87-B76C-74868479EC06)
- [DBMS_CLOUD_OCI_OPSI_MY_SQL_SQL_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-09B08089-6506-4D76-A753-FB81AB611269)
- [DBMS_CLOUD_OCI_OPSI_MY_SQL_SQL_TEXT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-62A04516-BD16-4009-9490-7886B89DA510)
- [DBMS_CLOUD_OCI_OPSI_INGEST_MY_SQL_SQL_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C0AD8851-3669-42A4-9A35-DDE9B5C9B456)
- [DBMS_CLOUD_OCI_OPSI_INGEST_MY_SQL_SQL_TEXT_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1C85007F-10D9-4DC1-8FBF-B92D417F20DF)
- [DBMS_CLOUD_OCI_OPSI_SQL_BUCKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FCE647AA-8062-4408-9C9C-93D41758FB83)
- [DBMS_CLOUD_OCI_OPSI_SQL_BUCKET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E0CDB08A-FEAA-4965-9D22-255EADF992D7)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_BUCKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3805CFE7-8228-4301-99CF-7C12958390AA)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_BUCKET_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2319614A-5A54-4BB0-B47F-151E7FB00DBB)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_LINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-482EB8F9-A640-4BE7-A9F7-437C7EB5003C)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_LINE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2EDF4AA2-4699-4AD9-89AA-966056D7F932)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_PLAN_LINES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E21E9FDF-9C34-46A9-88F5-B6FDFC271C5F)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_PLAN_LINES_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D3809E34-C2A8-4784-AF3C-4FF0D77CE9E1)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D00DA832-C2D9-4EC5-B30A-CA3C200D50B8)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3BE608B9-CB57-4343-BAC5-5981AEA81C6E)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_STATS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1AD3E154-31F8-4CBC-9DFC-4B53FCF523EA)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_STATS_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B87D1B7A-6B59-4FC9-988B-ED86B78A145B)
- [DBMS_CLOUD_OCI_OPSI_SQL_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F4625F19-02C8-4CC1-8607-8140EEDF84F6)
- [DBMS_CLOUD_OCI_OPSI_SQL_TEXT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F800E6EA-5B3D-48D5-8958-A198C2D2F082)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7933343E-C38A-46A4-82CD-7B73F9772C2E)
- [DBMS_CLOUD_OCI_OPSI_INGEST_SQL_TEXT_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-91AA9FA4-C2AF-4201-AD66-1FC7EE6BFD89)
- [DBMS_CLOUD_OCI_OPSI_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2094A4F6-D558-4588-A2E5-355932B6919C)
- [DBMS_CLOUD_OCI_OPSI_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E331AE64-E56A-469C-B51B-BCCA716CC943)
- [DBMS_CLOUD_OCI_OPSI_LIST_OBJECTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6594000B-FC3A-4BA6-90C7-F0F7EB4E2D9B)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_CLOUD_HOST_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EECECEDF-7D24-4299-9F61-B441EF7A3DFF)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_CLOUD_HOST_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C52DD4EF-9544-4129-AE0D-65C216097E4B)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_CLOUD_HOST_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AE4FF75E-1F5B-41D2-9613-0FABE20FF755)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_DATABASE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0DC2913C-2639-4D87-9A95-ACDF10892CDB)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_DATABASE_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B4A056FC-26B9-4E20-A02C-050A27591A91)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_DATABASE_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1F773BB2-CF1B-4F55-9EA2-8948D4735ACE)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_HOST_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CAEC7F53-E9D4-44C4-A39E-B3A80749C553)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9D70F718-C1AF-466E-A9D9-B96AD1D90EAC)
- [DBMS_CLOUD_OCI_OPSI_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EB6FEB99-2DD9-47E2-839F-603AEC24FFCF)
- [DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E8C23324-5963-4D8D-A81F-7C228C498C89)
- [DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EC7B96CF-EA7D-43DB-8214-779E80F0B557)
- [DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EF40DA96-9421-437F-97FE-E132A94EB20E)
- [DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FF89AA31-FC0F-401D-ADBB-EA60CE09000A)
- [DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3FBDAF37-B95C-43D4-918C-D0B568DF1386)
- [DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1089EFF6-67BB-4F2F-8AF6-A51AF05C2C90)
- [DBMS_CLOUD_OCI_OPSI_NEWS_REPORT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-135EC109-43DF-4A2A-AB0A-A4181DF5C60C)
- [DBMS_CLOUD_OCI_OPSI_NEWS_REPORTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-35B82679-42B8-48CD-8B34-9849776C241D)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B866077E-9A12-4FF9-882D-A14E40E8C0F9)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-55CEE339-A2DA-456F-AA9E-59F3C20D6C43)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9592C2D3-10A1-461A-8BB1-CEE848A0342E)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-267B0D52-E113-4E21-827B-D6C8274950E2)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7BDCDAB9-31C0-4773-9333-7E23D29D3632)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-25A1EC6F-530D-43C4-8547-5D388E54DAD5)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-51E1D0AA-30C8-45A5-93BE-633A7B429106)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B6D6890C-9AF6-4A18-928C-1DB557430294)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E3A9EA01-5857-4A3D-8D7C-C2F8FFC32101)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-99E31E79-6A19-4A57-B8B7-F7A90BC62B5E)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-83BE4F5E-25EF-4196-A908-A2E2428EB5BA)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USER_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-29B603A7-A967-4220-8168-96C27AC59D04)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSE_USERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-96F92EFB-B610-4928-95CF-78F91848322A)
- [DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS_WAREHOUSES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BEDB0C1C-07E3-4FCF-82CD-6A29D4E7BF84)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_CONFIGURATION_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C6DD584B-48AF-4A53-932C-6A3686E2B3DB)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_CONFIGURATION_ITEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AE94ED34-2CB1-461E-B721-C7B10B923CA7)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B0F8CFF9-A873-47EE-A470-6AC30EB02C6E)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_BASIC_CONFIGURATION_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1D16C47B-3231-48E4-A23C-4C888C11CB2D)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A7654DA0-0237-4959-9283-A66AC19E0053)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3191C944-B82C-4E93-AEF4-43FDC399179D)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CC388479-6104-4256-8A0C-2B9617911C5D)
- [DBMS_CLOUD_OCI_OPSI_OPSI_CONFIGURATIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3934E08D-A60B-4BB8-BF1D-3FA44C204641)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_TYPE_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3353648E-18E3-41A9-B6AE-FAA0B7F16E31)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8883F92A-17C1-40DA-AB7A-562DCE5605B2)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-076CF752-B0FF-4B89-964D-3E58F26FA21D)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECTS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-795BB22B-F117-4E2F-945A-68CDA470891B)
- [DBMS_CLOUD_OCI_OPSI_OPSI_UX_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A8F707B8-58E6-40AC-B9BD-E47AA510AE34)
- [DBMS_CLOUD_OCI_OPSI_OPSI_UX_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DF055FFB-9A03-422B-99C5-577513E0AD37)
- [DBMS_CLOUD_OCI_OPSI_OPSI_WAREHOUSE_DATA_OBJECTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4423E878-F25C-4A0B-B7A0-E32097F63298)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A6167ACD-DF15-4C17-B958-73C5D07BA68A)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_DATABASE_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-37E2BBC2-E9AD-4866-8ECD-FD0625B5C86E)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_EXADATA_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FB804BE2-D34C-4D11-9CF0-FB62A89D39B7)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_EXADATA_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6F1DD4A9-ACA6-45FC-86A9-D34B9703387A)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_HOST_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D4F56A19-5F6A-4958-8D1C-F8D94222FBB9)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_HOST_INSIGHT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D96748F5-C931-4500-8B3D-EE172A07A80D)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_HOST_INSIGHT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C990FA54-BEB9-406F-8BE0-7EABE93523F9)
- [DBMS_CLOUD_OCI_OPSI_PE_COMANAGED_MANAGED_EXTERNAL_DATABASE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E282B44B-5DC5-4C9C-A16E-247865CC8FEE)
- [DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_RESULT_SET_COLUMN_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6F23C914-D7ED-4923-9B5B-953D492A046F)
- [DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_RESULT_SET_ROWS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5C041022-0E6E-4BC9-863D-494562E33F7E)
- [DBMS_CLOUD_OCI_OPSI_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-87F9CEE6-F9C0-454B-8D40-FE23644B928B)
- [DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_RESULT_SET_COLUMN_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F2A26785-1F88-4ACB-BB8B-33CE24D54B30)
- [DBMS_CLOUD_OCI_OPSI_QUERY_DATA_OBJECT_JSON_RESULT_SET_ROWS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D70FE0C3-7D71-4B87-9862-1B18AD9E00B2)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_FILTERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8646D528-12F2-4F55-B416-0C74EE9AB3C5)
- [DBMS_CLOUD_OCI_OPSI_OPSI_DATA_OBJECT_DETAILS_IN_QUERY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-90E67B04-A1C4-4370-BC98-DBA8944E8EA9)
- [DBMS_CLOUD_OCI_OPSI_QUERY_OPSI_DATA_OBJECT_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4925163E-2482-46AF-B848-1045060F0CC5)
- [DBMS_CLOUD_OCI_OPSI_QUERY_WAREHOUSE_DATA_OBJECT_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F5539A3B-2DBD-4927-9704-AD02FB7EB980)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4519652C-80C7-40E4-82FD-DB5CFFB83A3A)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_CURRENT_UTILIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6E32E8EB-30F8-4434-BBF9-48BD7BB1B8D4)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_PROJECTED_UTILIZATION_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0BF6AD62-D6D6-4F01-9A42-B26F89A8144F)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_PROJECTED_UTILIZATION_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0A715E04-1D4D-44CC-8309-CF2679AE3F4C)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_INSIGHT_PROJECTED_UTILIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7DF3140C-928C-46EA-8336-1F41775CBFE2)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AEEBA85C-9AE7-43B3-A821-0071DC1FF7BC)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_STATISTICS_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6833FC82-CEE8-4D78-8176-D76FE84CAB6F)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1D8E9B11-1405-445C-9522-4F35B5850BA3)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C6F4C21C-CC59-4085-83DA-816D9DC26A37)
- [DBMS_CLOUD_OCI_OPSI_SCHEMA_OBJECT_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FEC79852-3209-4C82-81D2-32BCFAE98792)
- [DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-90FDAF9E-BB96-4740-8CF4-BB62A8ECDF70)
- [DBMS_CLOUD_OCI_OPSI_SQL_INVENTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3B4D9976-5025-48E7-8915-D05DDD2440B8)
- [DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_THRESHOLDS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-06B78344-7B8F-4B8E-A7F2-A1A9D28DE089)
- [DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4C6708A1-5185-484C-A120-403E4F6C83EA)
- [DBMS_CLOUD_OCI_OPSI_SQL_INSIGHT_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A76582F0-6502-4CE1-9B28-84FE247CE4F2)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-24D0DE95-62DD-4091-9D53-DEDFC3E02BFF)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8111A6E3-1711-4E9B-82A2-1CCCC91B3371)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C0820804-6B1D-4066-ACF2-4371B4E0F579)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F3248522-4E51-482D-8A0B-A259CEAB7B8A)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-67F8B2DA-2B34-4B5F-B2A1-E3D1E159E059)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHTS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4F66AFE0-5B77-4649-B662-0EFFE5DCB06C)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHT_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CB85B668-A807-4DA1-A413-03BC950E13C1)
- [DBMS_CLOUD_OCI_OPSI_SQL_PLAN_INSIGHT_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3B943327-F80F-4FFC-9DC1-70D3167FEAA8)
- [DBMS_CLOUD_OCI_OPSI_SQL_RESPONSE_TIME_DISTRIBUTION_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-08015BBA-7E94-44CB-B896-1B55BE9B8B3B)
- [DBMS_CLOUD_OCI_OPSI_SQL_RESPONSE_TIME_DISTRIBUTION_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F1DF06E3-7523-4003-8C8D-9F1853D93DAB)
- [DBMS_CLOUD_OCI_OPSI_SQL_RESPONSE_TIME_DISTRIBUTION_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-37868F56-B3EE-4CD3-8C65-96C189FCA609)
- [DBMS_CLOUD_OCI_OPSI_SQL_SEARCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-29FFAFD2-479E-42A0-85A1-41B57B2C0DD5)
- [DBMS_CLOUD_OCI_OPSI_SQL_SEARCH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3E28716E-8731-493B-869A-14AA95E43D63)
- [DBMS_CLOUD_OCI_OPSI_SQL_SEARCH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FFDE61E6-D5A0-41D1-BB1D-55534DFDF420)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-241B3B93-678E-4A87-ABAD-9A7D265B8D28)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTIC_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-62859553-E25C-485A-9C67-53EB9D08843D)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTIC_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-58CEA5EB-869D-4680-81D3-FBD44D7B104B)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTIC_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8EAE43DA-6F6D-47B7-A79F-4E7080529F16)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-738841C9-FFA7-413B-BDF5-D7DB51014C94)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-13E93FFE-E083-448E-BFBC-FA3D6E2F32A1)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AE4F0D19-F587-4EBF-A9DC-895DD67CDDE2)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BB610B9C-255E-4DBB-BF84-A1B42267CDDF)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A9565CB2-3177-41E3-BC76-7B15202F11F2)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_BY_PLAN_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B74F9306-BF3D-437A-AE98-DB893E0C1DEF)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_BY_PLAN_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-56CCC63C-542E-45BB-9FB6-77200AF5D536)
- [DBMS_CLOUD_OCI_OPSI_SQL_STATISTICS_TIME_SERIES_BY_PLAN_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-66F4B000-098C-4170-B27E-2E0B8C42C95C)
- [DBMS_CLOUD_OCI_OPSI_SQL_TEXT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F616EDB6-A363-4FD1-9216-61EE7B43F64B)
- [DBMS_CLOUD_OCI_OPSI_SQL_TEXT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6A52848D-E48B-4FC7-B7B1-7C3043B7D2B6)
- [DBMS_CLOUD_OCI_OPSI_SQL_TEXT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CED33C34-426F-4385-AC04-AD6A071D406D)
- [DBMS_CLOUD_OCI_OPSI_SQL_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AFCA2E19-1D2A-427B-A4F1-1E420CFEBFF6)
- [DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-E68A508C-B5DF-4FEE-9D21-8ED11A08F42C)
- [DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-26B6D001-DBDE-442C-A3EC-4AE0CBD334A6)
- [DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-615F9063-2D47-485C-8535-194B6F999E33)
- [DBMS_CLOUD_OCI_OPSI_AWR_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F09751E1-5899-4302-8DD8-04918E83662D)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_AWR_SOURCES_SUMMARIES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-83640487-219A-42C2-8EFE-85AF6D517E27)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_CAPACITY_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-46D0C4FA-836E-4A26-8F75-7D7A4C7B9037)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-01100152-DC48-4977-8102-8B439334DFFF)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-991EBBB9-D9CF-4DBE-AFBA-36AAE2E3B972)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_STATISTICS_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A5C28311-83FE-4016-A013-35B363229C2F)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BA180159-C66E-40F0-B7B8-8A8D4285E917)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-46A1462A-A8F3-4884-980D-96663C99163E)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-40F40857-7010-455D-9450-E14E737AFBFA)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9F42E83D-0E02-4F9E-B13F-FEB516750ADC)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-220FB6D9-12C2-49B7-83BE-E273CD20C891)
- [DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1C197362-908E-4CCF-8D80-F978B7262077)
- [DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C9B6C323-84D2-4B9E-8903-0AAF7F44A781)
- [DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3BE63EFB-10A9-46D5-8801-9743EFBDD5DB)
- [DBMS_CLOUD_OCI_OPSI_TABLESPACE_USAGE_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4BFCB9D4-0AA3-4A42-AA55-09C2F7DFD067)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_DATABASE_INSIGHT_TABLESPACE_USAGE_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6DAFE756-1BF1-4C68-9558-EFD035C5ED3F)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DB79D971-3396-464E-9542-4F8F4AF85529)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-86C24988-5EE6-48BF-AEFA-3962CA3826A9)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CABB7FC1-F372-454B-9E51-DDD752A96AFF)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-15AA4B4A-5E3E-479B-8CFD-620ABB48790E)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AE18C81E-9219-4DC8-B46B-B52DA1507A71)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A7A16985-FEFE-4ACA-A35A-501FC1E01FA4)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-0140FBC1-9F65-4B44-A74C-7638957D9EFE)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-73D46520-CEE4-49D6-8286-10061F567942)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B6F50AC0-CB8E-470B-9336-6CE940F857B2)
- [DBMS_CLOUD_OCI_OPSI_RESOURCE_USAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D421ED52-ECE0-425B-B6D0-195D503A64C5)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-81DB4AB3-82EF-4ED8-808B-65221BDB2274)
- [DBMS_CLOUD_OCI_OPSI_EXADATA_INSIGHT_RESOURCE_INSIGHT_UTILIZATION_ITEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2EF88AA5-BB4C-44DD-B498-9BA0A3AAD87A)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_EXADATA_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BF766039-C607-47E8-8264-A8E70604FD66)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_HOST_RECOMMENDATION_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4E99C478-71F9-44D0-A2E6-0D1FF9DD1392)
- [DBMS_CLOUD_OCI_OPSI_NETWORK_USAGE_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8D4F2380-0CC9-4E76-A611-426A4429BE56)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_NETWORK_USAGE_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-40A9AE6E-3D13-4262-9AD3-26CBF8AFD322)
- [DBMS_CLOUD_OCI_OPSI_HOST_RESOURCE_CAPACITY_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7729ED39-FC8D-40BB-809F-72F69831D795)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BD2EE453-6224-445C-9AC1-2B2D903FFCCE)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-366EFBBE-1712-45D1-8959-EE96270D2B1D)
- [DBMS_CLOUD_OCI_OPSI_HOST_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-9972656B-1D29-4432-9311-21E8BBBFD0C8)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_STATISTICS_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-34C3B5D0-6391-4D09-9492-6F55286AFFAA)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2D69891C-CA28-459F-8CDD-D9EF7CC20473)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A6C998D1-22F7-48E4-B6B6-00629A07D6C8)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_RESOURCE_UTILIZATION_INSIGHT_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F5131CE1-A57A-426F-BE60-EB179F4636A4)
- [DBMS_CLOUD_OCI_OPSI_STORAGE_USAGE_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F6329FD9-DB00-49A7-B156-FF091DAA7E06)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHT_STORAGE_USAGE_TREND_AGGREGATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-13891DAC-A85A-4324-AB40-C8B7FA9819F1)
- [DBMS_CLOUD_OCI_OPSI_DISK_STATISTICS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EA9702D9-7B3E-4E24-9D5C-59142C7E5BFC)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHTS_DISK_STATISTICS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FA577D68-F7E4-4AF5-8091-FF9414EA348D)
- [DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8A78D594-B650-49AA-B884-460304C3282C)
- [DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6BD36E9F-BB08-4D34-92D2-6BE191D487EC)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHTS_TOP_PROCESSES_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6AC896CC-15BF-46A7-A532-E44DAF4FB7A3)
- [DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F2481040-DDA6-4DD8-B84A-4765B0B4760F)
- [DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-03FAC63C-58B4-4894-B9D4-CA85C9F5CD35)
- [DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1A4DFB0A-A8DD-4256-8369-BDBFA7A434A1)
- [DBMS_CLOUD_OCI_OPSI_TOP_PROCESSES_USAGE_TREND_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-72C002F0-40C4-459F-B9E2-A5C7C3930901)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_HOST_INSIGHTS_TOP_PROCESSES_USAGE_TREND_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-1DA2BD20-7F91-43DB-A4F8-E9A90182C0E4)
- [DBMS_CLOUD_OCI_OPSI_SUMMARIZE_OPERATIONS_INSIGHTS_WAREHOUSE_RESOURCE_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5754E166-7CC5-4624-8B2C-1DBA5F099E93)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-22DA1454-ABE3-44CA-927C-EABEB22FC481)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_AUTONOMOUS_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-585B747F-FA1E-4AF0-B3E8-4FB90EB0A5EA)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_AWR_HUB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-716F686C-C8DD-4544-B77A-A400ED1EE452)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_AWR_HUB_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-F053C928-C9CE-4719-82DB-7DD18C187C1A)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_CONFIGURATION_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-48DFC433-9923-4405-BE7E-4933CA38392B)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_BASIC_CONFIGURATION_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D3E04FC5-BE43-4BFA-942A-3F313C0CC79C)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_EM_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B9857BDB-2F61-4834-971E-F2D36FE503DC)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AE7FA250-EC07-46BA-9BC3-C4C21356CC6C)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_EM_MANAGED_EXTERNAL_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-4331BE93-BA7D-45DD-89EC-C11BA0F6EE3D)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-836A5B0B-EC40-485D-8617-E32E7298B548)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_EM_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-923E6C87-DE0D-4DB6-8103-52C16D361E03)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_ENTERPRISE_MANAGER_BRIDGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-71F18CE6-1CE1-4EDF-A6D0-CCBC2FDD4DF3)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_MACS_MANAGED_CLOUD_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-8423FF25-E0E9-4F91-8390-AB0F92D3F48E)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_MACS_MANAGED_EXTERNAL_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-04F1539E-33A8-40BA-9343-699177145D5A)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_MACS_MANAGED_EXTERNAL_HOST_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B16D6E6F-D026-4CA3-A8CC-DE2A458C8964)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_NEWS_REPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-ED29AE5C-4F14-431C-B45D-5FB974E1231C)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-ED539D29-8E2D-4AED-B86F-6F2BFBC93666)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-EFF8C4E8-CFBE-427E-917E-2FAEE2150CEC)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B9E3C428-B492-45E9-8DEB-D28C2A42703F)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_CONFIGURATION_ITEM_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-FAD0DD6F-5074-4173-AD89-F3F89FFA80DC)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_OPSI_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5BC223FE-6247-48C3-A86E-328699F8117E)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_OPSI_UX_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D4668694-8B1E-445B-877F-2896913C2AEA)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_PE_COMANAGED_DATABASE_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D53A5A90-D7EF-4C4B-8FA3-D98C31DC4E28)
- [DBMS_CLOUD_OCI_OPSI_UPDATE_PE_COMANAGED_EXADATA_INSIGHT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-AE95CC85-CA39-4822-BE83-AB317B3BE3BF)
- [DBMS_CLOUD_OCI_OPSI_UX_CONFIGURATION_ITEMS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BEEB4CC3-9631-4E9E-8F39-E99411A12B1E)
- [DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A7588350-4D94-4C8A-9B23-5C1C75A5A234)
- [DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-87E41D19-05FB-4E88-B0C3-9E2F6A34E343)
- [DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-CFAA6EC8-B43C-496E-AD27-2C7B93E649BC)
- [DBMS_CLOUD_OCI_OPSI_WAREHOUSE_DATA_OBJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-23766AC2-817F-4739-AD67-4286C70D930B)
- [DBMS_CLOUD_OCI_OPSI_WAREHOUSE_TABLE_DATA_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-C07C5DB1-E293-48BE-AE4F-75B5C70A03F0)
- [DBMS_CLOUD_OCI_OPSI_WAREHOUSE_VIEW_DATA_OBJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-151D080A-CD7A-4CB8-A444-44E5C76CCA19)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-B091DEBB-E9FA-437F-826D-73642C497E0F)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-70112E29-6F58-4ECA-AE1F-1C27A136FE6B)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-BB191029-E6F4-4F73-A77E-5D7753CF1429)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-6DC865F3-9B65-460E-88A2-35C0C6C8553F)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-3F75637F-0927-4C1D-B785-042D0508AFB1)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D3DE1BB3-B321-40B3-A702-4870EFEDB5D8)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-D67490CF-7CDF-4076-B2FB-EFF67488AE59)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-A16CCEE0-80B8-488F-BABB-D4DCE7A6B833)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-DE82EA26-B889-4F5C-BB7A-0A89B1E1AF3F)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-2BADE5F4-EAB3-4B2A-B56B-DB38D7EE2142)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-5D80126D-143A-410B-87B7-F3103A5DCB82)
- [DBMS_CLOUD_OCI_OPSI_WORK_REQUESTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/opsi_t.html#ADSDK-GUID-7367E9DE-3DEA-4A06-A906-1AFD1461572D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
