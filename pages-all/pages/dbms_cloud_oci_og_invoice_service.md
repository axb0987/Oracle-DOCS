# OSP Gateway Invoice Service Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#dcoc-content-body)

## OSP Gateway Invoice Service Functions

Package: DBMS_CLOUD_OCI_OG_INVOICE_SERVICE

### DOWNLOAD_PDF_CONTENT Function

Returns an invoice in pdf format

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`internal_invoice_id`

(required) The identifier of the invoice.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INVOICE Function

Returns an invoice by invoice id

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`internal_invoice_id`

(required) The identifier of the invoice.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INVOICE_LINES Function

Returns the invoice product list by invoice id

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`internal_invoice_id`

(required) The identifier of the invoice.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INVOICES Function

Returns a list of invoices

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`invoice_id`

(optional) The invoice query param (not unique).

`l_type`

(optional) A filter to only return resources that match the given type exactly.

Allowed values are: 'HARDWARE', 'SUBSCRIPTION', 'SUPPORT', 'LICENSE', 'EDUCATION', 'CONSULTING', 'SERVICE', 'USAGE'

`search_text`

(optional) A filter to only return resources that match the given value. Looking for partial matches in the following fileds: Invoice No., Reference No. (plan number), Payment Ref, Total Amount(plan number), Balance Due(plan number) and Party/Customer Name

`time_invoice_start`

(optional) description: Start time (UTC) of the target invoice date range for which to fetch invoice data (inclusive).

`time_invoice_end`

(optional) description: End time (UTC) of the target invoice date range for which to fetch invoice data (exclusive).

`time_payment_start`

(optional) description: Start time (UTC) of the target payment date range for which to fetch invoice data (inclusive).

`time_payment_end`

(optional) description: End time (UTC) of the target payment date range for which to fetch invoice data (exclusive).

`status`

(optional) A filter to only return resources that match one of the status elements.

Allowed values are: 'OPEN', 'PAST_DUE', 'PAYMENT_SUBMITTED', 'CLOSED'

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.

`sort_by`

(optional) The field to sort by. Only one field can be selected for sorting.

Allowed values are: 'INVOICE_NO', 'REF_NO', 'STATUS', 'TYPE', 'INVOICE_DATE', 'DUE_DATE', 'PAYM_REF', 'TOTAL_AMOUNT', 'BALANCE_DUE'

`sort_order`

(optional) The sort order to use (ascending or descending).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PAY_INVOICE Function

Pay an invoice

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`internal_invoice_id`

(required) The identifier of the invoice.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`pay_invoice_details`

(required) Invoice payment request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) For requests that are not idempotent (creates being the main place of interest), THE APIs should take a header called opc-retry-token to identify the customer desire across requests, to introduce some level of idempotency.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OSP Gateway Invoice Service Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#ADSDK-GUID-FAC01CAD-1530-4726-B0A0-55BB996CC29B)
- [DOWNLOAD_PDF_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#ADSDK-GUID-F20821AF-E518-40A5-9DBE-C4DAA1D78493)
- [GET_INVOICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#ADSDK-GUID-7FDD8DBC-522A-4964-9D2E-ADB1020B9FEF)
- [LIST_INVOICE_LINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#ADSDK-GUID-18F307EA-3849-45FE-BEF9-E1BB23131BD6)
- [LIST_INVOICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#ADSDK-GUID-9E2C2ED8-30EA-47F1-8456-205F2FAD8B08)
- [PAY_INVOICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_invoice_service.html#ADSDK-GUID-0096AF78-203D-4EFE-9452-B971DF4E66B6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
