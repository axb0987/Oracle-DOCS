# MySQL MySQLaaS Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#dcoc-content-body)

## MySQL MySQLaaS Functions

Package: DBMS_CLOUD_OCI_MS_MYSQLAAS

### CREATE_CONFIGURATION Function

Creates a new Configuration.

Syntax
```

```

Parameters

Parameter Description

`create_configuration_details`

(required) Request to create a Configuration.

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

### DELETE_CONFIGURATION Function

Deletes a Configuration. The Configuration must not be in use by any DB Systems.

Syntax
```

```

Parameters

Parameter Description

`configuration_id`

(required) The OCID of the Configuration.

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

### GET_CONFIGURATION Function

Get the full details of the specified Configuration, including the list of MySQL Variables and their values.

Syntax
```

```

Parameters

Parameter Description

`configuration_id`

(required) The OCID of the Configuration.

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

### LIST_CONFIGURATIONS Function

Lists the Configurations available when creating a DB System. This may include DEFAULT configurations per Shape and CUSTOM configurations. The default sort order is a multi-part sort by: - shapeName, ascending - DEFAULT-before-CUSTOM - displayName ascending

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`configuration_id`

(optional) The requested Configuration instance.

`lifecycle_state`

(optional) Configuration Lifecycle State

`l_type`

(optional) The requested Configuration types.

Allowed values are: 'DEFAULT', 'CUSTOM'

`display_name`

(optional) A filter to return only the resource matching the given display name exactly.

`shape_name`

(optional) The requested Shape name.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as ascending.

Allowed values are: 'displayName', 'shapeName', 'timeCreated', 'timeUpdated'

`sort_order`

(optional) The sort order to use (ASC or DESC).

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return in a paginated list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`page`

(optional) The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SHAPES Function

Gets a list of the shapes you can use to create a new MySQL DB System. The shape determines the resources allocated to the DB System: CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`is_supported_for`

(optional) Return shapes that are supported by the service feature.

Allowed values are: 'DBSYSTEM', 'HEATWAVECLUSTER'

`availability_domain`

(optional) The name of the Availability Domain.

`name`

(optional) Name

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VERSIONS Function

Get a list of supported and available MySQL database major versions. The list is sorted by version family.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mysql.{region}.ocp.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONFIGURATION Function

Updates the Configuration details.

Syntax
```

```

Parameters

Parameter Description

`configuration_id`

(required) The OCID of the Configuration.

`update_configuration_details`

(required) Request to update a Configuration.

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

- [MySQL MySQLaaS Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-F2C61FB2-E26A-4E22-AF0B-2931BC702999)
- [CREATE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-839C1B4A-2143-4C90-B948-5468FB4BE8AB)
- [DELETE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-A957009B-A00F-4442-838A-1F6BBAD8F6F2)
- [GET_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-A9FEA8E1-06D7-44EE-B954-D49E8CD81BB8)
- [LIST_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-8970DBBD-4601-490E-9550-F2E3F53CAED1)
- [LIST_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-683ED46A-5A0E-4574-A19A-8C2F9EFA4132)
- [LIST_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-999BA64A-2316-4843-A985-EE6AD4B06B49)
- [UPDATE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_mysqlaas.html#ADSDK-GUID-EA1868DE-AF34-4769-B010-14879809F5C5)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
