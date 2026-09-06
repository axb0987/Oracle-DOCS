# WAA Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html
- Fetched: 2026-09-05 19:22 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#dcoc-content-body)

## WAA Common Types

### DBMS_CLOUD_OCI_WAA_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_CHANGE_RESOURCE_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAA_CHANGE_WEB_APP_ACCELERATION_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAA_CHANGE_WEB_APP_ACCELERATION_POLICY_COMPARTMENT_DETAILS_T Type

Updates compartmentId of resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_WAA_CREATE_WEB_APP_ACCELERATION_DETAILS_T Type

The information about new WebAppAcceleration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppAcceleration display name, can be renamed.

`backend_type`

(required) Type of the WebAppFirewall, as example LOAD_BALANCER.

Allowed values are: 'LOAD_BALANCER'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppAccelerationPolicy, which is attached to the resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_CREATE_WEB_APP_ACCELERATION_LOAD_BALANCER_DETAILS_T Type

The information about new WebAppAccelerationLoadBalancer.

Syntax
```

```

`dbms_cloud_oci_waa_create_web_app_acceleration_load_balancer_details_t`is a subtype of the`dbms_cloud_oci_waa_create_web_app_acceleration_details_t`type.

Fields

Field Description

`load_balancer_id`

(required) LoadBalancer[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the WebAppAccelerationPolicy is attached to.

### DBMS_CLOUD_OCI_WAA_RESPONSE_CACHING_POLICY_T Type

An object that specifies an HTTP response caching policy.

Syntax
```

```

Fields

Field Description

`is_response_header_based_caching_enabled`

(optional) When false, responses will not be cached by the backend based on response headers. When true, responses that contain one of the supported cache control headers will be cached according to the values specified in the cache control headers. The \"X-Accel-Expires\" header field sets caching time of a response in seconds. The zero value disables caching for a response. If the value starts with the @ prefix, it sets an absolute time in seconds since Epoch, up to which the response may be cached. If the header does not include the \"X-Accel-Expires\" field, parameters of caching may be set in the header fields \"Expires\" or \"Cache-Control\". If the header includes the \"Set-Cookie\" field, such a response will not be cached. If the header includes the \"Vary\" field with the special value \"*\", such a response will not be cached. If the header includes the \"Vary\" field with another value, such a response will be cached taking into account the corresponding request header fields.

### DBMS_CLOUD_OCI_WAA_GZIP_COMPRESSION_POLICY_T Type

An object that specifies the gzip compression policy.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) When true, support for gzip compression is enabled. HTTP responses will be compressed with gzip only if the client indicates support for gzip via the \"Accept-Encoding: gzip\" request header. When false, support for gzip compression is disabled and HTTP responses will not be compressed with gzip even if the client indicates support for gzip.

### DBMS_CLOUD_OCI_WAA_RESPONSE_COMPRESSION_POLICY_T Type

An object that specifies a compression policy for HTTP response from ENABLEMENT POINT to the client. This compression policy can be used to enable support for HTTP response compression algorithms like gzip and configure the conditions of when a compression algorithm will be used. HTTP responses will only be compressed if the client indicates support for one of the enabled compression algorithms via the \"Accept-Encoding\" request header.

Syntax
```

```

Fields

Field Description

`gzip_compression`

(optional)

### DBMS_CLOUD_OCI_WAA_CREATE_WEB_APP_ACCELERATION_POLICY_DETAILS_T Type

The information about new WebAppAccelerationPolicy.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppAccelerationPolicy display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`response_caching_policy`

(optional)

`response_compression_policy`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_WAA_PURGE_WEB_APP_ACCELERATION_CACHE_DETAILS_T Type

Specifies options for a cache purge.

Syntax
```

```

Fields

Field Description

`purge_type`

(required) Type of cache purge to perform.

Allowed values are: 'ENTIRE_CACHE'

### DBMS_CLOUD_OCI_WAA_PURGE_ENTIRE_WEB_APP_ACCELERATION_CACHE_DETAILS_T Type

Clears all resources from the cache of the WebAppAcceleration.

Syntax
```

```

`dbms_cloud_oci_waa_purge_entire_web_app_acceleration_cache_details_t`is a subtype of the`dbms_cloud_oci_waa_purge_web_app_acceleration_cache_details_t`type.

### DBMS_CLOUD_OCI_WAA_UPDATE_WEB_APP_ACCELERATION_DETAILS_T Type

The information to be updated for WebAppAcceleration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppAcceleration display name, can be renamed.

