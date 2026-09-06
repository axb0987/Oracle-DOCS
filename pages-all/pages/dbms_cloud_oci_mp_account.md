# Marketplace Account Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_account.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_account.html#dcoc-content-body)

## Marketplace Account Functions

Package: DBMS_CLOUD_OCI_MP_ACCOUNT

### GET_LAUNCH_ELIGIBILITY Function

Returns Tenant eligibility and other information for launching a PIC image

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`image_id`

(required) Image ID

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_THIRD_PARTY_PAID_LISTING_ELIGIBILITY Function

Returns eligibility details of the tenancy to see and launch third party paid listings

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The unique identifier for the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://marketplace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Marketplace Account Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_account.html#ADSDK-GUID-176EEC46-1C07-40F4-8127-248FE344FC42)
- [GET_LAUNCH_ELIGIBILITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_account.html#ADSDK-GUID-755A59F3-3841-4C03-A715-CD6220468A37)
- [GET_THIRD_PARTY_PAID_LISTING_ELIGIBILITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mp_account.html#ADSDK-GUID-4EBE870B-849A-4E9A-906C-99E4F206C87C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
