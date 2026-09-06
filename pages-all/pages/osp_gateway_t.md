# OSP Gateway Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#dcoc-content-body)

## OSP Gateway Common Types

### DBMS_CLOUD_OCI_OSP_GATEWAY_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OSP_GATEWAY_ADDRESS_T Type

Address details model.

Syntax
```

```

Fields

Field Description

`address_key`

(optional) Address identifier.

`line1`

(optional) Address line 1.

`line2`

(optional) Address line 2.

`line3`

(optional) Address line 3.

`line4`

(optional) Address line 4.

`street_name`

(optional) Street name of the address.

`street_number`

(optional) Street number of the address.

`city`

(optional) Name of the city.

`county`

(optional) County of the address.

`country`

(optional) Country of the address.

`province`

(optional) Province of the address.

`postal_code`

(optional) Post code of the address.

`state`

(optional) State of the address.

`email_address`

(optional) Contact person email address.

`company_name`

(optional) Name of the customer company.

`first_name`

(optional) First name of the contact person.

`middle_name`

(optional) Middle name of the contact person.

`last_name`

(optional) Last name of the contact person.

`phone_country_code`

(optional) Phone country code of the contact person.

`phone_number`

(optional) Phone number of the contact person.

`job_title`

(optional) Job title of the contact person.

`department_name`

(optional) Department name of the customer company.

`internal_number`

(optional) Internal number of the customer company.

`contributor_class`

(optional) Contributor class of the customer company.

`state_inscription`

(optional) State Inscription.

`municipal_inscription`

(optional) Municipal Inscription.

### DBMS_CLOUD_OCI_OSP_GATEWAY_FORMAT_T Type

Format information

Syntax
```

```

Fields

Field Description

`value`

(required) Regex format specification

`example`

(optional) Example of the desired format that matches the regex

### DBMS_CLOUD_OCI_OSP_GATEWAY_LABEL_T Type

Label information

Syntax
```

```

Fields

Field Description

`value`

(required) Language token of the required label

`example`

(optional) English translation of the label (for reference only - translation is not provided)

### DBMS_CLOUD_OCI_OSP_GATEWAY_FIELD_T Type

Field information

Syntax
```

```

Fields

Field Description

`name`

(required) The field name

`is_required`

(required) The given field is requeired or not

`format`

(optional)

`label`

(optional)

`language`

(optional) Locale code (rfc4646 format) of a forced language (e.g.: jp addresses require jp always)

### DBMS_CLOUD_OCI_OSP_GATEWAY_FIELD_TBL Type

Nested table type of dbms_cloud_oci_osp_gateway_field_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSP_GATEWAY_ADDRESS_TYPE_RULE_T Type

Address type rule information

Syntax
```

```

Fields

Field Description

`third_party_validation`

(optional) Third party validation.

Allowed values are: 'OPTIONAL', 'REQUIRED', 'NEVER'

`fields`

(required) Address type rule fields

### DBMS_CLOUD_OCI_OSP_GATEWAY_CONTACT_TYPE_RULE_T Type

Contact type rule information

Syntax
```

```

Fields

Field Description

`fields`

(required) Contact type rule fields

### DBMS_CLOUD_OCI_OSP_GATEWAY_TAX_TYPE_RULE_T Type

Tax type rule information

Syntax
```

```

Fields

Field Description

`fields`

(required) Tax type rule fields

### DBMS_CLOUD_OCI_OSP_GATEWAY_ADDRESS_RULE_T Type

Addres rule information

Syntax
```

```

Fields

Field Description

`country_code`

(required) Country code for the address rule in ISO-3166-1 2-letter format

`address`

(required)

`contact`

(optional)

`tax`

(optional)

### DBMS_CLOUD_OCI_OSP_GATEWAY_TAX_INFO_T Type

Tax details.

Syntax
```

```

Fields

Field Description

`tax_payer_id`

(optional) Tay payer identifier.

`tax_reg_number`

(optional) Tax registration number.

`no_tax_reason_code`

(optional) Tax exemption reason code.

