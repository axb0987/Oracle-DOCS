# MySQL Replicas Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#dcoc-content-body)

## MySQL Replicas Functions

Package: DBMS_CLOUD_OCI_MS_REPLICAS

### CREATE_REPLICA Function

Creates a DB System read replica.

Syntax
```

```

Parameters

Parameter Description

`create_replica_details`

(required) The parameters of the request to create the read replica.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPLICA Function

Deletes the specified read replica.

Syntax
```

```

Parameters

Parameter Description

`replica_id`

(required) The Replica[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPLICA Function

Gets the full details of the specified read replica.

Syntax
```

```

Parameters

Parameter Description

`replica_id`

(required) The Replica[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`if_none_match`

(optional) For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPLICAS Function

Lists all the read replicas that match the specified filters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`limit`

(optional) The maximum number of items to return in a paginated list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`page`

(optional) The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`display_name`

(optional) A filter to return only the resource matching the given display name exactly.

`db_system_id`

(optional) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`lifecycle_state`

(optional) The LifecycleState of the read replica.

`replica_id`

(optional) The read replica[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`configuration_id`

(optional) The requested Configuration instance.

`is_up_to_date`

(optional) Filter instances if they are using the latest revision of the Configuration they are associated with.

`sort_by`

(optional) The field to sort by. You can sort by one field only. By default, the Time field is sorted in descending order and the Display Name field in ascending order.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use (ASC or DESC).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REPLICA Function

Updates the properties of the specified read replica.

Syntax
```

```

Parameters

Parameter Description

`replica_id`

(required) The Replica[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_replica_details`

(required) The parameters of the request to update the read replica.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [MySQL Replicas Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#ADSDK-GUID-6ADC552B-1184-4256-9CB8-AC3DF1EDCDD3)
- [CREATE_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#ADSDK-GUID-1D0AD4C0-9588-4931-AAE5-69DD37193AF4)
- [DELETE_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#ADSDK-GUID-80CC2C52-FC13-4067-80FA-302EB46F2813)
- [GET_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#ADSDK-GUID-EF9EC7F7-C001-43C2-BF81-71BCF66C496D)
- [LIST_REPLICAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#ADSDK-GUID-FDB97A34-7FD1-46DD-9840-A577920C2144)
- [UPDATE_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_replicas.html#ADSDK-GUID-FB6226AD-89BC-4789-B9CA-07A2794DEB5E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
