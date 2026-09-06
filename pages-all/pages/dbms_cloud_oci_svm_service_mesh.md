# Service Mesh Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#dcoc-content-body)

## Service Mesh Functions

Package: DBMS_CLOUD_OCI_SVM_SERVICE_MESH

### CANCEL_WORK_REQUEST Function

Cancels the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ACCESS_POLICY_COMPARTMENT Function

Moves an AccessPolicy resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`access_policy_id`

(required) Unique AccessPolicy identifier.

`change_access_policy_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_INGRESS_GATEWAY_COMPARTMENT Function

Moves a IngressGateway resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_id`

(required) Unique IngressGateway identifier.

`change_ingress_gateway_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_INGRESS_GATEWAY_ROUTE_TABLE_COMPARTMENT Function

Moves a IngressGatewayRouteTable resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_route_table_id`

(required) Unique IngressGatewayRouteTable identifier.

`change_ingress_gateway_route_table_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MESH_COMPARTMENT Function

Moves a Mesh resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`mesh_id`

(required) Unique Mesh identifier.

`change_mesh_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VIRTUAL_DEPLOYMENT_COMPARTMENT Function

Moves a VirtualDeployment resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`virtual_deployment_id`

(required) Unique VirtualDeployment identifier.

`change_virtual_deployment_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VIRTUAL_SERVICE_COMPARTMENT Function

Moves a VirtualService resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_id`

(required) Unique VirtualService identifier.

`change_virtual_service_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VIRTUAL_SERVICE_ROUTE_TABLE_COMPARTMENT Function

Moves a VirtualServiceRouteTable resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_route_table_id`

(required) Unique VirtualServiceRouteTable identifier.

`change_virtual_service_route_table_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ACCESS_POLICY Function

Creates a new AccessPolicy.

Syntax
```

```

Parameters

Parameter Description

`create_access_policy_details`

(required) Details for the new AccessPolicy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INGRESS_GATEWAY Function

Creates a new IngressGateway.

Syntax
```

```

Parameters

Parameter Description

`create_ingress_gateway_details`

(required) Details for the new IngressGateway.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INGRESS_GATEWAY_ROUTE_TABLE Function

Creates a new IngressGatewayRouteTable.

Syntax
```

```

Parameters

Parameter Description

`create_ingress_gateway_route_table_details`

(required) Details for the new IngressGatewayRouteTable.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MESH Function

Creates a new Mesh.

Syntax
```

```

Parameters

Parameter Description

`create_mesh_details`

(required) Details for the new Mesh.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VIRTUAL_DEPLOYMENT Function

Creates a new VirtualDeployment.

Syntax
```

```

Parameters

Parameter Description

`create_virtual_deployment_details`

(required) Details for the new VirtualDeployment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VIRTUAL_SERVICE Function

Creates a new VirtualService.

Syntax
```

```

Parameters

Parameter Description

`create_virtual_service_details`

(required) Details for the new VirtualService.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VIRTUAL_SERVICE_ROUTE_TABLE Function

Creates a new VirtualServiceRouteTable.

Syntax
```

```

Parameters

Parameter Description

`create_virtual_service_route_table_details`

(required) Details for the new VirtualServiceRouteTable.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ACCESS_POLICY Function

Deletes an AccessPolicy resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`access_policy_id`

(required) Unique AccessPolicy identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INGRESS_GATEWAY Function

Deletes an IngressGateway resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_id`

(required) Unique IngressGateway identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INGRESS_GATEWAY_ROUTE_TABLE Function

Deletes a IngressGatewayRouteTable resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_route_table_id`

(required) Unique IngressGatewayRouteTable identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MESH Function

Deletes a Mesh resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`mesh_id`

(required) Unique Mesh identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VIRTUAL_DEPLOYMENT Function

Deletes a VirtualDeployment resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`virtual_deployment_id`

(required) Unique VirtualDeployment identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VIRTUAL_SERVICE Function

Deletes a VirtualService resource by identifier

Syntax
```

```

Parameters

Parameter Description

`virtual_service_id`

(required) Unique VirtualService identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VIRTUAL_SERVICE_ROUTE_TABLE Function

Deletes a VirtualServiceRouteTable resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_route_table_id`

(required) Unique VirtualServiceRouteTable identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ACCESS_POLICY Function

Get an AccessPolicy by identifier.

Syntax
```

```

Parameters

Parameter Description

`access_policy_id`

(required) Unique AccessPolicy identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INGRESS_GATEWAY Function

Gets an IngressGateway by identifier.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_id`

(required) Unique IngressGateway identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INGRESS_GATEWAY_ROUTE_TABLE Function

Gets a IngressGatewayRouteTable by identifier.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_route_table_id`

(required) Unique IngressGatewayRouteTable identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MESH Function

Gets a Mesh by identifier.

Syntax
```

```

Parameters

Parameter Description

`mesh_id`

(required) Unique Mesh identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROXY_DETAILS Function

