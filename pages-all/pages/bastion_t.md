# Bastion Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#dcoc-content-body)

## Bastion Common Types

### DBMS_CLOUD_OCI_BASTION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_BASTION_BASTION_T Type

A bastion resource. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet.

Syntax
```

```

Fields

Field Description

`bastion_type`

(required) The type of bastion.

`id`

(required) The unique identifier (OCID) of the bastion, which can't be changed after creation.

`name`

(required) The name of the bastion, which can't be changed after creation.

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the bastion is located.

`target_vcn_id`

(required) The unique identifier (OCID) of the virtual cloud network (VCN) that the bastion connects to.

`target_subnet_id`

(required) The unique identifier (OCID) of the subnet that the bastion connects to.

`phone_book_entry`

(optional) The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.

`client_cidr_block_allow_list`

(optional) A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.

`static_jump_host_ip_addresses`

(optional) A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.

`private_endpoint_ip_address`

(optional) The private IP address of the created private endpoint.

`max_session_ttl_in_seconds`

(required) The maximum amount of time that any session on the bastion can remain active.

`max_sessions_allowed`

(optional) The maximum number of active sessions allowed on the bastion.

`dns_proxy_status`

(optional) The current dns proxy status of the bastion.

Allowed values are: 'DISABLED', 'ENABLED'

`time_created`

(required) The time the bastion was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(optional) The time the bastion was updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the bastion.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_BASTION_BASTION_SUMMARY_T Type

Summary information for a bastion resource. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet.

Syntax
```

```

Fields

Field Description

`bastion_type`

(required) The type of bastion.

`id`

(required) The unique identifier (OCID) of the bastion, which can't be changed after creation.

`name`

(required) The name of the bastion, which can't be changed after creation.

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the bastion is located.

`target_vcn_id`

(required) The unique identifier (OCID) of the virtual cloud network (VCN) that the bastion connects to.

`target_subnet_id`

(required) The unique identifier (OCID) of the subnet that the bastion connects to.

`dns_proxy_status`

(optional) The current dns proxy status of the bastion.

Allowed values are: 'DISABLED', 'ENABLED'

`time_created`

(required) The time the bastion was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(optional) The time the bastion was updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the bastion.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_BASTION_CHANGE_BASTION_COMPARTMENT_DETAILS_T Type

Details about the compartment that the bastion should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The unique identifier (OCID) of the compartment that the bastion should move to.

### DBMS_CLOUD_OCI_BASTION_CREATE_BASTION_DETAILS_T Type

The configuration details for a new bastion. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet.

Syntax
```

```

Fields

Field Description

`bastion_type`

(required) The type of bastion. Use `standard`.

`name`

(optional) The name of the bastion, which can't be changed after creation.

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the bastion is located.

`target_subnet_id`

(required) The unique identifier (OCID) of the subnet that the bastion connects to.

`phone_book_entry`

(optional) The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.

`static_jump_host_ip_addresses`

(optional) A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.

`client_cidr_block_allow_list`

(optional) A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.

`max_session_ttl_in_seconds`

(optional) The maximum amount of time that any session on the bastion can remain active.

`dns_proxy_status`

(optional) The desired dns proxy status of the bastion.

Allowed values are: 'DISABLED', 'ENABLED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BASTION_CREATE_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a bastion session's target resource.

Syntax
```

```

Fields

Field Description

`session_type`

(required) The session type.

Allowed values are: 'MANAGED_SSH', 'PORT_FORWARDING', 'DYNAMIC_PORT_FORWARDING'

### DBMS_CLOUD_OCI_BASTION_CREATE_DYNAMIC_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a dynamic port forwarding session for a target subnet.

Syntax
```

```

`dbms_cloud_oci_bastion_create_dynamic_port_forwarding_session_target_resource_details_t`is a subtype of the`dbms_cloud_oci_bastion_create_session_target_resource_details_t`type.

### DBMS_CLOUD_OCI_BASTION_CREATE_MANAGED_SSH_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a managed SSH session for a target resource.

Syntax
```

```

`dbms_cloud_oci_bastion_create_managed_ssh_session_target_resource_details_t`is a subtype of the`dbms_cloud_oci_bastion_create_session_target_resource_details_t`type.

Fields

Field Description

`target_resource_operating_system_user_name`

(required) The name of the user on the target resource operating system that the session uses for the connection.

`target_resource_id`

(required) The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.

`target_resource_private_ip_address`

(optional) The private IP address of the target resource that the session connects to.

`target_resource_port`

(optional) The port number to connect to on the target resource.

### DBMS_CLOUD_OCI_BASTION_CREATE_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a port forwarding session for a target resource.

Syntax
```

```

`dbms_cloud_oci_bastion_create_port_forwarding_session_target_resource_details_t`is a subtype of the`dbms_cloud_oci_bastion_create_session_target_resource_details_t`type.

Fields

Field Description

`target_resource_id`

