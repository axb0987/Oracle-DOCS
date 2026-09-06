# One Subscription Organization Subscription Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_organization_subscription.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_organization_subscription.html#dcoc-content-body)

## One Subscription Organization Subscription Functions

Package: DBMS_CLOUD_OCI_OS_ORGANIZATION_SUBSCRIPTION

### LIST_ORGANIZATION_SUBSCRIPTIONS Function

API that returns data for the list of subscription ids returned from Organizations API

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: '500'

`page`

(optional) The value of the 'opc-next-page' response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending ('ASC') or descending ('DESC').

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order ('sortOrder').

Allowed values are: 'ORDERNUMBER', 'TIMEINVOICING'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [One Subscription Organization Subscription Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_organization_subscription.html#ADSDK-GUID-3CE1A7E7-5439-4C8C-AC70-A24B59C3C058)
- [LIST_ORGANIZATION_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_organization_subscription.html#ADSDK-GUID-BAC1E91B-75C1-411F-9771-DD086C5895D6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