`no_tax_reason_code_details`

(optional) Tax exemption reason description.

`tax_cnpj`

(optional) Brazilian companies' CNPJ number.

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_OPTION_T Type

Payment option of a subscription.

Syntax
```

```

Fields

Field Description

`wallet_instrument_id`

(optional) Wallet instrument internal id.

`wallet_transaction_id`

(optional) Wallet transaction id.

`payment_method`

(required) Payment method

Allowed values are: 'CREDIT_CARD', 'PAYPAL'

### DBMS_CLOUD_OCI_OSP_GATEWAY_MERCHANT_DEFINED_DATA_T Type

Merchant details.

Syntax
```

```

Fields

Field Description

`promo_type`

(optional) Promotion type code.

`cloud_account_name`

(optional) Cloud account name.

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_GATEWAY_T Type

Payment gateway details.

Syntax
```

```

Fields

Field Description

`merchant_defined_data`

(optional)

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_OPTION_TBL Type

Nested table type of dbms_cloud_oci_osp_gateway_payment_option_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_T Type

Subscription details object which extends the SubscriptionSummary

Syntax
```

```

Fields

Field Description

`id`

(optional) Subscription id identifier (OCID).

`subscription_plan_number`

(required) Subscription plan number.

`plan_type`

(optional) Subscription plan type.

Allowed values are: 'FREE_TIER', 'PAYG'

`time_start`

(optional) Start date of the subscription.

`ship_to_cust_acct_site_id`

(optional) Ship to customer account site address id.

`ship_to_cust_acct_role_id`

(optional) Ship to customer account role.

`bill_to_cust_account_id`

(optional) Bill to customer Account id.

`is_intent_to_pay`

(optional) Payment intension.

`currency_code`

(optional) Currency code

`gsi_org_code`

(optional) GSI Subscription external code.

`language_code`

(optional) Language short code (en, de, hu, etc)

`organization_id`

(optional) GSI organization external identifier.

`upgrade_state`

(optional) Status of the upgrade.

Allowed values are: 'PROMO', 'SUBMITTED', 'ERROR', 'UPGRADED'

`upgrade_state_details`

(optional) This field is used to describe the Upgrade State in case of error (E.g. Upgrade failure caused by interfacing Tax details- TaxError)

Allowed values are: 'TAX_ERROR', 'UPGRADE_ERROR'

`account_type`

(optional) Account type.

Allowed values are: 'PERSONAL', 'CORPORATE', 'CORPORATE_SUBMITTED'

`tax_info`

(optional)

`payment_options`

(optional) Payment option list of a subscription.

`payment_gateway`

(optional)

`billing_address`

(optional)

`time_plan_upgrade`

(optional) Date of upgrade/conversion when planType changed from FREE_TIER to PAYG

`time_personal_to_corporate_conv`

(optional) Date of upgrade/conversion when account type changed from PERSONAL to CORPORATE

### DBMS_CLOUD_OCI_OSP_GATEWAY_AUTHORIZE_SUBSCRIPTION_PAYMENT_DETAILS_T Type

Request object for a subscription payment authorization

Syntax
```

```

Fields

Field Description

`subscription`

(required)

`language_code`

(required) Language code

`email`

(required) User email

### DBMS_CLOUD_OCI_OSP_GATEWAY_AUTHORIZE_SUBSCRIPTION_PAYMENT_RECEIPT_T Type

Subscription payment authorization response

Syntax
```

```

Fields

Field Description

`header_id`

(required) Payment header id

`api_token`

(optional) Parameters in a token for Payment Service

`user_token`

(optional) Session token created for Payment Service

### DBMS_CLOUD_OCI_OSP_GATEWAY_COUNTRY_T Type

Country details model

Syntax
```

```

Fields

Field Description

`country_id`

(optional) Indentifier of the country. This is a DB side unique id which was generated when the entity was created in the table

`country_code`

(optional) Country code in ISO-3166-1 2-letter format

`country_name`

(optional) Name of the country

`language_id`

(optional) Language identifier

