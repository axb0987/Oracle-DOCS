# Core Virtual Network Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#dcoc-content-body)

## Core Virtual Network Functions

Package: DBMS_CLOUD_OCI_CR_VIRTUAL_NETWORK

### ADD_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function

Adds one or more route distribution statements to the specified route distribution.

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`add_drg_route_distribution_statements_details`

(required) Request with one or more route distribution statements to be inserted into the route distribution.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_DRG_ROUTE_RULES Function

Adds one or more static route rules to the specified DRG route table.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`add_drg_route_rules_details`

(required) Request for one or more route rules to be inserted into the DRG route table.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_IPV6_SUBNET_CIDR Function

Add an IPv6 prefix to a subnet.

Syntax
```

```

Parameters

Parameter Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`add_subnet_ipv6_cidr_details`

(required) Details object for adding an IPv6 prefix to a subnet.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_IPV6_VCN_CIDR Function

Add an IPv6 prefix to a VCN. The VCN size is always /56 and assigned by Oracle. Once added the IPv6 prefix cannot be removed or modified.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`add_vcn_ipv6_cidr_details`

(optional) Details object for adding an IPv6 VCN CIDR.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES Function

Adds one or more security rules to the specified network security group.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`add_network_security_group_security_rules_details`

(required) Request with one or more security rules to be associated with the network security group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_PUBLIC_IP_POOL_CAPACITY Function

Adds some or all of a CIDR block to a public IP pool. The CIDR block (or subrange) must not overlap with any other CIDR block already added to this or any other public IP pool.

Syntax
```

```

Parameters

Parameter Description

`public_ip_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`add_public_ip_pool_capacity_details`

(required) Byoip Range prefix and a cidr from it

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_VCN_CIDR Function

Adds a CIDR block to a VCN. The CIDR block you add: - Must be valid. - Must not overlap with another CIDR block in the VCN, a CIDR block of a peered VCN, or the on-premises network CIDR block. - Must not exceed the limit of CIDR blocks allowed per VCN. **Note:** Adding a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can take a few minutes. You can use the `GetWorkRequest` operation to check the status of the update.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`add_vcn_cidr_details`

(required) Details object for deleting a VCN CIDR.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADVERTISE_BYOIP_RANGE Function

Begins BGP route advertisements for the BYOIP CIDR block you imported to the Oracle Cloud. The `ByoipRange` resource must be in the PROVISIONED state before the BYOIP CIDR block routes can be advertised with BGP.

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_SERVICE_ID Function

Adds the specified`SERVICE`Type to the list of enabled `Service` objects for the specified gateway. You must also set up a route rule with the `cidrBlock` of the `Service` as the rule's destination and the service gateway as the rule's target. See`ROUTE_TABLE`Type. **Note:** The `AttachServiceId` operation is an easy way to add an individual `Service` to the service gateway. Compare it with`UPDATE_SERVICE_GATEWAY`Function, which replaces the entire existing list of enabled `Service` objects with the list that you provide in the `Update` call.

Syntax
```

```

Parameters

Parameter Description

`service_gateway_id`

(required) The service gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`attach_service_details`

(required) ServiceId of Service to be attached to a service gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES Function

Adds one or more customer public IP prefixes to the specified public virtual circuit. Use this operation (and not`UPDATE_VIRTUAL_CIRCUIT`Function) to add prefixes to the virtual circuit. Oracle must verify the customer's ownership of each prefix before traffic for that prefix will flow across the virtual circuit.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`bulk_add_virtual_circuit_public_prefixes_details`

(required) Request with publix prefixes to be added to the virtual circuit

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES Function

Removes one or more customer public IP prefixes from the specified public virtual circuit. Use this operation (and not`UPDATE_VIRTUAL_CIRCUIT`Function) to remove prefixes from the virtual circuit. When the virtual circuit's state switches back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`bulk_delete_virtual_circuit_public_prefixes_details`

(required) Request with public prefixes to be deleted from the virtual circuit.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_BYOIP_RANGE_COMPARTMENT Function

Moves a BYOIP CIDR block to a different compartment. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`change_byoip_range_compartment_details`

(required) Request to change the compartment of a BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CAPTURE_FILTER_COMPARTMENT Function

Moves a capture filter to a new compartment in the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`capture_filter_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the capture filter.

`change_capture_filter_compartment_details`

(required) Request to change the compartment of a VTAP.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CPE_COMPARTMENT Function

Moves a CPE object into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE.

`change_cpe_compartment_details`

(required) Request to change the compartment of a CPE.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CROSS_CONNECT_COMPARTMENT Function

Moves a cross-connect into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`change_cross_connect_compartment_details`

(required) Request to change the compartment of a Cross Connect.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CROSS_CONNECT_GROUP_COMPARTMENT Function

Moves a cross-connect group into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`cross_connect_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group.

`change_cross_connect_group_compartment_details`

(required) Request to change the compartment of a Cross Connect Group.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DHCP_OPTIONS_COMPARTMENT Function

Moves a set of DHCP options into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`dhcp_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the set of DHCP options.

`change_dhcp_options_compartment_details`

(required) Request to change the compartment of a set of DHCP Options.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DRG_COMPARTMENT Function

Moves a DRG into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`change_drg_compartment_details`

(required) Request to change the compartment of a DRG.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_IP_SEC_CONNECTION_COMPARTMENT Function

Moves an IPSec connection into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`change_ip_sec_connection_compartment_details`

(required) Request to change the compartment of a IPSec connection.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_INTERNET_GATEWAY_COMPARTMENT Function

Moves an internet gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`ig_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the internet gateway.

`change_internet_gateway_compartment_details`

(required) Request to change the compartment of an internet gateway.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LOCAL_PEERING_GATEWAY_COMPARTMENT Function

Moves a local peering gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`local_peering_gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the local peering gateway.

`change_local_peering_gateway_compartment_details`

(required) Request to change the compartment of a given local peering gateway.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_NAT_GATEWAY_COMPARTMENT Function

Moves a NAT gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`nat_gateway_id`

(required) The NAT gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`change_nat_gateway_compartment_details`

(required) Request to change the compartment of a given NAT Gateway.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_NETWORK_SECURITY_GROUP_COMPARTMENT Function

Moves a network security group into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`change_network_security_group_compartment_details`

(required) Request to change the compartment of a network security group.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PUBLIC_IP_COMPARTMENT Function

Moves a public IP into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes). This operation applies only to reserved public IPs. Ephemeral public IPs always belong to the same compartment as their VNIC and move accordingly.

Syntax
```

```

Parameters

Parameter Description

`public_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP.

`change_public_ip_compartment_details`

(required) Request to change the compartment of a Public IP.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PUBLIC_IP_POOL_COMPARTMENT Function

Moves a public IP pool to a different compartment. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`public_ip_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`change_public_ip_pool_compartment_details`

(required) Request to change the compartment of a public IP pool.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REMOTE_PEERING_CONNECTION_COMPARTMENT Function

Moves a remote peering connection (RPC) into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`remote_peering_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote peering connection (RPC).

`change_remote_peering_connection_compartment_details`

(required) Request to change the compartment of a remote peering connection.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ROUTE_TABLE_COMPARTMENT Function

Moves a route table into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`rt_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table.

`change_route_table_compartment_details`

(required) Request to change the compartment of a given route table.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SECURITY_LIST_COMPARTMENT Function

Moves a security list into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list.

`change_security_list_compartment_details`

(required) Request to change the compartment of a given security list.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SERVICE_GATEWAY_COMPARTMENT Function

Moves a service gateway into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`service_gateway_id`

(required) The service gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`change_service_gateway_compartment_details`

(required) Request to change the compartment of a given Service Gateway.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SUBNET_COMPARTMENT Function

Moves a subnet into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`change_subnet_compartment_details`

(required) Request to change the compartment of a given subnet.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VCN_COMPARTMENT Function

Moves a VCN into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`change_vcn_compartment_details`

(required) Request to change the compartment of a given VCN.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VIRTUAL_CIRCUIT_COMPARTMENT Function

Moves a virtual circuit into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`change_virtual_circuit_compartment_details`

(required) Request to change the compartment of a virtual circuit.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VLAN_COMPARTMENT Function

Moves a VLAN into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN.

`change_vlan_compartment_details`

(required) Request to change the compartment of a given VLAN.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VTAP_COMPARTMENT Function

Moves a VTAP to a new compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`vtap_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VTAP.

`change_vtap_compartment_details`

(required) Request to change the compartment that contains a VTAP.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONNECT_LOCAL_PEERING_GATEWAYS Function

Connects this local peering gateway (LPG) to another one in the same region. This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to LPGs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm).

Syntax
```

```

Parameters

Parameter Description

`local_peering_gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the local peering gateway.

`connect_local_peering_gateways_details`

(required) Details regarding the local peering gateway to connect.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONNECT_REMOTE_PEERING_CONNECTIONS Function

Connects this RPC to another one in a different region. This operation must be called by the VCN administrator who is designated as the *requestor* in the peering relationship. The *acceptor* must implement an Identity and Access Management (IAM) policy that gives the requestor permission to connect to RPCs in the acceptor's compartment. Without that permission, this operation will fail. For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm).

Syntax
```

```

Parameters

Parameter Description

`remote_peering_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote peering connection (RPC).

`connect_remote_peering_connections_details`

(required) Details to connect peering connection with peering connection from remote region

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BYOIP_RANGE Function

Creates a subrange of the BYOIP CIDR block.

Syntax
```

```

Parameters

Parameter Description

`create_byoip_range_details`

(required) Details needed to create a BYOIP CIDR block subrange.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CAPTURE_FILTER Function

Creates a virtual test access point (VTAP) capture filter in the specified compartment. For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the VTAP. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the VTAP, otherwise a default is provided. It does not have to be unique, and you can change it.

Syntax
```

```

Parameters

Parameter Description

`create_capture_filter_details`

(required) Details for creating a capture filter.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CPE Function

Creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For more information, see[Site-to-Site VPN Overview](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec connection or other Networking Service components. If you're not sure which compartment to use, put the CPE in the same compartment as the DRG. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must provide the public IP address of your on-premises router. See[CPE Configuration](https://docs.oracle.com/iaas/Content/Network/Tasks/configuringCPE.htm). You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_cpe_details`

(required) Details for creating a CPE.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CROSS_CONNECT Function

Creates a new cross-connect. Oracle recommends you create each cross-connect in a`CROSS_CONNECT_GROUP`Type so you can use link aggregation with the connection. After creating the `CrossConnect` object, you need to go the FastConnect location and request to have the physical cable installed. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the cross-connect to reside. If you're not sure which compartment to use, put the cross-connect in the same compartment with your VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the cross-connect. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_cross_connect_details`

(required) Details to create a CrossConnect

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CROSS_CONNECT_GROUP Function

Creates a new cross-connect group to use with Oracle Cloud Infrastructure FastConnect. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the cross-connect group to reside. If you're not sure which compartment to use, put the cross-connect group in the same compartment with your VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the cross-connect group. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_cross_connect_group_details`

(required) Details to create a CrossConnectGroup

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DHCP_OPTIONS Function

Creates a new set of DHCP options for the specified VCN. For more information, see`DHCP_OPTIONS`Type. For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the set of DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the set of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_dhcp_details`

(required) Request object for creating a new set of DHCP options.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DRG Function

Creates a new dynamic routing gateway (DRG) in the specified compartment. For more information, see[Dynamic Routing Gateways (DRGs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN, the DRG attachment, or other Networking Service components. If you're not sure which compartment to use, put the DRG in the same compartment as the VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the DRG, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_drg_details`

(required) Details for creating a DRG.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DRG_ATTACHMENT Function

