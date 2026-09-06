# One Subscription Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#dcoc-content-body)

## One Subscription Common Types

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_PRODUCT_T Type

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

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_AGGREGATION_T Type

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

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_AGGREGATION_TBL Type

Nested table type of dbms_cloud_oci_onesubscription_computed_usage_aggregation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_AGGREGATED_COMPUTED_USAGE_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_BILLING_SCHEDULE_PRODUCT_T Type

Product description

Syntax
```

```

Fields

Field Description

`part_number`

(required) Indicates the associated AR Invoice Number

`name`

(required) Product name

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_BILLING_SCHEDULE_SUMMARY_T Type

Billing schedule details related to Subscription Id

Syntax
```

```

Fields

Field Description

`subscribed_service_id`

(optional) SPM internal Subscribed Service ID

`time_start`

(optional) Billing schedule start date

`time_end`

(optional) Billing schedule end date

`time_invoicing`

(optional) Billing schedule invoicing date

`invoice_status`

(optional) Billing schedule invoice status

Allowed values are: 'INVOICED', 'NOT_INVOICED'

`quantity`

(optional) Billing schedule quantity

`net_unit_price`

(optional) Billing schedule net unit price

`amount`

(optional) Billing schedule line net amount

`billing_frequency`

(optional) Billing frequency

`ar_invoice_number`

(optional) Indicates the associated AR Invoice Number

`ar_customer_transaction_id`

(optional) Indicates the associated AR Customer transaction id a unique identifier existing on AR.

`order_number`

(optional) Order number associated with the Subscribed Service

`product`

(optional)

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_T Type

Subscribed Service commitment summary

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Commitment ID

`subscribed_service_id`

(optional) SPM internal Subscribed Service ID

`time_start`

(optional) Commitment start date

`time_end`

(optional) Commitment end date

`quantity`

(optional) Commitment quantity

`used_amount`

(optional) Commitment used amount

`available_amount`

(optional) Commitment available amount

`funded_allocation_value`

(optional) Funded Allocation line value example: 12000.00

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_SERVICE_T Type

Subscribed service commitment details

Syntax
```

```

Fields

Field Description

`time_start`

(optional) Commitment start date

`time_end`

(optional) Commitment end date

`quantity`

(optional) Commitment quantity

`available_amount`

(optional) Commitment available amount

`line_net_amount`

(optional) Commitment line net amount

`funded_allocation_value`

(optional) Funded Allocation line value

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_SUMMARY_T Type

Subscribed Service commitment summary

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Commitment ID

`subscribed_service_id`

(optional) SPM internal Subscribed Service ID

`time_start`

(optional) Commitment start date

`time_end`

(optional) Commitment end date

`quantity`

(optional) Commitment quantity

`used_amount`

(optional) Commitment used amount

`available_amount`

(optional) Commitment available amount

`funded_allocation_value`

(optional) Funded Allocation line value example: 12000.00

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_T Type

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

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_ERROR_T Type

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

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_PRODUCT_T Type

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

(required) Unit of Measure

`billing_category`

(optional) Metered service billing category

`product_category`

(optional) Product category

`ucm_rate_card_part_type`

(required) Rate card part type of Product

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICE_LINE_SUMMARY_T Type

Invoice Line

Syntax
```

```

Fields

Field Description

`id`

(required) SPM Invoice Line internal identifier

`product`

(required)

`ar_invoice_number`

(optional) AR Invoice Number for Invoice Line

`data_center`

(required) Data Center Attribute.

`time_start`

(required) Usage start time

`time_end`

(required) Usage end time

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_BUSINESS_PARTNER_T Type

Business partner.

Syntax
```

```

Fields

Field Description

`name`

(optional) Commercial name also called customer name.

`name_phonetic`

(optional) Phonetic name.

`tca_customer_account_number`

(optional) TCA customer account number.

`is_public_sector`

(optional) The business partner is part of the public sector or not.

`is_chain_customer`

(optional) The business partner is chain customer or not.

`customer_chain_type`

(optional) Customer chain type.

`tca_party_number`

(optional) TCA party number.

`tca_party_id`

(optional) TCA party ID.

`tca_customer_account_id`

(optional) TCA customer account ID.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_USER_T Type

User.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name.

`user_name`

(optional) userName.

`first_name`

(optional) First name.

