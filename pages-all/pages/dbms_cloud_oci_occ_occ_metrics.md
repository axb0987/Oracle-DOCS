# OCI Control Center Metrics Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_occ_occ_metrics.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_occ_occ_metrics.html#dcoc-content-body)

## OCI Control Center Metrics Functions

Package: DBMS_CLOUD_OCI_OCC_OCC_METRICS

### LIST_METRIC_PROPERTIES Function

Returns a list of available metrics for the given namespace. The results for metrics with dimensions includes list of all the associated dimensions. The results are sorted by the metricName and then by dimension in ascending alphabetical order. For a list of valid namespaces, see`LIST_NAMESPACES`Function.

Syntax
```

```

Parameters

Parameter Description

`namespace_name`

(required) The name of the source service emitting the metric.

`compartment_id`

(required) The OCID of the compartment to use for authorization. To use the root compartment, provide the tenancyId.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see &lt;a href=\"https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine\"&gt;List Pagination&lt;/a&gt;.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://control-center.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NAMESPACES Function

List all the available source services called namespaces emitting metrics for this region. The namespaces are sorted in ascending alphabetical order.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment to use for authorization. To use the root compartment, provide the tenancyId.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see &lt;a href=\"https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine\"&gt;List Pagination&lt;/a&gt;.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://control-center.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_METRIC_DATA Function

Returns the summarized data for the given metric from the given namespace. The aggregation method depends on the metric. The metric data can be filtered by providing the dimension, startTime or endTime. The metric data in the response is sorted by dimension in ascending order and then by sampleTime in ascending chronological order.

Syntax
```

```

Parameters

Parameter Description

`request_summarized_metric_data_details`

(required) Filters to apply to the metric data query

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see &lt;a href=\"https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine\"&gt;List Pagination&lt;/a&gt;.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.

`opc_request_id`

(optional) Customer part of the request identifier token. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://control-center.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OCI Control Center Metrics Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_occ_occ_metrics.html#ADSDK-GUID-F3ED22DD-9F63-4E84-9BB7-370CF1424C29)
- [LIST_METRIC_PROPERTIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_occ_occ_metrics.html#ADSDK-GUID-3E5516F6-2705-4F29-AFFC-6BB69EEE7200)
- [LIST_NAMESPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_occ_occ_metrics.html#ADSDK-GUID-85F1AFE0-8207-402C-B297-FF0267545DB8)
- [REQUEST_SUMMARIZED_METRIC_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_occ_occ_metrics.html#ADSDK-GUID-EC21EAA4-16E4-44CE-AC9A-9E296C89AD80)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
