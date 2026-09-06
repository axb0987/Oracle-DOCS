# Database Management Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#dcoc-content-body)

## Database Management Functions

Package: DBMS_CLOUD_OCI_DM_DB_MANAGEMENT

### ADD_DATA_FILES Function

Adds data files or temp files to the tablespace.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`tablespace_name`

(required) The name of the tablespace.

`add_data_files_details`

(required) The details required to add data files or temp files to the tablespace.

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

### ADD_MANAGED_DATABASE_TO_MANAGED_DATABASE_GROUP Function

Adds a Managed Database to a specific Managed Database Group. After the database is added, it will be included in the management activities performed on the Managed Database Group.

Syntax
```

```

Parameters

Parameter Description

`managed_database_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`add_managed_database_to_managed_database_group_details`

(required) The Managed Database details required to add the Managed Database to a Managed Database Group.

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

### ADDM_TASKS Function

Lists the metadata for each ADDM task who's end snapshot time falls within the provided start and end time. Details include the name of the ADDM task, description, user, status and creation date time.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`time_start`

(required) The beginning of the time range to search for ADDM tasks as defined by date-time RFC3339 format.

`time_end`

(required) The end of the time range to search for ADDM tasks as defined by date-time RFC3339 format.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the list of ADDM tasks.

Allowed values are: 'TASK_NAME', 'TASK_ID', 'DESCRIPTION', 'DB_USER', 'STATUS', 'TIME_CREATED', 'BEGIN_TIME', 'END_TIME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_PARAMETERS Function

Changes database parameter values. There are two kinds of database parameters: - Dynamic parameters: They can be changed for the current Oracle Database instance. The changes take effect immediately. - Static parameters: They cannot be changed for the current instance. You must change these parameters and then restart the database before changes take effect. **Note:** If the instance is started using a text initialization parameter file, the parameter changes are applicable only for the current instance. You must update them manually to be passed to a future instance.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`change_database_parameters_details`

(required) The details required to change database parameter values.

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

### CHANGE_DB_MANAGEMENT_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves the Database Management private endpoint and its dependent resources to the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`db_management_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`change_db_management_private_endpoint_compartment_details`

(required) The details used to move the Database Management private endpoint to another compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXTERNAL_DB_SYSTEM_COMPARTMENT Function

Moves the external DB system and its related resources (excluding databases) to the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`change_external_db_system_compartment_details`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which the external DB system should be moved.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXTERNAL_EXADATA_INFRASTRUCTURE_COMPARTMENT Function

Moves the Exadata infrastructure and its related resources (Exadata storage server, Exadata storage server connectors and Exadata storage server grid) to the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`change_external_exadata_infrastructure_compartment_details`

(required) The details required to move the Exadata infrastructure from one compartment to another.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_JOB_COMPARTMENT Function

Moves a job.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The identifier of the job.

`change_job_compartment_details`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the job to.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MANAGED_DATABASE_GROUP_COMPARTMENT Function

Moves a Managed Database Group to a different compartment. The destination compartment must not have a Managed Database Group with the same name.

Syntax
```

```

Parameters

Parameter Description

`managed_database_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`change_managed_database_group_compartment_details`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the Managed Database Group to.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PLAN_RETENTION Function

Changes the retention period of unused plans. The period can range between 5 and 523 weeks. The database purges plans that have not been used for longer than the plan retention period.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`change_plan_retention_details`

(required) The details required to change the plan retention period.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SPACE_BUDGET Function

Changes the disk space limit for the SQL Management Base. The allowable range for this limit is between 1% and 50%.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`change_space_budget_details`

(required) The details required to change the disk space limit for the SQL Management Base.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SQL_PLAN_BASELINES_ATTRIBUTES Function

Changes one or more attributes of a single plan or all plans associated with a SQL statement.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`change_sql_plan_baselines_attributes_details`

(required) The details required to change SQL plan baseline attributes.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHECK_EXTERNAL_DB_SYSTEM_CONNECTOR_CONNECTION_STATUS Function

Checks the status of the external DB system component connection specified in this connector. This operation will refresh the connectionStatus and timeConnectionStatusLastUpdated fields.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### CHECK_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function

Checks the status of the Exadata storage server connection specified by exadataStorageConnectorId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connector to the Exadata storage server.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### CONFIGURE_AUTOMATIC_CAPTURE_FILTERS Function

Configures automatic capture filters to capture only those statements that match the filter criteria.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`configure_automatic_capture_filters_details`

(required) The details required to configure automatic capture filters.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONFIGURE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function

Configures the Automatic SPM Evolve Advisor task `SYS_AUTO_SPM_EVOLVE_TASK` by specifying task parameters. As the task is owned by `SYS`, only `SYS` can set task parameters.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`configure_automatic_spm_evolve_advisor_task_details`

(required) The configuration details of the Automatic SPM Evolve Advisor task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DB_MANAGEMENT_PRIVATE_ENDPOINT Function

Creates a new Database Management private endpoint.

Syntax
```

```

Parameters

Parameter Description

`create_db_management_private_endpoint_details`

(required) Details used to create a new Database Management private endpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_DB_SYSTEM Function

Creates an external DB system and its related resources.

Syntax
```

```

Parameters

Parameter Description

`create_external_db_system_details`

(required) The details required to create an external DB system.

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

### CREATE_EXTERNAL_DB_SYSTEM_CONNECTOR Function

Creates a new external connector.

Syntax
```

```

Parameters

Parameter Description

`create_external_db_system_connector_details`

(required) The details required to create an external connector.

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

### CREATE_EXTERNAL_DB_SYSTEM_DISCOVERY Function

Creates an external DB system discovery resource and initiates the discovery process.

Syntax
```

```

Parameters

Parameter Description

`create_external_db_system_discovery_details`

(required) The details required to create an external DB system discovery.

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

### CREATE_EXTERNAL_EXADATA_INFRASTRUCTURE Function

Creates an OCI resource for the Exadata infrastructure and enables the Monitoring service for the Exadata infrastructure. The following resource/subresources are created: Infrastructure Storage server connectors Storage servers Storage grids

Syntax
```

```

Parameters

Parameter Description

`create_external_exadata_infrastructure_details`

(required) The details required to create the managed Exadata infrastructure resources.

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

### CREATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function

Creates the Exadata storage server connector after validating the connection information.

Syntax
```

```

Parameters

Parameter Description

`create_external_exadata_storage_connector_details`

(required) The details required to add connections to the Exadata storage servers.

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

### CREATE_JOB Function

Creates a job to be executed on a Managed Database or Managed Database Group. Only one of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as input in CreateJobDetails resource in request body.

Syntax
```

```

Parameters

Parameter Description

`create_job_details`

(required) The details required to create a job.

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

### CREATE_MANAGED_DATABASE_GROUP Function

Creates a Managed Database Group. The group does not contain any Managed Databases when it is created, and they must be added later.

Syntax
```

```

Parameters

Parameter Description

`create_managed_database_group_details`

(required) The details required to create a Managed Database Group.

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

### CREATE_TABLESPACE Function

Creates a tablespace within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`create_tablespace_details`

(required) The details required to create a tablespace.

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

### DELETE_DB_MANAGEMENT_PRIVATE_ENDPOINT Function

Deletes a specific Database Management private endpoint.

Syntax
```

```

Parameters

Parameter Description

`db_management_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_DB_SYSTEM Function

Deletes the external DB system specified by `externalDbSystemId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_DB_SYSTEM_CONNECTOR Function

Deletes the external connector specified by `externalDbSystemConnectorId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_DB_SYSTEM_DISCOVERY Function

Deletes the external DB system discovery resource specified by `externalDbSystemDiscoveryId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_discovery_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system discovery.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_EXADATA_INFRASTRUCTURE Function

Deletes the Exadata infrastructure specified by externalExadataInfrastructureId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function

Deletes the Exadata storage server connector specified by exadataStorageConnectorId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connector to the Exadata storage server.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JOB Function

Deletes the job specified by jobId.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The identifier of the job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGED_DATABASE_GROUP Function

Deletes the Managed Database Group specified by managedDatabaseGroupId. If the group contains Managed Databases, then it cannot be deleted.

Syntax
```

```

Parameters

Parameter Description

`managed_database_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PREFERRED_CREDENTIAL Function

Deletes the preferred credential based on the credentialName.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`l_credential_name`

(required) The name of the preferred credential.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE Function

Disables automatic initial plan capture.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`disable_automatic_initial_plan_capture_details`

(required) The details required to disable automatic initial plan capture.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function

Disables the Automatic SPM Evolve Advisor task. One client controls both Automatic SQL Tuning Advisor and Automatic SPM Evolve Advisor. Thus, the same task enables or disables both.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`disable_automatic_spm_evolve_advisor_task_details`

(required) The details required to disable Automatic SPM Evolve Advisor task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT Function

Disables Database Management service for all the components of the specified external DB system (except databases).

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_DB_SYSTEM_STACK_MONITORING Function

Disables Stack Monitoring for all the components of the specified external DB system (except databases).

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_EXADATA_INFRASTRUCTURE_MANAGEMENT Function

