# Resource Search Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rs_resource_search.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rs_resource_search.html#dcoc-content-body)

## Resource Search Functions

Package: DBMS_CLOUD_OCI_RS_RESOURCE_SEARCH

### GET_RESOURCE_TYPE Function

Gets detailed information about a resource type by using the resource type name.

Syntax
```

```

Parameters

Parameter Description

`name`

(required) The name of the resource type.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://query.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_TYPES Function

Lists all resource types that you can search or query for.

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) The maximum number of items to return. The value must be between 1 and 1000.

`page`

(optional) The page at which to start retrieving results.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://query.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SEARCH_RESOURCES Function

Queries any and all compartments in the specified tenancy to find resources that match the specified criteria. Results include resources that you have permission to view and can span different resource types. You can also sort results based on a specified resource attribute.

Syntax
```

```

Parameters

Parameter Description

`search_details`

(required) Request parameters that describe query criteria. For more information, see`SEARCH_DETAILS`Function.

`limit`

(optional) The maximum number of items to return. The value must be between 1 and 1000.

`page`

(optional) The page at which to start retrieving results.

`tenant_id`

(optional) The tenancy ID, which can be used to specify a different tenancy (for cross-tenancy authorization) when searching for resources in a different tenancy.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://query.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Resource Search Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rs_resource_search.html#ADSDK-GUID-B00EFEE6-921A-4143-9F87-6FC5BEBA58BE)
- [GET_RESOURCE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rs_resource_search.html#ADSDK-GUID-4DE416C5-B63D-430A-B12D-8A4ADC1A1B26)
- [LIST_RESOURCE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rs_resource_search.html#ADSDK-GUID-D1721CE7-AAF1-4F23-AFE3-011DFE2321C5)
- [SEARCH_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rs_resource_search.html#ADSDK-GUID-27392E71-E44A-4806-8F4D-A43127385D6B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
