# Roving Edge Infrastructure Cluster Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#dcoc-content-body)

## Roving Edge Infrastructure Cluster Functions

Package: DBMS_CLOUD_OCI_RV_ROVER_CLUSTER

### CHANGE_ROVER_CLUSTER_COMPARTMENT Function

Moves a cluster into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

`change_rover_cluster_compartment_details`

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

### CREATE_ROVER_CLUSTER Function

Creates a new RoverCluster.

Syntax
```

```

Parameters

Parameter Description

`create_rover_cluster_details`

(required) Details for the new RoverCluster.

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

### DELETE_ROVER_CLUSTER Function

Deletes a RoverCluster resource by identifier

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

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

### GET_ROVER_CLUSTER Function

Gets a RoverCluster by identifier

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROVER_CLUSTER_CERTIFICATE Function

Get the certificate for a rover cluster

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROVER_CLUSTERS Function

Returns a list of RoverClusters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`cluster_type`

(optional) A filter to return only Clusters of type matched with the given cluster type.

Allowed values are: 'STANDALONE', 'STATION'

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

### REQUEST_ADDITIONAL_NODES Function

Submit additional nodes request for a roverCluster.

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

`request_additional_nodes_details`

(required) Details object to request additional nodes.

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

### UPDATE_ROVER_CLUSTER Function

Updates the RoverCluster

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

`update_rover_cluster_details`

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

- [Roving Edge Infrastructure Cluster Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-E332719E-482F-42FD-A657-F63CDB92F69D)
- [CHANGE_ROVER_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-FE9E13CA-222E-44D4-962A-D579FA7376FF)
- [CREATE_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-387A1965-68CC-4284-9064-930CD6044852)
- [DELETE_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-4E3013E3-BA08-43A2-8D3C-562F79A9EF71)
- [GET_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-843C77D5-0D2C-44CC-A1DB-1AA4E3B9E781)
- [GET_ROVER_CLUSTER_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-C7737D1A-7A74-4917-BA0F-F031A60CA9E8)
- [LIST_ROVER_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-E1663AA9-754C-4667-AB9E-A157FD289F64)
- [REQUEST_ADDITIONAL_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-45DCAC56-3EF8-49BA-8430-6273A9DA1741)
- [UPDATE_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_cluster.html#ADSDK-GUID-F59017D6-7147-437E-A09D-847489FACEC0)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