Disables Database Management for the Exadata infrastructure specified by externalExadataInfrastructureId. It covers the following components: - Exadata infrastructure - Exadata storage grid - Exadata storage server Note that Database Management will not be disabled for the DB systems within the Exadata infrastructure and should be disabled explicitly, if required.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function

Disables the high-frequency Automatic SPM Evolve Advisor task. It is available only on Oracle Exadata Database Machine, Oracle Database Exadata Cloud Service (ExaCS) and Oracle Database Exadata Cloud@Customer (ExaCC).

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`disable_high_frequency_automatic_spm_evolve_advisor_task_details`

(required) The details required to disable high frequency Automatic SPM Evolve Advisor task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_SQL_PLAN_BASELINES_USAGE Function

Disables the use of SQL plan baselines stored in SQL Management Base. When disabled, the optimizer does not use any SQL plan baselines.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`disable_sql_plan_baselines_usage_details`

(required) The details required to disable SQL plan baseline usage.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISCOVER_EXTERNAL_EXADATA_INFRASTRUCTURE Function

Completes the Exadata system prechecking on the following: - Verifies if the DB systems are valid RAC DB systems or return 400 status code with NON_RAC_DATABASE_SYSTEM error code. - Verifies if the ASM connector defined for each DB system or return 400 status code with CONNECTOR_NOT_DEFINED error code. - Verifies if the agents associated with ASM are valid and could be used for the Exadata storage servers or return 400 status code with INVALID_AGENT error code. - Verifies if it is an Exadata system or return 400 status code with INVALID_EXADATA_SYSTEM error code. Starts the discovery process for the Exadata system infrastructure. The following resources/components are discovered - Exadata storage servers from each DB systems - Exadata storage grid for all Exadata storage servers - Exadata infrastructure The same API covers both new discovery and rediscovery cases. For the new discovery case, new managed resources/sub-resources are created or the existing ones are overridden. For rediscovery case, the existing managed resources/sub-resources are checked to find out which ones should be added or which ones should be removed based on the unique key defined for each resource/sub-resource.

Syntax
```

```

Parameters

Parameter Description

`discover_external_exadata_infrastructure_details`

(required) The details required to discover and monitor the Exadata infrastructure.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DROP_SQL_PLAN_BASELINES Function

Drops a single plan or all plans associated with a SQL statement.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`drop_sql_plan_baselines_details`

(required) The details required to drop SQL plan baselines.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DROP_TABLESPACE Function

Drops the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`tablespace_name`

(required) The name of the tablespace.

`drop_tablespace_details`

(required) The details required to drop a tablespace.

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

### ENABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE Function

Enables automatic initial plan capture. When enabled, the database checks whether executed SQL statements are eligible for automatic capture. It creates initial plan baselines for eligible statements. By default, the database creates a SQL plan baseline for every eligible repeatable statement, including all recursive SQL and monitoring SQL. Thus, automatic capture may result in the creation of an extremely large number of plan baselines. To limit the statements that are eligible for plan baselines, configure filters.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`enable_automatic_initial_plan_capture_details`

(required) The details required to enable automatic initial plan capture.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function

Enables the Automatic SPM Evolve Advisor task. By default, the automatic task `SYS_AUTO_SPM_EVOLVE_TASK` runs every day in the scheduled maintenance window. The SPM Evolve Advisor performs the following tasks: - Checks AWR for top SQL - Looks for alternative plans in all available sources - Adds unaccepted plans to the plan history - Tests the execution of as many plans as possible during the maintenance window - Adds the alternative plan to the baseline if it performs better than the current plan One client controls both Automatic SQL Tuning Advisor and Automatic SPM Evolve Advisor. Thus, the same task enables or disables both.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`enable_automatic_spm_evolve_advisor_task_details`

(required) The details required to enable Automatic SPM Evolve Advisor task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT Function

Enables Database Management service for all the components of the specified external DB system (except databases).

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`enable_external_db_system_database_management_details`

(required) The details required to enable Database Management for an external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_DB_SYSTEM_STACK_MONITORING Function

Enables Stack Monitoring for all the components of the specified external DB system (except databases).

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`enable_external_db_system_stack_monitoring_details`

(required) The details required to enable Stack Monitoring for an external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_EXADATA_INFRASTRUCTURE_MANAGEMENT Function

Enables Database Management for the Exadata infrastructure specified by externalExadataInfrastructureId. It covers the following components: - Exadata infrastructure - Exadata storage grid - Exadata storage server

Syntax
```

```

Parameters

Parameter Description

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`enable_external_exadata_infrastructure_management_details`

(required) The details required to enable management for the Exadata infrastructure.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function

Enables the high-frequency Automatic SPM Evolve Advisor task. The high-frequency task runs every hour and runs for no longer than 30 minutes. These settings are not configurable. The high-frequency task complements the standard Automatic SPM Evolve Advisor task. They are independent and are scheduled through two different frameworks. It is available only on Oracle Exadata Database Machine, Oracle Database Exadata Cloud Service (ExaCS) and Oracle Database Exadata Cloud@Customer (ExaCC).

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`enable_high_frequency_automatic_spm_evolve_advisor_task_details`

(required) The details required to enable high frequency Automatic SPM Evolve Advisor task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_SQL_PLAN_BASELINES_USAGE Function

Enables the use of SQL plan baselines stored in SQL Management Base. When enabled, the optimizer uses SQL plan baselines to select plans to avoid potential performance regressions.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`enable_sql_plan_baselines_usage_details`

(required) The details required to enable SQL plan baseline usage.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_AWR_SNAPSHOT Function

Creates an AWR snapshot for the target database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_DB_REPORT Function

Gets the AWR report for the specific database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`inst_nums`

(optional) The optional multiple value query parameter to filter the database instance numbers.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`report_type`

(optional) The query parameter to filter the AWR report types.

Allowed values are: 'AWR', 'ASH'

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`report_format`

(optional) The format of the AWR report.

Allowed values are: 'HTML', 'TEXT'

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

### GET_AWR_DB_SQL_REPORT Function

Gets the SQL health check report for one SQL of the specific database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`sql_id`

(required) The parameter to filter SQL by ID. Note that the SQL ID is generated internally by Oracle for each SQL statement and can be retrieved from AWR Report API (/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbReport) or Performance Hub API (/internal/managedDatabases/{managedDatabaseId}/actions/retrievePerformanceData)

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`report_format`

(optional) The format of the AWR report.

Allowed values are: 'HTML', 'TEXT'

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

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

### GET_CLUSTER_CACHE_METRIC Function

Gets the metrics related to cluster cache for the Oracle Real Application Clusters (Oracle RAC) database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`start_time`

(required) The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_FLEET_HEALTH_METRICS Function

Gets the health metrics for a fleet of databases in a compartment or in a Managed Database Group. Either the CompartmentId or the ManagedDatabaseGroupId query parameters must be provided to retrieve the health metrics.

Syntax
```

```

Parameters

Parameter Description

`compare_baseline_time`

(required) The baseline time for metrics comparison.

`compare_target_time`

(required) The target time for metrics comparison.

`opc_request_id`

(optional) The client request ID for tracing.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`compare_type`

(optional) The time window used for metrics comparison.

Allowed values are: 'HOUR', 'DAY', 'WEEK'

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`filter_by_database_type`

(optional) The filter used to filter the databases in the fleet by a specific Oracle Database type.

`filter_by_database_sub_type`

(optional) The filter used to filter the databases in the fleet by a specific Oracle Database subtype.

`filter_by_database_deployment_type`

(optional) The filter used to filter the databases in the fleet by a specific Oracle Database deployment type.

`filter_by_database_version`

(optional) The filter used to filter the databases in the fleet by a specific Oracle Database version.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_HOME_METRICS Function

Gets a summary of the activity and resource usage metrics like DB Time, CPU, User I/O, Wait, Storage, and Memory for a Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`start_time`

(required) The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_MANAGEMENT_PRIVATE_ENDPOINT Function

Gets the details of a specific Database Management private endpoint.

Syntax
```

```

Parameters

Parameter Description

`db_management_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_ASM Function

Gets the details for the external ASM specified by `externalAsmId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_ASM_CONFIGURATION Function

Gets configuration details including disk groups for the external ASM specified by `externalAsmId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_ASM_INSTANCE Function

Gets the details for the external ASM instance specified by `externalAsmInstanceId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM instance.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_CLUSTER Function

Gets the details for the external cluster specified by `externalClusterId`.

Syntax
```

```

Parameters

Parameter Description

`external_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_CLUSTER_INSTANCE Function

Gets the details for the external cluster instance specified by `externalClusterInstanceId`.

Syntax
```

```

Parameters

Parameter Description

`external_cluster_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster instance.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_DB_HOME Function

Gets the details for the external DB home specified by `externalDbHomeId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_home_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database home.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_DB_NODE Function

Gets the details for the external DB node specified by `externalDbNodeId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_node_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database node.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_DB_SYSTEM Function

Gets the details for the external DB system specified by `externalDbSystemId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_DB_SYSTEM_CONNECTOR Function

Gets the details for the external connector specified by `externalDbSystemConnectorId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_DB_SYSTEM_DISCOVERY Function

