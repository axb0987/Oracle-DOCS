# Usage Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#dcoc-content-body)

## Usage Common Types

### DBMS_CLOUD_OCI_USAGE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_T Type

The summary of a user that can redeem rewards.

Syntax
```

```

Fields

Field Description

`email_id`

(required) The email ID for a user that can redeem rewards.

`first_name`

(optional) The first name of the user that can redeem rewards.

`last_name`

(optional) The last name of the user that can redeem rewards.

### DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_TBL Type

Nested table type of dbms_cloud_oci_usage_redeemable_user_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_CREATE_REDEEMABLE_USER_DETAILS_T Type

A list of new user to be added to the list of user that can redeem rewards.

Syntax
```

```

Fields

Field Description

`items`

(optional) The list of new user to be added to the list of user that can redeem rewards.

### DBMS_CLOUD_OCI_USAGE_ERROR_T Type

Error object model.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_USAGE_MONTHLY_REWARD_SUMMARY_T Type

Object describing the monthly rewards summary for the requested subscription ID.

Syntax
```

```

Fields

Field Description

`available_rewards`

(optional) The number of rewards available for a specific usage period.

`redeemed_rewards`

(optional) The number of rewards redeemed for a specific month.

`earned_rewards`

(optional) The number of rewards earned for the specific usage period.

`is_manual`

(optional) The boolean parameter to indicate whether or not the available rewards are manually posted.

`time_rewards_expired`

(optional) The date and time when rewards expire.

`time_rewards_earned`

(optional) The date and time when rewards accrue.

`time_usage_started`

(optional) The start date and time for the usage period.

`time_usage_ended`

(optional) The end date and time for the usage period.

`usage_amount`

(optional) The usage amount for the usage period.

`eligible_usage_amount`

(optional) The eligible usage amount for the usage period.

`ineligible_usage_amount`

(optional) The ineligible usage amount for the usage period.

`usage_period_key`

(optional) The usage period ID.

### DBMS_CLOUD_OCI_USAGE_PRODUCT_SUMMARY_T Type

Provides details about product rewards and the usage amount.

Syntax
```

```

Fields

Field Description

`product_number`

(optional) The rate card product number.

`product_name`

(optional) The rate card product name.

`usage_amount`

(optional) The rate card product usage amount.

`earned_rewards`

(optional) The earned rewards for the product.

`is_eligible_to_earn_rewards`

(optional) The boolean parameter to indicate if the product is eligible to earn rewards.

### DBMS_CLOUD_OCI_USAGE_PRODUCT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_product_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_PRODUCT_COLLECTION_T Type

A product list.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of product rewards summaries.

### DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_SUMMARY_T Type

User summary that can redeem rewards.

Syntax
```

```

Fields

Field Description

`email_id`

(optional) The email ID of the user that can redeem rewards.

`first_name`

(optional) The first name of the user that can redeem rewards.

`last_name`

(optional) The last name of the user that can redeem rewards.

### DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_redeemable_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_COLLECTION_T Type

The list of user summary that can redeem rewards.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of user summary that can redeem rewards.

### DBMS_CLOUD_OCI_USAGE_REDEMPTION_SUMMARY_T Type

The redemption summary for the requested subscription ID and date range.

Syntax
```

```

Fields

Field Description

`time_redeemed`

(optional) It provides redeem date.

`redemption_email`

(optional) It provides the redemption email id.

`redemption_code`

(optional) The redemption code used in the Billing Center during the reward redemption process.

`invoice_number`

(optional) It provides the invoice number against the redemption.

`invoice_total_amount`

(optional) It provides the invoice total amount of given redemption.

`invoice_currency`

(optional) The currency associated with invoice.

`redeemed_rewards`

(optional) It provides the redeemed rewards in invoice currency.

`base_rewards`

(optional) It provides the redeemed rewards in base/subscription currency.

`fx_rate`

(optional) It provides the fxRate between invoice currency and subscription currency.

`time_invoiced`

(optional) It provides the invoice date.

### DBMS_CLOUD_OCI_USAGE_REDEMPTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_redemption_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_REDEMPTION_COLLECTION_T Type

The list of redemption summary for the requested subscription ID and date range.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of redemption summary.

### DBMS_CLOUD_OCI_USAGE_RESOURCE_QUOTUM_SUMMARY_T Type

The resource quota balance details.

Syntax
```

```

Fields

Field Description

`name`

(optional) The resource name.

`is_allowed`

(optional) Used to indicate if further quota consumption isAllowed.