`web_app_acceleration_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppAccelerationPolicy, which is attached to the resource. This update guarantees that the resource always has WebAppAccelerationPolicy attached at any time.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_UPDATE_WEB_APP_ACCELERATION_POLICY_DETAILS_T Type

The information to be updated. When updating WebAppAccelerationPolicy, shallow merge is used for all top-level fields, meaning that top-level fields with defined values are completely overwritten and top-level fields without defined values are unchanged.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) WebAppAccelerationPolicy display name, can be renamed.

`response_caching_policy`

(optional)

`response_compression_policy`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_T Type

A resource connecting a WebAppAccelerationPolicy to a backend of particular type, applying that policy's coverage to the backend.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`display_name`

(required) WebAppAcceleration display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`backend_type`

(required) Type of the WebAppFirewall, as example LOAD_BALANCER.

Allowed values are: 'LOAD_BALANCER'

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppAccelerationPolicy, which is attached to the resource.

`time_created`

(required) The time the WebAppAcceleration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppAcceleration was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppAcceleration.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_SUMMARY_T Type

Summary of the WebAppAcceleration.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`display_name`

(required) WebAppAcceleration display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`backend_type`

(required) Type of the WebAppFirewall, as example LOAD_BALANCER.

Allowed values are: 'LOAD_BALANCER'

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of WebAppAccelerationPolicy, which is attached to the resource.

`time_created`

(required) The time the WebAppAcceleration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppAcceleration was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppAcceleration.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waa_web_app_acceleration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_COLLECTION_T Type

Result of a WebAppAcceleration list operation.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WebAppAccelerations.

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_LOAD_BALANCER_T Type

WebAppAcceleration to a LoadBalancer resource.

Syntax
```

```

`dbms_cloud_oci_waa_web_app_acceleration_load_balancer_t`is a subtype of the`dbms_cloud_oci_waa_web_app_acceleration_t`type.

Fields

Field Description

`load_balancer_id`

(required) LoadBalancer[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the WebAppAccelerationPolicy is attached to.

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_LOAD_BALANCER_SUMMARY_T Type

Summary of the WebAppAccelerationLoadBalancer.

Syntax
```

