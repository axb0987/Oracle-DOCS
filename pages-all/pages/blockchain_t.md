# Blockchain Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#dcoc-content-body)

## Blockchain Common Types

### DBMS_CLOUD_OCI_BLOCKCHAIN_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_AVAILABILITY_DOMAIN_T Type

Availability Domains

Syntax
```

```

Fields

Field Description

`ads`

(optional) Availability Domain Identifiers

Allowed values are: 'AD1', 'AD2', 'AD3'

### DBMS_CLOUD_OCI_BLOCKCHAIN_OCPU_ALLOCATION_NUMBER_PARAM_T Type

OCPU allocation parameter

Syntax
```

```

Fields

Field Description

`ocpu_allocation_number`

(required) Number of OCPU allocation

### DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_T Type

An Ordering Service Node details

Syntax
```

```

Fields

Field Description

`osn_key`

(required) OSN identifier

`ad`

(required) Availability Domain of OSN

`ocpu_allocation_param`

(optional)

`lifecycle_state`

(optional) The current state of the OSN.

Allowed values are: 'ACTIVE', 'INACTIVE', 'FAILED'

### DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_T Type

A Peer details

Syntax
```

```

Fields

Field Description

`peer_key`

(required) peer identifier

`role`

(required) Peer role

`alias`

(optional) peer alias

`ocpu_allocation_param`

(optional)

`host`

(required) Host on which the Peer exists

`ad`

(required) Availability Domain of peer

`lifecycle_state`

(optional) The current state of the peer.

Allowed values are: 'ACTIVE', 'INACTIVE', 'FAILED'

### DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_TBL Type

Nested table type of dbms_cloud_oci_blockchain_osn_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_TBL Type

Nested table type of dbms_cloud_oci_blockchain_peer_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_COMPONENT_DETAILS_T Type

Blockchain Platform component details.

Syntax
```

```

Fields

Field Description

`osns`

(optional) List of OSNs

`peers`

(optional) List of Peers

### DBMS_CLOUD_OCI_BLOCKCHAIN_REPLICA_DETAILS_T Type

Number of replicas of service components like Rest Proxy, CA and Console

Syntax
```

```

Fields

Field Description

`proxy_count`

(optional) Number of REST proxy replicas

`ca_count`

(optional) Number of CA replicas

`console_count`

(optional) Number of console replicas

### DBMS_CLOUD_OCI_BLOCKCHAIN_OCPU_UTILIZATION_INFO_T Type

Ocpu utilization for a VM host

Syntax
```

```

Fields

Field Description

`host`

(optional) Host name of VM

`ocpu_utilization_number`

(optional) Number of OCPU utilized

`ocpu_capacity_number`

(optional) Number of total OCPU capacity on the host

### DBMS_CLOUD_OCI_BLOCKCHAIN_OCPU_UTILIZATION_INFO_TBL Type

Nested table type of dbms_cloud_oci_blockchain_ocpu_utilization_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_T Type

Blockchain Platform Instance Description.

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation

`display_name`

(required) Platform Instance Display name, can be renamed

`compartment_id`

(required) Compartment Identifier

`description`

(optional) Platform Instance Description

`is_byol`

(optional) Bring your own license

`time_created`

(optional) The time the the Platform Instance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Platform Instance was updated. An RFC3339 formatted datetime string

`platform_version`

(optional) Platform Version

`service_version`

(optional) The version of the Platform Instance.

`platform_role`

(required) Role of platform - FOUNDER or PARTICIPANT

Allowed values are: 'FOUNDER', 'PARTICIPANT'

`compute_shape`

(required) Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM

Allowed values are: 'STANDARD', 'ENTERPRISE_SMALL', 'ENTERPRISE_MEDIUM', 'ENTERPRISE_LARGE', 'ENTERPRISE_EXTRA_LARGE', 'ENTERPRISE_CUSTOM'

`platform_shape_type`

(optional) Type of Platform shape - DEFAULT or CUSTOM

Allowed values are: 'DEFAULT', 'CUSTOM'

`load_balancer_shape`

(optional) Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.

Allowed values are: 'LB_100_MBPS', 'LB_400_MBPS'

`service_endpoint`

(optional) Service endpoint URL, valid post-provisioning

`lifecycle_state`

(optional) The current state of the Platform Instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'SCALING', 'INACTIVE', 'FAILED'

`lifecycle_details`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`storage_size_in_t_bs`

(optional) Storage size in TBs