`last_name`

(optional) Last name.

`email`

(optional) Email.

`tca_contact_id`

(optional) TCA contact ID.

`tca_cust_accnt_site_id`

(optional) TCA customer account site ID.

`tca_party_id`

(optional) TCA party ID.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_LOCATION_T Type

Address location.

Syntax
```

```

Fields

Field Description

`address1`

(optional) Address first line.

`address2`

(optional) Address second line.

`postal_code`

(optional) Postal code.

`city`

(optional) City.

`country`

(optional) Country.

`l_region`

(optional) Region.

`tca_location_id`

(optional) TCA Location identifier.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_ADDRESS_T Type

Address.

Syntax
```

```

Fields

Field Description

`location`

(optional)

`name`

(optional) Address name identifier.

`phone`

(optional) Phone.

`is_bill_to`

(optional) Identify as the customer's billing address.

`is_ship_to`

(optional) Identify as the customer's shipping address.

`bill_site_use_id`

(optional) Bill to site use Id.

`service2_site_use_id`

(optional) Service to site use Id.

`tca_cust_acct_site_id`

(optional) TCA customer account site Id.

`tca_party_site_number`

(optional) Party site number.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_PAYMENT_TERM_T Type

Payment Term details

Syntax
```

```

Fields

Field Description

`name`

(required) Payment Term name

`value`

(optional) Payment Term value

`description`

(optional) Payment term Description

`is_active`

(optional) Payment term active flag

`time_created`

(optional) Payment term last update date

`created_by`

(optional) User that created the Payment term

`time_updated`

(optional) Payment term last update date

`updated_by`

(optional) User that updated the Payment term

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_CURRENCY_T Type

Currency details

Syntax
```

```

Fields

Field Description

`name`

(optional) Currency name

`iso_code`

(required) Currency Code

`std_precision`

(optional) Standard Precision of the Currency

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_ORGANIZATION_T Type

Organization details

Syntax
```

```

Fields

Field Description

`name`

(required) Organization name

`l_number`

(required) Organization ID

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICE_LINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_onesubscription_invoice_line_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICE_SUMMARY_T Type

Invoice details

Syntax
```

```

Fields

Field Description

`spm_invoice_number`

(required) SPM Document Number is an functional identifier for invoice in SPM

`ar_invoices`

(optional) AR Invoice Numbers comma separated under one invoice

`bill_to_customer`

(required)

`bill_to_contact`

(required)

`bill_to_address`

(required)

`payment_method`

(required) Payment Method

`payment_term`

(required)

`receipt_method`

(optional) Receipt Method of Payment Mode

`currency`

(required)

`organization`

(required)

`l_type`

(required) Document Type in SPM like SPM Invoice,SPM Credit Memo etc.,

`status`

(required) Document Status in SPM which depicts current state of invoice

`subscription_number`

(required) Invoice associated subscription plan number.

`time_invoice_date`

(required) Invoice Date

`time_created`

(optional) SPM Invocie creation date

`created_by`

(optional) User that executed SPM Invoice process

`time_updated`

(optional) SPM Invoice updated date

`updated_by`

(optional) User that updated SPM Invoice

`invoice_lines`

(optional) Invoice Lines under particular invoice.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICELINE_COMPUTED_USAGE_SUMMARY_T Type

Computed Usage Summary object

Syntax
```

```

Fields

Field Description

`parent_product`

(required)

`product`

(optional)

`quantity`

(required) Total Quantity that was used for computation

`net_unit_price`

(required) Net Unit Price for the product in consideration, price actual.

`time_metered_on`

(required) Metered Service date.

`l_type`

(required) Usage compute type in SPM.

Allowed values are: 'PROMOTION', 'DO_NOT_BILL', 'USAGE', 'COMMIT', 'OVERAGE', 'PAY_AS_YOU_GO', 'MONTHLY_MINIMUM', 'DELAYED_USAGE_INVOICE_TIMING', 'DELAYED_USAGE_COMMITMENT_EXP', 'ON_ACCOUNT_CREDIT', 'SERVICE_CREDIT'

`cost`

(optional) Sum of Usage/Service Billing Line net Amount

`cost_rounded`

(required) Computed Line Amount rounded.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_ORGNIZATION_SUBS_CURRENCY_T Type

Currency details

Syntax
```

```

Fields

