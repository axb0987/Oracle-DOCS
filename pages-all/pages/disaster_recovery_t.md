# Disaster Recovery Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#dcoc-content-body)

## Disaster Recovery Common Types

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_ASSOCIATE_DR_PROTECTION_GROUP_DETAILS_T Type

The details for associating a DR protection group with a peer DR protection group.

Syntax
```

```

Fields

Field Description

`peer_id`

(optional) The OCID of the peer DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(optional) The region of the peer DR protection group. Example: `us-ashburn-1`

`role`

(required) The role of the DR protection group. Example: `STANDBY`

Allowed values are: 'PRIMARY', 'STANDBY', 'UNCONFIGURED'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_BLOCK_VOLUME_ATTACHMENT_DETAILS_T Type

The details for attaching or detaching a block volume.

Syntax
```

```

Fields

Field Description

`volume_attachment_reference_instance_id`

(required) The OCID of the reference compute instance from which to obtain the attachment details for the volume. This reference compute instance is from the peer DR protection group. Example: `ocid1.instance.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_BLOCK_VOLUME_MOUNT_DETAILS_T Type

The details for mounting or unmounting the file system on a block volume.

Syntax
```

```

Fields

Field Description

`mount_point`

(required) The physical mount point used for mounting and unmounting the file system on a block volume. Example: `/mnt/yourmountpoint`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_CONTROL_DETAILS_T Type

The details for controlling plan execution.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The type of control action.

Allowed values are: 'CANCEL', 'PAUSE', 'RESUME'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CANCEL_DR_PLAN_EXECUTION_DETAILS_T Type

The details for cancelling a DR plan execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_cancel_dr_plan_execution_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_control_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CHANGE_DR_PROTECTION_GROUP_COMPARTMENT_DETAILS_T Type

The details for moving a DR protection group to another compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to which the DR protection group should be moved. Example: `ocid1.compartment.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_MOUNT_DETAILS_T Type

Mount details of a file system.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(required) The OCID of the mount target for this file system. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_UNMOUNT_DETAILS_T Type

Unmount details for a file system.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(required) The OCID of the mount target for this file system. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_T Type

The details of operations performed on a file system.

Syntax
```

```

Fields

Field Description

`export_path`

(required) The export path of the file system. Example: `/fs-export-path`

`mount_point`

(required) The physical mount point of the file system on a host. Example: `/mnt/yourmountpoint`

`mount_details`

(required)

`unmount_details`

(required)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_T Type

Source VNIC to destination subnet mapping for a movable compute instance.

Syntax
```

```

Fields

Field Description

`source_vnic_id`

(required) The OCID of the source VNIC. Example: `ocid1.vnic.oc1..uniqueID`

`destination_subnet_id`

(required) The OCID of the destination subnet to which the source VNIC should connect. Example: `ocid1.subnet.oc1..uniqueID`

`destination_primary_private_ip_address`

(optional) The private IP address to be assigned as the VNIC's primary IP address in the destination subnet. This must be a valid IP address in the destination subnet and the IP address must be available. Example: `10.0.3.3`

`destination_primary_private_ip_hostname_label`

(optional) The hostname label to be assigned in the destination subnet for the primary private IP of the source VNIC. This label is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, 'myhost1' in the FQDN 'myhost1.subnet123.vcn1.oraclevcn.com'). Example: `myhost1`

`destination_nsg_id_list`

(optional) A list of OCIDs of network security groups (NSG) in the destination region which should be assigned to the source VNIC. Example: `[ ocid1.networksecuritygroup.oc1..uniqueID, ocid1.networksecuritygroup.oc1..uniqueID ]`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_DETAILS_T Type

Source VNIC to destination subnet mapping for a movable compute instance.

Syntax
```

```

Fields

Field Description

`source_vnic_id`

(required) The OCID of the source VNIC. Example: `ocid1.vnic.oc1..uniqueID`

`destination_subnet_id`

(required) The OCID of the destination subnet to which the source VNIC should connect. Example: `ocid1.subnet.oc1..uniqueID`

`destination_primary_private_ip_address`

(optional) The primary private IP address to be assigned to the source VNIC in the destination subnet. This IP address must belong to the destination subnet. Example: `10.0.3.3`

`destination_primary_private_ip_hostname_label`

(optional) The hostname label to be assigned in the destination subnet for the primary private IP of the source VNIC. This label is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, 'myhost1' in the FQDN 'myhost1.subnet123.vcn1.oraclevcn.com'). Example: `myhost1`

`destination_nsg_id_list`

(optional) A list of OCIDs of network security groups (NSG) in the destination region which should be assigned to the source VNIC. Example: `[ ocid1.networksecuritygroup.oc1..uniqueID, ocid1.networksecuritygroup.oc1..uniqueID ]`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_T Type

The details of operations performed on a block volume.

Syntax
```

```

Fields

Field Description

`block_volume_id`

(required) The OCID of the block volume. Example: `ocid1.volume.oc1..uniqueID`

`attachment_details`

(optional)

`mount_details`

(optional)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_T Type

The details of operations performed on a file system.

Syntax
```

```

Fields

Field Description

`export_path`

(required) The export path of the file system. Example: `/fs-export-path`

`mount_point`

(required) The physical mount point of the file system on a host. Example: `/mnt/yourmountpoint`

`mount_target_id`

(required) The OCID of mount target. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_T Type

Deprecated. Source VNIC to destination subnet mapping for a compute instance.

Syntax
```

```

Fields

Field Description

`source_vnic_id`

(required) The OCID of the VNIC. Example: `ocid1.vnic.oc1..uniqueID`

`destination_subnet_id`

(required) The OCID of the destination subnet to which the source VNIC should connect. Example: `ocid1.subnet.oc1..uniqueID`

`destination_nsg_id_list`

(optional) A list of OCIDs of network security groups (NSG) in the destination region which should be assigned to the source VNIC. Example: `[ ocid1.networksecuritygroup.oc1..uniqueID1, ocid1.networksecuritygroup.oc1..uniqueID2 ]`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_DETAILS_T Type

Deprecated. Source VNIC to destination subnet mapping for a compute instance.

Syntax
```

```

Fields

Field Description

`source_vnic_id`

(required) The OCID of the VNIC. Example: `ocid1.vnic.oc1..uniqueID`

`destination_subnet_id`

(required) The OCID of the destination subnet to which this source VNIC should connect. Example: `ocid1.subnet.oc1..uniqueID`

`destination_primary_private_ip_address`

(optional) The primary private IP address to be assigned to the VNIC in the destination region. This address must belong to the destination subnet. Example: `10.0.3.3`

`destination_primary_private_ip_hostname_label`

(optional) The hostname label to be assigned in the destination subnet for the primary private IP of the source VNIC. This label is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, 'myhost1' in the FQDN 'myhost1.subnet123.vcn1.oraclevcn.com'). Example: `myhost1`

`destination_nsg_id_list`

(optional) A list of OCIDs of network security groups (NSG) in the destination region which should be assigned to the source VNIC. Example: `[ ocid1.networksecuritygroup.oc1..uniqueID, ocid1.networksecuritygroup.oc1..uniqueID ]`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_BLOCK_VOLUME_ATTACHMENT_DETAILS_T Type

The details for creating a block volume attachment.

Syntax
```

```

Fields

Field Description

`volume_attachment_reference_instance_id`

(optional) The OCID of the reference compute instance from which to obtain the attachment details for the volume. This reference compute instance is from the peer DR protection group. Example: `ocid1.instance.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_BLOCK_VOLUME_MOUNT_DETAILS_T Type

The details for creating a mount for a file system on a block volume.

Syntax
```

```

Fields

Field Description

`mount_point`

(optional) The physical mount point used for mounting the file system on the block volume. Example: `/mnt/yourmountpoint`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_FILE_SYSTEM_MOUNT_DETAILS_T Type

The details for creating a file system mount.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(optional) The OCID of the mount target for this file system. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_FILE_SYSTEM_UNMOUNT_DETAILS_T Type

The details for creating a file system unmount.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(optional) The OCID of the mount target. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type

The details for creating the operations performed on a file system for movable compute instance.

Syntax
```

```

Fields

Field Description

`export_path`

(required) The export path of the file system. Example: `/fs-export-path`

`mount_point`

(required) The physical mount point of the file system on a host. Example: `/mnt/yourmountpoint`

`mount_details`

(required)

`unmount_details`

(required)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_T Type

The details for creating the operations performed on a block volume.

Syntax
```

```

Fields

Field Description

`block_volume_id`

(required) The OCID of the block volume. Example: `ocid1.volume.oc1..uniqueID`

`attachment_details`

(optional)

`mount_details`

(optional)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type

The details for creating the operations performed on a file system for non-movable compute instance.

Syntax
```

```

Fields

Field Description

`export_path`

(required) The export path of the file system. Example: `/fs-export-path`

`mount_point`

(required) The physical mount point of the file system on a host. Example: `/mnt/yourmountpoint`

`mount_target_id`

(required) The OCID of the mount target. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PLAN_DETAILS_T Type

The details for creating a DR plan.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The display name of the DR plan being created. Example: `EBS Switchover PHX to IAD`

`l_type`

(required) The type of DR plan to be created.

Allowed values are: 'SWITCHOVER', 'FAILOVER', 'START_DRILL', 'STOP_DRILL'

`dr_protection_group_id`

(required) The OCID of the DR protection group to which this DR plan belongs. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_OPTION_DETAILS_T Type

The options for a plan execution.

Syntax
```

```

Fields

Field Description

`plan_execution_type`

(required) The type of the plan execution.

Allowed values are: 'SWITCHOVER', 'SWITCHOVER_PRECHECK', 'FAILOVER', 'FAILOVER_PRECHECK', 'START_DRILL', 'START_DRILL_PRECHECK', 'STOP_DRILL', 'STOP_DRILL_PRECHECK'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PLAN_EXECUTION_DETAILS_T Type

The details for creating a DR plan execution.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the DR plan execution. Example: `Execution - EBS Switchover PHX to IAD`

`plan_id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`execution_options`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_OBJECT_STORAGE_LOG_LOCATION_DETAILS_T Type

The details for creating an object storage log location for a DR protection group.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The namespace in object storage (Note - this is usually the tenancy name). Example: `myocitenancy`

`bucket`

(required) The bucket name inside the object storage namespace. Example: `operation_logs`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_T Type

Create properties for a member in a DR protection group.

Syntax
```

```

Fields

Field Description

`member_id`

(required) The OCID of the member. Example: `ocid1.instance.oc1..uniqueID`

`member_type`

(required) The type of the member.