`storage_used_in_t_bs`

(optional) Storage used in TBs

`is_multi_ad`

(optional) True for multi-AD blockchain plaforms, false for single-AD

`total_ocpu_capacity`

(optional) Number of total OCPUs allocated to the platform cluster

`component_details`

(optional)

`replicas`

(optional)

`host_ocpu_utilization_info`

(optional) List of OcpuUtilization for all hosts

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_BY_HOSTNAME_T Type

Blockchain Platform Instance Details For Hostname.

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation

`service_endpoint`

(optional) Service endpoint URL, valid post-provisioning

`display_name`

(required) Platform Instance Display name, can be renamed

`compartment_id`

(required) Compartment Identifier

`description`

(optional) Platform Instance Description

`time_created`

(optional) The time the the Platform Instance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Platform Instance was updated. An RFC3339 formatted datetime string

`platform_role`

(optional) Role of platform - founder or participant

`compute_shape`

(required) Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM

`lifecycle_state`

(optional) The current state of the Platform Instance.

`lifecycle_details`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_SUMMARY_T Type

Blockchain Platform Instance Summary.

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation

`display_name`

(required) Platform Instance Display name, can be renamed

`compartment_id`

(required) Compartment Identifier

`description`

(optional) Platform Instance Description

`time_created`

(optional) The time the the Platform Instance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Platform Instance was updated. An RFC3339 formatted datetime string

`platform_role`

(optional) Role of platform - founder or participant

`compute_shape`

(required) Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM

`service_endpoint`

(optional) Service endpoint URL, valid post-provisioning

`lifecycle_state`

(optional) The current state of the Platform Instance.

`lifecycle_details`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_blockchain_blockchain_platform_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_COLLECTION_T Type

Result of a platform list or search. Contains BlockchainPlatformSummary

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of BlockchainPlatformSummary

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_PATCH_SUMMARY_T Type

Patch Details

Syntax
```

```

Fields

Field Description

`id`

(optional) patch id

`service_version`

(optional) patch service version

`patch_info_url`

(optional) A URL for the patch specific documentation

`time_patch_due`

(optional) patch due date for customer initiated patching

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_PATCH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_blockchain_blockchain_platform_patch_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_PATCH_COLLECTION_T Type

Result of a patch list. Contains PatchSummary

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of PatchSummary

### DBMS_CLOUD_OCI_BLOCKCHAIN_CHANGE_BLOCKCHAIN_PLATFORM_COMPARTMENT_DETAILS_T Type

Input payload to change a resource's compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the new compartment.

### DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_BLOCKCHAIN_PLATFORM_DETAILS_T Type

Blockchain Platform details for creating a new service.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Platform Instance Display name, can be renamed

`compartment_id`

(required) Compartment Identifier

`description`

(optional) Platform Instance Description

`platform_role`

(required) Role of platform - founder or participant

`compute_shape`

(required) Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE

`is_byol`

(optional) Bring your own license

`platform_version`

(optional) Platform version

`idcs_access_token`

(required) IDCS access token with Identity Domain Administrator role

`federated_user_id`

(optional) Identifier for a federated user

`ca_cert_archive_text`

(optional) Base64 encoded text in ASCII character set of a Thirdparty CA Certificates archive file. The Archive file is a zip file containing third part CA Certificates, the ca key and certificate files used when issuing enrollment certificates (ECerts) and transaction certificates (TCerts). The chainfile (if it exists) contains the certificate chain which should be trusted for this CA, where the 1st in the chain is always the root CA certificate. File list in zip file [ca-cert.pem,ca-key.pem,ca-chain.pem(optional)].

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_OSN_DETAILS_T Type

The Ordering Service Node details to be added

Syntax
```

```

Fields

Field Description

`ad`

(required) Availability Domain to place new OSN

`ocpu_allocation_param`

(optional)

### DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_PEER_DETAILS_T Type

The Peer details to be added

Syntax
```

```

Fields

Field Description

`role`

(required) Peer role

`alias`

(optional) peer alias

`ocpu_allocation_param`

(required)

`ad`

(required) Availability Domain to place new peer

### DBMS_CLOUD_OCI_BLOCKCHAIN_ERROR_T Type

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

### DBMS_CLOUD_OCI_BLOCKCHAIN_METADATA_DETAILS_T Type

Metadata parameter details

Syntax
```

```

Fields

Field Description

`param_name`

(required) Metadata param name

`param_value`

(required) Metadata param value. Complex value will be a JSON string.

