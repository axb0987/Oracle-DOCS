# Application Performance Monitoring Config Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#dcoc-content-body)

## Application Performance Monitoring Config Functions

Package: DBMS_CLOUD_OCI_AC_CONFIG

### CREATE_CONFIG Function

Creates a new configuration item.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`create_config_details`

(required) The configuration details of the new item.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_dry_run`

(optional) Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONFIG Function

Deletes the configuration item identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`config_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration item.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONFIG Function

Gets the configuration item identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`config_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration item.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONFIGS Function

Returns all configuration items, which can optionally be filtered by configuration type.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`config_type`

(optional) A filter to match configuration items of a given type. Supported values are SPAN_FILTER, METRIC_GROUP, and APDEX.

`display_name`

(optional) A filter to return resources that match the given display name.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The maximum number of results per page, or items to return in a paginated \"List\" call. For information on how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The displayName sort order is case-sensitive.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one \"sortBy\" value. The default order for displayName, timeCreated and timeUpdated is ascending. The displayName sort by is case-sensitive.

Allowed values are: 'displayName', 'timeCreated', 'timeUpdated'

`options_group`

(optional) A filter to return OPTIONS resources that match the given group.

`defined_tag_equals`

(optional) A list of tag filters to apply. Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_equals`

(optional) A list of tag filters to apply. Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\". All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\". Values for different tag names are interpreted as \"AND\".

`defined_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

`freeform_tag_exists`

(optional) A list of tag existence filters to apply. Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\". All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRIEVE_NAMESPACE_METRICS Function

Returns all metrics associated with the specified namespace.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`retrieve_namespace_metrics_details`

(required) The namespace to get the metrics for.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRIEVE_NAMESPACES Function

Returns all namespaces available in APM.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONFIG Function

Updates the details of the configuration item identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`config_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration item.

`update_config_details`

(required) The configuration details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_dry_run`

(optional) Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_SPAN_FILTER_PATTERN Function

Validates the Span Filter pattern (filterText) for syntactic correctness. Returns 204 on success, 422 when validation fails.

Syntax
```

```

Parameters

Parameter Description

`apm_domain_id`

(required) The APM Domain ID the request is intended for.

`validate_span_filter_pattern_details`

(required) The Span Filter pattern to validate.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://apm-config.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Application Performance Monitoring Config Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-1709F793-FB8F-4576-8FBB-75CC00D646E3)
- [CREATE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-8946B0B3-9EAE-4B91-A655-FF64284F610F)
- [DELETE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-43014B3D-013A-4406-88DD-E59C1C3A457D)
- [GET_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-F5F4DFB1-9DA7-4C7E-BC3F-FE3A7052EE45)
- [LIST_CONFIGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-34E702E6-4CCD-432D-A39B-8CF5B7875F6A)
- [RETRIEVE_NAMESPACE_METRICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-BE263787-ED32-4B84-9DA5-145A4726B017)
- [RETRIEVE_NAMESPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-4AA72635-443F-43A8-90EC-0322CFACA6F0)
- [UPDATE_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-68C92DBC-93E0-498C-A43E-DDF4052C021A)
- [VALIDATE_SPAN_FILTER_PATTERN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ac_config.html#ADSDK-GUID-D2E0579B-1771-40C1-BE74-B636D27263AE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
