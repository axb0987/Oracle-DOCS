# MySQL DB System Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#dcoc-content-body)

## MySQL DB System Functions

Package: DBMS_CLOUD_OCI_MS_DB_SYSTEM

### ADD_HEAT_WAVE_CLUSTER Function

Adds a HeatWave cluster to the DB System.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`add_heat_wave_cluster_details`

(required) Request to add a HeatWave cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DB_SYSTEM Function

Creates and launches a DB System.

Syntax
```

```

Parameters

Parameter Description

`create_db_system_details`

(required) Request to create a DB System.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DB_SYSTEM Function

Delete a DB System, including terminating, detaching, removing, finalizing and otherwise deleting all related resources.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_HEAT_WAVE_CLUSTER Function

Deletes the HeatWave cluster including terminating, detaching, removing, finalizing and otherwise deleting all related resources.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_HEAT_WAVE_CLUSTER_MEMORY_ESTIMATE Function

Sends a request to estimate the memory footprints of user tables when loaded to HeatWave cluster memory.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_SYSTEM Function

Get information about the specified DB System.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`if_none_match`

(optional) For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HEAT_WAVE_CLUSTER Function

Gets information about the HeatWave cluster.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`if_none_match`

(optional) For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HEAT_WAVE_CLUSTER_MEMORY_ESTIMATE Function

Gets the most recent HeatWave cluster memory estimate that can be used to determine a suitable HeatWave cluster size.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEMS Function

Get a list of DB Systems in the specified compartment. The default sort order is by timeUpdated, descending.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`is_heat_wave_cluster_attached`

(optional) If true, return only DB Systems with a HeatWave cluster attached, if false return only DB Systems with no HeatWave cluster attached. If not present, return all DB Systems.

`db_system_id`

(optional) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`display_name`

(optional) A filter to return only the resource matching the given display name exactly.

`lifecycle_state`

(optional) DbSystem Lifecycle State

`configuration_id`

(optional) The requested Configuration instance.

`is_up_to_date`

(optional) Filter instances if they are using the latest revision of the Configuration they are associated with.

`database_management`

(optional) Filter DB Systems by their Database Management configuration.

Allowed values are: 'ENABLED', 'DISABLED'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as ascending.

Allowed values are: 'displayName', 'timeCreated'

`sort_order`

(optional) The sort order to use (ASC or DESC).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return in a paginated list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`page`

(optional) The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTART_DB_SYSTEM Function

Restarts the specified DB System.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`restart_db_system_details`

(required) Optional parameters for the stop portion of the restart action.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTART_HEAT_WAVE_CLUSTER Function

Restarts the HeatWave cluster.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_DB_SYSTEM Function

Start the specified DB System.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_HEAT_WAVE_CLUSTER Function

Starts the HeatWave cluster.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_DB_SYSTEM Function

Stops the specified DB System. A stopped DB System is not billed.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`stop_db_system_details`

(required) Optional parameters for the stop action.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_HEAT_WAVE_CLUSTER Function

Stops the HeatWave cluster.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DB_SYSTEM Function

Update the configuration of a DB System. Updating different fields in the DB System will have different results on the uptime of the DB System. For example, changing the displayName of a DB System will take effect immediately, but changing the shape of a DB System is an asynchronous operation that involves provisioning new Compute resources, pausing the DB System and migrating storage before making the DB System available again.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_db_system_details`

(required) Request to update a DB System.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HEAT_WAVE_CLUSTER Function

Updates the HeatWave cluster.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_heat_wave_cluster_details`

(required) Request to update a HeatWave cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [MySQL DB System Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-5ADAD013-2EDE-4DAB-9C1A-66C45BDD730E)
- [ADD_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-6C7CDE33-7F83-4A0A-A66C-C5DD24977979)
- [CREATE_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-9341CD5A-1004-401A-B97D-229F439B3784)
- [DELETE_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-94B2E2BC-C01D-4792-97C4-0788817E74A4)
- [DELETE_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-51655917-74A2-493E-A10A-31383052FCB1)
- [GENERATE_HEAT_WAVE_CLUSTER_MEMORY_ESTIMATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-DAE59EEC-F8D4-45D7-8028-D1DEB9907D4C)
- [GET_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-3D803F28-D4BA-41BB-8638-BE5DE15FEA91)
- [GET_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-D3BF9DF9-CF3F-4D48-B376-F54EE8BB6CE6)
- [GET_HEAT_WAVE_CLUSTER_MEMORY_ESTIMATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-CE69553D-CF78-453D-9868-65B2209B451D)
- [LIST_DB_SYSTEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-7099313F-A708-459F-B2C4-9039B0A26097)
- [RESTART_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-5EC5B3A0-F038-4E47-B1FA-62F84684BD5B)
- [RESTART_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-738C2542-FA59-4095-AD11-856313A9196C)
- [START_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-CCDE3A26-D6FC-42D5-9DFF-C957AA259AFE)
- [START_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-CB4BDF37-6F66-4872-8844-C979A3A0313A)
- [STOP_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-5C1BD430-016F-49A2-BA1A-B1945E43A524)
- [STOP_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-7DF7DCDC-8E71-4A51-92D6-0B9C50B6FC04)
- [UPDATE_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-6F65957C-603B-4A0E-B134-1811DC74DD81)
- [UPDATE_HEAT_WAVE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_system.html#ADSDK-GUID-E5689E38-D644-4DDA-990B-908295DE6C86)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