`is_json_value`

(required) Indicates if the value is a JSON string

### DBMS_CLOUD_OCI_BLOCKCHAIN_MODIFY_PEER_DETAILS_T Type

peer to modify ocpu allocation

Syntax
```

```

Fields

Field Description

`peer_name`

(required) peer identifier

`ocpu_allocation_param`

(required)

### DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_SUMMARY_T Type

OSN summary information for returning in a list.

Syntax
```

```

Fields

Field Description

`osn_key`

(optional) OSN identifier

`lifecycle_state`

(optional) The current state of the OSN.

### DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_blockchain_osn_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_COLLECTION_T Type

Result of a OSN list or search. Contains OsnSummary

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of OsnSummary

### DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_SUMMARY_T Type

Peer summary information for returning in a list.

Syntax
```

```

Fields

Field Description

`peer_key`

(optional) Peer identifier

`lifecycle_state`

(optional) The current state of the peer.

### DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_blockchain_peer_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_COLLECTION_T Type

Result of a peer list or search. Contains PeerSummary

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of PeerSummary

### DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_ROLE_T Type

Peer role

Syntax
```

```

Fields

Field Description

`role`

(optional) Peer role names

Allowed values are: 'MEMBER', 'ADMIN'

### DBMS_CLOUD_OCI_BLOCKCHAIN_SCALE_STORAGE_DETAILS_T Type

storage size to increase

Syntax
```

```

Fields

Field Description

`storage_size_in_t_bs`

(required) Storage size in TBs

### DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_OSN_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_blockchain_create_osn_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_PEER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_blockchain_create_peer_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_MODIFY_PEER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_blockchain_modify_peer_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_SCALE_BLOCKCHAIN_PLATFORM_DETAILS_T Type

Scale operation details for a blockchain platform. The scale operation payload has multiple options - Add one or more Ordering Service Node (addOsns) - Add one or more Peers (addPeers) - Add more replicas of CA, Console and Rest Proxy (addReplicas) - Add more storage to the platform (addStorage) - Modify the CPU allocation for Peer Nodes (modifyPeers) - Remove one or more replicas of CA, Console and Rest Proxy (removeReplicas) - Remove one or more Ordering Service Node (removeOsns) - Remove one or more Peers (removePeers). The scale operation payload must have at least one of the above options.

Syntax
```

```

Fields

Field Description

`add_osns`

(optional) new OSNs to add

`add_replicas`

(optional)

`add_peers`

(optional) new Peers to add

`add_storage`

(optional)

`modify_peers`

(optional) modify ocpu allocation to existing Peers

`remove_replicas`

(optional)

`remove_osns`

(optional) OSN id list to remove

`remove_peers`

(optional) Peer id list to remove

### DBMS_CLOUD_OCI_BLOCKCHAIN_SCALED_PLATFORM_METERING_PREVIEW_T Type

Blockchain Platform Metering Preview after Scaling

Syntax
```

```

Fields

Field Description

`total_ocpu_allocation`

(optional) Number of total OCPU allocation for the blockchain platform

`total_ocpu_allocation_post_scaling`

(optional) Number of total OCPU allocation for the blockchain platform after Scaling

`storage_metered_units`

(optional) Current Storage metered units in TBs

`extra_storage_metered_units`

(optional) Extra Storage units required in TBs

`storage_metered_units_post_scaling`

(optional) Total Post Scaling Storage metered units in TBs

### DBMS_CLOUD_OCI_BLOCKCHAIN_SCALED_BLOCKCHAIN_PLATFORM_PREVIEW_T Type

Blockchain Platform Instance Description Preview after Scaling.

Syntax
```

```

Fields

Field Description

`id`

(required) unique identifier that is immutable on creation

`display_name`

(required) Platform Instance Display name, can be renamed

`compartment_id`

(required) Compartment Identifier

`description`

(optional) Platform Instance Description

`compute_shape`

(required) Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM

`storage_size_in_t_bs`

(optional) Storage size in TBs

`storage_size_in_t_bs_post_scaling`

(optional) Storage size in TBs post scaling

`component_details`

(optional)

`replicas`

(optional)

`component_details_post_scaling`

(optional)

`replicas_post_scaling`

(optional)

`host_ocpu_utilization_info`

(optional) List of OcpuUtilization for all hosts

`host_ocpu_utilization_info_post_scaling`

(optional) List of OcpuUtilization for all hosts after scaling

`new_vm_count`

