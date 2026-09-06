# OPSI Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#dcoc-content-body)

## OPSI Functions

Package: DBMS_CLOUD_OCI_OPSI_OPERATIONS_INSIGHTS

### ADD_EXADATA_INSIGHT_MEMBERS Function

Add new members (e.g. databases and hosts) to an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`add_exadata_insight_members_details`

(required) Details for the members (e.g. databases and hosts) of an Exadata system to be added in Operations Insights.

`exadata_insight_id`

(required) Unique Exadata insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES Function

Update connection detail for advanced features of Autonomous Database in Operations Insights.

Syntax
```

```

Parameters

Parameter Description

`change_autonomous_database_insight_advanced_features_details`

(required) Details for the advanced features of Autonomous Database in Operations Insights.

`database_insight_id`

(required) Unique database insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AWR_HUB_SOURCE_COMPARTMENT Function

Moves an AwrHubSource resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`change_awr_hub_source_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_INSIGHT_COMPARTMENT Function

Moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`change_database_insight_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ENTERPRISE_MANAGER_BRIDGE_COMPARTMENT Function

Moves a EnterpriseManagerBridge resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`enterprise_manager_bridge_id`

(required) Unique Enterprise Manager bridge identifier

`change_enterprise_manager_bridge_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXADATA_INSIGHT_COMPARTMENT Function

Moves an Exadata insight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required) Unique Exadata insight identifier

`change_exadata_insight_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_HOST_INSIGHT_COMPARTMENT Function

Moves a HostInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`host_insight_id`

(required) Unique host insight identifier

`change_host_insight_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_NEWS_REPORT_COMPARTMENT Function

Moves a news report resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`news_report_id`

(required) Unique news report identifier.

`change_news_report_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves a private endpoint from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Operation Insights private endpoint.

`change_operations_insights_private_endpoint_compartment_details`

(required) The details used to change the compartment of a private endpoint

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_OPERATIONS_INSIGHTS_WAREHOUSE_COMPARTMENT Function

Moves a Operations Insights Warehouse resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`change_operations_insights_warehouse_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_OPSI_CONFIGURATION_COMPARTMENT Function

Moves an OpsiConfiguration resource from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`opsi_configuration_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of OPSI configuration resource.

`change_opsi_configuration_compartment_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PE_COMANAGED_DATABASE_INSIGHT Function

Change the connection details of a co-managed database insight. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`change_pe_comanaged_database_insight_details`

(required) The information to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AWR_HUB Function

Create a AWR hub resource for the tenant in Operations Insights. This resource will be created in root compartment.

Syntax
```

```

Parameters

Parameter Description

`create_awr_hub_details`

(required) Details using which an AWR hub resource will be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AWR_HUB_SOURCE Function

Register Awr Hub source

Syntax
```

```

Parameters

Parameter Description

`create_awr_hub_source_details`

(required) Payload containing details to register the source database

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATABASE_INSIGHT Function

Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`create_database_insight_details`

(required) Details for the database for which a Database Insight resource will be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ENTERPRISE_MANAGER_BRIDGE Function

Create a Enterprise Manager bridge in Operations Insights.

Syntax
```

```

Parameters

Parameter Description

`create_enterprise_manager_bridge_details`

(required) Details for the Enterprise Manager bridge to be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXADATA_INSIGHT Function

Create an Exadata insight resource for an Exadata system in Operations Insights. The Exadata system will be enabled in Operations Insights. Exadata-related metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`create_exadata_insight_details`

(required) Details for the Exadata system for which an Exadata insight resource will be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_HOST_INSIGHT Function

Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`create_host_insight_details`

(required) Details for the host for which a Host Insight resource will be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NEWS_REPORT Function

Create a news report in Operations Insights. The report will be enabled in Operations Insights. Insights will be emailed as per selected frequency.

Syntax
```

```

Parameters

Parameter Description

`create_news_report_details`

(required) Details for the news report that will be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function

Create a private endpoint resource for the tenant in Operations Insights. This resource will be created in customer compartment.

Syntax
```

```

Parameters

Parameter Description

`create_operations_insights_private_endpoint_details`

(required) Details to create a new private endpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OPERATIONS_INSIGHTS_WAREHOUSE Function

Create a Operations Insights Warehouse resource for the tenant in Operations Insights. New ADW will be provisioned for this tenant. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. If the 'opsi-warehouse-type' header is passed to the API, a warehouse resource without ADW or Schema provisioning is created.

Syntax
```

```

Parameters

Parameter Description

`create_operations_insights_warehouse_details`

(required) Details using which an Operations Insights Warehouse resource will be created in Operations Insights.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function

Create a Operations Insights Warehouse user resource for the tenant in Operations Insights. This resource will be created in root compartment.

Syntax
```

```

Parameters

Parameter Description

`create_operations_insights_warehouse_user_details`

(required) Parameter using which an Operations Insights Warehouse user resource will be created.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OPSI_CONFIGURATION Function

Create an OPSI configuration resource.

Syntax
```

```

Parameters

Parameter Description

`create_opsi_configuration_details`

(required) Information about OPSI configuration resource to be created.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opsi_config_field`

(optional) Optional fields to return as part of OpsiConfiguration object. Unless requested, these fields will not be returned by default.

Allowed values are: 'configItems'

`config_item_custom_status`

(optional) Specifies whether only customized configuration items or only non-customized configuration items or both have to be returned. By default only customized configuration items are returned.

Allowed values are: 'customized', 'nonCustomized'

`config_items_applicable_context`

(optional) Returns the configuration items filtered by applicable contexts sent in this param. By default configuration items of all applicable contexts are returned.

`config_item_field`

(optional) Specifies the fields to return in a config item summary.

Allowed values are: 'name', 'value', 'defaultValue', 'metadata', 'applicableContexts'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AWR_HUB Function

Deletes an AWR hub.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AWR_HUB_OBJECT Function

Deletes an Awr Hub object.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`object_name`

(required) Unique Awr Hub Object identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AWR_HUB_SOURCE Function

Deletes an Awr Hub source object.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATABASE_INSIGHT Function

Deletes a database insight. The database insight will be deleted and cannot be enabled again.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ENTERPRISE_MANAGER_BRIDGE Function

Deletes an Operations Insights Enterprise Manager bridge. If any database insight is still referencing this bridge, the operation will fail.

Syntax
```

```

Parameters

Parameter Description

`enterprise_manager_bridge_id`

(required) Unique Enterprise Manager bridge identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXADATA_INSIGHT Function

Deletes an Exadata insight. The Exadata insight will be deleted and cannot be enabled again.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required) Unique Exadata insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_HOST_INSIGHT Function

Deletes a host insight. The host insight will be deleted and cannot be enabled again.

Syntax
```

```

Parameters

Parameter Description

`host_insight_id`

(required) Unique host insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NEWS_REPORT Function

Deletes a news report. The news report will be deleted and cannot be enabled again.

Syntax
```

```

Parameters

Parameter Description

`news_report_id`

(required) Unique news report identifier.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function

Deletes a private endpoint.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Operation Insights private endpoint.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OPERATIONS_INSIGHTS_WAREHOUSE Function

Deletes an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. User must delete AWR Hub resource for this warehouse before calling this operation. User must delete the warehouse users before calling this operation.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function

Deletes an Operations Insights Warehouse User.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_user_id`

(required) Unique Operations Insights Warehouse User identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OPSI_CONFIGURATION Function

Deletes an OPSI configuration resource.

Syntax
```

```

Parameters

Parameter Description

`opsi_configuration_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of OPSI configuration resource.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES Function

Disable advanced features for an Autonomous Database in Operations Insights. The connection detail and advanced features will be removed.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_AWR_HUB_SOURCE Function

Disables a Awr Hub source database in Operations Insights. This will stop the Awr data flow for the given Awr Hub source.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_DATABASE_INSIGHT Function

Disables a database in Operations Insights. Database metric collection and analysis will be stopped.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXADATA_INSIGHT Function

Disables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be stopped.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required) Unique Exadata insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_HOST_INSIGHT Function

Disables a host in Operations Insights. Host metric collection and analysis will be stopped.

Syntax
```

```

Parameters

Parameter Description

`host_insight_id`

(required) Unique host insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_OPERATIONS_INSIGHTS_WAREHOUSE_WALLET Function

Download the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`download_operations_insights_warehouse_wallet_details`

(required) The information to be updated.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES Function

Enables advanced features for an Autonomous Database in Operations Insights. A direct connection will be available for further collection.

Syntax
```

```

Parameters

Parameter Description

`enable_autonomous_database_insight_advanced_features_details`

(required) Connection Details for the Autonomous Database in Operations Insights.

`database_insight_id`

(required) Unique database insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_AWR_HUB_SOURCE Function

Enables a Awr Hub source database in Operations Insights. This will resume the Awr data flow for the given Awr Hub source if it was stopped earlier.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_DATABASE_INSIGHT Function

Enables a database in Operations Insights. Database metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`enable_database_insight_details`

(required) Details for the database to be enabled in Operations Insights.

`database_insight_id`

(required) Unique database insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXADATA_INSIGHT Function

Enables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`enable_exadata_insight_details`

(required) Details for the Exadata system to be enabled in Operations Insights.

`exadata_insight_id`

(required) Unique Exadata insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_HOST_INSIGHT Function

Enables a host in Operations Insights. Host metric collection and analysis will be started.

Syntax
```

```

Parameters

Parameter Description

`enable_host_insight_details`

(required) Details for the host to be enabled in Operations Insights.

`host_insight_id`

(required) Unique host insight identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_DATABASE_REPORT Function

Gets the AWR report for the specified database.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`report_type`

(optional) The query parameter to filter the AWR report types.

Allowed values are: 'AWR', 'ASH'

`report_format`

(optional) The format of the AWR report.

Allowed values are: 'HTML', 'TEXT'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_DATABASE_SQL_REPORT Function

Gets the SQL health check report for one SQL of the specified database.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`sql_id`

(required) The parameter to filter SQL by ID. Note that the SQL ID is generated internally by Oracle for each SQL statement and can be retrieved from AWR Report API (/awrHubs/{awrHubId}/awrDbReport).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`report_format`