```

`dbms_cloud_oci_waa_web_app_acceleration_load_balancer_summary_t`is a subtype of the`dbms_cloud_oci_waa_web_app_acceleration_summary_t`type.

Fields

Field Description

`load_balancer_id`

(required) LoadBalancer[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to which the WebAppAccelerationPolicy is attached to.

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_T Type

The details of WebAppAccelerationPolicy. A policy is comprised of rules, which allows enablement of Caching and Compression of HTTP response. Caching can be enabled for a particular path Compression is enabled at global level

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAccelerationPolicy.

`display_name`

(required) WebAppAccelerationPolicy display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time the WebAppAccelerationPolicy was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppAccelerationPolicy was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppAccelerationPolicy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`response_caching_policy`

(optional)

`response_compression_policy`

(optional)

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_SUMMARY_T Type

Summary of the WebAppAccelerationPolicy.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAccelerationPolicy.

`display_name`

(required) WebAppAccelerationPolicy display name, can be renamed.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`time_created`

(required) The time the WebAppAccelerationPolicy was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the WebAppAccelerationPolicy was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the WebAppAccelerationPolicy.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(required) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_waa_web_app_acceleration_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_COLLECTION_T Type

Contains WebAppAccelerationPolicySummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of WebAppAccelerationPolicySummary objects.

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a WorkRequest.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the WorkRequest affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the WorkRequest. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource the WorkRequest affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_waa_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_T Type

A description of WorkRequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the WorkRequest

Allowed values are: 'CREATE_WAA_POLICY', 'UPDATE_WAA_POLICY', 'DELETE_WAA_POLICY', 'MOVE_WAA_POLICY', 'CREATE_WEB_APP_ACCELERATION', 'UPDATE_WEB_APP_ACCELERATION', 'DELETE_WEB_APP_ACCELERATION', 'MOVE_WEB_APP_ACCELERATION', 'PURGE_WEB_APP_ACCELERATION_CACHE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WorkRequest.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the WorkRequest. WorkRequests should be scoped to the same compartment as the resource the work request affects.

`resources`

(required) The resources affected by this WorkRequest.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_waa_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_COLLECTION_T Type

Result of a WorkRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequests.

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_ERROR_T Type

An error encountered while executing a WorkRequest.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on https://docs.cloud.oracle.com/Content/API/References/apierrors.htm.

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_waa_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_ERROR_COLLECTION_T Type

Result of a WorkRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestError objects.

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a WorkRequest.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_waa_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WAA_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Result of a WorkRequestLog search. Contains both WorkRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of WorkRequestLogEntries.

- [WAA Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-E04B65F3-6559-489C-AF90-74618661F538)
- [DBMS_CLOUD_OCI_WAA_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-C6F9629B-5691-4FA0-9F0C-93F09245A6DA)
- [DBMS_CLOUD_OCI_WAA_CHANGE_RESOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-546F3DF6-8F52-4211-A103-A6FECDABE2F3)
- [DBMS_CLOUD_OCI_WAA_CHANGE_WEB_APP_ACCELERATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-264B3EC4-E47B-48CD-ABD5-2242ECCA0EDE)
- [DBMS_CLOUD_OCI_WAA_CHANGE_WEB_APP_ACCELERATION_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-DBB0D8F0-A048-4A21-BCFA-A969E2BCD77B)
- [DBMS_CLOUD_OCI_WAA_CREATE_WEB_APP_ACCELERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-ED4546E8-52AB-49AF-8DF3-15E3DD583A14)
- [DBMS_CLOUD_OCI_WAA_CREATE_WEB_APP_ACCELERATION_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-683B4196-CE61-44BB-888B-CCEB6BFAB480)
- [DBMS_CLOUD_OCI_WAA_RESPONSE_CACHING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-EC809798-D780-48ED-A4A6-EDE6984C8F43)
- [DBMS_CLOUD_OCI_WAA_GZIP_COMPRESSION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-5A494B4F-3C63-4DBC-9EC6-7004F7138CE0)
- [DBMS_CLOUD_OCI_WAA_RESPONSE_COMPRESSION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-F790333D-4C72-4745-8267-9F81C3826101)
- [DBMS_CLOUD_OCI_WAA_CREATE_WEB_APP_ACCELERATION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-34F211E3-A7F8-451A-8033-E93E9013BF4D)
- [DBMS_CLOUD_OCI_WAA_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-193B6B35-4E0F-423D-8F3B-021140D3E4B1)
- [DBMS_CLOUD_OCI_WAA_PURGE_WEB_APP_ACCELERATION_CACHE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-5F013B95-AC13-46D8-A211-FD2E06680471)
- [DBMS_CLOUD_OCI_WAA_PURGE_ENTIRE_WEB_APP_ACCELERATION_CACHE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-CFF6D2CF-128C-4DD5-AEF7-212FBBB40F77)
- [DBMS_CLOUD_OCI_WAA_UPDATE_WEB_APP_ACCELERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-6B19DE67-4097-47A8-ACA0-9845BA1E5892)
- [DBMS_CLOUD_OCI_WAA_UPDATE_WEB_APP_ACCELERATION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-B5F61593-DA30-4897-A810-299A21ADECF9)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-C786F282-1C2C-468B-AEB9-10F0C0926350)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-4C4276AE-027A-486F-80EC-3BB1C1FF1EE5)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-6F119A96-8B08-4654-936E-156D025A6804)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-9568DF8D-E50F-43A9-96F9-0CE9860160A9)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_LOAD_BALANCER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-3DA55956-FFF7-4539-A6D6-51C3938AE82E)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_LOAD_BALANCER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-5DFBB7C6-8BFD-40EF-8C96-4562C92FCA69)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-42C89F5C-0E75-49AE-88DF-D0492BBB82D5)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-E0F02FA4-CB85-4BD7-9413-F98067FCA1BA)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-9F06F418-9742-4587-AF24-D1E782BCE455)
- [DBMS_CLOUD_OCI_WAA_WEB_APP_ACCELERATION_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-FEF69678-27D6-4003-A31B-6AFB42B4AC6F)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-BE86A4A8-910B-41AC-9B46-874A2AE8F105)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-93C9AE24-B2A9-4295-BCDF-921E1AE11F9F)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-301DFA57-6064-40B0-BD65-63A59F64F5F8)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-0327AB73-8217-417C-98E5-962BB4B46270)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-1F5A3C59-3AA5-4D64-91F9-C3A4A5471B61)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-FAA38453-CC4A-442E-B1DD-3B66A74E0D97)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-0019DB83-F798-4160-A73D-CE6D4D2D2F2D)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-F8FB0C32-4FCB-4CC2-B08D-1B8F0543E4EC)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-8124CDB6-7D29-4BDA-9EEB-ABD43C385AC2)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-54766810-D4F6-4F2C-A536-626F6F6A30D8)
- [DBMS_CLOUD_OCI_WAA_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/waa_t.html#ADSDK-GUID-44D08C5E-BB7F-4865-AB8D-E09CA984D6CD)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