(optional) Number of new VMs that would be created

`metering_preview`

(optional)

`scale_payload`

(optional)

### DBMS_CLOUD_OCI_BLOCKCHAIN_UPDATE_BLOCKCHAIN_PLATFORM_DETAILS_T Type

Blockchain Platform details for updating a service.

Syntax
```

```

Fields

Field Description

`description`

(optional) Platform Description

`storage_size_in_t_bs`

(optional) Storage size in TBs

`replicas`

(optional)

`total_ocpu_capacity`

(optional) Number of total OCPUs to allocate

`load_balancer_shape`

(optional) Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BLOCKCHAIN_UPDATE_OSN_DETAILS_T Type

OSN attributes that can be updated.

Syntax
```

```

Fields

Field Description

`ocpu_allocation_param`

(required)

### DBMS_CLOUD_OCI_BLOCKCHAIN_UPDATE_PEER_DETAILS_T Type

peer to modify ocpu allocation

Syntax
```

```

Fields

Field Description

`ocpu_allocation_param`

(required)

### DBMS_CLOUD_OCI_BLOCKCHAIN_UPGRADE_BLOCKCHAIN_PLATFORM_DETAILS_T Type

Input payload to upgrade the blockchain platform.

Syntax
```

```

Fields

Field Description

`patch_id`

(required) The patch ID corresponding to the version to which platform will be upgraded.

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_SUB_TYPE_DETAIL_T Type

SubType information for a work request resource.

Syntax
```

```

Fields

Field Description

`sub_type`

(required) Subtype of the work request resource like osn or peer.

`sub_type_key`

(required) The identifier of the resource subType.

`sub_type_status`

(required) Status of the resource subType, as a result of the work tracked in this work request. A resource subType would be CREATED, UPDATED or DELETED, after the work request is completed.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED'

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_SUB_TYPE_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_blockchain_work_request_resource_sub_type_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

`sub_type_details`

(optional) Collection of SubType information for a work request resource©

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_blockchain_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) type of the work request

Allowed values are: 'CREATE_PLATFORM', 'UPDATE_PLATFORM', 'UPGRADE_PLATFORM', 'DELETE_PLATFORM', 'SCALE_PLATFORM', 'START_PLATFORM', 'STOP_PLATFORM', 'CUSTOMIZE_PLATFORM', 'SCALE_STORAGE'

`status`

(required) status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

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

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_SUMMARY_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) type of the work request

Allowed values are: 'CREATE_PLATFORM', 'UPDATE_PLATFORM', 'UPGRADE_PLATFORM', 'DELETE_PLATFORM', 'SCALE_PLATFORM', 'START_PLATFORM', 'STOP_PLATFORM', 'CUSTOMIZE_PLATFORM', 'SCALE_STORAGE'

`status`

(optional) status of current work request.

`id`

(required) The id of the work request.

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

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_blockchain_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_COLLECTION_T Type

Result of a platform list or search. Contains WorkRequestSummary

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of WorkRequestSummary

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_blockchain_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_ERROR_COLLECTION_T Type

Result of a platform list or search. Contains WorkRequestError

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of WorkRequestError

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_blockchain_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Result of a platform lpnist or search. Contains WorkRequestLogEntry

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of WorkRequestLogEntry

