# OSub Usage Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#dcoc-content-body)

## OSub Usage Common Types

### DBMS_CLOUD_OCI_OSUB_USAGE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_USAGE_PRODUCT_T Type

Product description

Syntax
```

```

Fields

Field Description

`part_number`

(required) Product part number

`name`

(required) Product name

`unit_of_measure`

(optional) Unit of Measure

`provisioning_group`

(optional) Product provisioning group

`billing_category`

(optional) Metered service billing category

`product_category`

(optional) Product category

`ucm_rate_card_part_type`

(optional) Rate card part type of Product

### DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_T Type

Computed Usage Summary object

Syntax
```

```

Fields

Field Description

`time_created`

(optional) Computed Usage created time, expressed in RFC 3339 timestamp format.

`time_updated`

(optional) Computed Usage updated time, expressed in RFC 3339 timestamp format.

`parent_subscribed_service_id`

(optional) Subscribed service line parent id

`parent_product`

(optional)

`plan_number`

(optional) Subscription plan number

`currency_code`

(optional) Currency code

`rate_card_tierd_id`

(optional) References the tier in the ratecard for that usage (OCI will be using the same reference to cross-reference for correctness on the usage csv report), comes from Entity OBSCNTR_IPT_PRODUCTTIER.

`rate_card_id`

(optional) Ratecard Id at subscribed service level

`compute_source`

(optional) SPM Internal compute records source .

`data_center`

(optional) Data Center Attribute as sent by MQS to SPM.

`mqs_message_id`

(optional) MQS Identfier send to SPM , SPM does not transform this attribute and is received as is.

`id`

(required) SPM Internal computed usage Id , 32 character string

`quantity`

(optional) Total Quantity that was used for computation

`usage_number`

(optional) SPM Internal usage Line number identifier in SPM coming from Metered Services entity.

`original_usage_number`

(optional) SPM Internal Original usage Line number identifier in SPM coming from Metered Services entity.

`commitment_service_id`

(optional) Subscribed service commitmentId.

`is_invoiced`

(optional) Invoicing status for the aggregated compute usage

`l_type`

(optional) Usage compute type in SPM.

Allowed values are: 'PROMOTION', 'DO_NOT_BILL', 'USAGE', 'COMMIT', 'OVERAGE', 'PAY_AS_YOU_GO', 'MONTHLY_MINIMUM', 'DELAYED_USAGE_INVOICE_TIMING', 'DELAYED_USAGE_COMMITMENT_EXP', 'ON_ACCOUNT_CREDIT', 'SERVICE_CREDIT', 'COMMITMENT_EXPIRATION', 'FUNDED_ALLOCATION', 'DONOT_BILL_USAGE_POST_TERMINATION', 'DELAYED_USAGE_POST_TERMINATION'

`time_of_arrival`

(optional) Usae computation date, expressed in RFC 3339 timestamp format.

`time_metered_on`

(optional) Metered Service date, expressed in RFC 3339 timestamp format.

`net_unit_price`

(optional) Net Unit Price for the product in consideration, price actual.

`cost_rounded`

(optional) Computed Line Amount rounded.

`cost`

(optional) Computed Line Amount not rounded

`product`

(optional)

`unit_of_measure`

(optional) Unit of Messure

### DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_AGGREGATION_T Type

Computed Usage Aggregation object

Syntax
```

```

Fields

Field Description

`quantity`

(optional) Total Quantity that was used for computation

`product`

(optional)

`data_center`

(optional) Data Center Attribute as sent by MQS to SPM.

`time_metered_on`

(optional) Metered Service date , expressed in RFC 3339 timestamp format.

`net_unit_price`

(optional) Net Unit Price for the product in consideration.

`cost_unrounded`

(optional) Sum of Computed Line Amount unrounded

`cost`

(optional) Sum of Computed Line Amount rounded

`l_type`

(optional) Usage compute type in SPM.

Allowed values are: 'PROMOTION', 'DO_NOT_BILL', 'USAGE', 'COMMIT', 'OVERAGE', 'PAY_AS_YOU_GO', 'MONTHLY_MINIMUM', 'DELAYED_USAGE_INVOICE_TIMING', 'DELAYED_USAGE_COMMITMENT_EXP', 'ON_ACCOUNT_CREDIT', 'SERVICE_CREDIT', 'COMMITMENT_EXPIRATION', 'FUNDED_ALLOCATION', 'DONOT_BILL_USAGE_POST_TERMINATION', 'DELAYED_USAGE_POST_TERMINATION'

### DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_osub_usage_computed_usage_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_AGGREGATED_SUMMARY_T Type

Subscribed Service Contract details

Syntax
```

```

Fields

Field Description

`subscription_id`

(required) Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM

`parent_subscribed_service_id`

(optional) Subscribed service line parent id

`parent_product`

(optional)

`time_start`

(optional) Subscribed services contract line start date, expressed in RFC 3339 timestamp format.

`time_end`

(optional) Subscribed services contract line end date, expressed in RFC 3339 timestamp format.

`plan_number`

(optional) Subscribed service asociated subscription plan number.

`currency_code`

(optional) Currency code

`rate_card_id`

(optional) Inernal SPM Ratecard Id at line level

`pricing_model`

(optional) Subscribed services pricing model

Allowed values are: 'PAY_AS_YOU_GO', 'MONTHLY', 'ANNUAL', 'PREPAID', 'FUNDED_ALLOCATION'

`aggregated_computed_usages`

(optional) Aggregation of computed usages for the subscribed service.

### DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_SUMMARY_T Type

Computed Usage Summary object

Syntax
```

```

Fields

Field Description

`time_created`

(optional) Computed Usage created time, expressed in RFC 3339 timestamp format.

`time_updated`

(optional) Computed Usage updated time, expressed in RFC 3339 timestamp format.

`parent_subscribed_service_id`

(optional) Subscribed service line parent id

`parent_product`

(optional)

`plan_number`

(optional) Subscription plan number

`currency_code`

(optional) Currency code

`rate_card_tierd_id`

(optional) References the tier in the ratecard for that usage (OCI will be using the same reference to cross-reference for correctness on the usage csv report), comes from Entity OBSCNTR_IPT_PRODUCTTIER.

`rate_card_id`

(optional) Ratecard Id at subscribed service level

`compute_source`

(optional) SPM Internal compute records source .

`data_center`

(optional) Data Center Attribute as sent by MQS to SPM.

`mqs_message_id`

(optional) MQS Identfier send to SPM , SPM does not transform this attribute and is received as is.

`computed_usage_id`

(required) SPM Internal computed usage Id , 32 character string

`quantity`

(optional) Total Quantity that was used for computation

`usage_number`

(optional) SPM Internal usage Line number identifier in SPM coming from Metered Services entity.

`original_usage_number`

(optional) SPM Internal Original usage Line number identifier in SPM coming from Metered Services entity.

`commitment_service_id`

(optional) Subscribed service commitmentId.

`is_invoiced`

(optional) Invoicing status for the aggregated compute usage

`l_type`

(optional) Usage compute type in SPM.

Allowed values are: 'PROMOTION', 'DO_NOT_BILL', 'USAGE', 'COMMIT', 'OVERAGE', 'PAY_AS_YOU_GO', 'MONTHLY_MINIMUM', 'DELAYED_USAGE_INVOICE_TIMING', 'DELAYED_USAGE_COMMITMENT_EXP', 'ON_ACCOUNT_CREDIT', 'SERVICE_CREDIT', 'COMMITMENT_EXPIRATION', 'FUNDED_ALLOCATION', 'DONOT_BILL_USAGE_POST_TERMINATION', 'DELAYED_USAGE_POST_TERMINATION'

`time_of_arrival`

(optional) Usae computation date, expressed in RFC 3339 timestamp format.

`time_metered_on`

(optional) Metered Service date, expressed in RFC 3339 timestamp format.

`net_unit_price`

(optional) Net Unit Price for the product in consideration, price actual.

`cost_rounded`

(optional) Computed Line Amount rounded.

`cost`

(optional) Computed Line Amount not rounded

`product`

(optional)

`unit_of_measure`

(optional) Unit of Messure

### DBMS_CLOUD_OCI_OSUB_USAGE_ERROR_T Type

Internal error object model.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

- [OSub Usage Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-4351E0DD-A093-43B6-8939-C161355FB688)
- [DBMS_CLOUD_OCI_OSUB_USAGE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-1012BBF0-F8C3-4F09-8613-C2F9626CB07A)
- [DBMS_CLOUD_OCI_OSUB_USAGE_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-BEE8DC8F-12B1-45F5-A1CF-C29F15BA3887)
- [DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-961709B5-AB08-46C3-863E-89285FE7C5A9)
- [DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-5AD02D41-0002-40D1-8096-7B396B914509)
- [DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-88E41889-B992-4BFD-BB99-177AB7E7273C)
- [DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_AGGREGATED_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-89FC011A-CC7B-4E6F-86E9-48198EDDD50E)
- [DBMS_CLOUD_OCI_OSUB_USAGE_COMPUTED_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-7534C1AF-E2B4-4A73-9E03-795638FA17FF)
- [DBMS_CLOUD_OCI_OSUB_USAGE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_usage_t.html#ADSDK-GUID-3FE18780-A9C0-428C-BB62-41B436CF1362)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