Field Description

`name`

(optional) Currency name

`iso_code`

(required) Currency Code

`std_precision`

(optional) Standard Precision of the Currency

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_ORGANIZATION_SUBSCRIPTION_SUMMARY_T Type

Subscription summary

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Subscription ID

`service_name`

(optional) Customer friendly service name provided by PRG

`l_type`

(optional) Subscription Type i.e. IAAS,SAAS,PAAS

`status`

(optional) Status of the plan

`time_start`

(optional) Represents the date when the first service of the subscription was activated

`time_end`

(optional) Represents the date when the last service of the subscription ends

`currency`

(optional)

`total_value`

(optional) Total aggregate TCLV of all lines for the subscription including expired, active, and signed

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_PRODUCT_T Type

Product description

Syntax
```

```

Fields

Field Description

`part_number`

(required) Product part numner

`name`

(required) Product name

`unit_of_measure`

(required) Unit of measure

`billing_category`

(optional) Metered service billing category

`product_category`

(optional) Product category

`ucm_rate_card_part_type`

(optional) Rate card part type of Product

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_CURRENCY_T Type

Currency details

Syntax
```

```

Fields

Field Description

`name`

(optional) Currency name

`iso_code`

(required) Currency Code

`std_precision`

(optional) Standard Precision of the Currency

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_TIER_T Type

Rate Card Tier details

Syntax
```

```

Fields

Field Description

`up_to_quantity`

(optional) Rate card tier quantity range

`net_unit_price`

(optional) Rate card tier net unit price

`overage_price`

(optional) Rate card tier overage price

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_TIER_TBL Type

Nested table type of dbms_cloud_oci_onesubscription_rate_card_tier_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_SUMMARY_T Type

Rate Card Summary

Syntax
```

```

Fields

Field Description

`subscribed_service_id`

(optional) SPM internal Subscribed Service ID

`product`

(required)

`time_start`

(optional) Rate card start date

`time_end`

(optional) Rate card end date

`net_unit_price`

(required) Rate card net unit price

`discretionary_discount_percentage`

(optional) Rate card discretionary discount percentage

`overage_price`

(required) Rate card overage price

`is_tier`

(optional) Rate card price tier flag

`currency`

(optional)

`rate_card_tiers`

(optional) List of tiered rate card prices

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_BUSINESS_PARTNER_T Type

Business partner.

Syntax
```

```

Fields

Field Description

`name`

(optional) Commercial name also called customer name.

`name_phonetic`

(optional) Phonetic name.

`tca_cust_account_number`

(optional) TCA customer account number.

`is_public_sector`

(optional) The business partner is part of the public sector or not.

`is_chain_customer`

(optional) The business partner is chain customer or not.

`customer_chain_type`

(optional) Customer chain type.

`tca_party_number`

(optional) TCA party number.

`tca_party_id`

(optional) TCA party ID.

`tca_customer_account_id`

(optional) TCA customer account ID.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_USER_T Type

User.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name.

`username`

(optional) Username.

`first_name`

(optional) First name.

`last_name`

(optional) Last name.

`email`

(optional) Email.

`tca_contact_id`

(optional) TCA contact ID.

`tca_cust_accnt_site_id`

(optional) TCA customer account site ID.

`tca_party_id`

(optional) TCA party ID.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_LOCATION_T Type

Address location.

Syntax
```

```

Fields

Field Description

`address1`

(optional) Address first line.

`address2`

(optional) Address second line.

`postal_code`

(optional) Postal code.

`city`

(optional) City.

`country`

(optional) Country.

`l_region`

(optional) Region.

`tca_location_id`

(optional) Region.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_ADDRESS_T Type

Address.

Syntax
```

```

Fields

Field Description

`location`

(optional)

`name`

(optional) Address name identifier.

`phone`

(optional) Phone.

`is_bill_to`

(optional) Identify as the customer shipping address.

`is_ship_to`

(optional) Identify as the customer invoicing address.

`bill_site_use_id`

(optional) Bill to site use Id.

`service2_site_use_id`

(optional) Service to site use Id.

`tca_cust_acct_site_id`

(optional) TCA customer account site Id.

`tca_party_site_number`

(optional) Party site number.

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_PAYMENT_TERM_T Type

Payment Term details

Syntax
```

```

Fields

Field Description

`name`