(optional) The format of the AWR report.

Allowed values are: 'HTML', 'TEXT'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_HUB Function

Gets details of an AWR hub.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_HUB_OBJECT Function

Gets the Awr Hub object metadata and body.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`object_name`

(required) Unique Awr Hub Object identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_HUB_SOURCE Function

Gets the Awr Hub source object.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AWR_REPORT Function

Gets the AWR report for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should not be greater than 7 days. Either beginSnapshotIdentifierGreaterThanOrEqualTo &amp; endSnapshotIdentifierLessThanOrEqualTo params Or timeGreaterThanOrEqualTo &amp; timeLessThanOrEqualTo params are required.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) AWR source database identifier.

`report_format`

(optional) The format of the AWR report. Default report format is HTML.

Allowed values are: 'HTML', 'TEXT'

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_INSIGHT Function

Gets details of a database insight.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ENTERPRISE_MANAGER_BRIDGE Function

Gets details of an Operations Insights Enterprise Manager bridge.

Syntax
```

```

Parameters

Parameter Description

`enterprise_manager_bridge_id`

(required) Unique Enterprise Manager bridge identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXADATA_INSIGHT Function

Gets details of an Exadata insight.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required) Unique Exadata insight identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HOST_INSIGHT Function

Gets details of a host insight.

Syntax
```

```

Parameters

Parameter Description

`host_insight_id`

(required) Unique host insight identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NEWS_REPORT Function

Gets details of a news report.

Syntax
```

```

Parameters

Parameter Description

`news_report_id`

(required) Unique news report identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function

Gets the details of the specified private endpoint.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Operation Insights private endpoint.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPERATIONS_INSIGHTS_WAREHOUSE Function

Gets details of an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function

Gets details of an Operations Insights Warehouse User.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_user_id`

(required) Unique Operations Insights Warehouse User identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPSI_CONFIGURATION Function

Gets details of an OPSI configuration resource. Values specified in configItemField and configItemCustomStatus query params will be considered, only if configItems field is requested as part of opsiConfigField query param. Values specified in configItemCustomStatus will determine whether only customized configuration items or only non-customized configuration items or both have to be returned.

Syntax
```

```

Parameters

Parameter Description

`opsi_configuration_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of OPSI configuration resource.

`opsi_config_field`

(optional) Optional fields to return as part of OpsiConfiguration object. Unless requested, these fields will not be returned by default.

Allowed values are: 'configItems'

`config_item_custom_status`

(optional) Specifies whether only customized configuration items or only non-customized configuration items or both have to be returned. By default only customized configuration items are returned.

Allowed values are: 'customized', 'nonCustomized'

`config_items_applicable_context`

(optional) Returns the configuration items filtered by applicable contexts sent in this param. By default configuration items of all applicable contexts are returned.

`config_item_field`

(optional) Specifies the fields to return in a config item summary.

Allowed values are: 'name', 'value', 'defaultValue', 'metadata', 'applicableContexts'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPSI_DATA_OBJECT Function

Gets details of an OPSI data object.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opsi_data_object_identifier`

(required) Unique OPSI data object identifier.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### HEAD_AWR_HUB_OBJECT Function

Gets the Awr Hub object's user-defined metadata and entity tag (ETag).

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`object_name`

(required) Unique Awr Hub Object identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_ADDM_REPORTS Function

This endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`ingest_addm_reports_details`

(required) Collection of addm reports for a particular database.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_DATABASE_CONFIGURATION Function

This is a generic ingest endpoint for all database configuration metrics.

Syntax
```

```

Parameters

Parameter Description

`ingest_database_configuration_details`

(required) Payload for one or more database configuration metrics for a particular database.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_HOST_CONFIGURATION Function

This is a generic ingest endpoint for all the host configuration metrics

Syntax
```

```

Parameters

Parameter Description

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`ingest_host_configuration_details`

(required) Payload for one or more host configuration metrics for a particular host.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_HOST_METRICS Function

This is a generic ingest endpoint for all the host performance metrics

Syntax
```

```

Parameters

Parameter Description

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`ingest_host_metrics_details`

(required) Payload for one or more host performance metrics for a particular host.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_SQL_BUCKET Function

The sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`ingest_sql_bucket_details`

(required) Collection of SQL bucket objects for a particular database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_SQL_PLAN_LINES Function

The SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`ingest_sql_plan_lines_details`

(required) Collection of SQL plan line objects for a particular database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_SQL_STATS Function

The SQL Stats endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`ingest_sql_stats_details`

(required) Collection of SQL stats objects for a particular database.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INGEST_SQL_TEXT Function

The SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified. Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.

Syntax
```

```

Parameters

Parameter Description

`ingest_sql_text_details`

(required) Collection of SQL text objects for a particular database.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDM_DB_FINDING_CATEGORIES Function

Gets list of ADDM finding categories.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the finding categories

Allowed values are: 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDM_DB_FINDINGS_TIME_SERIES Function

Get the ADDM findings time series for the specified databases for a given time period.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`category_name`

(optional) Optional value filter to match the finding category exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the ADDM finding time series summary data

Allowed values are: 'timestamp'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDM_DB_PARAMETER_CATEGORIES Function

Gets list of ADDM database parameter categories for the specified databases.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the database parameter categories

Allowed values are: 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDM_DB_RECOMMENDATION_CATEGORIES Function

Gets list of ADDM recommendation categories for the specified databases.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the recommendation categories

Allowed values are: 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDM_DB_RECOMMENDATIONS_TIME_SERIES Function

Gets time series data for ADDM recommendations for the specified databases.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`category_name`

(optional) Optional value filter to match the finding category exactly.

`sql_identifier`

(optional) Optional filter to return only resources whose sql id matches the value given. Only considered when categoryName is SQL_TUNING.

`owner_or_name_contains`

(optional) Optional filter to return only resources whose owner or name contains the substring given. The match is not case sensitive. Only considered when categoryName is SCHEMA_OBJECT.

`name_contains`

(optional) Optional filter to return only resources whose name contains the substring given. The match is not case sensitive. Only considered when categoryName is DATABASE_CONFIGURATION.

`name`

(optional) Optional filter to return only resources whose name exactly matches the substring given. The match is case sensitive. Only considered when categoryName is DATABASE_CONFIGURATION.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the ADDM recommendation time series summary data

Allowed values are: 'timestamp'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ADDM_DBS Function

Gets a list of ADDM database information

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting ADDM database data

Allowed values are: 'databaseName', 'numberOfFindings'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_DATABASE_SNAPSHOTS Function

Lists AWR snapshots for the specified database in the AWR.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR snapshot summary data.

Allowed values are: 'TIME_BEGIN', 'SNAPSHOT_ID'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_DATABASES Function

Gets the list of databases and their snapshot summary details available in the AWRHub.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`name`

(optional) The optional single value query parameter to filter the entity name.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR summary data.

Allowed values are: 'END_INTERVAL_TIME', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_HUB_OBJECTS Function

Gets a list of Awr Hub objects. Awr Hub id needs to specified.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`prefix`

(optional) The string to use for matching against the start of object names in a Awr Hub list objects query.

`l_start`

(optional) Object names returned by Awr Hub list objects query must be greater or equal to this parameter.

`l_end`

(optional) Object names returned by Awr Hub list objects query must be strictly less than this parameter.

`delimiter`

(optional) When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the Awr Hub list objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.

`start_after`

(optional) Awr Hub Object name after which remaining objects are listed

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`fields`

(optional) By default all the fields are returned. Use this parameter to fetch specific fields 'size', 'etag', 'md5', 'timeCreated', 'timeModified', 'storageTier' and 'archivalState' fields. List the names of those fields in a comma-separated, case-insensitive list as the value of this parameter. For example: 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'.

Allowed values are: 'name', 'size', 'etag', 'timeCreated', 'md5', 'archivalState', 'timeModified', 'storageTier'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_HUB_SOURCES Function

Gets a list of Awr Hub source objects.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`awr_hub_source_id`

(optional) Awr Hub source identifier

`source_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW_S', 'ATP_S', 'ADW_D', 'ATP_D', 'EXTERNAL_PDB', 'EXTERNAL_NONCDB', 'COMANAGED_VM_CDB', 'COMANAGED_VM_PDB', 'COMANAGED_VM_NONCDB', 'COMANAGED_BM_CDB', 'COMANAGED_BM_PDB', 'COMANAGED_BM_NONCDB', 'COMANAGED_EXACS_CDB', 'COMANAGED_EXACS_PDB', 'COMANAGED_EXACS_NONCDB', 'UNDEFINED'

`name`

(optional) Awr Hub source database name

`status`

(optional) Resource Status

Allowed values are: 'ACCEPTING', 'NOT_ACCEPTING', 'NOT_REGISTERED', 'TERMINATED'

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_HUBS Function

Gets a list of AWR hubs. Either compartmentId or id must be specified. All these resources are expected to be in root compartment.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to return only resources that match the entire display name.

`id`

(optional) Unique Awr Hub identifier

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AWR_SNAPSHOTS Function

Lists AWR snapshots for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should not exceed an elapsed range of 1 day. The timeGreaterThanOrEqualTo &amp; timeLessThanOrEqualTo params are optional. If these params are not provided, by default last 1 day snapshots will be returned.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) AWR source database identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The option to sort the AWR snapshot summary data. Default sort is by timeBegin.

Allowed values are: 'timeBegin', 'snapshotId'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_CONFIGURATIONS Function

Gets a list of database insight configurations based on the query parameters specified. Either compartmentId or databaseInsightId query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of database insight configurations in that compartment and in all sub-compartments will be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`enterprise_manager_bridge_id`

(optional) Unique Enterprise Manager bridge identifier

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Database configuration list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

Allowed values are: 'databaseName', 'databaseDisplayName', 'databaseType'

`host_name`

(optional) Filter by one or more hostname.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_INSIGHTS Function

Gets a list of database insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of database insights in that compartment and in all sub-compartments will be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`enterprise_manager_bridge_id`

