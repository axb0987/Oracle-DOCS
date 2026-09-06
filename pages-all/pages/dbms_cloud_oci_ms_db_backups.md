# MySQL DB Backups Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#dcoc-content-body)

## MySQL DB Backups Functions

Package: DBMS_CLOUD_OCI_MS_DB_BACKUPS

### CHANGE_BACKUP_COMPARTMENT Function

Moves a DB System Backup into a different compartment. When provided, If-Match is checked against ETag values of the Backup.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The OCID of the Backup

`change_backup_compartment_details`

(required) Target compartment for a DB System Backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

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

### CREATE_BACKUP Function

Create a backup of a DB System.

Syntax
```

```

Parameters

Parameter Description

`create_backup_details`

(required) Create a Backup of a DB System.

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

### DELETE_BACKUP Function

Delete a Backup.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The OCID of the Backup

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

### GET_BACKUP Function

Get information about the specified Backup

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The OCID of the Backup

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

### LIST_BACKUPS Function

Get a list of DB System backups.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Customer-defined unique identifier for the request. If you need to contact Oracle about a specific request, please provide the request ID that you supplied in this header with the request.

`backup_id`

(optional) Backup OCID

`lifecycle_state`

(optional) Backup Lifecycle State

`db_system_id`

(optional) The DB System[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`display_name`

(optional) A filter to return only the resource matching the given display name exactly.

`creation_type`

(optional) Backup creationType

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending.

Allowed values are: 'timeCreated', 'timeUpdated', 'displayName'

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

### UPDATE_BACKUP Function

Update the metadata of a Backup. Metadata such as the displayName or description

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The OCID of the Backup

`update_backup_details`

(required) Request to update a Backup's metadata.

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

- [MySQL DB Backups Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-FC1CFA23-F672-44B7-B4FD-4BAF0EA3EF60)
- [CHANGE_BACKUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-793CB20B-8875-4B35-8863-74A14FA810B6)
- [CREATE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-7B041B17-4E21-4A61-AC7D-1BE9B1606AF4)
- [DELETE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-0E49534D-F12C-49CE-AA06-44D14361F431)
- [GET_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-E70379DB-EDA0-48AB-AC23-4C73EABACE70)
- [LIST_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-C54C9B51-1796-4383-B13C-2B3E8F3BDA1F)
- [UPDATE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ms_db_backups.html#ADSDK-GUID-D0C8BD5C-381A-4DBD-A945-BD7A128BF6FE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
