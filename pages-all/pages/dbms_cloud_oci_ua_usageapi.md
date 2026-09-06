# Usage API Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#dcoc-content-body)

## Usage API Functions

Package: DBMS_CLOUD_OCI_UA_USAGEAPI

### CREATE_CUSTOM_TABLE Function

Returns the created custom table.

Syntax
```

```

Parameters

Parameter Description

`create_custom_table_details`

(required) New custom table details.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_QUERY Function

Returns the created query.

Syntax
```

```

Parameters

Parameter Description

`create_query_details`

(required) New query details. Up to ten saved queries.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SCHEDULE Function

Returns the created schedule.

Syntax
```

```

Parameters

Parameter Description

`create_schedule_details`

(required) New schedule details.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_USAGE_CARBON_EMISSIONS_QUERY Function

Returns the created usage carbon emissions query.

Syntax
```

```

Parameters

Parameter Description

`create_usage_carbon_emissions_query_details`

(required) New query details. Up to ten saved queries.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CUSTOM_TABLE Function

Delete a saved custom table by the OCID.

Syntax
```

```

Parameters

Parameter Description

`custom_table_id`

(required) The custom table unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_QUERY Function

Delete a saved query by the OCID.

Syntax
```

```

Parameters

Parameter Description

`query_id`

(required) The query unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SCHEDULE Function

Delete a saved scheduled report by the OCID.

Syntax
```

```

Parameters

Parameter Description

`schedule_id`

(required) The schedule unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_USAGE_CARBON_EMISSIONS_QUERY Function

Delete a usage carbon emissions saved query by the OCID.

Syntax
```

```

Parameters

Parameter Description

`usage_carbon_emissions_query_id`

(required) The query unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CUSTOM_TABLE Function

Returns the saved custom table.

Syntax
```

```

Parameters

Parameter Description

`custom_table_id`

(required) The custom table unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_QUERY Function

Returns the saved query.

Syntax
```

```

Parameters

Parameter Description

`query_id`

(required) The query unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCHEDULE Function

Returns the saved schedule.

Syntax
```

```

Parameters

Parameter Description

`schedule_id`

(required) The schedule unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCHEDULED_RUN Function

Returns the saved schedule run.

Syntax
```

```

Parameters

Parameter Description

`scheduled_run_id`

(required) The scheduledRun unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USAGE_CARBON_EMISSIONS_QUERY Function

Returns the usage carbon emissions saved query.

Syntax
```

```

Parameters

Parameter Description

`usage_carbon_emissions_query_id`

(required) The query unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CUSTOM_TABLES Function

Returns the saved custom table list.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment ID in which to list resources.

`saved_report_id`

(required) The saved report ID in which to list resources.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximumimum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort by. If not specified, the default is displayName.

Allowed values are: 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_QUERIES Function

Returns the saved query list.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment ID in which to list resources.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximumimum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort by. If not specified, the default is displayName.

Allowed values are: 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEDULED_RUNS Function

Returns schedule history list.

Syntax
```

```

Parameters

Parameter Description

`schedule_id`

(required) The unique ID of a schedule.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximumimum number of items to return.

`sort_by`

(optional) The field to sort by. If not specified, the default is timeCreated.

Allowed values are: 'timeCreated'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEDULES Function

Returns the saved schedule list.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment ID in which to list resources.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximumimum number of items to return.

`sort_by`

(optional) The field to sort by. If not specified, the default is timeCreated.

Allowed values are: 'name', 'timeCreated'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`name`

(optional) Query parameter for filtering by name

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USAGE_CARBON_EMISSIONS_QUERIES Function

Returns the usage carbon emissions saved query list.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment ID in which to list resources.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximumimum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort by. If not specified, the default is displayName.

Allowed values are: 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_AVERAGE_CARBON_EMISSION Function

Returns the average carbon emissions summary by SKU.

Syntax
```

```

Parameters

Parameter Description

`sku_part_number`

(required) The SKU part number.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_CLEAN_ENERGY_USAGE Function

Returns the clean energy usage summary by region.

Syntax
```

```

Parameters

Parameter Description

`l_region`

(required) The region.

`ad`

(optional) The availability domain.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_CONFIGURATIONS Function

Returns the configurations list for the UI drop-down list.

Syntax
```

```

Parameters

Parameter Description

`tenant_id`

(required) tenant id

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_USAGES Function

Returns usage for the given account.

Syntax
```

```

Parameters

Parameter Description

`request_summarized_usages_details`

(required) getUsageRequest contains query inforamtion.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximumimum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_USAGE_CARBON_EMISSION_CONFIG Function

Returns the configuration list for the UI drop-down list of carbon emission console.

Syntax
```

```

