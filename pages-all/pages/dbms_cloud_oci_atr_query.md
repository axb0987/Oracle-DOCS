# Application Performance Monitoring Traces Query Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_query.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_query.html#dcoc-content-body)

## Application Performance Monitoring Traces Query Functions

Package: DBMS_CLOUD_OCI_ATR_QUERY

### LIST_QUICK_PICKS Function

Returns a list of predefined Quick Pick queries intended to assist the user to choose a query to run. There is no sorting applied on the results.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-trace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### QUERY Function

Retrieves the results (selected attributes and aggregations) of a query constructed according to the Application Performance Monitoring Defined Query Syntax. Query results are filtered by the filter criteria specified in the where clause. Further query results are grouped by the attributes specified in the group by clause. Finally, ordering (asc/desc) is done by the specified attributes in the order by clause.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`time_span_started_greater_than_or_equal_to`

(required) Include spans that have a `spanStartTime` equal to or greater than this value.

`time_span_started_less_than`

(required) Include spans that have a `spanStartTime`less than this value.

`query_details`

(required) Request body containing the query to be run against the trace data and to filter and retrieve trace data results.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-trace.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Application Performance Monitoring Traces Query Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_query.html#ADSDK-GUID-667FC091-FE7A-478E-9607-A9368679428D)
- [LIST_QUICK_PICKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_query.html#ADSDK-GUID-1A385C19-AC06-413C-AC7A-BE204FE8E83A)
- [QUERY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_atr_query.html#ADSDK-GUID-F6546D6F-C7AC-4C00-95F7-C9B81552C0C4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
