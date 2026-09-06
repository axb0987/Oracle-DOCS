# Core Blockstorage Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#dcoc-content-body)

## Core Blockstorage Functions

Package: DBMS_CLOUD_OCI_CR_BLOCKSTORAGE

### CHANGE_BOOT_VOLUME_BACKUP_COMPARTMENT Function

Moves a boot volume backup into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`boot_volume_backup_id`

(required) The OCID of the boot volume backup.

`change_boot_volume_backup_compartment_details`

(required) Request to change the compartment of given boot volume backup.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_BOOT_VOLUME_COMPARTMENT Function

Moves a boot volume into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`change_boot_volume_compartment_details`

(required) Request to change the compartment of given boot volume.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VOLUME_BACKUP_COMPARTMENT Function

Moves a volume backup into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`volume_backup_id`

(required) The OCID of the volume backup.

`change_volume_backup_compartment_details`

(required) Request to change the compartment of given volume backup.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VOLUME_COMPARTMENT Function

Moves a volume into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`change_volume_compartment_details`

(required) Request to change the compartment of given volume.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VOLUME_GROUP_BACKUP_COMPARTMENT Function

Moves a volume group backup into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`volume_group_backup_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

`change_volume_group_backup_compartment_details`

(required) Request to change the compartment of given volume group backup.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VOLUME_GROUP_COMPARTMENT Function

Moves a volume group into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`volume_group_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

`change_volume_group_compartment_details`

(required) Request to change the compartment of given volume group.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COPY_BOOT_VOLUME_BACKUP Function

Creates a boot volume backup copy in specified region. For general information about volume backups, see[Overview of Boot Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm)

Syntax
```

```

Parameters

Parameter Description

`boot_volume_backup_id`

(required) The OCID of the boot volume backup.

`copy_boot_volume_backup_details`

(required) Request to create a cross-region copy of given boot volume backup.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COPY_VOLUME_BACKUP Function

Creates a volume backup copy in specified region. For general information about volume backups, see[Overview of Block Volume Service Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm)

Syntax
```

```

Parameters

Parameter Description

`volume_backup_id`

(required) The OCID of the volume backup.

`copy_volume_backup_details`

(required) Request to create a cross-region copy of given backup.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COPY_VOLUME_GROUP_BACKUP Function

