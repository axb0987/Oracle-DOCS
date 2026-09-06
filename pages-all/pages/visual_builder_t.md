# Visual Builder Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#dcoc-content-body)

## Visual Builder Common Types

### DBMS_CLOUD_OCI_VISUAL_BUILDER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_APPLICATION_SUMMARY_T Type

Summary of the Vb Instance's applications.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier of the application.

`project_id`

(required) Project identifier.

`version`

(required) Version of deployed application.

`state`

(required) Represents the deployment state of the application.

Allowed values are: 'STAGE', 'LIVE'

### DBMS_CLOUD_OCI_VISUAL_BUILDER_APPLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_application_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_APPLICATION_SUMMARY_COLLECTION_T Type

Result of listing VbInstance's applications. Contains ApplicationSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) The collection of ApplicationSummary objects.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_ATTACHMENT_DETAILS_T Type

Description of an attachments for this instance

Syntax
```

```

Fields

Field Description

`target_role`

(required) The role of the target attachment. * `PARENT` - The target instance is the parent of this attachment. * `CHILD` - The target instance is the child of this attachment.

Allowed values are: 'PARENT', 'CHILD'

`is_implicit`

(required) * If role == `PARENT`, the attached instance was created by this service instance * If role == `CHILD`, this instance was created from attached instance on behalf of a user

`target_id`

(required) The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.

`target_instance_url`

(required) The dataplane instance URL of the attached instance

`target_service_type`

(required) The type of the target instance, such as \"FUSION\".

### DBMS_CLOUD_OCI_VISUAL_BUILDER_CHANGE_VB_INSTANCE_COMPARTMENT_DETAILS_T Type

Compartment the VbInstance will be moved to

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment Identifier.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_CREATE_CUSTOM_ENDPOINT_DETAILS_T Type

Details for a custom endpoint for the vb instance (update).

Syntax
```

```

Fields

Field Description

`hostname`

(required) A custom hostname to be used for the vb instance URL, in FQDN format.

`certificate_secret_id`

(optional) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret Note the update will fail if this is not a valid certificate.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_CREATE_CUSTOM_ENDPOINT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_create_custom_endpoint_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_CREATE_VB_INSTANCE_DETAILS_T Type

The information about new VbInstance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Vb Instance Identifier.

`compartment_id`

(required) Compartment Identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`idcs_open_id`

(optional) Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter

`node_count`

(required) The number of Nodes

`is_visual_builder_enabled`

(optional) Visual Builder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints to be used for the vb instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

`consumption_model`

(optional) Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.

Allowed values are: 'UCM', 'GOV', 'VB4SAAS'

### DBMS_CLOUD_OCI_VISUAL_BUILDER_CUSTOM_ENDPOINT_DETAILS_T Type

Details for a custom endpoint for the vb instance.

Syntax
```

```

Fields

Field Description

`hostname`

(required) A custom hostname to be used for the vb instance URL, in FQDN format.

`certificate_secret_id`

(optional) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.

`certificate_secret_version`

(optional) The secret version used for the certificate-secret-id (if certificate-secret-id is specified).

### DBMS_CLOUD_OCI_VISUAL_BUILDER_ERROR_T Type

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

### DBMS_CLOUD_OCI_VISUAL_BUILDER_IDCS_INFO_DETAILS_T Type

Information for IDCS access

Syntax
```

```

Fields

Field Description

`idcs_app_location_url`

(required) URL for the location of the IDCS Application (used by IDCS APIs)

`idcs_app_display_name`

(required) The IDCS application display name associated with the instance

`idcs_app_id`

(required) The IDCS application ID associated with the instance

`idcs_app_name`

(required) The IDCS application name associated with the instance

`instance_primary_audience_url`

(required) The URL used as the primary audience for visual builder flows in this instance type: string

### DBMS_CLOUD_OCI_VISUAL_BUILDER_REQUEST_SUMMARIZED_APPLICATIONS_DETAILS_T Type

The information to summarize the applications.

Syntax
```

```

Fields

Field Description

`idcs_open_id`

(optional) Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter

### DBMS_CLOUD_OCI_VISUAL_BUILDER_UPDATE_CUSTOM_ENDPOINT_DETAILS_T Type

Details for a custom endpoint for the vb instance (update).

Syntax
```

```

Fields

Field Description

`hostname`

(required) A custom hostname to be used for the vb instance URL, in FQDN format.

`certificate_secret_id`

(optional) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret. Note the update will fail if this is not a valid certificate.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_UPDATE_CUSTOM_ENDPOINT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_update_custom_endpoint_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_UPDATE_VB_INSTANCE_DETAILS_T Type

Information about updating a VbInstance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Vb Instance Identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`idcs_open_id`

(optional) Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter

`node_count`

(optional) The number of Nodes

`is_visual_builder_enabled`

(optional) Enable Visual Builder. If Visual Builder is enabled alredy, then it cannot be disabled.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints to be used for the vb instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

### DBMS_CLOUD_OCI_VISUAL_BUILDER_CUSTOM_ENDPOINT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_custom_endpoint_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_ATTACHMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_attachment_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_T Type

Description of Vb Instance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Vb Instance Identifier, can be renamed.

`compartment_id`

(required) Compartment Identifier.

`time_created`

(optional) The time the the VbInstance was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the VbInstance was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the vb instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`state_message`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`instance_url`

(required) The Vb Instance URL.

`node_count`

(required) The number of Nodes

`is_visual_builder_enabled`

(optional) Visual Builder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints used for the vb instance URL.

`consumption_model`

(optional) The entitlement used for billing purposes.

Allowed values are: 'UCM', 'GOV', 'VB4SAAS'

