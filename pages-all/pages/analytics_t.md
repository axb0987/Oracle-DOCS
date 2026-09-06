# Analytics Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#dcoc-content-body)

## Analytics Common Types

### DBMS_CLOUD_OCI_ANALYTICS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ANALYTICS_CAPACITY_T Type

Service instance capacity metadata (e.g.: OLPU count, number of users, ...etc...).

Syntax
```

```

Fields

Field Description

`capacity_type`

(required) The capacity model to use.

Allowed values are: 'OLPU_COUNT', 'USER_COUNT'

`capacity_value`

(required) The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the number of CPUs, amount of memory or other resources allocated to the instance.

### DBMS_CLOUD_OCI_ANALYTICS_NETWORK_ENDPOINT_DETAILS_T Type

Base representation of a network endpoint.

Syntax
```

```

Fields

Field Description

`network_endpoint_type`

(required) The type of network endpoint.

Allowed values are: 'PUBLIC', 'PRIVATE'

### DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_DNS_ZONE_T Type

Private source DNS Zone model.

Syntax
```

```

Fields

Field Description

`dns_zone`

(required) Private Source DNS Zone. Ex: example-vcn.oraclevcn.com, corp.example.com.

`description`

(optional) Description of private source dns zone.

### DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_SCAN_HOST_T Type

Private source Scan Hostname model.

Syntax
```

```

Fields

Field Description

`scan_hostname`

(required) Private Source Scan hostname. Ex: db01-scan.corp.example.com, prd-db01-scan.mycompany.com.

`scan_port`

(required) Private Source Scan host port. This is the source port where SCAN protocol will get connected (e.g. 1521).

`description`

(optional) Description of private source scan host zone.

### DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_DNS_ZONE_TBL Type

Nested table type of dbms_cloud_oci_analytics_private_source_dns_zone_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_SCAN_HOST_TBL Type

Nested table type of dbms_cloud_oci_analytics_private_source_scan_host_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_ACCESS_CHANNEL_T Type

Analytics Instance Private Access Channel model.

Syntax
```

```

Fields

Field Description

`key`

(required) Private Access Channel unique identifier key.

`display_name`

(required) Display Name of the Private Access Channel.

`vcn_id`

(required) OCID of the customer VCN peered with private access channel.

`subnet_id`

(required) OCID of the customer subnet connected to private access channel.

`ip_address`

(required) IP Address of the Private Access channel.

`egress_source_ip_addresses`

(required) The list of IP addresses from the customer subnet connected to private access channel, used as a source Ip by Private Access Channel for network traffic from the AnalyticsInstance to Private Sources.

`private_source_dns_zones`

(optional) List of Private Source DNS zones registered with Private Access Channel, where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance. Min of 1 is required and Max of 30 Private Source DNS zones can be registered.

`private_source_scan_hosts`

(optional) List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.

`network_security_group_ids`

(optional) Network Security Group OCIDs for an Analytics instance.

### DBMS_CLOUD_OCI_ANALYTICS_VANITY_URL_DETAILS_T Type

Vanity url configuration details.

Syntax
```

```

Fields

Field Description

`key`

(optional) The vanity url unique identifier key.

`description`

(optional) Description of the vanity url.

`urls`

(optional) List of urls supported by this vanity URL definition (max of 3).

`hosts`

(optional) List of fully qualified hostnames supported by this vanity URL definition (max of 3).

`public_certificate`

(optional) PEM certificate for HTTPS connections.

### DBMS_CLOUD_OCI_ANALYTICS_ANALYTICS_INSTANCE_T Type

Analytics Instance metadata.

Syntax
```

```

Fields

Field Description

`id`

(required) The resource OCID.

`name`

(required) The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.

`description`

(optional) Optional description.

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(required) The current state of an instance.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING'

`feature_set`

(required) Analytics feature set.

Allowed values are: 'SELF_SERVICE_ANALYTICS', 'ENTERPRISE_ANALYTICS'

`l_capacity`

(required)

`license_type`

(optional) The license used for the service.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`email_notification`

