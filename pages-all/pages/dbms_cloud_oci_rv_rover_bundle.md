# Roving Edge Infrastructure Bundle Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#dcoc-content-body)

## Roving Edge Infrastructure Bundle Functions

Package: DBMS_CLOUD_OCI_RV_ROVER_BUNDLE

### LIST_ROVER_CLUSTER_ROVER_BUNDLE_REQUESTS Function

List all the roverBundleRequests for a given roverClusterId.

Syntax
```

```

Parameters

Parameter Description

`rover_cluster_id`

(required) Unique RoverCluster identifier

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeTaskCreated is descending. If no value is specified timeTaskCreated is default.

Allowed values are: 'timeTaskCreated'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROVER_NODE_ROVER_BUNDLE_REQUESTS Function

List all the roverBundleRequests for a given roverNodeId.

Syntax
```

```

Parameters

Parameter Description

`rover_node_id`

(required) Unique RoverNode identifier

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeTaskCreated is descending. If no value is specified timeTaskCreated is default.

Allowed values are: 'timeTaskCreated'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_BUNDLE_ROVER_CLUSTER Function

Request to get rover bundle to the bucket in customer's tenancy.

Syntax
```

```

Parameters

Parameter Description

`request_rover_bundle_details`

(required) Request the rover bundle details.

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

### REQUEST_BUNDLE_ROVER_NODE Function

Request to get rover bundle to the bucket in customer's tenancy.

Syntax
```

```

Parameters

Parameter Description

`request_rover_bundle_details`

(required) Request the rover bundle details.

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

### RETRIEVE_AVAILABLE_BUNDLE_VERSIONS_ROVER_CLUSTER Function

Retrieve the latest available rover bundle version that can be upgraded to based on current bundle version.

Syntax
```

```

Parameters

Parameter Description

`current_rover_bundle_details`

(required) Provide the current rover bundle details.

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

### RETRIEVE_AVAILABLE_BUNDLE_VERSIONS_ROVER_NODE Function

Retrieve the latest available rover bundle version that can be upgraded to based on current bundle version.

Syntax
```

```

Parameters

Parameter Description

`current_rover_bundle_details`

(required) Provide the current rover bundle details.

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

### RETRIEVE_BUNDLE_STATUS_ROVER_CLUSTER Function

Retrieve the status and progress of a rover bundle copy request.

Syntax
```

```

Parameters

Parameter Description

`rover_bundle_status_details`

(required) Provide the rover bundle details that requires to retrieve its status.

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

### RETRIEVE_BUNDLE_STATUS_ROVER_NODE Function

Retrieve the status and progress of a rover bundle copy request.

Syntax
```

```

Parameters

Parameter Description

`rover_bundle_status_details`

(required) Provide the rover bundle details that requires to retrieve its status.

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

- [Roving Edge Infrastructure Bundle Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-E9BA87D9-9FBA-435C-AFAD-EA59C28FD1CA)
- [LIST_ROVER_CLUSTER_ROVER_BUNDLE_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-A5C1431B-4159-46C5-AE86-AA46CC688249)
- [LIST_ROVER_NODE_ROVER_BUNDLE_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-DFF7FA59-8906-463D-9123-7AF6B63CF900)
- [REQUEST_BUNDLE_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-A4707693-5F70-4527-942F-30E6B48CAA6F)
- [REQUEST_BUNDLE_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-913B9788-B975-4308-9AD5-42E15DEE0E43)
- [RETRIEVE_AVAILABLE_BUNDLE_VERSIONS_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-577ECB67-48D9-4FCD-BED6-FE22DF655A3F)
- [RETRIEVE_AVAILABLE_BUNDLE_VERSIONS_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-4F6C6811-52F3-432C-BD01-EB18722C66AA)
- [RETRIEVE_BUNDLE_STATUS_ROVER_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-48856C06-9D36-44AF-BEF9-B5E2D3EF805D)
- [RETRIEVE_BUNDLE_STATUS_ROVER_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_bundle.html#ADSDK-GUID-B6DCC912-FEEE-47EC-AC5E-925BC6D1AB6B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