Gets the details for the external DB system discovery resource specified by `externalDbSystemDiscoveryId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_discovery_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system discovery.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_EXADATA_INFRASTRUCTURE Function

Gets the details for the Exadata infrastructure specified by externalExadataInfrastructureId. It includes the DB systems and storage grid within the Exadata infrastructure.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function

Gets the details for the Exadata storage server connector specified by exadataStorageConnectorId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connector to the Exadata storage server.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_EXADATA_STORAGE_GRID Function

Gets the details for the Exadata storage server grid specified by exadataStorageGridId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_grid_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage grid.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_EXADATA_STORAGE_SERVER Function

Gets the summary for the Exadata storage server specified by exadataStorageServerId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_LISTENER Function

Gets the details for the external listener specified by `externalListenerId`.

Syntax
```

```

Parameters

Parameter Description

`external_listener_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IORM_PLAN Function

Get the IORM plan from the specific Exadata storage server.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB Function

Gets the details for the job specified by jobId.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The identifier of the job.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_EXECUTION Function

Gets the details for the job execution specified by jobExecutionId.

Syntax
```

```

Parameters

Parameter Description

`job_execution_id`

(required) The identifier of the job execution.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JOB_RUN Function

Gets the details for the job run specified by jobRunId.

Syntax
```

```

Parameters

Parameter Description

`job_run_id`

(required) The identifier of the job run.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGED_DATABASE Function

Gets the details for the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGED_DATABASE_GROUP Function

Gets the details for the Managed Database Group specified by managedDatabaseGroupId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPEN_ALERT_HISTORY Function

Gets the open alerts from the specified Exadata storage server.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION Function

Gets a comprehensive report of the Optimizer Statistics Advisor execution, which includes details of the Managed Database, findings, recommendations, rationale, and examples.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`execution_name`

(required) The name of the Optimizer Statistics Advisor execution.

`task_name`

(required) The name of the optimizer statistics collection execution task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SCRIPT Function

Gets the Oracle system-generated script for the specified Optimizer Statistics Advisor execution.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`execution_name`

(required) The name of the Optimizer Statistics Advisor execution.

`task_name`

(required) The name of the optimizer statistics collection execution task.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPTIMIZER_STATISTICS_COLLECTION_OPERATION Function

Gets a detailed report of the Optimizer Statistics Collection operation for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`optimizer_statistics_collection_operation_id`

(required) The ID of the Optimizer Statistics Collection operation.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PDB_METRICS Function

Gets a summary of the resource usage metrics such as CPU, User I/O, and Storage for each PDB within a specific CDB. If comparmentId is specified, then the metrics for each PDB (within the CDB) in the specified compartment are retrieved. If compartmentId is not specified, then the metrics for all the PDBs within the CDB are retrieved.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`start_time`

(required) The start time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the health metrics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`compare_type`

(optional) The time window used for metrics comparison.

Allowed values are: 'HOUR', 'DAY', 'WEEK'

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PREFERRED_CREDENTIAL Function

Gets the preferred credential details for a Managed Database based on credentialName.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`l_credential_name`

(required) The name of the preferred credential.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SQL_PLAN_BASELINE Function

Gets the SQL plan baseline details for the specified planName.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`plan_name`

(required) The plan name of the SQL plan baseline.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SQL_PLAN_BASELINE_CONFIGURATION Function

Gets the configuration details of SQL plan baselines for the specified Managed Database. The details include the settings for the capture and use of SQL plan baselines, SPM Evolve Advisor task, and SQL Management Base.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TABLESPACE Function

Gets the details of the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`tablespace_name`

(required) The name of the tablespace.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TOP_SQL_CPU_ACTIVITY Function

Gets the SQL IDs with the top CPU activity from the Exadata storage server.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata storage server.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER Function

Gets the details of the user specified by managedDatabaseId and userName.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given Work Request ID

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPLEMENT_OPTIMIZER_STATISTICS_ADVISOR_RECOMMENDATIONS Function

Asynchronously implements the findings and recommendations of the Optimizer Statistics Advisor execution.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`execution_name`

(required) The name of the Optimizer Statistics Advisor execution.

`implement_optimizer_statistics_advisor_recommendations_details`

(required) The Optimizer Statistics Advisor recommendations implementation request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ASM_PROPERTIES Function

Gets the list of ASM properties for the specified managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### LIST_ASSOCIATED_DATABASES Function

Gets the list of databases using a specific Database Management private endpoint.

Syntax
```

```

Parameters

Parameter Description

`db_management_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The option to sort databases using a specific Database Management private endpoint.

Allowed values are: 'timeRegistered'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_DB_SNAPSHOTS Function

Lists AWR snapshots for the specified database in the AWR.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the AWR snapshot summary data.

Allowed values are: 'TIME_BEGIN', 'SNAPSHOT_ID'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### LIST_AWR_DBS Function

Gets the list of databases and their snapshot summary details available in the AWR of the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(optional) The optional single value query parameter to filter the entity name.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the AWR summary data.

Allowed values are: 'END_INTERVAL_TIME', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### LIST_CONSUMER_GROUP_PRIVILEGES Function

Gets the list of consumer group privileges granted to a specific user.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CURSOR_CACHE_STATEMENTS Function

Lists the SQL statements from shared SQL area, also called the cursor cache.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`sql_text`

(optional) A filter to return all the SQL plan baselines that match the SQL text. By default, the search is case insensitive. To run an exact or case-sensitive search, double-quote the search string. You may also use the '%' symbol as a wildcard.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the SQL statement summary data.

Allowed values are: 'sqlId', 'schema'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_ACCESS_CONTAINERS Function

Gets the list of containers for a specific user. This is only applicable if ALL_CONTAINERS !='Y'.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_PARAMETERS Function

Gets the list of database parameters for the specified Managed Database. The parameters are listed in alphabetical order, along with their current values.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`source`

(optional) The source used to list database parameters. `CURRENT` is used to get the database parameters that are currently in effect for the database instance. `SPFILE` is used to list parameters from the server parameter file. Default is `CURRENT`.

Allowed values are: 'CURRENT', 'SPFILE'

`name`

(optional) A filter to return all parameters that have the text given in their names.

`is_allowed_values_included`

(optional) When true, results include a list of valid values for parameters (if applicable).

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `NAME` is ascending and it is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_MANAGEMENT_PRIVATE_ENDPOINTS Function

Gets a list of Database Management private endpoints.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(optional) A filter to return only resources that match the entire name.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`is_cluster`

(optional) The option to filter Database Management private endpoints that can used for Oracle Databases in a cluster. This should be used along with the vcnId query parameter.

`lifecycle_state`

(optional) The lifecycle state of a resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_ASM_DISK_GROUPS Function

Lists ASM disk groups for the external ASM specified by `externalAsmId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `NAME` is ascending and it is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_ASM_INSTANCES Function

Lists the ASM instances in the specified external ASM.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_asm_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_ASM_USERS Function

Lists ASM users for the external ASM specified by `externalAsmId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `NAME` is ascending and it is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_ASMS Function

Lists the ASMs in the specified external DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_CLUSTER_INSTANCES Function

Lists the cluster instances in the specified external cluster.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_CLUSTERS Function

Lists the clusters in the specified external DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DATABASES Function

Lists the external databases in the specified compartment or in the specified DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DB_HOMES Function

Lists the DB homes in the specified external DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DB_NODES Function

Lists the external DB nodes in the specified external DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DB_SYSTEM_CONNECTORS Function

Lists the external connectors in the specified external DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DB_SYSTEM_DISCOVERIES Function

Lists the external DB system discovery resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DB_SYSTEMS Function

Lists the external DB systems in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_EXADATA_INFRASTRUCTURES Function

Lists the Exadata infrastructure resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) The optional single value query filter parameter on the entity display name.

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

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_EXADATA_STORAGE_CONNECTORS Function

Lists the Exadata storage server connectors for the specified Exadata infrastructure.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`display_name`

(optional) The optional single value query filter parameter on the entity display name.

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

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_EXADATA_STORAGE_SERVERS Function

Lists the Exadata storage servers for the specified Exadata infrastructure.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`display_name`

(optional) The optional single value query filter parameter on the entity display name.

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

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_LISTENER_SERVICES Function

Lists the database services registered with the specified external listener for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`external_listener_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `NAME` is ascending and it is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_LISTENERS Function

