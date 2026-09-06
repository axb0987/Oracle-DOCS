# OSub Subscription Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_subscription.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_subscription.html#dcoc-content-body)

## OSub Subscription Functions

Package: DBMS_CLOUD_OCI_OSS_SUBSCRIPTION

### LIST_SUBSCRIPTIONS Function

This list API returns all subscriptions for a given plan number or subscription id or buyer email and provides additional parameters to include ratecard and commitment details. This API expects exactly one of the above mentioned parameters as input. If more than one parameters are provided the API will throw a 400 - invalid parameters exception and if no parameters are provided it will throw a 400 - missing parameter exception

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`plan_number`

(optional) The Plan Number

`subscription_id`

(optional) Line level Subscription Id

`buyer_email`

(optional) Buyer Email Id

`is_commit_info_required`

(optional) Boolean value to decide whether commitment services will be shown

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

`x_one_gateway_subscription_id`

(optional) This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is to help on Gateway to API calls identification.

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OSub Subscription Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_subscription.html#ADSDK-GUID-56DF8EE6-42C7-4AA5-8237-1074EAB72401)
- [LIST_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_subscription.html#ADSDK-GUID-24085807-52F6-4789-90D8-D76CAB0AA2E9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
