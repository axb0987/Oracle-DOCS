# Cloud Migrations Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#dcoc-content-body)

## Cloud Migrations Common Types

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_RESOURCE_ASSESSMENT_STRATEGY_T Type

Migration strategy for the resource to be migrated.

Syntax
```

```

Fields

Field Description

`resource_type`

(required) The type of resource.

Allowed values are: 'CPU', 'MEMORY', 'ALL'

`strategy_type`

(required) The type of strategy used for migration.

Allowed values are: 'AS_IS', 'AVERAGE', 'PEAK', 'PERCENTILE'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AS_IS_RESOURCE_ASSESSMENT_STRATEGY_T Type

The 'As-Is' based strategy.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_as_is_resource_assessment_strategy_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_resource_assessment_strategy_t`type.

Fields

Field Description

`adjustment_multiplier`

(optional) The real resource usage is multiplied to this number before making any recommendation.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_T Type

Asset source.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.

Allowed values are: 'VMWARE'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the resource.

`display_name`

(required) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the environment.

`inventory_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the inventory that will contain created assets.

`assets_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an attached discovery schedule.

`lifecycle_state`

(required) The current state of the asset source.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING', 'NEEDS_ATTENTION'

`lifecycle_details`

(required) The detailed state of the asset source.

`time_created`

(required) The time when the asset source was created in the RFC3339 format.

`time_updated`

(required) The point in time that the asset source was last updated in the RFC3339 format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_SUMMARY_T Type

Summary of an asset source provided in the list.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.

Allowed values are: 'VMWARE'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resourse.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the resource.

`environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the environment.

`display_name`

(required) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`lifecycle_state`

(required) The current state of the asset source.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING', 'NEEDS_ATTENTION'

`lifecycle_details`

(required) The detailed state of the asset source.

`inventory_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the inventory that will contain created assets.

`assets_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`time_created`

(optional) The time when the asset source was created in RFC3339 format.

`time_updated`

(optional) The point in time that the asset source was last updated in RFC3339 format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_asset_source_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_COLLECTION_T Type

Results of an asset source search. Contains asset source items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of asset sources.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CONNECTION_T Type

Descriptor of a connection to an asset source.

Syntax
```

```

Fields

Field Description

`connection_type`

(required) The type of connection for an asset source.

Allowed values are: 'DISCOVERY', 'REPLICATION'

`connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud bridge connector used for migration operations.

`asset_source_key`

(required) Type-specific identifier for an asset source.

`lifecycle_state`

(required) The current state of the connection.

Allowed values are: 'ACTIVE', 'UPDATING', 'NEEDS_ATTENTION', 'DELETED', 'CREATING'

`lifecycle_details`

(required) The detailed sub-state of the connection.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CONNECTION_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_asset_source_connection_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CONNECTION_COLLECTION_T Type

List of connections for an asset source.

Syntax
```

```

Fields

Field Description

`items`

(required) List of connections.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CREDENTIALS_T Type

Credentials for an asset source.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Authentication type

Allowed values are: 'BASIC'

`secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret in a vault. If the the type of the credentials is BASIC`, the secret must contain the username and password in JSON format, which is in the form of `{ \"username\": \"&lt;VMwareUser&gt;\", \"password\": \"&lt;VMwarePassword&gt;\" }`.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVAILABLE_SHAPE_SUMMARY_T Type

Sumarized information about a shape.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) Availability domain of the shape.

`pagination_token`

(required) Shape name and availability domain. Used for pagination.

`min_total_baseline_ocpus_required`

(optional) Minimum CPUs required.

`shape`

(required) Name of the shape.

`processor_description`

(required) Description of the processor.

`ocpus`

(required) Number of CPUs.

`memory_in_g_bs`

(required) Amount of memory for the shape.

`networking_bandwidth_in_gbps`

(optional) Shape bandwidth.

`max_vnic_attachments`

(optional) Maximum number of virtual network interfaces that can be attached.

`gpus`

(optional) Number of GPUs.

`gpu_description`

(optional) Description of the GPUs.

`local_disks`

(optional) Number of local disks.

`local_disks_total_size_in_g_bs`

(optional) Total size of local disks for shape.

`local_disk_description`

(optional) Description of local disks.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVAILABLE_SHAPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_available_shape_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVAILABLE_SHAPES_COLLECTION_T Type

Results of an available shapes search. Contains list of shapes.

Syntax
```

```

Fields

Field Description

`items`

(required) Available shapes list.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVERAGE_RESOURCE_ASSESSMENT_STRATEGY_T Type

The strategy based on average usage.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_average_resource_assessment_strategy_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_resource_assessment_strategy_t`type.

Fields

Field Description

`adjustment_multiplier`

(optional) The real resource usage is multiplied to this number before making any recommendation.

`metric_type`

(optional) The current state of the migration plan.

Allowed values are: 'AUTO', 'HISTORICAL', 'RUNTIME'

`metric_time_window`

(optional) The current state of the migration plan.

Allowed values are: '1d', '7d', '30d'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_ASSET_SOURCE_COMPARTMENT_DETAILS_T Type

Details for which compartment to move the resource to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_DISCOVERY_SCHEDULE_COMPARTMENT_DETAILS_T Type

Information about the compartment into which the discovery schedule should be moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the discovery schedule should be moved.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_MIGRATION_COMPARTMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_MIGRATION_PLAN_COMPARTMENT_DETAILS_T Type

Details about the compartment into which the resource can be moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_REPLICATION_SCHEDULE_COMPARTMENT_DETAILS_T Type

Information about compartment into which the replication schedule should be moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the replication schedule should be moved.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COMPATIBILITY_MESSAGE_T Type

Information about shape compatibility with the client's current resource configuration.

Syntax
```

```

Fields

Field Description

`severity`

(optional) Severity level of the compatibility issue.

Allowed values are: 'ERROR', 'WARNING', 'INFO'

`name`

(optional) Name of the compatibility issue.

Allowed values are: 'NOT_ENOUGH_DATA', 'INVALID_DATA', 'CPU_COMPATIBILITY_WARNING', 'CPU_METRIC_INFO', 'MEMORY_COMPATIBILITY_WARNING', 'MEMORY_METRIC_INFO', 'VNICS_COMPATIBILITY_WARNING', 'BANDWIDTH_COMPATIBILITY_WARNING', 'GPU_COMPATIBILITY_WARNING', 'OS_WARNING'

`message`

(optional) Detailed description of the compatibility issue.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COMPUTE_COST_ESTIMATION_T Type

Cost estimation for compute

Syntax
```

