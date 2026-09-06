# Health Checks Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#dcoc-content-body)

## Health Checks Functions

Package: DBMS_CLOUD_OCI_HC_HEALTH_CHECKS

### CHANGE_HTTP_MONITOR_COMPARTMENT Function

Moves a monitor into a different compartment. When provided, `If-Match` is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`change_http_monitor_compartment_details`

(required) The details needed to move the monitor.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_PING_MONITOR_COMPARTMENT Function

Moves a monitor into a different compartment. When provided, `If-Match` is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`change_ping_monitor_compartment_details`

(required) The details needed to move the monitor.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_HTTP_MONITOR Function

Creates an HTTP monitor. Vantage points will be automatically selected if not specified, and probes will be initiated from each vantage point to each of the targets at the frequency specified by `intervalInSeconds`.

Syntax
```

```

Parameters

Parameter Description

`create_http_monitor_details`

(required) The configuration details for creating an HTTP monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ON_DEMAND_HTTP_PROBE Function

Creates an on-demand HTTP probe. The location response header contains the URL for fetching the probe results. *Note:* On-demand probe configurations are not saved.

Syntax
```

```

Parameters

Parameter Description

`create_on_demand_http_probe_details`

(required) The configuration of the HTTP probe.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ON_DEMAND_PING_PROBE Function

Creates an on-demand ping probe. The location response header contains the URL for fetching probe results. *Note:* The on-demand probe configuration is not saved.

Syntax
```

```

Parameters

Parameter Description

`create_on_demand_ping_probe_details`

(required) Configuration details for creating an on-demand ping probe.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PING_MONITOR Function

Creates a ping monitor. Vantage points will be automatically selected if not specified, and probes will be initiated from each vantage point to each of the targets at the frequency specified by `intervalInSeconds`.

Syntax
```

```

Parameters

Parameter Description

`create_ping_monitor_details`

(required) The configuration details for creating a ping monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request that can be retried in case of a timeout or server error without risk of executing the same action again. Retry tokens expire after 24 hours. *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting operations, such as a resource being deleted or purged from the system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_HTTP_MONITOR Function

Deletes the HTTP monitor and its configuration. All future probes of this monitor are stopped. Results associated with the monitor are not deleted.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PING_MONITOR Function

Deletes the ping monitor and its configuration. All future probes of this monitor are stopped. Results associated with the monitor are not deleted.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HTTP_MONITOR Function

Gets the configuration for the specified monitor.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PING_MONITOR Function

Gets the configuration for the specified ping monitor.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_none_match`

(optional) The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HEALTH_CHECKS_VANTAGE_POINTS Function

Gets information about all vantage points available to the user.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to sort by when listing vantage points.

Allowed values are: 'name', 'displayName'

`sort_order`

(optional) Controls the sort order of results.

Allowed values are: 'ASC', 'DESC'

`name`

(optional) Filters results that exactly match the `name` field.

`display_name`

(optional) Filters results that exactly match the `displayName` field.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HTTP_MONITORS Function

Gets a list of HTTP monitors.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) Filters results by compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to sort by when listing monitors.

Allowed values are: 'id', 'displayName', 'timeCreated'

`sort_order`

(optional) Controls the sort order of results.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) Filters results that exactly match the `displayName` field.

`home_region`

(optional) Filters results that match the `homeRegion`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HTTP_PROBE_RESULTS Function

Gets the HTTP probe results for the specified probe or monitor, where the `probeConfigurationId` is the OCID of either a monitor or an on-demand probe.

Syntax
```