(optional) Email address receiving notifications.

`network_endpoint_details`

(required)

`private_access_channels`

(optional) Map of PrivateAccessChannel unique identifier key as KEY and PrivateAccessChannel Object as VALUE.

`vanity_url_details`

(optional) Map of VanityUrl unique identifier key as KEY and VanityUrl Object as VALUE.

`service_url`

(optional) URL of the Analytics service.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.

`time_created`

(required) The date and time the instance was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the instance was last updated (in the format defined by RFC3339). This timestamp represents updates made through this API. External events do not influence it.

### DBMS_CLOUD_OCI_ANALYTICS_ANALYTICS_INSTANCE_SUMMARY_T Type

Analytics Instance metadata (summary view).

Syntax
```

```

Fields

Field Description

`id`

(required) The resource OCID.

`name`

(required) The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.

`description`

(optional) Optional description.

`compartment_id`

(required) The OCID of the compartment.

`lifecycle_state`

(required) The current state of an instance.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING'

`feature_set`

(required) Analytics feature set.

Allowed values are: 'SELF_SERVICE_ANALYTICS', 'ENTERPRISE_ANALYTICS'

`l_capacity`

(required)

`license_type`

(optional) The license used for the service.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`email_notification`

(optional) Email address receiving notifications.

`network_endpoint_details`

(required)

`service_url`

(optional) URL of the Analytics service.

`time_created`

(required) The date and time the instance was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the instance was last updated (in the format defined by RFC3339). This timestamp represents updates made through this API. External events do not influence it.

### DBMS_CLOUD_OCI_ANALYTICS_CHANGE_ANALYTICS_INSTANCE_NETWORK_ENDPOINT_DETAILS_T Type

Input payload to update an Analytics instance endpoint details.

Syntax
```

```

Fields

Field Description

`network_endpoint_details`

(required)

### DBMS_CLOUD_OCI_ANALYTICS_CHANGE_COMPARTMENT_DETAILS_T Type

Input payload to change a resource's compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the new compartment.

### DBMS_CLOUD_OCI_ANALYTICS_CREATE_ANALYTICS_INSTANCE_DETAILS_T Type

Input payload to create an Anaytics instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.

`description`

(optional) Optional description.

`compartment_id`

(required) The OCID of the compartment.

`feature_set`

(required) Analytics feature set.

Allowed values are: 'SELF_SERVICE_ANALYTICS', 'ENTERPRISE_ANALYTICS'

`l_capacity`

(required)

`license_type`

(required) The license used for the service.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`email_notification`

(optional) Email address receiving notifications.

`network_endpoint_details`

(optional)

`idcs_access_token`

(optional) IDCS access token identifying a stripe and service administrator user.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.

### DBMS_CLOUD_OCI_ANALYTICS_CREATE_PRIVATE_ACCESS_CHANNEL_DETAILS_T Type

Input payload to create a Private Access Channel.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Display Name of the Private Access Channel.

`vcn_id`

(required) OCID of the customer VCN peered with private access channel.

`subnet_id`

(required) OCID of the customer subnet connected to private access channel.

`private_source_dns_zones`

(required) List of Private Source DNS zones registered with Private Access Channel, where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance. Min of 1 is required and Max of 30 Private Source DNS zones can be registered.

`private_source_scan_hosts`

(optional) List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.

`network_security_group_ids`

(optional) Network Security Group OCIDs for an Analytics instance.

### DBMS_CLOUD_OCI_ANALYTICS_CREATE_VANITY_URL_DETAILS_T Type

Input payload to create a vanity url.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description.

`hosts`

(required) List of fully qualified hostnames supported by this vanity URL definition (max of 3).

`passphrase`

(optional) Passphrase for the PEM Private key (if any).

`private_key`

(required) PEM Private key for HTTPS connections.

`public_certificate`

(required) PEM certificate for HTTPS connections.

`ca_certificate`

(required) PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.

### DBMS_CLOUD_OCI_ANALYTICS_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_ENDPOINT_DETAILS_T Type