Lists the listeners in the specified external DB system.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`external_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`display_name`

(optional) A filter to only return the resources that match the entire display name.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending. The `DISPLAYNAME` sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_EXECUTIONS Function

Gets the job execution for a specific ID or the list of job executions for a job, job run, Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, jobId, jobRunId, managedDatabaseId or managedDatabaseGroupId should be provided. If none of these parameters is provided, all the job executions in the compartment are listed. Job executions can also be filtered based on the name and status parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) The identifier of the resource.

`job_id`

(optional) The identifier of the job.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`status`

(optional) The status of the job execution.

`name`

(optional) A filter to return only resources that match the entire name.

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

`job_run_id`

(optional) The identifier of the job run.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JOB_RUNS Function

Gets the job run for a specific ID or the list of job runs for a job, Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId, or managedDatabaseGroupId should be provided. If none of these parameters is provided, all the job runs in the compartment are listed. Job runs can also be filtered based on name and runStatus parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) The identifier of the resource.

`job_id`

(optional) The identifier of the job.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`run_status`

(optional) The status of the job run.

`name`

(optional) A filter to return only resources that match the entire name.

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

### LIST_JOBS Function

Gets the job for a specific ID or the list of jobs for a Managed Database or Managed Database Group in a specific compartment. Only one of the parameters, ID, managedDatabaseId or managedDatabaseGroupId, should be provided. If none of these parameters is provided, all the jobs in the compartment are listed. Jobs can also be filtered based on the name and lifecycleState parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) The identifier of the resource.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(optional) A filter to return only resources that match the entire name.

`lifecycle_state`

(optional) The lifecycle state of the job.

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

### LIST_MANAGED_DATABASE_GROUPS Function

Gets the Managed Database Group for a specific ID or the list of Managed Database Groups in a specific compartment. Managed Database Groups can also be filtered based on the name parameter. Only one of the parameters, ID or name should be provided. If none of these parameters is provided, all the Managed Database Groups in the compartment are listed.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) The identifier of the resource.

`name`

(optional) A filter to return only resources that match the entire name.

`lifecycle_state`

(optional) The lifecycle state of a resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

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

### LIST_MANAGED_DATABASES Function

Gets the Managed Database for a specific ID or the list of Managed Databases in a specific compartment. Managed Databases can be filtered based on the name parameter. Only one of the parameters, ID or name should be provided. If neither of these parameters is provided, all the Managed Databases in the compartment are listed. Managed Databases can also be filtered based on the deployment type and management option. If the deployment type is not specified or if it is `ONPREMISE`, then the management option is not considered and Managed Databases with `ADVANCED` management option are listed.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) The identifier of the resource.

`name`

(optional) A filter to return only resources that match the entire name.

`management_option`

(optional) A filter to return Managed Databases with the specified management option.

Allowed values are: 'BASIC', 'ADVANCED'

`deployment_type`

(optional) A filter to return Managed Databases of the specified deployment type.

Allowed values are: 'ONPREMISE', 'BM', 'VM', 'EXADATA', 'EXADATA_CC', 'AUTONOMOUS'

`external_exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

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

### LIST_OBJECT_PRIVILEGES Function

Gets the list of object privileges granted to a specific user.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPTIMIZER_STATISTICS_ADVISOR_EXECUTIONS Function

Lists the details of the Optimizer Statistics Advisor task executions, such as their duration, and the number of findings, if any. Optionally, you can specify a date-time range (of seven days) to obtain the list of executions that fall within the specified time range. If the date-time range is not specified, then the executions in the last seven days are listed.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`start_time_greater_than_or_equal_to`

(optional) The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time_less_than_or_equal_to`

(optional) The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATIONS Function

Gets a list of the optimizer statistics collection operations per hour, grouped by task or object status for the specified Managed Database. You must specify a value for GroupByQueryParam to determine whether the data should be grouped by task status or task object status. Optionally, you can specify a date-time range (of seven days) to obtain collection aggregations within the specified time range. If the date-time range is not specified, then the operations in the last seven days are listed. You can further filter the results by providing the optional type of TaskTypeQueryParam. If the task type not provided, then both Auto and Manual tasks are considered for aggregation.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`group_type`

(required) The optimizer statistics tasks grouped by type.

Allowed values are: 'TASK_STATUS', 'TASK_OBJECTS_STATUS'

`start_time_greater_than_or_equal_to`

(optional) The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time_less_than_or_equal_to`

(optional) The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`task_type`

(optional) The filter types of the optimizer statistics tasks.

Allowed values are: 'ALL', 'MANUAL', 'AUTO'

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPTIMIZER_STATISTICS_COLLECTION_OPERATIONS Function

Lists the Optimizer Statistics Collection (Auto and Manual) task operation summary for the specified Managed Database. The summary includes the details of each operation and the number of tasks grouped by status: Completed, In Progress, Failed, and so on. Optionally, you can specify a date-time range (of seven days) to obtain the list of operations that fall within the specified time range. If the date-time range is not specified, then the operations in the last seven days are listed. This API also enables the pagination of results and the opc-next-page response header indicates whether there is a next page. If you use the same header value in a consecutive request, the next page records are returned. To obtain the required results, you can apply the different types of filters supported by this API.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`start_time_greater_than_or_equal_to`

(optional) The start time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time_less_than_or_equal_to`

(optional) The end time of the time range to retrieve the optimizer statistics of a Managed Database in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`task_type`

(optional) The filter types of the optimizer statistics tasks.

Allowed values are: 'ALL', 'MANUAL', 'AUTO'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`filter_by`

(optional) The parameter used to filter the optimizer statistics operations. Any property of the OptimizerStatisticsCollectionOperationSummary can be used to define the filter condition. The allowed conditional operators are AND or OR, and the allowed binary operators are are &gt;, &lt; and =. Any other operator is regarded invalid. Example: jobName=&lt;replace with job name&gt; AND status=&lt;replace with status&gt;

`sort_by`

(optional) Sorts the list of optimizer statistics operations based on a specific attribute.

Allowed values are: 'START_TIME', 'END_TIME', 'STATUS'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PREFERRED_CREDENTIALS Function

Gets the list of preferred credentials for a given Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROXIED_FOR_USERS Function

Gets the list of users on whose behalf the current user acts as proxy.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROXY_USERS Function

Gets the list of proxy users for the current user.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROLES Function

Gets the list of roles granted to a specific user.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_PLAN_BASELINE_JOBS Function

Lists the database jobs used for loading SQL plan baselines in the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(optional) A filter to return the SQL plan baseline jobs that match the name.

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

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_PLAN_BASELINES Function

Lists the SQL plan baselines for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`plan_name`

(optional) A filter to return only SQL plan baselines that match the plan name.

`sql_handle`

(optional) A filter to return all the SQL plan baselines for the specified SQL handle.

`sql_text`

(optional) A filter to return all the SQL plan baselines that match the SQL text. By default, the search is case insensitive. To run an exact or case-sensitive search, double-quote the search string. You may also use the '%' symbol as a wildcard.

`is_enabled`

(optional) A filter to return only SQL plan baselines that are either enabled or not enabled. By default, all SQL plan baselines are returned.

`is_accepted`

(optional) A filter to return only SQL plan baselines that are either accepted or not accepted. By default, all SQL plan baselines are returned.

`is_reproduced`

(optional) A filter to return only SQL plan baselines that were either reproduced or not reproduced by the optimizer. By default, all SQL plan baselines are returned.

`is_fixed`

(optional) A filter to return only SQL plan baselines that are either fixed or not fixed. By default, all SQL plan baselines are returned.

`is_adaptive`

(optional) A filter to return only SQL plan baselines that are either adaptive or not adaptive. By default, all SQL plan baselines are returned.

`origin`

(optional) A filter to return all the SQL plan baselines that match the origin.

Allowed values are: 'ADDM_SQLTUNE', 'AUTO_CAPTURE', 'AUTO_SQLTUNE', 'EVOLVE_AUTO_INDEX_LOAD', 'EVOLVE_CREATE_FROM_ADAPTIVE', 'EVOLVE_LOAD_FROM_STS', 'EVOLVE_LOAD_FROM_AWR', 'EVOLVE_LOAD_FROM_CURSOR_CACHE', 'MANUAL_LOAD', 'MANUAL_LOAD_FROM_AWR', 'MANUAL_LOAD_FROM_CURSOR_CACHE', 'MANUAL_LOAD_FROM_STS', 'MANUAL_SQLTUNE', 'STORED_OUTLINE', 'UNKNOWN'

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the SQL plan baseline summary data.

Allowed values are: 'timeCreated', 'timeLastModified'

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

### LIST_SYSTEM_PRIVILEGES Function

Gets the list of system privileges granted to a specific user.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`user_name`

(required) The name of the user whose details are to be viewed.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TABLE_STATISTICS Function

Lists the database table statistics grouped by different statuses such as Not Stale Stats, Stale Stats, and No Stats. This also includes the percentage of each status.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TABLESPACES Function

Gets the list of tablespaces for the specified managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### LIST_USERS Function

Gets the list of users for the specified managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`opc_request_id`

(optional) The client request ID for tracing.

`name`

(optional) A filter to return only resources that match the entire name.

`sort_by`

(optional) The field to sort information by. Only one sortOrder can be used. The default sort order for ‘TIMECREATED’ is descending and the default sort order for ‘NAME’ is ascending. The ‘NAME’ sort order is case-sensitive.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of records returned in the paginated response.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Returns a paginated list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided and the default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a paginated list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided and the default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

The list of work requests in a specific compartment was retrieved successfully.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`work_request_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous work request.

`status`

(optional) A filter that returns the resources whose status matches the given WorkRequestStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided and the default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

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

