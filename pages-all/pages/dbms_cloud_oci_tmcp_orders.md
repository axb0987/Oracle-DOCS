# Tenant Manager Control Plane Orders Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_orders.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_orders.html#dcoc-content-body)

## Tenant Manager Control Plane Orders Functions

Package: DBMS_CLOUD_OCI_TMCP_ORDERS

### ACTIVATE_ORDER Function

Triggers an order activation workflow on behalf of the tenant, given by compartment ID in the body.

Syntax
```

```

Parameters

Parameter Description

`activate_order_details`

(required) The information needed to activate an order in a tenancy.

`activation_token`

(required) Activation token containing an order ID. A JWT RFC 7519-formatted string.

`opc_retry_token`

(optional) A token that uniquely identifies a request, so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request will be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ORDER Function

Returns the order details given by the order ID in the JWT.

Syntax
```

```

Parameters

Parameter Description

`activation_token`

(required) Activation token containing an order ID. A JWT RFC 7519-formatted string.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Tenant Manager Control Plane Orders Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_orders.html#ADSDK-GUID-BBE4BBB2-77B7-438D-B788-9C67E0160DB7)
- [ACTIVATE_ORDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_orders.html#ADSDK-GUID-6131E486-7B43-45A9-B20C-B6ED15DE5870)
- [GET_ORDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_orders.html#ADSDK-GUID-B7A367F2-8122-4F81-82F6-991056B242C8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
