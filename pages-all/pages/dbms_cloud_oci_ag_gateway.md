# API Gateway Gateway Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#dcoc-content-body)

## API Gateway Gateway Functions

Package: DBMS_CLOUD_OCI_AG_GATEWAY

### CHANGE_GATEWAY_COMPARTMENT Function

Changes the gateway compartment.

Syntax
```

```

Parameters

Parameter Description

`gateway_id`

(required) The ocid of the gateway.

`change_gateway_compartment_details`

(required) Details of the target compartment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_GATEWAY Function

Creates a new gateway.

Syntax
```

```

Parameters

Parameter Description

`create_gateway_details`

(required) Details for the new gateway.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_GATEWAY Function

Deletes the gateway with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`gateway_id`

(required) The ocid of the gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GATEWAY Function

Gets a gateway by identifier.

Syntax
```

```

Parameters

Parameter Description

`gateway_id`

(required) The ocid of the gateway.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GATEWAYS Function

Returns a list of gateways.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ocid of the compartment in which to list resources.

`certificate_id`

(optional) Filter gateways by the certificate ocid.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state. Example: `SUCCEEDED`

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for `timeCreated` is descending. Default order for `displayName` is ascending. The `displayName` sort order is case sensitive.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GATEWAY Function

Updates the gateway with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`gateway_id`

(required) The ocid of the gateway.

`update_gateway_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request id for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apigateway.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [API Gateway Gateway Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-BFA0ABE4-FA84-438F-A6EC-943B190201CE)
- [CHANGE_GATEWAY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-F3C0F392-8E95-446A-AFC7-AD9F6488F8A0)
- [CREATE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-0C61E0B0-3017-4FD8-BD81-4FE6DA8D1F84)
- [DELETE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-B12F1035-4E27-4B3F-B81F-8BE811BCD898)
- [GET_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-82800660-7DB8-4200-81A7-62A346A47258)
- [LIST_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-29B6C251-058F-41FE-9F61-B8981184D969)
- [UPDATE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ag_gateway.html#ADSDK-GUID-9DD42FA6-F096-49BC-93FC-813F33FAC32E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