`ascii3_country_code`

(optional) Country code in ISO-3166-1 3-letter format

### DBMS_CLOUD_OCI_OSP_GATEWAY_BILL_TO_ADDRESS_T Type

Address details model

Syntax
```

```

Fields

Field Description

`contact_name`

(optional) Name of the contact person

`company_name`

(optional) Name of the customer company

`address_line1`

(optional) Address line 1

`address_line2`

(optional) Address line 2

`address_line3`

(optional) Address line 3

`address_line4`

(optional) Address line 4

`street_name`

(optional) Street name

`street_number`

(optional) House no

`city`

(optional) Name of the city

`country`

(optional)

`county`

(optional) County name

`state`

(optional) Name of the state

`postal_code`

(optional) ZIP no

`province`

(optional) Name of the province

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_DETAIL_T Type

Payment related details

Syntax
```

```

Fields

Field Description

`time_paid_on`

(optional) Paid the invoice on this day

`paid_by`

(optional) example

`payment_method`

(required) Payment method

Allowed values are: 'CREDIT_CARD', 'PAYPAL', 'ECHECK', 'OTHER'

`amount_paid`

(optional) Amount that paid

### DBMS_CLOUD_OCI_OSP_GATEWAY_CREDIT_CARD_PAYMENT_DETAIL_T Type

Credit card Payment related details

Syntax
```

```

`dbms_cloud_oci_osp_gateway_credit_card_payment_detail_t`is a subtype of the`dbms_cloud_oci_osp_gateway_payment_detail_t`type.

Fields

Field Description

`name_on_card`

(optional) Name on the credit card

`credit_card_type`

(optional) Credit card type

Allowed values are: 'VISA', 'AMEX', 'MASTERCARD', 'DISCOVER', 'JCB', 'DINER', 'ELO'

`last_digits`

(optional) Last four digits of the card

`time_expiration`

(optional) Expired date of the credit card

### DBMS_CLOUD_OCI_OSP_GATEWAY_CREDIT_CARD_PAYMENT_OPTION_T Type

Credit card Payment related details

Syntax
```

```

`dbms_cloud_oci_osp_gateway_credit_card_payment_option_t`is a subtype of the`dbms_cloud_oci_osp_gateway_payment_option_t`type.

Fields

Field Description

`credit_card_type`

(optional) Credit card type.

Allowed values are: 'VISA', 'AMEX', 'MASTERCARD', 'DISCOVER', 'JCB', 'DINER', 'ELO'

`last_digits`

(optional) Last four digits of the card.

`name_on_card`

(optional) Name on the credit card.

`time_expiration`

(optional) Expired date of the credit card.

### DBMS_CLOUD_OCI_OSP_GATEWAY_CURRENCY_T Type

Currency details model

Syntax
```

```

Fields

Field Description

`currency_code`

(optional) Currency code

`currency_symbol`

(optional) Currency symbol

`name`

(optional) Name of the currency

`usd_conversion`

(optional) USD conversion rate of the currency

`round_decimal_point`

(optional) Round decimal point

### DBMS_CLOUD_OCI_OSP_GATEWAY_ECHECK_PAYMENT_DETAIL_T Type

Echeck Payment related details

Syntax
```

```

`dbms_cloud_oci_osp_gateway_echeck_payment_detail_t`is a subtype of the`dbms_cloud_oci_osp_gateway_payment_detail_t`type.

Fields

Field Description

`name_on_card`

(optional) Name on the echeck card

`card_type`

(optional) Echeck card type

Allowed values are: 'SAVING', 'CHECKING', 'CORPORATE_CHECKING'

`account_number`

(optional) Account number of the card owner

`routing_number`

(optional) Routing number of the echeck card

### DBMS_CLOUD_OCI_OSP_GATEWAY_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_T Type

Invoice details

Syntax
```

```

Fields

Field Description

`invoice_id`

(required) Invoice identifier which is generated on the on-premise sie. Pls note this is not an OCID

`invoice_number`

(optional) Invoice external reference