Private endpoint configuration details.

Syntax
```

```

`dbms_cloud_oci_analytics_private_endpoint_details_t`is a subtype of the`dbms_cloud_oci_analytics_network_endpoint_details_t`type.

Fields

Field Description

`vcn_id`

(required) The VCN OCID for the private endpoint.

`subnet_id`

(required) The subnet OCID for the private endpoint.

`network_security_group_ids`

(optional) Network Security Group OCIDs for an Analytics instance.

### DBMS_CLOUD_OCI_ANALYTICS_VIRTUAL_CLOUD_NETWORK_T Type

Virtual Cloud Network definition.

Syntax
```

```

Fields

Field Description

`id`

(required) The Virtual Cloud Network OCID.

`whitelisted_ips`

(optional) Source IP addresses or IP address ranges in ingress rules.

### DBMS_CLOUD_OCI_ANALYTICS_VIRTUAL_CLOUD_NETWORK_TBL Type

Nested table type of dbms_cloud_oci_analytics_virtual_cloud_network_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANALYTICS_PUBLIC_ENDPOINT_DETAILS_T Type

Public endpoint configuration details.

Syntax
```

```

`dbms_cloud_oci_analytics_public_endpoint_details_t`is a subtype of the`dbms_cloud_oci_analytics_network_endpoint_details_t`type.

Fields

Field Description

`whitelisted_ips`

(optional) Source IP addresses or IP address ranges in ingress rules.

`whitelisted_vcns`

(optional) Virtual Cloud Networks allowed to access this network endpoint.

`whitelisted_services`

(optional) Oracle Cloud Services that are allowed to access this Analytics instance.

Allowed values are: 'ALL'

### DBMS_CLOUD_OCI_ANALYTICS_SCALE_ANALYTICS_INSTANCE_DETAILS_T Type

Input payload to scale an Analytics instance up or down.

Syntax
```

```

Fields

Field Description

`l_capacity`

(required)

### DBMS_CLOUD_OCI_ANALYTICS_SET_KMS_KEY_DETAILS_T Type

Input payload to reset the OCI Vault encryption key.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(required) OCID of the OCI Vault Key encrypting the customer data stored in this Analytics instance. An empty value indicates Oracle managed default encryption (null is not supported in this API).

### DBMS_CLOUD_OCI_ANALYTICS_UPDATE_ANALYTICS_INSTANCE_DETAILS_T Type

Input payload to update an Analytics instance. Fields that are not provided will not be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) Optional description.

`email_notification`

(optional) Email address receiving notifications.

`license_type`

(optional) The license used for the service.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_ANALYTICS_UPDATE_PRIVATE_ACCESS_CHANNEL_DETAILS_T Type

Input payload to update a Private Access Channel.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display Name of the Private Access Channel.

`vcn_id`

(optional) OCID of the customer VCN peered with private access channel.

`subnet_id`

(optional) OCID of the customer subnet connected to private access channel.

`private_source_dns_zones`

(optional) List of Private Source DNS zones registered with Private Access Channel, where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance. Min of 1 is required and Max of 30 Private Source DNS zones can be registered.

`private_source_scan_hosts`

(optional) List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.

`network_security_group_ids`

(optional) Network Security Group OCIDs for an Analytics instance.

### DBMS_CLOUD_OCI_ANALYTICS_UPDATE_VANITY_URL_DETAILS_T Type

Input payload to update a vanity url.

Syntax
```

```

Fields

Field Description

`passphrase`

(optional) Passphrase for the PEM Private key (if any).

`private_key`

(required) PEM Private key for HTTPS connections.

`public_certificate`

(required) PEM certificate for HTTPS connections.

`ca_certificate`

(required) PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.

### DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_RESOURCE_T Type

Syntax
```

```

Fields

Field Description

`action_result`

(required) The way in which this resource was affected by this work request.