(optional) Payment Term name

`value`

(optional) Payment Term value

`description`

(optional) Payment term Description

`is_active`

(optional) Payment term active flag

`time_created`

(optional) Payment term last update date

`created_by`

(optional) User that created the Payment term

`time_updated`

(optional) Payment term last update date

`updated_by`

(optional) User that updated the Payment term

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_SERVICE_TBL Type

Nested table type of dbms_cloud_oci_onesubscription_commitment_service_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_onesubscription_rate_card_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_T Type

Subscribed service contract details

Syntax
```

```

Fields

Field Description

`id`

(optional) SPM internal Subscribed Service ID

`l_type`

(optional) Subscribed Service line type

`serial_number`

(optional) Subscribed service line number

`subscription_id`

(optional) Subscription ID associated to the subscribed service

`product`

(optional)

`time_start`

(optional) Subscribed service start date

`time_end`

(optional) Subscribed service end date

`quantity`

(optional) Subscribed service quantity

`status`

(optional) Subscribed service status

`operation_type`

(optional) Subscribed service operation type

`net_unit_price`

(optional) Subscribed service net unit price

`price_period`

(optional) Indicates the period for which the commitment amount can be utilised exceeding which the amount lapses. Also used in calculation of total contract line value

`line_net_amount`

(optional) Subscribed service line net amount

`is_variable_commitment`

(optional) Indicates if the commitment lines can have different quantities

`is_allowance`

(optional) Indicates if a service can recieve usages and consequently have available amounts computed

`used_amount`

(optional) Subscribed service used amount

`available_amount`

(optional) Subscribed sercice available or remaining amount

`funded_allocation_value`

(optional) Funded Allocation line value example: 12000.00

`is_having_usage`

(optional) Indicator on whether or not there has been usage for the subscribed service

`is_cap_to_price_list`

(optional) If true compares rate between ratecard and the active pricelist and minimum rate would be fetched

`credit_percentage`

(optional) Subscribed service credit percentage

`partner_transaction_type`

(optional) This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ

`is_credit_enabled`

(optional) Used in context of service credit lines

`overage_policy`

(optional) Overage Policy of Subscribed Service

`overage_bill_to`

(optional) Overage Bill To of Subscribed Service

`payg_policy`

(optional) Pay As You Go policy of Subscribed Service (Can be null - indicating no payg policy)

`promo_order_line_id`

(optional) Not null if this service has an associated promotion line in SPM. Contains the line identifier from Order Management of the associated promo line.

`promotion_pricing_type`

(optional) Promotion Pricing Type of Subscribed Service (Can be null - indicating no promotion pricing)

`rate_card_discount_percentage`

(optional) Subscribed service Rate Card Discount Percentage

`overage_discount_percentage`

(optional) Subscribed service Overage Discount Percentage

`bill_to_customer`

(optional)

`bill_to_contact`

(optional)

`bill_to_address`

(optional)

`payment_number`

(optional) Payment Number of Subscribed Service

`time_payment_expiry`

(optional) Subscribed service payment expiry date

`payment_term`

(optional)

`payment_method`

(optional) Payment Method of Subscribed Service

`transaction_extension_id`

(optional) Subscribed service Transaction Extension Id

`sales_channel`

(optional) Sales Channel of Subscribed Service

`eligible_to_renew`

(optional) Subscribed service eligible to renew field

`renewed_subscribed_service_id`

(optional) SPM renewed Subscription ID

`term_value`

(optional) Term value in Months

`term_value_uom`

(optional) Term value UOM

`renewal_opty_id`

(optional) Subscribed service Opportunity Id

`renewal_opty_number`

(optional) Renewal Opportunity Number of Subscribed Service

`renewal_opty_type`

(optional) Renewal Opportunity Type of Subscribed Service

`booking_opty_number`

(optional) Booking Opportunity Number of Subscribed Service

`revenue_line_id`

(optional) Subscribed service Revenue Line Id

`revenue_line_number`

(optional) Revenue Line NUmber of Subscribed Service

`major_set`

(optional) Subscribed service Major Set

`time_majorset_start`

(optional) Subscribed service Major Set Start date

`time_majorset_end`

(optional) Subscribed service Major Set End date

`system_arr_in_lc`

(optional) Subscribed service System ARR

`system_arr_in_sc`

