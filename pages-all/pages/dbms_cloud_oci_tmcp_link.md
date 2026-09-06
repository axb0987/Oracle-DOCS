# Tenant Manager Control Plane Link Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_link.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_link.html#dcoc-content-body)

## Tenant Manager Control Plane Link Functions

Package: DBMS_CLOUD_OCI_TMCP_LINK

### DELETE_LINK Function

Starts the link termination workflow.

Syntax
```

```

Parameters

Parameter Description

`link_id`

(required) OCID of the link to terminate.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LINK Function

Gets information about the link.

Syntax
```

```

Parameters

Parameter Description

`link_id`

(required) OCID of the link to retrieve.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LINKS Function

Return a (paginated) list of links.

Syntax
```

```

Parameters

Parameter Description

`parent_tenancy_id`

(optional) The ID of the parent tenancy this link is associated with.

`child_tenancy_id`

(optional) The ID of the child tenancy this link is associated with.

`lifecycle_state`

(optional) The lifecycle state of the resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

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

- [Tenant Manager Control Plane Link Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_link.html#ADSDK-GUID-B1A8681E-B49D-493D-8037-9C0AF512C1CA)
- [DELETE_LINK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_link.html#ADSDK-GUID-9A7C609F-6CC3-43C3-AC05-4632F4B6C9FE)
- [GET_LINK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_link.html#ADSDK-GUID-04A4FD63-D67F-415F-8084-37C120540669)
- [LIST_LINKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_link.html#ADSDK-GUID-7F961230-5A13-4D03-B20C-903E97869BD1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