(optional) Unique Enterprise Manager bridge identifier

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`status`

(optional) Resource Status

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`fields`

(optional) Specifies the fields to return in a database summary response. By default all fields are returned if omitted.

Allowed values are: 'compartmentId', 'databaseName', 'databaseDisplayName', 'databaseType', 'databaseVersion', 'databaseHostNames', 'freeformTags', 'definedTags'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

Allowed values are: 'databaseName', 'databaseDisplayName', 'databaseType'

`exadata_insight_id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`opsi_private_endpoint_id`

(optional) Unique Operations Insights PrivateEndpoint identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ENTERPRISE_MANAGER_BRIDGES Function

Gets a list of Operations Insights Enterprise Manager bridges. Either compartmentId or id must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of bridges in that compartment and in all sub-compartments will be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to return only resources that match the entire display name.

`id`

(optional) Unique Enterprise Manager bridge identifier

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXADATA_CONFIGURATIONS Function

Gets a list of exadata insight configurations. Either compartmentId or exadataInsightsId query parameter must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Exadata configuration list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

Allowed values are: 'exadataName', 'exadataDisplayName', 'exadataType'

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXADATA_INSIGHTS Function

Gets a list of Exadata insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of Exadata insights in that compartment and in all sub-compartments will be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`enterprise_manager_bridge_id`

(optional) Unique Enterprise Manager bridge identifier

`id`

(optional) Optional list of Exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`status`

(optional) Resource Status

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Exadata insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified. Default order for timeCreated is descending. Default order for exadataName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'exadataName'

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HOST_CONFIGURATIONS Function

Gets a list of host insight configurations based on the query parameters specified. Either compartmentId or hostInsightId query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of host insight configurations in that compartment and in all sub-compartments will be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`enterprise_manager_bridge_id`

(optional) Unique Enterprise Manager bridge identifier

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Host configuration list sort options.

Allowed values are: 'hostName', 'platformType'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HOST_INSIGHTS Function

Gets a list of host insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of host insights in that compartment and in all sub-compartments will be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`status`

(optional) Resource Status

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Host insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

Allowed values are: 'hostName', 'hostType'

`enterprise_manager_bridge_id`

(optional) Unique Enterprise Manager bridge identifier

`exadata_insight_id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HOSTED_ENTITIES Function

Get a list of hosted entities details.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`exadata_insight_id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Hosted entity list sort options.

Allowed values are: 'entityName', 'entityType'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMPORTABLE_AGENT_ENTITIES Function

Gets a list of agent entities available to add a new hostInsight. An agent entity is \"available\" and will be shown if all the following conditions are true: 1. The agent OCID is not already being used for an existing hostInsight. 2. The agent availabilityStatus = 'ACTIVE' 3. The agent lifecycleState = 'ACTIVE'

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Hosted entity list sort options.

Allowed values are: 'entityName', 'entityType'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMPORTABLE_COMPUTE_ENTITIES Function

Gets a list of available compute intances running cloud agent to add a new hostInsight. An Compute entity is \"available\" and will be shown if all the following conditions are true: 1. Compute is running OCA 2. OCI Management Agent is not enabled or If OCI Management Agent is enabled 2.1 The agent OCID is not already being used for an existing hostInsight. 2.2 The agent availabilityStatus = 'ACTIVE' 2.3 The agent lifecycleState = 'ACTIVE'

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Compute entity list sort options.

Allowed values are: 'computeId', 'computeDisplayName', 'platformType', 'hostName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMPORTABLE_ENTERPRISE_MANAGER_ENTITIES Function

Gets a list of importable entities for an Operations Insights Enterprise Manager bridge that have not been imported before.

Syntax
```

```

Parameters

Parameter Description

`enterprise_manager_bridge_id`

(required) Unique Enterprise Manager bridge identifier

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`enterprise_manager_entity_type`

(optional) Filter by one or more Enterprise Manager entity types. Currently, the supported types are \"oracle_pdb\", \"oracle_database\", \"host\", \"oracle_dbmachine\", \"oracle_exa_cloud_service\", and \"oracle_oci_exadata_cloud_service\". If this parameter is not specified, targets of all supported entity types are returned by default.

`enterprise_manager_identifier`

(optional) Used in combination with enterpriseManagerParentEntityIdentifier to return the members of a particular Enterprise Manager parent entity. Both enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular Enterprise Manager parent entity.

`enterprise_manager_parent_entity_identifier`

(optional) Used in combination with enterpriseManagerIdentifier to return the members of a particular Enterprise Manager parent entity. Both enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular Enterprise Manager parent entity.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NEWS_REPORTS Function

Gets a list of news reports based on the query parameters specified. Either compartmentId or id query parameter must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`news_report_id`

(optional) Unique Operations Insights news report identifier

`status`

(optional) Resource Status

Allowed values are: 'DISABLED', 'ENABLED', 'TERMINATED'

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) News report list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

Allowed values are: 'name', 'newsFrequency'

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINTS Function

Gets a list of Operation Insights private endpoints.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to return only resources that match the entire display name.

`opsi_private_endpoint_id`

(optional) Unique Operations Insights PrivateEndpoint identifier

`is_used_for_rac_dbs`

(optional) The option to filter OPSI private endpoints that can used for RAC. Should be used along with vcnId query parameter.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort private endpoints.

Allowed values are: 'timeCreated', 'id', 'displayName'

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPERATIONS_INSIGHTS_WAREHOUSE_USERS Function

Gets a list of Operations Insights Warehouse users. Either compartmentId or id must be specified. All these resources are expected to be in root compartment.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to return only resources that match the entire display name.

`id`

(optional) Unique Operations Insights Warehouse User identifier

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPERATIONS_INSIGHTS_WAREHOUSES Function

Gets a list of Operations Insights warehouses. Either compartmentId or id must be specified. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to return only resources that match the entire display name.

`id`

(optional) Unique Operations Insights Warehouse identifier

`lifecycle_state`

(optional) Lifecycle states

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPSI_CONFIGURATIONS Function

Gets a list of OPSI configuration resources based on the query parameters specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) Filter to return based on resources that match the entire display name.

`lifecycle_state`

(optional) Filter to return based on Lifecycle state of OPSI configuration.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`opsi_config_type`

(optional) Filter to return based on configuration type of OPSI configuration.

Allowed values are: 'UX_CONFIGURATION'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) OPSI configurations list sort options.

Allowed values are: 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPSI_DATA_OBJECTS Function

Gets a list of OPSI data objects based on the query parameters specified. CompartmentId id query parameter must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`data_object_type`

(optional) OPSI data object types.

Allowed values are: 'DATABASE_INSIGHTS_DATA_OBJECT', 'HOST_INSIGHTS_DATA_OBJECT', 'EXADATA_INSIGHTS_DATA_OBJECT'

`display_name`

(optional) A filter to return only resources that match the entire display name.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) OPSI data object list sort options.

Allowed values are: 'displayName', 'dataObjectType', 'name'

`group_name`

(optional) A filter to return only data objects that belongs to the group of the given group name. By default, no filtering will be applied on group name.

`name`

(optional) A filter to return only data objects that match the entire data object name. By default, no filtering will be applied on data object name.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_PLANS Function

Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single plan. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`

`plan_hash`

(required) Unique plan hash for a SQL Plan of a particular SQL Statement. Example: `9820154385`

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_SEARCHES Function

Search SQL by SQL Identifier across databases in a compartment and in all sub-compartments if specified. And get the SQL Text and the details of the databases executing the SQL for a given time period.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_TEXTS Function

Query SQL Warehouse to get the full SQL Text for a SQL in a compartment and in all sub-compartments if specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the assosicated DBaaS entity.

`id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WAREHOUSE_DATA_OBJECTS Function

Gets a list of Warehouse data objects (e.g: views, tables), based on the query parameters specified.

Syntax
```

```

Parameters

Parameter Description

`warehouse_type`

(required) Type of the Warehouse.

Allowed values are: 'awrHubs'

`warehouse_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Warehouse.

`data_object_type`

(optional) A filter to return only data objects that match the data object type. By default, no filtering will be applied on data object type.

Allowed values are: 'VIEW', 'TABLE'

`name`

(optional) A filter to return only data objects that match the entire data object name. By default, no filtering will be applied on data object name.

`owner`

(optional) A filter to return only data objects that match the entire data object owner name. By default, no filtering will be applied on data object owner name.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort options for Warehouse data objects list.

Allowed values are: 'dataObjectType', 'name', 'owner'

`summary_field`

(optional) Specifies the optional fields to return in a WarehouseDataObjectSummary. Unless requested, these fields are not returned by default.

Allowed values are: 'details'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment. Either compartmentId or id must be specified. Only one of id, resourceId or relatedResourceId can be specified optionally.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(optional) The ID of the asynchronous work request.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`related_resource_id`

(optional) The ID of the related resource for the resource affected by the work request, e.g. the related Exadata Insight OCID of the Database Insight work request

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_AWR_HUB_OBJECT Function

Creates a new object or overwrites an existing object with the same name to the Awr Hub.

Syntax
```

```

Parameters

Parameter Description

`put_awr_hub_object_body`

(required) The object to be uploaded to the Awr Hub.

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`object_name`

(required) Unique Awr Hub Object identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### QUERY_OPSI_DATA_OBJECT_DATA Function

Queries an OPSI data object with the inputs provided and sends the result set back. Either analysisTimeInterval or timeIntervalStart and timeIntervalEnd parameters need to be passed as well.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`query_opsi_data_object_data_details`

(required) The information to be used for querying an OPSI data object.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### QUERY_WAREHOUSE_DATA_OBJECT_DATA Function

Queries Warehouse data objects (e.g: views, tables) with the inputs provided and sends the result set back. Any data to which an OperationsInsightsWarehouseUser with a permission to the corresponding Warehouse can be queried.

Syntax
```

```

Parameters

Parameter Description

`warehouse_type`

(required) Type of the Warehouse.

Allowed values are: 'awrHubs'

