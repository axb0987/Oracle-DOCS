# File Storage Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#dcoc-content-body)

## File Storage Functions

Package: DBMS_CLOUD_OCI_FS_FILE_STORAGE

### CHANGE_FILE_SYSTEM_COMPARTMENT Function

Moves a file system and its associated snapshots into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes)

Syntax
```

```

Parameters

Parameter Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`change_file_system_compartment_details`

(required) Details for changing the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_FILESYSTEM_SNAPSHOT_POLICY_COMPARTMENT Function

Moves a file system snapshot policy into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`filesystem_snapshot_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`change_filesystem_snapshot_policy_compartment_details`

(required) Details for changing the compartment of a file system snapshot policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MOUNT_TARGET_COMPARTMENT Function

Moves a mount target and its associated export set or share set into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes)

Syntax
```

```

Parameters

Parameter Description

`mount_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target.

`change_mount_target_compartment_details`

(required) Details for changing the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_OUTBOUND_CONNECTOR_COMPARTMENT Function

Moves an outbound connector into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes)

Syntax
```

```

Parameters

Parameter Description

`outbound_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the outbound connector.

`change_outbound_connector_compartment_details`

(required) Details for changing the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REPLICATION_COMPARTMENT Function

Moves a replication and its replication target into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`replication_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`change_replication_compartment_details`

(required) Details for changing the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXPORT Function

Creates a new export in the specified export set, path, and file system.

Syntax
```

```

Parameters

Parameter Description

`create_export_details`

(required) Details for creating a new export.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FILE_SYSTEM Function

Creates a new file system in the specified compartment and availability domain. Instances can mount file systems in another availability domain, but doing so might increase latency when compared to mounting instances in the same availability domain. After you create a file system, you can associate it with a mount target. Instances can then mount the file system by connecting to the mount target's IP address. You can associate a file system with more than one mount target at a time. For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about Network Security Groups access control, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. All Oracle Cloud Infrastructure resources, including file systems, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type or by viewing the resource in the Console.

Syntax
```

```

Parameters

Parameter Description

`create_file_system_details`

(required) Details for creating a new file system.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FILESYSTEM_SNAPSHOT_POLICY Function

Creates a new file system snapshot policy in the specified compartment and availability domain. After you create a file system snapshot policy, you can associate it with file systems.

Syntax
```

```

Parameters

Parameter Description

`create_filesystem_snapshot_policy_details`

(required) Details for creating a new file system snapshot policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MOUNT_TARGET Function

Creates a new mount target in the specified compartment and subnet. You can associate a file system with a mount target only when they exist in the same availability domain. Instances can connect to mount targets in another availablity domain, but you might see higher latency than with instances in the same availability domain as the mount target. Mount targets have one or more private IP addresses that you can provide as the host portion of remote target parameters in client mount commands. These private IP addresses are listed in the privateIpIds property of the mount target and are highly available. Mount targets also consume additional IP addresses in their subnet. Do not use /30 or smaller subnets for mount target creation because they do not have sufficient available IP addresses. Allow at least three IP addresses for each mount target. For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. All Oracle Cloud Infrastructure Services resources, including mount targets, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

Syntax
```

```

Parameters

Parameter Description

`create_mount_target_details`

(required) Details for creating a new mount target.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OUTBOUND_CONNECTOR Function

Creates a new outbound connector in the specified compartment. You can associate an outbound connector with a mount target only when they exist in the same availability domain. For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. All Oracle Cloud Infrastructure Services resources, including outbound connectors, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

Syntax
```

```

Parameters

Parameter Description

`create_outbound_connector_details`

(required) Details for creating a new outbound connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REPLICATION Function