(optional) The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.

`target_resource_private_ip_address`

(optional) The private IP address of the target resource that the session connects to.

`target_resource_fqdn`

(optional) The Fully Qualified Domain Name of the target resource that the session connects to.

`target_resource_port`

(optional) The port number to connect to on the target resource.

### DBMS_CLOUD_OCI_BASTION_PUBLIC_KEY_DETAILS_T Type

Public key details for a bastion session.

Syntax
```

```

Fields

Field Description

`public_key_content`

(required) The public key in OpenSSH format of the SSH key pair for the session. When you connect to the session, you must provide the private key of the same SSH key pair.

### DBMS_CLOUD_OCI_BASTION_CREATE_SESSION_DETAILS_T Type

The configuration details for a new bastion session. A session lets authorized users connect to a target resource for a predetermined amount of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the session.

`bastion_id`

(required) The unique identifier (OCID) of the bastion on which to create this session.

`target_resource_details`

(required)

`key_type`

(optional) The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.

Allowed values are: 'PUB'

`key_details`

(required)

`session_ttl_in_seconds`

(optional) The amount of time the session can remain active.

### DBMS_CLOUD_OCI_BASTION_TARGET_RESOURCE_DETAILS_T Type

Details about a bastion session's target resource.

Syntax
```

```

Fields

Field Description

`session_type`

(required) The Bastion service recognizes three types of sessions, managed SSH sessions, SSH port forwarding sessions, and Dynamic SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.

Allowed values are: 'MANAGED_SSH', 'PORT_FORWARDING', 'DYNAMIC_PORT_FORWARDING'

### DBMS_CLOUD_OCI_BASTION_DYNAMIC_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a dynamic port forwarding session for a target subnet.

Syntax
```

```

`dbms_cloud_oci_bastion_dynamic_port_forwarding_session_target_resource_details_t`is a subtype of the`dbms_cloud_oci_bastion_target_resource_details_t`type.

### DBMS_CLOUD_OCI_BASTION_ERROR_T Type

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

### DBMS_CLOUD_OCI_BASTION_MANAGED_SSH_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a managed SSH session for a target resource.

Syntax
```

```

`dbms_cloud_oci_bastion_managed_ssh_session_target_resource_details_t`is a subtype of the`dbms_cloud_oci_bastion_target_resource_details_t`type.

Fields

Field Description

`target_resource_operating_system_user_name`

(required) The name of the user on the target resource operating system that the session uses for the connection.

`target_resource_id`

(required) The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.

`target_resource_private_ip_address`

(optional) The private IP address of the target resource that the session connects to.

`target_resource_display_name`

(required) The display name of the target Compute instance that the session connects to.

`target_resource_port`

(optional) The port number to connect to on the target resource.

### DBMS_CLOUD_OCI_BASTION_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type

Details about a port forwarding session for a target resource.

Syntax
```

```

`dbms_cloud_oci_bastion_port_forwarding_session_target_resource_details_t`is a subtype of the`dbms_cloud_oci_bastion_target_resource_details_t`type.

Fields

Field Description

`target_resource_id`

(optional) The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.

`target_resource_private_ip_address`

(optional) The private IP address of the target resource that the session connects to.

`target_resource_display_name`

(optional) The display name of the target Compute instance that the session connects to.

`target_resource_fqdn`

(optional) The Fully Qualified Domain Name of the target resource that the session connects to.

`target_resource_port`

(optional) The port number to connect to on the target resource.

### DBMS_CLOUD_OCI_BASTION_SESSION_T Type

A bastion session resource. A bastion session lets authorized users connect to a target resource using a Secure Shell (SSH) for a predetermined amount of time.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the session, which can't be changed after creation.

`display_name`

(optional) The name of the session.

`bastion_id`

(required) The unique identifier (OCID) of the bastion that is hosting this session.

`bastion_name`

(required) The name of the bastion that is hosting this session.

`bastion_user_name`

(optional) The username that the session uses to connect to the target resource.

`target_resource_details`

(required)

`ssh_metadata`

(optional) The connection message for the session.

`key_type`

(optional) The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.

Allowed values are: 'PUB'

`key_details`

(required)

`bastion_public_host_key_info`

(optional) The public key of the bastion host. You can use this to verify that you're connecting to the correct bastion.

`time_created`

(required) The time the session was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(optional) The time the session was updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the session.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current session state in more detail.

`session_ttl_in_seconds`

(required) The amount of time the session can remain active.

### DBMS_CLOUD_OCI_BASTION_SESSION_SUMMARY_T Type

Summary information for a bastion session resource.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the session, which can't be changed after creation.

`display_name`

(optional) The name of the session.

`bastion_name`

(required) The name of the bastion that is hosting this session.

`bastion_id`

(required) The unique identifier (OCID) of the bastion that is hosting this session.

`target_resource_details`

(required)

`time_created`

(required) The time the session was created. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`time_updated`