`warehouse_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Warehouse.

`query_warehouse_data_object_data_details`

(required) The information to be used for querying a Warehouse.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_OPERATIONS_INSIGHTS_WAREHOUSE_WALLET Function

Rotate the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ADDM_DB_FINDINGS Function

Summarizes ADDM findings for the specified databases.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`category_name`

(optional) Optional value filter to match the finding category exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the ADDM finding summary data

Allowed values are: 'impactOverallPercent', 'impactMaxPercent', 'impactAvgActiveSessions', 'frequencyCount'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ADDM_DB_PARAMETER_CHANGES Function

Summarizes the AWR database parameter change history for the specified parameter. There will be one element for each time that parameter changed during the specified time period. This API is limited to only one parameter per request.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(required) Required filter to return only changes for the specified parameter. The match is case sensitive.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`value_contains`

(optional) Optional filter to return only resources whose value contains the substring given. The match is not case sensitive.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the database parameter change data

Allowed values are: 'isChanged', 'beginSnapId'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ADDM_DB_PARAMETERS Function

Summarizes database parameter history information for the specified databases. Return a list of parameters with information on whether the parameter values were changed or not within the specified time period. The response does not include the individual parameter changes within the time period.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`category_name`

(optional) Optional value filter to match the parameter category exactly. Note the list of possible category names can be retrieved from the following endpoint: /databases/{databaseId}/addmDbParameterCategories.

`name_or_value_contains`

(optional) Optional filter to return only resources whose name or value contains the substring given. The match is not case sensitive.

`is_changed`

(optional) Optional filter to return only parameters whose value changed in the specified time period. Valid values include: TRUE, FALSE

Allowed values are: 'true', 'false'

`is_default`

(optional) Optional filter to return only parameters whose end value was set to the default value (TRUE) or was specified in the parameter file (FALSE). Valid values include: TRUE, FALSE

Allowed values are: 'true', 'false'

`has_recommendations`

(optional) Optional filter to return only parameters which have recommendations in the specified time period. Valid values include: TRUE, FALSE

Allowed values are: 'true', 'false'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the database parameter data

Allowed values are: 'isChanged', 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ADDM_DB_RECOMMENDATIONS Function

Summarizes ADDM recommendations for the specified databases.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`category_name`

(optional) Optional value filter to match the finding category exactly.

`finding_identifier`

(optional) Unique finding ID

`sql_identifier`

(optional) Optional filter to return only resources whose sql id matches the value given. Only considered when categoryName is SQL_TUNING.

`owner_or_name_contains`

(optional) Optional filter to return only resources whose owner or name contains the substring given. The match is not case sensitive. Only considered when categoryName is SCHEMA_OBJECT.

`name_contains`

(optional) Optional filter to return only resources whose name contains the substring given. The match is not case sensitive. Only considered when categoryName is DATABASE_CONFIGURATION.

`name`

(optional) Optional filter to return only resources whose name exactly matches the substring given. The match is case sensitive. Only considered when categoryName is DATABASE_CONFIGURATION.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Field name for sorting the recommendation data

Allowed values are: 'maxBenefitPercent', 'maxBenefitAvgActiveSessions', 'frequencyCount'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ADDM_DB_SCHEMA_OBJECTS Function

Summarizes Schema objects for the specified databases for the specified objectIdentifiers

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`object_identifier`

(required) One or more unique Object id (from RDBMS)

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_ADDM_DB_SQL_STATEMENTS Function

Summarizes SQL Statements for the specified databases for the specified sqlIdentifiers

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_CPU_USAGES Function

Summarizes the AWR CPU resource limits and metrics for the specified database in AWR. Based on the time range provided as part of query param, the metrics points will be returned in the response as below. - if time range is &lt;=7 days then the metrics points will be for every MINUTES - if time range is &lt;=2 hours then the metrics points will be for every 10 SECONDS - if time range is &gt;7 days then the metrics points will be for every HOUR.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`session_type`

(optional) The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

Allowed values are: 'FOREGROUND', 'BACKGROUND', 'ALL'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR CPU usage summary data.

Allowed values are: 'TIME_SAMPLED', 'AVG_VALUE'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_METRICS Function

Summarizes the metric samples for the specified database in the AWR. The metric samples are summarized based on the Time dimension for each metric.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`name`

(required) The required multiple value query parameter to filter the entity name.

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR time series summary data.

Allowed values are: 'TIMESTAMP', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_PARAMETER_CHANGES Function

Summarizes the database parameter change history for one database parameter of the specified database in AWR. One change history record contains the previous value, the changed value, and the corresponding time range. If the database parameter value was changed multiple times within the time range, then multiple change history records are created for the same parameter. Note that this API only returns information on change history details for one database parameter. To get a list of all the database parameters whose values were changed during a specified time range, use the following API endpoint: /awrHubs/{awrHubId}/awrDbParameters?awrSourceDatabaseIdentifier={awrSourceDbId}

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`name`

(required) The required single value query parameter to filter the entity name.

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR database parameter change history data.

Allowed values are: 'IS_CHANGED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_PARAMETERS Function

Summarizes the database parameter history for the specified database in AWR. This includes the list of database parameters, with information on whether the parameter values were modified within the query time range. Note that each database parameter is only listed once. Depending on the optional query parameters, the returned summary gets all the database parameters, which include: Queryparam (valueChanged =\"Y\") - Each parameter whose value was changed during the time range, \"isChanged : true\" in response for the DB params. Queryparam (valueChanged =\"N\") - Each parameter whose value was unchanged during the time range, \"isChanged : false\" in response for the DB params. Queryparam (valueChanged =\"Y\" and valueModified = \"SYSTEM_MOD\") - Each parameter whose value was changed at the system level during the time range, \"isChanged : true\" &amp; \"valueModified : SYSTEM_MOD\" in response for the DB params. Queryparam (valueChanged =\"N\" and valueDefault = \"FALSE\") - Each parameter whose value was unchanged during the time range, however, the value is not the default value, \"isChanged : true\" &amp; \"isDefault : false\" in response for the DB params. Note that this API does not return information on the number of times each database parameter has been changed within the time range. To get the database parameter value change history for a specific parameter, use the following API endpoint: /awrHubs/{awrHubId}/awrDbParameterChanges?awrSourceDatabaseIdentifier={awrSourceDbId}

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

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

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR database parameter change history data.

Allowed values are: 'IS_CHANGED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_SNAPSHOT_RANGES Function

Summarizes the AWR snapshot ranges that contain continuous snapshots, for the specified AWRHub.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`name`

(optional) The optional single value query parameter to filter the entity name.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the AWR summary data.

Allowed values are: 'END_INTERVAL_TIME', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_SYSSTATS Function

Summarizes the AWR SYSSTAT sample data for the specified database in AWR. The statistical data is summarized based on the Time dimension for each statistic.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`name`

(required) The required multiple value query parameter to filter the entity name.

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the data within a time period.

Allowed values are: 'TIME_BEGIN', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_TOP_WAIT_EVENTS Function

Summarizes the AWR top wait events.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`session_type`

(optional) The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

Allowed values are: 'FOREGROUND', 'BACKGROUND', 'ALL'

`top_n`

(optional) The optional query parameter to filter the number of top categories to be returned.

`sort_by`

(optional) The option to sort the AWR top event summary data.

Allowed values are: 'WAITS_PERSEC', 'AVG_WAIT_TIME_PERSEC'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_WAIT_EVENT_BUCKETS Function

Summarizes AWR wait event data into value buckets and frequency, for the specified database in the AWR.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`name`

(required) The required single value query parameter to filter the entity name.

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`num_bucket`

(optional) The number of buckets within the histogram.

`min_value`

(optional) The minimum value of the histogram.

`max_value`

(optional) The maximum value of the histogram.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort distribution data.

Allowed values are: 'CATEGORY', 'PERCENTAGE'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_DATABASE_WAIT_EVENTS Function

Summarizes the AWR wait event sample data for the specified database in the AWR. The event data is summarized based on the Time dimension for each event.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`awr_source_database_identifier`

(required) The internal ID of the database. The internal ID of the database is not the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). It can be retrieved from the following endpoint: /awrHubs/{awrHubId}/awrDatabases

`instance_number`

(optional) The optional single value query parameter to filter by database instance number.

`begin_snapshot_identifier_greater_than_or_equal_to`

(optional) The optional greater than or equal to filter on the snapshot ID.

`end_snapshot_identifier_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the snapshot Identifier.

`time_greater_than_or_equal_to`

(optional) The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`time_less_than_or_equal_to`

(optional) The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

`name`

(optional) The optional multiple value query parameter to filter the entity name.

`session_type`

(optional) The optional query parameter to filter ASH activities by FOREGROUND or BACKGROUND.

Allowed values are: 'FOREGROUND', 'BACKGROUND', 'ALL'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_by`

(optional) The option to sort the data within a time period.

Allowed values are: 'TIME_BEGIN', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_AWR_SOURCES_SUMMARIES Function

Gets a list of summary of AWR Sources.

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`name`

(optional) Name for an Awr source database

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The order in which Awr sources summary records are listed

Allowed values are: 'snapshotsUploaded', 'name'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_CONFIGURATION_ITEMS Function

Gets the applicable configuration items based on the query parameters specified. Configuration items for an opsiConfigType with respect to a compartmentId can be fetched. Values specified in configItemField param will determine what fields for each configuration items have to be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opsi_config_type`

(optional) Filter to return configuration items based on configuration type of OPSI configuration.

Allowed values are: 'UX_CONFIGURATION'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`config_items_applicable_context`

(optional) Returns the configuration items filtered by applicable contexts sent in this param. By default configuration items of all applicable contexts are returned.

`config_item_field`

(optional) Specifies the fields to return in a config item summary.

Allowed values are: 'name', 'value', 'defaultValue', 'valueSourceConfig', 'metadata', 'applicableContexts'

`name`

(optional) A filter to return only configuration items that match the entire name.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_RESOURCE_CAPACITY_TREND Function

Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`utilization_level`

(optional) Filter by utilization level by the following buckets: - HIGH_UTILIZATION: DBs with utilization greater or equal than 75. - LOW_UTILIZATION: DBs with utilization lower than 25. - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75. - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