```

Parameters

Parameter Description

`probe_configuration_id`

(required) The OCID of a monitor or on-demand probe.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`start_time_greater_than_or_equal_to`

(optional) Returns results with a `startTime` equal to or greater than the specified value.

`start_time_less_than_or_equal_to`

(optional) Returns results with a `startTime` equal to or less than the specified value.

`sort_order`

(optional) Controls the sort order of results.

Allowed values are: 'ASC', 'DESC'

`target`

(optional) Filters results that match the `target`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PING_MONITORS Function

Gets a list of configured ping monitors. Results are paginated based on `page` and `limit`. The `opc-next-page` header provides a URL for fetching the next page.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) Filters results by compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to sort by when listing monitors.

Allowed values are: 'id', 'displayName', 'timeCreated'

`sort_order`

(optional) Controls the sort order of results.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) Filters results that exactly match the `displayName` field.

`home_region`

(optional) Filters results that match the `homeRegion`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PING_PROBE_RESULTS Function

Returns the results for the specified probe, where the `probeConfigurationId` is the OCID of either a monitor or an on-demand probe. Results are paginated based on `page` and `limit`. The `opc-next-page` header provides a URL for fetching the next page. Use `sortOrder` to set the order of the results. If `sortOrder` is unspecified, results are sorted in ascending order by `startTime`.

Syntax
```

```

Parameters

Parameter Description

`probe_configuration_id`

(required) The OCID of a monitor or on-demand probe.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`start_time_greater_than_or_equal_to`

(optional) Returns results with a `startTime` equal to or greater than the specified value.

`start_time_less_than_or_equal_to`

(optional) Returns results with a `startTime` equal to or less than the specified value.

`sort_order`

(optional) Controls the sort order of results.

Allowed values are: 'ASC', 'DESC'

`target`

(optional) Filters results that match the `target`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HTTP_MONITOR Function

Updates the configuration of the specified HTTP monitor. Only the fields specified in the request body will be updated; all other configuration properties will remain unchanged.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`update_http_monitor_details`

(required) The configuration details to update for the HTTP monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PING_MONITOR Function

Updates the configuration of the specified ping monitor. Only the fields specified in the request body will be updated; all other configuration properties will remain unchanged.

Syntax
```

```

Parameters

Parameter Description

`monitor_id`

(required) The OCID of a monitor.

`update_ping_monitor_details`

(required) Details for updating a Ping monitor.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://healthchecks.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Health Checks Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-5AF8309A-E200-41AA-8E8F-CB1C5092165C)
- [CHANGE_HTTP_MONITOR_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-6559BD34-2A15-44EF-A4D1-A3303765FE28)
- [CHANGE_PING_MONITOR_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-DF2D892C-F4B6-47DC-A189-242D5F355334)
- [CREATE_HTTP_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-A160FBBC-9F6F-4C77-BCB6-058974D9E5DE)
- [CREATE_ON_DEMAND_HTTP_PROBE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-0430C352-CA51-4205-B17E-7B1F5FA9B704)
- [CREATE_ON_DEMAND_PING_PROBE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-1FB2E36A-264A-4394-8796-C486AEFC5A9B)
- [CREATE_PING_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-B406F45E-E71C-4186-946D-6AC0ECADA3AF)
- [DELETE_HTTP_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-C08A602C-E8D5-4D35-AA1E-B8CBDFA8ADD6)
- [DELETE_PING_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-F1849359-8F69-4FE1-BF3E-5530954614C6)
- [GET_HTTP_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-13B3BCE5-9BCA-4CDD-B787-535F4B0E1AB1)
- [GET_PING_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-B6B29205-C5EF-4595-A3E6-D4B53E962E07)
- [LIST_HEALTH_CHECKS_VANTAGE_POINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-0A996AA8-61A7-457D-89A8-3D68E53AC8F0)
- [LIST_HTTP_MONITORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-17AE6F54-92C1-472F-9A98-5094B72DA4D0)
- [LIST_HTTP_PROBE_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-ED4BC20D-F7AC-4508-8D5B-8643A905500A)
- [LIST_PING_MONITORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-57200C09-DE56-4BAD-8BA5-93B570D65202)
- [LIST_PING_PROBE_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-A83919B4-A3A8-46EF-8119-F3B59BD17FF0)
- [UPDATE_HTTP_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-471AD3F1-A4B2-4960-9A68-612341D5BDFD)
- [UPDATE_PING_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_hc_health_checks.html#ADSDK-GUID-772B2C2A-51A4-4CEE-A521-BCF1A544C65F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
