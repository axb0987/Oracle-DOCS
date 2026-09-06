# OSP Gateway Address Service Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_address_service.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_address_service.html#dcoc-content-body)

## OSP Gateway Address Service Functions

Package: DBMS_CLOUD_OCI_OG_ADDRESS_SERVICE

### GET_ADDRESS Function

Get the address by id for the compartment

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`address_id`

(required) The identifier of the address.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ospap.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VERIFY_ADDRESS Function

Verify address

Syntax
```

```

Parameters

Parameter Description

`osp_home_region`

(required) The home region's public name of the logged in user.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`verify_address_details`

(required) Address request.

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

- [OSP Gateway Address Service Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_address_service.html#ADSDK-GUID-E4F0FD15-19F7-4A62-B60F-8F991F9E8358)
- [GET_ADDRESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_address_service.html#ADSDK-GUID-592E76C9-5B7B-4BFC-8C58-0ED204DEF6B1)
- [VERIFY_ADDRESS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_og_address_service.html#ADSDK-GUID-BC214798-7E7D-48A1-9599-BA3691E83B77)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