`internal_invoice_id`

(optional) Transaction identifier

`is_credit_card_payable`

(optional) Is credit card payment eligible

`time_invoice`

(optional) Date of invoice

`tax`

(optional) Tax of invoice amount

`invoice_amount`

(optional) Total amount of invoice

`invoice_amount_due`

(optional) Balance of invoice

`invoice_amount_credited`

(optional) Invoice amount credit

`invoice_amount_adjusted`

(optional) Invoice amount adjust

`invoice_amount_applied`

(optional) Invoice amount applied

`currency`

(optional)

`invoice_type`

(optional) Type of invoice

Allowed values are: 'HARDWARE', 'SUBSCRIPTION', 'SUPPORT', 'LICENSE', 'EDUCATION', 'CONSULTING', 'SERVICE', 'USAGE'

`time_invoice_due`

(optional) Due date of invoice

`invoice_ref_number`

(optional) Invoice reference number

`invoice_po_number`

(optional) Invoice PO number

`invoice_status`

(optional) Invoice status

Allowed values are: 'OPEN', 'PAST_DUE', 'PAYMENT_SUBMITTED', 'CLOSED'

`preferred_email`

(optional) Preferred Email on the invoice

`is_pdf_email_available`

(optional) Is emailing pdf allowed

`is_display_download_pdf`

(optional) Is pdf download access allowed

`is_payable`

(optional) Whether invoice can be payed

`payment_terms`

(optional) Payment terms

`last_payment_detail`

(optional)

`bill_to_address`

(optional)

`subscription_ids`

(optional) List of subscription identifiers

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_SUMMARY_T Type

Invoice list elements

Syntax
```

```

Fields

Field Description

`invoice_id`

(required) Invoice identifier

`invoice_number`

(optional) Invoice external reference

`internal_invoice_id`

(optional) PC invoice identifier

`is_credit_card_payable`

(optional) Is credit card payment eligible

`invoice_status`

(optional) Invoice status

Allowed values are: 'OPEN', 'PAST_DUE', 'PAYMENT_SUBMITTED', 'CLOSED'

`invoice_type`

(optional) Type of invoice

Allowed values are: 'HARDWARE', 'SUBSCRIPTION', 'SUPPORT', 'LICENSE', 'EDUCATION', 'CONSULTING', 'SERVICE', 'USAGE'

`is_paid`

(optional) Is the invoice has been already payed

`is_payable`

(optional) Whether invoice can be payed

`invoice_amount`

(optional) Invoice amount

`invoice_amount_due`

(optional) Invoice amount due

`invoice_amount_credited`

(optional) Invoice amount credit

`invoice_amount_adjusted`

(optional) Invoice amount adjust

`invoice_amount_applied`

(optional) Invoice amount applied

`time_invoice_due`

(optional) Due date of invoice amount

`is_payment_failed`

(optional) Is the last payment failed

`invoice_amount_in_dispute`

(optional) Invoice amount in dispute

`invoice_ref_number`

(optional) Invoice reference number

`invoice_po_number`

(optional) Invoice PO number

`time_invoice`

(optional) Date of invoice

`currency`

(optional)

`is_pdf_email_available`

(optional) Is emailing pdf allowed

`is_display_view_pdf`

(optional) Is view access allowed

`is_display_download_pdf`

(optional) Is pdf download access allowed

`last_payment_detail`

(optional)

`party_name`

(optional) Name of the bill to customer

`subscription_ids`

(optional) List of subscription identifiers

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_osp_gateway_invoice_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_COLLECTION_T Type

Invoice list

Syntax
```

```

Fields

Field Description

`items`

(required) Invoice list elements

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_LINE_SUMMARY_T Type

Product items of the invoice

Syntax
```

```

Fields

Field Description

`product`

(required) Product of the item

`order_no`

(optional) Product of the item

`part_number`

(optional) Part number

`time_start`

(optional) Start date

`time_end`

(optional) End date

`quantity`

(optional) Quantity of the ordered product

`net_unit_price`

(optional) Unit price of the ordered product