Attaches the specified DRG to the specified network resource. A VCN can be attached to only one DRG at a time, but a DRG can be attached to more than one VCN. The response includes a `DrgAttachment` object with its own[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). For more information about DRGs, see[Dynamic Routing Gateways (DRGs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm). You may optionally specify a *display name* for the attachment, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. For the purposes of access control, the DRG attachment is automatically placed into the currently selected compartment. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

Syntax
```

```

Parameters

Parameter Description

`create_drg_attachment_details`

(required) Details for creating a `DrgAttachment`.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DRG_ROUTE_DISTRIBUTION Function

Creates a new route distribution for the specified DRG. Assign the route distribution as an import distribution to a DRG route table using the `UpdateDrgRouteTable` or `CreateDrgRouteTable` operations. Assign the route distribution as an export distribution to a DRG attachment using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations.

Syntax
```

```

Parameters

Parameter Description

`create_drg_route_distribution_details`

(required) Details for creating a route distribution.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DRG_ROUTE_TABLE Function

Creates a new DRG route table for the specified DRG. Assign the DRG route table to a DRG attachment using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations.

Syntax
```

```

Parameters

Parameter Description

`create_drg_route_table_details`

(required) Details for creating a DRG route table.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_IP_SEC_CONNECTION Function

Creates a new IPSec connection between the specified DRG and CPE. For more information, see[Site-to-Site VPN Overview](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm). If you configure at least one tunnel to use static routing, then in the request you must provide at least one valid static route (you're allowed a maximum of 10). For example: 10.0.0.0/16. If you configure both tunnels to use BGP dynamic routing, you can provide an empty list for the static routes. For more information, see the important note in`IP_SEC_CONNECTION`Type. For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to use, put the IPSec connection in the same compartment as the DRG. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. After creating the IPSec connection, you need to configure your on-premises router with tunnel-specific information. For tunnel status and the required configuration information, see: *`IP_SEC_CONNECTION_TUNNEL`Type *`IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Type For each tunnel, you need the IP address of Oracle's VPN headend and the shared secret (that is, the pre-shared key). For more information, see[CPE Configuration](https://docs.oracle.com/iaas/Content/Network/Tasks/configuringCPE.htm).

Syntax
```

```

Parameters

Parameter Description

`create_ip_sec_connection_details`

(required) Details for creating an `IPSecConnection`.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INTERNET_GATEWAY Function

Creates a new internet gateway for the specified VCN. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the Internet Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or other Networking Service components. If you're not sure which compartment to use, put the Internet Gateway in the same compartment with the VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in the subnet's route table (for example, 0.0.0.0/0 &gt; internet gateway). See`UPDATE_ROUTE_TABLE`Function. You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later use`UPDATE_INTERNET_GATEWAY`Function to easily disable/enable the gateway without changing the route rule.

Syntax
```

```

Parameters

Parameter Description

`create_internet_gateway_details`

(required) Details for creating a new internet gateway.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_IPV6 Function

Creates an IPv6 for the specified VNIC.

Syntax
```

```

Parameters

Parameter Description

`create_ipv6_details`

(required) Create IPv6 details.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LOCAL_PEERING_GATEWAY Function

Creates a new local peering gateway (LPG) for the specified VCN.

Syntax
```

```

Parameters

Parameter Description

`create_local_peering_gateway_details`

(required) Details for creating a new local peering gateway.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NAT_GATEWAY Function

Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the NAT gateway as the rule's target. See`ROUTE_TABLE`Type.

Syntax
```

```

Parameters

Parameter Description

`create_nat_gateway_details`

(required) Details for creating a NAT gateway.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NETWORK_SECURITY_GROUP Function

Creates a new network security group for the specified VCN.

Syntax
```

```

Parameters

Parameter Description

`create_network_security_group_details`

(required) Details for creating a network security group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PRIVATE_IP Function

Creates a secondary private IP for the specified VNIC. For more information about secondary private IPs, see[IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm).

Syntax
```

```

Parameters

Parameter Description

`create_private_ip_details`

(required) Create private IP details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PUBLIC_IP Function

Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or reserved public IP. For information about limits on how many you can create, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm). * **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId` with the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the primary private IP you want to assign the public IP to. The public IP is created in the same availability domain as the private IP. An ephemeral public IP must always be assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary private IP. Exception: If you create a`NAT_GATEWAY`Type, Oracle automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove. * **For a reserved public IP:** You may also optionally assign the public IP to a private IP by specifying `privateIpId`. Or you can later assign the public IP with`UPDATE_PUBLIC_IP`Function. **Note:** When assigning a public IP to a private IP, the private IP must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned. Also, for reserved public IPs, the optional assignment part of this operation is asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment succeeded.

Syntax
```

```

Parameters

Parameter Description

`create_public_ip_details`

(required) Create public IP details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PUBLIC_IP_POOL Function

Creates a public IP pool.

Syntax
```

```

Parameters

Parameter Description

`create_public_ip_pool_details`

(required) Create Public Ip Pool details

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REMOTE_PEERING_CONNECTION Function

Creates a new remote peering connection (RPC) for the specified DRG.

Syntax
```

```

Parameters

Parameter Description

`create_remote_peering_connection_details`

(required) Request to create peering connection to remote region

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ROUTE_TABLE Function

Creates a new route table for the specified VCN. In the request you must also include at least one route rule for the new route table. For information on the number of rules you can have in a route table, see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). For general information about route tables in your VCN and the types of targets you can use in route rules, see[Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the route table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the route table in the same compartment as the VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the route table, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_route_table_details`

(required) Details for creating a new route table.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SECURITY_LIST Function

Creates a new security list for the specified VCN. For more information about security lists, see[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). For information on the number of rules you can have in a security list, see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the security list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets, or other Networking Service components. If you're not sure which compartment to use, put the security list in the same compartment as the VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the security list, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_security_list_details`

(required) Details regarding the security list to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SERVICE_GATEWAY Function

Creates a new service gateway in the specified compartment. For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the service gateway to reside. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the service gateway, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_service_gateway_details`

(required) Details for creating a service gateway.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SUBNET Function

Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation, so it's important to think about the size of subnets you need before creating them. For more information, see[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm). For information on the number of subnets you can have in a VCN, see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the subnet to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or other Networking Service components. If you're not sure which compartment to use, put the subnet in the same compartment as the VCN. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally associate a route table with the subnet. If you don't, the subnet will use the VCN's default route table. For more information about route tables, see[Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm). You may optionally associate a security list with the subnet. If you don't, the subnet will use the VCN's default security list. For more information about security lists, see[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the VCN's default set. For more information about DHCP options, see[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm). You may optionally specify a *display name* for the subnet, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. You can also add a DNS label for the subnet, which is required if you want the Internet and VCN Resolver to resolve hostnames for instances in the subnet. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).

Syntax
```

```

Parameters

Parameter Description

`create_subnet_details`

(required) Details for creating a subnet.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VCN Function

Creates a new virtual cloud network (VCN). For more information, see[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm). For the VCN, you specify a list of one or more IPv4 CIDR blocks that meet the following criteria: - The CIDR blocks must be valid. - They must not overlap with each other or with the on-premises network CIDR block. - The number of CIDR blocks does not exceed the limit of CIDR blocks allowed per VCN. For a CIDR block, Oracle recommends that you use one of the private IP address ranges specified in[RFC 1918](https://tools.ietf.org/html/rfc1918)(10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR blocks can range from /16 to /30. For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the VCN to reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other Networking Service components. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to be unique, and you can change it. Avoid entering confidential information. You can also add a DNS label for the VCN, which is required if you want the instances to use the Interent and VCN Resolver option for DNS in the VCN. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). The VCN automatically comes with a default route table, default security list, and default set of DHCP options. The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for each is returned in the response. You can't delete these default objects, but you can change their contents (that is, change the route rules, security list rules, and so on). The VCN and subnets you create are not accessible until you attach an internet gateway or set up a Site-to-Site VPN or FastConnect. For more information, see[Overview of the Networking Service](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm).

Syntax
```

```

Parameters

Parameter Description

`create_vcn_details`

(required) Details for creating a new VCN.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VIRTUAL_CIRCUIT Function

Creates a new virtual circuit to use with Oracle Cloud Infrastructure FastConnect. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want the virtual circuit to reside. If you're not sure which compartment to use, put the virtual circuit in the same compartment with the DRG it's using. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the virtual circuit. It does not have to be unique, and you can change it. Avoid entering confidential information. **Important:** When creating a virtual circuit, you specify a DRG for the traffic to flow through. Make sure you attach the DRG to your VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise traffic will not flow. For more information, see[Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

Syntax
```

```

Parameters

Parameter Description

`create_virtual_circuit_details`

(required) Details to create a VirtualCircuit.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VLAN Function

Creates a VLAN in the specified VCN and the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`create_vlan_details`

(required) Details for creating a VLAN

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VTAP Function

Creates a virtual test access point (VTAP) in the specified compartment. For the purposes of access control, you must provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the VTAP. For more information about compartments and access control, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You may optionally specify a *display name* for the VTAP, otherwise a default is provided. It does not have to be unique, and you can change it.

Syntax
```

```

Parameters

Parameter Description

`create_vtap_details`

(required) Details used to create a VTAP.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BYOIP_RANGE Function

Deletes the specified `ByoipRange` resource. The resource must be in one of the following states: CREATING, PROVISIONED, ACTIVE, or FAILED. It must not have any subranges currently allocated to a PublicIpPool object or the deletion will fail. You must specify the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If the `ByoipRange` resource is currently in the PROVISIONED or ACTIVE state, it will be de-provisioned and then deleted.

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CAPTURE_FILTER Function

Deletes the specified VTAP capture filter. This is an asynchronous operation. The VTAP capture filter's `lifecycleState` will change to TERMINATING temporarily until the VTAP capture filter is completely removed.

Syntax
```

```

Parameters

Parameter Description

`capture_filter_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the capture filter.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CPE Function

Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous operation. The CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely removed.

Syntax
```

```

Parameters

Parameter Description

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CROSS_CONNECT Function

Deletes the specified cross-connect. It must not be mapped to a`VIRTUAL_CIRCUIT`Type.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CROSS_CONNECT_GROUP Function

Deletes the specified cross-connect group. It must not contain any cross-connects, and it cannot be mapped to a`VIRTUAL_CIRCUIT`Type.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DHCP_OPTIONS Function

Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a VCN's default set of DHCP options. This is an asynchronous operation. The state of the set of options will switch to TERMINATING temporarily until the set is completely removed.

Syntax
```

```

Parameters

Parameter Description

`dhcp_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the set of DHCP options.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DRG Function

Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous operation. The DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely removed.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DRG_ATTACHMENT Function

Detaches a DRG from a network resource by deleting the corresponding `DrgAttachment` resource. This is an asynchronous operation. The attachment's `lifecycleState` will temporarily change to DETACHING until the attachment is completely removed.

Syntax
```

```

Parameters

Parameter Description

`drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DRG_ROUTE_DISTRIBUTION Function

Deletes the specified route distribution. You can't delete a route distribution currently in use by a DRG attachment or DRG route table. Remove the DRG route distribution from a DRG attachment or DRG route table by using the \"RemoveExportDrgRouteDistribution\" or \"RemoveImportDrgRouteDistribution' operations.

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DRG_ROUTE_TABLE Function

Deletes the specified DRG route table. There must not be any DRG attachments assigned.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IP_SEC_CONNECTION Function

Deletes the specified IPSec connection. If your goal is to disable the Site-to-Site VPN between your VCN and on-premises network, it's easiest to simply detach the DRG but keep all the Site-to-Site VPN components intact. If you were to delete all the components and then later need to create an Site-to-Site VPN again, you would need to configure your on-premises router again with the new information returned from`CREATE_IP_SEC_CONNECTION`Function. This is an asynchronous operation. The connection's `lifecycleState` will change to TERMINATING temporarily until the connection is completely removed.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INTERNET_GATEWAY Function

Deletes the specified internet gateway. The internet gateway does not have to be disabled, but there must not be a route table that lists it as a target. This is an asynchronous operation. The gateway's `lifecycleState` will change to TERMINATING temporarily until the gateway is completely removed.

Syntax
```

```

Parameters

Parameter Description

`ig_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the internet gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IPV6 Function

Unassigns and deletes the specified IPv6. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). The IPv6 address is returned to the subnet's pool of available addresses.

Syntax
```

```

Parameters

Parameter Description

`ipv6_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPv6.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LOCAL_PEERING_GATEWAY Function

Deletes the specified local peering gateway (LPG). This is an asynchronous operation; the local peering gateway's `lifecycleState` changes to TERMINATING temporarily until the local peering gateway is completely removed.

Syntax
```

```

Parameters

Parameter Description

`local_peering_gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the local peering gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NAT_GATEWAY Function

Deletes the specified NAT gateway. The NAT gateway does not have to be disabled, but there must not be a route rule that lists the NAT gateway as a target. This is an asynchronous operation. The NAT gateway's `lifecycleState` will change to TERMINATING temporarily until the NAT gateway is completely removed.

Syntax
```

```

Parameters

Parameter Description

`nat_gateway_id`

(required) The NAT gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NETWORK_SECURITY_GROUP Function

Deletes the specified network security group. The group must not contain any VNICs. To get a list of the VNICs in a network security group, use`LIST_NETWORK_SECURITY_GROUP_VNICS`Function. Each returned`NETWORK_SECURITY_GROUP_VNIC`Type object contains both the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC and the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC's parent resource (for example, the Compute instance that the VNIC is attached to).

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PRIVATE_IP Function

Unassigns and deletes the specified private IP. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). The private IP address is returned to the subnet's pool of available addresses. This operation cannot be used with primary private IPs, which are automatically unassigned and deleted when the VNIC is terminated. **Important:** If a secondary private IP is the[target of a route rule](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip), unassigning it from the VNIC causes that route rule to blackhole and the traffic will be dropped.

Syntax
```

```

Parameters

Parameter Description

`private_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP or IPv6.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PUBLIC_IP Function

Unassigns and deletes the specified public IP (either ephemeral or reserved). You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). The public IP address is returned to the Oracle Cloud Infrastructure public IP pool. **Note:** You cannot update, unassign, or delete the public IP that Oracle automatically assigned to an entity for you (such as a load balancer or NAT gateway). The public IP is automatically deleted if the assigned entity is terminated. For an assigned reserved public IP, the initial unassignment portion of this operation is asynchronous. Poll the public IP's `lifecycleState` to determine if the operation succeeded. If you want to simply unassign a reserved public IP and return it to your pool of reserved public IPs, instead use`UPDATE_PUBLIC_IP`Function.

Syntax
```

```

Parameters

Parameter Description

`public_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PUBLIC_IP_POOL Function

Deletes the specified public IP pool. To delete a public IP pool it must not have any active IP address allocations. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)when deleting an IP pool.

Syntax
```

```

Parameters

Parameter Description

`public_ip_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REMOTE_PEERING_CONNECTION Function

Deletes the remote peering connection (RPC). This is an asynchronous operation; the RPC's `lifecycleState` changes to TERMINATING temporarily until the RPC is completely removed.

Syntax
```

```

Parameters

Parameter Description

`remote_peering_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote peering connection (RPC).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ROUTE_TABLE Function

Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a VCN's default route table. This is an asynchronous operation. The route table's `lifecycleState` will change to TERMINATING temporarily until the route table is completely removed.

Syntax
```

```

Parameters

Parameter Description

`rt_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SECURITY_LIST Function

Deletes the specified security list, but only if it's not associated with a subnet. You can't delete a VCN's default security list. This is an asynchronous operation. The security list's `lifecycleState` will change to TERMINATING temporarily until the security list is completely removed.

Syntax
```

```

Parameters

Parameter Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SERVICE_GATEWAY Function

Deletes the specified service gateway. There must not be a route table that lists the service gateway as a target.

Syntax
```

```

Parameters

Parameter Description

`service_gateway_id`

(required) The service gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SUBNET Function

Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous operation. The subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any instances in the subnet, the state will instead change back to AVAILABLE.

Syntax
```

```

Parameters

Parameter Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VCN Function

Deletes the specified VCN. The VCN must be completely empty and have no attached gateways. This is an asynchronous operation. A deleted VCN's `lifecycleState` changes to TERMINATING and then TERMINATED temporarily until the VCN is completely removed. A completely removed VCN does not appear in the results of a `ListVcns` operation and can't be used in a `GetVcn` operation.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VIRTUAL_CIRCUIT Function

Deletes the specified virtual circuit. **Important:** If you're using FastConnect via a provider, make sure to also terminate the connection with the provider, or else the provider may continue to bill you.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VLAN Function

Deletes the specified VLAN, but only if there are no VNICs in the VLAN.

Syntax
```

```

Parameters

Parameter Description

`vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VTAP Function

Deletes the specified VTAP. This is an asynchronous operation. The VTAP's `lifecycleState` will change to TERMINATING temporarily until the VTAP is completely removed.

Syntax
```

```

Parameters

Parameter Description

`vtap_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VTAP.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_SERVICE_ID Function

Removes the specified`SERVICE`Type from the list of enabled `Service` objects for the specified gateway. You do not need to remove any route rules that specify this `Service` object's `cidrBlock` as the destination CIDR. However, consider removing the rules if your intent is to permanently disable use of the `Service` through this service gateway. **Note:** The `DetachServiceId` operation is an easy way to remove an individual `Service` from the service gateway. Compare it with`UPDATE_SERVICE_GATEWAY`Function, which replaces the entire existing list of enabled `Service` objects with the list that you provide in the `Update` call. `UpdateServiceGateway` also lets you block all traffic through the service gateway without having to remove each of the individual `Service` objects.

Syntax
```

```

Parameters

Parameter Description

`service_gateway_id`

(required) The service gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`detach_service_details`

(required) ServiceId of Service to be detached from a service gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALL_DRG_ATTACHMENTS Function

Returns a complete list of DRG attachments that belong to a particular DRG.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`attachment_type`

(optional) The type for the network resource attached to the DRG.

Allowed values are: 'VCN', 'VIRTUAL_CIRCUIT', 'REMOTE_PEERING_CONNECTION', 'IPSEC_TUNNEL', 'ALL'

`is_cross_tenancy`

(optional) Whether the DRG attachment lives in a different tenancy than the DRG.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALLOWED_IKE_IP_SEC_PARAMETERS Function

The parameters allowed for IKE IPSec tunnels.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BYOIP_RANGE Function

Gets the `ByoipRange` resource. You must specify the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CAPTURE_FILTER Function

Gets information about the specified VTAP capture filter.

Syntax
```

```

Parameters

Parameter Description

`capture_filter_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the capture filter.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CPE Function

Gets the specified CPE's information.

Syntax
```

```

Parameters

Parameter Description

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CPE_DEVICE_CONFIG_CONTENT Function

Renders a set of CPE configuration content that can help a network engineer configure the actual CPE device (for example, a hardware router) represented by the specified`CPE`Type object. The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the`CPE`Type must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content optionally includes answers that the customer provides (see`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function), merged with a template of other information specific to the CPE device type. The operation returns configuration information for *all* of the`IP_SEC_CONNECTION`Type objects that use the specified CPE. Here are similar operations: *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function returns CPE configuration content for all IPSec tunnels in a single IPSec connection. *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function returns CPE configuration content for a specific IPSec tunnel in an IPSec connection.