(optional) Subscribed service System ARR in Standard Currency

`system_atr_arr_in_lc`

(optional) Subscribed service System ATR-ARR

`system_atr_arr_in_sc`

(optional) Subscribed service System ATR-ARR in Standard Currency

`revised_arr_in_lc`

(optional) Subscribed service Revised ARR

`revised_arr_in_sc`

(optional) Subscribed service Revised ARR in Standard Currency

`total_value`

(optional) Subscribed service total value

`original_promo_amount`

(optional) Subscribed service Promotion Amount

`order_header_id`

(optional) Sales Order Header associated to the subscribed service

`order_number`

(optional) Sales Order Number associated to the subscribed service

`order_type`

(optional) Order Type of Subscribed Service

`order_line_id`

(optional) Sales Order Line Id associated to the subscribed service

`order_line_number`

(optional) Sales Order Line Number associated to the subscribed service

`commitment_schedule_id`

(optional) Subscribed service commitment schedule Id

`sales_account_party_id`

(optional) Subscribed service sales account party id

`data_center`

(optional) Subscribed service data center

`data_center_region`

(optional) Subscribed service data center region

`admin_email`

(optional) Subscribed service admin email id

`buyer_email`

(optional) Subscribed service buyer email id

`subscription_source`

(optional) Subscribed service source

`provisioning_source`

(optional) Subscribed service provisioning source

`fulfillment_set`

(optional) Subscribed service fulfillment set

`is_intent_to_pay`

(optional) Subscribed service intent to pay flag

`is_payg`

(optional) Subscribed service payg flag

`pricing_model`

(optional) Subscribed service pricing model

`program_type`

(optional) Subscribed service program type

`start_date_type`

(optional) Subscribed service start date type

`time_provisioned`

(optional) Subscribed service provisioning date

`promo_type`

(optional) Subscribed service promotion type

`service_to_customer`

(optional)

`service_to_contact`

(optional)

`service_to_address`

(optional)

`sold_to_customer`

(optional)

`sold_to_contact`

(optional)

`end_user_customer`

(optional)

`end_user_contact`

(optional)

`end_user_address`

(optional)

`reseller_customer`

(optional)

`reseller_contact`

(optional)

`reseller_address`

(optional)

`csi`

(optional) Subscribed service CSI number

`customer_transaction_reference`

(optional) Identifier for a customer's transactions for purchase of ay oracle services

`partner_credit_amount`

(optional) Subscribed service partner credit amount

`is_single_rate_card`

(optional) Indicates if the Subscribed service has a single ratecard

`agreement_id`

(optional) Subscribed service agreement ID

`agreement_name`

(optional) Subscribed service agrrement name

`agreement_type`

(optional) Subscribed service agrrement type

`billing_frequency`

(optional) Subscribed service invoice frequency

`time_welcome_email_sent`

(optional) Subscribed service welcome email sent date

`time_service_configuration_email_sent`

(optional) Subscribed service service configuration email sent date

`time_customer_config`

(optional) Subscribed service customer config date

`time_agreement_end`

(optional) Subscribed service agrrement end date

`commitment_services`

(optional) List of Commitment services of a line

`rate_cards`

(optional) List of Rate Cards of a Subscribed Service

`time_created`

(optional) Subscribed service creation date

`created_by`

(optional) User that created the subscribed service

`time_updated`

(optional) Subscribed service last update date

`updated_by`

(optional) User that updated the subscribed service

`ratecard_type`

(optional) SPM Ratecard Type

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_SUMMARY_T Type

Subscribed service contract details

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Subscribed Service ID

`l_type`

(optional) Subscribed Service line type

`serial_number`

(optional) Subscribed service line number

`subscription_id`

(optional) Subscription ID associated to the subscribed service

`product`

(optional)

`time_start`

(optional) Subscribed service start date

`time_end`

(optional) Subscribed service end date

`quantity`

(optional) Subscribed service quantity

`status`

(optional) Subscribed service status

`operation_type`

(optional) Subscribed service operation type

`net_unit_price`

(optional) Subscribed service net unit price

`price_period`

(optional) Indicates the period for which the commitment amount can be utilised exceeding which the amount lapses. Also used in calculation of total contract line value

`line_net_amount`

(optional) Subscribed service line net amount

`is_variable_commitment`

(optional) Indicates if the commitment lines can have different quantities