(optional) The time the session was updated. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the session.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current session state in more detail.

`session_ttl_in_seconds`

(required) The amount of time the session can remain active.

### DBMS_CLOUD_OCI_BASTION_UPDATE_BASTION_DETAILS_T Type

The configuration to update on an existing bastion.

Syntax
```

```

Fields

Field Description

`max_session_ttl_in_seconds`

(optional) The maximum amount of time that any session on the bastion can remain active.

`static_jump_host_ip_addresses`

(optional) A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.

`client_cidr_block_allow_list`

(optional) A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BASTION_UPDATE_SESSION_DETAILS_T Type

The session information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the session.

### DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The unique identifier (OCID) of the resource that the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_bastion_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_T Type

A description of workrequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_BASTION', 'UPDATE_BASTION', 'DELETE_BASTION', 'CREATE_SESSION', 'DELETE_SESSION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The unique identifier (OCID) of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occurred. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_SUMMARY_T Type

A description of workrequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_BASTION', 'UPDATE_BASTION', 'DELETE_BASTION', 'CREATE_SESSION', 'DELETE_SESSION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The unique identifier (OCID) of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

- [Bastion Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-09E4A01C-D0AF-4EF7-ADCB-7EFFC7861FD5)
- [DBMS_CLOUD_OCI_BASTION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-500482C6-D69F-4D4E-BC3E-F4ED699AEBDF)
- [DBMS_CLOUD_OCI_BASTION_BASTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-B72F411B-2891-417B-893F-94FB5AC0EE43)
- [DBMS_CLOUD_OCI_BASTION_BASTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-08EE5046-85C7-469E-9324-BF87D7C74B3B)
- [DBMS_CLOUD_OCI_BASTION_CHANGE_BASTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-E656CD5A-B281-4065-9176-1A4F08FCCDAD)
- [DBMS_CLOUD_OCI_BASTION_CREATE_BASTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-75418B23-8F2E-4C44-B84F-8EEDEDCE37C9)
- [DBMS_CLOUD_OCI_BASTION_CREATE_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-8D2D0DA7-C386-48A0-B48B-1A1939207893)
- [DBMS_CLOUD_OCI_BASTION_CREATE_DYNAMIC_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-D2B9E299-35C9-4693-9171-2B06936563C0)
- [DBMS_CLOUD_OCI_BASTION_CREATE_MANAGED_SSH_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-3B00B7B8-D3F1-492A-BE90-9BFB39EE5E3D)
- [DBMS_CLOUD_OCI_BASTION_CREATE_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-500DC966-3EFB-4D97-90B3-52F8791020DE)
- [DBMS_CLOUD_OCI_BASTION_PUBLIC_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-923C8EF5-748B-44A2-BE99-FDF120C939BC)
- [DBMS_CLOUD_OCI_BASTION_CREATE_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-91C33020-DF79-44A0-9920-9DBF94F95C8D)
- [DBMS_CLOUD_OCI_BASTION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-3164EBA4-A6C1-4B2A-ABB4-7424AC1C6A3B)
- [DBMS_CLOUD_OCI_BASTION_DYNAMIC_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-3F3583B7-B1C9-4031-9E0C-BA9855364399)
- [DBMS_CLOUD_OCI_BASTION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-0EC2DA06-CA13-45E9-AC59-53464193A487)
- [DBMS_CLOUD_OCI_BASTION_MANAGED_SSH_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-C948534C-810D-41E1-8554-F3C78901DF1C)
- [DBMS_CLOUD_OCI_BASTION_PORT_FORWARDING_SESSION_TARGET_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-D6310FE7-B840-4B32-AAC0-B1D97FE88A2E)
- [DBMS_CLOUD_OCI_BASTION_SESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-96BA8E74-ABAB-46E5-BD8B-B0D92E4C171B)
- [DBMS_CLOUD_OCI_BASTION_SESSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-0B0899C0-2914-4217-9B49-A3C0FF6DB3A9)
- [DBMS_CLOUD_OCI_BASTION_UPDATE_BASTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-8E21487E-CFA4-4A03-8DB5-B94FB51DE03E)
- [DBMS_CLOUD_OCI_BASTION_UPDATE_SESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-317A65FF-85DC-4997-B576-6EDF6F944A01)
- [DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-01C056F3-ADD0-4184-A167-C1DB50829D88)
- [DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-25E6F5A6-4362-43D6-ABE6-0A774DDDA717)
- [DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-64F1F231-4AC8-49C9-B928-7435798CE102)
- [DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-8F59A6B0-2B2D-48AA-8A3F-3CDC64C6913C)
- [DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-F25F2E5A-5EE0-4ECE-9574-9ADAA4C6A68F)
- [DBMS_CLOUD_OCI_BASTION_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bastion_t.html#ADSDK-GUID-780FACE0-13EB-44E5-BF1F-F7C0B9E92B01)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
