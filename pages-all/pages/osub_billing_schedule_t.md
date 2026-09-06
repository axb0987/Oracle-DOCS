# OSub Billing Schedule Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html#dcoc-content-body)

## OSub Billing Schedule Common Types

### DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_PRODUCT_T Type

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

### DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_BILLING_SCHEDULE_SUMMARY_T Type

Billing schedule details related to Subscription Id

Syntax
```

```

Fields

Field Description

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

### DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_ERROR_T Type

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

- [OSub Billing Schedule Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html#ADSDK-GUID-7CAE9F77-39D5-4E21-95D7-6A67688CABC9)
- [DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html#ADSDK-GUID-6BBEAD4D-4CE1-4E5E-9866-F1035B9EE83D)
- [DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_PRODUCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html#ADSDK-GUID-3A79A9EF-33C0-4609-B0F2-FF09153FBED1)
- [DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_BILLING_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html#ADSDK-GUID-4AB1F7BE-5952-448E-8F95-CF8DD14AA2A6)
- [DBMS_CLOUD_OCI_OSUB_BILLING_SCHEDULE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_billing_schedule_t.html#ADSDK-GUID-01560D5D-7C35-4F00-AB87-F940641B8D6F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
