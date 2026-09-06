# Usage Resources Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_resources.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_resources.html#dcoc-content-body)

## Usage Resources Functions

Package: DBMS_CLOUD_OCI_US_RESOURCES

### LIST_RESOURCE_QUOTA Function

Returns the resource quota details under a tenancy &gt; **Important**: Calls to this API will only succeed against the endpoint in the home region.

Syntax
```

```

Parameters

Parameter Description

`service_name`

(required) Service Name.

`compartment_id`

(required) The OCID of the root compartment.

`opc_request_id`

(optional) Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`service_entitlement`

(optional) Service entitlement Id.

`page`

(optional) The value of the 'opc-next-page' response header from the previous call.

`limit`

(optional) The maximum number of items to return in the paginated response.

`sort_order`

(optional) The sort order to use, which can be ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Supports one sort order.

Allowed values are: 'TIMECREATED', 'TIMESTART'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCES Function

Returns the resource details for a service &gt; **Important**: Calls to this API will only succeed against the endpoint in the home region.

Syntax
```

```

Parameters

Parameter Description

`service_name`

(required) Service Name.

`compartment_id`

(required) The OCID of the root compartment.

`entitlement_id`

(optional) Subscription or entitlement Id.

`opc_request_id`

(optional) Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the 'opc-next-page' response header from the previous call.

`limit`

(optional) The maximum number of items to return in the paginated response.

`sort_order`

(optional) The sort order to use, which can be ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Supports one sort order.

Allowed values are: 'TIMECREATED', 'TIMESTART'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Usage Resources Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_resources.html#ADSDK-GUID-DAEF6D8D-8D84-4CDA-BFB7-3D32EE944FED)
- [LIST_RESOURCE_QUOTA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_resources.html#ADSDK-GUID-D16C2C9F-8F58-485B-8B2E-8A92E6D45714)
- [LIST_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_resources.html#ADSDK-GUID-E92C7ECB-50FE-4A03-BF70-068A7ED0BBF1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
