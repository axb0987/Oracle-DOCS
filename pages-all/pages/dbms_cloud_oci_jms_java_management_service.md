# JMS Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#dcoc-content-body)

## JMS Functions

Package: DBMS_CLOUD_OCI_JMS_JAVA_MANAGEMENT_SERVICE

### ADD_FLEET_INSTALLATION_SITES Function

Add Java installation sites in a Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`add_fleet_installation_sites_details`

(required) List of installation sites to be added.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Deletes the work request specified by an identifier.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous work request.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FLEET_COMPARTMENT Function

Move a specified Fleet into the compartment identified in the POST form. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`change_fleet_compartment_details`

(required) Compartment identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BLOCKLIST Function

Add a new record to the fleet blocklist.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`create_blocklist_details`

(required) Details for the new blocklist record.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DRS_FILE Function

Request to perform validaition of the DRS file and create the file to the Object Storage.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`create_drs_file_details`

(required) Detail information to create DRS

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FLEET Function

Create a new Fleet using the information provided. `inventoryLog` is now a required parameter for CreateFleet API. Update existing applications using this API before July 15, 2022 to ensure the applications continue to work. See the[Service Change Notice](https://docs.oracle.com/iaas/Content/servicechanges.htm#JMS)for more details. Migrate existing fleets using the `UpdateFleet` API to set the `inventoryLog` parameter.

Syntax
```

```

Parameters

Parameter Description

`create_fleet_details`

(required) Details for the new Fleet.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BLOCKLIST Function

Deletes the blocklist record specified by an identifier.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`blocklist_key`

(required) The unique identifier of the blocklist record.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CRYPTO_ANALYSIS_RESULT Function

Deletes the metadata for the result of a Crypto event analysis. The actual report shall remain in the object storage.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`crypto_analysis_result_id`

(required) The OCID of the analysis result.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DRS_FILE Function

Request to delete the DRS file from the Object Storage.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`drs_file_key`

(required) The unique identifier of the DRS File in Object Storage.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FLEET Function

Deletes the Fleet specified by an identifier.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_JAVA_MIGRATION_ANALYSIS_RESULT Function

Delete the Java migration analysis result. The actual report will remain in the Object Storage bucket.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`java_migration_analysis_result_id`

(required) The OCID of the analysis result.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PERFORMANCE_TUNING_ANALYSIS_RESULT Function

Deletes only the metadata of the Performance Tuning Analysis result, but the file remains in the object storage.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`performance_tuning_analysis_result_id`

(required) The OCID of the performance tuning analysis result.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_DRS Function

Request to disable the DRS in the selected target in the Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`disable_drs_details`

(required) Detail information to disable DRS

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_DRS Function

Request to enable the DRS in the selected target in the Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`enable_drs_details`

(required) Detail information to enable DRS

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_AGENT_DEPLOY_SCRIPT Function

Generates Agent Deploy Script for Fleet using the information provided.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`generate_agent_deploy_script_details`

(required) Attributes to generate the agent deploy script for a Fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CRYPTO_ANALYSIS_RESULT Function

Retrieve the metadata for the result of a Crypto event analysis.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`crypto_analysis_result_id`

(required) The OCID of the analysis result.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DRS_FILE Function

Get the detail about the created DRS file in the Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`drs_file_key`

(required) The unique identifier of the DRS File in Object Storage.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXPORT_SETTING Function

Returns export setting for the specified Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXPORT_STATUS Function

Returns last export status for the specified Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FLEET Function

Retrieve a Fleet with the specified identifier.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FLEET_ADVANCED_FEATURE_CONFIGURATION Function

Returns Fleet level advanced feature configuration.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FLEET_AGENT_CONFIGURATION Function

Retrieve a Fleet Agent Configuration for the specified Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_FAMILY Function

Returns metadata associated with a specific Java release family.

Syntax
```

```

Parameters

Parameter Description

`family_version`

(required) Unique Java family version identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_MIGRATION_ANALYSIS_RESULT Function

Retrieve Java Migration Analysis result.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`java_migration_analysis_result_id`

(required) The OCID of the analysis result.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_JAVA_RELEASE Function

Returns detail of a Java release.

Syntax
```

```

Parameters

Parameter Description

`release_version`

(required) Unique Java release version identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PERFORMANCE_TUNING_ANALYSIS_RESULT Function

Retrieve metadata of the Performance Tuning Analysis result.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`performance_tuning_analysis_result_id`

(required) The OCID of the performance tuning analysis result.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Retrieve the details of a work request with the specified ID.

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

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ANNOUNCEMENTS Function

Return a list of AnnouncementSummary items

Syntax
```

```

Parameters

Parameter Description

`summary_contains`

(optional) Filter the list with summary contains the given value.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort AnnouncementSummary by. Only one sort order may be provided. If no value is specified _timeReleased_ is default.

Allowed values are: 'timeReleased', 'summary'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BLOCKLISTS Function

Returns a list of blocklist entities contained by a fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`operation`

(optional) The operation type.

Allowed values are: 'CREATE_FLEET', 'DELETE_FLEET', 'MOVE_FLEET', 'UPDATE_FLEET', 'UPDATE_FLEET_AGENT_CONFIGURATION', 'DELETE_JAVA_INSTALLATION', 'CREATE_JAVA_INSTALLATION', 'COLLECT_JFR', 'REQUEST_CRYPTO_EVENT_ANALYSIS', 'REQUEST_PERFORMANCE_TUNING_ANALYSIS', 'REQUEST_JAVA_MIGRATION_ANALYSIS', 'DELETE_JMS_REPORT', 'SCAN_JAVA_SERVER_USAGE', 'SCAN_LIBRARY_USAGE', 'EXPORT_DATA_CSV', 'CREATE_DRS_FILE', 'UPDATE_DRS_FILE', 'DELETE_DRS_FILE', 'ENABLE_DRS', 'DISABLE_DRS'

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used to sort blocklist records. Only one sort order may be provided. Default order for _operation_ is **ascending**. If no value is specified, _operation_ is default.

Allowed values are: 'operation'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CRYPTO_ANALYSIS_RESULTS Function

Lists the results of a Crypto event analysis.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`aggregation_mode`

(optional) The aggregation mode of the crypto event analysis result.

Allowed values are: 'JFR', 'MANAGED_INSTANCE'

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort crypto event analysis results. Only one sort order can be provided. Default order for _timeCreated_, and _jreVersion_ is **descending**. Default order for _managedInstanceId_, _jreDistribution_, _jreVendor_ and _osName_ is **ascending**. If no value is specified _timeCreated_ is default.

Allowed values are: 'timeCreated', 'managedInstanceId', 'workRequestId'

`opc_request_id`

(optional) The client request ID for tracing.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRS_FILES Function

List the details about the created DRS files in the Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field that sorts the DRS details results. Only one sort order can be provided. The default order for _drsFileKey_ is **descending**. If no value is specified, then _drsFileKey_ is default.

Allowed values are: 'bucketName', 'namespace', 'drsFileKey', 'drsFileName', 'checksumType', 'isDefault'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FLEET_DIAGNOSES Function

List potential diagnoses that would put a fleet into FAILED or NEEDS_ATTENTION lifecycle state.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FLEETS Function

Returns a list of all the Fleets contained by a compartment. The query parameter `compartmentId` is required unless the query parameter `id` is specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`id`

(optional) The ID of the Fleet.

`lifecycle_state`

(optional) The state of the lifecycle.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`display_name`

(optional) The display name.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort Fleets. Only one sort order may be provided. Default order for _timeCreated_, _approximateJreCount_, _approximateInstallationCount_, _approximateApplicationCount_ and _approximateManagedInstanceCount_ is **descending**. Default order for _displayName_ is **ascending**. If no value is specified _timeCreated_ is default.

Allowed values are: 'displayName', 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`display_name_contains`

(optional) Filter the list with displayName contains the given value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INSTALLATION_SITES Function

List Java installation sites in a Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`jre_vendor`

(optional) The vendor of the related Java Runtime.

`jre_distribution`

(optional) The distribution of the related Java Runtime.

`jre_version`

(optional) The version of the related Java Runtime.

`installation_path`

(optional) The file system path of the installation.

`application_id`

(optional) The Fleet-unique identifier of the related application.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort installation sites. Only one sort order may be provided. Default order for _timeLastSeen_, and _jreVersion_, _approximateApplicationCount_ is **descending**. Default order for _managedInstanceId_, _jreDistribution_, _jreVendor_ and _osName_ is **ascending**. If no value is specified _managedInstanceId_ is default.

Allowed values are: 'managedInstanceId', 'jreDistribution', 'jreVendor', 'jreVersion', 'path', 'approximateApplicationCount', 'osName', 'securityStatus'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The operating system type.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`jre_security_status`

(optional) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`path_contains`

(optional) Filter the list with path contains the given value.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_FAMILIES Function

Returns a list of the Java release family information. A Java release family is typically a major version in the Java version identifier.

Syntax
```

```

Parameters

Parameter Description

`family_version`

(optional) The version identifier for the Java family.

`display_name`

(optional) The display name for the Java family.

`is_supported_version`

(optional) Filter the Java Release Family versions by support status.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If no value is specified _familyVersion_ is default.

Allowed values are: 'familyVersion', 'endOfSupportLifeDate', 'supportType'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_MIGRATION_ANALYSIS_RESULTS Function

Lists the results of a Java migration analysis.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field that sorts the Java migration analysis results. Only one sort order can be provided. The default order for _timeCreated_, _managedInstanceId_ and _workRequestId_ is **descending**. If no value is specified, then _timeCreated_ is default.

Allowed values are: 'timeCreated', 'managedInstanceId', 'workRequestId'

`opc_request_id`

(optional) The client request ID for tracing.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JAVA_RELEASES Function

Returns a list of Java releases.

Syntax
```

```

Parameters

Parameter Description

`release_version`

(optional) Unique Java release version identifier

`family_version`

(optional) The version identifier for the Java family.

`release_type`

(optional) Java release type.

Allowed values are: 'CPU', 'FEATURE', 'BPR', 'PATCH_RELEASE'

`jre_security_status`

(optional) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`license_type`

(optional) Java license type.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If no value is specified _releaseDate_ is default.

Allowed values are: 'releaseDate', 'releaseVersion', 'familyVersion', 'licenseType'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_JRE_USAGE Function

List Java Runtime usage in a specified host filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`host_id`

(optional) The host[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the managed instance.

`application_id`

(optional) The Fleet-unique identifier of the application.

`application_name`

(optional) The name of the application.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort JRE usages. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, and _version_ is **descending**. Default order for _timeFirstSeen_, _timeLastSeen_, _version_, _approximateInstallationCount_, _approximateApplicationCount_ and _approximateManagedInstanceCount_ is **descending**. Default order for _distribution_, _vendor_, and _osName_ is **ascending**. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'distribution', 'timeFirstSeen', 'timeLastSeen', 'vendor', 'version', 'approximateInstallationCount', 'approximateApplicationCount', 'approximateManagedInstanceCount', 'osName', 'securityStatus'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PERFORMANCE_TUNING_ANALYSIS_RESULTS Function

List Performance Tuning Analysis results.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`application_id`

(optional) The Fleet-unique identifier of the related application.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort performance tuning analysis results. Only one sort order may be provided. Default order for _timeCreated_, and _jreVersion_ is **descending**. Default order for _managedInstanceId_, _jreDistribution_, _jreVendor_ and _osName_ is **ascending**. If no value is specified _timeCreated_ is default.

Allowed values are: 'timeCreated', 'managedInstanceId', 'workRequestId'

`opc_request_id`

(optional) The client request ID for tracing.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_ITEMS Function

Retrieve a paginated list of work items for a specified work request.

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

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Retrieve a (paginated) list of errors for a specified work request.

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

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Retrieve a paginated list of logs for a specified work request.

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

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

List the work requests in a compartment. The query parameter `compartmentId` is required unless the query parameter `id` or `fleetId` is specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`id`

(optional) The ID of an asynchronous work request.

`fleet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the fleet.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`managed_instance_id`

(optional) The Fleet-unique identifier of the managed instance.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_FLEET_INSTALLATION_SITES Function

Remove Java installation sites in a Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`remove_fleet_installation_sites_details`

(required) List of installation sites to be deleted.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_CRYPTO_ANALYSES Function

Request to perform crypto analysis on one or more selected targets in the Fleet. The result of the crypto analysis will be uploaded to the object storage bucket created by JMS on enabling the Crypto Event Analysis feature in the Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`request_crypto_analyses_details`

(required) Detail information to start Crypto Analyses

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_JAVA_MIGRATION_ANALYSES Function

Request to perform a Java migration analysis. The results of the Java migration analysis will be uploaded to the Object Storage bucket that you designate when you enable the Java Migration Analysis feature.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`request_java_migration_analyses_details`

(required) Detail information that starts the Java migration analysis

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_JFR_RECORDINGS Function

Request to collect the JFR recordings on the selected target in the Fleet. The JFR files are uploaded to the object storage bucket created by JMS on enabling Generic JFR feature in the Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`request_jfr_recordings_details`

(required) Detail information to start JFR recordings.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_PERFORMANCE_TUNING_ANALYSES Function

Request to perform performance tuning analyses. The result of performance tuning analysis will be uploaded to the object storage bucket that you designated when you enabled the recording feature.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`request_performance_tuning_analyses_details`

(required) Detail information to start Performance Tuning Analyses

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SCAN_JAVA_SERVER_USAGE Function

Scan Java Server usage in a fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`scan_java_server_usage_details`

(required) List of managed instances to be scanned.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SCAN_LIBRARY_USAGE Function

Scan library usage in a fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`scan_library_usage_details`

(required) List of managed instances to be scanned.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_APPLICATION_INSTALLATION_USAGE Function

Summarizes the application installation usage in a Fleet filtered by query parameters. In contrast to SummarizeApplicationUsage, which provides only information aggregated by application name, this operation provides installation details. This allows for better focusing of actions.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`application_installation_key`

(optional) The Fleet-unique identifier of the application installation.

`application_id`

(optional) The Fleet-unique identifier of the application.

`display_name`

(optional) The display name.

`display_name_contains`

(optional) Filter the list with displayName contains the given value.

`application_type`

(optional) The type of the application.

`app_installation_path_contains`

(optional) Filter the list with the application installation path that contains the given value.

`jre_vendor`

(optional) The vendor of the related Java Runtime.

`jre_distribution`

(optional) The distribution of the related Java Runtime.

`jre_version`

(optional) The version of the related Java Runtime.

`installation_path`

(optional) The file system path of the Java Runtime installation.

`library_key`

(optional) The library key.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`os_family`

(optional) The operating system type.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort application installation views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, _approximateJreCount_, _approximateInstallationCount_ and _approximateManagedInstanceCount_ is **descending**. Default order for _displayName_, _installationPath_ and _osName_ is **ascending**. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'timeFirstSeen', 'timeLastSeen', 'displayName', 'installationPath', 'osName', 'approximateJreCount', 'approximateInstallationCount', 'approximateManagedInstanceCount'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_APPLICATION_USAGE Function

List application usage in a Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`application_id`

(optional) The Fleet-unique identifier of the application.

`display_name`

(optional) The display name.

`application_type`

(optional) The type of the application.

`jre_vendor`

(optional) The vendor of the related Java Runtime.

`jre_distribution`

(optional) The distribution of the related Java Runtime.

`jre_version`

(optional) The version of the related Java Runtime.

`installation_path`

(optional) The file system path of the Java Runtime installation.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`fields`

(optional) Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'. For example 'approximateJreCount,approximateInstallationCount'.

Allowed values are: 'approximateJreCount', 'approximateInstallationCount', 'approximateManagedInstanceCount'

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort application views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, _approximateJreCount_, _approximateInstallationCount_ and _approximateManagedInstanceCount_ is **descending**. Default order for _displayName_ and _osName_ is **ascending**. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'timeFirstSeen', 'timeLastSeen', 'displayName', 'approximateJreCount', 'approximateInstallationCount', 'approximateManagedInstanceCount', 'osName'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The operating system type.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`display_name_contains`

(optional) Filter the list with displayName contains the given value.

`library_key`

(optional) The library key.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DEPLOYED_APPLICATION_INSTALLATION_USAGE Function

Summarize installation usage of an application deployed on Java servers in a fleet filtered by query parameters. In contrast to SummarizeDeployedApplicationUsage, which provides only information aggregated by the deployment information, this operation provides installation details and allows for better focusing of actions.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`server_key`

(optional) The server key.

`server_instance_key`

(optional) The Java Server instance key.

`managed_instance_id`

(optional) The Fleet-unique identifier of the managed instance.

`application_installation_key`

(optional) The deployed application installation key.

`application_key`

(optional) The deployed application key.

`application_name_contains`

(optional) Filter the list with deployed application name contains the given value.

`application_name`

(optional) The deployed application name.

`application_source_path_contains`

(optional) Filter the list with application source path contains the given value.

`library_key`

(optional) The library key.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort the deployed application installations. Only one sort order can be provided. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'applicationName', 'applicationType', 'applicationSourcePath', 'isClustered', 'javaServerInstanceCount', 'timeFirstSeen', 'timeLastSeen'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DEPLOYED_APPLICATION_USAGE Function

List of deployed applications in a Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`server_key`

(optional) The server key.

`server_instance_key`

(optional) The Java Server instance key.

`managed_instance_id`

(optional) The Fleet-unique identifier of the managed instance.

`library_key`

(optional) The library key.

`application_key`

(optional) The deployed application key.

`application_name_contains`

(optional) Filter the list with deployed application name contains the given value.

`application_name`

(optional) The deployed application name.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort the deployed applications. Only one sort order can be provided. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'applicationName', 'applicationType', 'isClustered', 'javaServerInstanceCount', 'timeFirstSeen', 'timeLastSeen'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_INSTALLATION_USAGE Function

List Java installation usage in a Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`jre_vendor`

(optional) The vendor of the related Java Runtime.

`jre_distribution`

(optional) The distribution of the related Java Runtime.

`jre_version`

(optional) The version of the related Java Runtime.

`installation_path`

(optional) The file system path of the installation.

`application_id`

(optional) The Fleet-unique identifier of the related application.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`fields`

(optional) Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateApplicationCount' and 'approximateManagedInstanceCount'. For example 'approximateApplicationCount,approximateManagedInstanceCount'.

Allowed values are: 'approximateApplicationCount', 'approximateManagedInstanceCount'

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort installation views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, and _jreVersion_, _approximateApplicationCount_ and _approximateManagedInstanceCount_ is **descending**. Default order for _jreDistribution_ and _jreVendor_ is **ascending**. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'jreDistribution', 'jreVendor', 'jreVersion', 'path', 'timeFirstSeen', 'timeLastSeen', 'approximateApplicationCount', 'approximateManagedInstanceCount', 'osName'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The operating system type.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`path_contains`

(optional) Filter the list with path contains the given value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_JAVA_SERVER_INSTANCE_USAGE Function

List Java Server instances in a fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`server_key`

(optional) The server key.

`server_instance_key`

(optional) The Java Server instance key.

`managed_instance_id`

(optional) The Fleet-unique identifier of the managed instance.

`application_key`

(optional) The deployed application key.

`library_key`

(optional) The library key.

`server_instance_name_contains`

(optional) Filter the list with the Java Server instance name contains the given value.

`server_instance_name`

(optional) The Java Server instance name.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort the Java Server instances. Only one sort order can be provided. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'serverInstanceName', 'managedInstanceName', 'approximateDeployedApplicationCount', 'timeFirstSeen', 'timeLastSeen'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_JAVA_SERVER_USAGE Function

List of Java servers in a Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`server_key`

(optional) The server key.

`server_name_contains`

(optional) Filter the list with server name contains the given value.

`server_name`

(optional) The server name.

`server_version`

(optional) The server version.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort a Java Server. Only one sort order can be provided. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'serverName', 'serverVersion', 'serverInstanceCount', 'approximateDeployedApplicationCount', 'timeFirstSeen', 'timeLastSeen'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_JRE_USAGE Function

List Java Runtime usage in a specified Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`jre_id`

(optional) The Fleet-unique identifier of the related Java Runtime.

`jre_vendor`

(optional) The vendor of the Java Runtime.

`jre_distribution`

(optional) The distribution of the Java Runtime.

`jre_version`

(optional) The version of the Java Runtime.

`application_id`

(optional) The Fleet-unique identifier of the related application.

`managed_instance_id`

(optional) The Fleet-unique identifier of the related managed instance.

`fields`

(optional) Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateApplicationCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'. For example 'approximateApplicationCount,approximateManagedInstanceCount'.

Allowed values are: 'approximateInstallationCount', 'approximateApplicationCount', 'approximateManagedInstanceCount'

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort JRE usages. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, and _version_ is **descending**. Default order for _timeFirstSeen_, _timeLastSeen_, _version_, _approximateInstallationCount_, _approximateApplicationCount_ and _approximateManagedInstanceCount_ is **descending**. Default order for _distribution_, _vendor_, and _osName_ is **ascending**. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'distribution', 'timeFirstSeen', 'timeLastSeen', 'vendor', 'version', 'approximateInstallationCount', 'approximateApplicationCount', 'approximateManagedInstanceCount', 'osName', 'securityStatus'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The operating system type.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`jre_security_status`

(optional) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_LIBRARY_USAGE Function

List libraries in a fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`server_instance_key`

(optional) The Java Server instance key.

`managed_instance_id`

(optional) The Fleet-unique identifier of the managed instance.

`application_key`

(optional) The deployed application key.

`library_key`

(optional) The library key.

`library_name_contains`

(optional) Filter the list with library name contains the given value.

`library_name`

(optional) The library name.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort libraries. Only one sort order may be provided. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'applicationCount', 'javaServerInstanceCount', 'cvssScore', 'deployedApplicationCount', 'libraryName', 'libraryVersion', 'managedInstanceCount', 'timeFirstSeen', 'timeLastSeen'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_MANAGED_INSTANCE_USAGE Function

List managed instance usage in a Fleet filtered by query parameters.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`managed_instance_id`

(optional) The Fleet-unique identifier of the managed instance.

`managed_instance_type`

(optional) The type of the managed instance.

Allowed values are: 'ORACLE_MANAGEMENT_AGENT'

`jre_vendor`

(optional) The vendor of the related Java Runtime.

`jre_distribution`

(optional) The distribution of the related Java Runtime.

`jre_version`

(optional) The version of the related Java Runtime.

`installation_path`

(optional) The file system path of the Java Runtime installation.

`application_id`

(optional) The Fleet-unique identifier of the related application.

`fields`

(optional) Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateApplicationCount'. For example 'approximateJreCount,approximateInstallationCount'.

Allowed values are: 'approximateJreCount', 'approximateInstallationCount', 'approximateApplicationCount'

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort managed instance views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, approximateJreCount_, _approximateInstallationCount_ and _approximateApplicationCount_ is **descending**. Default order for _osName_ is **ascending**. If no value is specified _timeLastSeen_ is default.

Allowed values are: 'timeFirstSeen', 'timeLastSeen', 'approximateJreCount', 'approximateInstallationCount', 'approximateApplicationCount', 'osName'

`opc_request_id`

(optional) The client request ID for tracing.

`os_family`

(optional) The operating system type.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`hostname_contains`

(optional) Filter the list with hostname contains the given value.

`library_key`

(optional) The library key.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_RESOURCE_INVENTORY Function

Retrieve the inventory of JMS resources in the specified compartment: a list of the number of _active_ fleets, managed instances, Java Runtimes, Java installations, and applications.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`time_start`

(optional) The start of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_end`

(optional) The end of the time period during which resources are searched (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRS_FILE Function

Request to perform validaition of the DRS file and update the existing file in the Object Storage.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`update_drs_file_details`

(required) Detail information to update DRS

`drs_file_key`

(required) The unique identifier of the DRS File in Object Storage.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXPORT_SETTING Function

Updates existing export setting for the specified Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`update_export_setting_details`

(required) The new details for the Export setting.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FLEET Function

Update the Fleet specified by an identifier.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`update_fleet_details`

(required) The new details for the Fleet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FLEET_ADVANCED_FEATURE_CONFIGURATION Function

Update advanced feature configurations for the Fleet. Ensure that the namespace and bucket storage are created prior to turning on the JfrRecording or CryptoEventAnalysis feature.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`update_fleet_advanced_feature_configuration_details`

(required) Update advanced feature configurations with new fields.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FLEET_AGENT_CONFIGURATION Function

Update the Fleet Agent Configuration for the specified Fleet.

Syntax
```

```

Parameters

Parameter Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`update_fleet_agent_configuration_details`

(required) The new details for the Fleet Agent Configuration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://javamanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [JMS Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-6A10EE44-365F-4429-902E-55CFFB83ABFC)
- [ADD_FLEET_INSTALLATION_SITES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-44A7DD25-BC90-44BF-8251-C84596DC0613)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-741BBFF0-5EE3-4E1A-BD6E-03B13B77FA71)
- [CHANGE_FLEET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-33FA22A8-2AF8-4A07-B4CF-52F8AFE908DC)
- [CREATE_BLOCKLIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-8269D3F1-B2D5-4BCC-B1D5-931A52B08B35)
- [CREATE_DRS_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-CAF6C1C0-9B7A-4011-8B70-133375A2B596)
- [CREATE_FLEET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-21F66690-4536-4A52-A63B-90596B858289)
- [DELETE_BLOCKLIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-2DD6C3A8-C13D-43CA-9533-E6730586E138)
- [DELETE_CRYPTO_ANALYSIS_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-207C38C8-60E4-4FC3-BAF9-B7AED517A699)
- [DELETE_DRS_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-6A815C28-4014-4C14-971E-6B2EA93115D5)
- [DELETE_FLEET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-7B77F3FB-1623-48E0-A5BC-6A9FF873BD89)
- [DELETE_JAVA_MIGRATION_ANALYSIS_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-153DE6BC-387E-4D4E-818F-360001985D8E)
- [DELETE_PERFORMANCE_TUNING_ANALYSIS_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-CD12B46B-E2EF-41B1-BF38-CB1CD956121D)
- [DISABLE_DRS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-FBF728D3-61F5-4F99-81AB-6EEA0603E691)
- [ENABLE_DRS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-8285E064-0CA8-4A9C-9891-085077BA149C)
- [GENERATE_AGENT_DEPLOY_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-670A7692-D5A9-4856-BB16-DA42602E333E)
- [GET_CRYPTO_ANALYSIS_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-62EAA66E-77AD-45D3-9C64-C53ADB0CE74D)
- [GET_DRS_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-661971AD-0BC5-42D5-A384-30EA6C55EF3E)
- [GET_EXPORT_SETTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-CB9BEDFE-3FD6-4C49-81BB-BFEFC72BEE66)
- [GET_EXPORT_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-23C5E4B1-DD05-4B34-AD40-5482DCF76B62)
- [GET_FLEET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-05FDEDCD-5560-4BA6-BDBC-96065DF319C1)
- [GET_FLEET_ADVANCED_FEATURE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-D1C959C0-AA66-4570-8C16-A56FE01EFBEC)
- [GET_FLEET_AGENT_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-8542047F-5F79-41B6-B39B-C9D0E1F2DBB9)
- [GET_JAVA_FAMILY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-ED00F37F-6BDF-4F01-B9D7-5DDADB01D37A)
- [GET_JAVA_MIGRATION_ANALYSIS_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-B6FB068E-E700-4C08-BFF9-1FC09C0EC229)
- [GET_JAVA_RELEASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-BC4E1EBE-8581-4F55-8B4E-200CE904986E)
- [GET_PERFORMANCE_TUNING_ANALYSIS_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-F03E6C9E-7CAA-4CBC-A6E3-255E61A19D68)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-622F147F-2BC0-4E98-AA87-EFD3948D1C17)
- [LIST_ANNOUNCEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-C27B60CD-3DC3-46EB-8E9E-8FF5FB809463)
- [LIST_BLOCKLISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-0C737743-C9C4-4032-9DE4-95FC9CC1DBEF)
- [LIST_CRYPTO_ANALYSIS_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-5DF2006B-3315-49AD-A728-B5D25DD71206)
- [LIST_DRS_FILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-94189FC1-F29B-4841-8BB0-2B5E3324F912)
- [LIST_FLEET_DIAGNOSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-DC52E47E-555C-4920-B867-D852470A93D2)
- [LIST_FLEETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-D7EC1EC4-16D6-48F4-B13F-1D122E11604B)
- [LIST_INSTALLATION_SITES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-B2D254BC-58C8-400F-9E46-1C8F99442353)
- [LIST_JAVA_FAMILIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-4E5757B6-E728-4474-BC4C-D0F1ABE4A428)
- [LIST_JAVA_MIGRATION_ANALYSIS_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-F7F6031F-D4A9-47FF-91BC-97D5C6EACFFB)
- [LIST_JAVA_RELEASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-06B3081B-CD8F-4EF3-904A-5A31B1EA1D96)
- [LIST_JRE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-B2A8F8CD-CE9B-4648-950A-A254CE92C344)
- [LIST_PERFORMANCE_TUNING_ANALYSIS_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-9EF520BA-8A46-4B2D-9D59-84ED4D006E44)
- [LIST_WORK_ITEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-FBCBB4BE-B589-4EEE-B9ED-063E1E5ED596)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-5F6C5A47-BFCD-4F3B-BB06-72D6BAB5530F)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-75405812-D748-47B6-A63F-7F0D2BEFC995)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-8E79322F-F2C0-4B86-B5B0-441430C78662)
- [REMOVE_FLEET_INSTALLATION_SITES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-94996A09-375F-4B8F-8E51-01B3EE2F8D56)
- [REQUEST_CRYPTO_ANALYSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-C7F0414B-5F56-4865-984F-8BF43FF07685)
- [REQUEST_JAVA_MIGRATION_ANALYSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-A4BC1FFF-E4F7-4889-ACDE-A6DE62935312)
- [REQUEST_JFR_RECORDINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-992C1F99-3B0C-4AE9-98FF-3F20A7B98331)
- [REQUEST_PERFORMANCE_TUNING_ANALYSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-384ED7C0-132A-496F-B8A3-BCCE97B17985)
- [SCAN_JAVA_SERVER_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-F5D07035-FF5E-47A7-B27F-627D0FB2A707)
- [SCAN_LIBRARY_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-C02C246C-5501-4004-94FC-2D10446B6A33)
- [SUMMARIZE_APPLICATION_INSTALLATION_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-9E73E510-407A-4229-B50A-5704720CF787)
- [SUMMARIZE_APPLICATION_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-4EA4DDDA-A3BD-4283-9B2D-F9321174C5C6)
- [SUMMARIZE_DEPLOYED_APPLICATION_INSTALLATION_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-3D312BEA-5E11-47CC-B60E-1D933643DDDD)
- [SUMMARIZE_DEPLOYED_APPLICATION_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-4A7D6BAA-E4AD-483A-9E66-F750C88FFFA7)
- [SUMMARIZE_INSTALLATION_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-EA1D9231-007C-4BAE-9BD6-466F46DC34B9)
- [SUMMARIZE_JAVA_SERVER_INSTANCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-4B7737BC-C340-4023-B56A-6B4F5DF6DEB9)
- [SUMMARIZE_JAVA_SERVER_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-F857FAC4-AC66-4198-AF24-69A1C98B09E7)
- [SUMMARIZE_JRE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-1FA22576-05DC-45FA-B6CC-481C565C80B9)
- [SUMMARIZE_LIBRARY_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-87D7697C-1F79-4D77-AB4D-1CC2ED0AAE54)
- [SUMMARIZE_MANAGED_INSTANCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-936DA369-7699-4DB0-A013-933D741E0241)
- [SUMMARIZE_RESOURCE_INVENTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-FC1DF403-ABE0-43AD-9734-82D0C7C5CAAC)
- [UPDATE_DRS_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-E19AF672-C848-4B60-84DB-84AFE5C38414)
- [UPDATE_EXPORT_SETTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-E0FC24EE-D381-4169-ACF4-E12FFFCEC8BB)
- [UPDATE_FLEET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-45ECD148-343E-4644-A3EA-4AE00A2FE2B1)
- [UPDATE_FLEET_ADVANCED_FEATURE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-54514EF8-84E7-4D86-AC61-37F10CBD61BB)
- [UPDATE_FLEET_AGENT_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_jms_java_management_service.html#ADSDK-GUID-AE6AA400-342C-46E7-9607-3CA71CEDB12D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