```

Fields

Field Description

`ocpu_per_hour`

(required) OCPU per hour

`ocpu_per_hour_by_subscription`

(optional) OCPU per hour by subscription

`memory_gb_per_hour`

(required) Gigabyte per hour

`memory_gb_per_hour_by_subscription`

(optional) Gigabyte per hour by subscription

`gpu_per_hour`

(required) GPU per hour

`gpu_per_hour_by_subscription`

(optional) GPU per hour by subscription

`total_per_hour`

(required) Total per hour

`total_per_hour_by_subscription`

(optional) Total usage per hour by subscription

`ocpu_count`

(optional) Total number of OCPUs

`memory_amount_gb`

(optional) Total usage of memory

`gpu_count`

(optional) Total number of GPU

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VOLUME_COST_ESTIMATION_T Type

Cost estimation for volume

Syntax
```

```

Fields

Field Description

`capacity_gb`

(required) Gigabyte storage capacity

`description`

(optional) Volume description

`total_gb_per_month`

(required) Gigabyte storage capacity per month.

`total_gb_per_month_by_subscription`

(optional) Gigabyte storage capacity per month by subscription

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VOLUME_COST_ESTIMATION_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_volume_cost_estimation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_STORAGE_COST_ESTIMATION_T Type

Cost estimation for storage

Syntax
```

```

Fields

Field Description

`volumes`

(required) Volume estimation

`total_gb_per_month`

(required) Gigabyte storage capacity per month.

`total_gb_per_month_by_subscription`

(optional) Gigabyte storage capacity per month by subscription.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_OS_IMAGE_ESTIMATION_T Type

Cost estimation for the OS image.

Syntax
```

```

Fields

Field Description

`total_per_hour`

(required) Total price per hour

`total_per_hour_by_subscription`

(optional) Total price per hour by subscription

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COST_ESTIMATION_T Type

Cost estimation description

Syntax
```

```

Fields

Field Description

`compute`

(required)

`storage`

(required)

`os_image`

(required)

`currency_code`

(optional) Currency code in the ISO format.

`total_estimation_per_month`

(required) Total estimation per month

`total_estimation_per_month_by_subscription`

(optional) Total estimation per month by subscription.

`subscription_id`

(optional) Subscription ID

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_ASSET_SOURCE_DETAILS_T Type

Asset source creation request.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Asset source type.

Allowed values are: 'VMWARE'

`display_name`

(optional) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for the resource.

`environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the environment.

`inventory_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the inventory that will contain created assets.

`assets_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule that is going to be attached to the created asset.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_DISCOVERY_SCHEDULE_DETAILS_T Type

Information about discovery schedule to be created.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the discovery schedule is created.

`execution_recurrences`

(required) Recurrence specification for the discovery schedule execution.

`display_name`

(optional) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_MIGRATION_ASSET_DETAILS_T Type

Details of the new migration asset.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. If empty, then source asset name will be used. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`inventory_asset_id`

(required) OCID of an asset for an inventory.

`migration_id`

(required) OCID of the associated migration.

`replication_schedule_id`

(optional) Replication schedule identifier

`availability_domain`

(required) Availability domain

`replication_compartment_id`

(required) Replication compartment identifier

`snap_shot_bucket_name`

(required) Name of snapshot bucket

`depends_on`

(optional) List of migration assets that depends on this asset.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_MIGRATION_DETAILS_T Type

The information about new migration.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Migration identifier

`compartment_id`

(required) Compartment identifier

`replication_schedule_id`

(optional) Replication schedule identifier

`is_completed`

(optional) Indicates whether migration is marked as complete.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ENVIRONMENT_T Type

Description of the target environment.

Syntax
```

```

Fields

Field Description

`target_compartment_id`

(optional) Target compartment identifier

`target_environment_type`

(required) The type of target environment.

Allowed values are: 'VM_TARGET_ENV'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_RESOURCE_ASSESSMENT_STRATEGY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_resource_assessment_strategy_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ENVIRONMENT_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_target_environment_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_MIGRATION_PLAN_DETAILS_T Type

The information about the new migration plan.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Migration plan identifier

`compartment_id`

(required) Compartment identifier

`migration_id`

(required) The OCID of the associated migration.

`source_migration_plan_id`

(optional) Source migraiton plan ID to be cloned.

`strategies`

(optional) List of strategies for the resources to be migrated.

`target_environments`

(optional) List of target environments.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_REPLICATION_SCHEDULE_DETAILS_T Type

Information about replication schedule to be created.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the replication schedule should be created.

`execution_recurrences`

(required) Recurrence specification for replication schedule execution.

`display_name`

(required) A user-friendly name for a replication schedule. Does not have to be unique, and is mutable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_TARGET_ASSET_DETAILS_T Type

Details of the new target asset.

Syntax
```

```

Fields

Field Description

`migration_plan_id`

(required) OCID of the associated migration plan.

`l_type`

(required) The type of target asset.

Allowed values are: 'INSTANCE'

`is_excluded_from_execution`

(required) A boolean indicating whether the asset should be migrated.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_VNIC_DETAILS_T Type

Contains properties for a VNIC. You use this object when creating the primary VNIC during instance launch or when creating a secondary VNIC. For more information about VNICs, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

Syntax
```

```

Fields

Field Description

`assign_public_ip`

(optional) Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the`SUBNET`Type), then no public IP address is assigned. If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then a public IP address is assigned. If set to true and `prohibitPublicIpOnVnic` = true, an error is returned. **Note:** This public IP address is associated with the primary private IP on the VNIC. For more information, see[IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm). **Note:** There's a limit to the number of`PUBLIC_IP`Type a VNIC or instance can have. If you try to create a secondary VNIC with an assigned public IP for an instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm). Example: `false` If you specify a `vlanId`, then `assignPublicIp` must be set to false. See`VLAN`Type.

`assign_private_dns_record`

(optional) Whether the VNIC should be assigned a DNS record. If set to false, there will be no DNS record registration for the VNIC. If set to true, the DNS record will be registered. By default, the value is true. If you specify a `hostnameLabel`, then `assignPrivateDnsRecord` must be set to true.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). When launching an instance, use this `hostnameLabel` instead of the deprecated `hostnameLabel` in`LAUNCH_INSTANCE_DETAILS`Function. If you provide both, the values must match. Example: `bminstance-1` If you specify a `vlanId`, the `hostnameLabel` cannot be specified. VNICs on a VLAN can not be assigned a hostname. See`VLAN`Type.

`nsg_ids`