Allowed values are: 'HIGH_UTILIZATION', 'LOW_UTILIZATION', 'MEDIUM_HIGH_UTILIZATION', 'MEDIUM_LOW_UTILIZATION'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sorts using end timestamp , capacity or baseCapacity

Allowed values are: 'endTimestamp', 'capacity', 'baseCapacity'

`tablespace_name`

(optional) Tablespace name for a database

`host_name`

(optional) Filter by one or more hostname.

`is_database_instance_level_metrics`

(optional) Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_RESOURCE_FORECAST_TREND Function

Get Forecast predictions for CPU and Storage resources since a time in the past. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`forecast_model`

(optional) Choose algorithm model for the forecasting. Possible values: - LINEAR: Uses linear regression algorithm for forecasting. - ML_AUTO: Automatically detects best algorithm to use for forecasting. - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

Allowed values are: 'LINEAR', 'ML_AUTO', 'ML_NO_AUTO'

`utilization_level`

(optional) Filter by utilization level by the following buckets: - HIGH_UTILIZATION: DBs with utilization greater or equal than 75. - LOW_UTILIZATION: DBs with utilization lower than 25. - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75. - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

Allowed values are: 'HIGH_UTILIZATION', 'LOW_UTILIZATION', 'MEDIUM_HIGH_UTILIZATION', 'MEDIUM_LOW_UTILIZATION'

`confidence`

(optional) This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`host_name`

(optional) Filter by one or more hostname.

`tablespace_name`

(optional) Tablespace name for a database

`is_database_instance_level_metrics`

(optional) Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_RESOURCE_STATISTICS Function

Lists the Resource statistics (usage,capacity, usage change percent, utilization percent, base capacity, isAutoScalingEnabled) for each database filtered by utilization level in a compartment and in all sub-compartments if specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`insight_by`

(optional) Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which resource statistics records are listed

Allowed values are: 'utilizationPercent', 'usage', 'usageChangePercent', 'databaseName', 'databaseType'

`host_name`

(optional) Filter by one or more hostname.

`is_database_instance_level_metrics`

(optional) Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE Function

A cumulative distribution function is used to rank the usage data points per database within the specified time period. For each database, the minimum data point with a ranking &gt; the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_name`

(optional) Filter by one or more hostname.

`is_database_instance_level_metrics`

(optional) Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`cdb_name`

(optional) Filter by one or more cdb name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE_TREND Function

Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sorts using end timestamp, usage or capacity

Allowed values are: 'endTimestamp', 'usage', 'capacity'

`host_name`

(optional) Filter by one or more hostname.

`is_database_instance_level_metrics`

(optional) Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`cdb_name`

(optional) Filter by one or more cdb name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_RESOURCE_UTILIZATION_INSIGHT Function

Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`host_name`

(optional) Filter by one or more hostname.

`is_database_instance_level_metrics`

(optional) Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`cdb_name`

(optional) Filter by one or more cdb name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_DATABASE_INSIGHT_TABLESPACE_USAGE_TREND Function

Returns response with usage time series data (endTimestamp, usage, capacity) with breakdown by tablespaceName for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND Function

Returns response with time series data (endTimestamp, capacity) for the time period specified for an exadata system for a resource metric. Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters. Top five resources are returned if total exceeds the limit specified. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId, cdbName and hostName query parameter applies to ResourceType DATABASE. Valid values for ResourceType HOST are CPU and MEMORY. HostName is returned in name field. HostInsightId and hostName query parameter applies to ResourceType HOST. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and THROUGHPUT and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER. Valid values for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field.

Syntax
```

```

Parameters

Parameter Description

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`exadata_insight_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_insight_id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_insight_id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`storage_server_name`

(optional) Optional storage server name on an exadata system.

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which resource capacity trend records are listed

Allowed values are: 'id', 'name'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATED Function

Returns response with time series data (endTimestamp, capacity) for the time period specified for an exadata system or fleet aggregation for a resource metric. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.

Syntax
```

```

Parameters

Parameter Description

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sorts using end timestamp or capacity.

Allowed values are: 'endTimestamp', 'capacity'

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND Function

Get historical usage and forecast predictions for an exadata system with breakdown by databases, hosts or storage servers. Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters. Top five resources are returned if total exceeds the limit specified. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId , cdbName and hostName query parameter applies to ResourceType DATABASE. Valid values for ResourceType HOST are CPU and MEMORY. HostName s returned in name field. HostInsightId and hostName query parameter applies to ResourceType HOST. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and THROUGHPUT and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER. Valid value for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field.

Syntax
```

```

Parameters

Parameter Description

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`exadata_insight_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`database_insight_id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`host_insight_id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`storage_server_name`

(optional) Optional storage server name on an exadata system.

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`forecast_start_day`

(optional) Number of days used for utilization forecast analysis.

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`forecast_model`

(optional) Choose algorithm model for the forecasting. Possible values: - LINEAR: Uses linear regression algorithm for forecasting. - ML_AUTO: Automatically detects best algorithm to use for forecasting. - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

Allowed values are: 'LINEAR', 'ML_AUTO', 'ML_NO_AUTO'

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`confidence`

(optional) This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which resource Forecast trend records are listed

Allowed values are: 'id', 'name', 'daysToReachCapacity'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATED Function

Get aggregated historical usage and forecast predictions for resources. Either compartmentId or exadataInsightsId query parameter must be specified. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.

Syntax
```

```

Parameters

Parameter Description

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`forecast_start_day`

(optional) Number of days used for utilization forecast analysis.

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`forecast_model`

(optional) Choose algorithm model for the forecasting. Possible values: - LINEAR: Uses linear regression algorithm for forecasting. - ML_AUTO: Automatically detects best algorithm to use for forecasting. - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

Allowed values are: 'LINEAR', 'ML_AUTO', 'ML_NO_AUTO'

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`confidence`

(optional) This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_STATISTICS Function

Lists the Resource statistics (usage, capacity, usage change percent, utilization percent) for each resource based on resourceMetric filtered by utilization level. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS, THROUGHPUT. Valid value for ResourceType DISKGROUP is STORAGE.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which resource statistics records are listed

Allowed values are: 'utilizationPercent', 'usage', 'usageChangePercent'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE Function

A cumulative distribution function is used to rank the usage data points per resource within the specified time period. For each resource, the minimum data point with a ranking &gt; the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which resource usage summary records are listed

Allowed values are: 'utilizationPercent', 'usage', 'capacity', 'usageChangePercent'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE_AGGREGATED Function

A cumulative distribution function is used to rank the usage data points per database within the specified time period. For each database, the minimum data point with a ranking &gt; the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_INSIGHT_RESOURCE_UTILIZATION_INSIGHT Function

Gets current utilization, projected utilization and days to reach projectedUtilization for an exadata system over specified time period. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_type`

(required) Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE

`resource_metric`

(required) Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`forecast_start_day`

(optional) Number of days used for utilization forecast analysis.

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by hostname.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_EXADATA_MEMBERS Function

Lists the software and hardware inventory of the Exadata System.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of exadata insight resource.

`exadata_type`

(optional) Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which exadata member records are listed

Allowed values are: 'name', 'displayName', 'entityType'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_DISK_STATISTICS Function

Returns response with disk(s) statistics for a host.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_HOST_RECOMMENDATION Function

Returns response with some recommendations if apply for a host.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_NETWORK_USAGE_TREND Function

Returns response with usage time series data with breakdown by network interface for the time period specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_RESOURCE_CAPACITY_TREND Function

