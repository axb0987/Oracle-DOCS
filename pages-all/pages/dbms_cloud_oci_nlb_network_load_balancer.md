# Network Load Balancer Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#dcoc-content-body)

## Network Load Balancer Functions

Package: DBMS_CLOUD_OCI_NLB_NETWORK_LOAD_BALANCER

### CHANGE_NETWORK_LOAD_BALANCER_COMPARTMENT Function

Moves a network load balancer into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`change_network_load_balancer_compartment_details`

(required) The configuration details for moving a network load balancer to a different compartment.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BACKEND Function

Adds a backend server to a backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`create_backend_details`

(required) The details to add a backend server to a backend set.

`backend_set_name`

(required) The name of the backend set to which to add the backend server. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BACKEND_SET Function

Adds a backend set to a network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`create_backend_set_details`

(required) The details for adding a backend set.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTENER Function

Adds a listener to a network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`create_listener_details`

(required) Details to add a listener.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NETWORK_LOAD_BALANCER Function

Creates a network load balancer.

Syntax
```

```

Parameters

Parameter Description

`create_network_load_balancer_details`

(required) Details for the new network load balancer.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BACKEND Function

Removes a backend server from a given network load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set associated with the backend server. Example: `example_backend_set`

`backend_name`

(required) The name of the backend server to remove. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as &lt;ipAddress&gt;:&lt;port&gt;. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as &lt;targetId&gt;:&lt;port&gt;. Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BACKEND_SET Function

Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the network load balancer. Before you can delete a backend set, you must remove it from any active listeners.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set to delete. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTENER Function

Deletes a listener from a network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`listener_name`

(required) The name of the listener to delete. Example: `example_listener`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NETWORK_LOAD_BALANCER Function

Deletes a network load balancer resource by identifier.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND Function

Retrieves the configuration information for the specified backend server.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set that includes the backend server. Example: `example_backend_set`

`backend_name`

(required) The name of the backend server to retrieve. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as &lt;ipAddress&gt;:&lt;port&gt;. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as &lt;targetId&gt;:&lt;port&gt;. Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND_HEALTH Function

Retrieves the current health status of the specified backend server.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set associated with the backend server for which to retrieve the health status. Example: `example_backend_set`

`backend_name`

(required) The name of the backend server to retrieve health status for. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as &lt;ipAddress&gt;:&lt;port&gt;. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as &lt;targetId&gt;:&lt;port&gt;. Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND_SET Function

Retrieves the configuration information for the specified backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set to retrieve. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND_SET_HEALTH Function

Retrieves the health status for the specified backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set for which to retrieve the health status. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HEALTH_CHECKER Function

Retrieves the health check policy information for a given network load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set associated with the health check policy to be retrieved. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LISTENER Function

Retrieves listener properties associated with a given network load balancer and listener name.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`listener_name`

(required) The name of the listener to get. Example: `example_listener`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORK_LOAD_BALANCER Function

Retrieves network load balancer configuration information by identifier.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORK_LOAD_BALANCER_HEALTH Function

Retrieves the health status for the specified network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Retrieves the details of the work request with the given identifier.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The identifier of the asynchronous request.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BACKEND_SETS Function

Lists all backend sets associated with a given network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BACKENDS Function

Lists the backend servers for a given network load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`backend_set_name`

(required) The name of the backend set associated with the backend servers. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTENERS Function

Lists all listeners associated with a given network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`if_none_match`

(optional) The system returns the requested resource, with a 200 status, only if the resource has no etag matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the HTTP status code `304 (Not Modified)`. Example: `example-etag`

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_LOAD_BALANCER_HEALTHS Function

Lists the summary health statuses for all network load balancers in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancers to list.

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_LOAD_BALANCERS Function

Returns a list of network load balancers.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancers to list.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_LOAD_BALANCERS_POLICIES Function

Lists the available network load balancer policies.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS Function

This API has been deprecated so it won't return the updated list of supported protocls. Lists all supported traffic protocols.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either 'asc' (ascending) or 'desc' (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending. The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The identifier of the asynchronous request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancers to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Returns a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The identifier of the asynchronous request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancers to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists all work requests.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the network load balancers to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`limit`

(optional) For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) The page token representing the page from which to start retrieving results. For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BACKEND Function

Updates the configuration of a backend server within the specified backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`update_backend_details`

(required) Details for updating a backend server.

`backend_set_name`

(required) The name of the backend set associated with the backend server. Example: `example_backend_set`

`backend_name`

(required) The name of the backend server to update. If the backend was created with an explicitly specified name, that name should be used here. If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as &lt;ipAddress&gt;:&lt;port&gt;. If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as &lt;targetId&gt;:&lt;port&gt;. Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BACKEND_SET Function

Updates a backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`update_backend_set_details`

(required) The details to update a backend set.

`backend_set_name`