`is_allowance`

(optional) Indicates if a service can recieve usages and consequently have available amounts computed

`used_amount`

(optional) Subscribed service used amount

`available_amount`

(optional) Subscribed sercice available or remaining amount

`funded_allocation_value`

(optional) Funded Allocation line value example: 12000.00

`is_having_usage`

(optional) Indicator on whether or not there has been usage for the subscribed service

`is_cap_to_price_list`

(optional) If true compares rate between ratecard and the active pricelist and minimum rate would be fetched

`credit_percentage`

(optional) Subscribed service credit percentage

`partner_transaction_type`

(optional) This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ

`is_credit_enabled`

(optional) Used in context of service credit lines

`overage_policy`

(optional) Overage Policy of Subscribed Service

`overage_bill_to`

(optional) Overage Bill To of Subscribed Service

`payg_policy`

(optional) Pay As You Go policy of Subscribed Service (Can be null - indicating no payg policy)

`promo_order_line_id`

(optional) Not null if this service has an associated promotion line in SPM. Contains the line identifier from Order Management of the associated promo line.

`promotion_pricing_type`

(optional) Promotion Pricing Type of Subscribed Service (Can be null - indicating no promotion pricing)

`rate_card_discount_percentage`

(optional) Subscribed service Rate Card Discount Percentage

`overage_discount_percentage`

(optional) Subscribed service Overage Discount Percentage

`bill_to_customer`

(optional)

`bill_to_contact`

(optional)

`bill_to_address`

(optional)

`payment_number`

(optional) Payment Number of Subscribed Service

`time_payment_expiry`

(optional) Subscribed service payment expiry date

`payment_term`

(optional)

`payment_method`

(optional) Payment Method of Subscribed Service

`transaction_extension_id`

(optional) Subscribed service Transaction Extension Id

`sales_channel`

(optional) Sales Channel of Subscribed Service

`eligible_to_renew`

(optional) Subscribed service eligible to renew field

`renewed_subscribed_service_id`

(optional) SPM renewed Subscription ID

`term_value`

(optional) Term value in Months

`term_value_uom`

(optional) Term value UOM

`renewal_opty_id`

(optional) Subscribed service Opportunity Id

`renewal_opty_number`

(optional) Renewal Opportunity Number of Subscribed Service

`renewal_opty_type`

(optional) Renewal Opportunity Type of Subscribed Service

`booking_opty_number`

(optional) Booking Opportunity Number of Subscribed Service

`revenue_line_id`

(optional) Subscribed service Revenue Line Id

`revenue_line_number`

(optional) Revenue Line NUmber of Subscribed Service

`major_set`

(optional) Subscribed service Major Set

`time_majorset_start`

(optional) Subscribed service Major Set Start date

`time_majorset_end`

(optional) Subscribed service Major Set End date

`system_arr_in_lc`

(optional) Subscribed service System ARR

`system_arr_in_sc`

(optional) Subscribed service System ARR in Standard Currency

`system_atr_arr_in_lc`

(optional) Subscribed service System ATR-ARR

`system_atr_arr_in_sc`

(optional) Subscribed service System ATR-ARR in Standard Currency

`revised_arr_in_lc`

(optional) Subscribed service Revised ARR

`revised_arr_in_sc`

(optional) Subscribed service Revised ARR in Standard Currency

`total_value`

(optional) Subscribed service total value

`original_promo_amount`

(optional) Subscribed service Promotion Amount

`order_header_id`

(optional) Sales Order Header associated to the subscribed service

`order_number`

(optional) Sales Order Number associated to the subscribed service

`order_type`

(optional) Order Type of Subscribed Service

`order_line_id`

(optional) Sales Order Line Id associated to the subscribed service

`order_line_number`

(optional) Sales Order Line Number associated to the subscribed service

`commitment_schedule_id`

(optional) Subscribed service commitment schedule Id

`sales_account_party_id`

(optional) Subscribed service sales account party id

`data_center`

(optional) Subscribed service data center

`data_center_region`

(optional) Subscribed service data center region

`admin_email`

(optional) Subscribed service admin email id

`buyer_email`

(optional) Subscribed service buyer email id

`subscription_source`

(optional) Subscribed service source

`provisioning_source`

(optional) Subscribed service provisioning source

`fulfillment_set`

