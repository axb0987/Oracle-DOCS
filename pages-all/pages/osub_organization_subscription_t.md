# OSub Organization Subscription Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html#dcoc-content-body)

## OSub Organization Subscription Common Types

### DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_CURRENCY_T Type

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

### DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_ERROR_T Type

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

### DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_SUBSCRIPTION_SUMMARY_T Type

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

- [OSub Organization Subscription Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html#ADSDK-GUID-83D64686-A5D3-4A0A-9F3D-C040F6E5C70C)
- [DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html#ADSDK-GUID-18124999-B774-4813-B4BB-FEFDC0DB657B)
- [DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_CURRENCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html#ADSDK-GUID-812B2084-C297-4014-A5B6-BA768CB07BCF)
- [DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html#ADSDK-GUID-A869545E-8F3B-4B99-9A87-7ACBAEC9AD26)
- [DBMS_CLOUD_OCI_OSUB_ORGANIZATION_SUBSCRIPTION_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/osub_organization_subscription_t.html#ADSDK-GUID-C3F6EF58-1601-4790-B9AE-0301447DE9CA)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
