# Application Performance Monitoring Synthetics Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#dcoc-content-body)

## Application Performance Monitoring Synthetics Functions

Package: DBMS_CLOUD_OCI_ASY_APM_SYNTHETIC

### AGGREGATE_NETWORK_DATA Function

Gets aggregated network data for given executions.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`monitor_id`

(required) The OCID of the monitor.

`aggregate_network_data_details`

(required) Details of the vantage point and corresponding execution times.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEDICATED_VANTAGE_POINT Function

Registers a new dedicated vantage point.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`create_dedicated_vantage_point_details`

(required) The configuration details for registering a dedicated vantage point.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MONITOR Function

Creates a new monitor.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`create_monitor_details`

(required) The configuration details for creating a monitor.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SCRIPT Function

Creates a new script.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`create_script_details`

(required) The configuration details for creating a script.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEDICATED_VANTAGE_POINT Function

Deregisters the specified dedicated vantage point.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`dedicated_vantage_point_id`

(required) The OCID of the dedicated vantage point.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MONITOR Function

Deletes the specified monitor.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`monitor_id`

(required) The OCID of the monitor.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SCRIPT Function

Deletes the specified script.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`script_id`

(required) The OCID of the script.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEDICATED_VANTAGE_POINT Function

Gets the details of the dedicated vantage point identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`dedicated_vantage_point_id`

(required) The OCID of the dedicated vantage point.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MONITOR Function

Gets the configuration of the monitor identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`monitor_id`

(required) The OCID of the monitor.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MONITOR_RESULT Function

Gets the results for a specific execution of a monitor identified by OCID. The results are in a HAR file, Screenshot, Console Log or Network details.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`monitor_id`

(required) The OCID of the monitor.

`vantage_point`

(required) The vantagePoint name.

`result_type`

(required) The result type: har, screenshot, log, or network.

`result_content_type`

(required) The result content type: zip or raw.

`execution_time`

(required) The time the object was posted.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SCRIPT Function

Gets the configuration of the script identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`script_id`

(required) The OCID of the script.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEDICATED_VANTAGE_POINTS Function

Returns a list of dedicated vantage points.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The maximum number of results per page, or items to return in a paginated \"List\" call. For information on how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order of displayName is ascending. Default order of timeCreated and timeUpdated is descending. The displayName sort by is case-sensitive.

Allowed values are: 'displayName', 'name', 'timeCreated', 'timeUpdated', 'status'

`display_name`

(optional) A filter to return only the resources that match the entire display name.

`name`

(optional) A filter to return only the resources that match the entire name.

`status`

(optional) A filter to return only the dedicated vantage points that match a given status.

Allowed values are: 'ENABLED', 'DISABLED'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MONITORS Function

Returns a list of monitors.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`display_name`

(optional) A filter to return only the resources that match the entire display name.

`script_id`

(optional) A filter to return only monitors using scriptId.

`vantage_point`

(optional) The name of the public or dedicated vantage point.

`monitor_type`

(optional) A filter to return only monitors that match the given monitor type. Supported values are SCRIPTED_BROWSER, BROWSER, SCRIPTED_REST and REST.

`status`

(optional) A filter to return only monitors that match the status given.

Allowed values are: 'ENABLED', 'DISABLED', 'INVALID'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The maximum number of results per page, or items to return in a paginated \"List\" call. For information on how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`is_maintenance_window_active`

(optional) A filter to return the monitors whose maintenance window is currently active.

`is_maintenance_window_set`

(optional) A filter to return the monitors whose maintenance window is set.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order of displayName is ascending. Default order of timeCreated and timeUpdated is descending. The displayName sort by is case insensitive.

Allowed values are: 'displayName', 'timeCreated', 'timeUpdated', 'status', 'monitorType', 'maintenanceWindowTimeStarted'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PUBLIC_VANTAGE_POINTS Function

Returns a list of public vantage points.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The maximum number of results per page, or items to return in a paginated \"List\" call. For information on how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort by (`sortBy`). Default order for displayName or name is ascending. The displayName or name sort by is case insensitive.

Allowed values are: 'name', 'displayName'

`display_name`

(optional) A filter to return only the resources that match the entire display name.

`name`

(optional) A filter to return only the resources that match the entire name.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCRIPTS Function

Returns a list of scripts.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`display_name`

(optional) A filter to return only the resources that match the entire display name.

`content_type`

(optional) A filter to return only resources that match the content type given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The maximum number of results per page, or items to return in a paginated \"List\" call. For information on how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order of displayName and contentType is ascending. Default order of timeCreated and timeUpdated is descending. The displayName sort by is case insensitive.

Allowed values are: 'displayName', 'timeCreated', 'timeUpdated', 'contentType'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEDICATED_VANTAGE_POINT Function

Updates the dedicated vantage point.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`dedicated_vantage_point_id`

(required) The OCID of the dedicated vantage point.

`update_dedicated_vantage_point_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MONITOR Function

Updates the monitor.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`monitor_id`

(required) The OCID of the monitor.

`update_monitor_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SCRIPT Function

Updates the script.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM domain ID the request is intended for.

`script_id`

(required) The OCID of the script.

`update_script_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-synthetic.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Application Performance Monitoring Synthetics Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-DA67EF51-D7EA-4E79-9AFC-09F528CE276C)
- [AGGREGATE_NETWORK_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-FAA7E2F2-6B78-4951-A4DB-88B487EFBE0E)
- [CREATE_DEDICATED_VANTAGE_POINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-19759DFC-5A42-444F-8E7B-BDA90D94DADF)
- [CREATE_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-62ACEF2A-D6F4-4B46-8061-D2CCAF332F4C)
- [CREATE_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-6E5E64B7-D02B-4049-8DC2-903644773672)
- [DELETE_DEDICATED_VANTAGE_POINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-0AA6DE90-54E7-4A3E-832A-4CFAE9F41212)
- [DELETE_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-53D55B97-6850-4B87-A905-2C9216E41BC0)
- [DELETE_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-CF5C8072-2D02-4313-99FC-E0BB42FBCC08)
- [GET_DEDICATED_VANTAGE_POINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-E8110C79-872D-4C6E-A619-943F79082787)
- [GET_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-A627F1A4-7EA5-4923-B336-7966E49FFCEB)
- [GET_MONITOR_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-8408D6E0-95BB-4FC3-8CE5-41B3AAE6ADC1)
- [GET_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-96961346-479D-4EBB-9FCE-14017B8EF211)
- [LIST_DEDICATED_VANTAGE_POINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-F20F813F-BFCD-490C-B673-87D33CDE9913)
- [LIST_MONITORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-CD62C5E3-9944-4943-89E0-E3FA2A5BB133)
- [LIST_PUBLIC_VANTAGE_POINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-75D60F60-63B7-443F-8FCB-70E800782CFD)
- [LIST_SCRIPTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-C5881203-D5EE-40EC-BE28-7E8B28AF4FD1)
- [UPDATE_DEDICATED_VANTAGE_POINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-6DC0BFB5-23A0-4725-9233-826AE5CD1DCF)
- [UPDATE_MONITOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-7EC38107-2633-48F5-9233-F8EB968EBA32)
- [UPDATE_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asy_apm_synthetic.html#ADSDK-GUID-B0C9A9F4-0DA9-4E71-913F-70F3DFC3984D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