(optional) Subscribed service fulfillment set

`is_intent_to_pay`

(optional) Subscribed service intent to pay flag

`is_payg`

(optional) Subscribed service payg flag

`pricing_model`

(optional) Subscribed service pricing model

`program_type`

(optional) Subscribed service program type

`start_date_type`

(optional) Subscribed service start date type

`time_provisioned`

(optional) Subscribed service provisioning date

`promo_type`

(optional) Subscribed service promotion type

`service_to_customer`

(optional)

`service_to_contact`

(optional)

`service_to_address`

(optional)

`sold_to_customer`

(optional)

`sold_to_contact`

(optional)

`end_user_customer`

(optional)

`end_user_contact`

(optional)

`end_user_address`

(optional)

`reseller_customer`

(optional)

`reseller_contact`

(optional)

`reseller_address`

(optional)

`csi`

(optional) Subscribed service CSI number

`customer_transaction_reference`

(optional) Identifier for a customer's transactions for purchase of ay oracle services

`partner_credit_amount`

(optional) Subscribed service partner credit amount

`is_single_rate_card`

(optional) Indicates if the Subscribed service has a single ratecard

`agreement_id`

(optional) Subscribed service agreement ID

`agreement_name`

(optional) Subscribed service agrrement name

`agreement_type`

(optional) Subscribed service agrrement type

`billing_frequency`

(optional) Subscribed service invoice frequency

`time_welcome_email_sent`

(optional) Subscribed service welcome email sent date

`time_service_configuration_email_sent`

(optional) Subscribed service service configuration email sent date

`time_customer_config`

(optional) Subscribed service customer config date

`time_agreement_end`

(optional) Subscribed service agrrement end date

`time_created`

(optional) Subscribed service creation date

`created_by`

(optional) User that created the subscribed service

`time_updated`

(optional) Subscribed service last update date

`updated_by`

(optional) User that updated the subscribed service

`ratecard_type`

(optional) SPM Ratecard Type

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_PRODUCT_T Type

Product description

Syntax
```

```

Fields

Field Description

`part_number`

(required) Product part numner

`name`

(required) Product name

`unit_of_measure`

(required) Unit of measure

`provisioning_group`

(optional) Product provisioning group

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_SUBSCRIBED_SERVICE_T Type

Subscribed Service summary

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Subscribed Service ID

`product`

(optional)

`quantity`

(optional) Subscribed service quantity

`status`

(optional) Subscribed service status

`operation_type`

(optional) Subscribed service operation type

`net_unit_price`

(optional) Subscribed service net unit price

`used_amount`

(optional) Subscribed service used amount

`available_amount`

(optional) Subscribed sercice available or remaining amount

`funded_allocation_value`

(optional) Funded Allocation line value example: 12000.00

`partner_transaction_type`

(optional) This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ

`term_value`

(optional) Term value in Months

`term_value_uom`

(optional) Term value UOM

`booking_opty_number`

(optional) Booking Opportunity Number of Subscribed Service

`total_value`

(optional) Subscribed service total value

`original_promo_amount`

(optional) Subscribed service Promotion Amount

`order_number`

(optional) Sales Order Number associated to the subscribed service

`data_center_region`

(optional) Subscribed service data center region

`pricing_model`

(optional) Subscribed service pricing model

`program_type`

(optional) Subscribed service program type

`promo_type`

(optional) Subscribed service promotion type

`csi`

(optional) Subscribed service CSI number

`is_intent_to_pay`

(optional) Subscribed service intent to pay flag

`time_start`

(optional) Subscribed service start date

`time_end`

(optional) Subscribed service end date

`commitment_services`

(optional) List of Commitment services of a line

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_SUBSCRIBED_SERVICE_TBL Type

Nested table type of dbms_cloud_oci_onesubscription_subscription_subscribed_service_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_SUMMARY_T Type

Subscription summary

Syntax
```

```

Fields

Field Description

`status`

(optional) Status of the plan

`time_start`

(optional) Represents the date when the first service of the subscription was activated

`time_end`

(optional) Represents the date when the last service of the subscription ends

`currency`

(optional)

`service_name`

(optional) Customer friendly service name provided by PRG

`hold_reason`

(optional) Hold reason of the plan

`time_hold_release_eta`

(optional) Represents the date of the hold release

`subscribed_services`

