# One Subscription Subscription Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscription.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscription.html#dcoc-content-body)

## One Subscription Subscription Functions

Package: DBMS_CLOUD_OCI_OS_SUBSCRIPTION

### LIST_SUBSCRIPTIONS Function

This list API returns all subscriptions for a given plan number or subscription id or buyer email and provides additional parameters to include ratecard and commitment details. This API expects exactly one of the above mentioned parameters as input. If more than one parameters are provided the API will throw a 400 - invalid parameters exception and if no parameters are provided it will throw a 400 - missing parameter exception

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`plan_number`

(optional) The Plan Number

`subscription_id`

(optional) Line level Subscription Id

`buyer_email`

(optional) Buyer Email Id

`is_commit_info_required`

(optional) Boolean value to decide whether commitment services will be shown

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

- [One Subscription Subscription Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscription.html#ADSDK-GUID-FD98F18F-FE9A-48FF-9C08-A306B2E5F690)
- [LIST_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscription.html#ADSDK-GUID-E10A2A76-7959-494B-9EE3-6BA4059E0A49)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