- [Blockchain Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-6322217F-8BB2-4B59-8B0E-3F64EAD9E1C7)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-491B2405-3F02-423F-BC0F-9F575F564B66)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_AVAILABILITY_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-2FDD48A0-8FFC-43F9-B0ED-A15D59537FC8)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OCPU_ALLOCATION_NUMBER_PARAM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-3BCBA3CD-6723-4D7E-9F0F-F436E83BCE7C)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-0E45997B-94F0-4142-B1A7-50B4B3397CBD)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-5A52C69A-3122-4184-8C9D-50A4E423E1A5)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-E89F6DB2-762B-4938-815D-5EA3A2EDB405)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-28CB3244-D540-41CF-93AD-8FBCB24A0D92)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_COMPONENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-B5132D20-0AF0-4456-B12A-269AB6FA34BC)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-A946F2BE-6293-4279-88BB-EE216AA1D2D8)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OCPU_UTILIZATION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-925D658C-C7E4-4F4C-B3CE-F4CBF50A542F)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OCPU_UTILIZATION_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-AEF015A3-1814-4D8B-8FAA-5F4509E43D2C)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-2AE074BE-F26A-473D-90E1-4A1D63A85BDE)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_BY_HOSTNAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-7C59C9E2-601E-41F2-96A8-B56669E876FF)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-49221072-B8B4-40FC-8EB6-547D98235438)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-1AA3F145-C183-4A71-AA25-DA9BEC25647A)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-9FA6BE80-ED3B-4B33-8FD8-71FF608963AE)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-6695ACF1-525D-4C25-8E27-90B9FE839915)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_PATCH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-94546610-9285-4052-9F9F-4F297795AD84)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_BLOCKCHAIN_PLATFORM_PATCH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-64CACF55-CD1A-4C7B-9C90-B8E146E7ABB9)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_CHANGE_BLOCKCHAIN_PLATFORM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-249B9FC7-F95E-4DDB-8E75-CD4AC6F4708E)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_BLOCKCHAIN_PLATFORM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-479951D6-1C52-4E00-9B1C-021420102990)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_OSN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-D0E910A0-822F-44CF-BD46-32FB1CD47092)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_PEER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-A9A12CCA-827A-4FE6-8F59-19B4B627C526)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-51BFCCEA-4CD6-479B-B9EA-965BAC739E89)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_METADATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-4E80B276-66D2-475A-9F0B-C6923559CA62)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_MODIFY_PEER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-F92B5E75-F2CA-45E3-B7A0-135485821DD3)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-1AC2A5F9-E551-41C7-B6CD-05D5AD208757)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-10D4537E-FA29-4A41-A63E-3700DE4C9587)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_OSN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-2EF6E3DE-0853-4D46-8FA2-2999504570AB)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-30A37F78-0BA7-4F06-B786-D3D30B78D725)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-AADD9208-C806-4FBB-9996-288F29C1F862)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-BC25DAAC-E152-46C0-9ED2-552743798B96)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_PEER_ROLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-3D73AE41-AB8E-4157-AFE8-2A863695C70F)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_SCALE_STORAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-8D53DC62-390F-4574-9851-5C8B79A41587)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_OSN_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-B8C0702F-F8A8-4B25-850B-B4F4C3B54CFA)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_CREATE_PEER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-550E0D28-3911-4B2E-BA1C-3368EDF587ED)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_MODIFY_PEER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-8D94ED24-8042-45D5-BB1E-44B36EF70DC8)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_SCALE_BLOCKCHAIN_PLATFORM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-8E30A520-AC4D-47F2-B71D-7F6C8DDD28B5)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_SCALED_PLATFORM_METERING_PREVIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-52350A8D-AD4F-4D0C-A869-3C4C969136D0)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_SCALED_BLOCKCHAIN_PLATFORM_PREVIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-6F2FADEA-0B35-4A60-848C-07DC306ABEB9)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_UPDATE_BLOCKCHAIN_PLATFORM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-66B72380-7F68-4F3D-8354-2603B15AAC68)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_UPDATE_OSN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-32D7AE89-7918-42F9-A786-43E68F3AA28B)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_UPDATE_PEER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-1C83D344-0632-43D8-B053-EC20490D3DBC)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_UPGRADE_BLOCKCHAIN_PLATFORM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-A9D258CC-443E-4E00-8BB7-75AFFC11B53B)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_SUB_TYPE_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-65453F70-A347-4C21-8B33-A595AD7BA2E9)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_SUB_TYPE_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-76EFBEAF-0B19-499F-9728-4E342189ABF4)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-3604AEC9-C2D8-4EBA-A1A0-FBCE5347F8C4)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-5055C95C-2DDC-405C-9CE3-B260F36AF422)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-63B9D2BD-3AEC-4706-BF62-7C73408EB7F3)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-8BC0BA35-E2F7-4D68-AD6A-526B1248C3C7)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-E0B41FE1-6494-489C-A0B7-C90E97D0064E)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-C0A4D9E2-2A82-487D-B9BB-505BE5BB4AA1)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-C63B8E72-DEDF-400E-8CA7-624590E9C493)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-F3AB0D0D-CA4E-4C79-8668-844140CC2490)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-D90E82DD-FC3D-45A3-BB50-822958BDFF3F)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-FAD56593-3AFC-4FFF-9C77-396764CF883D)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-87CCA361-B02A-4D10-9AF3-4C99FC1B9CE8)
- [DBMS_CLOUD_OCI_BLOCKCHAIN_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/blockchain_t.html#ADSDK-GUID-EAB0FE36-BDA7-4694-9C30-8016542AC208)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