Syntax
```

```

Parameters

Parameter Description

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CPE_DEVICE_SHAPE Function

Gets the detailed information about the specified CPE device type. This might include a set of questions that are specific to the particular CPE device type. The customer must supply answers to those questions (see`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function). The service merges the answers with a template of other information for the CPE device type. The following operations return the merged content: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function

Syntax
```

```

Parameters

Parameter Description

`cpe_device_shape_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE device shape.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CROSS_CONNECT Function

Gets the specified cross-connect's information.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CROSS_CONNECT_GROUP Function

Gets the specified cross-connect group's information.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CROSS_CONNECT_LETTER_OF_AUTHORITY Function

Gets the Letter of Authority for the specified cross-connect.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CROSS_CONNECT_STATUS Function

Gets the status of the specified cross-connect.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DHCP_OPTIONS Function

Gets the specified set of DHCP options.

Syntax
```

```

Parameters

Parameter Description

`dhcp_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the set of DHCP options.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DRG Function

Gets the specified DRG's information.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DRG_ATTACHMENT Function

Gets the `DrgAttachment` resource.

Syntax
```

```

Parameters

Parameter Description

`drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DRG_REDUNDANCY_STATUS Function

Gets the redundancy status for the specified DRG. For more information, see[Redundancy Remedies](https://docs.oracle.com/iaas/Content/Network/Troubleshoot/drgredundancy.htm).

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DRG_ROUTE_DISTRIBUTION Function

Gets the specified route distribution's information.

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DRG_ROUTE_TABLE Function

Gets the specified DRG route table's information.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FAST_CONNECT_PROVIDER_SERVICE Function

Gets the specified provider service. For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

Syntax
```

```

Parameters

Parameter Description

`provider_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the provider service.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FAST_CONNECT_PROVIDER_SERVICE_KEY Function

Gets the specified provider service key's information. Use this operation to validate a provider service key. An invalid key returns a 404 error.

Syntax
```

```

Parameters

Parameter Description

`provider_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the provider service.

`provider_service_key_name`

(required) The provider service key that the provider gives you when you set up a virtual circuit connection from the provider to Oracle Cloud Infrastructure. You can set up that connection and get your provider service key at the provider's website or portal. For the portal location, see the `description` attribute of the`FAST_CONNECT_PROVIDER_SERVICE`Type.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IP_SEC_CONNECTION Function

Gets the specified IPSec connection's basic information, including the static routes for the on-premises router. If you want the status of the connection (whether it's up or down), use`GET_IP_SEC_CONNECTION_TUNNEL`Function.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IP_SEC_CONNECTION_DEVICE_CONFIG Function

Deprecated. To get tunnel information, instead use: *`GET_IP_SEC_CONNECTION_TUNNEL`Function *`GET_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Function

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IP_SEC_CONNECTION_DEVICE_STATUS Function

Deprecated. To get the tunnel status, instead use`GET_IP_SEC_CONNECTION_TUNNEL`Function.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IP_SEC_CONNECTION_TUNNEL Function

Gets the specified tunnel's information. The resulting object does not include the tunnel's shared secret (pre-shared key). To retrieve that, use`GET_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET`Function.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IP_SEC_CONNECTION_TUNNEL_ERROR Function

Gets the identified error for the specified IPSec tunnel ID.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET Function

Gets the specified tunnel's shared secret (pre-shared key). To get other information about the tunnel, use`GET_IP_SEC_CONNECTION_TUNNEL`Function.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INTERNET_GATEWAY Function

Gets the specified internet gateway's information.

Syntax
```

```

Parameters

Parameter Description

`ig_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the internet gateway.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT Function

Renders a set of CPE configuration content for the specified IPSec connection (for all the tunnels in the connection). The content helps a network engineer configure the actual CPE device (for example, a hardware router) that the specified IPSec connection terminates on. The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the`CPE`Type used by the specified`IP_SEC_CONNECTION`Type must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content optionally includes answers that the customer provides (see`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function), merged with a template of other information specific to the CPE device type. The operation returns configuration information for all tunnels in the single specified`IP_SEC_CONNECTION`Type object. Here are other similar operations: *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function returns CPE configuration content for a specific tunnel within an IPSec connection. *`GET_CPE_DEVICE_CONFIG_CONTENT`Function returns CPE configuration content for *all* IPSec connections that use a specific CPE.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IPV6 Function

Gets the specified IPv6. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Alternatively, you can get the object by using`LIST_IPV6S`Function with the IPv6 address (for example, 2001:0db8:0123:1111:98fe:dcba:9876:4321) and subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`ipv6_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPv6.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LOCAL_PEERING_GATEWAY Function

Gets the specified local peering gateway's information.

Syntax
```

```

Parameters

Parameter Description

`local_peering_gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the local peering gateway.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NAT_GATEWAY Function

Gets the specified NAT gateway's information.

Syntax
```

```

Parameters

Parameter Description

`nat_gateway_id`

(required) The NAT gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORK_SECURITY_GROUP Function

Gets the specified network security group's information. To list the VNICs in an NSG, see`LIST_NETWORK_SECURITY_GROUP_VNICS`Function. To list the security rules in an NSG, see`LIST_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORKING_TOPOLOGY Function

Gets a virtual networking topology for the current region.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`access_level`

(optional) Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`. Setting this to `ACCESSIBLE` returns only compartments for which a user has INSPECT permissions, either directly or indirectly (permissions can be on a resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has indirect INSPECT permissions. When set to `ANY` permissions are not checked.

Allowed values are: 'ANY', 'ACCESSIBLE'

`query_compartment_subtree`

(optional) When set to true, the hierarchy of compartments is traversed and the specified compartment and its subcompartments are inspected depending on the the setting of `accessLevel`. Default is false.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_none_match`

(optional) For querying if there is a cached value on the server. The If-None-Match HTTP request header makes the request conditional. For GET and HEAD methods, the server will send back the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. For other methods, the request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed.

`cache_control`

(optional) The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRIVATE_IP Function

Gets the specified private IP. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Alternatively, you can get the object by using`LIST_PRIVATE_IPS`Function with the private IP address (for example, 10.0.3.3) and subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`private_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP or IPv6.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLIC_IP Function

Gets the specified public IP. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Alternatively, you can get the object by using`GET_PUBLIC_IP_BY_IP_ADDRESS`Function with the public IP address (for example, 203.0.113.2). Or you can use`GET_PUBLIC_IP_BY_PRIVATE_IP_ID`Function with the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP that the public IP is assigned to. **Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` =[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target private IP.

Syntax
```

```

Parameters

Parameter Description

`public_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLIC_IP_BY_IP_ADDRESS Function

Gets the public IP based on the public IP address (for example, 203.0.113.2). **Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` =[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target private IP.

Syntax
```

```

Parameters

Parameter Description

`get_public_ip_by_ip_address_details`

(required) IP address details for fetching the public IP.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLIC_IP_BY_PRIVATE_IP_ID Function

Gets the public IP assigned to the specified private IP. You must specify the OCID of the private IP. If no public IP is assigned, a 404 is returned. **Note:** If you're fetching a reserved public IP that is in the process of being moved to a different private IP, and you provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the original private IP, this operation returns a 404. If you instead provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target private IP, or if you instead call`GET_PUBLIC_IP`Function or`GET_PUBLIC_IP_BY_IP_ADDRESS`Function, the service returns the public IP object with `lifecycleState` = ASSIGNING and `assignedEntityId` =[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target private IP.

Syntax
```

```

Parameters

Parameter Description

`get_public_ip_by_private_ip_id_details`

(required) Private IP details for fetching the public IP.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PUBLIC_IP_POOL Function

Gets the specified `PublicIpPool` object. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`public_ip_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REMOTE_PEERING_CONNECTION Function

Get the specified remote peering connection's information.

Syntax
```

```

Parameters

Parameter Description

`remote_peering_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote peering connection (RPC).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROUTE_TABLE Function

Gets the specified route table's information.

Syntax
```

```

Parameters

Parameter Description

`rt_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_LIST Function

Gets the specified security list's information.

Syntax
```

```

Parameters

Parameter Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE Function

Gets the specified`SERVICE`Type object.

Syntax
```

```

Parameters

Parameter Description

`service_id`

(required) The service's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SERVICE_GATEWAY Function

Gets the specified service gateway's information.

Syntax
```

```

Parameters

Parameter Description

`service_gateway_id`

(required) The service gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUBNET Function

Gets the specified subnet's information.

Syntax
```

```

Parameters

Parameter Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUBNET_TOPOLOGY Function

Gets a topology for a given subnet.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`access_level`

(optional) Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`. Setting this to `ACCESSIBLE` returns only compartments for which a user has INSPECT permissions, either directly or indirectly (permissions can be on a resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has indirect INSPECT permissions. When set to `ANY` permissions are not checked.

Allowed values are: 'ANY', 'ACCESSIBLE'

`query_compartment_subtree`

(optional) When set to true, the hierarchy of compartments is traversed and the specified compartment and its subcompartments are inspected depending on the the setting of `accessLevel`. Default is false.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_none_match`

(optional) For querying if there is a cached value on the server. The If-None-Match HTTP request header makes the request conditional. For GET and HEAD methods, the server will send back the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. For other methods, the request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed.

`cache_control`

(optional) The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TUNNEL_CPE_DEVICE_CONFIG Function

Gets the set of CPE configuration answers for the tunnel, which the customer provided in`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function. To get the full set of content for the tunnel (any answers merged with the template of other information specific to the CPE device type), use`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT Function

Renders a set of CPE configuration content for the specified IPSec tunnel. The content helps a network engineer configure the actual CPE device (for example, a hardware router) that the specified IPSec tunnel terminates on. The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the`CPE`Type used by the specified`IP_SEC_CONNECTION`Type must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content optionally includes answers that the customer provides (see`UPDATE_TUNNEL_CPE_DEVICE_CONFIG`Function), merged with a template of other information specific to the CPE device type. The operation returns configuration information for only the specified IPSec tunnel. Here are other similar operations: *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function returns CPE configuration content for all tunnels in a single IPSec connection. *`GET_CPE_DEVICE_CONFIG_CONTENT`Function returns CPE configuration content for *all* IPSec connections that use a specific CPE.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_UPGRADE_STATUS Function

Returns the DRG upgrade status. The status can be not updated, in progress, or updated. Also indicates how much of the upgrade is completed.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VCN Function

Gets the specified VCN's information.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VCN_DNS_RESOLVER_ASSOCIATION Function

Get the associated DNS resolver information with a vcn

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VCN_TOPOLOGY Function

Gets a virtual network topology for a given VCN.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`access_level`

(optional) Valid values are `ANY` and `ACCESSIBLE`. The default is `ANY`. Setting this to `ACCESSIBLE` returns only compartments for which a user has INSPECT permissions, either directly or indirectly (permissions can be on a resource in a subcompartment). A restricted set of fields is returned for compartments in which a user has indirect INSPECT permissions. When set to `ANY` permissions are not checked.

Allowed values are: 'ANY', 'ACCESSIBLE'

`query_compartment_subtree`

(optional) When set to true, the hierarchy of compartments is traversed and the specified compartment and its subcompartments are inspected depending on the the setting of `accessLevel`. Default is false.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_none_match`

(optional) For querying if there is a cached value on the server. The If-None-Match HTTP request header makes the request conditional. For GET and HEAD methods, the server will send back the requested resource, with a 200 status, only if it doesn't have an ETag matching the given ones. For other methods, the request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed.

`cache_control`

(optional) The Cache-Control HTTP header holds directives (instructions) for caching in both requests and responses.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VIRTUAL_CIRCUIT Function

Gets the specified virtual circuit's information.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VLAN Function

Gets the specified VLAN's information.

Syntax
```

```

Parameters

Parameter Description

`vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VNIC Function

Gets the information for the specified virtual network interface card (VNIC). You can get the VNIC[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)from the`LIST_VNIC_ATTACHMENTS`Function operation.

Syntax
```

```

Parameters

Parameter Description

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VTAP Function

Gets the specified `Vtap` resource.

Syntax
```

```

Parameters

Parameter Description

`vtap_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VTAP.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALLOWED_PEER_REGIONS_FOR_REMOTE_PEERING Function

Lists the regions that support remote VCN peering (which is peering across regions). For more information, see[VCN Peering](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm).

Syntax
```

```

Parameters

Parameter Description

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BYOIP_ALLOCATED_RANGES Function

Lists the subranges of a BYOIP CIDR block currently allocated to an IP pool. Each `ByoipAllocatedRange` object also lists the IP pool where it is allocated.

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BYOIP_RANGES Function

Lists the `ByoipRange` resources in the specified compartment. You can filter the list using query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CAPTURE_FILTERS Function

Lists the capture filters in the specified compartment.

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

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`lifecycle_state`

(optional) A filter to return only resources that match the given capture filter lifecycle state. The state value is case-insensitive.

`filter_type`

(optional) A filter to only return resources that match the given capture `filterType`. The `filterType` value is the string representation of enum - `VTAP`, `FLOWLOG`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CPE_DEVICE_SHAPES Function

Lists the CPE device types that the Networking service provides CPE configuration content for (example: Cisco ASA). The content helps a network engineer configure the actual CPE device represented by a`CPE`Type object. If you want to generate CPE configuration content for one of the returned CPE device types, ensure that the`CPE`Type object's `cpeDeviceShapeId` attribute is set to the CPE device type's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)(returned by this operation). For information about generating CPE configuration content, see these operations: *`GET_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT`Function *`GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT`Function

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CPES Function

Lists the customer-premises equipment objects (CPEs) in the specified compartment.

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

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CROSS_CONNECT_GROUPS Function

Lists the cross-connect groups in the specified compartment.

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

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CROSS_CONNECT_LOCATIONS Function

Lists the available FastConnect locations for cross-connect installation. You need this information so you can specify your desired location when you create a cross-connect.

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

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CROSS_CONNECT_MAPPINGS Function

Lists the Cross Connect mapping Details for the specified virtual circuit.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CROSS_CONNECTS Function

Lists the cross-connects in the specified compartment. You can filter the list by specifying the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a cross-connect group.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`cross_connect_group_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CROSSCONNECT_PORT_SPEED_SHAPES Function

Lists the available port speeds for cross-connects. You need this information so you can specify your desired port speed (that is, shape) when you create a cross-connect.

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

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DHCP_OPTIONS Function

Lists the sets of DHCP options in the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the sets of DHCP options from all VCNs in the specified compartment. The response includes the default set of options that automatically comes with each VCN, plus any other sets you've created.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRG_ATTACHMENTS Function

Lists the `DrgAttachment` resource for the specified compartment. You can filter the results by DRG, attached network, attachment type, DRG route table or VCN route table. The LIST API lists DRG attachments by attachment type. It will default to list VCN attachments, but you may request to list ALL attachments of ALL types.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`drg_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`network_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource (virtual circuit, VCN, IPSec tunnel, or remote peering connection) attached to the DRG.

`attachment_type`

(optional) The type for the network resource attached to the DRG.

Allowed values are: 'VCN', 'VIRTUAL_CIRCUIT', 'REMOTE_PEERING_CONNECTION', 'IPSEC_TUNNEL', 'ALL'

`drg_route_table_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table assigned to the DRG attachment.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function

Lists the statements for the specified route distribution.

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by.

Allowed values are: 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRG_ROUTE_DISTRIBUTIONS Function

Lists the route distributions in the specified DRG. To retrieve the statements in a distribution, use the ListDrgRouteDistributionStatements operation.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter that only returns resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRG_ROUTE_RULES Function

Lists the route rules in the specified DRG route table.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`route_type`

(optional) Static routes are specified through the DRG route table API. Dynamic routes are learned by the DRG from the DRG attachments through various routing protocols.

Allowed values are: 'STATIC', 'DYNAMIC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRG_ROUTE_TABLES Function

Lists the DRG route tables for the specified DRG. Use the `ListDrgRouteRules` operation to retrieve the route rules in a table.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`import_drg_route_distribution_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the import route distribution.

`lifecycle_state`

(optional) A filter that only returns matches for the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DRGS Function

Lists the DRGs in the specified compartment.

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

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FAST_CONNECT_PROVIDER_SERVICES Function

Lists the service offerings from supported providers. You need this information so you can specify your desired provider and service offering when you create a virtual circuit. For the compartment ID, provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of your tenancy (the root compartment). For more information, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

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

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FAST_CONNECT_PROVIDER_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES Function

Gets the list of available virtual circuit bandwidth levels for a provider. You need this information so you can specify your desired bandwidth level (shape) when you create a virtual circuit. For more information about virtual circuits, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

Syntax
```

```

Parameters

Parameter Description

`provider_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the provider service.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IP_SEC_CONNECTION_TUNNEL_ROUTES Function

The routes advertised to the on-premises network and the routes received from the on-premises network.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`advertiser`

(optional) Specifies the advertiser of the routes. If set to `ORACLE`, this returns only the routes advertised by Oracle. When set to `CUSTOMER`, this returns only the routes advertised by the CPE.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IP_SEC_CONNECTION_TUNNEL_SECURITY_ASSOCIATIONS Function

Lists the tunnel security associations information for the specified IPSec tunnel ID.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IP_SEC_CONNECTION_TUNNELS Function

Lists the tunnel information for the specified IPSec connection.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IP_SEC_CONNECTIONS Function

Lists the IPSec connections for the specified compartment. You can filter the results by DRG or CPE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`drg_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`cpe_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INTERNET_GATEWAYS Function

Lists the internet gateways in the specified VCN and the specified compartment. If the VCN ID is not provided, then the list includes the internet gateways from all VCNs in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IPV6S Function

Lists the`IPV6`Type objects based on one of these filters: * Subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). * VNIC[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). * Both IPv6 address and subnet OCID: This lets you get an `Ipv6` object based on its private IPv6 address (for example, 2001:0db8:0123:1111:abcd:ef01:2345:6789) and not its[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). For comparison,`GET_IPV6`Function requires the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`ip_address`

(optional) An IP address. This could be either IPv4 or IPv6, depending on the resource. Example: `10.0.3.3`

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`vnic_id`

(optional) The OCID of the VNIC.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LOCAL_PEERING_GATEWAYS Function

Lists the local peering gateways (LPGs) for the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the LPGs from all VCNs in the specified compartment.

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

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NAT_GATEWAYS Function

Lists the NAT gateways in the specified compartment. You may optionally specify a VCN OCID to filter the results by VCN.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_SECURITY_GROUP_SECURITY_RULES Function

Lists the security rules in the specified network security group.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`direction`

(optional) Direction of the security rule. Set to `EGRESS` for rules that allow outbound IP packets, or `INGRESS` for rules that allow inbound IP packets.

Allowed values are: 'EGRESS', 'INGRESS'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by.

Allowed values are: 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_SECURITY_GROUP_VNICS Function

Lists the VNICs in the specified network security group.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by.

Allowed values are: 'TIMEASSOCIATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_SECURITY_GROUPS Function

Lists either the network security groups in the specified compartment, or those associated with the specified VLAN. You must specify either a `vlanId` or a `compartmentId`, but not both. If you specify a `vlanId`, all other parameters are ignored.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRIVATE_IPS Function

Lists the`PRIVATE_IP`Type objects based on one of these filters: - Subnet[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). - VNIC[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). - Both private IP address and subnet OCID: This lets you get a `privateIP` object based on its private IP address (for example, 10.0.3.3) and not its[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). For comparison,`GET_PRIVATE_IP`Function requires the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If you're listing all the private IPs associated with a given subnet or VNIC, the response includes both primary and secondary private IPs. If you are an Oracle Cloud VMware Solution customer and have VLANs in your VCN, you can filter the list by VLAN[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). See`VLAN`Type.

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`ip_address`

(optional) An IP address. This could be either IPv4 or IPv6, depending on the resource. Example: `10.0.3.3`

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`vnic_id`

(optional) The OCID of the VNIC.

`vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLIC_IP_POOLS Function

Lists the public IP pools in the specified compartment. You can filter the list using query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`byoip_range_id`

(optional) A filter to return only resources that match the given BYOIP CIDR block.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLIC_IPS Function

Lists the`PUBLIC_IP`Type objects in the specified compartment. You can filter the list by using query parameters. To list your reserved public IPs: * Set `scope` = `REGION` (required) * Leave the `availabilityDomain` parameter empty * Set `lifetime` = `RESERVED` To list the ephemeral public IPs assigned to a regional entity such as a NAT gateway: * Set `scope` = `REGION` (required) * Leave the `availabilityDomain` parameter empty * Set `lifetime` = `EPHEMERAL` To list the ephemeral public IPs assigned to private IPs: * Set `scope` = `AVAILABILITY_DOMAIN` (required) * Set the `availabilityDomain` parameter to the desired availability domain (required) * Set `lifetime` = `EPHEMERAL` **Note:** An ephemeral public IP assigned to a private IP is always in the same availability domain and compartment as the private IP.

Syntax
```

```

Parameters

Parameter Description

`scope`

(required) Whether the public IP is regional or specific to a particular availability domain. * `REGION`: The public IP exists within a region and is assigned to a regional entity (such as a`NAT_GATEWAY`Type), or can be assigned to a private IP in any availability domain in the region. Reserved public IPs have `scope` = `REGION`, as do ephemeral public IPs assigned to a regional entity. * `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity it's assigned to, which is specified by the `availabilityDomain` property of the public IP object. Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`.

Allowed values are: 'REGION', 'AVAILABILITY_DOMAIN'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`lifetime`

(optional) A filter to return only public IPs that match given lifetime.

Allowed values are: 'EPHEMERAL', 'RESERVED'

`public_ip_pool_id`

(optional) A filter to return only resources that belong to the given public IP pool.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REMOTE_PEERING_CONNECTIONS Function

Lists the remote peering connections (RPCs) for the specified DRG and compartment (the RPC's compartment).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`drg_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROUTE_TABLES Function

Lists the route tables in the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the route tables from all VCNs in the specified compartment. The response includes the default route table that automatically comes with each VCN in the specified compartment, plus any route tables you've created.

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

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_LISTS Function

Lists the security lists in the specified VCN and compartment. If the VCN ID is not provided, then the list includes the security lists from all VCNs in the specified compartment.

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

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_GATEWAYS Function

Lists the service gateways in the specified compartment. You may optionally specify a VCN OCID to filter the results by VCN.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICES Function

Lists the available`SERVICE`Type objects that you can enable for a service gateway in this region.

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBNETS Function

Lists the subnets in the specified VCN and the specified compartment. If the VCN ID is not provided, then the list includes the subnets from all VCNs in the specified compartment.

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

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VCNS Function

Lists the virtual cloud networks (VCNs) in the specified compartment.

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

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_CIRCUIT_ASSOCIATED_TUNNELS Function

Gets the specified virtual circuit's associatedTunnelsInfo.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES Function

The deprecated operation lists available bandwidth levels for virtual circuits. For the compartment ID, provide the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of your tenancy (the root compartment).

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

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES Function

Lists the public IP prefixes and their details for the specified public virtual circuit.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`verification_state`

(optional) A filter to only return resources that match the given verification state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VIRTUAL_CIRCUITS Function

Lists the virtual circuits in the specified compartment.

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

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state. The value is case insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VLANS Function

Lists the VLANs in the specified VCN and the specified compartment.

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

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VTAPS Function

Lists the virtual test access points (VTAPs) in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`source`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VTAP source.

`target_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VTAP target.

`target_ip`

(optional) The IP address of the VTAP target.

`is_vtap_enabled`

(optional) Indicates whether to list all VTAPs or only running VTAPs. * When `FALSE`, lists ALL running and stopped VTAPs. * When `TRUE`, lists only running VTAPs (VTAPs where isVtapEnabled = `TRUE`).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`lifecycle_state`

(optional) A filter to return only resources that match the given VTAP administrative lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MODIFY_VCN_CIDR Function

Updates the specified CIDR block of a VCN. The new CIDR IP range must meet the following criteria: - Must be valid. - Must not overlap with another CIDR block in the VCN, a CIDR block of a peered VCN, or the on-premises network CIDR block. - Must not exceed the limit of CIDR blocks allowed per VCN. - Must include IP addresses from the original CIDR block that are used in the VCN's existing route rules. - No IP address in an existing subnet should be outside of the new CIDR block range. **Note:** Modifying a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can vary depending on the size of your network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can use the `GetWorkRequest` operation to check the status of the update.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`modify_vcn_cidr_details`

(required) Details object for updating a VCN CIDR.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function

Removes one or more route distribution statements from the specified route distribution's map.

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`remove_drg_route_distribution_statements_details`

(required) Request with one or more route distribution statements to remove from the route distribution.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_DRG_ROUTE_RULES Function

Removes one or more route rules from the specified DRG route table.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`remove_drg_route_rules_details`

(required) Request to remove one or more route rules in the DRG route table.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_EXPORT_DRG_ROUTE_DISTRIBUTION Function

Removes the export route distribution from the DRG attachment so no routes are advertised to it.

Syntax
```

```

Parameters

Parameter Description

`drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_IMPORT_DRG_ROUTE_DISTRIBUTION Function

Removes the import route distribution from the DRG route table so no routes are imported into it.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_IPV6_SUBNET_CIDR Function

Remove an IPv6 prefix from a subnet. At least one IPv6 CIDR should remain.

Syntax
```

```

Parameters

Parameter Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`remove_subnet_ipv6_cidr_details`

(required) Details object for removing an IPv6 SUBNET prefix.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_IPV6_VCN_CIDR Function

Removing an existing IPv6 prefix from a VCN.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`remove_vcn_ipv6_cidr_details`

(optional) Details object for removing a VCN IPv6 prefix.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES Function

Removes one or more security rules from the specified network security group.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`remove_network_security_group_security_rules_details`

(required) Request with one or more security rules associated with the network security group that will be removed.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_PUBLIC_IP_POOL_CAPACITY Function

Removes a CIDR block from the referenced public IP pool.

Syntax
```

```

Parameters

Parameter Description

`public_ip_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`remove_public_ip_pool_capacity_details`

(required) The CIDR block to remove from the IP pool.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_VCN_CIDR Function

Removes a specified CIDR block from a VCN. **Notes:** - You cannot remove a CIDR block if an IP address in its range is in use. - Removing a CIDR block places your VCN in an updating state until the changes are complete. You cannot create or update the VCN's subnets, VLANs, LPGs, or route tables during this operation. The time to completion can take a few minutes. You can use the `GetWorkRequest` operation to check the status of the update.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`remove_vcn_cidr_details`

(required) Details object for removing a VCN CIDR.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BYOIP_RANGE Function

Updates the tags or display name associated to the specified BYOIP CIDR block.

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`update_byoip_range_details`

(required) Byoip Range details.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CAPTURE_FILTER Function

Updates the specified VTAP capture filter's display name or tags.

Syntax
```

```

Parameters

Parameter Description

`capture_filter_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the capture filter.

`update_capture_filter_details`

(required) Details object for updating a VTAP.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CPE Function

Updates the specified CPE's display name or tags. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`cpe_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CPE.

`update_cpe_details`

(required) Details object for updating a CPE.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CROSS_CONNECT Function

Updates the specified cross-connect.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect.

`update_cross_connect_details`

(required) Update CrossConnect fields.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CROSS_CONNECT_GROUP Function

Updates the specified cross-connect group's display name. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`cross_connect_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cross-connect group.

`update_cross_connect_group_details`

(required) Update CrossConnectGroup fields

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DHCP_OPTIONS Function

Updates the specified set of DHCP options. You can update the display name or the options themselves. Avoid entering confidential information. Note that the `options` object you provide replaces the entire existing set of options.

Syntax
```

```

Parameters

Parameter Description

`dhcp_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the set of DHCP options.

`update_dhcp_details`

(required) Request object for updating a set of DHCP options.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRG Function

Updates the specified DRG's display name or tags. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`update_drg_details`

(required) Details object for updating a DRG.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRG_ATTACHMENT Function

Updates the display name and routing information for the specified `DrgAttachment`. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`drg_attachment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG attachment.

`update_drg_attachment_details`

(required) Details object for updating a `DrgAttachment`.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRG_ROUTE_DISTRIBUTION Function

Updates the specified route distribution

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`update_drg_route_distribution_details`

(required) Details object for updating a route distribution

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function

Updates one or more route distribution statements in the specified route distribution.

Syntax
```

```

Parameters

Parameter Description

`drg_route_distribution_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route distribution.

`update_drg_route_distribution_statements_details`

(required) Request to update one or more route distribution statements in the route distribution.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRG_ROUTE_RULES Function

Updates one or more route rules in the specified DRG route table.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`update_drg_route_rules_details`

(required) Request to update one or more route rules in the DRG route table.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DRG_ROUTE_TABLE Function

Updates the specified DRG route table.

Syntax
```

```

Parameters

Parameter Description

`drg_route_table_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG route table.

`update_drg_route_table_details`

(required) Details object used to updating a DRG route table.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IP_SEC_CONNECTION Function

Updates the specified IPSec connection. To update an individual IPSec tunnel's attributes, use`UPDATE_IP_SEC_CONNECTION_TUNNEL`Function.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`update_ip_sec_connection_details`

(required) Details object for updating an IPSec connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IP_SEC_CONNECTION_TUNNEL Function

Updates the specified tunnel. This operation lets you change tunnel attributes such as the routing type (BGP dynamic routing or static routing). Here are some important notes: * If you change the tunnel's routing type or BGP session configuration, the tunnel will go down while it's reprovisioned. * If you want to switch the tunnel's `routing` from `STATIC` to `BGP`, make sure the tunnel's BGP session configuration attributes have been set (`BGP_SESSION_INFO`Function). * If you want to switch the tunnel's `routing` from `BGP` to `STATIC`, make sure the`IP_SEC_CONNECTION`Type already has at least one valid CIDR static route.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`update_ip_sec_connection_tunnel_details`

(required) Details object for updating a IPSecConnection tunnel's details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET Function

Updates the shared secret (pre-shared key) for the specified tunnel. **Important:** If you change the shared secret, the tunnel will go down while it's reprovisioned.

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`update_ip_sec_connection_tunnel_shared_secret_details`

(required) Details object for updating a IPSec connection tunnel's sharedSecret.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INTERNET_GATEWAY Function

Updates the specified internet gateway. You can disable/enable it, or change its display name or tags. Avoid entering confidential information. If the gateway is disabled, that means no traffic will flow to/from the internet even if there's a route rule that enables that traffic.

Syntax
```

```

Parameters

Parameter Description

`ig_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the internet gateway.

`update_internet_gateway_details`

(required) Details for updating the internet gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IPV6 Function

Updates the specified IPv6. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Use this operation if you want to: * Move an IPv6 to a different VNIC in the same subnet. * Enable/disable internet access for an IPv6. * Change the display name for an IPv6. * Update resource tags for an IPv6.

Syntax
```

```

Parameters

Parameter Description

`ipv6_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPv6.

`update_ipv6_details`

(required) IPv6 details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LOCAL_PEERING_GATEWAY Function

Updates the specified local peering gateway (LPG).

Syntax
```

```

Parameters

Parameter Description

`local_peering_gateway_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the local peering gateway.

`update_local_peering_gateway_details`

(required) Details object for updating a local peering gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NAT_GATEWAY Function

Updates the specified NAT gateway.

Syntax
```

```

Parameters

Parameter Description

`nat_gateway_id`

(required) The NAT gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_nat_gateway_details`

(required) Details object for updating a NAT gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_SECURITY_GROUP Function

Updates the specified network security group. To add or remove an existing VNIC from the group, use`UPDATE_VNIC`Function. To add a VNIC to the group *when you create the VNIC*, specify the NSG's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)during creation. For example, see the `nsgIds` attribute in`CREATE_VNIC_DETAILS`Function. To add or remove security rules from the group, use`ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function or`REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function. To edit the contents of existing security rules in the group, use`UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES`Function.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`update_network_security_group_details`

(required) Details object for updating a network security group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES Function

Updates one or more security rules in the specified network security group.

Syntax
```

```

Parameters

Parameter Description

`network_security_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security group.

`update_network_security_group_security_rules_details`

(required) Request with one or more security rules associated with the network security group that will be updated.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PRIVATE_IP Function

Updates the specified private IP. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Use this operation if you want to: - Move a secondary private IP to a different VNIC in the same subnet. - Change the display name for a secondary private IP. - Change the hostname for a secondary private IP. This operation cannot be used with primary private IPs. To update the hostname for the primary IP on a VNIC, use`UPDATE_VNIC`Function.

Syntax
```

```

Parameters

Parameter Description

`private_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private IP or IPv6.

`update_private_ip_details`

(required) Private IP details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PUBLIC_IP Function

Updates the specified public IP. You must specify the object's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Use this operation if you want to: * Assign a reserved public IP in your pool to a private IP. * Move a reserved public IP to a different private IP. * Unassign a reserved public IP from a private IP (which returns it to your pool of reserved public IPs). * Change the display name or tags for a public IP. Assigning, moving, and unassigning a reserved public IP are asynchronous operations. Poll the public IP's `lifecycleState` to determine if the operation succeeded. **Note:** When moving a reserved public IP, the target private IP must not already have a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned. Also, the initial unassignment from the original private IP always succeeds, but the assignment to the target private IP is asynchronous and could fail silently (for example, if the target private IP is deleted or has a different public IP assigned to it in the interim). If that occurs, the public IP remains unassigned and its `lifecycleState` switches to AVAILABLE (it is not reassigned to its original private IP). You must poll the public IP's `lifecycleState` to determine if the move succeeded. Regarding ephemeral public IPs: * If you want to assign an ephemeral public IP to a primary private IP, use`CREATE_PUBLIC_IP`Function. * You can't move an ephemeral public IP to a different private IP. * If you want to unassign an ephemeral public IP from its private IP, use`DELETE_PUBLIC_IP`Function, which unassigns and deletes the ephemeral public IP. **Note:** If a public IP is assigned to a secondary private IP (see`PRIVATE_IP`Type), and you move that secondary private IP to another VNIC, the public IP moves with it. **Note:** There's a limit to the number of`PUBLIC_IP`Type a VNIC or instance can have. If you try to move a reserved public IP to a VNIC or instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

Syntax
```

```

Parameters

Parameter Description

`public_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP.

`update_public_ip_details`

(required) Public IP details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PUBLIC_IP_POOL Function

Updates the specified public IP pool.

Syntax
```

```

Parameters

Parameter Description

`public_ip_pool_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the public IP pool.

`update_public_ip_pool_details`

(required) Public IP pool details.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REMOTE_PEERING_CONNECTION Function

Updates the specified remote peering connection (RPC).

Syntax
```

```

Parameters

Parameter Description

`remote_peering_connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote peering connection (RPC).

`update_remote_peering_connection_details`

(required) Request to the update the peering connection to remote region

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ROUTE_TABLE Function

Updates the specified route table's display name or route rules. Avoid entering confidential information. Note that the `routeRules` object you provide replaces the entire existing set of rules.

Syntax
```

```

Parameters

Parameter Description

`rt_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the route table.

`update_route_table_details`

(required) Details object for updating a route table.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_LIST Function

Updates the specified security list's display name or rules. Avoid entering confidential information. Note that the `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire existing objects.

Syntax
```

```

Parameters

Parameter Description

`security_list_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the security list.

`update_security_list_details`

(required) Updated details for the security list.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SERVICE_GATEWAY Function

Updates the specified service gateway. The information you provide overwrites the existing attributes of the gateway.

Syntax
```

```

Parameters

Parameter Description

`service_gateway_id`

(required) The service gateway's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_service_gateway_details`

(required) Details object for updating a service gateway.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SUBNET Function

Updates the specified subnet.

Syntax
```

```

Parameters

Parameter Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet.

`update_subnet_details`

(required) Details object for updating a subnet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TUNNEL_CPE_DEVICE_CONFIG Function

Creates or updates the set of CPE configuration answers for the specified tunnel. The answers correlate to the questions that are specific to the CPE device type (see the `parameters` attribute of`CPE_DEVICE_SHAPE_DETAIL`Type).

Syntax
```

```

Parameters

Parameter Description

`ipsc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the IPSec connection.

`tunnel_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the tunnel.

`update_tunnel_cpe_device_config_details`

(required) Request to input the tunnel's cpe configuration parameters

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VCN Function

Updates the specified VCN.

Syntax
```

```

Parameters

Parameter Description

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN.

`update_vcn_details`

(required) Details object for updating a VCN.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VIRTUAL_CIRCUIT Function

Updates the specified virtual circuit. This can be called by either the customer who owns the virtual circuit, or the provider (when provisioning or de-provisioning the virtual circuit from their end). The documentation for`UPDATE_VIRTUAL_CIRCUIT_DETAILS`Function indicates who can update each property of the virtual circuit. **Important:** If the virtual circuit is working and in the PROVISIONED state, updating any of the network-related properties (such as the DRG being used, the BGP ASN, and so on) will cause the virtual circuit's state to switch to PROVISIONING and the related BGP session to go down. After Oracle re-provisions the virtual circuit, its state will return to PROVISIONED. Make sure you confirm that the associated BGP session is back up. For more information about the various states and how to test connectivity, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm). To change the list of public IP prefixes for a public virtual circuit, use`BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES`Function and`BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES`Function. Updating the list of prefixes does NOT cause the BGP session to go down. However, Oracle must verify the customer's ownership of each added prefix before traffic for that prefix will flow across the virtual circuit.

Syntax
```

```

Parameters

Parameter Description

`virtual_circuit_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual circuit.

`update_virtual_circuit_details`

(required) Update VirtualCircuit fields.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VLAN Function

Updates the specified VLAN. Note that this operation might require changes to all the VNICs in the VLAN, which can take a while. The VLAN will be in the UPDATING state until the changes are complete.

Syntax
```

```

Parameters

Parameter Description

`vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN.

`update_vlan_details`

(required) Details object for updating a subnet.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VNIC Function

Updates the specified VNIC.

Syntax
```

```

Parameters

Parameter Description

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

`update_vnic_details`

(required) Details object for updating a VNIC.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VTAP Function

Updates the specified VTAP's display name or tags.

Syntax
```

```

Parameters

Parameter Description

`vtap_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VTAP.

`update_vtap_details`

(required) Details object for updating a VTAP.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPGRADE_DRG Function

Upgrades the DRG. After upgrade, you can control routing inside your DRG via DRG attachments, route distributions, and DRG route tables.

Syntax
```

```

Parameters

Parameter Description

`drg_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DRG.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_BYOIP_RANGE Function

Submits the BYOIP CIDR block you are importing for validation. Do not submit to Oracle for validation if you have not already modified the information for the BYOIP CIDR block with your Regional Internet Registry. See[To import a CIDR block](https://docs.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr)for details.

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### WITHDRAW_BYOIP_RANGE Function

Withdraws BGP route advertisement for the BYOIP CIDR block.

Syntax
```

```

Parameters

Parameter Description

`byoip_range_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `ByoipRange` resource containing the BYOIP CIDR block.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Core Virtual Network Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-57F4B5F3-24BB-45DB-AF70-6A1A649543D6)
- [ADD_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7D4F058B-A070-4CAC-BDDA-4D186D5A4D93)
- [ADD_DRG_ROUTE_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E9A4D582-48F4-4E1A-9DD0-59C6B9508CC2)
- [ADD_IPV6_SUBNET_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6852CF2B-7F9A-4485-A5EF-CBDA9AA46DFF)
- [ADD_IPV6_VCN_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-EBD5FD5D-3471-40DA-BCD2-86CE0EB39785)
- [ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C70659FB-EA3E-4F8B-AD85-7951F87587BB)
- [ADD_PUBLIC_IP_POOL_CAPACITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D95F1937-3BB6-47A2-B0D3-65ACE6347588)
- [ADD_VCN_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4B8B649A-A579-45B7-8E92-FD3F81C93469)
- [ADVERTISE_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C1936988-3A44-4C4A-9B9B-D1E6D151C06F)
- [ATTACH_SERVICE_ID Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-80984875-0289-4026-8631-8501015F56EC)
- [BULK_ADD_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-61DC41E0-F1D9-45E7-862A-108385C7D7B3)
- [BULK_DELETE_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F583C2BE-A384-4FFB-82BE-1DE1D27B965F)
- [CHANGE_BYOIP_RANGE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-88374F0B-52EE-4C9C-A373-2943E32DEFC1)
- [CHANGE_CAPTURE_FILTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D11CACC0-DD39-42C2-9378-DA72F677C1DE)
- [CHANGE_CPE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0E27EF74-0441-4159-988B-D00E15FCCA44)
- [CHANGE_CROSS_CONNECT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DB69E08A-EC84-4352-8D83-BA2BCB3B911D)
- [CHANGE_CROSS_CONNECT_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7243D20F-D4AA-469D-AEDF-74816CD41F06)
- [CHANGE_DHCP_OPTIONS_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-BF6A82C2-9A8B-4865-996D-B9416578DC5C)
- [CHANGE_DRG_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3F9986D3-6036-47B5-B321-8FE9C12BFEAF)
- [CHANGE_IP_SEC_CONNECTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-31CC3422-4B13-46CD-8082-7A9B56EE396C)
- [CHANGE_INTERNET_GATEWAY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7C0DD3B2-81E7-4C4C-A188-54FB0066223A)
- [CHANGE_LOCAL_PEERING_GATEWAY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6E3DAE42-09CE-412A-ABCF-CB50512E3911)
- [CHANGE_NAT_GATEWAY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-74350F83-819D-4D5A-B097-3988AE1B15BF)
- [CHANGE_NETWORK_SECURITY_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7817CE39-70D3-4C14-9FE7-3DBA3D01BDEB)
- [CHANGE_PUBLIC_IP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B3A92E2E-0BFB-452F-8A89-95ECE20BFDDE)
- [CHANGE_PUBLIC_IP_POOL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2BA3239B-8945-4560-981D-6D26FAD0E4A4)
- [CHANGE_REMOTE_PEERING_CONNECTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FDD65043-1539-44DE-9543-9CC0E7A2C079)
- [CHANGE_ROUTE_TABLE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7B2B3D50-3110-441E-971D-78F3BAD7AD06)
- [CHANGE_SECURITY_LIST_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2BF9807F-7AE3-4CFD-92BD-707C1630E359)
- [CHANGE_SERVICE_GATEWAY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9B4D51BC-8F93-476A-9BEE-5F175352A79F)
- [CHANGE_SUBNET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FE15CA19-4D73-47CC-820B-C3CFDC6F3085)
- [CHANGE_VCN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-553AC13F-8B22-4A52-9CB1-805C1A0F2A51)
- [CHANGE_VIRTUAL_CIRCUIT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9F082A46-E745-4524-B7A3-14A03CF0597D)
- [CHANGE_VLAN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E78FF9E0-706D-4602-8E9E-E360E7694242)
- [CHANGE_VTAP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5328EF50-9B05-47EC-A0B5-2E3B46869BF1)
- [CONNECT_LOCAL_PEERING_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-05F21120-BA62-41DF-8835-664E55F9CBA0)
- [CONNECT_REMOTE_PEERING_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0527F31A-7810-4C26-8BBD-C732292FE997)
- [CREATE_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CD7E362A-B880-4655-A226-B285D6CF9C22)
- [CREATE_CAPTURE_FILTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-388B75F0-ADE6-4383-91C8-84C00CBC6745)
- [CREATE_CPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E380B3BD-DCE5-49FE-B992-63026D084A8A)
- [CREATE_CROSS_CONNECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CA9A34C1-3664-47F5-B3F0-78AA412F0149)
- [CREATE_CROSS_CONNECT_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-AC9FD366-E32F-4CFE-8E30-A9E86423715C)
- [CREATE_DHCP_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F7737973-4273-493A-BF68-DC9EEE2A929D)
- [CREATE_DRG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6A86D572-0A92-4E1B-8898-B500686A9D37)
- [CREATE_DRG_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-92703FD6-0B5E-4006-8D91-B0309910010A)
- [CREATE_DRG_ROUTE_DISTRIBUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DE1B10EC-507B-4A73-B76E-5C23EAB78F83)
- [CREATE_DRG_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5A791610-3027-4CE4-B900-C1511B7DD9AD)
- [CREATE_IP_SEC_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-787DE744-4DFE-4863-951D-B6638DC1F8D8)
- [CREATE_INTERNET_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-25C3A278-0FD4-492C-A13E-BA2560A8833A)
- [CREATE_IPV6 Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4B0131EC-2EA2-472E-8BC3-BA85DF833BA8)
- [CREATE_LOCAL_PEERING_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D7C78F53-2332-4AF7-86C5-C9F2F32D8CF4)
- [CREATE_NAT_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DFCA2023-DF95-45E1-B802-6977F96412FE)
- [CREATE_NETWORK_SECURITY_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B34D682D-1890-4A69-8A0D-0618085EFDB1)
- [CREATE_PRIVATE_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-15B8DEE8-3AA0-42C8-BD30-85497B7E6963)
- [CREATE_PUBLIC_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A6661949-52DB-488D-8C15-25979F256E6F)
- [CREATE_PUBLIC_IP_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-EECC197A-D63E-48BB-BD20-1C23A6C58DD1)
- [CREATE_REMOTE_PEERING_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-1F86345D-BDCA-43AC-9F6C-30D7F305F305)
- [CREATE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DE44002A-CB6D-4256-9596-D68551D799F5)
- [CREATE_SECURITY_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-77C4268A-7F10-46D7-8ED6-1EE284ED6208)
- [CREATE_SERVICE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-60A6C64A-E0F9-4501-B39A-4E42EC3004DE)
- [CREATE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CB9D7B78-313A-4FCD-8E4C-08C21DF91A86)
- [CREATE_VCN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-20633F01-1D66-4D3A-9665-875BA0048C03)
- [CREATE_VIRTUAL_CIRCUIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A6F09A9C-CB6E-40BD-870C-587A893D7CB7)
- [CREATE_VLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6B810206-4FB9-4C0B-8BF6-3C8F90635F67)
- [CREATE_VTAP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-27684C62-A293-4B3F-A55F-34FFC0DF249A)
- [DELETE_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B0966490-1977-4BC1-BB10-880EF26D54F1)
- [DELETE_CAPTURE_FILTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0308F575-6AF4-4C02-9F34-FA0F0F052B5E)
- [DELETE_CPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B88DEEBC-A289-4E92-84AB-2BB875D631A1)
- [DELETE_CROSS_CONNECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FFA5CA32-6267-4BAD-86CB-1A4EDE4A40E4)
- [DELETE_CROSS_CONNECT_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6FD66CF5-25F3-4FB2-97F3-20A2E5ECDB6D)
- [DELETE_DHCP_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0480AA2D-0A22-49F0-B3A8-3F4F72E6630D)
- [DELETE_DRG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7A41273C-BF00-44C2-BA3B-557EA4EBD4DB)
- [DELETE_DRG_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6E3E4C2A-5167-4FD8-9314-72FCA3517062)
- [DELETE_DRG_ROUTE_DISTRIBUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F23C7FB9-6155-4F79-94C0-E2EF268342C0)
- [DELETE_DRG_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C2A556B0-015E-4DE6-A16E-4EEA78F8D0EE)
- [DELETE_IP_SEC_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-13AC687A-E35D-43C0-8D74-3B00781AA3A9)
- [DELETE_INTERNET_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5E0E1086-5BB6-491D-B19E-3AF6A42BF02F)
- [DELETE_IPV6 Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2322DD8E-B372-4423-BA1B-FD67E31E3E47)
- [DELETE_LOCAL_PEERING_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E8A954FE-1598-499E-A4F5-9AB4BB4CDE9C)
- [DELETE_NAT_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-473277F5-0E26-4E5E-906B-872F32C91544)
- [DELETE_NETWORK_SECURITY_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-BE3570F3-9AE3-4C8E-8B45-4C054AF8CEBF)
- [DELETE_PRIVATE_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8BF2070B-A71F-402E-866C-FF35BF48906C)
- [DELETE_PUBLIC_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FC251808-46FF-4090-B616-944AFBDFB53C)
- [DELETE_PUBLIC_IP_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D6459172-5CE8-45FD-856C-4011205ECDA3)
- [DELETE_REMOTE_PEERING_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D7970D1F-AF29-4DDE-A6BD-3DA4DF15DF9D)
- [DELETE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-45D86887-38A1-4355-A842-D927F9212C8E)
- [DELETE_SECURITY_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2056F043-0277-4D54-B066-8809859C9079)
- [DELETE_SERVICE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A9211537-F9A2-4DFC-BCBA-8E5170DD62CB)
- [DELETE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CBF19F4E-5896-4C3D-8427-F99DE1D2C486)
- [DELETE_VCN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A749CC58-126F-4210-88CC-3017F73CFFA3)
- [DELETE_VIRTUAL_CIRCUIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3939B28A-19CC-4283-ABAC-DFFD625E4ABD)
- [DELETE_VLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-1AECD260-F33F-43EA-90A0-194EAE8C0189)
- [DELETE_VTAP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4745A054-CD87-4BD6-A001-11E2A47C2E84)
- [DETACH_SERVICE_ID Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-84CB3E95-44DC-4451-99C3-73340E128B9A)
- [GET_ALL_DRG_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-AB395239-8F61-4575-BBA8-171D0C3E2B03)
- [GET_ALLOWED_IKE_IP_SEC_PARAMETERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4C3F8E38-03CE-494B-8C42-9ECC47394683)
- [GET_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-04388C68-7E3B-472B-A023-2E642FABFB97)
- [GET_CAPTURE_FILTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-EE1619E9-1EED-4F1E-AFD1-03F0F7DCBB08)
- [GET_CPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CC3756A5-7448-423B-BAF8-0786C11BFA77)
- [GET_CPE_DEVICE_CONFIG_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8EDCED24-9E81-4009-83D6-BDB9A4185977)
- [GET_CPE_DEVICE_SHAPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DAB7DEFE-12FB-481F-8EA1-F16E26583136)
- [GET_CROSS_CONNECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2429BD71-A7EB-4763-8351-4EF47F757CA3)
- [GET_CROSS_CONNECT_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F3BD85E9-9944-475E-870D-FFCE968D4CD3)
- [GET_CROSS_CONNECT_LETTER_OF_AUTHORITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3087B494-7BEC-4EC1-A367-8AD23C4D3278)
- [GET_CROSS_CONNECT_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-EAA79ED7-7986-4C03-9279-DC62546E47C9)
- [GET_DHCP_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D41A00EC-679D-48D5-8447-96976FBFABD1)
- [GET_DRG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9C8C569D-5CE5-41BA-B61B-571F57076267)
- [GET_DRG_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E828A8F2-4937-438A-81B5-75EDFF532978)
- [GET_DRG_REDUNDANCY_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CB0E4CCD-5903-406B-8F81-F59938F4F5C6)
- [GET_DRG_ROUTE_DISTRIBUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B539A5F5-5E12-415C-825A-5E36E39232CF)
- [GET_DRG_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A954D550-CAAE-4482-913C-8400D34BAF95)
- [GET_FAST_CONNECT_PROVIDER_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2CF6D662-B12F-4DC1-8F56-8C7121236148)
- [GET_FAST_CONNECT_PROVIDER_SERVICE_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2EEF1705-3CA1-4237-8578-A897CA52C0A4)
- [GET_IP_SEC_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2BE846B7-DF8F-4C78-A9EF-72E7334BD0AE)
- [GET_IP_SEC_CONNECTION_DEVICE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-63624164-6BB6-4104-B010-D81EE98E9AC8)
- [GET_IP_SEC_CONNECTION_DEVICE_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5BF509CA-4793-4B23-8221-8ADC499B07C0)
- [GET_IP_SEC_CONNECTION_TUNNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4227A7FB-50E9-47A5-9FFC-BC10B1FE8DF4)
- [GET_IP_SEC_CONNECTION_TUNNEL_ERROR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6D515927-9314-45A3-9132-E1984F2F81C9)
- [GET_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-57CFDA51-2E08-4BEE-AA05-9B598BD2F1BA)
- [GET_INTERNET_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2FFE9D84-A382-475C-8E1F-F9B149B1EE93)
- [GET_IPSEC_CPE_DEVICE_CONFIG_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A8E14E3D-6270-4BF3-BB3A-D681B419B52D)
- [GET_IPV6 Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F1784E69-5087-4F0D-954C-B7A323C8223E)
- [GET_LOCAL_PEERING_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-78110B6D-E83B-40F8-A752-89690A7FC6B3)
- [GET_NAT_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C48D1807-29BD-45D5-8227-5505C55C3E7F)
- [GET_NETWORK_SECURITY_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3ED3527A-EAB5-4689-9FC7-827C48E1E55E)
- [GET_NETWORKING_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-11836CE6-A7A9-4C94-8717-D149723A55BA)
- [GET_PRIVATE_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-84B0040B-854D-4F76-BF4D-21BCCFC41F43)
- [GET_PUBLIC_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-18B0A82F-0880-4E19-907D-AAA8A2F8F00D)
- [GET_PUBLIC_IP_BY_IP_ADDRESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-632162FF-9CD3-48F7-A3D0-9F1E5A81D1D3)
- [GET_PUBLIC_IP_BY_PRIVATE_IP_ID Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-24E77816-2E02-4AD1-BFC9-E856CD42E45F)
- [GET_PUBLIC_IP_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0B1642EC-AA79-4CB3-BF46-290ACCE37B69)
- [GET_REMOTE_PEERING_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FC751F64-E3BF-41F5-9B42-267036253288)
- [GET_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-1FB431CF-B147-4969-B58F-16697D7E86F6)
- [GET_SECURITY_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DE975307-A520-49B3-82BC-EB5FEB9038BE)
- [GET_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-360919DE-022E-46D2-8E36-798E6C5EC648)
- [GET_SERVICE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-83011D6A-18A3-4CA0-8E14-14366DF2A1E9)
- [GET_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-11A8DD56-939D-4419-B6C5-021B8649BB07)
- [GET_SUBNET_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-16F8CCA2-C33D-4859-B4AD-5CAF9730D6B5)
- [GET_TUNNEL_CPE_DEVICE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E6D55218-CBBA-4D22-9521-A76B241418B0)
- [GET_TUNNEL_CPE_DEVICE_CONFIG_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C811E6D8-3770-471D-B421-40C02F18084B)
- [GET_UPGRADE_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3F4EDD3F-F27A-4913-BEBA-9849434D5FEF)
- [GET_VCN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6AEAA823-9145-4DE2-9B38-BE9CF3F6A028)
- [GET_VCN_DNS_RESOLVER_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2F33C8BD-97EB-4DD6-94C7-F70C65ADC54C)
- [GET_VCN_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-23EAD27C-8F73-4DD0-A060-E9F77C8D839B)
- [GET_VIRTUAL_CIRCUIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-58B69673-B6ED-41AD-8860-F56AEA3C5E5F)
- [GET_VLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D8D7A015-1B5E-4515-910D-BF1E3CB44838)
- [GET_VNIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C936D0EA-8CE8-44FA-BA80-D980569EB8E5)
- [GET_VTAP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9BF5BDBE-D081-4A16-BBC0-04B0594507F5)
- [LIST_ALLOWED_PEER_REGIONS_FOR_REMOTE_PEERING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2ABCD2A6-B74D-482F-AEC0-24972D7255AD)
- [LIST_BYOIP_ALLOCATED_RANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E5FD5B19-BCE5-429F-B6FC-F4F860A85910)
- [LIST_BYOIP_RANGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-71096E2D-865B-414E-8330-E5CEC38792E3)
- [LIST_CAPTURE_FILTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9E87499C-44B0-4A1A-BFD1-05B69A9C6C43)
- [LIST_CPE_DEVICE_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D39EC13B-BB93-449F-B7A2-D52B1C01762F)
- [LIST_CPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-90657F90-B3BE-4120-8B01-BF936068B2E4)
- [LIST_CROSS_CONNECT_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DFAD3884-8E88-4ED5-BB03-CB90CB21C8EF)
- [LIST_CROSS_CONNECT_LOCATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5E1E4863-0508-4510-AAF9-1D6D881EBF5F)
- [LIST_CROSS_CONNECT_MAPPINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F439DEE1-693D-4C82-A06A-6ED65A16AA3B)
- [LIST_CROSS_CONNECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-051C1E95-1418-4D5C-BDD0-6A8E377747CF)
- [LIST_CROSSCONNECT_PORT_SPEED_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8EDD2B95-31A0-4570-A941-8607D7CC45B3)
- [LIST_DHCP_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-66E98508-944F-45E0-B7B8-B36AE128AC1E)
- [LIST_DRG_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0CEA8433-0C13-493E-9846-E9E139EC14BD)
- [LIST_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7AC0409A-FB13-4B44-9731-A459E14FF452)
- [LIST_DRG_ROUTE_DISTRIBUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D8E2A886-C66D-4D57-A5F4-3A60A57D0A6B)
- [LIST_DRG_ROUTE_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E6F93E76-DE6D-4D3A-B04C-1BE71C17EB45)
- [LIST_DRG_ROUTE_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-620FC421-148E-4040-B91D-CFFA67265823)
- [LIST_DRGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C42CA9AB-88D2-485C-9B7F-DD88DCC9BB11)
- [LIST_FAST_CONNECT_PROVIDER_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2AA48D29-0B22-4D9B-939B-A04B91E6D294)
- [LIST_FAST_CONNECT_PROVIDER_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-081185E9-4ADB-4D75-B426-AD294D1A530D)
- [LIST_IP_SEC_CONNECTION_TUNNEL_ROUTES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A61C39BE-73D8-4968-99DE-948D01798275)
- [LIST_IP_SEC_CONNECTION_TUNNEL_SECURITY_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8E02350A-3347-42D0-AF2B-25FB5403F853)
- [LIST_IP_SEC_CONNECTION_TUNNELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-28FF6772-8B8D-485B-AF75-41FBBD107471)
- [LIST_IP_SEC_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-EB8155D8-F751-4F6E-B7CE-C1169F303E7C)
- [LIST_INTERNET_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-0865F2A3-5D5E-4D6C-97C6-A275EC637E3C)
- [LIST_IPV6S Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-07F8D86C-CB45-4247-A290-2B8C4F5B6002)
- [LIST_LOCAL_PEERING_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8134BD9C-FD73-471A-9AF5-028D51CB0F41)
- [LIST_NAT_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-1BE2D448-B901-4FBC-8119-E13263C69443)
- [LIST_NETWORK_SECURITY_GROUP_SECURITY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-09D29C55-39B1-4F03-8F75-C1E9FA60636F)
- [LIST_NETWORK_SECURITY_GROUP_VNICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F883E671-7121-4085-B195-D99069994829)
- [LIST_NETWORK_SECURITY_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C6627565-8634-48AA-A54A-0AFF521136B0)
- [LIST_PRIVATE_IPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7B7BC80F-3509-47E1-95AD-BD81EDC180B9)
- [LIST_PUBLIC_IP_POOLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D1C83A29-B339-4834-A8B7-929FE6865A3C)
- [LIST_PUBLIC_IPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5B0B0600-1CC6-4F13-B2DC-4F2EED7BE533)
- [LIST_REMOTE_PEERING_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-CCCB30A3-70F8-4330-8719-237BC75C2CFC)
- [LIST_ROUTE_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6130BD96-7292-4425-AC2A-23B9A60658FB)
- [LIST_SECURITY_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-7D98580E-7992-4C88-836E-CF0916A7F5D2)
- [LIST_SERVICE_GATEWAYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-768557E5-68A5-44A8-B4D8-A99E85149497)
- [LIST_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4A293634-6A3D-45EB-A26B-225600B4172F)
- [LIST_SUBNETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-88815DFC-F2A6-43D2-83CA-C97F26005397)
- [LIST_VCNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-06D202B8-8716-41C9-BA97-6597BB7DB4FC)
- [LIST_VIRTUAL_CIRCUIT_ASSOCIATED_TUNNELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3947843E-29C8-4807-ABA1-7F945FE02E44)
- [LIST_VIRTUAL_CIRCUIT_BANDWIDTH_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-BE23C262-7599-42B2-B4C8-9AE2C5AC1D62)
- [LIST_VIRTUAL_CIRCUIT_PUBLIC_PREFIXES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-340AD5A1-3BE7-4303-B0B0-CAD74F04B7EB)
- [LIST_VIRTUAL_CIRCUITS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D393776E-C03B-4175-A0D4-CBDDA6B77484)
- [LIST_VLANS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4F62E7AD-0EE3-4CAE-8700-AE8B19C36D59)
- [LIST_VTAPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-638A88AD-44FB-429D-82F3-7B4593418829)
- [MODIFY_VCN_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E90879E6-5764-44FE-8982-BE5047CDAFC2)
- [REMOVE_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3F7B6172-F651-4ABA-BB38-168458D5ED51)
- [REMOVE_DRG_ROUTE_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-DA790640-1808-4601-B0B9-018EA4C3A4E9)
- [REMOVE_EXPORT_DRG_ROUTE_DISTRIBUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6D75E2E5-54B4-4369-8475-0EE853B65DD8)
- [REMOVE_IMPORT_DRG_ROUTE_DISTRIBUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3608AF6B-C9BE-453B-842C-FA31883B6F8D)
- [REMOVE_IPV6_SUBNET_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2B3DF342-8DBD-4926-AAE7-A279B0B52DC9)
- [REMOVE_IPV6_VCN_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-3D66A7DA-5A0A-430B-8958-C9A2D6ABCD30)
- [REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-99AED690-03DC-4D92-94AE-68B1ABA6F314)
- [REMOVE_PUBLIC_IP_POOL_CAPACITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-113533BA-B363-4AE6-AD45-6E80EEFAB7B6)
- [REMOVE_VCN_CIDR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4D206B3C-FCAB-4C6E-931C-5B4614317B86)
- [UPDATE_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-C050E2C9-7660-41E4-B811-3F64B341ECCC)
- [UPDATE_CAPTURE_FILTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-090C501F-4E81-414B-AFEA-701CB1029214)
- [UPDATE_CPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-88927D16-2791-423D-B1C7-DEA92ACAEE8E)
- [UPDATE_CROSS_CONNECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-5E9E8DDD-F62C-4B3D-BC2A-43EEFFEF7F4D)
- [UPDATE_CROSS_CONNECT_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6625906B-FAD4-45C7-B79D-DD16D43975B2)
- [UPDATE_DHCP_OPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2EBDA89F-1695-41F0-B189-D5AB69E9C79C)
- [UPDATE_DRG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B886C20D-E840-42EC-828D-15696392CDFE)
- [UPDATE_DRG_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8908E0EC-A3F4-48F9-B07D-BAE4B09BFB47)
- [UPDATE_DRG_ROUTE_DISTRIBUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-D2775E84-9FBD-4CC1-A958-45672F5593A4)
- [UPDATE_DRG_ROUTE_DISTRIBUTION_STATEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FE8A39AD-0E16-4247-83DE-97513933A3D2)
- [UPDATE_DRG_ROUTE_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F699D335-310E-47B7-B6AC-3D6E3799BC35)
- [UPDATE_DRG_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-FDD868D8-8E45-4E60-A1CE-BCB9371A6F94)
- [UPDATE_IP_SEC_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A05265AD-9F0B-433F-8B68-E2ECEACF3923)
- [UPDATE_IP_SEC_CONNECTION_TUNNEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9248D99C-A8C0-4898-92A6-FBA7BD9AFD5C)
- [UPDATE_IP_SEC_CONNECTION_TUNNEL_SHARED_SECRET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-1EFB237E-2AB1-47A5-A85C-185D96FBC695)
- [UPDATE_INTERNET_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-46F4E610-C7A9-48B1-B1A6-5D37D53E913B)
- [UPDATE_IPV6 Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B3DDCF7F-F3BC-46B0-8A91-472653B21CCF)
- [UPDATE_LOCAL_PEERING_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-8DD55546-7E12-4DC9-AD24-C3E1F8A0FE7E)
- [UPDATE_NAT_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-A2ECAFC8-352D-4092-BFE2-C6748C02FF7E)
- [UPDATE_NETWORK_SECURITY_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-096CD7DA-F7AA-4D0C-9FB8-B308DAED5EE0)
- [UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-E14B0272-0BEE-4924-A2CF-39F0FC98EE77)
- [UPDATE_PRIVATE_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-EDA64BDB-7116-4326-95A6-54DBEE43391C)
- [UPDATE_PUBLIC_IP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-06ECD18C-1918-4CA9-8D50-42E0F1B785B0)
- [UPDATE_PUBLIC_IP_POOL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2E5F4280-0CFD-4F36-8BDC-C841555354A0)
- [UPDATE_REMOTE_PEERING_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B42EBD24-982B-4DE9-A585-E7D57BAD8C54)
- [UPDATE_ROUTE_TABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-26C633DB-AB42-4921-98EB-9FDD67FC8C8B)
- [UPDATE_SECURITY_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-94602C0D-C537-46A9-875B-D33BCB465A04)
- [UPDATE_SERVICE_GATEWAY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-F03118D6-CEB2-442E-A84C-B5237E0D28AD)
- [UPDATE_SUBNET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-4E6875A2-559B-44FC-94E4-CAEEE4B3964A)
- [UPDATE_TUNNEL_CPE_DEVICE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-2D1F507A-0D33-479C-B2EA-F076B5BBCA8F)
- [UPDATE_VCN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-AA80D201-695D-4308-8F5C-2FC902FFBCDC)
- [UPDATE_VIRTUAL_CIRCUIT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B105CE32-FF26-43A6-B5DF-CFB32970509D)
- [UPDATE_VLAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-9B136E46-87BC-4D8F-8031-6100AABBE160)
- [UPDATE_VNIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-1497D2B0-EAF4-44BC-80C7-A38CF71CBF6B)
- [UPDATE_VTAP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-B54AAD6A-109B-436A-A98D-583C5EF4E1C1)
- [UPGRADE_DRG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-BD50D668-6376-4E91-A87C-17C3D79FB364)
- [VALIDATE_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-6907AC4D-9DC5-4459-B1A2-1C509B7AE816)
- [WITHDRAW_BYOIP_RANGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_virtual_network.html#ADSDK-GUID-74BD929A-FF99-4436-B0D2-056BDDE7E4F2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