`idcs_info`

(optional)

`attachments`

(optional) A list of associated attachments to other services

`service_nat_gateway_ip`

(optional) The NAT gateway IP address for the VB service VCN

`management_nat_gateway_ip`

(optional) The NAT gateway IP address for the VB management VCN

`service_vcn_id`

(optional) The Oracle Cloud ID (OCID) of the Visual Builder service VCN

`management_vcn_id`

(optional) The Oracle Cloud ID (OCID) of the Visual Builder management VCN

### DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_SUMMARY_T Type

Summary of the Vb Instance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Vb Instance Identifier, can be renamed.

`compartment_id`

(required) Compartment Identifier.

`time_created`

(optional) The time the the Vb Instance was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the VbInstance was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Vb Instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`state_message`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`instance_url`

(required) The Vb Instance URL.

`node_count`

(required) The number of Nodes

`is_visual_builder_enabled`

(optional) Visual Builder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints used for the vb instance URL.

`consumption_model`

(optional) The entitlement used for billing purposes.

Allowed values are: 'UCM', 'GOV', 'VB4SAAS'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_vb_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_SUMMARY_COLLECTION_T Type

Result of a VbInstance Summary request. Contains VbInstanceSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) The collection of VbInstanceSummary objects.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request is affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'STOPPED', 'STARTED', 'DELETED', 'IN_PROGRESS'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_T Type

A description of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_VB_INSTANCE', 'UPDATE_VB_INSTANCE', 'STOP_VB_INSTANCE', 'START_VB_INSTANCE', 'DELETE_VB_INSTANCE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_ERROR_T Type

Errors related to a specific work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_ERROR_COLLECTION_T Type

Result of a WorkRequest Error request. Contains list of WorkRequestError items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of objects containing errors related to a specific work request..

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_LOG_ENTRY_T Type

Log entries related to a specific work request.

Syntax
```

```

Fields

Field Description

`message`

(required) The description of an action that occurred.

`l_timestamp`

(required) The date and time the log entry occurred.

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Result of a WorkRequest Log request. Contains list of WorkRequestLog items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of objects containing logs related to a specific work request..

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_SUMMARY_T Type

A description of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_VB_INSTANCE', 'UPDATE_VB_INSTANCE', 'STOP_VB_INSTANCE', 'START_VB_INSTANCE', 'DELETE_VB_INSTANCE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_visual_builder_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Result of a WorkRequest Summary request. Contains WorkRequestSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) The collection of WorkRequestSummary objects.

- [Visual Builder Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-E3704B5D-56B3-4681-B975-2F54987893D1)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-1C245B6F-196C-4C71-B129-BEB1D29C29CB)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-08813F3C-924F-4BC5-83FE-E49DC32AEBB9)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_APPLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-2746F4AD-C14B-4389-A528-36ED8A39F237)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_APPLICATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-F94D90FF-7338-47A9-9BFC-E3B3C83B82B3)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-CE4A4A9F-FB2E-4DBF-A4D1-696552A0F57F)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_CHANGE_VB_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-8B301984-18F9-4DE2-BA7F-B7D09EB213E9)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_CREATE_CUSTOM_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-FEC9027F-7811-4312-9B96-12F6B0A392A7)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_CREATE_CUSTOM_ENDPOINT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-F566C940-7AA2-49F3-9411-9B652638365C)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_CREATE_VB_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-02921806-806E-4F23-BE8F-78282CDC5877)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_CUSTOM_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-A8C043DF-F990-427E-AB01-115B881CD1A8)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-9F5F40A0-09B5-451B-BA4F-99FBE4688414)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_IDCS_INFO_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-EC4F39C0-012A-46B5-81A5-B6DC8AC3CE51)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_REQUEST_SUMMARIZED_APPLICATIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-65DB358E-A0FD-4A08-A469-442982A1430A)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_UPDATE_CUSTOM_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-A7201C3D-1404-45F1-9F63-499E13E32F76)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_UPDATE_CUSTOM_ENDPOINT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-61E2AC72-F572-4190-9960-6B13F74E6BDE)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_UPDATE_VB_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-CB98A5E9-7A93-41DA-8A81-86B95AFEB127)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_CUSTOM_ENDPOINT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-915AE89A-14F9-4635-8CAC-C63A15422659)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_ATTACHMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-9F8A82D3-1D58-433A-9789-9D732EE2F7D3)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-9A3E642A-8BDA-4440-A9DB-4D34471087E7)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-6DF38048-4554-466B-A4B8-C54DB6DB63E2)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-9A67EF9A-6C41-41A6-A953-9C0F8EAF6D85)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_VB_INSTANCE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-6E4CEDCF-D57C-42F7-BFF9-47F999585FBC)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-2EC7F863-A086-443C-9338-636AC145DEB8)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-95783FD6-452E-4F35-85FC-D59F37D408A7)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-F9B7C6FA-26C7-426A-9E00-33311C0F017E)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-DA32E31D-C0AE-4587-B688-73381E5B117C)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-85C16068-8A3D-4B05-B62D-2329F70216CB)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-8F0D8B15-576D-4615-9CB0-5B25FE3A3967)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-C080B411-355B-4F55-BF29-F55DF909647F)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-F8C381C5-7353-4443-8448-8253BF7D7C69)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-0697DB14-1295-4643-9331-DE30A8A7ABC8)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-E90C2B8F-5B95-4326-901E-628351ADE563)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-986E67AC-8333-412D-BD5D-1B0CF567ACFD)
- [DBMS_CLOUD_OCI_VISUAL_BUILDER_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/visual_builder_t.html#ADSDK-GUID-2CD65AD7-D88B-4448-82C2-8156B98EE729)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
