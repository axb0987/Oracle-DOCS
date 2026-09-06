# One Subscription Ratecard Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_ratecard.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_ratecard.html#dcoc-content-body)

## One Subscription Ratecard Functions

Package: DBMS_CLOUD_OCI_OS_RATECARD

### LIST_RATE_CARDS Function

List API that returns all ratecards for given Subscription Id and Account ID (if provided) and for a particular date range

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) Line level Subscription Id

`compartment_id`

(required) The OCID of the root compartment.

`time_from`

(optional) This param is used to get the rate card(s) whose effective start date starts on or after a particular date

`time_to`

(optional) This param is used to get the rate card(s) whose effective end date ends on or before a particular date

`part_number`

(optional) This param is used to get the rate card(s) filterd by the partNumber

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

- [One Subscription Ratecard Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_ratecard.html#ADSDK-GUID-B753C29B-595E-451B-80BC-9B8151EA3B42)
- [LIST_RATE_CARDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_ratecard.html#ADSDK-GUID-57A0F448-22AB-4EA1-AE40-200F52AF4471)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