Allowed values are: 'COMPUTE_INSTANCE', 'COMPUTE_INSTANCE_MOVABLE', 'COMPUTE_INSTANCE_NON_MOVABLE', 'VOLUME_GROUP', 'DATABASE', 'AUTONOMOUS_DATABASE', 'LOAD_BALANCER', 'NETWORK_LOAD_BALANCER', 'FILE_SYSTEM'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_DETAILS_T Type

The details for creating a DR protection group.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment in which to create the DR protection group. Example: `ocid1.compartment.oc1..uniqueID`

`display_name`

(required) The display name of the DR protection group. Example: `EBS PHX Group`

`log_location`

(required)

`association`

(optional)

`members`

(optional) A list of DR protection group members.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_AUTONOMOUS_DATABASE_DETAILS_T Type

Create properties for an Autonomous Database Serverless member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_autonomous_database_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_vnic_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_DETAILS_T Type

Deprecated. Create properties for a compute instance member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_compute_instance_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`is_movable`

(optional) A flag indicating if the compute instance should be moved during DR operations. Example: `false`

`vnic_mapping`

(optional) A list of compute instance VNIC mappings.

`destination_compartment_id`

(optional) The OCID of a compartment in the destination region in which the compute instance should be launched. Example: `ocid1.compartment.oc1..uniqueID`

`destination_dedicated_vm_host_id`

(optional) The OCID of a dedicated VM host in the destination region where the compute instance should be launched. Example: `ocid1.dedicatedvmhost.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_movable_vnic_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_create_compute_instance_movable_file_system_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_MOVABLE_DETAILS_T Type

Create properties for a movable compute instance member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_compute_instance_movable_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`is_retain_fault_domain`

(optional) A flag indicating if the compute instance should be moved to the same fault domain in the destination region. The compute instance launch will fail if this flag is set to true and capacity is not available in the specified fault domain in the destination region. Example: `false`

`destination_capacity_reservation_id`

(optional) The OCID of a capacity reservation in the destination region which will be used to launch the compute instance. Example: `ocid1.capacityreservation.oc1..uniqueID`

`vnic_mappings`

(optional) A list of compute instance VNIC mappings.

`destination_compartment_id`

(optional) The OCID of a compartment in the destination region in which the compute instance should be launched. Example: `ocid1.compartment.oc1..uniqueID`

`destination_dedicated_vm_host_id`

(optional) The OCID of a dedicated VM host in the destination region where the compute instance should be launched. Example: `ocid1.dedicatedvmhost.oc1..uniqueID`

`file_system_operations`

(optional) A list of operations performed on file systems used by the compute instance.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_create_compute_instance_non_movable_file_system_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_create_compute_instance_non_movable_block_volume_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_NON_MOVABLE_DETAILS_T Type

Create properties for a non-movable compute instance member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_compute_instance_non_movable_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`is_start_stop_enabled`

(optional) A flag indicating whether the non-movable compute instance should be started and stopped during DR operations. *Prechecks cannot be executed on stopped instances that are configured to be started.*

`file_system_operations`

(optional) A list of operations performed on file systems used by the compute instance.

`block_volume_operations`

(optional) A list of operations performed on block volumes used by the compute instance.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_DATABASE_DETAILS_T Type

Create properties for a Database (DBCS) member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_database_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`password_vault_secret_id`

(optional) The OCID of the vault secret where the database SYSDBA password is stored. Example: `ocid1.vaultsecret.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_DETAILS_T Type

The mapping between a file system export in the primary region and a mount target in the standby region.

Syntax
```

```

Fields

Field Description

`export_id`

(required) The OCID of the export path in the primary region used to mount or unmount the file system. Example: `ocid1.export.oc1..uniqueID`

`destination_mount_target_id`

(required) The OCID of the destination mount target in the destination region which is used to export the file system. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_file_system_export_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_FILE_SYSTEM_DETAILS_T Type

Create properties for a file system member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_file_system_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`destination_availability_domain`

(optional) The availability domain of the destination mount target. Example: `BBTh:region-AD`

`export_mappings`

(optional) A list of mappings between file system exports in the primary region and mount targets in the standby region.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_T Type

Create backend set mapping properties for a load balancer member.

Syntax
```

```

Fields

Field Description

`is_backend_set_for_non_movable`

(required) This flag specifies if this backend set is used for traffic for non-movable compute instances. Backend sets that point to non-movable instances are only enabled or disabled during DR, their contents are not altered. For non-movable instances this flag should be set to 'true'. Backend sets that point to movable instances are emptied and their contents are transferred to the destination region load balancer. For movable instances this flag should be set to 'false'. Example: `true`

`source_backend_set_name`

(required) The name of the source backend set. Example: `Source-BackendSet-1`

`destination_backend_set_name`

(required) The name of the destination backend set. Example: `Destination-BackendSet-1`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_load_balancer_backend_set_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_LOAD_BALANCER_DETAILS_T Type

Create properties for a load balancer member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_load_balancer_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`destination_load_balancer_id`

(optional) The OCID of the destination load balancer. Example: `ocid1.loadbalancer.oc1..uniqueID`

`backend_set_mappings`

(optional) A list of backend set mappings that are used to transfer or update backends during DR.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_T Type

Create backend set mapping properties for a network load balancer member.

Syntax
```

```

Fields

Field Description

`is_backend_set_for_non_movable`

(required) This flag specifies if this backend set is used for traffic for non-movable compute instances. Backend sets that point to non-movable instances are only enabled or disabled during DR, their contents are not altered. For non-movable instances this flag should be set to 'true'. Backend sets that point to movable instances are emptied and their contents are transferred to the destination region load balancer. For movable instances this flag should be set to 'false'. Example: `true`

`source_backend_set_name`

(required) The name of the source backend set. Example: `Source-BackendSet-1`

`destination_backend_set_name`

(required) The name of the destination backend set. Example: `Destination-BackendSet-1`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_network_load_balancer_backend_set_mapping_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_NETWORK_LOAD_BALANCER_DETAILS_T Type

Create properties for a network load balancer member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_network_load_balancer_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

Fields

Field Description

`destination_network_load_balancer_id`

(optional) The OCID of the destination network load balancer. Example: `ocid1.networkloadbalancer.oc1..uniqueID`

`backend_set_mappings`

(optional) A list of backend set mappings that are used to transfer or update backends during DR.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_VOLUME_GROUP_DETAILS_T Type

Create properties for a volume group member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_volume_group_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_create_dr_protection_group_member_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DISASSOCIATE_DR_PROTECTION_GROUP_DETAILS_T Type

The details for disassociating this DR protection group from a peer DR protection group.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The default type.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DISASSOCIATE_DR_PROTECTION_GROUP_DEFAULT_DETAILS_T Type

The default type.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_disassociate_dr_protection_group_default_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_disassociate_dr_protection_group_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_USER_DEFINED_STEP_T Type

The details for a user-defined step in a DR plan.

Syntax
```

```

Fields

Field Description

`step_type`

(required) The type of the user-defined step. **RUN_OBJECTSTORE_SCRIPT_PRECHECK** - A step which performs a precheck on a script stored in OCI object storage. **RUN_LOCAL_SCRIPT_PRECHECK** - A step which performs a precheck on a script which resides locally on a compute instance. **INVOKE_FUNCTION_PRECHECK** - A step which performs a precheck on an OCI function. See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm. **RUN_OBJECTSTORE_SCRIPT** - A step which runs a script stored in OCI object storage. **RUN_LOCAL_SCRIPT** - A step which runs a script that resides locally on a compute instance. **INVOKE_FUNCTION** - A step which invokes an OCI function. See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

Allowed values are: 'RUN_OBJECTSTORE_SCRIPT_PRECHECK', 'RUN_LOCAL_SCRIPT_PRECHECK', 'INVOKE_FUNCTION_PRECHECK', 'RUN_OBJECTSTORE_SCRIPT', 'RUN_LOCAL_SCRIPT', 'INVOKE_FUNCTION'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_T Type

Details of a step in a DR plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique id of the step. Must not be modified by the user. Example: `sgid1.step..uniqueID`

`group_id`

(required) The unique id of the group to which this step belongs. Must not be modified by user. Example: `sgid1.group..uniqueID`

`member_id`

(optional) The OCID of the member associated with this step. Example: `ocid1.database.oc1..uniqueID`

`l_type`

(required) The plan step type.

Allowed values are: 'COMPUTE_INSTANCE_STOP_PRECHECK', 'COMPUTE_INSTANCE_LAUNCH_PRECHECK', 'COMPUTE_INSTANCE_TERMINATE_PRECHECK', 'COMPUTE_INSTANCE_REMOVE_PRECHECK', 'VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK', 'VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK', 'DATABASE_SWITCHOVER_PRECHECK', 'DATABASE_FAILOVER_PRECHECK', 'AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK', 'AUTONOMOUS_DATABASE_FAILOVER_PRECHECK', 'USER_DEFINED_PRECHECK', 'COMPUTE_INSTANCE_LAUNCH', 'COMPUTE_INSTANCE_STOP', 'COMPUTE_INSTANCE_TERMINATE', 'COMPUTE_INSTANCE_REMOVE', 'DATABASE_SWITCHOVER', 'DATABASE_FAILOVER', 'AUTONOMOUS_DATABASE_SWITCHOVER', 'AUTONOMOUS_DATABASE_FAILOVER', 'VOLUME_GROUP_RESTORE_SWITCHOVER', 'VOLUME_GROUP_RESTORE_FAILOVER', 'VOLUME_GROUP_REVERSE', 'VOLUME_GROUP_DELETE', 'VOLUME_GROUP_REMOVE', 'VOLUME_GROUP_TERMINATE', 'USER_DEFINED', 'VOLUME_GROUP_RESTORE_START_DRILL_PRECHECK', 'VOLUME_GROUP_REMOVE_PRECHECK', 'VOLUME_GROUP_TERMINATE_PRECHECK', 'VOLUME_GROUP_RESTORE_START_DRILL', 'AUTONOMOUS_DATABASE_CREATE_CLONE_PRECHECK', 'AUTONOMOUS_DATABASE_DELETE_CLONE_PRECHECK', 'LOAD_BALANCER_UPDATE_PRIMARY_BACKEND_SET_PRECHECK', 'LOAD_BALANCER_UPDATE_STANDBY_BACKEND_SET_PRECHECK', 'FILE_SYSTEM_SWITCHOVER_PRECHECK', 'FILE_SYSTEM_FAILOVER_PRECHECK', 'FILE_SYSTEM_START_DRILL_PRECHECK', 'FILE_SYSTEM_STOP_DRILL_PRECHECK', 'FILE_SYSTEM_REMOVE_PRECHECK', 'FILE_SYSTEM_TERMINATE_PRECHECK', 'FILE_SYSTEM_MOUNT_PRECHECK', 'FILE_SYSTEM_UNMOUNT_PRECHECK', 'COMPUTE_INSTANCE_START_PRECHECK', 'COMPUTE_INSTANCE_ATTACH_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_INSTANCE_DETACH_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_INSTANCE_MOUNT_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_INSTANCE_UNMOUNT_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_CAPACITY_RESERVATION_START_DRILL_PRECHECK', 'COMPUTE_CAPACITY_AVAILABILITY_START_DRILL_PRECHECK', 'AUTONOMOUS_DATABASE_CREATE_CLONE', 'AUTONOMOUS_DATABASE_DELETE_CLONE', 'LOAD_BALANCER_UPDATE_PRIMARY_BACKEND_SET', 'LOAD_BALANCER_UPDATE_STANDBY_BACKEND_SET', 'FILE_SYSTEM_SWITCHOVER', 'FILE_SYSTEM_FAILOVER', 'FILE_SYSTEM_REMOVE', 'FILE_SYSTEM_REVERSE', 'FILE_SYSTEM_TERMINATE', 'FILE_SYSTEM_START_DRILL', 'FILE_SYSTEM_STOP_DRILL', 'COMPUTE_INSTANCE_START', 'COMPUTE_INSTANCE_ATTACH_BLOCK_VOLUMES', 'COMPUTE_INSTANCE_DETACH_BLOCK_VOLUMES', 'FILE_SYSTEM_MOUNT', 'FILE_SYSTEM_UNMOUNT', 'COMPUTE_CAPACITY_RESERVATION_SWITCHOVER_PRECHECK', 'COMPUTE_CAPACITY_RESERVATION_FAILOVER_PRECHECK', 'COMPUTE_CAPACITY_AVAILABILITY_SWITCHOVER_PRECHECK', 'COMPUTE_CAPACITY_AVAILABILITY_FAILOVER_PRECHECK'

