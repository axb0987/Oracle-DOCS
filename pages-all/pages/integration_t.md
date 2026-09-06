# Integration Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#dcoc-content-body)

## Integration Common Types

### DBMS_CLOUD_OCI_INTEGRATION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_ATTACHMENT_DETAILS_T Type

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

### DBMS_CLOUD_OCI_INTEGRATION_CHANGE_INTEGRATION_INSTANCE_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) Compartment Identifier.

### DBMS_CLOUD_OCI_INTEGRATION_NETWORK_ENDPOINT_DETAILS_T Type

Base representation of a network endpoint.

Syntax
```

```

Fields

Field Description

`network_endpoint_type`

(required) The type of network endpoint.

Allowed values are: 'PUBLIC'

### DBMS_CLOUD_OCI_INTEGRATION_CHANGE_INTEGRATION_INSTANCE_NETWORK_ENDPOINT_DETAILS_T Type

Input payload to update an Integration instance endpoint details. An empty payload will clear out any existing configuration. Some actions may not be applicable to specific integration types, see[Differences in Instance Management](https://docs.oracle.com/en/cloud/paas/application-integration/whats-new/index.html#GUID-6366FC51-5836-4D2E-AF8E-E9E939BF7330)for details.

Syntax
```

```

Fields

Field Description

`network_endpoint_details`

(optional)

### DBMS_CLOUD_OCI_INTEGRATION_OUTBOUND_CONNECTION_T Type

Base representation for Outbound Connection (Reverse Connection).

Syntax
```

```

Fields

Field Description

`outbound_connection_type`

(required) The type of Outbound Connection.

Allowed values are: 'PRIVATE_ENDPOINT', 'NONE'

### DBMS_CLOUD_OCI_INTEGRATION_CHANGE_PRIVATE_ENDPOINT_OUTBOUND_CONNECTION_DETAILS_T Type

Input payload to ADD/REMOVE Private Endpoint Outbound Connection for given IntegrationInstance. Some actions may not be applicable to specific integration types, see[Differences in Instance Management](https://docs.oracle.com/en/cloud/paas/application-integration/whats-new/index.html#GUID-6366FC51-5836-4D2E-AF8E-E9E939BF7330)for details.

Syntax
```

```

Fields

Field Description

`private_endpoint_outbound_connection`

(optional)

### DBMS_CLOUD_OCI_INTEGRATION_CREATE_CUSTOM_ENDPOINT_DETAILS_T Type

Details for a custom endpoint for the integration instance (update).

Syntax
```

```

Fields

Field Description

`hostname`

(required) A custom hostname to be used for the integration instance URL, in FQDN format.

`certificate_secret_id`

(optional) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret Note the update will fail if this is not a valid certificate.

### DBMS_CLOUD_OCI_INTEGRATION_CREATE_CUSTOM_ENDPOINT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_integration_create_custom_endpoint_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_CREATE_INTEGRATION_INSTANCE_DETAILS_T Type

The information about new IntegrationInstance. Some properties may not be applicable to specific integration types, see[Differences in Instance Management](https://docs.oracle.com/en/cloud/paas/application-integration/whats-new/index.html#GUID-6366FC51-5836-4D2E-AF8E-E9E939BF7330)for details.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Integration Instance Identifier.

`compartment_id`

(required) Compartment Identifier.

`integration_instance_type`

(required) Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX

Allowed values are: 'STANDARD', 'ENTERPRISE', 'STANDARDX', 'ENTERPRISEX'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_byol`

(required) Bring your own license.

`idcs_at`

(optional) IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.

`message_packs`

(required) The number of configured message packs

`is_visual_builder_enabled`

(optional) Visual Builder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints to be used for the integration instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

`consumption_model`

(optional) Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.

Allowed values are: 'UCM', 'GOV', 'OIC4SAAS'

`is_file_server_enabled`

(optional) The file server is enabled or not.

`network_endpoint_details`

(optional)

`shape`

(optional) Shape

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`domain_id`

(optional) The OCID of the identity domain, that will be used to determine the corresponding Idcs Stripe and create an Idcs application within the stripe. This parameter is mutually exclusive with parameter: idcsAt, i.e only one of two parameters should be specified.

### DBMS_CLOUD_OCI_INTEGRATION_CUSTOM_ENDPOINT_DETAILS_T Type

Details for a custom endpoint for the integration instance.

Syntax
```

```

Fields

Field Description

`hostname`

(required) A custom hostname to be used for the integration instance URL, in FQDN format.

`certificate_secret_id`

(optional) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.

`certificate_secret_version`

(optional) The secret version used for the certificate-secret-id (if certificate-secret-id is specified).

`alias`

(optional) When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.

### DBMS_CLOUD_OCI_INTEGRATION_ERROR_T Type

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

### DBMS_CLOUD_OCI_INTEGRATION_IDCS_INFO_DETAILS_T Type

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

(required) The URL used as the primary audience for integration flows in this instance type: string

### DBMS_CLOUD_OCI_INTEGRATION_CUSTOM_ENDPOINT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_integration_custom_endpoint_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_ATTACHMENT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_integration_attachment_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_INTEGRATION_INSTANCE_T Type

Description of Integration Instance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Integration Instance Identifier, can be renamed.

`compartment_id`

(required) Compartment Identifier.

`integration_instance_type`

(required) Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX

Allowed values are: 'STANDARD', 'ENTERPRISE', 'STANDARDX', 'ENTERPRISEX'

`time_created`

(optional) The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the integration instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`state_message`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_byol`

(required) Bring your own license.

`instance_url`

(required) The Integration Instance URL.

`message_packs`

(required) The number of configured message packs (if any)

`is_file_server_enabled`

(optional) The file server is enabled or not.

`is_visual_builder_enabled`

(optional) VisualBuilder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints used for the integration instance URL.

`consumption_model`

(optional) The entitlement used for billing purposes.

Allowed values are: 'UCM', 'GOV', 'OIC4SAAS'

`network_endpoint_details`

(optional)

`idcs_info`

(optional)

`attachments`

(optional) A list of associated attachments to other services

`shape`

(optional) Shape

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`private_endpoint_outbound_connection`

(optional)

### DBMS_CLOUD_OCI_INTEGRATION_INTEGRATION_INSTANCE_SUMMARY_T Type

Summary of the Integration Instance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) Integration Instance Identifier, can be renamed.

`compartment_id`

(required) Compartment Identifier.

`integration_instance_type`

(required) Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX

Allowed values are: 'STANDARD', 'ENTERPRISE', 'STANDARDX', 'ENTERPRISEX'

`time_created`

(optional) The time the the Integration Instance was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Integration Instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`state_message`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`is_byol`

(required) Bring your own license.

`instance_url`

(required) The Integration Instance URL.

`message_packs`

(required) The number of configured message packs (if any)

`is_file_server_enabled`

(optional) The file server is enabled or not.

`is_visual_builder_enabled`

(optional) Visual Builder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints used for the integration instance URL.

`consumption_model`

(optional) The entitlement used for billing purposes.

Allowed values are: 'UCM', 'GOV', 'OIC4SAAS'

`network_endpoint_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`shape`

(optional) Shape

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`private_endpoint_outbound_connection`

(optional)

### DBMS_CLOUD_OCI_INTEGRATION_NONE_OUTBOUND_CONNECTION_T Type

Details required for removing Private Endpoint Outbound Connection (ReverseConnection).

Syntax
```

```

`dbms_cloud_oci_integration_none_outbound_connection_t`is a subtype of the`dbms_cloud_oci_integration_outbound_connection_t`type.

### DBMS_CLOUD_OCI_INTEGRATION_PRIVATE_ENDPOINT_OUTBOUND_CONNECTION_T Type

Details required for creating Private Endpoint Outbound Connection (ReverseConnection).

Syntax
```

```

`dbms_cloud_oci_integration_private_endpoint_outbound_connection_t`is a subtype of the`dbms_cloud_oci_integration_outbound_connection_t`type.

Fields

Field Description

`subnet_id`

(required) Customer Private Network VCN Subnet OCID. This is a required argument.

`nsg_ids`

(optional) One or more Network security group Ids. This is an optional argument.

### DBMS_CLOUD_OCI_INTEGRATION_VIRTUAL_CLOUD_NETWORK_T Type

Virtual Cloud Network definition.

Syntax
```

```

Fields

Field Description

`id`

(required) The Virtual Cloud Network OCID.

`allowlisted_ips`

(optional) Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\") An invalid IP or CIDR block will result in a 400 response.

### DBMS_CLOUD_OCI_INTEGRATION_VIRTUAL_CLOUD_NETWORK_TBL Type

Nested table type of dbms_cloud_oci_integration_virtual_cloud_network_t.

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_PUBLIC_ENDPOINT_DETAILS_T Type

Public endpoint configuration details.

Syntax
```

```

`dbms_cloud_oci_integration_public_endpoint_details_t`is a subtype of the`dbms_cloud_oci_integration_network_endpoint_details_t`type.

Fields

Field Description

`allowlisted_http_ips`

(optional) Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\") An invalid IP or CIDR block will result in a 400 response.

`allowlisted_http_vcns`

(optional) Virtual Cloud Networks allowed to access this network endpoint.

`is_integration_vcn_allowlisted`

(optional) The Integration service's VCN is allow-listed to allow integrations to call back into other integrations

### DBMS_CLOUD_OCI_INTEGRATION_UPDATE_CUSTOM_ENDPOINT_DETAILS_T Type

Details for a custom endpoint for the integration instance (update).

Syntax
```

```

Fields

Field Description

`hostname`

(required) A custom hostname to be used for the integration instance URL, in FQDN format.

`certificate_secret_id`

(optional) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret. Note the update will fail if this is not a valid certificate.

### DBMS_CLOUD_OCI_INTEGRATION_UPDATE_CUSTOM_ENDPOINT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_integration_update_custom_endpoint_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_UPDATE_INTEGRATION_INSTANCE_DETAILS_T Type

The information to be updated. Some properties may not be applicable to specific integration types, see[Differences in Instance Management](https://docs.oracle.com/en/cloud/paas/application-integration/whats-new/index.html#GUID-6366FC51-5836-4D2E-AF8E-E9E939BF7330)for details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Integration Instance Identifier.

`integration_instance_type`

(optional) Standard or Enterprise type, Oracle Integration Generation 2 uses ENTERPRISE and STANDARD, Oracle Integration 3 uses ENTERPRISEX and STANDARDX

Allowed values are: 'STANDARD', 'ENTERPRISE', 'STANDARDX', 'ENTERPRISEX'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_byol`

(optional) Bring your own license.

`message_packs`

(optional) The number of configured message packs

`is_file_server_enabled`

(optional) The file server is enabled or not.

`is_visual_builder_enabled`

(optional) Visual Builder is enabled or not.

`custom_endpoint`

(optional)

`alternate_custom_endpoints`

(optional) A list of alternate custom endpoints to be used for the integration instance URL (contact Oracle for alternateCustomEndpoints availability for a specific instance).

### DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_RESOURCE_T Type

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

### DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_integration_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_T Type

A description of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_INTEGRATION_INSTANCE', 'UPDATE_INTEGRATION_INSTANCE', 'STOP_INTEGRATION_INSTANCE', 'START_INTEGRATION_INSTANCE', 'DELETE_INTEGRATION_INSTANCE', 'CHANGE_PRIVATE_ENDPOINT_OUTBOUND_CONNECTION', 'ENABLE_PROCESS_AUTOMATION'

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

### DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_SUMMARY_T Type

A description of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_INTEGRATION_INSTANCE', 'UPDATE_INTEGRATION_INSTANCE', 'STOP_INTEGRATION_INSTANCE', 'START_INTEGRATION_INSTANCE', 'DELETE_INTEGRATION_INSTANCE', 'CHANGE_PRIVATE_ENDPOINT_OUTBOUND_CONNECTION', 'ENABLE_PROCESS_AUTOMATION'

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

- [Integration Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-33F28078-784C-4CA8-8D2F-D5F1B02A95C4)
- [DBMS_CLOUD_OCI_INTEGRATION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-A8449AD5-6307-47C8-BD69-C0FC821DF5EB)
- [DBMS_CLOUD_OCI_INTEGRATION_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-E10DF9D2-1D1B-4A5C-852A-5E15946084C7)
- [DBMS_CLOUD_OCI_INTEGRATION_CHANGE_INTEGRATION_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-A05CD515-725A-4110-B240-95E44BCE65A4)
- [DBMS_CLOUD_OCI_INTEGRATION_NETWORK_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-6EBD5211-2310-4186-9B7A-7CC0EDAFBECC)
- [DBMS_CLOUD_OCI_INTEGRATION_CHANGE_INTEGRATION_INSTANCE_NETWORK_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-BD7EAE2E-C5B9-465A-8288-46743C39BC1E)
- [DBMS_CLOUD_OCI_INTEGRATION_OUTBOUND_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-AC9CB0A4-A240-4DF3-811A-7D2131C5B502)
- [DBMS_CLOUD_OCI_INTEGRATION_CHANGE_PRIVATE_ENDPOINT_OUTBOUND_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-7C13E470-AD01-499B-A71A-37A0AC0CB0FD)
- [DBMS_CLOUD_OCI_INTEGRATION_CREATE_CUSTOM_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-79AF531D-A84C-42CC-BAFC-766C788C0E27)
- [DBMS_CLOUD_OCI_INTEGRATION_CREATE_CUSTOM_ENDPOINT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-248C70D7-1BE4-4758-9609-79EBBF24E3F2)
- [DBMS_CLOUD_OCI_INTEGRATION_CREATE_INTEGRATION_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-800A217C-6E67-4127-BBBD-DB33CF9D56B0)
- [DBMS_CLOUD_OCI_INTEGRATION_CUSTOM_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-C9E87C43-7E7F-46A7-950E-B09CF552420E)
- [DBMS_CLOUD_OCI_INTEGRATION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-89EDC344-5BE4-4CAF-BA27-86DB7BC6A375)
- [DBMS_CLOUD_OCI_INTEGRATION_IDCS_INFO_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-638F3E1A-ECD5-4E22-95BA-AFB902E7E071)
- [DBMS_CLOUD_OCI_INTEGRATION_CUSTOM_ENDPOINT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-D340683C-6635-44B7-8882-0A8D66E6E7AD)
- [DBMS_CLOUD_OCI_INTEGRATION_ATTACHMENT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-9076A5AB-058D-466C-B7E5-5E34405249CB)
- [DBMS_CLOUD_OCI_INTEGRATION_INTEGRATION_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-F81C43E6-1C28-423B-963A-B754CB0D70A3)
- [DBMS_CLOUD_OCI_INTEGRATION_INTEGRATION_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-015D9B4C-345B-4AFD-8CD1-CB040C0B9BB2)
- [DBMS_CLOUD_OCI_INTEGRATION_NONE_OUTBOUND_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-20C1F7C1-B3F6-4B91-80AC-5335899FD1D3)
- [DBMS_CLOUD_OCI_INTEGRATION_PRIVATE_ENDPOINT_OUTBOUND_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-64D41BEC-5B2F-45FB-ABA3-D325766F3ADE)
- [DBMS_CLOUD_OCI_INTEGRATION_VIRTUAL_CLOUD_NETWORK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-CAAAF857-992F-48BC-AEF2-B9D9E4ADB631)
- [DBMS_CLOUD_OCI_INTEGRATION_VIRTUAL_CLOUD_NETWORK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-04C5A5F3-21A1-4775-B2FE-24D744DE02B9)
- [DBMS_CLOUD_OCI_INTEGRATION_PUBLIC_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-16192548-74D1-4861-995F-A64325B6041F)
- [DBMS_CLOUD_OCI_INTEGRATION_UPDATE_CUSTOM_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-BCB905E4-6863-4839-9D6D-7E9A646262E1)
- [DBMS_CLOUD_OCI_INTEGRATION_UPDATE_CUSTOM_ENDPOINT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-2756ECCC-6B5B-4972-A810-6866282FE1E6)
- [DBMS_CLOUD_OCI_INTEGRATION_UPDATE_INTEGRATION_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-BC01EB7F-B7FC-4C5B-99D2-6E3B54CE3231)
- [DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-19660C2D-95C0-473F-AE49-2C9B6B74E78E)
- [DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-2F36DB6A-49D7-4DD3-9CC3-94B9E6522B36)
- [DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-4891C91D-E46A-4603-A5F1-EEA4CCA69DBA)
- [DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-ADBD8336-8A5D-43C3-88AB-845097EE6083)
- [DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-E56EF6C9-65FC-499F-8ED3-151C98C4BD59)
- [DBMS_CLOUD_OCI_INTEGRATION_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/integration_t.html#ADSDK-GUID-427F2394-0311-4605-BF15-76FFBD6CC309)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
