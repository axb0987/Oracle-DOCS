# Cloud Bridge Inventory Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#dcoc-content-body)

## Cloud Bridge Inventory Functions

Package: DBMS_CLOUD_OCI_CB_INVENTORY

### ANALYZE_ASSETS Function

Returns an aggregation of assets. Aggregation groups are sorted by groupBy property. Default sort order is ascending, but can be overridden by the sortOrder parameter.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`aggregation_properties`

(required) An array of properties on which to aggregate.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`lifecycle_state`

(optional) A filter to return only assets whose lifecycleState matches the given lifecycleState.

`source_key`

(optional) Source key from where the assets originate.

`external_asset_key`

(optional) External asset key.

`asset_type`

(optional) The type of asset.

Allowed values are: 'VMWARE_VM', 'VM'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`group_by`

(optional) The dimensions in which to group the aggregations.

`inventory_id`

(optional) Unique Inventory identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ASSET_COMPARTMENT Function

Moves an asset resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) Unique asset identifier.

`change_asset_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ASSET_TAGS Function

Change an asset's tag.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) Unique asset identifier.

`change_asset_tags_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ASSET Function

Creates an asset.

Syntax
```

```

Parameters

Parameter Description

`create_asset_details`

(required) The information to be updated.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INVENTORY Function

Creates an inventory.

Syntax
```

```

Parameters

Parameter Description

`create_inventory_details`

(required) The information to be updated.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ASSET Function

Deletes an asset resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) Unique asset identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INVENTORY Function

Deletes an inventory resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`inventory_id`

(required) Inventory OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ASSET Function

Gets an asset by identifier.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) Unique asset identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INVENTORY Function

Gets an inventory by identifier.

Syntax
```

```

Parameters

Parameter Description

`inventory_id`

(required) Inventory OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_INVENTORY Function

Import resources in inventory.

Syntax
```

```

Parameters

Parameter Description

`import_inventory_details`

(required) The file input to create resources.

`inventory_id`

(required) Inventory OCID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours, but can be invalidated before 24 hours due to conflicting operations. For example, if a resource has been deleted and purged from the system, a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ASSETS Function

Returns a list of assets.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`lifecycle_state`

(optional) A filter to return only assets whose lifecycleState matches the given lifecycleState.

`source_key`

(optional) Source key from where the assets originate.

`external_asset_key`

(optional) External asset key.

`asset_type`

(optional) The type of asset.

Allowed values are: 'VMWARE_VM', 'VM'

`asset_id`

(optional) Unique asset identifier.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`inventory_id`

(optional) Unique Inventory identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HISTORICAL_METRICS Function

List asset historical metrics.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) Unique asset identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INVENTORIES Function

Returns a list of inventories.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`lifecycle_state`

(optional) A filter to return inventory if the lifecycleState matches the given lifecycleState.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUBMIT_HISTORICAL_METRICS Function

Creates or updates all metrics related to the asset.

Syntax
```

```

Parameters

Parameter Description

`submit_historical_metrics_details`

(required) Creates or updates all metrics related to the asset.

`asset_id`

(required) Unique asset identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ASSET Function

Updates the asset.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) Unique asset identifier.

`update_asset_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INVENTORY Function

Updates an inventory.

Syntax
```

```

Parameters

Parameter Description

`inventory_id`

(required) Inventory OCID.

`update_inventory_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudbridge.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Cloud Bridge Inventory Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-E22EDBCA-881C-4CC1-AB62-B70C324C8E8E)
- [ANALYZE_ASSETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-76E14E00-83F8-414E-90E5-F9C9E92E0085)
- [CHANGE_ASSET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-A59160D0-CFEA-429C-B4EF-19D25FD2D8CC)
- [CHANGE_ASSET_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-6D582419-8FC9-4671-B198-06A3FD75F5D1)
- [CREATE_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-9FE51E76-DF22-413F-888D-1140A580F5A2)
- [CREATE_INVENTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-93CD60C6-7D10-4140-8F05-F785532D7AC4)
- [DELETE_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-C359B79C-8BD0-448F-B170-FCFA7004EF08)
- [DELETE_INVENTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-4C0E0AF9-8AE9-4D9A-A998-E9AFAFA69166)
- [GET_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-70406BA1-0690-4D5F-AFE8-2B65E0C4B316)
- [GET_INVENTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-7FF4D806-87EE-4B39-907D-265EC16038EF)
- [IMPORT_INVENTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-FCFF3945-8EC8-4F54-9C4D-BFE9E72A5E33)
- [LIST_ASSETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-8B30C377-1716-40B5-8ECA-9DD8A02C4E9C)
- [LIST_HISTORICAL_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-AAFBA47C-996D-46EC-9F27-D9B5C4204291)
- [LIST_INVENTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-80F35044-40E8-4C92-8B8B-C21F3AABC3A1)
- [SUBMIT_HISTORICAL_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-B73ADD94-F337-4665-9231-C52386B9F080)
- [UPDATE_ASSET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-AD15142D-269A-4ED2-A044-C3E045BB3D7E)
- [UPDATE_INVENTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cb_inventory.html#ADSDK-GUID-CF45B24E-C9FD-4092-8648-0AD4234CD1EB)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
