# OSub Subscription Ratecard Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_ratecard.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_ratecard.html#dcoc-content-body)

## OSub Subscription Ratecard Functions

Package: DBMS_CLOUD_OCI_OSS_RATECARD

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

(required) The OCID of the compartment.

`time_from`

(optional) This param is used to get the rate card(s) whose effective start date starts on or after a particular date

`time_to`

(optional) This param is used to get the rate card(s) whose effective end date ends on or before a particular date

`part_number`

(optional) This param is used to get the rate card(s) filterd by the partNumber

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: `500`

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`).

Allowed values are: 'TIMECREATED', 'TIMESTART'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OSub Subscription Ratecard Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_ratecard.html#ADSDK-GUID-849A1E3A-EBEE-41EE-8F4B-822EA91322E7)
- [LIST_RATE_CARDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_ratecard.html#ADSDK-GUID-4D07F38F-3137-47AE-ABF7-003049E7817E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