`limit`

(optional) The quota limit.

`balance`

(optional) The quota balance.

`is_overage`

(optional) Used to indicate if overages are incurred.

`purchased_limit`

(optional) The purchased quota limit.

`service`

(optional) The service name.

`is_dependency`

(optional) Used to indicate any resource dependencies.

`affected_resource`

(optional) The affected resource name.

### DBMS_CLOUD_OCI_USAGE_RESOURCE_QUOTUM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_resource_quotum_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_RESOURCE_QUOTUM_COLLECTION_T Type

The quota details of resources under a tenancy.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of resource quota details.

`is_allowed`

(required) Used to indicate if further quota consumption isAllowed.

### DBMS_CLOUD_OCI_USAGE_SKU_PRODUCTS_T Type

The SKU Product Id details for a resource.

Syntax
```

```

Fields

Field Description

`sku_id`

(optional) The Sku Id for the resource.

`sku_type`

(optional) The Sku type for the resource.

`cloud_credit_type`

(optional) The cloud credit type for the resource.

### DBMS_CLOUD_OCI_USAGE_SKU_PRODUCTS_TBL Type

Nested table type of dbms_cloud_oci_usage_sku_products_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_RESOURCE_SUMMARY_T Type

The details of a resource under a service.

Syntax
```

```

Fields

Field Description

`daily_unit_display_name`

(optional) Units to be used for daily aggregated data.

`hourly_unit_display_name`

(optional) Units to be used for hourly aggregated data.

`raw_unit_display_name`

(optional) Default units to use when unspecified.

`usage_data_type`

(optional) Usage data type of the resource.

Allowed values are: 'INTERVAL', 'POINT_DATA'

`name`

(optional) Name of the resource.

`servicename`

(optional) Name of the service.

`description`

(optional) Description of the resource.

`instance_type`

(optional) Instance type for the resource.

`is_purchased`

(optional) Indicates if the SKU was purchased

`child_resources`

(optional) The details of any child resources.

`skus`

(optional) The details of resource Skus.

### DBMS_CLOUD_OCI_USAGE_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_RESOURCES_COLLECTION_T Type

The resources of a service.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of resource details for a service.

### DBMS_CLOUD_OCI_USAGE_REWARD_DETAILS_T Type

The overall monthly reward summary.

Syntax
```

```

Fields

Field Description

`tenancy_id`

(optional) The OCID of the target tenancy.

`subscription_id`

(optional) The entitlement ID from MQS, which is the same as the subcription ID.

`currency`

(optional) The currency unit for the reward amount.

`rewards_rate`

(optional) The current Rewards percentage in decimal format.

`total_rewards_available`

(optional) The total number of available rewards for a given subscription ID.

`redemption_code`

(optional) The redemption code used in the Billing Center during the reward redemption process.

### DBMS_CLOUD_OCI_USAGE_MONTHLY_REWARD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_monthly_reward_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_REWARD_COLLECTION_T Type

The response object for the ListRewards API call. Provides information about the subscription rewards.

Syntax
```

```

Fields

Field Description

`summary`

(required)

`items`

(optional) The monthly summary of rewards.

### DBMS_CLOUD_OCI_USAGE_USAGE_LIMIT_SUMMARY_T Type

Encapsulates a collection of Hard and Soft Limits for a resource within a subscription.

Syntax
```

```

Fields

Field Description

`time_created`

(required) Time when the usage limit was created

`entitlement_id`

(required) Entitlement ID of the usage limit

`id`

(required) The usage limit ID

`time_modified`

(required) Time when the usage limit was modified

`resource_name`

(required) The resource for which the limit is defined

`service_name`

(required) The service for which the limit is defined

`limit`

(required) The limit value

`created_by`

(required) The user who created the limit

`modified_by`

(required) The user who modified the limit

`action`

(required) The action when usage limit is hit

Allowed values are: 'QUOTA_BREACH', 'QUOTA_ALERT'

`alert_level`

(required) The alert level of the usage limit

`limit_type`

(required) The limit type of the usage limit

Allowed values are: 'HARD', 'SOFT'

`value_type`

(required) The value type of the usage limit

Allowed values are: 'ABSOLUTE', 'PERCENTAGE'

`lifecycle_state`

(required) The usage limit lifecycle state.

Allowed values are: 'ACTIVE'

`max_hard_limit`

(optional) The maximum hard limit set for the usage limit

`sku_part_id`

(optional) The SKU for which the usage limit is set

