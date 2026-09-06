# OSP Gateway Subscription Service Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#dcoc-content-body)

## OSP Gateway Subscription Service Functions

Package: DBMS_CLOUD_OCI_OG_SUBSCRIPTION_SERVICE

### AUTHORIZE_SUBSCRIPTION_PAYMENT Function

PSD2 authorization for subscription payment

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`subscription_id`

(required) Subscription id(OCID).

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`authorize_subscription_payment_details`

(required) subscription payment request.

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

### GET_SUBSCRIPTION Function

Get the subscription plan.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) Subscription id(OCID).

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIPTIONS Function

Get the subscription data for the compartment

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

### PAY_SUBSCRIPTION Function

Pay a subscription

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`subscription_id`

(required) Subscription id(OCID).

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`pay_subscription_details`

(required) subscription payment request.

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

### UPDATE_SUBSCRIPTION Function

Update plan of the subscription.

Syntax
```

```

Parameters

Parameter Description

`subscription_id`

(required) Subscription id(OCID).

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`update_subscription_details`

(required) Subscription update request.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OSP Gateway Subscription Service Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#ADSDK-GUID-B1132E22-AE11-49D7-89AB-DA8C59FC8283)
- [AUTHORIZE_SUBSCRIPTION_PAYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#ADSDK-GUID-3F96B383-DB9C-45EE-AC25-8EC173B8D91B)
- [GET_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#ADSDK-GUID-554A76EA-68B6-43C9-9F3C-8121C0C4922D)
- [LIST_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#ADSDK-GUID-F264AC65-804A-4097-971B-30A75400E21B)
- [PAY_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#ADSDK-GUID-EA13F56F-2CA7-4877-A65E-4FFC13C0A971)
- [UPDATE_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_subscription_service.html#ADSDK-GUID-AD8A8CB2-1398-44C7-A242-CC50BC1B7BC1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