(required) The name of the backend set to update. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HEALTH_CHECKER Function

Updates the health check policy for a given network load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`update_health_checker_details`

(required) The health check policy configuration details.

`backend_set_name`

(required) The name of the backend set associated with the health check policy to be retrieved. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTENER Function

Updates a listener for a given network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`update_listener_details`

(required) Details to update a listener.

`listener_name`

(required) The name of the listener to update. Example: `example_listener`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_LOAD_BALANCER Function

Updates the network load balancer

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`update_network_load_balancer_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_SECURITY_GROUPS Function

Updates the network security groups associated with the specified network load balancer.

Syntax
```

```

Parameters

Parameter Description

`network_load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network load balancer to update.

`update_network_security_groups_details`

(required) The details for updating the network security groups associated with the specified network load balancer.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you must contact Oracle about a particular request, then provide the request identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that it can be retried in case of a timeout or server error without risk of rerunning that same action. Retry tokens expire after 24 hours but they can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the current etag value of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://network-load-balancer-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Network Load Balancer Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-8B269B99-8D1E-4ADB-B929-D054759D52D6)
- [CHANGE_NETWORK_LOAD_BALANCER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-0EDE241D-565D-4E3D-9FB5-16B370691CAC)
- [CREATE_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-848B7E23-416C-4F6F-9C82-6FA25F38585B)
- [CREATE_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-DA3EF399-E815-48D3-AC61-EAB1E7256985)
- [CREATE_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-AA82BAAF-9AFC-484E-AC76-608718EAE8E1)
- [CREATE_NETWORK_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-831D3257-3F6A-4B72-A7E6-D7CFA09DCAD8)
- [DELETE_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-F6814E0D-9F30-4358-9EA2-97822C96E8DB)
- [DELETE_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-5645403B-CAB0-4557-BAD5-C2AAE401E179)
- [DELETE_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-16A702BC-0860-4C59-AB25-006225A63F0B)
- [DELETE_NETWORK_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-68C757F1-87C2-4917-8DCB-F0CA922C1685)
- [GET_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-B3AA410B-B6BF-4CE5-808D-567506606BF6)
- [GET_BACKEND_HEALTH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-7FAB75F0-E3A2-4B1D-9E33-BEED600EDD4A)
- [GET_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-214A80C0-593E-4165-968C-E39D2533C870)
- [GET_BACKEND_SET_HEALTH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-27411B59-8AD0-42C3-BEA4-BDF93E8E0004)
- [GET_HEALTH_CHECKER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-6DD8A01A-6ABF-4FB0-A01D-72C684AE16C0)
- [GET_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-276F5C30-66DB-4CF9-98F1-F95C5438FCE7)
- [GET_NETWORK_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-118FE58F-3F71-48AE-9251-4101B277351B)
- [GET_NETWORK_LOAD_BALANCER_HEALTH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-02B128F7-B195-41AF-8582-B9638C969E33)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-178290AA-D0CE-4328-B701-F0267AE018C9)
- [LIST_BACKEND_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-F7C52642-D520-40D5-AB6D-2699453801E5)
- [LIST_BACKENDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-2EC02D84-0A8A-4755-83C8-B3E503B0CFCF)
- [LIST_LISTENERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-6AC41E6D-833B-46F7-87BC-24A9A7CA389F)
- [LIST_NETWORK_LOAD_BALANCER_HEALTHS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-9CFAE617-B93F-432B-8561-B256622B8DA3)
- [LIST_NETWORK_LOAD_BALANCERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-12BF5645-2AAC-4FAE-A97F-FA4B56C00E41)
- [LIST_NETWORK_LOAD_BALANCERS_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-B125DBC2-4D9D-4E7F-8A40-609CE3CCC0E8)
- [LIST_NETWORK_LOAD_BALANCERS_PROTOCOLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-25AD9359-E0C2-4C4E-AA1C-D20C1C0A3331)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-88FD2867-487A-44DD-B8CE-563193EBB8E5)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-C76BFBAC-AF03-4021-B525-4520DA21F55D)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-9DFDC01E-1036-43FA-8880-B63BFD0838D5)
- [UPDATE_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-7C0490C5-A73D-4CFB-8423-A543071B50B8)
- [UPDATE_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-512DD29E-8EA5-4DBB-A345-1C235AEF9579)
- [UPDATE_HEALTH_CHECKER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-F10CBA3E-CF3B-4D13-99CC-E7A281C96389)
- [UPDATE_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-313CB1D9-42C4-4BCA-B6C8-2A912DB73AAD)
- [UPDATE_NETWORK_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-54819BB4-9784-4D71-8C3C-10A9152A6101)
- [UPDATE_NETWORK_SECURITY_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_nlb_network_load_balancer.html#ADSDK-GUID-AEFCAD73-3FB3-4D8A-BF89-D53DA7C0484C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