`display_name`

(required) The display name of the group. Example: `DATABASE_SWITCHOVER`

`error_mode`

(required) The error mode for this step.

Allowed values are: 'STOP_ON_ERROR', 'CONTINUE_ON_ERROR'

`timeout`

(required) The timeout in seconds for executing this step. Example: `600`

`is_enabled`

(required) A flag indicating whether this step should be enabled for execution. Example: `true`

`user_defined_step`

(optional)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_plan_step_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_T Type

Details of a group in a DR plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique id of the group. Must not be modified by user. Example: `sgid1.group..uniqueID`

`l_type`

(required) The group type. Example: `BUILT_IN`

Allowed values are: 'USER_DEFINED', 'BUILT_IN', 'BUILT_IN_PRECHECK'

`display_name`

(required) The display name of the group. Example: `DATABASE_SWITCHOVER`

`steps`

(required) The list of steps in the group.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_plan_group_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_T Type

The details of a DR plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`display_name`

(required) The display name of the DR plan. Example: `EBS Switchover PHX to IAD`

`compartment_id`

(required) The OCID of the compartment containing the DR plan. Example: `ocid1.compartment.oc1..uniqueID`

`l_type`

(required) The type of the DR plan.

Allowed values are: 'SWITCHOVER', 'FAILOVER', 'START_DRILL', 'STOP_DRILL'

`time_created`

(required) The date and time the DR plan was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_updated`

(required) The date and time the DR plan was updated. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`dr_protection_group_id`

(required) The OCID of the DR protection group to which this DR plan belongs. Example: `ocid1.drplan.oc1..uniqueID`

`peer_dr_protection_group_id`

(required) The OCID of the peer DR protection group associated with this plan's DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(required) The region of the peer DR protection group associated with this plan's DR protection group. Example: `us-ashburn-1`

`plan_groups`

(required) The list of groups in this DR plan.

`lifecycle_state`

(required) The current state of the DR plan.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`life_cycle_details`

(optional) A message describing the DR plan's current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_SUMMARY_T Type

The summary of a DR plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment containing the DR plan. Example: `ocid1.compartment.oc1..uniqueID`

`display_name`

(required) The display name of the DR plan. Example: `EBS Switchover PHX to IAD`

`l_type`

(required) The type of the DR plan. Example: `SWITCHOVER`

Allowed values are: 'SWITCHOVER', 'FAILOVER', 'START_DRILL', 'STOP_DRILL'

`dr_protection_group_id`

(required) The OCID of the DR protection group to which this DR plan belongs. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_dr_protection_group_id`

(required) The OCID of the peer DR protection group associated with this plan's DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(required) The region of the peer DR protection group associated with this plan's DR protection group. Example: `us-ashburn-1`

`time_created`

(required) The date and time the DR plan was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_updated`

(required) The date and time the DR plan was updated. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`lifecycle_state`

(required) The current state of the DR plan. Example: `ACTIVE`

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`life_cycle_details`

(optional) A message describing the DR plan's current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_plan_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_COLLECTION_T Type

A list of DR plan summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of DR plan summaries.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_OPTIONS_T Type

The options for a plan execution.

Syntax
```

```

Fields

Field Description

`plan_execution_type`

(required) The type of the plan execution.

Allowed values are: 'SWITCHOVER', 'SWITCHOVER_PRECHECK', 'FAILOVER', 'FAILOVER_PRECHECK', 'START_DRILL_PRECHECK', 'START_DRILL', 'STOP_DRILL_PRECHECK', 'STOP_DRILL'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_OBJECT_STORAGE_LOG_LOCATION_T Type

The details of an object storage log location for a DR protection group.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The namespace in object storage (Note - this is usually the tenancy name). Example: `myocitenancy`

`bucket`

(required) The bucket name inside the object storage namespace. Example: `operation_logs`

`object`

(optional) The object name inside the object storage bucket. Example: `switchover_plan_executions`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_EXECUTION_T Type

The details of a step execution in a DR plan execution.

Syntax
```

```

Fields

Field Description

`step_id`

(required) The unique id of the step. Must not be modified by user. Example: `sgid1.step..uniqueID`

`l_type`

(required) The step type.

Allowed values are: 'COMPUTE_INSTANCE_STOP_PRECHECK', 'COMPUTE_INSTANCE_LAUNCH_PRECHECK', 'COMPUTE_INSTANCE_TERMINATE_PRECHECK', 'COMPUTE_INSTANCE_REMOVE_PRECHECK', 'VOLUME_GROUP_RESTORE_SWITCHOVER_PRECHECK', 'VOLUME_GROUP_RESTORE_FAILOVER_PRECHECK', 'DATABASE_SWITCHOVER_PRECHECK', 'DATABASE_FAILOVER_PRECHECK', 'AUTONOMOUS_DATABASE_SWITCHOVER_PRECHECK', 'AUTONOMOUS_DATABASE_FAILOVER_PRECHECK', 'USER_DEFINED_PRECHECK', 'COMPUTE_INSTANCE_LAUNCH', 'COMPUTE_INSTANCE_STOP', 'COMPUTE_INSTANCE_TERMINATE', 'COMPUTE_INSTANCE_REMOVE', 'DATABASE_SWITCHOVER', 'DATABASE_FAILOVER', 'AUTONOMOUS_DATABASE_SWITCHOVER', 'AUTONOMOUS_DATABASE_FAILOVER', 'VOLUME_GROUP_RESTORE_SWITCHOVER', 'VOLUME_GROUP_RESTORE_FAILOVER', 'VOLUME_GROUP_REVERSE', 'VOLUME_GROUP_DELETE', 'VOLUME_GROUP_REMOVE', 'VOLUME_GROUP_TERMINATE', 'USER_DEFINED', 'VOLUME_GROUP_RESTORE_START_DRILL_PRECHECK', 'VOLUME_GROUP_REMOVE_PRECHECK', 'VOLUME_GROUP_TERMINATE_PRECHECK', 'VOLUME_GROUP_RESTORE_START_DRILL', 'AUTONOMOUS_DATABASE_CREATE_CLONE_PRECHECK', 'AUTONOMOUS_DATABASE_DELETE_CLONE_PRECHECK', 'LOAD_BALANCER_UPDATE_PRIMARY_BACKEND_SET_PRECHECK', 'LOAD_BALANCER_UPDATE_STANDBY_BACKEND_SET_PRECHECK', 'FILE_SYSTEM_SWITCHOVER_PRECHECK', 'FILE_SYSTEM_FAILOVER_PRECHECK', 'FILE_SYSTEM_START_DRILL_PRECHECK', 'FILE_SYSTEM_STOP_DRILL_PRECHECK', 'FILE_SYSTEM_REMOVE_PRECHECK', 'FILE_SYSTEM_TERMINATE_PRECHECK', 'FILE_SYSTEM_MOUNT_PRECHECK', 'FILE_SYSTEM_UNMOUNT_PRECHECK', 'COMPUTE_INSTANCE_START_PRECHECK', 'COMPUTE_INSTANCE_ATTACH_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_INSTANCE_DETACH_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_INSTANCE_MOUNT_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_INSTANCE_UNMOUNT_BLOCK_VOLUMES_PRECHECK', 'COMPUTE_CAPACITY_RESERVATION_START_DRILL_PRECHECK', 'COMPUTE_CAPACITY_AVAILABILITY_START_DRILL_PRECHECK', 'AUTONOMOUS_DATABASE_CREATE_CLONE', 'AUTONOMOUS_DATABASE_DELETE_CLONE', 'LOAD_BALANCER_UPDATE_PRIMARY_BACKEND_SET', 'LOAD_BALANCER_UPDATE_STANDBY_BACKEND_SET', 'FILE_SYSTEM_SWITCHOVER', 'FILE_SYSTEM_FAILOVER', 'FILE_SYSTEM_REMOVE', 'FILE_SYSTEM_REVERSE', 'FILE_SYSTEM_TERMINATE', 'FILE_SYSTEM_START_DRILL', 'FILE_SYSTEM_STOP_DRILL', 'COMPUTE_INSTANCE_START', 'COMPUTE_INSTANCE_ATTACH_BLOCK_VOLUMES', 'COMPUTE_INSTANCE_DETACH_BLOCK_VOLUMES', 'FILE_SYSTEM_MOUNT', 'FILE_SYSTEM_UNMOUNT', 'COMPUTE_CAPACITY_RESERVATION_SWITCHOVER_PRECHECK', 'COMPUTE_CAPACITY_RESERVATION_FAILOVER_PRECHECK', 'COMPUTE_CAPACITY_AVAILABILITY_SWITCHOVER_PRECHECK', 'COMPUTE_CAPACITY_AVAILABILITY_FAILOVER_PRECHECK'

`group_id`

(required) The unique id of the group to which this step belongs. Must not be modified by user. Example: `sgid1.group..uniqueID`

`display_name`

(required) The display name of the step execution. Example: `DATABASE_SWITCHOVER`

`log_location`

(required)

`status`

(required) The status of the step execution.

Allowed values are: 'QUEUED', 'DISABLED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'FAILED_IGNORED', 'TIMED_OUT', 'TIMED_OUT_IGNORED', 'PAUSED', 'CANCELED'

`status_details`

(optional) Additional details on the step execution status. Example: `This step failed to complete due to a timeout`

`time_started`

(optional) The time when step execution began. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_ended`

