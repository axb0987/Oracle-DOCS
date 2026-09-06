# Application Performance Monitoring Traces Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html#dcoc-content-body)

## Application Performance Monitoring Traces Functions

Package: DBMS_CLOUD_OCI_ATR_TRACE

### GET_AGGREGATED_SNAPSHOT Function

Gets the aggregated snapshot identified by trace ID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`trace_key`

(required) Unique Application Performance Monitoring trace identifier (traceId).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-trace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SPAN Function

Gets the span details identified by spanId.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`span_key`

(required) Unique Application Performance Monitoring span identifier (spanId).

`trace_key`

(required) Unique Application Performance Monitoring trace identifier (traceId).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-trace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TRACE Function

Gets the trace details identified by traceId.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`trace_key`

(required) Unique Application Performance Monitoring trace identifier (traceId).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-trace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TRACE_SNAPSHOT Function

Gets the trace snapshots data identified by trace ID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`trace_key`

(required) Unique Application Performance Monitoring trace identifier (traceId).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_summarized`

(optional) If enabled, then only span level details will be sent.

`thread_id`

(optional) Thread id for which snapshots needs to be retrieved. This is an identifier of a thread, and is a positive long number generated when when a thread is created.

`snapshot_time`

(optional) Epoch time of snapshot.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-trace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Application Performance Monitoring Traces Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html#ADSDK-GUID-1D03F7EC-3C07-4B56-9BD1-FD6AEF6C8C91)
- [GET_AGGREGATED_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html#ADSDK-GUID-B65C4EAF-8085-4900-9938-1C79DC750C2A)
- [GET_SPAN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html#ADSDK-GUID-E76A1AAC-24CB-4AF4-8765-0DAAF2D74FE3)
- [GET_TRACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html#ADSDK-GUID-84425B9E-BFC1-49E4-8D94-9EE14987CD32)
- [GET_TRACE_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_trace.html#ADSDK-GUID-742B9388-C80C-4383-8EB9-86CA75FCFB36)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