(optional) List of Subscribed Services of the plan

- [One Subscription Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-1CBC56E5-E194-4433-A468-AEDE084192A6)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-EA053FE0-EBE7-4E5D-9CF7-3313018BC473)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-E7A5CCDA-5BE0-4C4B-B1EA-75D6A56E979A)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-4F9AF8E9-7C82-457F-A9D9-500F061F886E)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_AGGREGATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-01C62A00-B3FA-49CC-A365-FB63558D3736)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_AGGREGATED_COMPUTED_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-6C34A649-A62F-4DAF-BAEB-C1580D7AF253)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_BILLING_SCHEDULE_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-5FA8669E-E78D-4501-A01A-8160A1512A8A)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_BILLING_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-F0D8D35B-CECA-4653-952C-9E746C4CAF24)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-87E90D38-6986-48EF-BCD3-531EB1965523)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-86180281-EB42-4AAA-BC1D-15BF95442981)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-7B30CC06-CCA4-4236-AF50-E6F45BE6992D)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-D5E37907-4E9F-41AA-9BC3-818F88C6C5D6)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMPUTED_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-A0043B87-1F01-462D-BE49-40C83B912422)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-918B33A1-FA02-4376-84D1-E0F1ECB5DA1E)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-E46DCFE9-0171-4189-9DB0-23FF54EB034E)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICE_LINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-00023732-76D1-46CB-9EFC-07C6AF7A2209)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_BUSINESS_PARTNER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-D3B00E0C-ED16-40BD-87F8-F7F000D3E7C4)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-5400C675-D258-4BAA-A274-81D68B0905D3)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-DB8248CD-8C5E-4C97-9441-71B9A6253131)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-5B1EC692-B870-46FD-9DF4-CA2FEECED43B)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_PAYMENT_TERM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-AA5EFEEA-D686-472E-80BD-FAD22659D6A6)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_CURRENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-D5E64E34-3C88-4E91-B374-7E98FC8449CB)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICING_ORGANIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-873597DA-30B9-4E81-AD44-49B241F23B91)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICE_LINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-523ECAEF-A2FB-4963-8217-422982834D60)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-FC295E7B-942F-49E8-82F8-C35686ADB9D6)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_INVOICELINE_COMPUTED_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-1C3BCE9E-F2EC-4294-B525-945933220204)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_ORGNIZATION_SUBS_CURRENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-6C3E07D5-D10C-4817-9735-DFDA34D2ADB0)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_ORGANIZATION_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-75DD47AD-B7F5-4F73-AC50-5F1670B2C745)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-126094A5-2BA7-4C16-9B46-AAD6024247DC)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_CURRENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-14ECD507-1428-4CE7-B99A-8784A033DB7E)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_TIER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-06598BEC-78C3-4D8B-B018-DB48D0BABCDE)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_TIER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-13C81FB4-605F-4D43-B2DF-4887C62D41E9)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-7B3B7F59-3015-432D-940A-D5148D016A6D)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_BUSINESS_PARTNER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-94B05C2D-2120-4593-8A44-A388C69CBD2C)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-C7D35D2E-8BE1-43C3-9BB0-B14301197CD4)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-ACC33FDA-9780-4425-8738-AAAECBB9BB88)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-02505F40-D91C-43C2-9C72-49C7C2A92873)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_PAYMENT_TERM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-E363DC4A-7CCA-4FBB-997B-3391A596E8DE)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_COMMITMENT_SERVICE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-109AA842-667E-4F68-8C3D-B13ACF04222E)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_RATE_CARD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-D9BC9412-1272-4B36-BFA3-9EA7D9BFAE12)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-F2463D2A-7074-4CA0-ACD3-A18F62EBEB4B)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIBED_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-0004671E-B1BA-4008-9258-874F3723F02D)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-14661D42-3068-42CA-B7B8-97BD5C593A11)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_SUBSCRIBED_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-78C46545-DD31-4E71-9CE0-92B80A66EA2A)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_SUBSCRIBED_SERVICE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-CFB1972A-70A5-40EB-AB05-4DA5CA7FB990)
- [DBMS_CLOUD_OCI_ONESUBSCRIPTION_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/onesubscription_t.html#ADSDK-GUID-2ACE2FC7-3556-4E5B-BFE2-ACB1BA429F9E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