Allowed values are: 'COMPARTMENT_CHANGED', 'CREATED', 'DELETED', 'STARTED', 'STOPPED', 'SCALED', 'NETWORK_ENDPOINT_CHANGED', 'VANITY_URL_CREATED', 'VANITY_URL_UPDATED', 'VANITY_URL_DELETED', 'PRIVATE_ACCESS_CHANNEL_CREATED', 'PRIVATE_ACCESS_CHANNEL_UPDATED', 'PRIVATE_ACCESS_CHANNEL_DELETED', 'NONE'

`resource_type`

(required) The type of the resource the work request is affecting.

Allowed values are: 'ANALYTICS_INSTANCE'

`identifier`

(required) The OCID of the resource the work request is affecting.

`resource_uri`

(required) The URI of the affected resource.

`metadata`

(optional) Additional metadata of the resource.

### DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_analytics_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The resource OCID.

`operation_type`

(required) The operation performed by the work request.

Allowed values are: 'CREATE_ANALYTICS_INSTANCE', 'DELETE_ANALYTICS_INSTANCE', 'START_ANALYTICS_INSTANCE', 'STOP_ANALYTICS_INSTANCE', 'SCALE_ANALYTICS_INSTANCE', 'CHANGE_ANALYTICS_INSTANCE_COMPARTMENT', 'CHANGE_ANALYTICS_INSTANCE_NETWORK_ENDPOINT', 'CREATE_VANITY_URL', 'UPDATE_VANITY_URL', 'DELETE_VANITY_URL', 'CREATE_PRIVATE_ACCESS_CHANNEL', 'UPDATE_PRIVATE_ACCESS_CHANNEL', 'DELETE_PRIVATE_ACCESS_CHANNEL', 'UPDATE_INSTANCE_ENCRYPTION_KEY'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The compartment OCID of this work request.

`resources`

(required) The resources this work request affects.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The time the work request was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) The time the work request was started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) The time the work request was finished, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_ERROR_T Type

Error encountered during the execution of a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) Error message.

`l_timestamp`

(required) The date and time the error occured, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_LOG_T Type

Log entries related to a specific work request.

Syntax
```

```

Fields

Field Description

`message`

(required) The description of the event that occurred.

`l_timestamp`

(required) The date and time the log entry occured, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_SUMMARY_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The resource OCID.

`operation_type`

(required) The operation performed by the work request.

Allowed values are: 'CREATE_ANALYTICS_INSTANCE', 'DELETE_ANALYTICS_INSTANCE', 'START_ANALYTICS_INSTANCE', 'STOP_ANALYTICS_INSTANCE', 'SCALE_ANALYTICS_INSTANCE', 'CHANGE_ANALYTICS_INSTANCE_COMPARTMENT', 'CHANGE_ANALYTICS_INSTANCE_NETWORK_ENDPOINT', 'CREATE_VANITY_URL', 'UPDATE_VANITY_URL', 'DELETE_VANITY_URL', 'CREATE_PRIVATE_ACCESS_CHANNEL', 'UPDATE_PRIVATE_ACCESS_CHANNEL', 'DELETE_PRIVATE_ACCESS_CHANNEL', 'UPDATE_INSTANCE_ENCRYPTION_KEY'

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The compartment OCID of this work request.

`resources`

(required) The resources this work request affects.

`time_accepted`

(required) The time the work request was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) The time the work request was started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) The time the work request was finished, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