`total_price`

(optional) Total price of the ordered product (Net unit price x quantity)

`currency`

(optional)

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_LINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_osp_gateway_invoice_line_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_LINE_COLLECTION_T Type

Invoice line list

Syntax
```

```

Fields

Field Description

`items`

(required) Invoice line list elements

### DBMS_CLOUD_OCI_OSP_GATEWAY_OTHER_PAYMENT_DETAIL_T Type

Other Payment related details

Syntax
```

```

`dbms_cloud_oci_osp_gateway_other_payment_detail_t`is a subtype of the`dbms_cloud_oci_osp_gateway_payment_detail_t`type.

Fields

Field Description

`echeck_routing`

(optional) Last four routing digits of the card

`name_on_card`

(optional) Name on the echeck card

`credit_card_type`

(optional) Echeck card type

Allowed values are: 'VISA', 'AMEX', 'MASTERCARD', 'DISCOVER', 'JCB', 'DINER', 'ELO', 'SAVING', 'CHECKING', 'CORPORATE_CHECKING'

`last_digits`

(optional) Last four digits of the card

`time_expiration`

(optional) Expired date of the echeck card

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_INVOICE_DETAILS_T Type

Request object for invoice payment

Syntax
```

```

Fields

Field Description

`language_code`

(optional) Language code

`return_url`

(optional) Callback URL

`email`

(required) User email

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_INVOICE_RECEIPT_T Type

Invoice payment action response

Syntax
```

```

Fields

Field Description

`url`

(optional) Url of the Payment Service

`header_id`

(required) Payment header id

`token`

(optional) Token created for Payment Service

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_SUBSCRIPTION_DETAILS_T Type

Request object for paying a subscription

Syntax
```

```

Fields

Field Description

`subscription`

(required)

`language_code`

(required) Language code

`email`

(required) User email

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_SUBSCRIPTION_RECEIPT_T Type

Subscription payment action response

Syntax
```

```

Fields

Field Description

`header_id`

(required) Payment header id

`api_token`

(optional) Parameters in a token for Payment Service

`user_token`

(optional) Session token created for Payment Service

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAYPAL_PAYMENT_DETAIL_T Type

PayPal Payment related details

Syntax
```

```

`dbms_cloud_oci_osp_gateway_paypal_payment_detail_t`is a subtype of the`dbms_cloud_oci_osp_gateway_payment_detail_t`type.

Fields

Field Description

`paypal_id`

(optional) The id (email address) of the paypal payment

`paypal_reference`

(optional) paypal payment reference

### DBMS_CLOUD_OCI_OSP_GATEWAY_PAYPAL_PAYMENT_OPTION_T Type

PayPal Payment related details

Syntax
```

```

`dbms_cloud_oci_osp_gateway_paypal_payment_option_t`is a subtype of the`dbms_cloud_oci_osp_gateway_payment_option_t`type.

Fields

Field Description

`email_address`

(optional) The email address of the paypal user.

`first_name`

(optional) First name of the paypal user.

`last_name`

(optional) Last name of the paypal user.

`ext_billing_agreement_id`

(optional) Agreement id for the paypal account.

### DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_SUMMARY_T Type

Subscription object which contains the common subscription data.

Syntax
```

```

Fields

Field Description

`id`

(optional) Subscription id identifier (OCID).

`subscription_plan_number`

(required) Subscription plan number.

`plan_type`

(optional) Subscription plan type.

Allowed values are: 'FREE_TIER', 'PAYG'

`time_start`

(optional) Start date of the subscription.

`ship_to_cust_acct_site_id`

(optional) Ship to customer account site address id.

`ship_to_cust_acct_role_id`

(optional) Ship to customer account role.

`bill_to_cust_account_id`

(optional) Bill to customer Account id.

`is_intent_to_pay`

(optional) Payment intension.

`currency_code`

(optional) Currency code

`gsi_org_code`

(optional) GSI Subscription external code.

`language_code`

(optional) Language short code (en, de, hu, etc)

`organization_id`

