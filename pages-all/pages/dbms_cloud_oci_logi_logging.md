# Logging Ingestion Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_logi_logging.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_logi_logging.html#dcoc-content-body)

## Logging Ingestion Functions

Package: DBMS_CLOUD_OCI_LOGI_LOGGING

### PUT_LOGS Function

This API allows ingesting logs associated with a logId. A success response implies the data has been accepted.

Syntax
```

```

Parameters

Parameter Description

`log_id`

(required) OCID of a log to work with.

`put_logs_details`

(required) The logs to emit.

`timestamp_opc_agent_processing`

(optional) Effective timestamp, for when the agent started processing the log segment being sent. An RFC3339-formatted date-time string with milliseconds precision.

`opc_agent_version`

(optional) Version of the agent sending the request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ingestion.logging.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Logging Ingestion Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_logi_logging.html#ADSDK-GUID-445A6167-A73A-4F75-AC45-8680B79D9E54)
- [PUT_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_logi_logging.html#ADSDK-GUID-C004A80E-9583-43C0-AC83-ED6C4A2C4912)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
