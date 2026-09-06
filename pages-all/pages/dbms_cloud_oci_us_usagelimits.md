# Usage Limits Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_usagelimits.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_usagelimits.html#dcoc-content-body)

## Usage Limits Functions

Package: DBMS_CLOUD_OCI_US_USAGELIMITS

### LIST_USAGE_LIMITS Function

Returns the list of usage limit for the subscription ID and tenant ID.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

`limit_type`

(optional) Hard or soft limit. Hard limits lead to breaches, soft to alerts.

`resource_type`

(optional) Resource Name.

`service_type`

(optional) Service Name.

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

- [Usage Limits Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_usagelimits.html#ADSDK-GUID-6DCFD8B8-952D-4417-A625-DB26FF7CB14A)
- [LIST_USAGE_LIMITS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_usagelimits.html#ADSDK-GUID-33B24EF7-AB5B-4D84-AF22-F76A6348861D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