(optional) GSI organization external identifier.

`upgrade_state`

(optional) Status of the upgrade.

Allowed values are: 'PROMO', 'SUBMITTED', 'ERROR', 'UPGRADED'

`upgrade_state_details`

(optional) This field is used to describe the Upgrade State in case of error (E.g. Upgrade failure caused by interfacing Tax details- TaxError)

Allowed values are: 'TAX_ERROR', 'UPGRADE_ERROR'

`account_type`

(optional) Account type.

Allowed values are: 'PERSONAL', 'CORPORATE', 'CORPORATE_SUBMITTED'

`tax_info`

(optional)

`payment_options`

(optional) Payment option list of a subscription.

`payment_gateway`

(optional)

`billing_address`

(optional)

`time_plan_upgrade`

(optional) Date of upgrade/conversion when planType changed from FREE_TIER to PAYG

`time_personal_to_corporate_conv`

(optional) Date of upgrade/conversion when account type changed from PERSONAL to CORPORATE

### DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_osp_gateway_subscription_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_COLLECTION_T Type

Subscription list

Syntax
```

```

Fields

Field Description

`items`

(required) Subscription list elements

### DBMS_CLOUD_OCI_OSP_GATEWAY_UPDATE_SUBSCRIPTION_DETAILS_T Type

Request object for updating a subscription

Syntax
```

```

Fields

Field Description

`subscription`

(required)

`email`

(required) User email

### DBMS_CLOUD_OCI_OSP_GATEWAY_VERIFY_ADDRESS_DETAILS_T Type

Verify address related details

Syntax
```

```

Fields

Field Description

`address_key`

(optional) Address identifier.

`line1`

(optional) Address line 1.

`line2`

(optional) Address line 2.

`line3`

(optional) Address line 3.

`line4`

(optional) Address line 4.

`street_name`

(optional) Street name of the address.

`street_number`

(optional) Street number of the address.

`city`

(optional) Name of the city.

`county`

(optional) County of the address.

`country`

(optional) Country of the address.

`province`

(optional) Province of the address.

`postal_code`

(optional) Post code of the address.

`state`

(optional) State of the address.

`email_address`

(optional) Contact person email address.

`company_name`

(optional) Name of the customer company.

`first_name`

(optional) First name of the contact person.

`middle_name`

(optional) Middle name of the contact person.

`last_name`

(optional) Last name of the contact person.

`phone_country_code`

(optional) Phone country code of the contact person.

`phone_number`

(optional) Phone number of the contact person.

`job_title`

(optional) Job title of the contact person.

`department_name`

(optional) Department name of the customer company.

`internal_number`

(optional) Internal number of the customer company.

`contributor_class`

(optional) Contributor class of the customer company.

`state_inscription`

(optional) State Inscription.

`municipal_inscription`

(optional) Municipal Inscription.

### DBMS_CLOUD_OCI_OSP_GATEWAY_VERIFY_ADDRESS_RECEIPT_T Type

Address verficiation result

Syntax
```

```

Fields

Field Description

`address`

(required)

`quality`

(required) Address quality type.

Allowed values are: 'EXCELLENT', 'GOOD', 'AVERAGE', 'POOR', 'BAD'

`verification_code`

(required) Address verification code.

Allowed values are: 'VERIFIED', 'PARTIALLY_VERIFIED', 'AMBIGUOUS', 'REVERTED', 'UNVERIFIED'