(optional) The time when execution ended. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`execution_duration_in_sec`

(optional) The total duration in seconds taken to complete the step execution. Example: `35`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_EXECUTION_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_plan_step_execution_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_EXECUTION_T Type

The details of a group execution in a DR plan execution.

Syntax
```

```

Fields

Field Description

`group_id`

(required) The unique id of the group. Must not be modified by user. Example: `sgid1.group..uniqueID`

`l_type`

(required) The group type. Example: `BUILT_IN`

Allowed values are: 'USER_DEFINED', 'BUILT_IN', 'BUILT_IN_PRECHECK'

`display_name`

(required) The display name of the group execution. Example: `DATABASE_SWITCHOVER`

`status`

(required) The status of the group execution.

Allowed values are: 'QUEUED', 'DISABLED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_WARNING', 'FAILED', 'FAILED_IGNORED', 'TIMED_OUT', 'TIMED_OUT_IGNORED', 'PAUSED', 'CANCELED'

`status_details`

(optional) Additional details on the group execution status. Example: `A total of [3] steps failed in the group`

`time_started`

(optional) The time when group execution began. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_ended`

(optional) The time when group execution ended. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`execution_duration_in_sec`

(optional) The total duration in seconds taken to complete group execution. Example: `120`

`step_executions`

(required) A list of step executions in the group.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_EXECUTION_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_plan_group_execution_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_T Type

The details of a DR plan execution.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment containing this DR plan execution. Example: `ocid1.compartment.oc1..uniqueID`

`display_name`

(required) The display name of the DR plan execution. Example: `Execution - EBS Switchover PHX to IAD`

`plan_id`

(required) The OCID of the DR plan. Example: `ocid1.drplan.oc1..uniqueID`

`plan_execution_type`

(required) The type of the DR plan executed.

Allowed values are: 'SWITCHOVER', 'SWITCHOVER_PRECHECK', 'FAILOVER', 'FAILOVER_PRECHECK', 'START_DRILL', 'START_DRILL_PRECHECK', 'STOP_DRILL', 'STOP_DRILL_PRECHECK'

`execution_options`

(required)

`dr_protection_group_id`

(required) The OCID of the DR protection group to which this DR plan execution belongs. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_dr_protection_group_id`

(required) The OCID of peer DR protection group associated with this plan's DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(required) The region of the peer DR protection group associated with this plan's DR protection group. Example: `us-ashburn-1`

`log_location`

(required)

`time_created`

(required) The date and time at which DR plan execution was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_started`

(optional) The date and time at which DR plan execution began. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_updated`

(required) The time when DR plan execution was last updated. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_ended`

(optional) The date and time at which DR plan execution succeeded, failed, was paused, or was canceled. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`execution_duration_in_sec`

(optional) The total duration in seconds taken to complete the DR plan execution. Example: `750`

`group_executions`

(required) A list of groups executed in this DR plan execution.

`lifecycle_state`

(required) The current state of the DR plan execution.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'FAILED', 'DELETING', 'DELETED', 'PAUSING', 'PAUSED', 'RESUMING'

`life_cycle_details`

(optional) A message describing the DR plan execution's current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_SUMMARY_T Type

The summary of a DR plan execution.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DR plan execution. Example: `ocid1.drplanexecution.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment containing this plan execution. Example: `ocid1.compartment.oc1..uniqueID`

`display_name`

(required) The display name of the DR plan execution. Example: `Execution - EBS Switchover PHX to IAD`

`plan_id`

(required) The OCID of the DR plan for this DR plan execution. Example: `ocid1.drplan.oc1..uniqueID`

`plan_execution_type`

(required) The type of the DR plan execution.

Allowed values are: 'SWITCHOVER', 'SWITCHOVER_PRECHECK', 'FAILOVER', 'FAILOVER_PRECHECK', 'START_DRILL', 'START_DRILL_PRECHECK', 'STOP_DRILL', 'STOP_DRILL_PRECHECK'

`dr_protection_group_id`

(required) The OCID of the DR protection group to which this DR plan execution belongs. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_dr_protection_group_id`

(required) The OCID of peer DR protection group associated with this DR plan execution's DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(required) The region of the peer DR protection group associated with this DR plan execution's DR protection group. Example: `us-ashburn-1`

`log_location`

(required)

`time_created`

(required) The date and time at which DR plan execution was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_started`

(optional) The date and time at which DR plan execution began. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_updated`

(required) The time when this DR plan execution was last updated. Example: `2019-03-29T09:36:42Z`

`time_ended`

(optional) The date and time at which DR plan execution succeeded, failed, was paused, or canceled. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`execution_duration_in_sec`

(optional) The total duration in seconds taken to complete the DR plan execution. Example: `750`

`lifecycle_state`

(required) The current state of the DR plan execution.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'FAILED', 'DELETING', 'DELETED', 'PAUSING', 'PAUSED', 'RESUMING'

`life_cycle_details`

(optional) A message describing the DR plan execution's current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_plan_execution_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_COLLECTION_T Type

A list of DR plan execution summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of DR plan execution summaries.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_T Type

The properties of a member in a DR protection group.

Syntax
```

```

Fields

Field Description

`member_id`

(required) The OCID of the member. Example: `ocid1.instance.oc1..uniqueID`

`member_type`

(required) The type of the member.

Allowed values are: 'COMPUTE_INSTANCE', 'COMPUTE_INSTANCE_MOVABLE', 'COMPUTE_INSTANCE_NON_MOVABLE', 'VOLUME_GROUP', 'DATABASE', 'AUTONOMOUS_DATABASE', 'LOAD_BALANCER', 'NETWORK_LOAD_BALANCER', 'FILE_SYSTEM'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_T Type

The details of a DR protection group.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment containing the DR protection group. Example: `ocid1.compartment.oc1..uniqueID`

`display_name`

(required) The display name of the DR protection group. Example: `EBS PHX Group`

`role`

(required) The role of the DR protection group.

Allowed values are: 'PRIMARY', 'STANDBY', 'UNCONFIGURED'

`peer_id`

(optional) The OCID of the peer DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(optional) The region of the peer DR protection group. Example: `us-ashburn-1`

`log_location`

(optional)

`members`

(optional) A list of DR protection group members.

`time_created`

(required) The date and time the DR protection group was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_updated`

(required) The date and time the DR protection group was updated. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`lifecycle_state`

(required) The current state of the DR protection group.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`life_cycle_details`

(optional) A message describing the DR protection group's current state in more detail.

`lifecycle_sub_state`

(optional) The current sub-state of the DR protection group.

Allowed values are: 'DR_DRILL_IN_PROGRESS'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_SUMMARY_T Type

The summary of a DR protection group.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment containing the DR protection group. Example: `ocid1.compartment.oc1..uniqueID`

`display_name`

(required) The display name of the DR protection group. Example: `EBS PHX Group`

`role`

(required) The role of the DR protection group.

Allowed values are: 'PRIMARY', 'STANDBY', 'UNCONFIGURED'

`peer_id`

(optional) The OCID of the peer DR protection group. Example: `ocid1.drprotectiongroup.oc1..uniqueID`

`peer_region`

(optional) The region of the peer DR protection group. Example: `us-ashburn-1`

`time_created`

(required) The date and time the DR protection group was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_updated`

(required) The date and time the DR protection group was updated. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`lifecycle_state`

(required) The current state of the DR protection group.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'INACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`life_cycle_details`

(optional) A message describing the DR protection group's current state in more detail.

`lifecycle_sub_state`

(optional) The current sub-state of the DR protection group.

Allowed values are: 'DR_DRILL_IN_PROGRESS'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_dr_protection_group_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_COLLECTION_T Type

A list of DR protection group summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of DR protection group summaries.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_AUTONOMOUS_DATABASE_T Type

The properties for an Autonomous Database Serverless member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_autonomous_database_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_vnic_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_T Type

Deprecated. Properties for a compute instance member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_compute_instance_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`is_movable`

(optional) A flag indicating if the compute instance should be moved during DR operations. Example: `false`

`vnic_mapping`

(optional) A list of compute instance VNIC mappings.

`destination_compartment_id`

(optional) The OCID of a compartment in the destination region in which the compute instance should be launched. Example: `ocid1.compartment.oc1..uniqueID`

`destination_dedicated_vm_host_id`

(optional) The OCID of a dedicated VM host in the destination region where the compute instance should be launched. Example: `ocid1.dedicatedvmhost.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_movable_vnic_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_movable_file_system_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_MOVABLE_T Type

Properties for a movable compute instance member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_compute_instance_movable_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`is_retain_fault_domain`

(optional) A flag indicating if the compute instance should be moved to the same fault domain in the destination region. The compute instance launch will fail if this flag is set to true and capacity is not available in the specified fault domain in the destination region. Example: `false`

`destination_capacity_reservation_id`

(optional) The OCID of a capacity reservation in the destination region which will be used to launch the compute instance. Example: `ocid1.capacityreservation.oc1..uniqueID`

`vnic_mappings`

(optional) A list of compute instance VNIC mappings.

`destination_compartment_id`

(optional) The OCID of a compartment in the destination region in which the compute instance should be launched. Example: `ocid1.compartment.oc1..uniqueID`

`destination_dedicated_vm_host_id`

(optional) The OCID of a dedicated VM host in the destination region where the compute instance should be launched. Example: `ocid1.dedicatedvmhost.oc1..uniqueID`

`file_system_operations`

(optional) A list of details of operations performed on file systems.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_non_movable_file_system_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_compute_instance_non_movable_block_volume_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_NON_MOVABLE_T Type

Properties for a non-movable compute instance member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_compute_instance_non_movable_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`is_start_stop_enabled`

(optional) A flag indicating whether the non-movable compute instance needs to be started and stopped during DR operations.

`file_system_operations`

(optional) Operations performed on a list of file systems used on the non-movable compute instance.

`block_volume_operations`

(optional) Operations performed on a list of block volumes used on the non-movable compute instance.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_DATABASE_T Type

The properties for a Base Database or Exadata Database member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_database_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`password_vault_secret_id`

