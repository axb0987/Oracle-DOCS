# Load Balancer Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#dcoc-content-body)

## Load Balancer Functions

Package: DBMS_CLOUD_OCI_LB_LOAD_BALANCER

### CHANGE_LOAD_BALANCER_COMPARTMENT Function

Moves a load balancer into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to move.

`change_load_balancer_compartment_details`

(required) The configuration details for moving a load balancer to a different compartment.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BACKEND Function

Adds a backend server to a backend set.

Syntax
```

```

Parameters

Parameter Description

`create_backend_details`

(required) The details to add a backend server to a backend set.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set and servers.

`backend_set_name`

(required) The name of the backend set to add the backend server to. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BACKEND_SET Function

Adds a backend set to a load balancer.

Syntax
```

```

Parameters

Parameter Description

`create_backend_set_details`

(required) The details for adding a backend set.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer on which to add a backend set.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CERTIFICATE Function

Creates an asynchronous request to add an SSL certificate bundle.

Syntax
```

```

Parameters

Parameter Description

`create_certificate_details`

(required) The details of the certificate bundle to add.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer on which to add the certificate bundle.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_HOSTNAME Function

Adds a hostname resource to the specified load balancer. For more information, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

Syntax
```

```

Parameters

Parameter Description

`create_hostname_details`

(required) The details of the hostname resource to add to the specified load balancer.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to add the hostname to.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LISTENER Function

Adds a listener to a load balancer.

Syntax
```

```

Parameters

Parameter Description

`create_listener_details`

(required) Details to add a listener.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer on which to add a listener.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LOAD_BALANCER Function

Creates a new load balancer in the specified compartment. For general information about load balancers, see[Overview of the Load Balancing Service](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm). For the purposes of access control, you must provide the OCID of the compartment where you want the load balancer to reside. Notice that the load balancer doesn't have to be in the same compartment as the VCN or backend set. If you're not sure which compartment to use, put the load balancer in the same compartment as the VCN. For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). You must specify a display name for the load balancer. It does not have to be unique, and you can change it. For information about Availability Domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. All Oracle Cloud Infrastructure resources, including load balancers, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. Fore more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). After you send your request, the new object's state will temporarily be PROVISIONING. Before using the object, first make sure its state has changed to RUNNING. When you create a load balancer, the system assigns an IP address. To get the IP address, use the`GET_LOAD_BALANCER`Function operation.

Syntax
```

```

Parameters

Parameter Description

`create_load_balancer_details`

(required) The configuration details for creating a load balancer.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PATH_ROUTE_SET Function

Adds a path route set to a load balancer. For more information, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

Syntax
```

```

Parameters

Parameter Description

`create_path_route_set_details`

(required) The details of the path route set to add.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to add the path route set to.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ROUTING_POLICY Function