- [OSP Gateway Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-DCDD4AD8-828B-448C-A546-57B675DE1508)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-F5ED3FB7-BEB5-4D66-9706-A600BB0FE888)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-E9135664-FF35-4800-A2D3-880A569A7117)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_FORMAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-20C84D8A-19AC-4CF3-8D96-966EF11CAF9D)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-3226B4CF-BFDA-4B4B-947F-FEDCA35552A8)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-5C40AD71-F615-4EA6-8698-C5BAB572BBB3)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_FIELD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-BCADCCA1-0D59-4A99-9113-EB4D252BC983)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_ADDRESS_TYPE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-ED3A8E98-9B31-460A-BC84-BF9D20611169)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_CONTACT_TYPE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-7226B911-84C6-4B5E-A684-7488C853F9D2)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_TAX_TYPE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-6B119858-2E93-444E-BD5F-A2256DBFFCF2)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_ADDRESS_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-E59D0502-074A-483B-8437-31DC9D6D0262)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_TAX_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-BD655938-C49C-4C00-B97F-72D584AA77BE)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-8DB9C3D1-5FD9-4B80-BF53-44654139516D)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_MERCHANT_DEFINED_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-FCDF1875-A01C-4B8E-B92B-8621BE7CE244)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_GATEWAY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-52EC9AB6-50EB-467C-A57E-43B7D20654E7)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_OPTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-20268D8C-69C2-46B8-A2B4-57AAFFB91FBC)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-AB326799-616B-488F-9890-61590F87F655)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_AUTHORIZE_SUBSCRIPTION_PAYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-301DC049-1F8D-4863-8760-58BBA607BCFB)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_AUTHORIZE_SUBSCRIPTION_PAYMENT_RECEIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-D92818E0-F12B-4FF6-98F3-7F65ACEAF717)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_COUNTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-648D6164-BE10-4D51-B6E6-1B8C53EB53EC)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_BILL_TO_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-C5B84CD4-7B8D-46F8-AA09-D69CE5D5672E)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAYMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-F0CA884C-0B3C-41CE-A508-9907565B6C7D)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_CREDIT_CARD_PAYMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-B0BE42B5-AC11-434A-B513-21F8E8F1F38C)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_CREDIT_CARD_PAYMENT_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-86C6C8EE-80DB-41F2-BB5D-3056D2F2CDC9)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_CURRENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-78AFB1F5-F07B-4530-9E1D-47A5D30D7EE1)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_ECHECK_PAYMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-5219B40A-FDE5-4287-ACD9-E25ADEE8BC70)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-1375DCE0-4374-4D08-A58D-EF8A303310D9)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-433404C7-3D75-4071-9E68-EB6F0DF73060)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-AC1EE7CC-D9BE-4030-B1CE-E93024371261)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-83FF5D23-B808-40B6-BEE7-CB2E4C9EA677)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-C8E7FEB9-0299-4A90-9E1C-30143F5A4BDF)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_LINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-A92BDF8E-AC4C-4320-91AC-6DA09FA994FD)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_LINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-32D9539E-0277-4B12-9DFA-9CD495E32073)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_INVOICE_LINE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-194AFEF4-EF5D-4381-83F0-16C245B4E744)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_OTHER_PAYMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-FF468237-78B3-4AFC-A456-536DEB5FB555)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_INVOICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-0A133155-F9D9-4AC7-9E3D-737AD1F8DDC9)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_INVOICE_RECEIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-5A9F0FD7-96F5-4336-8D1F-E6DEAD35CE2B)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-70C84DB2-62FF-457C-AEE0-23F95357FC44)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAY_SUBSCRIPTION_RECEIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-FD95E454-A3B7-49BD-BF55-B3948596CD4C)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAYPAL_PAYMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-E43FE45C-0AE0-49BB-A39A-2D7A79108E32)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_PAYPAL_PAYMENT_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-41C652A8-BCD7-4712-8305-A65DE289FD82)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-1E64AC6C-1700-4BC9-9FD2-679240696013)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-E7A8286A-B56C-4F6F-A333-6A195FC6B589)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_SUBSCRIPTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-02AC0504-E759-4247-A055-24F65EDC4CAE)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_UPDATE_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-C6D40746-F428-49C4-A084-70C1DC959931)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_VERIFY_ADDRESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-F2F88376-1B58-42D9-BD8D-3BC4EF5FF2AA)
- [DBMS_CLOUD_OCI_OSP_GATEWAY_VERIFY_ADDRESS_RECEIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osp_gateway_t.html#ADSDK-GUID-82D15FDF-847D-4805-9B56-CD532468DE8A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