Returns response with time series data (endTimestamp, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`utilization_level`

(optional) Filter by utilization level by the following buckets: - HIGH_UTILIZATION: DBs with utilization greater or equal than 75. - LOW_UTILIZATION: DBs with utilization lower than 25. - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75. - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

Allowed values are: 'HIGH_UTILIZATION', 'LOW_UTILIZATION', 'MEDIUM_HIGH_UTILIZATION', 'MEDIUM_LOW_UTILIZATION'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sorts using end timestamp or capacity

Allowed values are: 'endTimestamp', 'capacity'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_RESOURCE_FORECAST_TREND Function

Get Forecast predictions for CPU or memory resources since a time in the past. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`forecast_model`

(optional) Choose algorithm model for the forecasting. Possible values: - LINEAR: Uses linear regression algorithm for forecasting. - ML_AUTO: Automatically detects best algorithm to use for forecasting. - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

Allowed values are: 'LINEAR', 'ML_AUTO', 'ML_NO_AUTO'

`utilization_level`

(optional) Filter by utilization level by the following buckets: - HIGH_UTILIZATION: DBs with utilization greater or equal than 75. - LOW_UTILIZATION: DBs with utilization lower than 25. - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75. - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

Allowed values are: 'HIGH_UTILIZATION', 'LOW_UTILIZATION', 'MEDIUM_HIGH_UTILIZATION', 'MEDIUM_LOW_UTILIZATION'

`confidence`

(optional) This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`mount_point`

(optional) Mount points are specialized NTFS filesystem objects.

`interface_name`

(optional) Name of the network interface.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_RESOURCE_STATISTICS Function

Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered by utilization level in a compartment and in all sub-compartments if specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`insight_by`

(optional) Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The order in which resource statistics records are listed.

Allowed values are: 'utilizationPercent', 'usage', 'usageChangePercent', 'hostName', 'platformType'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE Function

A cumulative distribution function is used to rank the usage data points per host within the specified time period. For each host, the minimum data point with a ranking &gt; the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`percentile`

(optional) Percentile values of daily usage to be used for computing the aggregate resource usage.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE_TREND Function

Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sorts using end timestamp, usage or capacity

Allowed values are: 'endTimestamp', 'usage', 'capacity'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_RESOURCE_UTILIZATION_INSIGHT Function

Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_metric`

(required) Filter by host resource metric. Supported values are CPU, MEMORY, LOGICAL_MEMORY, STORAGE and NETWORK.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`platform_type`

(optional) Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX, SOLARIS, WINDOWS]. Supported platformType(s) for MACS-managed cloud host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX, WINDOWS, AIX, HP-UX].

Allowed values are: 'LINUX', 'SOLARIS', 'SUNOS', 'ZLINUX', 'WINDOWS', 'AIX', 'HP_UX'

`id`

(optional) Optional list of host insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`forecast_days`

(optional) Number of days used for utilization forecast analysis.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`high_utilization_threshold`

(optional) Percent value in which a resource metric is considered highly utilized.

`low_utilization_threshold`

(optional) Percent value in which a resource metric is considered low utilized.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_STORAGE_USAGE_TREND Function

Returns response with usage time series data with breakdown by filesystem for the time period specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_TOP_PROCESSES_USAGE Function

Returns response with aggregated data (timestamp, usageData) for top processes on a specific date. Data is aggregated for the time specified and processes are sorted descendent by the process metric specified (CPU, MEMORY, VIRTUAL_MEMORY). hostInsightId, processMetric must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`resource_metric`

(required) Host top processes resource metric sort options. Supported values are CPU, MEMORY, VIIRTUAL_MEMORY.

`l_timestamp`

(required) Timestamp at which to gather the top processes. This will be top processes over the hour or over the day pending the time range passed into the query.

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_HOST_INSIGHT_TOP_PROCESSES_USAGE_TREND Function

Returns response with aggregated time series data (timeIntervalstart, timeIntervalEnd, commandArgs, usageData) for top processes. Data is aggregated for the time period specified and proceses are sorted descendent by the proces metric specified (CPU, MEMORY, VIRTUAL_MEMORY). HostInsight Id and Process metric must be specified

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`id`

(required) Required[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host insight resource.

`resource_metric`

(required) Host top processes resource metric sort options. Supported values are CPU, MEMORY, VIIRTUAL_MEMORY.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`host_type`

(optional) Filter by one or more host types. Possible values are CLOUD-HOST, EXTERNAL-HOST, COMANAGED-VM-HOST, COMANAGED-BM-HOST, COMANAGED-EXACS-HOST

`host_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host (Compute Id)

`process_hash`

(optional) Unique identifier for a process.

`statistic`

(optional) Choose the type of statistic metric data to be used for forecasting.

Allowed values are: 'AVG', 'MAX'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_OPERATIONS_INSIGHTS_WAREHOUSE_RESOURCE_USAGE Function

Gets the details of resources used by an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_INSIGHTS Function

Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given time period across the given databases or database types in a compartment and in all sub-compartments if specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by one or more hostname.

`database_time_pct_greater_than`

(optional) Filter sqls by percentage of db time.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_PLAN_INSIGHTS Function

Query SQL Warehouse to get the performance insights on the execution plans for a given SQL for a given time period. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_RESPONSE_TIME_DISTRIBUTIONS Function

Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_STATISTICS Function

Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given time period across the given databases or database types in a compartment and in all sub-compartments if specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_type`

(optional) Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

Allowed values are: 'ADW-S', 'ATP-S', 'ADW-D', 'ATP-D', 'EXTERNAL-PDB', 'EXTERNAL-NONCDB', 'COMANAGED-VM-CDB', 'COMANAGED-VM-PDB', 'COMANAGED-VM-NONCDB', 'COMANAGED-BM-CDB', 'COMANAGED-BM-PDB', 'COMANAGED-BM-NONCDB', 'COMANAGED-EXACS-CDB', 'COMANAGED-EXACS-PDB', 'COMANAGED-EXACS-NONCDB'

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by one or more hostname.

`database_time_pct_greater_than`

(optional) Filter sqls by percentage of db time.

`sql_identifier`

(optional) One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to use when sorting SQL statistics. Example: databaseTimeInSec

Allowed values are: 'databaseTimeInSec', 'executionsPerHour', 'executionsCount', 'cpuTimeInSec', 'ioTimeInSec', 'inefficientWaitTimeInSec', 'responseTimeInSec', 'planCount', 'variability', 'averageActiveSessions', 'databaseTimePct', 'inefficiencyInPct', 'changeInCpuTimeInPct', 'changeInIoTimeInPct', 'changeInInefficientWaitTimeInPct', 'changeInResponseTimeInPct', 'changeInAverageActiveSessionsInPct', 'changeInExecutionsPerHourInPct', 'changeInInefficiencyInPct'

`category`

(optional) Filter sqls by one or more performance categories.

Allowed values are: 'DEGRADING', 'VARIANT', 'INEFFICIENT', 'CHANGING_PLANS', 'IMPROVING', 'DEGRADING_VARIANT', 'DEGRADING_INEFFICIENT', 'DEGRADING_CHANGING_PLANS', 'DEGRADING_INCREASING_IO', 'DEGRADING_INCREASING_CPU', 'DEGRADING_INCREASING_INEFFICIENT_WAIT', 'DEGRADING_CHANGING_PLANS_AND_INCREASING_IO', 'DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU', 'DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT', 'VARIANT_INEFFICIENT', 'VARIANT_CHANGING_PLANS', 'VARIANT_INCREASING_IO', 'VARIANT_INCREASING_CPU', 'VARIANT_INCREASING_INEFFICIENT_WAIT', 'VARIANT_CHANGING_PLANS_AND_INCREASING_IO', 'VARIANT_CHANGING_PLANS_AND_INCREASING_CPU', 'VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT', 'INEFFICIENT_CHANGING_PLANS', 'INEFFICIENT_INCREASING_INEFFICIENT_WAIT', 'INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT'

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_STATISTICS_TIME_SERIES Function

Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a given time period in a compartment and in all sub-compartments if specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`

`database_id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional) Optional list of database[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`exadata_insight_id`

(optional) Optional list of exadata insight resource[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cdb_name`

(optional) Filter by one or more cdb name.

`host_name`

(optional) Filter by one or more hostname.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`compartment_id_in_subtree`

(optional) A flag to search all resources within a given compartment and all sub-compartments.

`vmcluster_name`

(optional) Optional list of Exadata Insight VM cluster name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_SQL_STATISTICS_TIME_SERIES_BY_PLAN Function

Query SQL Warehouse to get the performance statistics time series for a given SQL by execution plans for a given time period. Either databaseId or id must be specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`sql_identifier`

(required) Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`

`database_id`

(optional) Optional[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated DBaaS entity.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database insight resource.

`analysis_time_interval`

(optional) Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

`time_interval_start`

(optional) Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.

`time_interval_end`

(optional) Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AWR_HUB Function

Updates the configuration of a hub .

Syntax
```

```

Parameters

Parameter Description

`awr_hub_id`

(required) Unique Awr Hub identifier

`update_awr_hub_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AWR_HUB_SOURCE Function

Update Awr Hub Source object.

Syntax
```

```

Parameters

Parameter Description

`update_awr_hub_source_details`

(required) The configuration to be updated.

`awr_hub_source_id`

(required) Unique Awr Hub Source identifier

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE_INSIGHT Function

Updates configuration of a database insight.

Syntax
```

```

Parameters

Parameter Description

`database_insight_id`

(required) Unique database insight identifier

`update_database_insight_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ENTERPRISE_MANAGER_BRIDGE Function

Updates configuration of an Operations Insights Enterprise Manager bridge.

Syntax
```

```

Parameters

Parameter Description

`enterprise_manager_bridge_id`

(required) Unique Enterprise Manager bridge identifier

`update_enterprise_manager_bridge_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXADATA_INSIGHT Function

Updates configuration of an Exadata insight.

Syntax
```

```

Parameters

Parameter Description

`exadata_insight_id`

(required) Unique Exadata insight identifier

`update_exadata_insight_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HOST_INSIGHT Function

Updates configuration of a host insight.

Syntax
```

```

Parameters

Parameter Description

`host_insight_id`

(required) Unique host insight identifier

`update_host_insight_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NEWS_REPORT Function

Updates the configuration of a news report.

Syntax
```

```

Parameters

Parameter Description

`news_report_id`

(required) Unique news report identifier.

`update_news_report_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function

Updates one or more attributes of the specified private endpoint.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Operation Insights private endpoint.

`update_operations_insights_private_endpoint_details`

(required) The details used to update a private endpoint.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE Function

Updates the configuration of an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_id`

(required) Unique Operations Insights Warehouse identifier

`update_operations_insights_warehouse_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function

Updates the configuration of an Operations Insights Warehouse User.

Syntax
```

```

Parameters

Parameter Description

`operations_insights_warehouse_user_id`

(required) Unique Operations Insights Warehouse User identifier

`update_operations_insights_warehouse_user_details`

(required) The configuration to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPSI_CONFIGURATION Function

Updates an OPSI configuration resource with the given ID.

Syntax
```

```

Parameters

Parameter Description

`opsi_configuration_id`

(required)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of OPSI configuration resource.

`update_opsi_configuration_details`

(required) The OPSI configuration resource details to be updated.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operationsinsights.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OPSI Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-DB70E26F-11F1-4CE4-8040-7E789A14FCDD)
- [ADD_EXADATA_INSIGHT_MEMBERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-0AC42C20-8D7E-4A23-A351-73894326F33B)
- [CHANGE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-0CCD5D28-C2A5-49C4-8920-8149C91499F0)
- [CHANGE_AWR_HUB_SOURCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-F6CDC4DC-DD17-47CE-A9C4-7A6D2A6AD8D0)
- [CHANGE_DATABASE_INSIGHT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-0D8C48FE-273F-469F-B6A7-9317B5F68BE8)
- [CHANGE_ENTERPRISE_MANAGER_BRIDGE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6EADE69C-C5EC-46C2-BD6E-C72C513C7706)
- [CHANGE_EXADATA_INSIGHT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D63F0F8F-D60E-4588-A7DE-01CE9BE82388)
- [CHANGE_HOST_INSIGHT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-AB42BFE9-9DBA-4EFE-A9C4-F90A422C97D0)
- [CHANGE_NEWS_REPORT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E2EFE453-D102-4653-B499-28FB61927745)
- [CHANGE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E465D337-8ADE-4933-8F22-BE1D1550992C)
- [CHANGE_OPERATIONS_INSIGHTS_WAREHOUSE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E77C6097-F24B-4343-8D95-F12BE7A33FAC)
- [CHANGE_OPSI_CONFIGURATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E42FD839-E3EC-47C2-AA0D-7DD46D9DBBE2)
- [CHANGE_PE_COMANAGED_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-110AA69B-DDC8-4C82-A5E6-6B72B368148A)
- [CREATE_AWR_HUB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7B1BC9A2-59D0-498F-A0F8-F5757CF27D34)
- [CREATE_AWR_HUB_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3AAAC7C8-162B-4EF0-AA0B-28F7EA28E2B7)
- [CREATE_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-A391091F-AD76-43DC-B092-40798B20F780)
- [CREATE_ENTERPRISE_MANAGER_BRIDGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6110A537-973F-4BD0-BDFA-767E03BC4231)
- [CREATE_EXADATA_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-64566FED-22D8-417F-B74B-5DE970DB78DA)
- [CREATE_HOST_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-1B287E8F-8E6D-42C4-A772-CE6302DC2AF6)
- [CREATE_NEWS_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7911DCE6-BED0-40EF-81C8-10515EF3345B)
- [CREATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3EF80BF6-0AA9-4113-AD25-61204A6ED2FD)
- [CREATE_OPERATIONS_INSIGHTS_WAREHOUSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-783F78B4-450B-4B9B-9337-2767F121197D)
- [CREATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6920D857-771D-4060-90A3-FB50BFC3ECBD)
- [CREATE_OPSI_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-460B7ADA-B87D-4957-AB7B-94A0E4000FDA)
- [DELETE_AWR_HUB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-93E777F0-FC9E-4C50-804A-FE90F2FFCE8B)
- [DELETE_AWR_HUB_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-CAD0BBF3-07AA-4D17-BC02-74397448D3AA)
- [DELETE_AWR_HUB_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3D23C7FC-2B88-49D1-9B8F-0E723E22BEAD)
- [DELETE_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-BBB01F22-3E2E-496D-9C95-05A340648915)
- [DELETE_ENTERPRISE_MANAGER_BRIDGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-EF21AD8E-8066-4235-A0F7-F8E5BF8A1615)
- [DELETE_EXADATA_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-31CB7A4C-D2D7-460E-94DA-0A509758CC18)
- [DELETE_HOST_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3AB9E770-014E-41AC-B482-882CE1B52FBC)
- [DELETE_NEWS_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-1D9D2DBD-C1EB-4C7B-9DE7-775FE6047D9E)
- [DELETE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-F639AA44-F6C4-4C60-AF90-06EE48A79123)
- [DELETE_OPERATIONS_INSIGHTS_WAREHOUSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-4E150BC6-23C2-487D-9B6B-1A6D6B629726)
- [DELETE_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E4444B26-1AC4-4F93-91EA-11DCB7F840DC)
- [DELETE_OPSI_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D2E6A4DD-ABF4-412D-95BB-C6E7946C46DC)
- [DISABLE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C6ADCDCE-D601-4E0C-83FB-FAF280FCB858)
- [DISABLE_AWR_HUB_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C912AB79-F7F6-473C-8FA6-9734F2BE4B97)
- [DISABLE_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-04C7B77F-EB25-4CC1-8DAA-0C5E21F8ED2A)
- [DISABLE_EXADATA_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-993941A0-F2EF-48F3-971A-5CC5056ADEF0)
- [DISABLE_HOST_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-8112D672-6348-4C5C-9DA9-8BDA237681A3)
- [DOWNLOAD_OPERATIONS_INSIGHTS_WAREHOUSE_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-97D8C79D-2D78-49B0-A638-17F4ED1FD499)
- [ENABLE_AUTONOMOUS_DATABASE_INSIGHT_ADVANCED_FEATURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-2D100ACE-EC36-4961-BD92-25820013B24D)
- [ENABLE_AWR_HUB_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-0B48CA5F-0642-4B32-A6F1-9660562427BC)
- [ENABLE_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-DD3EBE00-78A9-4C97-BA1A-7BA69D2534E9)
- [ENABLE_EXADATA_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-23019AC9-EC6F-49B4-A413-7A3D988FA80F)
- [ENABLE_HOST_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D8544981-0C3C-47ED-9043-F6BD9C024E3B)
- [GET_AWR_DATABASE_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6132DEAF-FC97-43D8-907F-824E7E6175B6)
- [GET_AWR_DATABASE_SQL_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-923A30ED-0CFD-4D7F-813A-3A3C8E244A1D)
- [GET_AWR_HUB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-681CFD4D-A921-4865-A83F-19EBF72AC8FB)
- [GET_AWR_HUB_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D82F6661-2B3B-4E57-B2D8-9CD05F0A3712)
- [GET_AWR_HUB_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6DCEB207-CD5A-46A4-83F3-7109A9C96241)
- [GET_AWR_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-EDFF5A0A-933B-43B6-8719-A68233AAB85C)
- [GET_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-8975B2B6-68E8-4DC6-8129-5C4C0E4429E4)
- [GET_ENTERPRISE_MANAGER_BRIDGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-17747EE0-5CD8-4F4F-8756-ACF17943D2ED)
- [GET_EXADATA_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3E069D94-05F2-44B8-8D28-D3EE9CDB70C7)
- [GET_HOST_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C397BD01-C6DB-4424-B53B-F4E378BBD0A6)
- [GET_NEWS_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3926F151-623B-4533-A538-2D98AF67B848)
- [GET_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-FCD388B5-CF7C-40C5-9819-77AEAB4A1464)
- [GET_OPERATIONS_INSIGHTS_WAREHOUSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-751547AB-4964-4CA2-AE85-A3160BD62A2C)
- [GET_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C5B002FB-85DA-4E96-831B-2B1759EFD707)
- [GET_OPSI_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-602F4DC3-6C21-4FC8-9F5D-C70F8A682019)
- [GET_OPSI_DATA_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D826EDBA-FF5C-4BEE-B3C0-AB43FE35FA28)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-11AA228D-6AB1-461F-85AF-FEA9ED78D19D)
- [HEAD_AWR_HUB_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3C4EB991-F65C-4E30-92C1-61B6CFED68A1)
- [INGEST_ADDM_REPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-71A46014-D3EE-46D1-A550-D72A99A705A5)
- [INGEST_DATABASE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-04AE4774-9725-4710-B22A-E920214DDD6D)
- [INGEST_HOST_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-DFFA7B77-762B-4504-9864-8C5FA912136A)
- [INGEST_HOST_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B33EB24D-065F-4319-A041-36ADECD3A96E)
- [INGEST_SQL_BUCKET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-ECD2B23E-D141-4509-BED9-E7942DD2A035)
- [INGEST_SQL_PLAN_LINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-65DA9072-6972-44F5-A9E7-993FAB89C05D)
- [INGEST_SQL_STATS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-93035CF8-3F9D-4A06-9AD0-C1533B1F44CC)
- [INGEST_SQL_TEXT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E19E137E-FE5A-435E-A8ED-BBFEB8D4B206)
- [LIST_ADDM_DB_FINDING_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-2F066CAE-38FF-4F15-921D-BE764F17E2B4)
- [LIST_ADDM_DB_FINDINGS_TIME_SERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-13E09FBF-6DDA-4598-A3B7-E3090EA2AB5B)
- [LIST_ADDM_DB_PARAMETER_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-914D7026-2AA6-47A5-A41D-A9FD9D4F2B87)
- [LIST_ADDM_DB_RECOMMENDATION_CATEGORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B7A3D204-8BEF-4838-BAC6-D9DF0DD65F9B)
- [LIST_ADDM_DB_RECOMMENDATIONS_TIME_SERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-BC17DB27-36F6-4E95-AF12-3EE75E6C0236)
- [LIST_ADDM_DBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-40004FA8-D1D5-411E-91FC-BA8E5566D45A)
- [LIST_AWR_DATABASE_SNAPSHOTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-A07D729F-54CB-4E68-8100-56CEC849387C)
- [LIST_AWR_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D56A95CA-E733-43D7-AD9A-1F203CC3E4E8)
- [LIST_AWR_HUB_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C8C50A41-9C94-4ACC-B107-0DBCB6A0711D)
- [LIST_AWR_HUB_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-8EF2CFE4-5476-4372-97EF-1335A600C61A)
- [LIST_AWR_HUBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5FFAEBBA-2126-4B3A-8A05-CBC0BE2D907C)
- [LIST_AWR_SNAPSHOTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-0D996FB5-09B3-4544-83CE-1E9FCD337D94)
- [LIST_DATABASE_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D2E2F26E-5C6B-4861-83C8-EABDE75CF176)
- [LIST_DATABASE_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C8A71FB8-E536-4A9E-9A6B-7D878CA1123A)
- [LIST_ENTERPRISE_MANAGER_BRIDGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-2AE78FDA-AD99-4C19-B987-64ECEA6BFDB3)
- [LIST_EXADATA_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-46B48F65-B7BA-4B2E-BF1A-A979357B1BE1)
- [LIST_EXADATA_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6EF4D77E-BDDD-407A-91FB-D12B2CEB0473)
- [LIST_HOST_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C5F935FC-6577-47AC-AB34-0531B35300EE)
- [LIST_HOST_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5B477564-9C4B-46E8-B5E6-AF7E6629A901)
- [LIST_HOSTED_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B75E158F-0ACE-4186-81B8-F87B3F3556A7)
- [LIST_IMPORTABLE_AGENT_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-43331C8B-9C96-43F5-8C31-4EA8882D0A2D)
- [LIST_IMPORTABLE_COMPUTE_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-116595AE-94D6-435C-978D-8394DC0F7659)
- [LIST_IMPORTABLE_ENTERPRISE_MANAGER_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5BA19262-A289-4593-B9E4-42CA2583BA01)
- [LIST_NEWS_REPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-57195A2C-36D1-46AF-A46F-5A1FAFC68D67)
- [LIST_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-101D4BD7-2DCA-4DCD-ACD9-D91B87634729)
- [LIST_OPERATIONS_INSIGHTS_WAREHOUSE_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7781E704-0C4E-45B6-8EEE-786579145094)
- [LIST_OPERATIONS_INSIGHTS_WAREHOUSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3DA37987-D477-48BC-B9E0-E4AC94B0129A)
- [LIST_OPSI_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-E85B831E-7FBE-43B7-8B22-DE6C10B06C66)
- [LIST_OPSI_DATA_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3F7A06A9-A74B-4CB6-A472-2BF5D2333F2A)
- [LIST_SQL_PLANS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7102CCC8-F13B-4E92-8A18-C66AF9DF160D)
- [LIST_SQL_SEARCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-90E5283A-F739-4AE9-A5D2-16763BB3E605)
- [LIST_SQL_TEXTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-CCD260A1-83BC-426E-9DD3-EDE5474D5A4F)
- [LIST_WAREHOUSE_DATA_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5DB6AC75-6F20-4E4A-84F8-329BA861E770)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-27C4AE46-8E95-4BAA-A575-DB66A1FF4599)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7D785A74-491B-4F7B-A53B-113C70A4EC04)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6F97E861-DF02-406F-ADAE-4EC234DF7D00)
- [PUT_AWR_HUB_OBJECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-4B0C1582-D29B-4AE7-8659-45FCAEE45534)
- [QUERY_OPSI_DATA_OBJECT_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-AC26B671-481D-4B65-9501-9EA8109694F0)
- [QUERY_WAREHOUSE_DATA_OBJECT_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-66FA1B77-08FA-4990-8207-3FE9BB7F5EC1)
- [ROTATE_OPERATIONS_INSIGHTS_WAREHOUSE_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B56E1CD1-C8DD-4285-BAD6-ACB18F2C84E3)
- [SUMMARIZE_ADDM_DB_FINDINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-DB78ADD6-8A74-48F1-8B10-2C9980883A0C)
- [SUMMARIZE_ADDM_DB_PARAMETER_CHANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-BBEB497F-0E58-4958-BF25-A514482BF322)
- [SUMMARIZE_ADDM_DB_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-EF843FE4-14F6-40FC-A2F1-779DC973ADAE)
- [SUMMARIZE_ADDM_DB_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-4375B104-D657-4FCD-B3A3-4074D8D7203B)
- [SUMMARIZE_ADDM_DB_SCHEMA_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-AD285664-8A56-43BA-9106-17C5652068F3)
- [SUMMARIZE_ADDM_DB_SQL_STATEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-FA8C403F-AFD3-4243-BCB5-D4F968C9D745)
- [SUMMARIZE_AWR_DATABASE_CPU_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6BF0023A-1238-4626-AA4E-0966BF0720EC)
- [SUMMARIZE_AWR_DATABASE_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-522E8FE0-213B-411C-AD93-35E8BFC90D6F)
- [SUMMARIZE_AWR_DATABASE_PARAMETER_CHANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C00F3364-2791-4E9C-8AEB-D8B3ACEFA004)
- [SUMMARIZE_AWR_DATABASE_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-9A14BF14-572E-457E-A3F3-35C66E730395)
- [SUMMARIZE_AWR_DATABASE_SNAPSHOT_RANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-AD812826-4AF9-4288-B3C2-3668F8550885)
- [SUMMARIZE_AWR_DATABASE_SYSSTATS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-FCA6340F-811D-452E-9AAE-BB34FF619E99)
- [SUMMARIZE_AWR_DATABASE_TOP_WAIT_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-FCDE75FF-53FB-4C0E-A5A2-E21D3E74555A)
- [SUMMARIZE_AWR_DATABASE_WAIT_EVENT_BUCKETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B5DA44D0-1C20-45BA-BA50-EC77C976EF0C)
- [SUMMARIZE_AWR_DATABASE_WAIT_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-BFC2F02E-ED3B-4DDB-9301-D5303038327F)
- [SUMMARIZE_AWR_SOURCES_SUMMARIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C92A861C-D157-4D91-B640-E8F1733FF48F)
- [SUMMARIZE_CONFIGURATION_ITEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-DE8505D2-DAAE-4B09-94E0-38B70DB9F707)
- [SUMMARIZE_DATABASE_INSIGHT_RESOURCE_CAPACITY_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-21598E53-316D-4234-B572-9D73B22762B8)
- [SUMMARIZE_DATABASE_INSIGHT_RESOURCE_FORECAST_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-D8562B38-AED2-4563-9376-E106E44B5EAA)
- [SUMMARIZE_DATABASE_INSIGHT_RESOURCE_STATISTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-829AB9DF-5EFE-4255-ACA2-3DB9E80497AC)
- [SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-51183D79-89D9-43E4-862C-A1C09B38E20F)
- [SUMMARIZE_DATABASE_INSIGHT_RESOURCE_USAGE_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-DE9E11D6-271B-44D6-BA14-38AD58466378)
- [SUMMARIZE_DATABASE_INSIGHT_RESOURCE_UTILIZATION_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-164D7C9D-2838-4AED-82C3-0592567E5793)
- [SUMMARIZE_DATABASE_INSIGHT_TABLESPACE_USAGE_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C1AF2CCD-744C-4478-AD5D-749B803A133A)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3DD5CE2D-C6F7-41CC-975C-4DBFD48FDFB1)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_CAPACITY_TREND_AGGREGATED Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B258002B-2A42-4895-A823-075FE88B10B6)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-12207732-E8A9-4045-80B2-A84869FE779A)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_FORECAST_TREND_AGGREGATED Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5CCDAC55-1E2B-465E-91E7-EE7F8650228B)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_STATISTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5A4604D6-7FE1-4DE0-BF62-301191B5498E)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-CF53CA4E-D6A3-4D69-937F-5764E5EA31F1)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_USAGE_AGGREGATED Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-29065A00-CC00-409F-BFD1-95D0D5DADD09)
- [SUMMARIZE_EXADATA_INSIGHT_RESOURCE_UTILIZATION_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-9F61CE1D-A013-4AE3-A345-D20142EEEBF2)
- [SUMMARIZE_EXADATA_MEMBERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-500DE24A-10E7-460F-9490-78680E6DAD94)
- [SUMMARIZE_HOST_INSIGHT_DISK_STATISTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-8FD56B06-3E96-4BD6-86FC-D63382F17C2F)
- [SUMMARIZE_HOST_INSIGHT_HOST_RECOMMENDATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7039EE61-65EF-4167-AF1E-90A413AB727E)
- [SUMMARIZE_HOST_INSIGHT_NETWORK_USAGE_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-C4F6857B-11AC-4683-83E0-0E37330E397D)
- [SUMMARIZE_HOST_INSIGHT_RESOURCE_CAPACITY_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3B19390C-C84E-4550-A048-0AF31AB1FEC4)
- [SUMMARIZE_HOST_INSIGHT_RESOURCE_FORECAST_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-24E2DD27-B440-45F3-A4FA-299973607680)
- [SUMMARIZE_HOST_INSIGHT_RESOURCE_STATISTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-9E0B8856-2BB2-457F-836B-28060E3124FE)
- [SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-1AE52B6C-F432-4E3A-9536-8E7141756F20)
- [SUMMARIZE_HOST_INSIGHT_RESOURCE_USAGE_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-33F8F204-9ADA-41F2-872B-6505A23827CF)
- [SUMMARIZE_HOST_INSIGHT_RESOURCE_UTILIZATION_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-0195898C-C259-41CB-9297-9F2B85E916C2)
- [SUMMARIZE_HOST_INSIGHT_STORAGE_USAGE_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5EF5C849-677A-466F-BD5A-7127A6DA6F28)
- [SUMMARIZE_HOST_INSIGHT_TOP_PROCESSES_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-59DDA62E-C18D-45A0-8921-1A313FB6A730)
- [SUMMARIZE_HOST_INSIGHT_TOP_PROCESSES_USAGE_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-14F34036-ECB7-44B0-A391-97F579522AE6)
- [SUMMARIZE_OPERATIONS_INSIGHTS_WAREHOUSE_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-8262DE2E-798A-4282-BDA9-C4C669EB1D6D)
- [SUMMARIZE_SQL_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-65347B00-0242-4A6D-9939-1B391F8EAB3B)
- [SUMMARIZE_SQL_PLAN_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-5A5A15A0-AE26-42CB-87C7-D715F22640C4)
- [SUMMARIZE_SQL_RESPONSE_TIME_DISTRIBUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-23C58565-42A4-45F4-8B11-0BBEF048B573)
- [SUMMARIZE_SQL_STATISTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-CAB0C9BB-1F1E-430E-86D6-156EA108D1F6)
- [SUMMARIZE_SQL_STATISTICS_TIME_SERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3FDF62D9-64C9-4BCC-9CB8-667558DF52C9)
- [SUMMARIZE_SQL_STATISTICS_TIME_SERIES_BY_PLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-3A0E6AEA-BEEE-497D-8FE3-CED23C01C2BA)
- [UPDATE_AWR_HUB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-849EC30A-0714-478B-BE34-F8C93DA15845)
- [UPDATE_AWR_HUB_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B7AEAD2B-71B7-450B-A3B3-D72E7446F0CD)
- [UPDATE_DATABASE_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-87F58ECA-3331-41B8-8C7E-57DF9BECA962)
- [UPDATE_ENTERPRISE_MANAGER_BRIDGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-8D1CD9A8-7A55-42BA-99EE-FC293D1DA06A)
- [UPDATE_EXADATA_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-B7EE7082-775C-4726-9493-DE8EE668E2EF)
- [UPDATE_HOST_INSIGHT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-A2DAB417-0266-43C0-82F6-708609F7BE2A)
- [UPDATE_NEWS_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-9E8C7A9E-6792-4768-935F-A9EB4A013EBF)
- [UPDATE_OPERATIONS_INSIGHTS_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-7FC17E3C-4C23-4DA4-8CB9-BE9B91414871)
- [UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6D658F75-BD5B-481A-B401-CCF056D4908A)
- [UPDATE_OPERATIONS_INSIGHTS_WAREHOUSE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-A19362F6-E9EE-46E1-9937-2A30822736D1)
- [UPDATE_OPSI_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_opsi_operations_insights.html#ADSDK-GUID-6BB3E72A-C6FD-43D8-B7F0-53F14D95F2C8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