(optional) List of OCIDs of the network security groups (NSGs) that are added to the VNIC. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type. If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId` indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs, all VNICs in the VLAN belong to the NSGs that are associated with the VLAN. See`VLAN`Type.

`private_ip`

(optional) A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC's *primary* private IP address. The value appears in the`VNIC`Type object and also the`PRIVATE_IP`Type object returned by`LIST_PRIVATE_IPS`Function and`GET_PRIVATE_IP`Function. If you specify a `vlanId`, the `privateIp` cannot be specified. See`VLAN`Type. Example: `10.0.3.3`

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you should skip the source/destination check, see[Using a Private IP as a Route Target](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip). If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the source/destination check is always disabled for VNICs in a VLAN. See`VLAN`Type. Example: `true`

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet to create the VNIC. When launching an instance, use this `subnetId` instead of the deprecated `subnetId` in`LAUNCH_INSTANCE_DETAILS`Function. At least one of them is required; if you provide both, the values must match. If you are an Oracle Cloud VMware Solution customer and creating a secondary VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`. If you provide both `vlanId` and `subnetId`, the request fails.

`vlan_id`

(optional) Provide this attribute only if you are an Oracle Cloud VMware Solution customer and creating a secondary VNIC in a VLAN. The value is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN. See`VLAN`Type. Provide a `vlanId` instead of a `subnetId`. If you provide both `vlanId` and `subnetId`, the request fails.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_OPTIONS_T Type

Optional mutable instance options

Syntax
```

```

Fields

Field Description

`are_legacy_imds_endpoints_disabled`

(optional) Whether to disable the legacy (/v1) instance metadata service endpoints. Customers who have migrated to /v2 should set this to true for added security. Default is false.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PREEMPTION_ACTION_T Type

The action to run when the preemptible instance is interrupted for eviction.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of action to run when the instance is interrupted for eviction.

Allowed values are: 'TERMINATE'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PREEMPTIBLE_INSTANCE_CONFIG_DETAILS_T Type

Configuration options for preemptible instances.

Syntax
```

```

Fields

Field Description

`preemption_action`

(required)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_T Type

The configuration of plugins associated with this instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The plugin name. To get a list of available plugins, use the`LIST_INSTANCEAGENT_AVAILABLE_PLUGINS`Function operation in the Oracle Cloud Agent API. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`desired_state`

(required) Whether the plugin should be enabled or disabled. To enable the monitoring and management plugins, the `isMonitoringDisabled` and `isManagementDisabled` attributes must also be set to false.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_instance_agent_plugin_config_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_LAUNCH_INSTANCE_AGENT_CONFIG_DETAILS_T Type

Configuration options for the Oracle Cloud Agent software running on the instance.

Syntax
```

```

Fields

Field Description

`is_monitoring_disabled`

(optional) Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins. By default, the value is false (monitoring plugins are enabled). These are the monitoring plugins: Compute instance monitoring and Custom logs monitoring. The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object. - If `isMonitoringDisabled` is true, all the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.

`is_management_disabled`

(optional) Whether Oracle Cloud Agent can run all the available management plugins. By default, the value is false (management plugins are enabled). These are the management plugins: OS Management Service Agent and Compute instance run command. The management plugins are controlled by this parameter and the per-plugin configuration in the `pluginsConfig` object. - If `isManagementDisabled` is true, all the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.

`are_all_plugins_disabled`

(optional) Whether Oracle Cloud Agent can run all the available plugins. This includes the management and monitoring plugins. To get a list of available plugins, use the`LIST_INSTANCEAGENT_AVAILABLE_PLUGINS`Function operation in the Oracle Cloud Agent API. For more information about the available plugins, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).

`plugins_config`

(optional) The configuration of plugins associated with this instance.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_LAUNCH_INSTANCE_SHAPE_CONFIG_DETAILS_T Type

The shape configuration requested for the instance. If the parameter is provided, the instance is created with the resources that you specify. If some properties are missing or the entire parameter is not provided, the instance is created with the default configuration values for the `shape` that you specify. Each shape only supports certain configurable values. If the values that you provide are not valid for the specified `shape`, an error is returned.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the instance.

`memory_in_g_bs`

(optional) The total amount of memory in gigabytes that is available to the instance.

`baseline_ocpu_utilization`

(optional) The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`. The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.

Allowed values are: 'BASELINE_1_8', 'BASELINE_1_2', 'BASELINE_1_1'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_LAUNCH_INSTANCE_DETAILS_T Type

Instance launch details. Use the `sourceDetails` parameter to specify whether a boot volume or an image should be used to launch a new instance.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain of the instance. Example: `Uocm:PHX-AD-1`

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation under which this instance is launched. You can opt out of all default reservations by specifying an empty string as input for this field. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

`compartment_id`

(optional) The OCID of the compartment.

`create_vnic_details`

(optional)

`dedicated_vm_host_id`

(optional) The OCID of the dedicated VM host.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`fault_domain`

(optional) A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains lets you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains. If you do not specify the fault domain, the system selects one for you. To get a list of fault domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`hostname_label`

(optional) Deprecated. Instead use `hostnameLabel` in`CREATE_VNIC_DETAILS`Type. If you provide both, the values must match.

`ipxe_script`

(optional) This is an advanced option. When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process. If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots. Be aware that the same iPXE script will run every time an instance boots, not only after the initial LaunchInstance call. By default, the iPXE script connects to the instance's local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance's local boot volume over iSCSI in the same way as the default iPXE script, use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot. If your instance boot volume type is paravirtualized, the boot volume is attached to the instance through virtio-scsi and no iPXE script is used. If your instance boot volume type is paravirtualized and you use custom iPXE to perform network-boot into your instance, the primary boot volume is attached as a data volume through the virtio-scsi drive. For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see[Bring Your Own Image](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm). For more information about iPXE, see http://ipxe.org.

`instance_options`

(optional)

`preemptible_instance_config`

(optional)

`agent_config`

(optional)

`shape`

(optional) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance. You can enumerate all available shapes by calling`LIST_SHAPES`Function.

`shape_config`

(optional)

`source_details`

(optional)

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. By default, the value is false.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_VM_TARGET_ASSET_DETAILS_T Type

Description of the VM target asset.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_create_vm_target_asset_details_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_create_target_asset_details_t`type.

Fields

Field Description

`preferred_shape_type`

(required) Preferred VM shape type that you provide.

`block_volumes_performance`

(optional) Performance of the block volumes.

`ms_license`

(optional) Microsoft license for the VM configuration.

`user_spec`

(required)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type