Returns the attributes of the Proxy such as proxy image version.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIRTUAL_DEPLOYMENT Function

Gets a VirtualDeployment by identifier.

Syntax
```

```

Parameters

Parameter Description

`virtual_deployment_id`

(required) Unique VirtualDeployment identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIRTUAL_SERVICE Function

Gets a VirtualService by identifier.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_id`

(required) Unique VirtualService identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIRTUAL_SERVICE_ROUTE_TABLE Function

Gets a VirtualServiceRouteTable by identifier.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_route_table_id`

(required) Unique VirtualServiceRouteTable identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ACCESS_POLICIES Function

Returns a list of AccessPolicy objects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.

Allowed values are: 'id', 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`mesh_id`

(optional) Unique Mesh identifier.

`id`

(optional) Unique AccessPolicy identifier.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INGRESS_GATEWAY_ROUTE_TABLES Function

Returns a list of IngressGatewayRouteTable objects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.

Allowed values are: 'id', 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`ingress_gateway_id`

(optional) Unique IngressGateway identifier.

`id`

(optional) Unique IngressGatewayRouteTable identifier.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INGRESS_GATEWAYS Function

Returns a list of IngressGateway objects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.

Allowed values are: 'id', 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`mesh_id`

(optional) Unique Mesh identifier.

`id`

(optional) Unique IngressGateway identifier.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MESHES Function

Returns a list of Mesh objects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire displayName given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'id', 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`id`

(optional) Unique Mesh identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_DEPLOYMENTS Function

Returns a list of VirtualDeployments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.

Allowed values are: 'id', 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`virtual_service_id`

(optional) Unique VirtualService identifier.

`id`

(optional) Unique VirtualDeployment identifier.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_SERVICE_ROUTE_TABLES Function

Returns a list of VirtualServiceRouteTable objects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.

Allowed values are: 'id', 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`virtual_service_id`

(optional) Unique VirtualService identifier.

`id`

(optional) Unique VirtualServiceRouteTable identifier.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_SERVICES Function

Returns a list of VirtualService objects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`name`

(optional) A filter to return only resources that match the entire name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.

Allowed values are: 'id', 'timeCreated', 'name'

`opc_request_id`

(optional) The client request ID for tracing.

`mesh_id`

(optional) Unique Mesh identifier.

`id`

(optional) Unique VirtualService identifier.

`lifecycle_state`

(optional) A filter to return only resources that match the life cycle state given.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.

Allowed values are: 'timestamp'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timestamp is descending.

Allowed values are: 'timestamp'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`work_request_id`

(optional) The ID of the asynchronous work request.

`resource_id`

(optional) A filter to return work requests that match the given resourceId.

`operation_status`

(optional) A filter to return only resources that match the operation status given.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'WAITING', 'NEEDS_ATTENTION', 'CANCELING', 'CANCELED'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ACCESS_POLICY Function

Updates the AccessPolicy.

Syntax
```

```

Parameters

Parameter Description

`access_policy_id`

(required) Unique AccessPolicy identifier.

`update_access_policy_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INGRESS_GATEWAY Function

Updates the IngressGateway.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_id`

(required) Unique IngressGateway identifier.

`update_ingress_gateway_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INGRESS_GATEWAY_ROUTE_TABLE Function

Updates the IngressGatewayRouteTable.

Syntax
```

```

Parameters

Parameter Description

`ingress_gateway_route_table_id`

(required) Unique IngressGatewayRouteTable identifier.

`update_ingress_gateway_route_table_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MESH Function

Updates the Mesh.

Syntax
```

```

Parameters

Parameter Description

`mesh_id`

(required) Unique Mesh identifier.

`update_mesh_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VIRTUAL_DEPLOYMENT Function

Updates the VirtualDeployment.

Syntax
```

```

Parameters

Parameter Description

`virtual_deployment_id`

(required) Unique VirtualDeployment identifier.

`update_virtual_deployment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VIRTUAL_SERVICE Function

Updates the VirtualService.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_id`

(required) Unique VirtualService identifier.

`update_virtual_service_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VIRTUAL_SERVICE_ROUTE_TABLE Function

Updates the VirtualServiceRouteTable.

Syntax
```

```

Parameters

Parameter Description

`virtual_service_route_table_id`

(required) Unique VirtualServiceRouteTable identifier.