(optional) The OCID of the vault secret where the database SYSDBA password is stored. This password is used for performing database DR operations. Example: `ocid1.vaultsecret.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_T Type

The mapping between a primary region file system export path and destination region mount target.

Syntax
```

```

Fields

Field Description

`export_id`

(required) The OCID of the export path. Example: `ocid1.export.oc1..uniqueID`

`destination_mount_target_id`

(required) The OCID of the destination mount target on which this file system export should be created. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_file_system_export_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_FILE_SYSTEM_T Type

The properties for a file system member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_file_system_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`destination_availability_domain`

(optional) The availability domain of the destination mount target. Example: `BBTh:region-AD`

`export_mappings`

(optional) A list of mappings between the primary region file system export and destination region mount target.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_T Type

A backend set mapping between source and destination load balancer.

Syntax
```

```

Fields

Field Description

`is_backend_set_for_non_movable`

(required) This flag specifies if this backend set is used for traffic for non-movable compute instances. Backend sets that point to non-movable instances are only enabled or disabled during DR. For non-movable instances this flag should be set to 'true'. Backend sets that point to movable instances are emptied and their contents are transferred to the destination region load balancer. For movable instances this flag should be set to 'false'. Example: `true`

`source_backend_set_name`

(required) The name of the source backend set. Example: `My_Source_Backend_Set`

`destination_backend_set_name`

(required) The name of the destination backend set. Example: `My_Destination_Backend_Set`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_load_balancer_backend_set_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_LOAD_BALANCER_T Type

The properties for a load balancer member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_load_balancer_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`destination_load_balancer_id`

(optional) The OCID of the destination load balancer. The backend sets in this destination load balancer are updated during DR. Example: `ocid1.loadbalancer.oc1..uniqueID`

`backend_set_mappings`

(optional) A list of backend set mappings that are used to transfer or update backends during DR.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_T Type

A backend set mapping between source and destination network load balancer.

Syntax
```

```

Fields

Field Description

`is_backend_set_for_non_movable`

(required) This flag specifies if this backend set is used for traffic for non-movable compute instances. Backend sets that point to non-movable instances are only enabled or disabled during DR. For non-movable instances this flag should be set to 'true'. Backend sets that point to movable instances are emptied and their contents are transferred to the destination region network load balancer. For movable instances this flag should be set to 'false'. Example: `true`

`source_backend_set_name`

(required) The name of the source backend set. Example: `example_backend_set`

`destination_backend_set_name`

(required) The name of the destination backend set. Example: `example_backend_set`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_network_load_balancer_backend_set_mapping_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_NETWORK_LOAD_BALANCER_T Type

The properties for a network load balancer member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_network_load_balancer_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

Fields

Field Description

`destination_network_load_balancer_id`

(optional) The OCID of the destination network load balancer. The backend sets in this destination network load balancer are updated during DR. Example: `ocid1.networkloadbalancer.oc1..uniqueID`

`backend_set_mappings`

(optional) A list of backend set mappings that are used to transfer or update backends during DR.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_VOLUME_GROUP_T Type

The properties for a volume group member of a DR protection group.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_volume_group_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_protection_group_member_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. Example: `429`

`message`

(required) A human-readable error string. Example: `Too many requests`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_EXECUTION_OPTION_DETAILS_T Type

Options for failover execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_failover_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `true`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the failover. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_EXECUTION_OPTIONS_T Type

Options for failover execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_failover_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `true`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the plan execution. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_PRECHECK_EXECUTION_OPTION_DETAILS_T Type

Options for a failover precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_failover_precheck_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the failover precheck. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_PRECHECK_EXECUTION_OPTIONS_T Type

Options for failover precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_failover_precheck_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the precheck. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_IGNORE_DR_PLAN_EXECUTION_DETAILS_T Type

The details for ignoring a failed group or step.

Syntax
```

```

Fields

Field Description

`group_id`

(required) The unique id of the group to ignore as a whole, or the group containing the step to ignore. Example: `sgid1.group..uniqueID`

`step_id`

(optional) The unique id of the step to ignore (optional). Only needed when ignoring a step. Example: `sgid1.step..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_INVOKE_FUNCTION_PRECHECK_STEP_T Type

Invoke Oracle function precheck step details.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_invoke_function_precheck_step_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_user_defined_step_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_INVOKE_FUNCTION_STEP_T Type