Creates a new replication in the specified compartment. Replications are the primary resource that governs the policy of cross-region replication between source and target file systems. Replications are associated with a secondary resource called a`REPLICATION_TARGET`Type located in another availability domain. The associated replication target resource is automatically created along with the replication resource. The replication retrieves the delta of data between two snapshots of a source file system and sends it to the associated `ReplicationTarget`, which retrieves the delta and applies it to the target file system. Only unexported file systems can be used as target file systems. For more information, see[Using Replication](https://docs.oracle.com/iaas/Content/File/Tasks/FSreplication.htm). For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. All Oracle Cloud Infrastructure Services resources, including replications, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.

Syntax
```

```

Parameters

Parameter Description

`create_replication_details`

(required) Details for creating a new replication.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SNAPSHOT Function

Creates a new snapshot of the specified file system. You can access the snapshot at `.snapshot/&lt;name&gt;`.

Syntax
```

```

Parameters

Parameter Description

`create_snapshot_details`

(required) Details for creating a new snapshot.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXPORT Function

Deletes the specified export.

Syntax
```

```

Parameters

Parameter Description

`export_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FILE_SYSTEM Function

Deletes the specified file system. Before you delete the file system, verify that no remaining export resources still reference it. Deleting a file system also deletes all of its snapshots.

Syntax
```

```

Parameters

Parameter Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FILESYSTEM_SNAPSHOT_POLICY Function

Deletes the specified file system snapshot policy.

Syntax
```

```

Parameters

Parameter Description

`filesystem_snapshot_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MOUNT_TARGET Function

Deletes the specified mount target. This operation also deletes the mount target's VNICs.

Syntax
```

```

Parameters

Parameter Description

`mount_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_OUTBOUND_CONNECTOR Function

Deletes the specified outbound connector.

Syntax
```

```

Parameters

Parameter Description

`outbound_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the outbound connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPLICATION Function

Deletes the specified replication and the the associated replication target.

Syntax
```

```

Parameters

Parameter Description

`replication_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`delete_mode`

(optional) You can choose a mode for deleting the replication resource. - `FINISH_CYCLE_IF_CAPTURING_OR_APPLYING` Before deleting, complete the current delta cycle. If cycle is idle, delete immediately. Safest option. - `ONE_MORE_CYCLE` Before deleting, complete the current delta cycle, and initiate one more cycle. If cycle is idle, initiate one more cycle. Use for lossless failover. - `FINISH_CYCLE_IF_APPLYING` Before deleting, finish applying. If cycle is idle or capturing, delete immediately. Fastest option.

Allowed values are: 'FINISH_CYCLE_IF_CAPTURING_OR_APPLYING', 'ONE_MORE_CYCLE', 'FINISH_CYCLE_IF_APPLYING'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPLICATION_TARGET Function

Deletes the specified replication target. This operation causes the immediate release of the target file system if there are currently no delta application operations. If there is any current delta being applied the delete operation is blocked until the current delta has been completely applied.

Syntax
```

```

Parameters

Parameter Description

`replication_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication target.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SNAPSHOT Function

Deletes the specified snapshot.

Syntax
```

```

Parameters

Parameter Description

`snapshot_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ESTIMATE_REPLICATION Function

Provides estimates for replication created using specific file system.

Syntax
```

```

Parameters

Parameter Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`change_rate_in_m_bps`

(optional) The rate of change of data on source file system in MegaBytes per second.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXPORT Function

Gets the specified export's information.

Syntax
```

```

Parameters

Parameter Description

`export_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXPORT_SET Function

Gets the specified export set's information.

Syntax
```

```

Parameters

Parameter Description

`export_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export set.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FILE_SYSTEM Function

Gets the specified file system's information.

Syntax
```

```

Parameters

Parameter Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FILESYSTEM_SNAPSHOT_POLICY Function

Gets the specified file system snapshot policy's information.

Syntax
```

```

Parameters

Parameter Description

`filesystem_snapshot_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MOUNT_TARGET Function

Gets the specified mount target's information.

Syntax
```

```

Parameters

Parameter Description

`mount_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_OUTBOUND_CONNECTOR Function

Gets the specified outbound connector's information.

Syntax
```

```

Parameters

Parameter Description

`outbound_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the outbound connector.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPLICATION Function

Gets the specified replication's information.

Syntax
```

```

Parameters

Parameter Description

`replication_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPLICATION_TARGET Function

Gets the specified replication target's information.

Syntax
```

```

Parameters

Parameter Description

`replication_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication target.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SNAPSHOT Function

Gets the specified snapshot's information.

Syntax
```

```

Parameters

Parameter Description

`snapshot_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXPORT_SETS Function

Lists the export set resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXPORTS Function

Lists export resources by compartment, file system, or export set. You must specify an export set ID, a file system ID, and / or a compartment ID.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`export_set_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export set.

`file_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by path, results are shown in ascending alphanumeric order.

Allowed values are: 'TIMECREATED', 'PATH'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FILE_SYSTEMS Function

Lists the file system resources in the specified compartment, or by the specified compartment and file system snapshot policy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`source_snapshot_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot used to create a cloned file system. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`parent_file_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system that contains the source snapshot of a cloned file system. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`filesystem_snapshot_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy that is associated with the file systems.

`sort_by`

(optional) The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FILESYSTEM_SNAPSHOT_POLICIES Function

Lists file system snapshot policies in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by displayName, results are shown in ascending alphanumeric order.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MOUNT_TARGETS Function

Lists the mount target resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`export_set_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export set.

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can choose either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_OUTBOUND_CONNECTORS Function

Lists the outbound connector resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can choose either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPLICATION_TARGETS Function

Lists the replication target resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can choose either value, but not both. By default, when you sort by `timeCreated`, results are shown in descending order. When you sort by `displayName`, results are shown in ascending order.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPLICATIONS Function

Lists the replication resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `500`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Example: `My resource`

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`sort_by`

(optional) The field to sort by. You can choose either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`file_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source file system.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SNAPSHOTS Function

Lists snapshots of the specified file system, or by file system snapshot policy and compartment, or by file system snapshot policy and file system. If file system ID is not specified, a file system snapshot policy ID and compartment ID must be specified. Users can only sort by time created when listing snapshots by file system snapshot policy ID and compartment ID (sort by name is NOT supported for listing snapshots by policy and compartment).

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 100 is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `100`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) Filter results by the specified lifecycle state. Must be a valid state for the resource type.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`id`