### LOAD_SQL_PLAN_BASELINES_FROM_AWR Function

Loads plans from Automatic Workload Repository (AWR) snapshots. You must specify the beginning and ending of the snapshot range. Optionally, you can apply a filter to load only plans that meet specified criteria. By default, the optimizer uses the loaded plans the next time that the database executes the SQL statements.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`load_sql_plan_baselines_from_awr_details`

(required) The details required to load plans from Automatic Workload Repository (AWR).

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LOAD_SQL_PLAN_BASELINES_FROM_CURSOR_CACHE Function

Loads plans for statements directly from the shared SQL area, also called the cursor cache. By applying a filter on the module name, the schema, or the SQL ID you identify the SQL statement or set of SQL statements to load.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`load_sql_plan_baselines_from_cursor_cache_details`

(required) The details of SQL statements and plans to be loaded from cursor cache.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_EXTERNAL_DB_SYSTEM_DISCOVERY Function

Patches the external DB system discovery specified by `externalDbSystemDiscoveryId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_discovery_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system discovery.

`patch_external_db_system_discovery_details`

(required) The details required to update an external DB system discovery.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DATA_FILE Function

Removes a data file or temp file from the tablespace.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`tablespace_name`

(required) The name of the tablespace.

`remove_data_file_details`

(required) The details required to remove a data file or temp file from the tablespace.

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

### REMOVE_MANAGED_DATABASE_FROM_MANAGED_DATABASE_GROUP Function

Removes a Managed Database from a Managed Database Group. Any management activities that are currently running on this database will continue to run to completion. However, any activities scheduled to run in the future will not be performed on this database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`remove_managed_database_from_managed_database_group_details`

(required) The Managed Database details required to remove the Managed Database from a Managed Database Group.

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

### RESET_DATABASE_PARAMETERS Function

Resets database parameter values to their default or startup values.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`reset_database_parameters_details`

(required) The details required to reset database parameters.

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

### RESIZE_DATA_FILE Function

Resizes a data file or temp file within the tablespace.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`tablespace_name`

(required) The name of the tablespace.

`resize_data_file_details`

(required) The details required to resize a data file or temp file within the tablespace.

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

### RUN_HISTORIC_ADDM Function

Creates and executes a historic ADDM task using the specified AWR snapshot IDs. If an existing ADDM task uses the provided awr snapshot IDs, the existing task will be returned.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`run_historic_addm_details`

(required) The details of the ADDM task, which include the beginning and ending AWR snapshot IDs.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DB_CPU_USAGES Function

Summarizes the AWR CPU resource limits and metrics for the specified database in AWR.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`session_type`

(optional) The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

Allowed values are: 'FOREGROUND', 'BACKGROUND', 'ALL'

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort the AWR CPU usage summary data.

Allowed values are: 'TIME_SAMPLED', 'AVG_VALUE'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_METRICS Function

Summarizes the metric samples for the specified database in the AWR. The metric samples are summarized based on the Time dimension for each metric.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`name`

(required) The required multiple value query parameter to filter the entity name.

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort the AWR time series summary data.

Allowed values are: 'TIMESTAMP', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_PARAMETER_CHANGES Function

Summarizes the database parameter change history for one database parameter of the specified database in AWR. One change history record contains the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range, then multiple change history records are created for the same parameter. Note that this API only returns information on change history details for one database parameter. To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameters

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`name`

(required) The required single value query parameter to filter the entity name.

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort the AWR database parameter change history data.

Allowed values are: 'IS_CHANGED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_PARAMETERS Function

Summarizes the database parameter history for the specified database in AWR. This includes the list of database parameters, with information on whether the parameter values were modified within the query time range. Note that each database parameter is only listed once. Depending on the optional query parameters, the returned summary gets all the database parameters, which include: - Each parameter whose value was changed during the time range: (valueChanged =\"Y\") - Each parameter whose value was unchanged during the time range: (valueChanged =\"N\") - Each parameter whose value was changed at the system level during the time range: (valueChanged =\"Y\" and valueModified = \"SYSTEM_MOD\") - Each parameter whose value was unchanged during the time range, however, the value is not the default value: (valueChanged =\"N\" and valueDefault = \"FALSE\") Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database parameter value change history for a specific parameter, use the following API endpoint: /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbParameterChanges

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`name`

(optional) The optional multiple value query parameter to filter the entity name.

`name_contains`

(optional) The optional contains query parameter to filter the entity name by any part of the name.

`value_changed`

(optional) The optional query parameter to filter database parameters whose values were changed.

Allowed values are: 'Y', 'N'

`value_default`

(optional) The optional query parameter to filter the database parameters that had the default value in the last snapshot.

Allowed values are: 'TRUE', 'FALSE'

`value_modified`

(optional) The optional query parameter to filter the database parameters that had a modified value in the last snapshot.

Allowed values are: 'MODIFIED', 'SYSTEM_MOD', 'FALSE'

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort the AWR database parameter change history data.

Allowed values are: 'IS_CHANGED', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_SNAPSHOT_RANGES Function

Summarizes the AWR snapshot ranges that contain continuous snapshots, for the specified Managed Database.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(optional) The optional single value query parameter to filter the entity name.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`sort_by`

(optional) The option to sort the AWR summary data.

Allowed values are: 'END_INTERVAL_TIME', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_SYSSTATS Function

Summarizes the AWR SYSSTAT sample data for the specified database in AWR. The statistical data is summarized based on the Time dimension for each statistic.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`name`

(required) The required multiple value query parameter to filter the entity name.

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort the data within a time period.

Allowed values are: 'TIME_BEGIN', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_TOP_WAIT_EVENTS Function

Summarizes the AWR top wait events.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`session_type`

(optional) The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

Allowed values are: 'FOREGROUND', 'BACKGROUND', 'ALL'

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`top_n`

(optional) The optional query parameter to filter the number of top categories to be returned.

`sort_by`

(optional) The option to sort the AWR top event summary data.

Allowed values are: 'WAITS_PERSEC', 'AVG_WAIT_TIME_PERSEC'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_WAIT_EVENT_BUCKETS Function

Summarizes AWR wait event data into value buckets and frequency, for the specified database in the AWR.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`name`

(required) The required single value query parameter to filter the entity name.

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`num_bucket`

(optional) The number of buckets within the histogram.

`min_value`

(optional) The minimum value of the histogram.

`max_value`

(optional) The maximum value of the histogram.

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort distribution data.

Allowed values are: 'CATEGORY', 'PERCENTAGE'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Ascending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_AWR_DB_WAIT_EVENTS Function

Summarizes the AWR wait event sample data for the specified database in the AWR. The event data is summarized based on the Time dimension for each event.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`awr_db_id`

(required) The parameter to filter the database by internal ID. Note that the internal ID of the database can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbs

`inst_num`

(optional) The optional single value query parameter to filter the database instance number.

`begin_sn_id_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_sn_id_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot ID.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp.

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp.

`name`

(optional) The optional multiple value query parameter to filter the entity name.

`session_type`

(optional) The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

Allowed values are: 'FOREGROUND', 'BACKGROUND', 'ALL'

`container_id`

(optional) The optional query parameter to filter the database container by an exact ID value. Note that the database container ID can be retrieved from the following endpoint: /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in large paginated response.

`sort_by`

(optional) The option to sort the data within a time period.

Allowed values are: 'TIME_BEGIN', 'NAME'

`sort_order`

(optional) The option to sort information in ascending (‘ASC’) or descending (‘DESC’) order. Descending order is the default order.

Allowed values are: 'ASC', 'DESC'

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

### SUMMARIZE_EXTERNAL_ASM_METRICS Function

Gets metrics for the external ASM specified by `externalAsmId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`start_time`

(required) The beginning of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`end_time`

(required) The end of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXTERNAL_CLUSTER_METRICS Function

Gets metrics for the external cluster specified by `externalClusterId`.

Syntax
```

```

Parameters

Parameter Description

`external_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster.

`start_time`

(required) The beginning of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`end_time`

(required) The end of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXTERNAL_DB_NODE_METRICS Function

Gets metrics for the external DB node specified by `externalDbNodeId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_node_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database node.

`start_time`

(required) The beginning of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`end_time`

(required) The end of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXTERNAL_DB_SYSTEM_AVAILABILITY_METRICS Function

Gets availability metrics for the components present in the external DB system specified by `externalDbSystemId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`start_time`

(required) The beginning of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`end_time`

(required) The end of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`filter_by_component_types`

(optional) The filter used to retrieve metrics for a specific set of component types by passing the desired component types separated by a comma. Note that, by default, the service returns metrics for all DB system component types.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXTERNAL_LISTENER_METRICS Function

Gets metrics for the external listener specified by `externalListenerId`.

Syntax
```

```

Parameters

Parameter Description

