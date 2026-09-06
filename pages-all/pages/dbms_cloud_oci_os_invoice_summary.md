# One Subscription Invoice Summary Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_invoice_summary.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_invoice_summary.html#dcoc-content-body)

## One Subscription Invoice Summary Functions

Package: DBMS_CLOUD_OCI_OS_INVOICE_SUMMARY

### LIST_INVOICELINE_COMPUTED_USAGES Function

This is a collection API which returns a list of Invoiced Computed Usages for given Invoiceline id.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`invoice_line_id`

(required) Invoice Line Identifier - Primary Key SPM

`sort_order`

(optional) The sort order to use, either ascending ('ASC') or descending ('DESC').

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by Invoiced Computed Usages. You can provide one sort order (`sortOrder`).

Allowed values are: 'timeCreated', 'meteredOnDate'

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: '500'

`page`

(optional) The value of the 'opc-next-page' response header from the previous \"List\" call.

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. This parameter is used to control what fields to return.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INVOICES Function

This is a collection API which returns a list of Invoices for given filters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`ar_customer_transaction_id`

(required) AR Unique identifier for an invoice .

`time_from`

(optional) Initial date to filter Invoice data in SPM.

`time_to`

(optional) Final date to filter Invoice data in SPM.

`sort_order`

(optional) The sort order to use, either ascending ('ASC') or descending ('DESC').

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order ('sortOrder').

Allowed values are: 'ORDERNUMBER', 'TIMEINVOICING'

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: '500'

`page`

(optional) The value of the 'opc-next-page' response header from the previous \"List\" call.

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. This parameter is used to control what fields to return.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [One Subscription Invoice Summary Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_invoice_summary.html#ADSDK-GUID-A65D5AA1-532A-4A41-8D20-F8EC90BF4E74)
- [LIST_INVOICELINE_COMPUTED_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_invoice_summary.html#ADSDK-GUID-35657D9F-BB93-410E-AF51-CF3C06829D10)
- [LIST_INVOICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_invoice_summary.html#ADSDK-GUID-64195288-7FAF-4369-A302-9D7ACC99C656)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
