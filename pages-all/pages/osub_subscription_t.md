# OSub Subscription Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#dcoc-content-body)

## OSub Subscription Common Types

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_DETAIL_T Type

Subscribed Service commitment summary

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Commitment ID

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_SUMMARY_T Type

Subscribed Service commitment summary

Syntax
```

```

Fields

Field Description

`id`

(required) SPM internal Commitment ID

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_CURRENCY_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_ERROR_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_PRODUCT_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_RATE_CARD_TIER_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_RATE_CARD_TIER_TBL Type

Nested table type of dbms_cloud_oci_osub_subscription_rate_card_tier_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_RATE_CARD_SUMMARY_T Type

Rate Card Summary

Syntax
```

```

Fields

Field Description

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIPTION_PRODUCT_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_TBL Type

Nested table type of dbms_cloud_oci_osub_subscription_commitment_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIBED_SERVICE_SUMMARY_T Type

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

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIBED_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_osub_subscription_subscribed_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIPTION_SUMMARY_T Type

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

`subscribed_services`

(optional) List of Subscribed Services of the plan

- [OSub Subscription Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-21D421A9-22DE-406B-AB08-D944B87389F2)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-34EB58C0-B992-4E7A-890A-54744733D084)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-816A0770-C317-45C5-A04C-6F0182341CA1)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-89F2EBBB-602C-482B-B6CF-7D894D2BC17B)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-DAA43F14-A0BF-4218-A736-125D32A48AAD)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_CURRENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-1B7EF64B-CF30-4408-A9CB-9E4D37311E9D)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-C044212F-2090-4757-84A7-4F1ABF4AA4CD)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-C8F6EFD0-322A-49C2-BB9F-63E94403A786)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_RATE_CARD_TIER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-0B72CD23-AAE3-47CD-8997-307722AB6772)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_RATE_CARD_TIER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-E7E9D8F8-FB61-4E3A-9BA3-D17CC1A3B899)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_RATE_CARD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-7DF654D2-0196-4514-9869-5D1AB5B5F969)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIPTION_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-A6FA1FD0-540B-4583-B487-0F63AB20B42F)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_COMMITMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-DCF26232-250F-4169-9741-10F979E1DFE0)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIBED_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-AE4647E4-1E95-4C27-8872-FED810A6D889)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIBED_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-FB882D27-D1FE-47ED-99C1-E8744A8E0BB1)
- [DBMS_CLOUD_OCI_OSUB_SUBSCRIPTION_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_subscription_t.html#ADSDK-GUID-9EEBB724-4F27-4B6B-A014-F0632116ACEF)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