`external_listener_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`start_time`

(required) The beginning of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`end_time`

(required) The end of the time range set to retrieve metric data for the DB system and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of records returned in the paginated response.

`filter_by_metric_names`

(optional) The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the service returns all supported metrics.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_JOB_EXECUTIONS_STATUSES Function

Gets the number of job executions grouped by status for a job, Managed Database, or Database Group in a specific compartment. Only one of the parameters, jobId, managedDatabaseId, or managedDatabaseGroupId should be provided.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`start_time`

(required) The start time of the time range to retrieve the status summary of job executions in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`end_time`

(required) The end time of the time range to retrieve the status summary of job executions in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".

`opc_request_id`

(optional) The client request ID for tracing.

`id`

(optional) The identifier of the resource.

`managed_database_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`managed_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`name`

(optional) A filter to return only resources that match the entire name.

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

### SUMMARIZE_MANAGED_DATABASE_AVAILABILITY_METRICS Function

Gets the availability metrics related to managed database for the Oracle database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

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

### SUMMARIZE_SQL_PLAN_BASELINES Function

Gets the number of SQL plan baselines aggregated by their attributes.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_PLAN_BASELINES_BY_LAST_EXECUTION Function

Gets the number of SQL plan baselines aggregated by the age of their last execution in weeks.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`page`

(optional) The page token representing the page from where the next set of paginated results are retrieved. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TEST_PREFERRED_CREDENTIAL Function

Tests the preferred credential.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`l_credential_name`

(required) The name of the preferred credential.

`opc_request_id`

(optional) The client request ID for tracing.

`test_preferred_credential_details`

(optional) The details required to test preferred credential.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DB_MANAGEMENT_PRIVATE_ENDPOINT Function

Updates one or more attributes of a specific Database Management private endpoint.

Syntax
```

```

Parameters

Parameter Description

`db_management_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Management private endpoint.

`update_db_management_private_endpoint_details`

(required) The details used to update a Database Management private endpoint.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_ASM Function

Updates the external ASM specified by `externalAsmId`.

Syntax
```

```

Parameters

Parameter Description

`external_asm_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external ASM.

`update_external_asm_details`

(required) The details required to update an external ASM.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_CLUSTER Function

Updates the external cluster specified by `externalClusterId`.

Syntax
```

```

Parameters

Parameter Description

`external_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster.

`update_external_cluster_details`

(required) The details required to update an external cluster.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_CLUSTER_INSTANCE Function

Updates the external cluster instance specified by `externalClusterInstanceId`.

Syntax
```

```

Parameters

Parameter Description

`external_cluster_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external cluster instance.

`update_external_cluster_instance_details`

(required) The details required to update an external cluster instance.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_DB_NODE Function

Updates the external DB node specified by `externalDbNodeId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_node_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database node.

`update_external_db_node_details`

(required) The details required to update an external DB node.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_DB_SYSTEM Function

Updates the external DB system specified by `externalDbSystemId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system.

`update_external_db_system_details`

(required) The details required to update an external DB system.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_DB_SYSTEM_CONNECTOR Function

Updates the external connector specified by `externalDbSystemConnectorId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external connector.

`update_external_db_system_connector_details`

(required) The details required to update an external connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_DB_SYSTEM_DISCOVERY Function

Updates the external DB system discovery specified by `externalDbSystemDiscoveryId`.

Syntax
```

```

Parameters

Parameter Description

`external_db_system_discovery_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external DB system discovery.

`update_external_db_system_discovery_details`

(required) The details required to update an external DB system discovery.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_EXADATA_INFRASTRUCTURE Function

Updates the details for the Exadata infrastructure specified by externalExadataInfrastructureId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`update_external_exadata_infrastructure_details`

(required) The details required to update the managed Exadata infrastructure resources.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function

Updates the Exadata storage server connector specified by exadataStorageConnectorId.

Syntax
```

```

Parameters

Parameter Description

`external_exadata_storage_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connector to the Exadata storage server.

`update_external_exadata_storage_connector_details`

(required) The details required to update connections to the Exadata storage servers.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_LISTENER Function

Updates the external listener specified by `externalListenerId`.

Syntax
```

```

Parameters

Parameter Description

`external_listener_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external listener.

`update_external_listener_details`

(required) The details required to update an external listener.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_JOB Function

Updates the details for the recurring scheduled job specified by jobId. Note that non-recurring (one time) jobs cannot be updated.

Syntax
```

```

Parameters

Parameter Description

`job_id`

(required) The identifier of the job.

`update_job_details`

(required) The details required to update a job.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGED_DATABASE_GROUP Function

Updates the Managed Database Group specified by managedDatabaseGroupId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database Group.

`update_managed_database_group_details`

(required) The details required to update a Managed Database Group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PREFERRED_CREDENTIAL Function

Updates the preferred credential based on the credentialName.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`l_credential_name`

(required) The name of the preferred credential.

`update_preferred_credential_details`

(required) The details required to update preferred credential.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TABLESPACE Function

Updates the attributes of the tablespace specified by tablespaceName within the Managed Database specified by managedDatabaseId.

Syntax
```

```

Parameters

Parameter Description

`managed_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Managed Database.

`tablespace_name`

(required) The name of the tablespace.

`update_tablespace_details`