Description of an asset source.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_create_vm_ware_asset_source_details_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_create_asset_source_details_t`type.

Fields

Field Description

`vcenter_endpoint`

(required) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

`discovery_credentials`

(required)

`replication_credentials`

(optional)

`are_historical_metrics_collected`

(optional) Flag indicating whether historical metrics are collected for assets, originating from this asset source.

`are_realtime_metrics_collected`

(optional) Flag indicating whether real-time metrics are collected for assets, originating from this asset source.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_T Type

Discovery schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`display_name`

(required) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`execution_recurrences`

(required) Recurrence specification for the discovery schedule execution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the discovery schedule exists.

`lifecycle_state`

(required) Current state of the discovery schedule.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecycle_details`

(required) The detailed state of the discovery schedule.

`time_created`

(required) The time when the discovery schedule was created in RFC3339 format.

`time_updated`

(required) The time when the discovery schedule was last updated in RFC3339 format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_SUMMARY_T Type

Sumarized information about a discovery schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule.

`display_name`

(required) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the discovery schedule exists.

`lifecycle_state`

(required) Current state of the discovery schedule.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecycle_details`

(required) The detailed state of the discovery schedule.

`time_created`

(required) The time when the discovery schedule was created in RFC3339 format.

`time_updated`

(required) The time when the discovery schedule was last updated in RFC3339 format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_discovery_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_COLLECTION_T Type

Results of a discovery schedule search. Contains discovery schedule summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Discovery schedule summaries.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error that is meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_HYDRATED_VOLUME_T Type

Description of the hydration server volume.

Syntax
```

```

Fields

Field Description

`uuid`

(required) ID of the vCenter disk obtained from Inventory.

`volume_id`

(required) ID of the hydration server volume

`volume_type`

(required) The hydration server volume type

Allowed values are: 'BOOT', 'BLOCK'

`unmodified_volume_id`

(required) ID of the unmodified volume

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_SOURCE_VIA_BOOT_VOLUME_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_instance_source_via_boot_volume_details_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_instance_source_details_t`type.

Fields

Field Description

`boot_volume_id`

(required) The OCID of the boot volume used to boot the instance.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_SOURCE_VIA_IMAGE_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_instance_source_via_image_details_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_instance_source_details_t`type.

Fields

Field Description

`boot_volume_size_in_g_bs`

(optional) The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 32,768 GB (32 TB).

`image_id`

(required) The OCID of the image used to boot the instance.

`kms_key_id`

(optional) The OCID of the key management key to assign as the master encryption key for the boot volume.

`boot_volume_vpus_per_gb`

(optional) The number of volume performance units (VPUs) that will be applied to this volume per GB that represents the Block Volume service's elastic performance options. See[Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)for more information. Allowed values: * `10`: Represents Balanced option. * `20`: Represents Higher Performance option. * `30`-`120`: Represents the Ultra High Performance option. For volumes with the auto-tuned performance feature enabled, this is set to the default (minimum) VPUs/GB.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_T Type

A top-level container to track all aspects of a long-running migration workflow to OCI.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(optional) Migration Identifier that can be renamed

`compartment_id`

(required) Compartment Identifier

`lifecycle_state`

(required) The current state of migration.

Allowed values are: 'CREATING', 'UPDATING', 'NEEDS_ATTENTION', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`time_created`

(required) The time when the migration project was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time when the migration project was updated. An RFC3339 formatted datetime string

`replication_schedule_id`

(optional) Replication schedule identifier

`is_completed`

(optional) Indicates whether migration is marked as completed.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_T Type

Description of the migration asset.

Syntax
```

```

Fields

Field Description

`id`

(required) Asset ID generated by mirgration service. It is used in the mirgration service pipeline.

`l_type`

(required) The type of asset referenced for inventory.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(optional) Compartment Identifier

`lifecycle_state`

(required) The current state of the migration asset.

Allowed values are: 'CREATING', 'UPDATING', 'NEEDS_ATTENTION', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`time_created`

(required) The time when the migration asset was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the migration asset was updated. An RFC3339 formatted datetime string.

`migration_id`

(required) OCID of the associated migration.

`snapshots`

(optional) Key-value pair representing disks ID mapped to the OCIDs of replicated or hydration server volume snapshots. Example: `{\"bar-key\": \"value\"}`

`parent_snapshot`

(optional) The parent snapshot of the migration asset to be used by the replication task.

`source_asset_data`

(optional) Key-value pair representing asset metadata keys and values scoped to a namespace. Example: `{\"bar-key\": \"value\"}`

`notifications`

(optional) List of notifications

Allowed values are: 'OUT_OF_DATE', 'SOURCE_REMOVED'

`source_asset_id`

(optional) OCID that is referenced to an asset for an inventory.

`replication_schedule_id`

(optional) Replication schedule identifier

`availability_domain`

(required) Availability domain

`replication_compartment_id`

(required) Replication compartment identifier

`tenancy_id`

(optional) Tenancy identifier

`snap_shot_bucket_name`

(required) Name of snapshot bucket

`depended_on_by`

(optional) List of migration assets that depend on the asset.

`depends_on`

(optional) List of migration assets that depends on the asset.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_SUMMARY_T Type

Summary of the migration asset.

Syntax
```

```

Fields

Field Description

`id`

(required) The asset ID generated by the mirgration service. It is used in the migration service pipeline.

`l_type`

(required) The type of asset referenced for an inventory.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(optional) Compartment identifier

`lifecycle_state`

(required) The current state of the migration asset.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`time_created`

(required) The time when the migration asset was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the migration asset was updated. An RFC3339 formatted datetime string.

`migration_id`

(required) OCID of the associated migration.

`snapshots`

(optional) Key-value pair representing disk's ID that is mapped to the OCIDs of replicated/hydration server volume snapshots. Example: `{\"bar-key\": \"value\"}`

`parent_snapshot`

(optional) The parent snapshot of the mgration asset to be used by the replication task.

`snapshot_info`

(optional) The snapshot information.

`source_asset_data`

(optional) Key-value pair representing asset metadata keys and values scoped to a namespace. Example: `{\"bar-key\": \"value\"}`

`notifications`

(optional) List of notifications.

Allowed values are: 'OUT_OF_DATE', 'SOURCE_REMOVED'

`source_asset_id`

(optional) OCID that is referenced to an asset, for an inventory.

`depended_on_by`

(optional) List of migration assets that depend on this asset.

`depends_on`

(optional) List of migration assets that depend on this asset.

`replication_schedule_id`

(optional) Replication schedule identifier

`tenancy_id`

(optional) Tenancy Identifier

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_migration_asset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_COLLECTION_T Type

Results of a migration asset search. It contains an array of migration assets.

Syntax
```

```

Fields

Field Description

`items`

(required) List of migration asset summaries.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_SUMMARY_T Type

Summary of the migration project.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) Migration identifier that can be renamed

