# OpenSearch Cluster Backup Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html#dcoc-content-body)

## OpenSearch Cluster Backup Functions

Package: DBMS_CLOUD_OCI_OPS_OPENSEARCH_CLUSTER_BACKUP

### DELETE_OPENSEARCH_CLUSTER_BACKUP Function

Deletes a OpensearchClusterBackup resource by identifier

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_backup_id`

(required) unique OpensearchClusterBackup identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OPENSEARCH_CLUSTER_BACKUP Function

Gets a OpensearchClusterBackup by identifier

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_backup_id`

(required) unique OpensearchClusterBackup identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OPENSEARCH_CLUSTER_BACKUPS Function

Returns a list of OpensearchClusterBackups.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`source_opensearch_cluster_id`

(optional) A filter to return only resources that match the entire source cluster id given.

`id`

(optional) unique OpensearchClusterBackup identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

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

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OPENSEARCH_CLUSTER_BACKUP Function

Updates the OpensearchClusterBackup

Syntax
```

```

Parameters

Parameter Description

`opensearch_cluster_backup_id`

(required) unique OpensearchClusterBackup identifier

`update_opensearch_cluster_backup_details`

(required) Update the opensearch cluster backup details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://search-indexing.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OpenSearch Cluster Backup Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html#ADSDK-GUID-D82591F7-2E7A-4B4A-8B83-EEBFE432BBCA)
- [DELETE_OPENSEARCH_CLUSTER_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html#ADSDK-GUID-34C80305-A659-41C5-A262-282A83C622CB)
- [GET_OPENSEARCH_CLUSTER_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html#ADSDK-GUID-7A17A7D9-9CEA-44C3-88DC-8984BC202459)
- [LIST_OPENSEARCH_CLUSTER_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html#ADSDK-GUID-DC7DF5B6-15B1-4235-BAE3-473BCDCA45DB)
- [UPDATE_OPENSEARCH_CLUSTER_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ops_opensearch_cluster_backup.html#ADSDK-GUID-26E7F6A8-0A56-42CF-9131-65383B6B1A95)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