Parameters

Parameter Description

`tenant_id`

(required) tenant id

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_USAGE_CARBON_EMISSIONS Function

Returns usage carbon emission for the given account.

Syntax
```

```

Parameters

Parameter Description

`request_usage_carbon_emissions_details`

(required) getUsageCarbonEmissionRequest contains query inforamtion.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximumimum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CUSTOM_TABLE Function

Update a saved custom table by table id.

Syntax
```

```

Parameters

Parameter Description

`update_custom_table_details`

(required) The information to be updated.

`custom_table_id`

(required) The custom table unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_QUERY Function

Update a saved query by the OCID.

Syntax
```

```

Parameters

Parameter Description

`update_query_details`

(required) The information to be updated.

`query_id`

(required) The query unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SCHEDULE Function

Update a saved schedule

Syntax
```

```

Parameters

Parameter Description

`update_schedule_details`

(required) The information to be updated. Currently supports only tags

`schedule_id`

(required) The schedule unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_USAGE_CARBON_EMISSIONS_QUERY Function

Update a usage carbon emissions saved query by the OCID.

Syntax
```

```

Parameters

Parameter Description

`update_usage_carbon_emissions_query_details`

(required) The information to be updated.

`usage_carbon_emissions_query_id`

(required) The query unique OCID.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://usageapi.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Usage API Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-C27CFF7E-B937-4F08-92BC-0B574D5AE955)
- [CREATE_CUSTOM_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-B65AB3FD-5DCB-419A-9E81-7E418C3AA630)
- [CREATE_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-BF15F78B-EE4F-48F1-8082-087B54010F3F)
- [CREATE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-150D0EBC-8525-4377-BA19-D71906C2C29B)
- [CREATE_USAGE_CARBON_EMISSIONS_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-360417D0-195E-4D93-8FAB-855A9A073B70)
- [DELETE_CUSTOM_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-867D07B4-EC69-4EFC-8EAB-ACB8DFBBA58B)
- [DELETE_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-B697FA19-1D2D-4DFE-AC39-E1D5CEC71179)
- [DELETE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-C9B59621-4867-4B36-BD28-CC333B48CAE2)
- [DELETE_USAGE_CARBON_EMISSIONS_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-98ECF2E1-71BD-4DE4-A7A3-90FD398E6CC9)
- [GET_CUSTOM_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-29790706-1F24-4E5E-AB96-0AE9AA18024E)
- [GET_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-6B3A151C-96AE-4F1C-ADF4-83DD31257570)
- [GET_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-A775A155-9BEF-4510-89E5-608F3076B4B1)
- [GET_SCHEDULED_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-A7D621D5-649B-434A-9E26-9695C094939C)
- [GET_USAGE_CARBON_EMISSIONS_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-833AE4C0-01E5-46D1-82AB-442021FE1045)
- [LIST_CUSTOM_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-510E2A6F-CCD4-408E-98D3-7845635AF7F5)
- [LIST_QUERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-BAD3E701-1F4F-4D86-994C-2370DA3F6E91)
- [LIST_SCHEDULED_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-3A9DF9DF-9B04-4FE7-8E3E-4B5504AE32A9)
- [LIST_SCHEDULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-CE0D7F88-BB70-43CE-9D10-62D7D873B6AD)
- [LIST_USAGE_CARBON_EMISSIONS_QUERIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-95C2ED3B-2F25-4350-8E04-F6A031F5DDF3)
- [REQUEST_AVERAGE_CARBON_EMISSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-84D7D3FA-D0CC-4AF3-A5FD-EBB63478C812)
- [REQUEST_CLEAN_ENERGY_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-27958AF3-CA06-4A82-AA54-F1A5719CF1F0)
- [REQUEST_SUMMARIZED_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-4426F2DB-3AFE-4F6B-A387-527B0C8C5641)
- [REQUEST_SUMMARIZED_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-462CE8A5-0CA2-4F9B-A80E-93E5D716B98E)
- [REQUEST_USAGE_CARBON_EMISSION_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-D4077D06-162D-4EE6-9906-79409BF344F2)
- [REQUEST_USAGE_CARBON_EMISSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-88A8723F-4387-4146-BC8E-41FDB867C602)
- [UPDATE_CUSTOM_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-1B52CD40-4403-49C8-9811-AD52B02AB953)
- [UPDATE_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-6873DC8C-4FF7-4D0B-A30F-389A196AAFCA)
- [UPDATE_SCHEDULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-E9287D3D-077A-448D-893A-EB3B117691E5)
- [UPDATE_USAGE_CARBON_EMISSIONS_QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ua_usageapi.html#ADSDK-GUID-7D9B0DBC-D709-444E-A900-4F8BB54E3389)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