`compartment_id`

(required) Compartment identifier

`time_created`

(required) The time when the migration project was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the migration project was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of migration.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`is_completed`

(optional) Indicates whether migration is marked as complete.

`replication_schedule_id`

(optional) Replication schedule identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_migration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_COLLECTION_T Type

Results of a migration search. Contains both migration summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of migrations.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_STATS_T Type

Status of the migration plan.

Syntax
```

```

Fields

Field Description

`total_estimated_cost`

(optional)

`time_updated`

(optional) The time when the migration plan was calculated. An RFC3339 formatted datetime string.

`vm_count`

(optional) The total count of VMs in migration

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_T Type

Description of the migration plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique Oracle ID (OCID) that is immutable on creation.

`compartment_id`

(required) The OCID of the compartment containing the migration plan.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(required) The time when the migration plan was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the migration plan was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the migration plan.

Allowed values are: 'CREATING', 'UPDATING', 'NEEDS_ATTENTION', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`migration_id`

(required) The OCID of the associated migration.

`strategies`

(required) List of strategies for the resources to be migrated.

`migration_plan_stats`

(optional)

`calculated_limits`

(required) Limits of the resources that are needed for migration. Example: {\"BlockVolume\": 2, \"VCN\": 1}

`target_environments`

(required) List of target environments.

`reference_to_rms_stack`

(optional) OCID of the referenced ORM job.

`source_migration_plan_id`

(optional) Source migraiton plan ID to be cloned.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_SUMMARY_T Type

Summary of the migration plan.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique Oracle ID (OCID) that is immutable on creation.

`compartment_id`

(required) The OCID of the compartment containing the migration plan.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(required) The time when the migration plan was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time when the migration plan was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the migration plan.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`migration_id`

(required) The OCID of the associated migration.

`strategies`

(required) List of strategies for the resources to be migrated.

`migration_plan_stats`

(optional)

`calculated_limits`

(required) Limits of the resources that are needed for migration. Example: {\"BlockVolume\": 2, \"VCN\": 1}

`target_environments`

(required) List of target environments.

`reference_to_rms_stack`

(optional) OCID of the referenced ORM job.

`source_migration_plan_id`

(optional) Source migraiton plan ID to be cloned.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_migration_plan_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_COLLECTION_T Type

Results of a migration plan search. Contains both migration plan summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of migration plan summaries.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PEAK_RESOURCE_ASSESSMENT_STRATEGY_T Type

Peak usage based strategy.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_peak_resource_assessment_strategy_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_resource_assessment_strategy_t`type.

Fields

Field Description

`adjustment_multiplier`

(optional) The real resource usage is multiplied to this number before making any recommendation.

`metric_type`

(optional) The current state of the migration plan.

Allowed values are: 'AUTO', 'HISTORICAL', 'RUNTIME'

`metric_time_window`

(optional) The current state of the migration plan.

Allowed values are: '1d', '7d', '30d'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PERCENTILE_RESOURCE_ASSESSMENT_STRATEGY_T Type

The strategy based on percentile usage.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_percentile_resource_assessment_strategy_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_resource_assessment_strategy_t`type.

Fields

Field Description

`percentile`

(required) Percentile value

Allowed values are: 'P50', 'P90', 'P95', 'P99'

`adjustment_multiplier`

(optional) The real resource usage is multiplied to this number before making any recommendation.

`metric_time_window`

(optional) The current state of the migration plan.

Allowed values are: '1d', '7d', '30d'

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_PROGRESS_T Type

Progress of a migration asset's replication process.

Syntax
```

```

Fields

Field Description

`percentage`

(required) Percentage of the current replication progress from 0 to 100.

`status`

(optional) Status of the current replication progress. It can be None or InProgress.

Allowed values are: 'NONE', 'IN_PROGRESS'

`time_started`

(optional) Start time of the current replication process

`time_oflast_replication_start`

(optional) Start time of the last replication process. It can be Completed or Failed.

`time_of_last_replication_end`

(optional) End time of the last replication process. It can be Completed or Failed.

`time_of_last_replication_success`

(optional) End time of the last successful replication process, which has been completed.

`last_replication_status`

(optional) Status of the last replication task. It can be Completed or Failed.

Allowed values are: 'NONE', 'COMPLETED', 'FAILED'

`last_replication_error`

(optional) Error message if the last finished replication failed.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_T Type

Replication schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication schedule.

`display_name`

(required) A name of the replication schedule.

`execution_recurrences`

(required) Recurrence specification for the replication schedule execution.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the replication schedule exists.

`lifecycle_state`

(required) Current state of the replication schedule.

Allowed values are: 'CREATING', 'UPDATING', 'NEEDS_ATTENTION', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) The detailed state of the replication schedule.

`time_created`

(required) The time when the replication schedule was created in RFC3339 format.

`time_updated`

(required) The time when the replication schedule was last updated in RFC3339 format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_SUMMARY_T Type

Sumarized information about a replication schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication schedule.

`display_name`

(required) A name of the replication schedule.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the replication schedule exists.

`execution_recurrences`

(required) Recurrence specification for replication schedule execution.

`lifecycle_state`

(required) Current state of the replication schedule.

`lifecycle_details`

(required) The detailed state of the replication schedule.

`time_created`

(required) The time when the replication schedule was created in RFC3339 format.

`time_updated`

(required) The time when the replication schedule was last updated in RFC3339 format.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_replication_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_COLLECTION_T Type

Results of a replication schedule search. Contains replication schedule summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Replication schedule summaries.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COMPATIBILITY_MESSAGE_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_compatibility_message_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_T Type

Description of the target asset.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`lifecycle_state`

(required) The current state of the target asset.

Allowed values are: 'CREATING', 'UPDATING', 'NEEDS_ATTENTION', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`migration_plan_id`

(required) OCID of the associated migration plan.

`compartment_id`

(optional) Compartment identifier

`created_resource_id`

(optional) Created resource identifier

`l_type`

(required) The type of target asset.

Allowed values are: 'INSTANCE'

`is_excluded_from_execution`

(required) A boolean indicating whether the asset should be migrated.

`compatibility_messages`

(optional) Messages about the compatibility issues.

`estimated_cost`

(required)

`time_created`

(required) The time when the target asset was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time when the target asset was updated. An RFC3339 formatted datetime string.

`time_assessed`

(required) The time when the assessment was done. An RFC3339 formatted datetime string.

`migration_asset`

(optional)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_SUMMARY_T Type

Summary of the target asset.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`lifecycle_state`

(required) The current state of the target asset.

`migration_plan_id`

(required) OCID of the associated migration plan.

`compartment_id`

(optional) Compartment identifier

`created_resource_id`

(optional) Created resource identifier

`l_type`

(required) The type of target asset.

Allowed values are: 'INSTANCE'

`is_excluded_from_execution`

(required) A boolean indicating whether the asset should be migrated.

`compatibility_messages`

(optional) Messages about compatibility issues.

`estimated_cost`

(required)

`time_created`

(required) The time when the target asset was created. An RFC3339 formatted datetime string.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.

`time_updated`

(required) The time when the target asset was updated. An RFC3339 formatted datetime string.

`time_assessed`

(required) The time when the assessment was done. An RFC3339 formatted datetime string.

`migration_asset`

(optional)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_target_asset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_COLLECTION_T Type

Results of a target asset search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of target asset summaries.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TERMINATE_PREEMPTION_ACTION_T Type

Terminates the preemptible instance when it is interrupted for eviction.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_terminate_preemption_action_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_preemption_action_t`type.

Fields

Field Description

`preserve_boot_volume`

(optional) Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. By default, it is false if not specified.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_ASSET_SOURCE_DETAILS_T Type

The information about the new asset source.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Source type.

Allowed values are: 'VMWARE'

`display_name`

(optional) A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`assets_compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that is going to be used to create assets.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_DISCOVERY_SCHEDULE_DETAILS_T Type

Information about discovery schedule to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.

`execution_recurrences`

(optional) Recurrence specification for the discovery schedule execution.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_MIGRATION_ASSET_DETAILS_T Type

Details of the updated migration asset.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`replication_schedule_id`

(optional) Replication schedule identifier

`depends_on`

(optional) List of migration assets that depends on this asset.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_MIGRATION_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Migration identifier

`replication_schedule_id`

(optional) Replication schedule identifier

`is_completed`

(optional) Indicates whether migration is marked as complete.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_MIGRATION_PLAN_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Migration plan identifier

`strategies`

(optional) List of strategies for the resources to be migrated.

`target_environments`

(optional) List of target environments.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_REPLICATION_SCHEDULE_DETAILS_T Type

Information about replication schedule to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for a replication schedule. Does not have to be unique, and is mutable. Avoid entering confidential information.

`execution_recurrences`

(optional) Recurrence specification for replication schedule execution.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_TARGET_ASSET_DETAILS_T Type

Details of the updated target asset.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of target asset.

Allowed values are: 'INSTANCE'

`is_excluded_from_execution`

(optional) A boolean indicating whether the asset should be migrated.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_VM_TARGET_ASSET_DETAILS_T Type

Description of the VM target asset.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_update_vm_target_asset_details_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_update_target_asset_details_t`type.

Fields

Field Description

`preferred_shape_type`

(optional) Preferred VM shape type that you provided.

`block_volumes_performance`

(optional) Performance of the block volumes.

`ms_license`

(optional) Microsoft license for VM configuration.

`user_spec`

(optional)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type

Asset source update details.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_update_vm_ware_asset_source_details_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_update_asset_source_details_t`type.

Fields

Field Description

`vcenter_endpoint`

(optional) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

`discovery_credentials`

(optional)

`replication_credentials`

(optional)

`are_historical_metrics_collected`

(optional) Flag indicating whether historical metrics are collected for assets, originating from this asset source.

`are_realtime_metrics_collected`

(optional) Flag indicating whether real-time metrics are collected for assets, originating from this asset source.

`discovery_schedule_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the discovery schedule that is going to be assigned to an asset source.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_TARGET_ASSET_T Type

Description of the VM target asset.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_vm_target_asset_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_target_asset_t`type.

Fields

Field Description

`preferred_shape_type`

(required) Preferred VM shape type that you provide.

Allowed values are: 'VM', 'VM_INTEL', 'VM_INTEL_Standard', 'VM_INTEL_DensIO', 'VM_INTEL_GPU', 'VM_INTEL_Optimized', 'VM_AMD', 'VM_AMD_Standard'

`test_spec`

(optional)

`block_volumes_performance`

(optional) Performance of the block volumes.

`ms_license`

(optional) Microsoft license for VM configuration.

`user_spec`

(optional)

`recommended_spec`

(optional)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_TARGET_ASSET_SUMMARY_T Type

Summary of the VM target asset.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_vm_target_asset_summary_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_target_asset_summary_t`type.

Fields

Field Description

`preferred_shape_type`

(required) The preferred VM shape type that you provide.

`block_volumes_performance`

(optional) Performance of the block volumes.

`ms_license`

(optional) Microsoft license for VM configuration.

`user_spec`

(required)

`recommended_spec`

(required)

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_TARGET_ENVIRONMENT_T Type

Description of the VM target environment.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_vm_target_environment_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_target_environment_t`type.

Fields

Field Description

`availability_domain`

(optional) Availability Domain of the VM configuration.

`fault_domain`

(optional) Fault domain of the VM configuration.

`vcn`

(required) OCID of the VM configuration VCN.

`subnet`

(required) OCID of the VM configuration subnet.

`dedicated_vm_host`

(optional) OCID of the dedicated VM configuration host.

`ms_license`

(optional) Microsoft license for the VM configuration.

`preferred_shape_type`

(optional) Preferred VM shape type provided by the customer.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_WARE_ASSET_SOURCE_T Type

Description of an asset source.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_vm_ware_asset_source_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_asset_source_t`type.

Fields

Field Description

`vcenter_endpoint`

(required) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

`discovery_credentials`

(required)

`replication_credentials`

(optional)

`are_historical_metrics_collected`

(optional) Flag indicating whether historical metrics are collected for assets, originating from this asset source.

`are_realtime_metrics_collected`

(optional) Flag indicating whether real-time metrics are collected for assets, originating from this asset source.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_WARE_ASSET_SOURCE_SUMMARY_T Type

Description of an asset source.

Syntax
```

```

`dbms_cloud_oci_cloud_migrations_vm_ware_asset_source_summary_t`is a subtype of the`dbms_cloud_oci_cloud_migrations_asset_source_summary_t`type.

Fields

Field Description

`vcenter_endpoint`

(required) Endpoint for VMware asset discovery and replication in the form of ```https://&lt;host&gt;:&lt;port&gt;/sdk```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_RESOURCE_T Type

A resource that is created and operated by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type that is affected by the work request.

`action_type`

(required) The way in which this resource is affected by the work is tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource. At this point, it transitions to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource that is affected by the work request.

`entity_uri`

(optional) The URI path where you can do a GET operation to access the resource metadata.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_T Type

A description of a work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of the work request.

Allowed values are: 'CREATE_MIGRATION', 'UPDATE_MIGRATION', 'REFRESH_MIGRATION', 'DELETE_MIGRATION', 'MOVE_MIGRATION', 'START_ASSET_REPLICATION', 'START_MIGRATION_REPLICATION', 'CREATE_REPLICATION_SCHEDULE', 'UPDATE_REPLICATION_SCHEDULE', 'DELETE_REPLICATION_SCHEDULE', 'MOVE_REPLICATION_SCHEDULE', 'CREATE_MIGRATION_PLAN', 'UPDATE_MIGRATION_PLAN', 'DELETE_MIGRATION_PLAN', 'MOVE_MIGRATION_PLAN', 'REFRESH_MIGRATION_PLAN', 'EXECUTE_MIGRATION_PLAN', 'REFRESH_MIGRATION_ASSET', 'CREATE_MIGRATION_ASSET', 'DELETE_MIGRATION_ASSET', 'CREATE_TARGET_ASSET', 'UPDATE_TARGET_ASSET', 'DELETE_TARGET_ASSET'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource that is affected by the work request. If the work request affects multiple resources, and these resources are not in the same compartment, the service team can choose the primary resource of the compartment to be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage of request completed.

`time_accepted`

(required) The date and time when the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time when the request started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time when the object was complete, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) The time when the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of the work request error search. Contains both work request error items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request error objects.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time when the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of the work request log search. Contains both work request log items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request log entries.

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The type of work request.