(required) The details required to update a tablespace.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://dbmgmt.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Database Management Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-AFF16810-7194-4913-B762-9E16CCA2D8F8)
- [ADD_DATA_FILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-90F82191-1A66-4784-A7C7-024455E708E6)
- [ADD_MANAGED_DATABASE_TO_MANAGED_DATABASE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-9CB38FD8-44DE-44DE-ACFB-0DB001524BA7)
- [ADDM_TASKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-7D2A4EFD-9CAC-4E4E-B8C8-F1879D6A965B)
- [CHANGE_DATABASE_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F95F4F26-320A-4AC9-88D9-125FFC8DDE86)
- [CHANGE_DB_MANAGEMENT_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-2ACC0B8B-F277-4F14-98FA-967EEAD4661E)
- [CHANGE_EXTERNAL_DB_SYSTEM_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D57AB512-B5F1-4C5F-894F-2D8C54C34527)
- [CHANGE_EXTERNAL_EXADATA_INFRASTRUCTURE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-38CEE5CA-3203-44EF-8CD1-25585E6631B6)
- [CHANGE_JOB_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-8D72CBE0-5B6F-4CA8-96F9-6BB67D7948A7)
- [CHANGE_MANAGED_DATABASE_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-277A16CA-E5BA-4A74-A954-425F8120EFE9)
- [CHANGE_PLAN_RETENTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-66BA5365-B890-472C-B756-3D22957BDE4B)
- [CHANGE_SPACE_BUDGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5C8C655A-D4FC-41AC-B685-F4314FFB723B)
- [CHANGE_SQL_PLAN_BASELINES_ATTRIBUTES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-69331084-B1A8-40B0-A32A-D7BE108977F3)
- [CHECK_EXTERNAL_DB_SYSTEM_CONNECTOR_CONNECTION_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D5104F42-516C-456F-AD81-5CECF0B6C4EA)
- [CHECK_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-828D3A8B-0D96-430E-A8EE-73FF70D4F0CB)
- [CONFIGURE_AUTOMATIC_CAPTURE_FILTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-BF5ADF14-83A0-40B6-86D2-56E09D7964C7)
- [CONFIGURE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-BE4107FE-3D65-4296-8F9E-832737F2538C)
- [CREATE_DB_MANAGEMENT_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-7F906E00-8AFA-4A41-B238-0D14FBD02633)
- [CREATE_EXTERNAL_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-33B9A1B9-9510-4F08-A987-29365438EE91)
- [CREATE_EXTERNAL_DB_SYSTEM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F957367E-7528-48E7-B432-3A5D71B16840)
- [CREATE_EXTERNAL_DB_SYSTEM_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-33F6B1A4-28C7-4AF3-93CD-09BA17C0D431)
- [CREATE_EXTERNAL_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-4E7BB9B6-EACB-4F9E-A1D1-6B41E317C050)
- [CREATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F3CEAA27-3879-43B9-AB9E-3505864885F8)
- [CREATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3645F989-47F7-47BC-81E4-19E66E1F49E6)
- [CREATE_MANAGED_DATABASE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-A5413B19-16A0-479F-A547-B3E31857608C)
- [CREATE_TABLESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0E952452-720B-4C64-BC7A-11F44A184C7E)
- [DELETE_DB_MANAGEMENT_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-9AA932B0-C349-40AC-AFE9-363D2F9C91CD)
- [DELETE_EXTERNAL_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-9C43F479-0CD8-442C-BA7F-05C802BB9C2A)
- [DELETE_EXTERNAL_DB_SYSTEM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-4F708279-3674-415E-A27F-357B14FDD589)
- [DELETE_EXTERNAL_DB_SYSTEM_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5782DFA7-35AC-4417-A1E5-FD3FFC7E66EB)
- [DELETE_EXTERNAL_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-1FBA20AE-9813-4590-84C6-5A473AE45351)
- [DELETE_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5E62C164-C783-4789-BF82-E83BFEFC0557)
- [DELETE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-98B91069-D866-4550-8887-ACAAE904B065)
- [DELETE_MANAGED_DATABASE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3941FA5C-0109-4056-BACE-C98EB1036B91)
- [DELETE_PREFERRED_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-375AC248-09F2-4262-AD69-5000956FD4DF)
- [DISABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0DBB4F21-CAB6-4B1B-A665-0A7B3CAAA171)
- [DISABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-26039AD8-68CE-4D8F-9709-594CD9DA4A26)
- [DISABLE_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CB06DBC2-CAF6-4FF5-A405-1B5CB776C93F)
- [DISABLE_EXTERNAL_DB_SYSTEM_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F1C8D1FF-DEE5-4221-98F9-CB0E1D2920F9)
- [DISABLE_EXTERNAL_EXADATA_INFRASTRUCTURE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-1B3A4702-3A67-4E75-AC1F-A849E36C921E)
- [DISABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-385538C0-9395-48FB-8CE5-09630828A2B6)
- [DISABLE_SQL_PLAN_BASELINES_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D65A8FCD-2767-498A-B11E-B14FD559EBA4)
- [DISCOVER_EXTERNAL_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-E3A1AF63-4D05-4A98-8F03-9397CF4F871D)
- [DROP_SQL_PLAN_BASELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CCC434B8-11AD-4B26-9304-4C1170AAD830)
- [DROP_TABLESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-306FD09C-C456-40B7-ACC4-896C8F8F96B1)
- [ENABLE_AUTOMATIC_INITIAL_PLAN_CAPTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-795CE892-E779-499D-9D2F-08CFA352A0A3)
- [ENABLE_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-97C22DFD-5C1E-40E6-ADC6-9D1B767FF8FE)
- [ENABLE_EXTERNAL_DB_SYSTEM_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-2E068D8D-81D9-481A-A649-C7049A737558)
- [ENABLE_EXTERNAL_DB_SYSTEM_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B16BCB60-159F-4748-B63E-F579DD1B298B)
- [ENABLE_EXTERNAL_EXADATA_INFRASTRUCTURE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-DA22E625-799F-4451-AD4E-2ACDD0B53FAF)
- [ENABLE_HIGH_FREQUENCY_AUTOMATIC_SPM_EVOLVE_ADVISOR_TASK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-E4B53869-F90D-4770-B81F-D92C88CE50E7)
- [ENABLE_SQL_PLAN_BASELINES_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-FAD514B9-86FC-4928-939A-D6D1EA54844E)
- [GENERATE_AWR_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CFAD3C26-12FD-4B74-B5F4-FD29323F10BA)
- [GET_AWR_DB_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-4905E12C-5A06-44FE-A054-AF7DF205F92D)
- [GET_AWR_DB_SQL_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-7CEF3329-F85E-41FA-B0FB-8CA8567C79D8)
- [GET_CLUSTER_CACHE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-121C4D8B-09E9-458D-AC07-570B514E4A08)
- [GET_DATABASE_FLEET_HEALTH_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0B366663-3043-49B6-BF8B-D580A02C3472)
- [GET_DATABASE_HOME_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CE790EFA-21C8-49C9-9411-C5592BF8C0F5)
- [GET_DB_MANAGEMENT_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D60D88FC-BFB2-4A53-BED5-D9C626ED7676)
- [GET_EXTERNAL_ASM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-1FC762D7-48C1-4B73-8AED-0C5571EB8142)
- [GET_EXTERNAL_ASM_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-2098F869-BA0E-494A-B5E2-659B3C06A32D)
- [GET_EXTERNAL_ASM_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-888D4A4A-5741-48C1-A807-14D2C59A5B3E)
- [GET_EXTERNAL_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-9BF27B28-FCE6-45EA-A75A-6662489BB586)
- [GET_EXTERNAL_CLUSTER_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-852F8BCA-AEA4-499A-AB8E-0077D4483A4C)
- [GET_EXTERNAL_DB_HOME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3E7D95D2-3807-44F7-8F90-45C88CDB673D)
- [GET_EXTERNAL_DB_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-E0E66A87-FCE4-46D9-A249-9CE51B9679B3)
- [GET_EXTERNAL_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F36C1AA2-71DE-41F7-835B-59824B54D1AB)
- [GET_EXTERNAL_DB_SYSTEM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CD4899C8-BFB1-41CB-AD65-5E5F70286EA2)
- [GET_EXTERNAL_DB_SYSTEM_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B66DB269-9911-4D98-BFF4-1C1A85B24F56)
- [GET_EXTERNAL_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-2765BA9D-DBA0-4363-BFA4-27CE80148EF1)
- [GET_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-E0CB53F4-3BC7-482F-85B9-53E0F84CAC18)
- [GET_EXTERNAL_EXADATA_STORAGE_GRID Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-EF7CCD98-C0C8-4EF2-8E64-B2272B69D0AF)
- [GET_EXTERNAL_EXADATA_STORAGE_SERVER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-6BE0E6D5-EEFB-4DBE-B47A-5512DCB1147A)
- [GET_EXTERNAL_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B332409B-9CD6-4304-8CF3-9B88C5B8B0B7)
- [GET_IORM_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-A6F186EC-9630-4B9D-9EB8-431D19AC34E2)
- [GET_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D960F0C9-7CA2-4E10-A246-33D7B81A7A3E)
- [GET_JOB_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B2F4DB62-B6EF-4178-B1C1-40649920CFF4)
- [GET_JOB_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-327A8104-D0D9-40C4-92A2-AF08E9BE118F)
- [GET_MANAGED_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-45875789-CDDE-48A9-9E66-3B528BD6F863)
- [GET_MANAGED_DATABASE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-AB543D9A-F987-4D17-AAF9-7C1CC4121049)
- [GET_OPEN_ALERT_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3358C2A7-689D-4A40-92A3-F988A94670FF)
- [GET_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-EE0AD771-A0F1-46CC-8208-03009DD54F3A)
- [GET_OPTIMIZER_STATISTICS_ADVISOR_EXECUTION_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F262EB92-FDAA-4959-B5A6-565A37AB1161)
- [GET_OPTIMIZER_STATISTICS_COLLECTION_OPERATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D1B11C67-B73B-4C03-BDF9-421605D02FBA)
- [GET_PDB_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-C8C63096-A3F2-4000-A2A5-F474573F77FB)
- [GET_PREFERRED_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-9495E3CC-6B65-4A70-ADE9-51F760F19312)
- [GET_SQL_PLAN_BASELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D07DBB6B-8978-44A8-817D-8780708224F7)
- [GET_SQL_PLAN_BASELINE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B1F621F6-6D4E-422F-8671-2FD94442B166)
- [GET_TABLESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-DF6C01CC-C890-41C7-A027-64B91B7A41E9)
- [GET_TOP_SQL_CPU_ACTIVITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5B37CC92-5B35-40A8-BE4E-5AEFADA810D7)
- [GET_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-84332630-90B1-47AB-8831-473729725EF4)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-71BD2F48-20DB-43E5-8CCA-A2C07A642814)
- [IMPLEMENT_OPTIMIZER_STATISTICS_ADVISOR_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-FFACCCBD-C822-4ECB-99B3-47254064C313)
- [LIST_ASM_PROPERTIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-845C4829-4C1A-430C-9517-D0143DE9CB69)
- [LIST_ASSOCIATED_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-71AF572B-9B65-448E-96D2-6A418D31A348)
- [LIST_AWR_DB_SNAPSHOTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-22D841E1-92EF-42EE-A4FC-AE8252A4D08A)
- [LIST_AWR_DBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F2787614-40DB-40BE-B4DF-6B5DEDD628A9)
- [LIST_CONSUMER_GROUP_PRIVILEGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-A2EFB1C0-D6EC-40F6-A072-851AE7F8088B)
- [LIST_CURSOR_CACHE_STATEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-539C53A4-0DBE-4151-B67D-234AD1AC1725)
- [LIST_DATA_ACCESS_CONTAINERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-64CC1CCA-2E28-4895-BAA6-A46320AA020B)
- [LIST_DATABASE_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-DE69F920-3391-4325-9AD4-BD0C44809253)
- [LIST_DB_MANAGEMENT_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-707F2B2A-62D3-425E-A44C-6CC6221BC8B5)
- [LIST_EXTERNAL_ASM_DISK_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-EB0AC43F-C2CB-4C3A-8224-80094E7ABEF1)
- [LIST_EXTERNAL_ASM_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-937164A3-21BD-4928-971D-274BCC646EFC)
- [LIST_EXTERNAL_ASM_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-44F6C0FC-2D6B-4070-B8CE-258174B99B07)
- [LIST_EXTERNAL_ASMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0F0EE8C4-3390-41A8-9487-56F3CCD34229)
- [LIST_EXTERNAL_CLUSTER_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CF73D74B-D515-488D-9A6A-2F5404290D41)
- [LIST_EXTERNAL_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F10813CC-D982-455C-A602-723C944EBBFA)
- [LIST_EXTERNAL_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-168DFBAE-EEB4-408E-ADE9-A43243D550FB)
- [LIST_EXTERNAL_DB_HOMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-E2C0914A-3062-4216-9511-811F3480C3CD)
- [LIST_EXTERNAL_DB_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-DC9121B6-E6A1-4D65-96BC-2DFF88CDDB17)
- [LIST_EXTERNAL_DB_SYSTEM_CONNECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-C2E5280A-09A8-4D75-8F2D-40358471DD35)
- [LIST_EXTERNAL_DB_SYSTEM_DISCOVERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5CFF5EA6-69A9-4E3C-ABE4-109EB1B137F2)
- [LIST_EXTERNAL_DB_SYSTEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-9CF6D310-1982-46A9-9056-5677EE52F856)
- [LIST_EXTERNAL_EXADATA_INFRASTRUCTURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-A70DF373-B7E2-45DC-89E3-840CB0A458BC)
- [LIST_EXTERNAL_EXADATA_STORAGE_CONNECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-89F1B7C0-D0CF-4FE0-82F6-A10BF07809A6)
- [LIST_EXTERNAL_EXADATA_STORAGE_SERVERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-66AA06D5-D308-43B0-B511-01277B14C1FB)
- [LIST_EXTERNAL_LISTENER_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-2CD3D36A-D266-458C-8809-CE059C13917C)
- [LIST_EXTERNAL_LISTENERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-07438916-7282-40D4-B8AA-AB6A4BC40973)
- [LIST_JOB_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-8B491824-A227-4C9C-BFFC-63000B9D4C1B)
- [LIST_JOB_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-392932E8-6500-4C9B-B2BD-7FF2B9AAD31A)
- [LIST_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3DD2972A-658C-4669-8E84-824664478662)
- [LIST_MANAGED_DATABASE_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-6627965A-8267-471B-839F-29501A39ED53)
- [LIST_MANAGED_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-238D48AD-41C2-47EB-88E7-E2FBC96BED6F)
- [LIST_OBJECT_PRIVILEGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-1296DE3F-2E8C-4EA0-968E-98A6B1E7A852)
- [LIST_OPTIMIZER_STATISTICS_ADVISOR_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-60994A9B-68AB-42C6-A550-A87235048759)
- [LIST_OPTIMIZER_STATISTICS_COLLECTION_AGGREGATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-13D56FDC-4829-401F-8A8D-DED552462DBC)
- [LIST_OPTIMIZER_STATISTICS_COLLECTION_OPERATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B90D58AA-CE4B-424C-8F9B-896D523CDB69)
- [LIST_PREFERRED_CREDENTIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-63ECDECB-1D3F-42AA-BF0A-B3A2B1CB6011)
- [LIST_PROXIED_FOR_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-57C4F76D-3711-43E1-B0D9-BB925EAC6F66)
- [LIST_PROXY_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-7EBBA8BD-FBF9-4158-96A6-FD5C667791FD)
- [LIST_ROLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-6C37C4BD-FFD7-4FD9-97A0-192C74EC2B2C)
- [LIST_SQL_PLAN_BASELINE_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5898D4DF-E05D-4233-BA84-E5FBFB1FD762)
- [LIST_SQL_PLAN_BASELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-403BE0F8-0C5C-4BF3-906F-F9E35A6DC6EE)
- [LIST_SYSTEM_PRIVILEGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-64BA93B3-C071-495F-A01B-D89904040E42)
- [LIST_TABLE_STATISTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D2AF0200-BD12-42E2-85A5-18BF63E942E5)
- [LIST_TABLESPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0466DC3D-3A93-4F34-92F4-64E4E976439B)
- [LIST_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-66EFF993-440A-4451-B5D4-6FE6FC3D4D1A)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-778EABB9-0B18-44F3-B134-ABE38EF24401)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-D7C10F8E-4671-427B-A336-1456BA906E33)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CA30A7CB-DF39-4351-8E9C-3EE01A7E4A70)
- [LOAD_SQL_PLAN_BASELINES_FROM_AWR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-17447EF2-AC5C-4255-9178-1F00EBC535AB)
- [LOAD_SQL_PLAN_BASELINES_FROM_CURSOR_CACHE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F7A0E350-BA0B-4618-8074-A8851D7C3246)
- [PATCH_EXTERNAL_DB_SYSTEM_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-1F6F135F-3791-4660-8996-6812923A353E)
- [REMOVE_DATA_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-22F2F10E-6E0E-4160-919A-CD60B9082E89)
- [REMOVE_MANAGED_DATABASE_FROM_MANAGED_DATABASE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-58C8072D-8513-4162-94AE-DAAB017B866E)
- [RESET_DATABASE_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-C6C93776-934B-4E52-B776-9B6D0A8F3195)
- [RESIZE_DATA_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0653EFDE-B13D-4CB6-9D12-86CC2992EAB1)
- [RUN_HISTORIC_ADDM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3AC6B50D-323A-4247-8C81-D50A9A0DF66F)
- [SUMMARIZE_AWR_DB_CPU_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-913352E0-3374-4438-B532-3D31266A824C)
- [SUMMARIZE_AWR_DB_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-5749270C-074A-4719-8831-521537886CBB)
- [SUMMARIZE_AWR_DB_PARAMETER_CHANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-3B21FEC4-D801-4D73-8113-9208F4A48598)
- [SUMMARIZE_AWR_DB_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-34C09067-8580-43F2-8FC1-F286372C214B)
- [SUMMARIZE_AWR_DB_SNAPSHOT_RANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-834F5E15-54E0-4EEA-A3E3-EC3FC92B9C57)
- [SUMMARIZE_AWR_DB_SYSSTATS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-8B4C9DE3-5CA0-4941-933A-8BA58583C00A)
- [SUMMARIZE_AWR_DB_TOP_WAIT_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-8C28F5B1-37CF-4F70-B02F-C90AE03589FE)
- [SUMMARIZE_AWR_DB_WAIT_EVENT_BUCKETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-4BBC0DEE-4F29-4F6C-9ADE-19B1FD732091)
- [SUMMARIZE_AWR_DB_WAIT_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-C739DF75-1A6E-4262-9300-2387C598671B)
- [SUMMARIZE_EXTERNAL_ASM_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-7268164B-B00F-4C79-AE0B-F9626350A322)
- [SUMMARIZE_EXTERNAL_CLUSTER_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-37423911-8D64-4388-9D6F-C22B0564A3A6)
- [SUMMARIZE_EXTERNAL_DB_NODE_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-BF70303E-66DC-4D3A-A61F-B2751D1ED131)
- [SUMMARIZE_EXTERNAL_DB_SYSTEM_AVAILABILITY_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-0DA66D1C-83A4-4A1E-8583-D0D5BB254884)
- [SUMMARIZE_EXTERNAL_LISTENER_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F0D4CAF3-E77C-46B2-92FA-6C857817F62F)
- [SUMMARIZE_JOB_EXECUTIONS_STATUSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B6864D62-A655-4C1D-B493-9426EE71785E)
- [SUMMARIZE_MANAGED_DATABASE_AVAILABILITY_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-99F50DEC-BEB1-46AB-9A19-D2F0BF6BB171)
- [SUMMARIZE_SQL_PLAN_BASELINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-033AC9E1-9828-4E5E-8CB1-3AE011DA0DEB)
- [SUMMARIZE_SQL_PLAN_BASELINES_BY_LAST_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-4616EFC8-0D6A-4B49-91DA-8C7A2E5BB1D2)
- [TEST_PREFERRED_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B128980E-8968-4CA3-BC4E-9ECCA267FD9D)
- [UPDATE_DB_MANAGEMENT_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-E09BE431-664C-4C3B-AE22-4C6E7D2DD89E)
- [UPDATE_EXTERNAL_ASM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-78229E7B-83FC-413A-A114-DF255FE86DFF)
- [UPDATE_EXTERNAL_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-07F40CE2-78E6-450B-B7AA-63439BCD8631)
- [UPDATE_EXTERNAL_CLUSTER_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-DE39E420-F639-434E-8360-96DE945DE4F4)
- [UPDATE_EXTERNAL_DB_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-1D60CC2E-B9A2-4647-AEFA-641843924189)
- [UPDATE_EXTERNAL_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-6AC1934C-16D6-45CF-AE6F-181E014463FE)
- [UPDATE_EXTERNAL_DB_SYSTEM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-CAA1BD34-7F50-43FD-B28D-3FDE59E9619C)
- [UPDATE_EXTERNAL_DB_SYSTEM_DISCOVERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-BD13779E-35CD-4FEE-89C4-34F6FDBC6664)
- [UPDATE_EXTERNAL_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-074E3F69-BDB0-4F6D-959A-E2FE1688949A)
- [UPDATE_EXTERNAL_EXADATA_STORAGE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-7A53A3C8-9D24-4D57-BE90-E5B2944C0D2E)
- [UPDATE_EXTERNAL_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-B4AAD8DA-A2ED-4F66-88ED-9A3813D551AA)
- [UPDATE_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-DA2057AC-8938-4421-BB23-22CD9483D649)
- [UPDATE_MANAGED_DATABASE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-F7FD1057-D34D-4ACE-8CC5-2B614005208A)
- [UPDATE_PREFERRED_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-A9129349-00FE-47BD-AA6C-4D2FAEC07CA8)
- [UPDATE_TABLESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_dm_db_management.html#ADSDK-GUID-77402EC3-43A1-4D64-B4D0-2B3ADFD0176A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