(optional) Filter results by[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.

`filesystem_snapshot_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy that is used to create the snapshots.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`file_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending. The default order is 'desc' except for numeric values.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PAUSE_FILESYSTEM_SNAPSHOT_POLICY Function

This operation pauses the scheduled snapshot creation and snapshot deletion of the policy and updates the lifecycle state of the file system snapshot policy from ACTIVE to INACTIVE. When a file system snapshot policy is paused, file systems that are associated with the policy will not have scheduled snapshots created or deleted. If the policy is already paused, or in the INACTIVE state, you cannot pause it again. You can't pause a policy that is in a DELETING, DELETED, FAILED, CREATING or INACTIVE state; attempts to pause a policy in these states result in a 409 conflict error.

Syntax
```

```

Parameters

Parameter Description

`filesystem_snapshot_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UNPAUSE_FILESYSTEM_SNAPSHOT_POLICY Function

This operation unpauses a paused file system snapshot policy and updates the lifecycle state of the file system snapshot policy from INACTIVE to ACTIVE. By default, file system snapshot policies are in the ACTIVE state. When a file system snapshot policy is not paused, or in the ACTIVE state, file systems that are associated with the policy will have snapshots created and deleted according to the schedules defined in the policy. If the policy is already in the ACTIVE state, you cannot unpause it. You can't unpause a policy that is in a DELETING, DELETED, FAILED, CREATING, or ACTIVE state; attempts to unpause a policy in these states result in a 409 conflict error.

Syntax
```

```

Parameters

Parameter Description

`filesystem_snapshot_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXPORT Function

Updates the specified export's information.

Syntax
```

```

Parameters

Parameter Description

`export_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export.

`update_export_details`

(required) Details object for updating an export.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXPORT_SET Function

Updates the specified export set's information.

Syntax
```

```

Parameters

Parameter Description

`export_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export set.

`update_export_set_details`

(required) Details object for updating an export set.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FILE_SYSTEM Function

Updates the specified file system's information. You can use this operation to rename a file system.

Syntax
```

```

Parameters

Parameter Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`update_file_system_details`

(required) Details object for updating a file system.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FILESYSTEM_SNAPSHOT_POLICY Function

Updates the specified file system snapshot policy's information.

Syntax
```

```

Parameters

Parameter Description

`filesystem_snapshot_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`update_filesystem_snapshot_policy_details`

(required) Details object for updating a file system snapshot policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MOUNT_TARGET Function

Updates the specified mount target's information.

Syntax
```

```

Parameters

Parameter Description

`mount_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target.

`update_mount_target_details`

(required) Details object for updating a mount target.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_OUTBOUND_CONNECTOR Function

Updates the specified outbound connector's information.

Syntax
```

```

Parameters

Parameter Description

`outbound_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the outbound connector.

`update_outbound_connector_details`

(required) Details object for updating a outbound connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REPLICATION Function

Updates the information for the specified replication and its associated replication target.

Syntax
```

```

Parameters

Parameter Description

`replication_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`update_replication_details`

(required) Details object for updating a replication.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SNAPSHOT Function

Updates the specified snapshot's information.

Syntax
```

```

Parameters

Parameter Description

`snapshot_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot.

`update_snapshot_details`

(required) Details object for updating a snapshot.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_KEY_TABS Function

Validates keytab contents for the secret details passed on the request or validte keytab contents associated with the mount target passed in the request. The keytabs are deserialized, the contents are validated for compatibility and the principal, key version number and encryption type of each entry is provided as part of the response.

Syntax
```

```

Parameters

Parameter Description

`validate_key_tabs_details`

(required) Keytab secret details or mount target ID for validating keytabs.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://filestorage.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [File Storage Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-2A2572E5-86D5-4268-97BB-4372E7DC9238)
- [CHANGE_FILE_SYSTEM_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-A8486553-A5F5-4C83-B740-F3B4E883A6C6)
- [CHANGE_FILESYSTEM_SNAPSHOT_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-B1CE101F-43FF-44F6-BADA-89800B1325F0)
- [CHANGE_MOUNT_TARGET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-D5A6ED03-52C2-44F7-B17C-0929CB2A6735)
- [CHANGE_OUTBOUND_CONNECTOR_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-3D451ED2-71B1-4D11-A292-9226852A5C4C)
- [CHANGE_REPLICATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-EF7F8DBE-4A88-4874-91B8-E2F9364A93EA)
- [CREATE_EXPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-C701E7C6-D964-4192-A89E-9B0E4E2AD412)
- [CREATE_FILE_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-37374AC6-79F0-4C5B-8ACA-61B0F4DA443B)
- [CREATE_FILESYSTEM_SNAPSHOT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-F5D9F6D9-237C-4CED-AA78-D0E84FC73FA6)
- [CREATE_MOUNT_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-85DF9826-7CF3-4664-940B-B5A3028F7CF8)
- [CREATE_OUTBOUND_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-56852E1A-278D-4A54-AD88-DB3FBC264A38)
- [CREATE_REPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-1CC0C2E5-BAF3-4C53-BA86-43AB26DF9A0E)
- [CREATE_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-629BAB7E-9A72-499A-AB87-BB6E51C662D7)
- [DELETE_EXPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-318F30F5-9772-4896-8D7F-8E5F7519402D)
- [DELETE_FILE_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-53F67190-EEC3-47AD-9D59-0BFF7196526A)
- [DELETE_FILESYSTEM_SNAPSHOT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-7079F42F-1195-4BB5-AAFB-D69CFEB2173B)
- [DELETE_MOUNT_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-B0893F54-CF57-4322-91E1-C3D3BC66E0E3)
- [DELETE_OUTBOUND_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-FC117143-873D-46F4-8F45-704D03AFCB08)
- [DELETE_REPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-6CD6AD5E-9098-4816-A36E-AEE9BE398AEC)
- [DELETE_REPLICATION_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-9B282F8A-3F83-4754-9CF3-748D863FF0DA)
- [DELETE_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-33D03FF5-0A48-420B-9160-48F6C5769D15)
- [ESTIMATE_REPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-28C1E0B5-0A05-4A2C-A80F-1112788EFBA5)
- [GET_EXPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-6903C2A3-A60F-4016-8764-8FDB0D56DB3D)
- [GET_EXPORT_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-18FB7427-AF41-4A6A-B593-43A2FC437FCE)
- [GET_FILE_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-6FB24B1B-BCD1-4C6B-B18F-1D248D008651)
- [GET_FILESYSTEM_SNAPSHOT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-172AA65F-9C9D-499D-97EA-2666DF83594C)
- [GET_MOUNT_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-36BE7C0D-2FD5-4433-A906-7A4570E2B2B9)
- [GET_OUTBOUND_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-34873260-AF56-4B96-8E44-3A34DA2B0825)
- [GET_REPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-D1DDA2FA-8C0A-4348-9181-BFA25178700D)
- [GET_REPLICATION_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-269C3FC3-5A4B-412F-A4CD-445A11923120)
- [GET_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-BDDA22A0-C48D-4465-A66F-F59E0B53A4F1)
- [LIST_EXPORT_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-915A4B5E-9230-48D3-A52E-516323C84B54)
- [LIST_EXPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-523F9D62-55BE-4017-81A6-C45A022F87C8)
- [LIST_FILE_SYSTEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-07AC21EA-771E-461F-8592-C431B26A8D99)
- [LIST_FILESYSTEM_SNAPSHOT_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-70B62128-5803-4E40-992A-7881D3D91A85)
- [LIST_MOUNT_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-1F480989-3939-46B4-96D5-77AC34793D35)
- [LIST_OUTBOUND_CONNECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-371BB018-3EB2-4E6D-A9BF-56BBAD17D894)
- [LIST_REPLICATION_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-84D5E20C-880D-49DB-8027-B94229E92537)
- [LIST_REPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-29C77A48-C920-4B74-87CE-0246BC6D5DFE)
- [LIST_SNAPSHOTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-83230929-F652-41F3-942A-4247884C2ADB)
- [PAUSE_FILESYSTEM_SNAPSHOT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-F01488FD-E6DA-4255-8642-C8A5401AA512)
- [UNPAUSE_FILESYSTEM_SNAPSHOT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-F3EF89F1-80F0-484C-ACE8-3A5BC04E46F6)
- [UPDATE_EXPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-236E0A6A-82A3-4CEB-8D9F-44533207EBBB)
- [UPDATE_EXPORT_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-794F8759-315A-4DB4-A31A-0C5145E97A9C)
- [UPDATE_FILE_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-B98C25D7-6069-43C7-A7A2-191FA61DEEB3)
- [UPDATE_FILESYSTEM_SNAPSHOT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-32011875-8D53-4A3D-93A1-62F48F625891)
- [UPDATE_MOUNT_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-E78CBCF7-9777-4059-B938-CCB4972096F4)
- [UPDATE_OUTBOUND_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-52892123-17DF-4847-A026-4F5AFBFA5626)
- [UPDATE_REPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-C44E1983-C8AE-4796-87DD-CDB0EBCB0A00)
- [UPDATE_SNAPSHOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-AF705601-154A-4487-B876-8ADD067C2E81)
- [VALIDATE_KEY_TABS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fs_file_storage.html#ADSDK-GUID-C9FED3F7-15E1-4BB2-AE91-613348B8CD9D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