Allowed values are: 'CREATE_MIGRATION', 'UPDATE_MIGRATION', 'REFRESH_MIGRATION', 'DELETE_MIGRATION', 'MOVE_MIGRATION', 'START_ASSET_REPLICATION', 'START_MIGRATION_REPLICATION', 'CREATE_REPLICATION_SCHEDULE', 'UPDATE_REPLICATION_SCHEDULE', 'DELETE_REPLICATION_SCHEDULE', 'MOVE_REPLICATION_SCHEDULE', 'CREATE_MIGRATION_PLAN', 'UPDATE_MIGRATION_PLAN', 'DELETE_MIGRATION_PLAN', 'MOVE_MIGRATION_PLAN', 'REFRESH_MIGRATION_PLAN', 'EXECUTE_MIGRATION_PLAN', 'REFRESH_MIGRATION_ASSET', 'CREATE_MIGRATION_ASSET', 'DELETE_MIGRATION_ASSET', 'CREATE_TARGET_ASSET', 'UPDATE_TARGET_ASSET', 'DELETE_TARGET_ASSET'

`status`

(required) Status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'NEEDS_ATTENTION'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource that is affected by the work request. If the work request affects multiple resources, and these resources are not in the same compartment, the service team can choose the primary resource of the compartment to be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage of request completed.

