# Roving Edge Infrastructure Node Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#dcoc-content-body)

## Roving Edge Infrastructure Node Functions

Package: DBMS_CLOUD_OCI_RV_ROVER_NODE

### CHANGE_ROVER_NODE_COMPARTMENT Function

Moves a rover node into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`change_rover_node_compartment_details`

(required) CompartmentId of the destination compartment

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ROVER_NODE Function

Creates a new RoverNode.

Syntax
```

```

Parameters

Parameter Description

`create_rover_node_details`

(required) Details for the new RoverNode.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ROVER_NODE Function

Deletes a RoverNode resource by identifier

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROVER_NODE Function

Gets a RoverNode by identifier.

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROVER_NODE_CERTIFICATE Function

Get the certificate for a rover node

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROVER_NODE_ENCRYPTION_KEY Function

Get the data encryption key for a rover node.

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Serial number of the rover node.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROVER_NODE_GET_RPT Function

Get the resource principal token for a rover node

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`jwt`

(required) The Java Web Token which is a signature of the request that is signed with the resource's private key This is meant solely in the context of getRpt

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROVER_NODES Function

Returns a list of RoverNodes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`node_type`

(optional) A filter to return only Nodes of type matched with the given node type.

Allowed values are: 'STANDALONE', 'CLUSTERED', 'STATION'

`shape`

(optional) A filter to return only Nodes of type matched with the given node shape.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROVER_NODE_ACTION_RETRIEVE_CA_BUNDLE Function

Retrieve Ca Bundle for a rover node

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROVER_NODE_ACTION_SET_KEY Function

Get the resource principal public key for a rover node

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`jwt`

(required) The Java Web Token which is a signature of the request that is signed with the resource's private key This is meant solely in the context of getRpt

`rover_node_action_set_key_details`

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

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROVER_NODE_GENERATE_CERTIFICATE Function

Request to generate certificate for a roverNode.

Syntax
```

```

Parameters

Parameter Description

`rover_node_generate_certificate_details`

(required) The information provided to generate certificate.

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROVER_NODE_RENEW_CERTIFICATE Function

Request to renew certificate for a roverNode.

Syntax
```

```

Parameters

Parameter Description

`rover_node_renew_certificate_details`

(required) The information provided to renew certificate.

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROVER_NODE_REPLACE_CERTIFICATE_AUTHORITY Function

Request to replace certificate authority for a roverNode.

Syntax
```

```

Parameters

Parameter Description

`rover_node_replace_certificate_authority_details`

(required) The information provided to replace certificate authority.

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROVER_NODE_RETRIEVE_LEAF_CERTIFICATE Function

Retrieve the leaf certificate info for a rover node

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ROVER_NODE Function

Updates the RoverNode

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`update_rover_node_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Roving Edge Infrastructure Node Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-942BC869-2B17-424E-8851-E8C0399F8987)
- [CHANGE_ROVER_NODE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-0BCBDD70-3741-4524-9419-87A7D2672DD5)
- [CREATE_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-4226A1FD-82EF-49B4-B1C9-4361A38B438C)
- [DELETE_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-AA5C13B4-17CB-495B-9B58-6431B72C0FDC)
- [GET_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-D6DC01FD-0228-4B3E-B293-C2C8891C04CA)
- [GET_ROVER_NODE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-5AAB46EE-6943-426D-9B60-DAE96BFA9D0D)
- [GET_ROVER_NODE_ENCRYPTION_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-73BD60C3-F649-42F7-AC59-2101E90B6BF4)
- [GET_ROVER_NODE_GET_RPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-8090A794-8A85-4452-B549-69A3DEC56A47)
- [LIST_ROVER_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-7876642E-61F5-493B-B7DD-A189397309E1)
- [ROVER_NODE_ACTION_RETRIEVE_CA_BUNDLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-D33D11D6-ABF5-4D40-A14C-47836DC1E4CC)
- [ROVER_NODE_ACTION_SET_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-76211C7D-AF4F-49DE-99B4-85A4B96EFBCB)
- [ROVER_NODE_GENERATE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-5584AFAB-B563-4A6D-8D3E-35D741EB955F)
- [ROVER_NODE_RENEW_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-6E7CD648-0D19-4655-98E4-298799E48211)
- [ROVER_NODE_REPLACE_CERTIFICATE_AUTHORITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-0A0A49D6-D34E-4E04-BFCB-0794F8312979)
- [ROVER_NODE_RETRIEVE_LEAF_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-C2FE0418-1E61-44D6-A239-9CA415017306)
- [UPDATE_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_node.html#ADSDK-GUID-3BA650F0-2895-4C1B-AC60-F81C88A8235C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