`update_virtual_service_route_table_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://servicemesh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Service Mesh Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-96C24E86-2646-4A56-8CC5-1F3B2D091E7F)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-AF596225-8B45-4D93-9CF6-B2C926926981)
- [CHANGE_ACCESS_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-A209FC01-B6E4-4C0B-BD11-87E21506C646)
- [CHANGE_INGRESS_GATEWAY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-618DCE78-E87D-4154-9689-49DDFAAC542D)
- [CHANGE_INGRESS_GATEWAY_ROUTE_TABLE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-C51A7F9B-C289-40C5-8C89-5EB223E5A0D2)
- [CHANGE_MESH_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-C9C4059E-9B5E-4753-B304-4439EE38CB50)
- [CHANGE_VIRTUAL_DEPLOYMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-BDEC3E38-E598-434F-9CA4-1D950161E6C9)
- [CHANGE_VIRTUAL_SERVICE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-E8E6E394-EDE4-4B75-A549-04DC65BBF858)
- [CHANGE_VIRTUAL_SERVICE_ROUTE_TABLE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-3F9046BE-E605-4859-9539-A0797C345C2D)
- [CREATE_ACCESS_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-9B9D4E94-F20B-45E0-AF33-843D32F6623E)
- [CREATE_INGRESS_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-646A8F4C-4568-44EA-BDEE-E2151E600043)
- [CREATE_INGRESS_GATEWAY_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-403C2CC9-FC65-4C1E-BE87-AEBC9D196648)
- [CREATE_MESH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-EE36BA65-F1E2-4092-B84A-F3B5E05E6FB7)
- [CREATE_VIRTUAL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-AF91D603-9C47-43C4-A9DF-A507E1D01CE3)
- [CREATE_VIRTUAL_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-110005A1-B144-4088-911C-26023593C431)
- [CREATE_VIRTUAL_SERVICE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-A7F24CCB-1E51-4A1E-8D81-703AA1B8A0A1)
- [DELETE_ACCESS_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-82389A32-F58E-4CE9-ABE9-DD5F463842D6)
- [DELETE_INGRESS_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-297DA4AA-B760-43DF-9243-A8CCF7647932)
- [DELETE_INGRESS_GATEWAY_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-05F0B566-C3A3-4786-90AC-935864745A23)
- [DELETE_MESH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-2C4FB1F3-FBD4-4877-B7E1-1EAC61AB65F1)
- [DELETE_VIRTUAL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-16701864-8276-4B1A-80FA-39D5594EE031)
- [DELETE_VIRTUAL_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-F1E8587A-0C5F-457A-BF90-94B04DE77981)
- [DELETE_VIRTUAL_SERVICE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-1B8B7F8D-EE95-41F9-A387-0879A4A51ECC)
- [GET_ACCESS_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-C0E04729-3DE4-4624-8FA8-FFBCA12B00E2)
- [GET_INGRESS_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-28601DD7-C066-48F9-A2A0-F53AB4296916)
- [GET_INGRESS_GATEWAY_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-A6C6C53F-124B-4BC0-883C-907B6E0DB0BB)
- [GET_MESH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-0E6D63FE-C89E-4402-B377-E0F58942D034)
- [GET_PROXY_DETAILS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-B772CF0C-44D8-4F14-849C-6CD13CCF8CFF)
- [GET_VIRTUAL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-06300C0D-B9B4-4D53-8F44-D757B826F3E5)
- [GET_VIRTUAL_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-0752409F-42DF-4917-98A6-15DE988B3B8B)
- [GET_VIRTUAL_SERVICE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-C9B6446C-749F-4D5F-B307-109AB1D63A6B)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-D92FD829-7AA0-422B-AC23-8D94BCF4EAE6)
- [LIST_ACCESS_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-BA15B063-DCD7-4606-977B-DFAFA056CEFC)
- [LIST_INGRESS_GATEWAY_ROUTE_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-72492B01-E106-4621-9DDF-57CC1D68AFC7)
- [LIST_INGRESS_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-2EC58C9B-B839-4F22-BF7A-AE8B580EC1CB)
- [LIST_MESHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-6A79EACD-1861-4BC4-8E4D-D32C79BEBFE1)
- [LIST_VIRTUAL_DEPLOYMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-1F409604-B65F-4473-82D3-0479B930A261)
- [LIST_VIRTUAL_SERVICE_ROUTE_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-21134C8C-ABD7-4A1F-82A9-8891392BCD55)
- [LIST_VIRTUAL_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-9A6BF9BD-0B39-422F-9BDC-A9013113A556)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-03044733-3128-4654-9E4D-410FA5AA1408)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-807852E4-A3DD-4BF2-ACCB-EB183A621A9C)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-204AD972-D966-4326-8E00-B007ED35EE54)
- [UPDATE_ACCESS_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-12E38FD5-8CA3-4ED6-BCE9-53CC29FBC9D4)
- [UPDATE_INGRESS_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-F4057B94-F9AC-4CAA-B0C6-12A1E8D6292E)
- [UPDATE_INGRESS_GATEWAY_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-3A0BFD7C-AF16-47F4-A5BD-87A8FE7E507E)
- [UPDATE_MESH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-81766492-A7A3-4F9A-A25F-E279BB52665C)
- [UPDATE_VIRTUAL_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-B0835A27-FBB5-4765-8AA6-7C82DB89C390)
- [UPDATE_VIRTUAL_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-FC18554B-86B2-48EE-A249-E1ADB3AE3328)
- [UPDATE_VIRTUAL_SERVICE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_svm_service_mesh.html#ADSDK-GUID-4FB1A650-390C-4AF1-B16D-1785F67A2141)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