- [Analytics Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-B899816D-662E-4A7D-B26D-99C42F7368A9)
- [DBMS_CLOUD_OCI_ANALYTICS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-72FEF3FB-8D7D-4F9D-A6E6-60670E72CE77)
- [DBMS_CLOUD_OCI_ANALYTICS_CAPACITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-89CD84FC-D30A-4483-9576-B921A53674C3)
- [DBMS_CLOUD_OCI_ANALYTICS_NETWORK_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-765A5F31-6BCA-41F4-802A-D00B5F74FDAA)
- [DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_DNS_ZONE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-356B9D24-8D63-4BD9-ABE6-8C7627E59600)
- [DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_SCAN_HOST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-5731A1EB-B380-4C1F-B3F6-39CB08DCE37D)
- [DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_DNS_ZONE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-1E72CC5D-A55B-4745-A5A7-3478BB21C2BE)
- [DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_SOURCE_SCAN_HOST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-61AA5CC2-7D3D-48E8-98F4-F39F8F850E7D)
- [DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_ACCESS_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-498581FA-09DA-4E6E-AAE7-D3B6E31E6656)
- [DBMS_CLOUD_OCI_ANALYTICS_VANITY_URL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-33FBF1B9-FD18-4CBA-A903-609AEED8C6A8)
- [DBMS_CLOUD_OCI_ANALYTICS_ANALYTICS_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-1A3EE28A-C3A6-41C2-97A7-0D7284FE3F5B)
- [DBMS_CLOUD_OCI_ANALYTICS_ANALYTICS_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-8C817512-9362-4EBB-86E5-0DB2F6E5DB0A)
- [DBMS_CLOUD_OCI_ANALYTICS_CHANGE_ANALYTICS_INSTANCE_NETWORK_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-D36EC411-F92A-484F-8528-CEFF33F9F2AF)
- [DBMS_CLOUD_OCI_ANALYTICS_CHANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-022972A5-9CDD-49F8-82C9-74EC77AD9BC4)
- [DBMS_CLOUD_OCI_ANALYTICS_CREATE_ANALYTICS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-24279EE5-3184-487B-B974-0FAEFA2317DA)
- [DBMS_CLOUD_OCI_ANALYTICS_CREATE_PRIVATE_ACCESS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-98F5C25C-05E6-40CC-8E1E-4DF49B8009D1)
- [DBMS_CLOUD_OCI_ANALYTICS_CREATE_VANITY_URL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-81AA0AD5-3F6E-4C1C-91A3-396552B59A0D)
- [DBMS_CLOUD_OCI_ANALYTICS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-E280302E-A537-4B60-82B0-C44E8094A0D1)
- [DBMS_CLOUD_OCI_ANALYTICS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-ED9A0B76-1176-4E23-965B-D8B592D700D4)
- [DBMS_CLOUD_OCI_ANALYTICS_VIRTUAL_CLOUD_NETWORK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-06E226F3-3624-4E5E-B2ED-8112824DB18C)
- [DBMS_CLOUD_OCI_ANALYTICS_VIRTUAL_CLOUD_NETWORK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-4E3A386C-A87B-4760-97EC-35CF1AB3FE01)
- [DBMS_CLOUD_OCI_ANALYTICS_PUBLIC_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-C2DDC92A-2DD9-4BD9-B170-3A97A5F1855A)
- [DBMS_CLOUD_OCI_ANALYTICS_SCALE_ANALYTICS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-B16213B9-6E37-4D74-9E45-F3DEE73B8B78)
- [DBMS_CLOUD_OCI_ANALYTICS_SET_KMS_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-A55A196C-0E97-47F4-B92D-588AA09132A5)
- [DBMS_CLOUD_OCI_ANALYTICS_UPDATE_ANALYTICS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-1EB97264-BB06-4F38-B7E7-4F58722CC916)
- [DBMS_CLOUD_OCI_ANALYTICS_UPDATE_PRIVATE_ACCESS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-F4580400-4E1F-4246-9192-C93D274AEFFC)
- [DBMS_CLOUD_OCI_ANALYTICS_UPDATE_VANITY_URL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-41ABBCAB-4FFD-43DC-90DF-501157967FDC)
- [DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-151D0A68-B77A-4D3D-B7A4-C2AA8C50D041)
- [DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-559E80B1-AA3E-4540-9187-C69405DDE8CD)
- [DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-2DA9E191-8B05-4FC1-90AB-627796EC1579)
- [DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-8DA3C05E-A041-4307-B262-D17071F9FBE4)
- [DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-6F52CCDC-E721-4676-9022-650D08150778)
- [DBMS_CLOUD_OCI_ANALYTICS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/analytics_t.html#ADSDK-GUID-18D24873-2DBE-4826-BCD3-C661204FEE26)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
