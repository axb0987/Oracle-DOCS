# Media Services Media Stream Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_stream.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_stream.html#dcoc-content-body)

## Media Services Media Stream Functions

Package: DBMS_CLOUD_OCI_MDS_MEDIA_STREAM

### GENERATE_PLAYLIST Function

Gets the playlist content for the specified Packaging Configuration and Media Asset combination.

Syntax
```

```

Parameters

Parameter Description

`stream_packaging_config_id`

(required) Unique Stream Packaging Configuration identifier.

`media_asset_id`

(required) Unique MediaAsset identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`token`

(optional) Streaming session authentication token.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_SESSION_TOKEN Function

Generate a new streaming session token.

Syntax
```

```

Parameters

Parameter Description

`generate_session_token_details`

(required) Details to generate a new stream session token.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://mediaservices.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Media Services Media Stream Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_stream.html#ADSDK-GUID-24538A70-6376-40F2-AF0B-49C2CF7E5085)
- [GENERATE_PLAYLIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_stream.html#ADSDK-GUID-2B4756B5-2E64-4922-A64E-070A3AE025F6)
- [GENERATE_SESSION_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_mds_media_stream.html#ADSDK-GUID-653F75CD-C33C-44C4-85D2-6F26D38052C6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