Creates a volume group backup copy in specified region. For general information about volume group backups, see[Overview of Block Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_backup_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

`copy_volume_group_backup_details`

(required) Request to create a cross-region copy of given volume group backup.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BOOT_VOLUME Function

Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup. For general information about boot volumes, see[Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm). You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_boot_volume_details`

(required) Request to create a new boot volume.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BOOT_VOLUME_BACKUP Function

Creates a new boot volume backup of the specified boot volume. For general information about boot volume backups, see[Overview of Boot Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm)When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

Syntax
```

```

Parameters

Parameter Description

`create_boot_volume_backup_details`

(required) Request to create a new backup of given boot volume.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VOLUME Function

Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see[Overview of Block Volume Service](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm). A volume and instance can be in separate compartments but must be in the same availability domain. For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_volume_details`

(required) Request to create a new volume.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VOLUME_BACKUP Function

Creates a new backup of the specified volume. For general information about volume backups, see[Overview of Block Volume Service Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm)When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

Syntax
```

```

Parameters

Parameter Description

`create_volume_backup_details`

(required) Request to create a new backup of given volume.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VOLUME_BACKUP_POLICY Function

Creates a new user defined backup policy. For more information about Oracle defined backup policies and user defined backup policies, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Syntax
```

```

Parameters

Parameter Description

`create_volume_backup_policy_details`

(required) Request to create a new scheduled backup policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VOLUME_BACKUP_POLICY_ASSIGNMENT Function

Assigns a volume backup policy to the specified volume. Note that a given volume can only have one backup policy assigned to it. If this operation is used for a volume that already has a different backup policy assigned, the prior backup policy will be silently unassigned.

Syntax
```

```

Parameters

Parameter Description

`create_volume_backup_policy_assignment_details`

(required) Request to assign a specified policy to a particular volume.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VOLUME_GROUP Function

Creates a new volume group in the specified compartment. A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing volume group, or by restoring a volume group backup. You may optionally specify a *display name* for the volume group, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`create_volume_group_details`

(required) Request to create a new volume group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VOLUME_GROUP_BACKUP Function

Creates a new backup volume group of the specified volume group. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`create_volume_group_backup_details`

(required) Request to create a new backup group of given volume group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BOOT_VOLUME Function

Deletes the specified boot volume. The volume cannot have an active connection to an instance. To disconnect the boot volume from a connected instance, see[Disconnecting From a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/deletingbootvolume.htm). **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BOOT_VOLUME_BACKUP Function

Deletes a boot volume backup.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_backup_id`

(required) The OCID of the boot volume backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BOOT_VOLUME_KMS_KEY Function

Removes the specified boot volume's assigned Vault Service encryption key.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME Function

Deletes the specified volume. The volume cannot have an active connection to an instance. To disconnect the volume from a connected instance, see[Disconnecting From a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/disconnectingfromavolume.htm). **Warning:** All data on the volume will be permanently lost when the volume is deleted.

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME_BACKUP Function

Deletes a volume backup.

Syntax
```

```

Parameters

Parameter Description

`volume_backup_id`

(required) The OCID of the volume backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME_BACKUP_POLICY Function

Deletes a user defined backup policy. For more information about user defined backup policies, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies). Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`policy_id`

(required) The OCID of the volume backup policy.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME_BACKUP_POLICY_ASSIGNMENT Function

Deletes a volume backup policy assignment.

Syntax
```

```

Parameters

Parameter Description

`policy_assignment_id`

(required) The OCID of the volume backup policy assignment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME_GROUP Function

Deletes the specified volume group. Individual volumes are not deleted, only the volume group is deleted. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME_GROUP_BACKUP Function

Deletes a volume group backup. This operation deletes all the backups in the volume group. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_backup_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VOLUME_KMS_KEY Function

Removes the specified volume's assigned Vault service encryption key.

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BLOCK_VOLUME_REPLICA Function

Gets information for the specified block volume replica.

Syntax
```

```

Parameters

Parameter Description

`block_volume_replica_id`

(required) The OCID of the block volume replica.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BOOT_VOLUME Function

Gets information for the specified boot volume.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BOOT_VOLUME_BACKUP Function

Gets information for the specified boot volume backup.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_backup_id`

(required) The OCID of the boot volume backup.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BOOT_VOLUME_KMS_KEY Function

Gets the Vault service encryption key assigned to the specified boot volume.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BOOT_VOLUME_REPLICA Function

Gets information for the specified boot volume replica.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_replica_id`

(required) The OCID of the boot volume replica.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME Function

Gets information for the specified volume.

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_BACKUP Function

Gets information for the specified volume backup.

Syntax
```

```

Parameters

Parameter Description

`volume_backup_id`

(required) The OCID of the volume backup.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_BACKUP_POLICY Function

Gets information for the specified volume backup policy.

Syntax
```

```

Parameters

Parameter Description

`policy_id`

(required) The OCID of the volume backup policy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_BACKUP_POLICY_ASSET_ASSIGNMENT Function

Gets the volume backup policy assignment for the specified volume. The `assetId` query parameter is required, and the returned list will contain at most one item, since volume can only have one volume backup policy assigned at a time.

Syntax
```

```

Parameters

Parameter Description

`asset_id`

(required) The OCID of an asset (e.g. a volume).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_BACKUP_POLICY_ASSIGNMENT Function

Gets information for the specified volume backup policy assignment.

Syntax
```

```

Parameters

Parameter Description

`policy_assignment_id`

(required) The OCID of the volume backup policy assignment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_GROUP Function

Gets information for the specified volume group. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_GROUP_BACKUP Function

Gets information for the specified volume group backup. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_backup_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_GROUP_REPLICA Function

Gets information for the specified volume group replica.

Syntax
```

```

Parameters

Parameter Description

`volume_group_replica_id`

(required) The OCID of the volume replica group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_KMS_KEY Function

Gets the Vault service encryption key assigned to the specified volume.

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BLOCK_VOLUME_REPLICAS Function

Lists the block volume replicas in the specified compartment and availability domain.

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`volume_group_replica_id`

(optional) The OCID of the volume group replica.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BOOT_VOLUME_BACKUPS Function

Lists the boot volume backups in the specified compartment. You can filter the results by boot volume.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`boot_volume_id`

(optional) The OCID of the boot volume.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`source_boot_volume_backup_id`

(optional) A filter to return only resources that originated from the given source boot volume backup.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BOOT_VOLUME_REPLICAS Function

Lists the boot volume replicas in the specified compartment and availability domain.

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`volume_group_replica_id`

(optional) The OCID of the volume group replica.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BOOT_VOLUMES Function

Lists the boot volumes in the specified compartment and availability domain.

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`volume_group_id`

(optional) The OCID of the volume group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUME_BACKUP_POLICIES Function

Lists all the volume backup policies available in the specified compartment. For more information about Oracle defined backup policies and user defined backup policies, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id`

(optional) The OCID of the compartment. If no compartment is specified, the Oracle defined backup policies are listed.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUME_BACKUPS Function

Lists the volume backups in the specified compartment. You can filter the results by volume.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`volume_id`

(optional) The OCID of the volume.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`source_volume_backup_id`

(optional) A filter to return only resources that originated from the given source volume backup.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUME_GROUP_BACKUPS Function

Lists the volume group backups in the specified compartment. You can filter the results by volume group. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`volume_group_id`

(optional) The OCID of the volume group.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUME_GROUP_REPLICAS Function

Lists the volume group replicas in the specified compartment. You can filter the results by volume group. For more information, see[Volume Group Replication](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroupreplication.htm).

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUME_GROUPS Function

Lists the volume groups in the specified compartment and availability domain. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUMES Function

Lists the volumes in the specified compartment and availability domain.

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`volume_group_id`

(optional) The OCID of the volume group.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BOOT_VOLUME Function

Updates the specified boot volume's display name, defined tags, and free-form tags.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`update_boot_volume_details`

(required) Update boot volume's display name.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BOOT_VOLUME_BACKUP Function

Updates the display name for the specified boot volume backup. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_backup_id`

(required) The OCID of the boot volume backup.

`update_boot_volume_backup_details`

(required) Update boot volume backup fields

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BOOT_VOLUME_KMS_KEY Function

Updates the specified volume with a new Vault service master encryption key.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_id`

(required) The OCID of the boot volume.

`update_boot_volume_kms_key_details`

(required) Updates the Vault service master encryption key assigned to the specified boot volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME Function

Updates the specified volume's display name. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`update_volume_details`

(required) Update volume's display name. Avoid entering confidential information.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME_BACKUP Function

Updates the display name for the specified volume backup. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`volume_backup_id`

(required) The OCID of the volume backup.

`update_volume_backup_details`

(required) Update volume backup fields

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME_BACKUP_POLICY Function

Updates a user defined backup policy. For more information about user defined backup policies, see[Policy-Based Backups](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies). Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`policy_id`

(required) The OCID of the volume backup policy.

`update_volume_backup_policy_details`

(required) Update volume backup policy fields

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME_GROUP Function

Updates the set of volumes in a volume group along with the display name. Use this operation to add or remove volumes in a volume group. Specify the full list of volume IDs to include in the volume group. If the volume ID is not specified in the call, it will be removed from the volume group. Avoid entering confidential information. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

`update_volume_group_details`

(required) Update volume group's set of volumes and/or display name

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`preserve_volume_replica`

(optional) Specifies whether to disable or preserve the individual volume replication when removing a volume from the replication enabled volume group. When set to `true`, the individual volume replica is preserved. The default value is `true`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME_GROUP_BACKUP Function

Updates the display name for the specified volume group backup. For more information, see[Volume Groups](https://docs.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

Syntax
```

```

Parameters

Parameter Description

`volume_group_backup_id`

(required) The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

`update_volume_group_backup_details`

(required) Update volume group backup fields

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME_KMS_KEY Function

Updates the specified volume with a new Key Management master encryption key.

Syntax
```

```

Parameters

Parameter Description

`volume_id`

(required) The OCID of the volume.

`update_volume_kms_key_details`

(required) Updates the Vault service master encryption key assigned to the specified volume.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Core Blockstorage Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-2146D59B-9535-4776-B83A-3EDF5F28876B)
- [CHANGE_BOOT_VOLUME_BACKUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-F28CC347-0C15-4D8C-B3E4-A9726FEF6E0C)
- [CHANGE_BOOT_VOLUME_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-6A52160D-DB49-4383-9126-F20F66359578)
- [CHANGE_VOLUME_BACKUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-C598A65E-6F36-49C7-B60F-726C61E68A66)
- [CHANGE_VOLUME_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-0AA334F7-4BC5-4A95-8E82-37C98593EA79)
- [CHANGE_VOLUME_GROUP_BACKUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-5D4E92B1-C70D-49F7-A312-BF5DA7F7FCE0)
- [CHANGE_VOLUME_GROUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-51382864-FE65-4E91-B2F0-5AF81F5A1A50)
- [COPY_BOOT_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-B7042E62-B6B9-48B0-A611-B3AF6D8B5AF7)
- [COPY_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-341B7601-B010-4E27-91C6-15A27C69028A)
- [COPY_VOLUME_GROUP_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-3BED53C2-22EA-4FCC-B0C1-9F20996A890B)
- [CREATE_BOOT_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-96888CE5-7029-4BC3-8B67-21AD29D558A6)
- [CREATE_BOOT_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-FD15C83E-5350-4BEC-9FAE-B510EAC9B5AB)
- [CREATE_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-69F032BC-4AC6-4FDC-A962-D1EC722207B7)
- [CREATE_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-BEB4E1BB-0D0A-4BA2-AB20-DC2E768BDB5F)
- [CREATE_VOLUME_BACKUP_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-B4179E62-9BA7-43A1-95CE-73386720538B)
- [CREATE_VOLUME_BACKUP_POLICY_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-993F2492-1DA3-4160-BE0E-282CD7279222)
- [CREATE_VOLUME_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-136905B2-8402-4723-84DD-F4CC08F0C003)
- [CREATE_VOLUME_GROUP_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-704C81EC-3033-445C-8FB2-F164493319A8)
- [DELETE_BOOT_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-033E03F1-EF96-4C53-BA4C-6EA5764BF2C2)
- [DELETE_BOOT_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-6AF08A03-3726-498F-9DD8-83DA53DC2843)
- [DELETE_BOOT_VOLUME_KMS_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-7C94548B-0E44-4103-B476-7FEAF55942FF)
- [DELETE_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-6CFD44F9-C25E-43A4-ABE1-E3231C0D059E)
- [DELETE_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-13EEDA03-4CA5-4AA2-ABC0-B9B784B3FF0B)
- [DELETE_VOLUME_BACKUP_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-7E3C56DF-F389-4793-9903-26FF24905C79)
- [DELETE_VOLUME_BACKUP_POLICY_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-BDFC0F1B-3A2C-40DC-B583-45E1F97FD896)
- [DELETE_VOLUME_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-9D546252-91CD-405A-A4DF-9D02FBBD4032)
- [DELETE_VOLUME_GROUP_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-22378050-EE95-4467-8BBC-FEF46452FE5D)
- [DELETE_VOLUME_KMS_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-FBD8D7C9-ED5A-4D38-B37A-680BB5C0E5FA)
- [GET_BLOCK_VOLUME_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-B6DE3711-8B8B-4AA8-968C-BD63BF796871)
- [GET_BOOT_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-606319F9-5507-4B55-B9E9-090F35BA0533)
- [GET_BOOT_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-36C36C2A-79CB-4F92-B379-327E7850D3C5)
- [GET_BOOT_VOLUME_KMS_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-4C43169B-C1DF-4D51-AB9E-04FD688863E6)
- [GET_BOOT_VOLUME_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-5654E195-8CAD-49E2-BFFF-FA3F53555E6C)
- [GET_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-D3AD485B-D2A6-44A0-8EF7-43C334A10021)
- [GET_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-6D044C9B-D888-409F-99B6-6A6F8AE16165)
- [GET_VOLUME_BACKUP_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-40EE2D18-3E97-4519-8675-2FB3841C6562)
- [GET_VOLUME_BACKUP_POLICY_ASSET_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-265C66B6-3DC1-406B-8954-6370FF1288DF)
- [GET_VOLUME_BACKUP_POLICY_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-C545EE8E-93B5-40EC-9807-3299BA54B344)
- [GET_VOLUME_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-486A3D9E-5D9F-4AD4-8B36-DC988E2D18F9)
- [GET_VOLUME_GROUP_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-527ECAB9-6A5E-4D1E-9D6A-71352D078D9C)
- [GET_VOLUME_GROUP_REPLICA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-02C1D470-3C0B-431D-B401-6730F6DCF9EA)
- [GET_VOLUME_KMS_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-2753D10D-5199-449F-89D8-B1F0B5E55434)
- [LIST_BLOCK_VOLUME_REPLICAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-A559B0BE-6A55-4F96-8B5B-E12D7F1F137A)
- [LIST_BOOT_VOLUME_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-0764513B-7EDA-473F-AB6B-1E3A4BF9A5B9)
- [LIST_BOOT_VOLUME_REPLICAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-538596CF-00BD-4AAE-A38F-EF9CCBA8ADEA)
- [LIST_BOOT_VOLUMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-6E33D96B-0C93-4BDD-973C-A495CA9DDA88)
- [LIST_VOLUME_BACKUP_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-16C1C301-0AC8-4DC5-9470-22C523607EAE)
- [LIST_VOLUME_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-5BACC5C8-3E7D-4D18-B439-458596F2CEF1)
- [LIST_VOLUME_GROUP_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-EB2C4DE5-350E-437B-B2FB-A74BC2473117)
- [LIST_VOLUME_GROUP_REPLICAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-B9FE8913-6BD7-4AD2-ADA4-CC02BD5A672F)
- [LIST_VOLUME_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-82FACC0C-FC1E-4AC3-94DC-72D5B944F021)
- [LIST_VOLUMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-42186A78-5186-4B73-9A81-6DFA2F541D47)
- [UPDATE_BOOT_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-D5CAC2F2-D3EB-459A-8695-D535E6938522)
- [UPDATE_BOOT_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-03DAC835-E930-4640-9821-1EE9D190CDE2)
- [UPDATE_BOOT_VOLUME_KMS_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-CBF7542E-7216-4008-A103-7D99A132AC93)
- [UPDATE_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-4A186C79-1140-4607-9FDD-6153BD3BC61F)
- [UPDATE_VOLUME_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-FD05F4B9-01E0-4FAF-899B-B82F86446746)
- [UPDATE_VOLUME_BACKUP_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-D1739F38-F4DC-4808-8A7A-098C81DB7933)
- [UPDATE_VOLUME_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-A034D705-9B7C-489F-9901-3E0F0B6C0346)
- [UPDATE_VOLUME_GROUP_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-BF1D4F7C-4916-4928-936A-D19C5A354B30)
- [UPDATE_VOLUME_KMS_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_blockstorage.html#ADSDK-GUID-4955C8CA-DFC8-4ACC-A58A-AB18750A3F82)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