`time_accepted`

(required) The date and time when the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time when the request started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time when the object was complete, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_cloud_migrations_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of the work request search. Contains both work request items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request summary objects.

- [Cloud Migrations Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-2D3A7A7E-95E6-45CA-8F15-4021392AC643)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-86A1B95D-92AC-47C0-9B21-9B5256CAD613)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_RESOURCE_ASSESSMENT_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-82C394FA-8F57-4E32-B039-9045E7E0E033)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AS_IS_RESOURCE_ASSESSMENT_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-0C54091B-0312-4058-8BC4-5AE879D271F8)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-54807FB8-6081-4ACB-93E8-66689939E2CB)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-610EEF42-8E90-47D3-BB35-0DD93E699663)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-98F0B40C-5EAF-471E-A47B-2DC1CAACA7EF)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-70AFAFE0-5178-4B1B-A7D2-561B8E0EFB4F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-340DF9FC-1C36-4C3A-BB21-BB0AD33F1390)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CONNECTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-039F0BEF-9CF9-4732-AF1F-CBAD6709E4DA)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-FDB877EB-F08A-40CF-A599-95697ABF03DA)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ASSET_SOURCE_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-9A28E527-AD68-4276-88E9-D9D4E952D195)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVAILABLE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-551943CE-EF3B-437E-BEAE-B01FFC4E5CE1)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVAILABLE_SHAPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-C37A4475-7D43-4B7E-BCD4-E99C20AA5B9D)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVAILABLE_SHAPES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-47EBBBD3-4821-48A6-9B81-699A5160196D)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_AVERAGE_RESOURCE_ASSESSMENT_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-B6B18143-4382-4C8A-A53D-6B6CE60A2E5C)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_ASSET_SOURCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-1F88AB79-B0A6-4255-A52F-F369D6FEF89D)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_DISCOVERY_SCHEDULE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-62028406-1C3C-4154-8F4A-DC4282D9C53E)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_MIGRATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-5396B7CC-E784-4171-A9C6-821D389EB28A)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_MIGRATION_PLAN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-DEE7DCA0-83AE-4B3F-9C8D-CA6E69AC4CA2)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CHANGE_REPLICATION_SCHEDULE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-712ABA07-9D50-4117-AF2D-5E17EA788E78)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COMPATIBILITY_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-39C540FE-0743-4FB9-85B4-29D56650E876)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COMPUTE_COST_ESTIMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4F882134-4151-43E6-BCB0-5EF9AC948539)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VOLUME_COST_ESTIMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4B2C9FD2-368A-467F-A003-C2F049626C11)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VOLUME_COST_ESTIMATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-D251A4F3-0378-424D-9899-7CFCDEBA3EBB)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_STORAGE_COST_ESTIMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-2C686EAF-7E10-40F7-AF33-B1B054337170)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_OS_IMAGE_ESTIMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-899D8B46-D305-46E0-A01E-3D86D7584008)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COST_ESTIMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-7B234DA7-CCF5-4EA3-8DA0-3EBB5FB5472F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-2B649B72-7D34-48C9-9841-D0DD26A63B64)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_DISCOVERY_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-CEC6F834-A134-4BAE-B3D7-3C1311D6AEE8)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_MIGRATION_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-8EBB2F45-EF53-4247-95F2-DA2AFE99E8AD)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4230BC54-AE1B-4744-9633-590B9B9D3AE3)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4FFD7AC1-0E44-465E-84E2-F99A690E2A29)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_RESOURCE_ASSESSMENT_STRATEGY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-E2024DF7-070E-4B61-89C9-4A31757432D6)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ENVIRONMENT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-68BA97A5-9471-4EE8-B0A8-3E6B01473E9B)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_MIGRATION_PLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-318B7B03-E662-40E6-86DB-D5BCD415B8E7)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_REPLICATION_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-BDD675E4-8843-4519-8D1A-13B84FF625A4)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_TARGET_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4199A77E-DCAF-4B5D-9503-88E344D79941)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-DFD796E5-57AA-4E55-BEFF-C58216765442)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-AC9DD620-BF97-4D2D-860D-D4376CFE2582)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PREEMPTION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-BE0069AC-B3AE-45B2-BBAC-8F48ECAD92F8)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PREEMPTIBLE_INSTANCE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-1B74B77F-8C64-4859-8D14-EEC05E770E11)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-28739AC7-97C9-4673-BF76-6921553514DA)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_AGENT_PLUGIN_CONFIG_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-7D4F08A5-5382-4644-A069-07CE2C5F6643)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_LAUNCH_INSTANCE_AGENT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-20C01E99-99BB-40A6-AA68-4B6660DD7363)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_LAUNCH_INSTANCE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-580484B2-6409-4FF9-8B0D-AA0FC3CFA9A7)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-16AF122F-A1BF-4034-B5DE-CED245AAEAF6)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_LAUNCH_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-7C0147B4-0117-456F-99A8-97B67EECDEFB)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_VM_TARGET_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-7233D157-442B-49C7-83ED-56D55ACD66E6)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_CREATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4E0E07B5-D6E6-4089-9C49-E87ABB2CE860)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-08E4615C-D724-4D6A-9D03-79BD7F6FAD5C)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-6949A4CB-E08C-4B46-A995-7CA501AB7A26)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-A3608381-059E-4D31-92B5-B4FBCA27D551)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_DISCOVERY_SCHEDULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-7FDAD5E4-728C-41B8-92AA-2370BE0B39E7)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-237E2F9A-5080-4396-B783-A000876C2AA8)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_HYDRATED_VOLUME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-2EDABE83-A120-42D3-806B-5208DD8F819C)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_SOURCE_VIA_BOOT_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-815AACA1-6ED4-4D94-A26E-F59CAE31B661)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_INSTANCE_SOURCE_VIA_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4B9B470D-7183-43B4-806C-66F6CF07B587)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-AE682655-9FA1-4296-923B-A285CF143635)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-F8D4C4A5-188C-4F2E-B135-2CB1D416300E)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-B47AF599-8BF7-4772-AAA9-A7D1CB0BD70A)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-6138D5D6-2763-4A77-861F-DB15A1B59379)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_ASSET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-F68AF7CB-E92F-4035-A3F8-4A7D77572779)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-8A7BCEFB-AC00-4155-ACED-010CE62DE3F7)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-6EE07CB0-3E10-415B-A962-7BEC6EE6CA75)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-5C6B69CA-A545-4414-B504-087A15AF36D4)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-A4F3DA9D-2EB5-4DEF-BCC4-85656B7C3893)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-1C921026-D8C4-42C2-84F4-DF0458CCAFE9)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-53F9FEDC-49D6-4351-9697-A34508477DA1)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-96C5E1A6-15A7-4DC5-B631-E81BB7F42B1D)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_MIGRATION_PLAN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-014B8F6D-4A09-46CF-9B33-EE5D9844DADC)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PEAK_RESOURCE_ASSESSMENT_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-DA83505A-908D-41D8-80A1-73D7B2A2B77A)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_PERCENTILE_RESOURCE_ASSESSMENT_STRATEGY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-5E96AFC8-86A0-4747-9FBD-1F847A83A836)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4FBFB2CC-B792-4299-9598-39DB786E497A)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-88DDDC95-AB81-4266-B5AB-6BEA504710DA)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-0EACA19A-884C-4F5C-8AC7-C6ABCFE7DD8F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-32D11E14-D1EC-4853-A9F1-D241CDB7C07E)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_REPLICATION_SCHEDULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4365E8BA-B5FC-4976-AA1F-6172F5106D82)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_COMPATIBILITY_MESSAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-415E5AFA-C418-4B74-89F0-F074746B5AAB)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-F95A6975-0188-4BB9-B15B-D5129963251A)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-73BEDEC1-101A-4EC0-8D71-F54F1222A23E)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4BDE62C6-99F2-453B-8AF8-848F9E765F6F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TARGET_ASSET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-F807C651-9C33-4784-A328-30B67FF3803F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_TERMINATE_PREEMPTION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-358D5F45-B199-4058-A906-B22A8BCE3831)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-6B8ED93F-E8D0-4090-8BE2-EA79AC7C084F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_DISCOVERY_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-EFC87627-B216-4CFE-9E43-C1B612C5BDDF)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_MIGRATION_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-180E2197-6D58-4E20-B8D1-28CEE57DC84F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-0BB2EF41-3ABE-4B89-904A-AC2A1BA9752F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_MIGRATION_PLAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-8E16D904-8A7D-4673-A292-ECD9BB8098EC)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_REPLICATION_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-1EC90559-3C13-4826-B9A6-82E0436584C6)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_TARGET_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-C95E93E7-BEF8-494D-971B-58160526760D)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_VM_TARGET_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-A8431B58-898A-4E04-8FE6-3791940A1E07)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_UPDATE_VM_WARE_ASSET_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-229C71F8-279E-4F52-ADF5-BF383E122856)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_TARGET_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-9E9EA978-158D-47A2-B22F-9C30D08AF190)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_TARGET_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4AFBD707-FF28-44D1-AC5F-562D9A092A1D)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_TARGET_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-3068ED7A-D3CC-4528-B1CD-BFB9ADF8E764)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_WARE_ASSET_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-703E4D9E-6A38-4042-8F11-2F6EF91DBC2B)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_VM_WARE_ASSET_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-A963136A-0647-4719-8D8A-4E31E7AC2506)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-F4E01D07-31B8-4F68-88A7-8F80C4A3637A)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-57A7E7F5-4A21-4DAC-9E93-94888EE09ECD)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-4A4D7086-7211-4266-BC14-92C28BA48350)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-95466E65-BF0B-4B4F-A7C5-9CD16219343F)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-91A940F9-B229-467E-99C1-A34B82255901)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-F2A1B007-2E3D-466D-B385-5931BD071687)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-59B114E9-88D2-4AEB-B068-6AE1F756BCBD)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-8CCA8932-909A-4B25-8A91-FF83B6C214BC)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-6FC12AF4-63D2-4CBF-83E7-CAF85B8413A3)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-E8AAF238-617C-45D7-92D2-5E8889350C54)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-0E97AC39-0F27-4D5A-835E-A369C1709791)
- [DBMS_CLOUD_OCI_CLOUD_MIGRATIONS_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cloud_migrations_t.html#ADSDK-GUID-C4C32CF0-B143-42D2-8ED4-6ACEDE544C2D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