### DBMS_CLOUD_OCI_USAGE_USAGE_LIMIT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usage_usage_limit_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGE_USAGE_LIMIT_COLLECTION_T Type

The list of usage limit summary for the requested tenancy ID and subscription ID.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of usage limits.

- [Usage Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-98F6FF81-798C-4075-9AC1-190ED801C190)
- [DBMS_CLOUD_OCI_USAGE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-F3B4D18D-7FDA-49BE-81D0-1B64B5EFA5F2)
- [DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-5D84F20B-AD19-45E0-B01B-58D01EB996E2)
- [DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-2F8EF6DF-71F3-4914-A131-3FFA17952673)
- [DBMS_CLOUD_OCI_USAGE_CREATE_REDEEMABLE_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-3B2F0A62-7F0E-483B-A2A1-6C0606BF547C)
- [DBMS_CLOUD_OCI_USAGE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-3B417A75-7ED0-40C2-BFB2-5D60A38BAA25)
- [DBMS_CLOUD_OCI_USAGE_MONTHLY_REWARD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-F0B26338-DFD2-46AA-8144-4D9649CB6D6E)
- [DBMS_CLOUD_OCI_USAGE_PRODUCT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-D5B5A660-5771-434A-922A-E5EFF9A41224)
- [DBMS_CLOUD_OCI_USAGE_PRODUCT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-DD3DF9AF-3691-427A-BA06-30EE330EF13A)
- [DBMS_CLOUD_OCI_USAGE_PRODUCT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-66212226-50F6-4D81-ABAE-C3919856D2D0)
- [DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-033E6AB8-5267-4DCC-9F02-64839DBBA7D5)
- [DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-A41E8F6F-8B08-4329-B6CF-EA1538E0BBD4)
- [DBMS_CLOUD_OCI_USAGE_REDEEMABLE_USER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-F7ED7812-5402-4925-BF9E-7B79F7C0FE69)
- [DBMS_CLOUD_OCI_USAGE_REDEMPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-07D403DA-FD60-4C5E-8DD4-69C96D7B3960)
- [DBMS_CLOUD_OCI_USAGE_REDEMPTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-B84D09E3-4C1D-40DC-B424-B2B92E1605E4)
- [DBMS_CLOUD_OCI_USAGE_REDEMPTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-59D2A5A8-9218-4115-8F09-E2CCFB43A0D3)
- [DBMS_CLOUD_OCI_USAGE_RESOURCE_QUOTUM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-8DA93FF5-BBAD-4AEC-ACC2-113BFE565416)
- [DBMS_CLOUD_OCI_USAGE_RESOURCE_QUOTUM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-CF82043D-31F8-4CC9-9804-5D983EC2B152)
- [DBMS_CLOUD_OCI_USAGE_RESOURCE_QUOTUM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-5E10CF60-E91F-40A8-8808-6264799E7252)
- [DBMS_CLOUD_OCI_USAGE_SKU_PRODUCTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-5FEDD3C0-744B-479B-845E-F605AEBE8C80)
- [DBMS_CLOUD_OCI_USAGE_SKU_PRODUCTS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-93BD836D-B8F1-4A74-8540-38637AD00178)
- [DBMS_CLOUD_OCI_USAGE_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-00080386-8A5B-42CB-A7C1-903EA6BE8156)
- [DBMS_CLOUD_OCI_USAGE_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-DAA6F9BC-11E0-412E-8C60-36B9A2431146)
- [DBMS_CLOUD_OCI_USAGE_RESOURCES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-104CDE31-61DA-4B6C-A5B9-72738AE259C4)
- [DBMS_CLOUD_OCI_USAGE_REWARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-2E2C17C2-6C04-4DC6-9F5E-A780391990C5)
- [DBMS_CLOUD_OCI_USAGE_MONTHLY_REWARD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-B3FF759D-1EA7-4986-BC09-BFC4613185BE)
- [DBMS_CLOUD_OCI_USAGE_REWARD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-2AE39894-AC39-4CAA-9DB1-D3BC8555ABF5)
- [DBMS_CLOUD_OCI_USAGE_USAGE_LIMIT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-84660FCE-629F-4008-B4DB-2019AA33D987)
- [DBMS_CLOUD_OCI_USAGE_USAGE_LIMIT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-23B813C7-643E-4A23-AE91-692027A9BE70)
- [DBMS_CLOUD_OCI_USAGE_USAGE_LIMIT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usage_t.html#ADSDK-GUID-1599D85A-BE87-4A0F-ABD6-B334734CFDCF)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
