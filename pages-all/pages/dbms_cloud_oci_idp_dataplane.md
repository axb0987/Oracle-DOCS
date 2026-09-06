# Identity Dataplane Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_idp_dataplane.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_idp_dataplane.html#dcoc-content-body)

## Identity Dataplane Functions

Package: DBMS_CLOUD_OCI_IDP_DATAPLANE

### GENERATE_SCOPED_ACCESS_TOKEN Function

Based on the calling Principal and the input payload, derive the claims, and generate a scoped-access token for specific resources. For example, set scope to urn:oracle:db::id::&lt;compartment-id&gt; for access to a database in a compartment.

Syntax
```

```

Parameters

Parameter Description

`generate_scoped_access_token_details`

(required) Scoped access token request

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://auth.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_USER_SECURITY_TOKEN Function

Exchanges a valid user token-based signature (API key and UPST) for a short-lived UPST of the authenticated user principal. When not specified, the user session duration is set to a default of 60 minutes in all realms. Resulting UPSTs are refreshable while the user session has not expired.

Syntax
```

```

Parameters

Parameter Description

`generate_user_security_token_details`

(required) The key-value pair object storing the token exchange request parameters required to obtain a UPST for self.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://auth.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Identity Dataplane Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_idp_dataplane.html#ADSDK-GUID-75E6FD4D-FE43-4624-AA37-34A9AB56E8C4)
- [GENERATE_SCOPED_ACCESS_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_idp_dataplane.html#ADSDK-GUID-F53BBF84-38BE-4CA8-8BDC-19FB6F0A85FE)
- [GENERATE_USER_SECURITY_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_idp_dataplane.html#ADSDK-GUID-F3521598-D6D6-44C8-A431-3DF385BC6C59)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
