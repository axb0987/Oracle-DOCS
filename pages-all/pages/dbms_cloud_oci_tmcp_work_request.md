# Tenant Manager Control Plane Work Request Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html#dcoc-content-body)

## Tenant Manager Control Plane Work Request Functions

Package: DBMS_CLOUD_OCI_TMCP_WORK_REQUEST

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Tenant Manager Control Plane Work Request Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html#ADSDK-GUID-62418E72-F71D-4F6B-8ACE-5913DC19A516)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html#ADSDK-GUID-4334FCBC-DB06-45ED-96C8-11FF4BDE032F)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html#ADSDK-GUID-E6E831F7-0F01-433C-AED0-FE79DEA5B152)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html#ADSDK-GUID-30FBD179-61F6-4780-95A6-87FA9A58599B)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_work_request.html#ADSDK-GUID-1B768844-1E13-418F-9E57-C0723D2010F2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