Adds a routing policy to a load balancer. For more information, see[Managing Request Routing](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

Syntax
```

```

Parameters

Parameter Description

`create_routing_policy_details`

(required) The details of the routing policy rules to add.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to add the routing policy rule list to.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_RULE_SET Function

Creates a new rule set associated with the specified load balancer. For more information, see[Managing Rule Sets](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm).

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`create_rule_set_details`

(required) The configuration details for the rule set to create.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SSL_CIPHER_SUITE Function

Creates a custom SSL cipher suite.

Syntax
```

```

Parameters

Parameter Description

`create_ssl_cipher_suite_details`

(required) The details of the SSL cipher suite to add.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated load balancer.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BACKEND Function

Removes a backend server from a given load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set and server.

`backend_set_name`

(required) The name of the backend set associated with the backend server. Example: `example_backend_set`

`backend_name`

(required) The IP address and port of the backend server to remove. Example: `10.0.0.3:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BACKEND_SET Function

Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the load balancer. Before you can delete a backend set, you must remove it from any active listeners.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set.

`backend_set_name`

(required) The name of the backend set to delete. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CERTIFICATE Function

Deletes an SSL certificate bundle from a load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the certificate bundle to be deleted.

`certificate_name`

(required) The name of the certificate bundle to delete. Example: `example_certificate_bundle`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_HOSTNAME Function

Deletes a hostname resource from the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the hostname to delete.

`name`

(required) The name of the hostname resource to delete. Example: `example_hostname_001`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LISTENER Function

Deletes a listener from a load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the listener to delete.

`listener_name`

(required) The name of the listener to delete. Example: `example_listener`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LOAD_BALANCER Function

Stops a load balancer and removes it from service.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to delete.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PATH_ROUTE_SET Function

Deletes a path route set from the specified load balancer. To delete a path route rule from a path route set, use the`UPDATE_PATH_ROUTE_SET`Function operation.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the path route set to delete.

`path_route_set_name`

(required) The name of the path route set to delete. Example: `example_path_route_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ROUTING_POLICY Function

Deletes a routing policy from the specified load balancer. To delete a routing rule from a routing policy, use the`UPDATE_ROUTING_POLICY`Function operation.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the routing policy to delete.

`routing_policy_name`

(required) The name of the routing policy to delete. Example: `example_routing_policy`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RULE_SET Function

Deletes a rule set from the specified load balancer. To delete a rule from a rule set, use the`UPDATE_RULE_SET`Function operation.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`rule_set_name`

(required) The name of the rule set to delete. Example: `example_rule_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SSL_CIPHER_SUITE Function

Deletes an SSL cipher suite from a load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated load balancer.

`name`

(required) The name of the SSL cipher suite to delete. example: `example_cipher_suite`

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND Function

Gets the specified backend server's configuration information.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set and server.

`backend_set_name`

(required) The name of the backend set that includes the backend server. Example: `example_backend_set`

`backend_name`

(required) The IP address and port of the backend server to retrieve. Example: `10.0.0.3:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND_HEALTH Function

Gets the current health status of the specified backend server.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend server health status to be retrieved.

`backend_set_name`

(required) The name of the backend set associated with the backend server to retrieve the health status for. Example: `example_backend_set`

`backend_name`

(required) The IP address and port of the backend server to retrieve the health status for. Example: `10.0.0.3:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND_SET Function

Gets the specified backend set's configuration information.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`backend_set_name`

(required) The name of the backend set to retrieve. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKEND_SET_HEALTH Function

Gets the health status for the specified backend set.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set health status to be retrieved.

`backend_set_name`

(required) The name of the backend set to retrieve the health status for. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HEALTH_CHECKER Function

Gets the health check policy information for a given load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the health check policy to be retrieved.

`backend_set_name`

(required) The name of the backend set associated with the health check policy to be retrieved. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HOSTNAME Function

Gets the specified hostname resource's configuration information.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`name`

(required) The name of the hostname resource to retrieve. Example: `example_hostname_001`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOAD_BALANCER Function

Gets the specified load balancer's configuration information.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOAD_BALANCER_HEALTH Function

Gets the health status for the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to return health status for.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PATH_ROUTE_SET Function

Gets the specified path route set's configuration information.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`path_route_set_name`

(required) The name of the path route set to retrieve. Example: `example_path_route_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROUTING_POLICY Function

Gets the specified routing policy.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`routing_policy_name`

(required) The name of the routing policy to retrieve. Example: `example_routing_policy`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RULE_SET Function

Gets the specified set of rules.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`rule_set_name`

(required) The name of the rule set to retrieve. Example: `example_rule_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SSL_CIPHER_SUITE Function

Gets the specified SSL cipher suite's configuration information.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated load balancer.

`name`

(required) The name of the SSL cipher suite to retrieve. example: `example_cipher_suite`

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the details of a work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BACKEND_SETS Function

Lists all backend sets associated with a given load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend sets to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BACKENDS Function

Lists the backend servers for a given load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set and servers.

`backend_set_name`

(required) The name of the backend set associated with the backend servers. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CERTIFICATES Function

Lists all SSL certificates bundles associated with a given load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the certificate bundles to be listed.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HOSTNAMES Function

Lists all hostname resources associated with the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the hostnames to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LISTENER_RULES Function

Lists all of the rules from all of the rule sets associated with the specified listener. The response organizes the rules in the following order: * Access control rules * Allow method rules * Request header rules * Response header rules

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the listener.

`listener_name`

(required) The name of the listener the rules are associated with.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOAD_BALANCER_HEALTHS Function

Lists the summary health statuses for all load balancers in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancers to return health status information for.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOAD_BALANCERS Function

Lists all load balancers in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancers to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`detail`

(optional) The level of detail to return for each result. Can be `full` or `simple`. Example: `full`

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the given display name exactly. Example: `example_load_balancer`

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state. Example: `SUCCEEDED`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PATH_ROUTE_SETS Function

Lists all path route sets associated with the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the path route sets to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_POLICIES Function

Lists the available load balancer policies.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancer policies to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROTOCOLS Function

Lists all supported traffic protocols.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancer protocols to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROUTING_POLICIES Function

Lists all routing policies associated with the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the routing policies.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RULE_SETS Function

Lists all rule sets associated with the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SSL_CIPHER_SUITES Function

Lists all SSL cipher suites associated with the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated load balancer.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SHAPES Function

Lists the valid load balancer shapes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the load balancer shapes to list.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests for a given load balancer.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the work requests to retrieve.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BACKEND Function

Updates the configuration of a backend server within the specified backend set.

Syntax
```

```

Parameters

Parameter Description

`update_backend_details`

(required) Details for updating a backend server.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set and server.

`backend_set_name`

(required) The name of the backend set associated with the backend server. Example: `example_backend_set`

`backend_name`

(required) The IP address and port of the backend server to update. Example: `10.0.0.3:8080`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BACKEND_SET Function

Updates a backend set.

Syntax
```

```

Parameters

Parameter Description

`update_backend_set_details`

(required) The details to update a backend set.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the backend set.

`backend_set_name`

(required) The name of the backend set to update. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HEALTH_CHECKER Function

Updates the health check policy for a given load balancer and backend set.

Syntax
```

```

Parameters

Parameter Description

`health_checker`

(required) The health check policy configuration details.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the health check policy to be updated.

`backend_set_name`

(required) The name of the backend set associated with the health check policy to be retrieved. Example: `example_backend_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HOSTNAME Function

Overwrites an existing hostname resource on the specified load balancer. Use this operation to change a virtual hostname.

Syntax
```

```

Parameters

Parameter Description

`update_hostname_details`

(required) The configuration details to update a virtual hostname.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the virtual hostname to update.

`name`

(required) The name of the hostname resource to update. Example: `example_hostname_001`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LISTENER Function

Updates a listener for a given load balancer.

Syntax
```

```

Parameters

Parameter Description

`update_listener_details`

(required) Details to update a listener.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the listener to update.

`listener_name`

(required) The name of the listener to update. Example: `example_listener`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOAD_BALANCER Function

Updates a load balancer's configuration.

Syntax
```

```

Parameters

Parameter Description

`update_load_balancer_details`

(required) The details for updating a load balancer's configuration.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to update.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOAD_BALANCER_SHAPE Function

Update the shape of a load balancer. The new shape can be larger or smaller compared to existing shape of the LB. The service will try to perform this operation in the least disruptive way to existing connections, but there is a possibility that they might be lost during the LB resizing process. The new shape becomes effective as soon as the related work request completes successfully, i.e. when reshaping to a larger shape, the LB will start accepting larger bandwidth and when reshaping to a smaller one, the LB will be accepting smaller bandwidth.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer whose shape will be updated.

`update_load_balancer_shape_details`

(required) The details for updating a load balancer's shape. This contains the new, desired shape.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_SECURITY_GROUPS Function

Updates the network security groups associated with the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`update_network_security_groups_details`

(required) The details for updating the NSGs associated with the specified load balancer.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer to update the NSGs for.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PATH_ROUTE_SET Function

Overwrites an existing path route set on the specified load balancer. Use this operation to add, delete, or alter path route rules in a path route set. To add a new path route rule to a path route set, the `pathRoutes` in the`UPDATE_PATH_ROUTE_SET_DETAILS`Function object must include both the new path route rule to add and the existing path route rules to retain.

Syntax
```

```

Parameters

Parameter Description

`update_path_route_set_details`

(required) The configuration details to update a path route set.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the path route set to update.

`path_route_set_name`

(required) The name of the path route set to update. Example: `example_path_route_set`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ROUTING_POLICY Function

Overwrites an existing routing policy on the specified load balancer. Use this operation to add, delete, or alter routing policy rules in a routing policy. To add a new routing rule to a routing policy, the body must include both the new routing rule to add and the existing rules to retain.

Syntax
```

```

Parameters

Parameter Description

`update_routing_policy_details`

(required) The configuration details needed to update a routing policy.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the load balancer associated with the routing policy to update.

`routing_policy_name`

(required) The name of the routing policy to update. Example: `example_routing_policy_name`

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RULE_SET Function

Overwrites an existing set of rules on the specified load balancer. Use this operation to add or alter the rules in a rule set. To add a new rule to a set, the body must include both the new rule to add and the existing rules to retain.

Syntax
```

```

Parameters

Parameter Description

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the specified load balancer.

`rule_set_name`

(required) The name of the rule set to update. Example: `example_rule_set`

`update_rule_set_details`

(required) The configuration details to update a set of rules.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SSL_CIPHER_SUITE Function

Updates an existing SSL cipher suite for the specified load balancer.

Syntax
```

```

Parameters

Parameter Description

`update_ssl_cipher_suite_details`

(required) The configuration details to update an SSL cipher suite.

`load_balancer_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated load balancer.

`name`

(required) The name of the SSL cipher suite to update. example: `example_cipher_suite`

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the ETag for the load balancer. This value can be obtained from a GET or POST response for any resource of that load balancer. For example, the eTag returned by getListener can be specified as the ifMatch for updateRuleSets. The resource is updated or deleted only if the ETag you provide matches the resource's current ETag value. Example: `example-etag`

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Load Balancer Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-05085C79-96CB-4F46-BEEA-F593E409C4EA)
- [CHANGE_LOAD_BALANCER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-B68AD3A6-A576-4041-A1CD-E9E9E749627B)
- [CREATE_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-1ED471F9-A92A-4652-9027-179A5B5957DD)
- [CREATE_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-36728938-22AB-4E5D-AA83-372824A7E973)
- [CREATE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-77A2C540-543D-45D5-A560-9B56615423AA)
- [CREATE_HOSTNAME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-2C2033EB-6533-47B5-B455-9EF432A8E6EE)
- [CREATE_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-1DCE3362-C961-4476-9171-6AB94DFF2EF9)
- [CREATE_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-4F27C80F-8DA3-4225-93BE-3B9C7829B41B)
- [CREATE_PATH_ROUTE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-B4FEED66-6768-4338-8D02-8739895038B3)
- [CREATE_ROUTING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-5FAD0370-A686-45B4-B26E-C0F207820D32)
- [CREATE_RULE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-D9517004-2D5E-456D-B1D0-9707065BF379)
- [CREATE_SSL_CIPHER_SUITE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-32F461A5-A538-4E83-BDE7-9E6BBE66C32F)
- [DELETE_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-5296F11D-EA9D-4761-9E6E-639DF557DF06)
- [DELETE_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-86B59876-2542-4D7C-945A-7C99DED381AA)
- [DELETE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-477E5237-9C81-4342-9CBA-8A58EBF391E8)
- [DELETE_HOSTNAME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-7C1BAAD3-6817-4CD9-929A-06775BDA963C)
- [DELETE_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-75E2A045-FC8D-427F-A087-2C8EF16B6868)
- [DELETE_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-6DE41077-4D29-4D8D-A57E-0548559884A5)
- [DELETE_PATH_ROUTE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-5D3B884F-310F-40CB-B35E-75FBA9F2B394)
- [DELETE_ROUTING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-1595AD1C-6A4B-4219-B5B7-7005515C54E0)
- [DELETE_RULE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-0107BC9E-DC11-4050-BA38-D55D288D79AB)
- [DELETE_SSL_CIPHER_SUITE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-F65475DC-C037-4C24-BF30-EA1BF0ADF25C)
- [GET_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-082CEEFB-A9CB-47C2-B53B-5303E7EB1552)
- [GET_BACKEND_HEALTH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-9670DA19-9F52-4AFF-839C-55F0F9AE1E2D)
- [GET_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-6D0C8389-8B93-4C58-9227-72B87AB6F181)
- [GET_BACKEND_SET_HEALTH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-04734179-1052-4D70-9351-2C6CD4619663)
- [GET_HEALTH_CHECKER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-2C170E70-D5CF-49BE-AA92-172ED85FF9C3)
- [GET_HOSTNAME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-7516AFCC-1789-495A-8AF3-7A31307B5D4E)
- [GET_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-DEB69746-C935-43FE-B49C-E39D5ABC2A43)
- [GET_LOAD_BALANCER_HEALTH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-8AFA9914-AAFC-438F-81E3-A5D3FB80C0D0)
- [GET_PATH_ROUTE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-F4BC777E-B0D7-471C-9F49-C5D419974AB0)
- [GET_ROUTING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-6FF5B4B1-0AB5-48FA-9F50-6867519EBA75)
- [GET_RULE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-84027D82-07B3-41BE-AEBE-06C7412E5C89)
- [GET_SSL_CIPHER_SUITE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-D776EE4B-A723-45C4-BFA7-8A5530D60677)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-3EF90470-2D64-4E4F-B02D-FF6BAC084C3F)
- [LIST_BACKEND_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-62FD6A55-0C6F-4452-BE2C-50EA27F19273)
- [LIST_BACKENDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-8B9E127D-E187-4802-8C58-DEFE94764145)
- [LIST_CERTIFICATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-F28D93A2-795A-4402-B6C9-632EEBB09393)
- [LIST_HOSTNAMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-E4BADDFB-6C84-4D91-A635-3AB37F2C69E8)
- [LIST_LISTENER_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-F9904A01-4C4D-4452-A867-6BBEDC2237A3)
- [LIST_LOAD_BALANCER_HEALTHS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-48FDDC24-2DE1-4E9C-9DD2-8B507DC69F07)
- [LIST_LOAD_BALANCERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-BF589B41-22C1-4A15-A70B-E2783BDCFF69)
- [LIST_PATH_ROUTE_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-EF814132-5319-40BC-A8A1-8AEB593C7D6D)
- [LIST_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-3E4BB35B-E7BD-4C02-9A79-249CC12AAEA7)
- [LIST_PROTOCOLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-16103C31-81DD-4D08-AF1C-FF0ECD6AB59A)
- [LIST_ROUTING_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-C0C3F5B6-90B1-4381-B87A-C47F9BF62935)
- [LIST_RULE_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-8B96D158-8DA1-4F6F-BBA1-3286DDDDFC04)
- [LIST_SSL_CIPHER_SUITES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-B1FA3A4C-DB31-402A-8741-9B2A1193371E)
- [LIST_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-B727DF93-D963-4A93-A983-063952360812)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-D9B2394E-8CFA-422F-8357-BAF390D2160D)
- [UPDATE_BACKEND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-DBACCC13-8255-4288-8D9E-3BA254500F81)
- [UPDATE_BACKEND_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-77CBE725-798F-4D1A-A40E-69CE90DCB42C)
- [UPDATE_HEALTH_CHECKER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-3AD209E8-2A4D-42B6-AF9A-EC476411D79E)
- [UPDATE_HOSTNAME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-3570D1FD-0B0B-41EF-A631-B0F1C19A37EC)
- [UPDATE_LISTENER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-2D4824D3-CB0F-4B98-B85B-4295568F2F8F)
- [UPDATE_LOAD_BALANCER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-65CC486C-9162-4A3A-87CF-463FA2CC9D6F)
- [UPDATE_LOAD_BALANCER_SHAPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-05E9E9A3-CA4E-4244-9C7A-6C74EB4D1E67)
- [UPDATE_NETWORK_SECURITY_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-5AC84DF7-4DD1-4B67-A433-27AC2ED27DFE)
- [UPDATE_PATH_ROUTE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-AA19131B-5502-42C1-AEE1-E13117AD3062)
- [UPDATE_ROUTING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-7A2679F9-E4CE-4681-9F2B-422B5A6C48AD)
- [UPDATE_RULE_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-153510FC-E7FF-4D56-9298-037C95D38472)
- [UPDATE_SSL_CIPHER_SUITE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lb_load_balancer.html#ADSDK-GUID-650E1E10-A3A9-46A4-BC92-AA89C52FEEE2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
