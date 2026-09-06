# OSub Organization Subscription Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osos_organization_subscription.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osos_organization_subscription.html#dcoc-content-body)

## OSub Organization Subscription Functions

Package: DBMS_CLOUD_OCI_OSOS_ORGANIZATION_SUBSCRIPTION

### LIST_ORGANIZATION_SUBSCRIPTIONS Function

API that returns data for the list of subscription ids returned from Organizations API

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`subscription_ids`

(required) Comma separated list of subscription ids

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: `500`

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`).

Allowed values are: 'SUBSCRIPTIONID', 'TIMESTART'

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

- [OSub Organization Subscription Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osos_organization_subscription.html#ADSDK-GUID-94C0F946-F30D-4B80-A78A-5E0D35FF5C44)
- [LIST_ORGANIZATION_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osos_organization_subscription.html#ADSDK-GUID-6C89B774-E572-4FF5-9189-C60C667BFC96)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
