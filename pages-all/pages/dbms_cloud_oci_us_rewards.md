# Usage Rewards Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#dcoc-content-body)

## Usage Rewards Functions

Package: DBMS_CLOUD_OCI_US_REWARDS

### CREATE_REDEEMABLE_USER Function

Adds the list of redeemable user summary for a subscription ID.

Syntax
```

```

Parameters

Parameter Description

`create_redeemable_user_details`

(required) CreateRedeemableUserDetails information.

`tenancy_id`

(required) The OCID of the tenancy.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

`user_id`

(optional) The user ID of the person to send a copy of an email.

`opc_request_id`

(optional) Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REDEEMABLE_USER Function

Deletes the list of redeemable user email ID for a subscription ID.

Syntax
```

```

Parameters

Parameter Description

`email_id`

(required) The email ID that needs to be deleted.

`tenancy_id`

(required) The OCID of the tenancy.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

`opc_request_id`

(optional) Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRODUCTS Function

Provides product information that is specific to a reward usage period and its usage details.

Syntax
```

```

Parameters

Parameter Description

`tenancy_id`

(required) The OCID of the tenancy.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

`usage_period_key`

(required) The SPM Identifier for the usage period.

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

`producttype`

(optional) The field to specify the type of product.

Allowed values are: 'ALL', 'ELIGIBLE', 'INELIGIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REDEEMABLE_USERS Function

Provides the list of user summary that can redeem rewards for the given subscription ID.

Syntax
```

```

Parameters

Parameter Description

`tenancy_id`

(required) The OCID of the tenancy.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

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

### LIST_REDEMPTIONS Function

Returns the list of redemption for the subscription ID.

Syntax
```

```

Parameters

Parameter Description

`tenancy_id`

(required) The OCID of the tenancy.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

`time_redeemed_greater_than_or_equal_to`

(optional) The starting redeemed date filter for the redemption history.

`time_redeemed_less_than`

(optional) The ending redeemed date filter for the redemption history.

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

(optional) The field to be used only for list redemptions API. Supports one sort order.

Allowed values are: 'TIMEREDEEMED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REWARDS Function

Returns the list of rewards for a subscription ID.

Syntax
```

```

Parameters

Parameter Description

`tenancy_id`

(required) The OCID of the tenancy.

`subscription_id`

(required) The subscription ID for which rewards information is requested for.

`opc_request_id`

(optional) Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Usage Rewards Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-C2572776-63F2-47FB-B2CA-6985B94A7344)
- [CREATE_REDEEMABLE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-AE77E8DF-2E46-43F5-99C4-989E529A267F)
- [DELETE_REDEEMABLE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-C039F999-56E0-4650-BDEC-9791B8BC826E)
- [LIST_PRODUCTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-E1BAD6E4-57C6-48AD-BFDE-8734FC4495F8)
- [LIST_REDEEMABLE_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-BD1D607B-1AA6-40EE-89B8-7C911B4A97D0)
- [LIST_REDEMPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-97F9C69C-D969-4DBD-BD4D-D91E06F88F33)
- [LIST_REWARDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_us_rewards.html#ADSDK-GUID-F17AA5A8-AF5D-496E-A789-B25472D02B4F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