Invoke Oracle function step details.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_invoke_function_step_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_user_defined_step_t`type.

Fields

Field Description

`function_id`

(required) The OCID of function to be invoked. Example: `ocid1.fnfunc.oc1..uniqueID`

`function_region`

(required) The region in which the function is deployed. Example: `us-ashburn-1`

`request_body`

(optional) The request body for the function. Example: `{ \"FnParam1\", \"FnParam2\" }`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOCAL_SCRIPT_PRECHECK_STEP_T Type

Run local script precheck step details.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_local_script_precheck_step_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_user_defined_step_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_OBJECT_STORAGE_SCRIPT_LOCATION_T Type

The details of an object storage script location for a user-defined step in a DR plan.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The namespace in object storage (Note - this is usually the tenancy name). Example: `myocitenancy`

`bucket`

(required) The bucket name inside the object storage namespace. Example: `custom_dr_scripts`

`object`

(required) The object name inside the object storage bucket. Example: `validate_app_start.sh`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_OBJECT_STORE_SCRIPT_PRECHECK_STEP_T Type

Run object store script precheck step details.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_object_store_script_precheck_step_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_user_defined_step_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_PAUSE_DR_PLAN_EXECUTION_DETAILS_T Type

The details for pausing a DR plan execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_pause_dr_plan_execution_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_control_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_RESUME_DR_PLAN_EXECUTION_DETAILS_T Type

The details for resuming a DR plan execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_resume_dr_plan_execution_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_control_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_RETRY_DR_PLAN_EXECUTION_DETAILS_T Type

The details for retrying a failed group or step.

Syntax
```

```

Fields

Field Description

`group_id`

(required) The unique id of the group to retry as a whole, or the group containing the step being retried. Example: `sgid1.group..uniqueID`

`step_id`

(optional) The unique id of the step to retry (optional). Only needed when retrying a step. Example: `sgid1.step..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_RUN_LOCAL_SCRIPT_USER_DEFINED_STEP_T Type

Run Local Script step details.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_run_local_script_user_defined_step_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_user_defined_step_t`type.

Fields

Field Description

`run_on_instance_id`

(required) The OCID of the instance on which this script or command should be executed. **For moving instances:** *runOnInstanceId* must be the OCID of the instance in the region where the instance is currently present. **For non-moving instances:** *runOnInstanceId* must be the OCID of the non-moving instance. Example: `ocid1.instance.oc1..uniqueID`

`run_on_instance_region`

(required) The region in which the instance is present. Example: `us-ashburn-1`

`script_command`

(required) The script name and arguments. Example: `/usr/bin/python3 /home/opc/scripts/my_app_script.py arg1 arg2 arg3`

`run_as_user`

(optional) The userid on the instance to be used for executing the script or command. Example: `opc`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_RUN_OBJECT_STORE_SCRIPT_USER_DEFINED_STEP_T Type

Run Object Store Script step details.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_run_object_store_script_user_defined_step_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_user_defined_step_t`type.

Fields

Field Description

`run_on_instance_id`

(required) The OCID of the instance on which this script or command should be executed. **For moving instances:** *runOnInstanceId* must be the OCID of the instance in the region where the instance is currently present. **For non-moving instances:** *runOnInstanceId* must be the OCID of the non-moving instance. Example: `ocid1.instance.oc1..uniqueID`

`run_on_instance_region`

(required) The region of the instance where this script or command should be executed. Example: `us-ashburn-1`

`object_storage_script_location`

(required)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_EXECUTION_OPTION_DETAILS_T Type

Options for start drill execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_start_drill_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `false`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the plan execution. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_EXECUTION_OPTIONS_T Type

Options for start drill execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_start_drill_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `true`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the plan execution. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_PRECHECK_EXECUTION_OPTION_DETAILS_T Type

Options for start drill precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_start_drill_precheck_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the precheck. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_PRECHECK_EXECUTION_OPTIONS_T Type

Options for start drill precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_start_drill_precheck_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the precheck. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_EXECUTION_OPTION_DETAILS_T Type

Options for stop drill execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_stop_drill_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `false`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the plan execution. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_EXECUTION_OPTIONS_T Type

Options for stop drill execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_stop_drill_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether a precheck should be executed before the plan execution. Example: `true`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the plan execution. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_PRECHECK_EXECUTION_OPTION_DETAILS_T Type

Options for stop drill precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_stop_drill_precheck_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the precheck. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_PRECHECK_EXECUTION_OPTIONS_T Type

Options for stop drill precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_stop_drill_precheck_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the precheck. Example: `false`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_EXECUTION_OPTION_DETAILS_T Type

Options for switchover execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_switchover_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `false`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the switchover. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_EXECUTION_OPTIONS_T Type

Options for switchover execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_switchover_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_prechecks_enabled`

(optional) A flag indicating whether prechecks should be executed before the plan execution. Example: `false`

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the plan execution. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_PRECHECK_EXECUTION_OPTION_DETAILS_T Type

Options for switchover precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_switchover_precheck_execution_option_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_option_details_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the switchover precheck. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_PRECHECK_EXECUTION_OPTIONS_T Type

Options for switchover precheck execution.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_switchover_precheck_execution_options_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_dr_plan_execution_options_t`type.

Fields

Field Description

`are_warnings_ignored`

(optional) A flag indicating whether warnings should be ignored during the precheck. Example: `true`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_BLOCK_VOLUME_ATTACHMENT_DETAILS_T Type

The details for attaching or detaching a block volume.

Syntax
```

```

Fields

Field Description

`volume_attachment_reference_instance_id`

(optional) The OCID of the reference compute instance from which to obtain the attachment details for the volume. This reference compute instance is from the peer DR protection group. Example: `ocid1.instance.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_BLOCK_VOLUME_MOUNT_DETAILS_T Type

The details for updating the file system mount on a block volume.

Syntax
```

```

Fields

Field Description

`mount_point`

(optional) The physical mount point used for mounting the file system on a block volume. Example: `/mnt/yourmountpoint`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_FILE_SYSTEM_MOUNT_DETAILS_T Type

The details for updating the mount properties of a file system.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(optional) The OCID of the mount target for this file system. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_FILE_SYSTEM_UNMOUNT_DETAILS_T Type

The details for updating the unmount properties of a file system.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(optional) The OCID of the mount target for this file system. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type

The details for updating the operations performed on a file systems for movable compute instance.

Syntax
```

```

Fields

Field Description

`export_path`

(required) The export path of the file system. Example: `/fs-export-path`

`mount_point`

(required) The physical mount point of the file system on a host. Example: `/mnt/yourmountpoint`

`mount_details`

(required)

`unmount_details`

(required)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_T Type

The details for updating the operations performed on a block volume.

Syntax
```

```

Fields

Field Description

`block_volume_id`

(required) The OCID of the block volume. Example: `ocid1.volume.oc1..uniqueID`

`attachment_details`

(optional)

`mount_details`

(optional)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type

The details for updating the operations performed on a file systems for non-movable compute instance.

Syntax
```

```

Fields

Field Description

`export_path`

(required) The export path of the file system. Example: `/fs-export-path`

`mount_point`

(required) The physical mount point of the file system on a host. Example: `/mnt/yourmountpoint`

`mount_target_id`

(required) The OCID of mount target. Example: `ocid1.mounttarget.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_USER_DEFINED_STEP_DETAILS_T Type

The details for updating a user-defined step in a DR plan.

Syntax
```

```

Fields

Field Description

`step_type`

(required) The type of the user-defined step. **RUN_OBJECTSTORE_SCRIPT_PRECHECK** - A step which performs a precheck on a script stored in OCI object storage. **RUN_LOCAL_SCRIPT_PRECHECK** - A step which performs a precheck on a script which resides locally on a compute instance. **INVOKE_FUNCTION_PRECHECK** - A step which performs a precheck on an OCI function. See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm. **RUN_OBJECTSTORE_SCRIPT** - A step which runs a script stored in OCI object storage. **RUN_LOCAL_SCRIPT** - A step which runs a script that resides locally on a compute instance. **INVOKE_FUNCTION** - A step which invokes an OCI function. See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm.

Allowed values are: 'RUN_OBJECTSTORE_SCRIPT_PRECHECK', 'RUN_LOCAL_SCRIPT_PRECHECK', 'INVOKE_FUNCTION_PRECHECK', 'RUN_OBJECTSTORE_SCRIPT', 'RUN_LOCAL_SCRIPT', 'INVOKE_FUNCTION'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_STEP_DETAILS_T Type

The details for updating a DR plan step.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique id of the step. Example: `sgid1.step..uniqueID`

`display_name`

(optional) The display name of the step in a group. Example: `My_STEP_3A - EBS Start - STAGE A`

`error_mode`

(optional) The error mode for this step.

Allowed values are: 'STOP_ON_ERROR', 'CONTINUE_ON_ERROR'

`timeout`

(optional) The timeout in seconds for executing this step. Example: `600`

`is_enabled`

(optional) A flag indicating whether this step should be enabled for execution. Example: `true`

`user_defined_step`

(optional)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_STEP_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_update_dr_plan_step_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_GROUP_DETAILS_T Type

The details for updating a group in a DR plan.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique id of the group. Must not be modified by user. Example: `sgid1.group..uniqueID`

`display_name`

(optional) The display name of the group. Example: `My_GROUP_3 - EBS Start`

`l_type`

(optional) The group type. Example: `BUILT_IN`

Allowed values are: 'USER_DEFINED', 'BUILT_IN', 'BUILT_IN_PRECHECK'

`steps`

(optional) The list of steps in this group.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_GROUP_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_update_dr_plan_group_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_DETAILS_T Type

The details for updating a DR plan.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the DR plan being updated. Example: `EBS Switchover PHX to IAD`

`plan_groups`

(optional) An ordered list of groups in a DR plan.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_EXECUTION_DETAILS_T Type

The details for updating a DR plan exection.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the DR protection group to update. Example: `EBS IAD Group`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_OBJECT_STORAGE_LOG_LOCATION_DETAILS_T Type

The details for updating an object storage log location for a DR protection group.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The namespace in object storage (Note - this is usually the tenancy name). Example: `myocitenancy`

`bucket`

(required) The bucket name inside the object storage namespace. Example: `operation_logs`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_T Type

Update properties for a member in a DR protection group.

Syntax
```

```

Fields

Field Description

`member_id`

(required) The OCID of the member. Example: `ocid1.database.oc1..uniqueID`

`member_type`

(required) The type of the member.

Allowed values are: 'COMPUTE_INSTANCE', 'COMPUTE_INSTANCE_MOVABLE', 'COMPUTE_INSTANCE_NON_MOVABLE', 'VOLUME_GROUP', 'DATABASE', 'AUTONOMOUS_DATABASE', 'LOAD_BALANCER', 'NETWORK_LOAD_BALANCER', 'FILE_SYSTEM'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_DETAILS_T Type

The details for updating a DR protection group.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the DR protection group. Example: `EBS PHX Group`

`log_location`

(optional)

`members`

(optional) A list of DR protection group members. When updating members, this list must contain all members being retained, including added and updated members. The list must not contain deleted members.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_AUTONOMOUS_DATABASE_DETAILS_T Type

Update properties for an Autonomous Database Serverless member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_autonomous_database_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_DETAILS_T Type

Deprecated. Update properties for a compute instance member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_compute_instance_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`is_movable`

(optional) A flag indicating if the compute instance should be moved during DR operations. Example: `false`

`vnic_mapping`

(optional) A list of compute instance VNIC mappings.

`destination_compartment_id`

(optional) The OCID of a compartment in the destination region in which the compute instance should be launched. Example: `ocid1.compartment.oc1..uniqueID`

`destination_dedicated_vm_host_id`

(optional) The OCID of a dedicated VM host in the destination region on which the compute instance should be launched. Example: `ocid1.dedicatedvmhost.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_update_compute_instance_movable_file_system_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_MOVABLE_DETAILS_T Type

Update properties for a movable compute instance member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_compute_instance_movable_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`is_retain_fault_domain`

(optional) A flag indicating if the compute instance should be moved to the same fault domain in the destination region. The compute instance launch will fail if this flag is set to true and capacity is not available in the specified fault domain in the destination region. Example: `false`

`destination_capacity_reservation_id`

(optional) The OCID of a capacity reservation in the destination region which will be used to launch the compute instance. Example: `ocid1.capacityreservation.oc1..uniqueID`

`vnic_mappings`

(optional) A list of compute instance VNIC mappings.

`destination_compartment_id`

(optional) The OCID of a compartment in the destination region in which the compute instance should be launched. Example: `ocid1.compartment.oc1..uniqueID`

`destination_dedicated_vm_host_id`

(optional) The OCID of a dedicated VM host in the destination region where the compute instance should be launched. Example: `ocid1.dedicatedvmhost.oc1..uniqueID`

`file_system_operations`

(optional) A list of operations performed on file systems used by the compute instance.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_update_compute_instance_non_movable_file_system_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_update_compute_instance_non_movable_block_volume_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_NON_MOVABLE_DETAILS_T Type

Update properties for a non-movable compute instance member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_compute_instance_non_movable_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`is_start_stop_enabled`

(optional) A flag indicating whether the non-movable compute instance should be started and stopped during DR operations. *Prechecks cannot be executed on stopped instances that are configured to be started.*

`file_system_operations`

(optional) A list of operations performed on file systems used by the compute instance.

`block_volume_operations`

(optional) A list of operations performed on block volumes used by the compute instance.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_DATABASE_DETAILS_T Type

Update properties for a Database (DBCS) member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_database_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`password_vault_secret_id`

(optional) The OCID of the vault secret where the database SYSDBA password is stored. Example: `ocid1.vaultsecret.oc1..uniqueID`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_FILE_SYSTEM_DETAILS_T Type

Update properties for a file system member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_file_system_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`destination_availability_domain`

(optional) The availability domain of the destination mount target. Example: `BBTh:region-AD`

`export_mappings`

(optional) A list of mappings between file system exports in the primary region and mount targets in the standby region.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_LOAD_BALANCER_DETAILS_T Type

Update properties for a load balancer member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_load_balancer_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`destination_load_balancer_id`

(optional) The OCID of the destination load balancer. Example: `ocid1.loadbalancer.oc1..uniqueID`

`backend_set_mappings`

(optional) A list of backend set mappings that are used to transfer or update backends during DR.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_NETWORK_LOAD_BALANCER_DETAILS_T Type

Update properties for a network load balancer member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_network_load_balancer_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

Fields

Field Description

`destination_network_load_balancer_id`

(optional) The OCID of the destination network load balancer. Example: `ocid1.networkloadbalancer.oc1..uniqueID`

`backend_set_mappings`

(optional) A list of backend set mappings that are used to transfer or update backends during DR.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_VOLUME_GROUP_DETAILS_T Type

Update properties for a volume group member.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_volume_group_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_protection_group_member_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_ROLE_DETAILS_T Type

The details for updating the role of a DR protection group.

Syntax
```

```

Fields

Field Description

`role`

(required) The new role of the DR protection group.

Allowed values are: 'PRIMARY', 'STANDBY', 'UNCONFIGURED'

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_INVOKE_FUNCTION_PRECHECK_STEP_DETAILS_T Type

The details for updating Invoke Oracle function precheck step.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_invoke_function_precheck_step_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_plan_user_defined_step_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_INVOKE_FUNCTION_USER_DEFINED_STEP_DETAILS_T Type

The details for updating an Invoke Oracle Function step.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_invoke_function_user_defined_step_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_plan_user_defined_step_details_t`type.

Fields

Field Description

`function_id`

(required) The OCID of function to be invoked. Example: `ocid1.fnfunc.oc1..uniqueID`

`request_body`

(optional) The request body for the function. Example: `{ \"FnParam1\", \"FnParam2\" }`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_LOCAL_SCRIPT_PRECHECK_STEP_DETAILS_T Type

The details for updating Run local script precheck step.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_local_script_precheck_step_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_plan_user_defined_step_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_OBJECT_STORAGE_SCRIPT_LOCATION_DETAILS_T Type

The details for updating an object storage script location for a user-defined step in a DR plan.

Syntax
```

```

Fields

Field Description

`namespace`

(required) The namespace in object storage (Note - this is usually the tenancy name). Example: `myocitenancy`

`bucket`

(required) The bucket name inside the object storage namespace. Example: `custom_dr_scripts`

`object`

(required) The object name inside the object storage bucket. Example: `validate_app_start.sh`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_OBJECT_STORE_SCRIPT_PRECHECK_STEP_DETAILS_T Type

The details for updating Run object store script precheck step.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_object_store_script_precheck_step_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_plan_user_defined_step_details_t`type.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_RUN_LOCAL_SCRIPT_USER_DEFINED_STEP_DETAILS_T Type

The details for updating a Run Local Script step.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_run_local_script_user_defined_step_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_plan_user_defined_step_details_t`type.

Fields

Field Description

`run_on_instance_id`

(required) The OCID of the instance on which this script or command should be executed. **For moving instances:** *runOnInstanceId* must be the OCID of the instance in the region where the instance is currently present. **For non-moving instances:** *runOnInstanceId* must be the OCID of the non-moving instance. Example: `ocid1.instance.oc1..uniqueID`

`script_command`

(required) The script name and arguments. Example: `/usr/bin/python3 /home/opc/scripts/my_app_script.py arg1 arg2 arg3`

`run_as_user`

(optional) The userid on the instance to be used for executing the script or command. Example: `opc`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_RUN_OBJECT_STORE_SCRIPT_USER_DEFINED_STEP_DETAILS_T Type

The details for updating a Run Object Store Script step.

Syntax
```

```

`dbms_cloud_oci_disaster_recovery_update_run_object_store_script_user_defined_step_details_t`is a subtype of the`dbms_cloud_oci_disaster_recovery_update_dr_plan_user_defined_step_details_t`type.

Fields

Field Description

`run_on_instance_id`

(required) The OCID of the instance on which this script or command should be executed. **For moving instances:** *runOnInstanceId* must be the OCID of the instance in the region where the instance is currently present. **For non-moving instances:** *runOnInstanceId* must be the OCID of the non-moving instance. Example: `ocid1.instance.oc1..uniqueID`

`object_storage_script_location`

(required)

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects. Example: `DrPlanExecution`

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier (OCID) of the resource the work request affects. Example: `ocid1.drplanexecution.oc1..uniqueID`

`entity_uri`

(optional) The URI path that the user can use to perform a GET on the resource metadata.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_T Type

Information on a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_DR_PROTECTION_GROUP', 'UPDATE_DR_PROTECTION_GROUP', 'DELETE_DR_PROTECTION_GROUP', 'MOVE_DR_PROTECTION_GROUP', 'ASSOCIATE_DR_PROTECTION_GROUP', 'DISASSOCIATE_DR_PROTECTION_GROUP', 'UPDATE_ROLE_DR_PROTECTION_GROUP', 'CREATE_DR_PLAN', 'UPDATE_DR_PLAN', 'DELETE_DR_PLAN', 'CREATE_DR_PLAN_EXECUTION', 'UPDATE_DR_PLAN_EXECUTION', 'DELETE_DR_PLAN_EXECUTION', 'RETRY_DR_PLAN_EXECUTION', 'IGNORE_DR_PLAN_EXECUTION', 'CANCEL_DR_PLAN_EXECUTION', 'PAUSE_DR_PLAN_EXECUTION', 'RESUME_DR_PLAN_EXECUTION'

`status`

(required) The status of work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'FAILED', 'NEEDS_ATTENTION'

`id`

(required) The OCID of the work request. Example: `ocid1.drworkrequest.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used Example: `ocid1.compartment.oc1..uniqueID`

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage of the request completed. Example: `75`

`time_accepted`

(required) The date and time the request was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_started`

(optional) The date and time the request was started. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_finished`

(optional) The date and time the request was finished. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_ERROR_T Type

An error associcated with a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed here -- (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm). Example: `429`

`message`

(required) A human-readable description of the issue encountered. Example: `TooManyRequests`

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_ERROR_COLLECTION_T Type

The results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request errors.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_LOG_ENTRY_T Type

A log message related to the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message. Example: `DR plan execution is in progress`

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

The results of a workRequestLog search. Contains both WorkRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of workRequestLogEntries.

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_SUMMARY_T Type

The summary of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_DR_PROTECTION_GROUP', 'UPDATE_DR_PROTECTION_GROUP', 'DELETE_DR_PROTECTION_GROUP', 'MOVE_DR_PROTECTION_GROUP', 'ASSOCIATE_DR_PROTECTION_GROUP', 'DISASSOCIATE_DR_PROTECTION_GROUP', 'UPDATE_ROLE_DR_PROTECTION_GROUP', 'CREATE_DR_PLAN', 'UPDATE_DR_PLAN', 'DELETE_DR_PLAN', 'CREATE_DR_PLAN_EXECUTION', 'UPDATE_DR_PLAN_EXECUTION', 'DELETE_DR_PLAN_EXECUTION', 'RETRY_DR_PLAN_EXECUTION', 'IGNORE_DR_PLAN_EXECUTION', 'CANCEL_DR_PLAN_EXECUTION', 'PAUSE_DR_PLAN_EXECUTION', 'RESUME_DR_PLAN_EXECUTION'

`status`

(required) The status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'FAILED', 'NEEDS_ATTENTION'

`id`

(required) The OCID of the work request. Example: `ocid1.workrequest.oc1..uniqueID`

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used. Example: `ocid1.compartment.oc1..uniqueID`

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage of the request completed. Example: `75`

`time_accepted`

(required) The date and time the request was created. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_started`

(optional) The date and time the request was started. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

`time_finished`

(optional) The date and time the request was finished. An RFC3339 formatted datetime string. Example: `2019-03-29T09:36:42Z`

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_disaster_recovery_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_SUMMARY_COLLECTION_T Type

The results of a workRequestSummary search. Contains both WorkRequestSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request summaries.

- [Disaster Recovery Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2D2C872F-F7F0-458E-AB2E-6D59AA8AC4F3)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-754F4368-62A4-4000-BFE1-0B3D3F604130)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_ASSOCIATE_DR_PROTECTION_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-DE6F5647-3DD2-48C5-AF08-FCCC7A0B691B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_BLOCK_VOLUME_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D49AECDA-631D-457F-B0F6-CAFB528E0893)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_BLOCK_VOLUME_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-4A46E5E1-328A-4DC6-B364-B84C64523AC1)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_CONTROL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0FAD2959-E860-4523-8EE1-DFC49803DF0C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CANCEL_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-84A261DB-A128-49BF-BE86-5C573C81D0F6)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CHANGE_DR_PROTECTION_GROUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-59528375-65CD-4B1E-8D51-ED830047EA15)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8AEC994A-3D54-44CC-9BDF-E3063BA807D7)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_UNMOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-6DF716C7-664C-49D2-89AD-129B94EDB1E0)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8D63EEA9-C1C8-40C6-A455-6E0EE65689DA)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-15653DF5-9181-4EE6-8317-F97542AE785F)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-914F2A1A-3823-48A7-AE96-BA3E4B208DD2)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-C0B241BB-A087-46C9-8F0F-9D51C4A20F18)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-BCD5C477-D0CD-4A60-8043-F24749A436A0)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B6E5FE14-B65E-4087-9D47-B4B88EE2EC41)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-3930DAE9-4593-4775-A611-AB163E471371)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_BLOCK_VOLUME_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-39030472-8FE5-44C8-AF46-66BE5BFCB9E8)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_BLOCK_VOLUME_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-63A12F58-5135-4204-885F-55654F306819)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_FILE_SYSTEM_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2B1B5CF5-FB6D-4BD3-AA04-9D8B7AFEAFD6)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_FILE_SYSTEM_UNMOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B6220B56-70D5-4579-93C3-2801A7078E6D)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-1E303F57-546A-4869-923C-E3FA3F90A131)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-A3FEAC76-875A-4179-B780-080AAD577602)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-EDE11926-E6E7-4613-8367-3A54B1AC3E36)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-287B2786-B9C6-48B9-AE72-3AE4795F4364)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-05DA05E8-7A11-41EA-98A4-51C146DD4D09)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B2553372-2170-4242-BF2C-D00BFB787D6D)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_OBJECT_STORAGE_LOG_LOCATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-14284CA1-7ADB-4573-87F8-FBB50BC72DD9)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-CEF71922-D608-48E7-A69D-90547A74A181)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-633852D5-E8B8-41E0-A5F9-EB761EF04DCB)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-5DA3ACE2-4593-48B8-9B4A-F46B8386F221)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_AUTONOMOUS_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-69AB9D4E-5C96-4C8E-A29C-098F82CA7458)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-BF2A3E84-C5D2-4995-9DDA-D6C28D8A03B5)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-CE9077E3-825C-43D6-AF0D-5EF5E82515A1)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-356DDFEB-87E3-4C2F-936C-423C96DAA575)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-21D89F36-3B8A-4364-BE76-86321EC2EF0B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_MOVABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-A45F8158-41DA-415B-9C17-85B0D196E401)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8A62C5C5-ACF5-4843-9CD0-9B484B0D9117)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2FAD1833-DCC8-4F1C-AA11-8A0BD6C7C1E1)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_NON_MOVABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-A9CB5DA3-8CE3-42A1-8718-9CBF73239197)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-FD45606D-95FB-4B19-8CBE-B194E4A37BB9)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-266A55D4-ED32-42F0-841B-B4D8F6713815)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-F05C78FA-7C05-436F-A0C8-825760713A69)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_FILE_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-BEB24E93-CBA2-4AF4-947F-EBE7BA59AA91)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8BE46A76-A2F9-4DDF-8AE7-C92FB5DF3A4E)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-27CBEB47-F7CB-4C8A-9564-6D9EB1CC14AA)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-F80ACB61-2D20-4498-B1A8-54C365FC4436)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8CF222F8-B95E-49F3-86B7-32FB2493B159)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-02638308-F23A-495E-8338-603970174B38)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_NETWORK_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-62DFA677-999B-46EB-9701-F453F5CE752C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_CREATE_DR_PROTECTION_GROUP_MEMBER_VOLUME_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-EB4B7D9B-D764-4510-8179-D57DBC041150)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DISASSOCIATE_DR_PROTECTION_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D281FADA-38FF-4CFD-8266-602140476498)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DISASSOCIATE_DR_PROTECTION_GROUP_DEFAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-37F6B5DE-9C6F-457B-9B70-6025F8FC76E9)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_USER_DEFINED_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-249D9CB2-B05C-461F-90D2-228122DC82C1)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-92F9202C-408F-47A6-959A-5C0BA6AC1CBE)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-CF005021-CAAB-4F8F-AA68-D32174B50D4C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-EAAD8AA2-7131-4464-B526-E148E39945CC)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-1F6125AD-E3BC-490B-9199-CAAA3299887B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-CED8B111-7D6F-435D-B326-5F756D80F9E3)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-9FAC1BBC-45A2-42A1-B8BA-5ECF89954401)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-E283E301-4EBC-4233-A231-F62BEB9DA4E8)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-96A8214B-79E7-4D7A-8561-9535143F5414)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-30A45015-F59F-4969-8D65-919B296EF20B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_OBJECT_STORAGE_LOG_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-001AE86A-BA21-4C6C-B04B-3AC4F513C25F)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-88C6AFA7-9B82-495F-8965-E68D27A517B0)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_STEP_EXECUTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-41D94C9A-3E19-42EF-B1A5-ED25B9238105)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8DDEFDB6-2C54-463E-BC78-FC6228973DED)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_GROUP_EXECUTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D730026C-4BA3-4DF5-836F-531AF05AA33E)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-9FD216D9-24D1-4EE9-B9BF-8705E10C5C80)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B6648D71-B517-49AD-8604-18A90878603B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-167EA9FF-232A-48C2-8B4B-C4E64A8D196C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PLAN_EXECUTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-AA1EC3BB-114F-4947-B58C-DF2BDB8B8615)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-E1B83D24-86E0-4C5F-9624-9DAE484A3EB5)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-6B9A50CF-1218-4C4D-B3DC-38F0853FB537)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-115ECBCF-1AB9-42D1-BF6D-30FA15BBFA42)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-6CD99D4D-8A15-4F8B-8187-ED3410DE70CE)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2D8E36E7-2C7F-4AC8-B031-667A79E53E9C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-97A95B27-C657-4186-A370-ADB2B671E208)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_AUTONOMOUS_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B5276E8B-8EAB-4980-B770-B343AAA0395C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_VNIC_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-26DE5B0F-8D4E-457B-9A0F-C57CD28409A6)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8D02B167-1B8A-4093-A572-5644DA763FDF)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_VNIC_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-3895F42A-6ADB-4AE4-8B81-2C99A95A003C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-25E1461B-70D4-4A78-AFD6-3E68C67BCC67)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_MOVABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-C3A345F9-5DB2-45F7-85CA-9F82070F8E92)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-75B4D14B-A9F9-47AD-A96E-BB6431A00E4E)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-40C6E911-C1B1-4E63-AAFE-97EC0383ABAA)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_NON_MOVABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-25AB097C-613A-4A1E-96EE-5D77A4B2C644)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-51535A63-20D7-449A-BE59-B334DED87FAC)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-10C986DC-8D82-4ACF-BDEC-6A0C40979D2E)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FILE_SYSTEM_EXPORT_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-22A8DD54-44C2-49A2-B7C9-470D36BE5B27)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_FILE_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-FEF1508F-4432-4688-8148-0CBB38116FE9)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-58C26FA2-23F6-4821-B54E-A2C2B054410B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOAD_BALANCER_BACKEND_SET_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-160440FC-4045-4D79-98A9-4E743DECA098)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_LOAD_BALANCER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-C809482A-8883-4A65-8E86-2DD0C7F34D81)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0029C2E5-B6DB-4BCA-B4B3-FDB37FB148E3)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_NETWORK_LOAD_BALANCER_BACKEND_SET_MAPPING_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-353F5061-5E3C-47BA-A9F7-92D0658B9916)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_NETWORK_LOAD_BALANCER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-6B151AED-F537-4F81-98D5-0C80553D4BFC)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_DR_PROTECTION_GROUP_MEMBER_VOLUME_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D0EDF044-F529-477A-B57A-33A48DAF1ED1)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-C9D0D636-D3C8-4C71-B63F-96846D6C1D67)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-73245DB5-A0AF-48B2-B021-3D5C072E613D)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-FAD10F51-A170-4606-A602-2C52777F66F0)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_PRECHECK_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-7B7EB3D0-A897-4F53-9FC7-3629962EA941)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_FAILOVER_PRECHECK_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2D7D9806-757C-4A19-8D31-5D4CF22119EE)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_IGNORE_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-F1B5594F-4B51-4911-B4E8-F38E2D98AC77)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_INVOKE_FUNCTION_PRECHECK_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-C34EAAE6-8F11-411A-B7D3-10F4FC8A30F3)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_INVOKE_FUNCTION_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-38297C02-B3A0-4CA3-B8D9-ECA25F45E628)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_LOCAL_SCRIPT_PRECHECK_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2D737D03-F983-4458-83C7-0054C5E36AC7)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_OBJECT_STORAGE_SCRIPT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B5260957-F77A-4100-AAEE-44B5E60B8F02)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_OBJECT_STORE_SCRIPT_PRECHECK_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-EAF2A2E5-A8E9-4DFF-B923-8A566B5BA17A)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_PAUSE_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-FE816195-4726-4AD9-AFC5-3893FB452306)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_RESUME_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-FA4398BC-D09C-4658-AE7E-09112563F741)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_RETRY_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-AFE2436F-A40C-456A-B2DB-578D6FA33824)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_RUN_LOCAL_SCRIPT_USER_DEFINED_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2DC90224-8AC5-441D-A2B5-52E7802A9329)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_RUN_OBJECT_STORE_SCRIPT_USER_DEFINED_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-23D591CA-9DB8-44FA-9B1E-14D92C23CCF1)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-DCC4ED95-557D-433B-966D-8C17958DD8F7)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-893713E0-7CD5-47B1-A825-79C7206A93B3)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_PRECHECK_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-BE88CE06-4AA2-4C3A-A8AB-5CC0DB720010)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_START_DRILL_PRECHECK_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-26AA5E4F-6B50-4B02-B170-B687D0DA275A)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-177156F1-A38A-4941-8F73-465028430E34)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-4DD77536-4AF2-4E4C-819D-881ED7AF6345)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_PRECHECK_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D88FD94B-03DC-4643-9EA5-0693AA42B5DE)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_STOP_DRILL_PRECHECK_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-83957864-A6BD-486C-8A45-B0338C206972)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-3C3D2E6B-0AB8-43F0-A30E-A0817E60F237)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-DB19DFCE-D0D5-4B9D-BC34-20D8D2DD9270)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_PRECHECK_EXECUTION_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-F16B379F-E619-4B81-B696-ED286C262288)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_SWITCHOVER_PRECHECK_EXECUTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-C939864B-D88E-4361-B963-DA81F0119821)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_BLOCK_VOLUME_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-08376A18-4F6B-4BBA-BB5B-F2779F1332EC)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_BLOCK_VOLUME_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-42977E52-CA6F-407C-8A94-BA323C6C56EE)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_FILE_SYSTEM_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-702D9123-1811-48B0-AA40-7F4153E80825)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_FILE_SYSTEM_UNMOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-9D2CE21F-73FB-4D7C-91DF-80799FA89E4F)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-085EEF56-1B25-4FC7-AED4-57A5A69FA486)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-A2B63C98-5B4F-4253-92BB-9F56E0662C1C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-6720A376-8135-47D6-BD6E-D69CE84F0531)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_USER_DEFINED_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-14A40465-58B3-44AE-88D0-731BA886F646)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-20893CFC-2884-47C3-A415-18BDD5818178)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_STEP_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-9033FED9-9C1A-4B6C-8834-6CC479CEFD39)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D9CD6B5D-1817-4336-83C1-49810A813D28)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_GROUP_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-AFD669ED-AA9B-4993-9183-43BF836D21B5)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-5CC66644-5BCE-4E72-8F04-54AC22F807F4)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PLAN_EXECUTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-61D7D0CB-BB5F-4D10-872D-CF992A00B323)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_OBJECT_STORAGE_LOG_LOCATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2CE56943-28FD-4FD9-8597-F0F8DE4C23F6)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0FA1ECD6-B8DA-4B7E-8CBC-4ED7DBD918AD)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-7D0DBE37-D118-487F-8E01-053A30E39FAC)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0D2D1E51-4948-4D6D-BDCD-A79199480E1E)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_AUTONOMOUS_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-314C423B-3BB5-4050-AB16-A6ECCC55A2BD)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-A3FC51DF-D7F3-4103-881D-7520455D83EA)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B9DC5E75-8D20-4388-BBA3-7D3DC01F17B8)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_MOVABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0624971D-CBC9-4C9E-AD95-DF17A9C93F33)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_FILE_SYSTEM_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2E24F4B3-75BC-433E-BB89-8998CB7E311C)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_COMPUTE_INSTANCE_NON_MOVABLE_BLOCK_VOLUME_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-DD437F23-0EF5-455E-90DB-E7287BF805D5)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_COMPUTE_INSTANCE_NON_MOVABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-381F069B-EA1F-4126-9875-9200E24998E8)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-181E02A4-7F4B-44D9-BA30-1F9910F1E23E)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_FILE_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-44AFB7D0-865A-4A17-9445-99E332640A54)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-57ADFF1F-3C30-4A2B-A4AF-760F76B87CDF)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_NETWORK_LOAD_BALANCER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-D3AED181-3011-4C6C-B20D-D8C7D1D25379)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_MEMBER_VOLUME_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B8C4AB6B-5B94-4511-BF14-B259FC736A39)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_DR_PROTECTION_GROUP_ROLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-2CE1646D-F009-4E68-8273-34679F710918)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_INVOKE_FUNCTION_PRECHECK_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-1E23B6B1-16BB-4D00-B13E-9803BDF32391)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_INVOKE_FUNCTION_USER_DEFINED_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-7922B4B5-E766-4D8D-88C1-44EBAD3F2737)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_LOCAL_SCRIPT_PRECHECK_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-91FBE31D-5A79-4DC9-AAF7-8394815E0623)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_OBJECT_STORAGE_SCRIPT_LOCATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0A0E28D1-DE60-486E-AEE6-A32291037CFC)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_OBJECT_STORE_SCRIPT_PRECHECK_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0D417E22-DCC5-47E1-8E0D-4A0F9B4779C6)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_RUN_LOCAL_SCRIPT_USER_DEFINED_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-A21BA84D-9814-4F0A-8DFE-54C2947B6A76)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_UPDATE_RUN_OBJECT_STORE_SCRIPT_USER_DEFINED_STEP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-0F26D870-27DA-4DFB-8CF8-77BA27D518C8)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-EC38B548-47F4-4868-814B-F4F6E7AA6CB2)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-13356368-215E-43C0-9DAD-AB04F5FA930D)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-F599FA7A-3748-43C2-8B3B-B46686064949)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-8725D6E1-4FEF-4BE4-A256-667E742E61B2)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-942B3032-2C96-4911-9F29-F81E3A74377D)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-3A0EAF8F-AD0A-4E3D-BE35-5DE3AAAAEB6B)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-4907A8C4-A71A-4791-AC87-0DF33F53C823)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-DB7685EB-E837-4C08-91EF-768596547274)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-B91B4BF5-474A-4D77-96E5-CC31CC329B27)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-3AF51295-9A7A-4C22-8D11-67E282EC8549)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-3AA605DE-BA53-430E-BF0F-23D611D67C71)
- [DBMS_CLOUD_OCI_DISASTER_RECOVERY_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/disaster_recovery_t.html#ADSDK-GUID-863422F4-9387-4229-A589-A9415695291D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
