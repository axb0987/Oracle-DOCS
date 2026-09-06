# BDS Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#dcoc-content-body)

## BDS Common Types

### DBMS_CLOUD_OCI_BDS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_ACTIVATE_BDS_METASTORE_CONFIGURATION_DETAILS_T Type

The reqeust body when activating a BDS metastore configuration

Syntax
```

```

Fields

Field Description

`bds_api_key_passphrase`

(optional) Base-64 encoded passphrase of the BDS Api Key. Set only if metastore's type is EXTERNAL.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_ADD_AUTO_SCALE_POLICY_DETAILS_T Type

Policy definition for the autoscale configuration. An autoscaling policy is part of an autoscaling configuration. For more information, see[Autoscaling](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-autoscale)You can create following type of autoscaling policies: - **MetricBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered when a performance metric exceeds a threshold - **MetricBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered when a performance metric exceeds a threshold - **ScheduleBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered at the specific times that you schedule. - **ScheduleBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered at the specific times that you schedule. An autoscaling configuration can have one of above supported policies.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) Type of autoscaling policy.

### DBMS_CLOUD_OCI_BDS_METRIC_THRESHOLD_RULE_T Type

An autoscale action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

Fields

Field Description

`duration_in_minutes`

(required) This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.

`operator`

(required) The comparison operator to use. Options are greater than (GT) or less than (LT).

Allowed values are: 'GT', 'LT'

`value`

(required) Integer non-negative value. 0 &lt; value &lt; 100

### DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_METRIC_RULE_T Type

Metric and threshold details for triggering an autoscale action.

Syntax
```

```

Fields

Field Description

`metric_type`

(required) Allowed value is CPU_UTILIZATION.

Allowed values are: 'CPU_UTILIZATION'

`threshold`

(required)

### DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_RULE_T Type

A rule that defines a specific autoscale action to take and the metric that triggers that action.

Syntax
```

```

Fields

Field Description

`action`

(required) The valid value are CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN.

Allowed values are: 'CHANGE_SHAPE_SCALE_UP', 'CHANGE_SHAPE_SCALE_DOWN'

`metric`

(required)

### DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_RULE_TBL Type

Nested table type of dbms_cloud_oci_bds_auto_scale_policy_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_T Type

This model for autoscaling policy is deprecated and not supported for ODH clusters. Use the `AutoScalePolicyDetails` model to manage autoscale policy details for ODH clusters.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)

Allowed values are: 'THRESHOLD_BASED', 'SCHEDULE_BASED', 'NONE'

`rules`

(required) The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.

### DBMS_CLOUD_OCI_BDS_ADD_AUTO_SCALING_CONFIGURATION_DETAILS_T Type

The information about the autoscale configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.

`node_type`

(required) A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.

`is_enabled`

(required) Whether the autoscale configuration is enabled.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`policy`

(optional)

`policy_details`

(optional)

### DBMS_CLOUD_OCI_BDS_ADD_BLOCK_STORAGE_DETAILS_T Type

The information about added block volumes.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`block_volume_size_in_g_bs`

(required) The size of block volume in GB to be added to each worker node. All the details needed for attaching the block volume are managed by service itself.

`node_type`

(required) Worker node types.

Allowed values are: 'WORKER', 'COMPUTE_ONLY_WORKER', 'KAFKA_BROKER'

### DBMS_CLOUD_OCI_BDS_SHAPE_CONFIG_DETAILS_T Type

The shape configuration requested for the node.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to the node.

`memory_in_g_bs`

(optional) The total amount of memory available to the node, in gigabytes.

`nvmes`

(optional) The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.

### DBMS_CLOUD_OCI_BDS_ADD_CLOUD_SQL_DETAILS_T Type

The information about the added Cloud SQL.

Syntax
```

```

Fields

Field Description

`shape`

(required) Shape of the node.

`shape_config`

(optional)

`block_volume_size_in_g_bs`

(optional) The size of block volume in GB to be attached to the given node. All details needed for attaching the block volume are managed by the service itself.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

### DBMS_CLOUD_OCI_BDS_ADD_KAFKA_DETAILS_T Type

The information about the Kafka service to be added.

Syntax
```

```

Fields

Field Description

`shape`

(required) Shape of the Kafka broker node.

`number_of_kafka_nodes`

(required) Number of Kafka nodes for the cluster.

`shape_config`

(optional)

`block_volume_size_in_g_bs`

(optional) The size of block volme in GB to be attached to the given node. All details needed for attaching the block volume are managed by the service itself.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_ADD_MASTER_NODES_DETAILS_T Type

The information about added master nodes.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded Cluster Admin Password for cluster admin user.

`number_of_master_nodes`

(required) Number of additional master nodes for the cluster.

`shape`

(optional) Shape of the node. It's a read-only property derived from existing Master node.

`block_volume_size_in_g_bs`

(optional) The size of block volume in GB to be attached to the given node. It's a read-only property.

`shape_config`

(optional)

### DBMS_CLOUD_OCI_BDS_METRIC_BASED_HORIZONTAL_SCALE_OUT_CONFIG_T Type

Configration for a metric based horizontal scale-out policy.

Syntax
```

```

Fields

Field Description

`metric`

(optional)

`max_node_count`

(optional) This value is the maximum number of nodes the cluster can be scaled-out to.

`step_size`

(optional) This value is the number of nodes to add during a scale-out event.

### DBMS_CLOUD_OCI_BDS_METRIC_BASED_HORIZONTAL_SCALE_IN_CONFIG_T Type

Configration for a metric based horizontal scale-in policy.

Syntax
```

```

Fields

Field Description

`metric`

(optional)

`min_node_count`

(optional) This value is the minimum number of nodes the cluster can be scaled-in to.

`step_size`

(optional) This value is the number of nodes to remove during a scale-in event.

### DBMS_CLOUD_OCI_BDS_ADD_METRIC_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type

Details of a metric based horizontal autoscaling policy. In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_bds_add_metric_based_horizontal_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_add_auto_scale_policy_details_t`type.

Fields

Field Description

`scale_out_config`

(optional)

`scale_in_config`

(optional)

### DBMS_CLOUD_OCI_BDS_METRIC_BASED_VERTICAL_SCALE_UP_CONFIG_T Type

Configration for a metric based vertical scale-up policy.

Syntax
```

```

Fields

Field Description

`metric`

(optional)

`max_ocpus_per_node`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.

`max_memory_per_node`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.

`ocpu_step_size`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.

`memory_step_size`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.

### DBMS_CLOUD_OCI_BDS_METRIC_BASED_VERTICAL_SCALE_DOWN_CONFIG_T Type

Configration for a metric based vertical scale-down policy.

Syntax
```

```

Fields

Field Description

`metric`

(optional)

`min_ocpus_per_node`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the minimum number of OCPUs each node can be scaled-down to. This value is not used for nodes with fixed compute shapes.

`min_memory_per_node`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the minimum memory in GBs each node can be scaled-down to. This value is not used for nodes with fixed compute shapes.

`ocpu_step_size`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the number of OCPUs to remove from each node during a scale-down event. This value is not used for nodes with fixed compute shapes.

`memory_step_size`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the size of memory in GBs to remove from each node during a scale-down event. This value is not used for nodes with fixed compute shapes.

### DBMS_CLOUD_OCI_BDS_ADD_METRIC_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type

Details of a metric based vertical autoscaling policy. In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_bds_add_metric_based_vertical_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_add_auto_scale_policy_details_t`type.

Fields

Field Description

`scale_up_config`

(optional)

`scale_down_config`

(optional)

### DBMS_CLOUD_OCI_BDS_HORIZONTAL_SCALING_SCHEDULE_DETAILS_T Type

Details of a horizontal scaling schedule.

Syntax
```

```

Fields

Field Description

`schedule_type`

(optional) The type of schedule.

### DBMS_CLOUD_OCI_BDS_HORIZONTAL_SCALING_SCHEDULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_bds_horizontal_scaling_schedule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_ADD_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type

Details of a schedule based horizontal autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_bds_add_schedule_based_horizontal_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_add_auto_scale_policy_details_t`type.

Fields

Field Description

`timezone`

(optional) The time zone of the execution schedule, in IANA time zone database name format

`schedule_details`

(optional) Details of a horizontal scaling schedule.

### DBMS_CLOUD_OCI_BDS_VERTICAL_SCALING_SCHEDULE_DETAILS_T Type

Details of a vertical scaling schedule.

Syntax
```

```

Fields

Field Description

`schedule_type`

(optional) The type of schedule.

### DBMS_CLOUD_OCI_BDS_VERTICAL_SCALING_SCHEDULE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_bds_vertical_scaling_schedule_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_ADD_SCHEDULE_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type

Details of a schedule based vertical autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_bds_add_schedule_based_vertical_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_add_auto_scale_policy_details_t`type.

Fields

Field Description

`timezone`

(optional) The time zone of the execution schedule, in IANA time zone database name format

`schedule_details`

(optional) Details of a vertical scaling schedule.

### DBMS_CLOUD_OCI_BDS_ADD_UTILITY_NODES_DETAILS_T Type

The information about added utility nodes.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded Cluster Admin Password for cluster admin user.

`number_of_utility_nodes`

(required) Number of additional utility nodes for the cluster.

`shape`

(optional) Shape of the node. It's a read-only property derived from existing Utility node.

`block_volume_size_in_g_bs`

(optional) The size of block volume in GB to be attached to the given node. It's a read-only property.

`shape_config`

(optional)

### DBMS_CLOUD_OCI_BDS_ADD_WORKER_NODES_DETAILS_T Type

The information about added nodes.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`number_of_worker_nodes`

(required) Number of additional worker nodes for the cluster.

`node_type`

(required) Worker node types, can either be Worker Data node or Compute only worker node.

Allowed values are: 'WORKER', 'COMPUTE_ONLY_WORKER', 'EDGE', 'KAFKA_BROKER'

`shape`

(optional) Shape of the node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.

`block_volume_size_in_g_bs`

(optional) The size of block volume in GB to be attached to the given node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.

`shape_config`

(optional)

### DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_DETAILS_T Type

Details of an autoscale policy. You can create following types of autoscaling policies: - **MetricBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered when a performance metric exceeds a threshold - **MetricBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered when a performance metric exceeds a threshold - **ScheduleBasedVerticalScalingPolicy:** Vertical autoscaling action is triggered at the specific times that you schedule. - **ScheduleBasedHorizontalScalingPolicy:** Horizontal autoscaling action is triggered at the specific times that you schedule.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) Type of autoscaling policy.

Allowed values are: 'METRIC_BASED_VERTICAL_SCALING_POLICY', 'METRIC_BASED_HORIZONTAL_SCALING_POLICY', 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY', 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY'

`trigger_type`

(required) The type of autoscaling trigger.

Allowed values are: 'METRIC_BASED', 'SCHEDULE_BASED'

`action_type`

(required) The type of autoscaling action to take.

Allowed values are: 'VERTICAL_SCALING', 'HORIZONTAL_SCALING'

### DBMS_CLOUD_OCI_BDS_AUTO_SCALING_CONFIGURATION_T Type

The information about the autoscale configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier for the autoscale configuration.

`display_name`

(required) A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.

`node_type`

(required) A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.

`lifecycle_state`

(required) The state of the autoscale configuration.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The time the cluster was created, shown as an RFC 3339 formatted datetime string.

`time_updated`

(required) The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.

`policy`

(required)

`policy_details`

(optional)

### DBMS_CLOUD_OCI_BDS_AUTO_SCALING_CONFIGURATION_SUMMARY_T Type

The information about the autoscale configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the autoscale configuration.

`display_name`

(required) A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.

`lifecycle_state`

(required) The state of the autoscale configuration.

`node_type`

(required) A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.

`time_created`

(required) The time the cluster was created, shown as an RFC 3339 formatted datetime string.

`time_updated`

(required) The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.

`policy`

(required)

`policy_details`

(optional)

### DBMS_CLOUD_OCI_BDS_BDS_API_KEY_T Type

The API key information.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier of the user's API key.

`user_id`

(required) The user OCID for which this API key was created.

`key_alias`

(required) User friendly identifier used to uniquely differentiate between different API keys. Only ASCII alphanumeric characters with no spaces allowed.

`default_region`

(required) The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .

`tenant_id`

(required) The OCID of your tenancy.

`fingerprint`

(required) The fingerprint that corresponds to the public API key requested.

`pemfilepath`

(required) The full path and file name of the private key used for authentication. This location will be automatically selected on the BDS local file system.

`time_created`

(optional) The time the API key was created, shown as an RFC 3339 formatted datetime string.

`lifecycle_state`

(required) The state of the key.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_BDS_BDS_API_KEY_SUMMARY_T Type

The API key summary.

Syntax
```

```

Fields

Field Description

`id`

(required) Identifier of the user's API key.

`key_alias`

(required) User friendly identifier used to uniquely differentiate between different API keys. Only ASCII alphanumeric characters with no spaces allowed.

`lifecycle_state`

(required) The current status of the API key.

`default_region`

(required) The name of the region to establish the Object Storage endpoint which was set as part of key creation operation. If no region was provided this will be set to be the same region where the cluster lives. Example us-phoenix-1 .

`time_created`

(required) The time the API key was created, shown as an RFC 3339 formatted datetime string.

### DBMS_CLOUD_OCI_BDS_NETWORK_CONFIG_T Type

Additional configuration of the user's network.

Syntax
```

```

Fields

Field Description

`is_nat_gateway_required`

(optional) A boolean flag whether to configure a NAT gateway.

`cidr_block`

(optional) The CIDR IP address block of the VCN.

### DBMS_CLOUD_OCI_BDS_CLUSTER_DETAILS_T Type

Specific info about a Hadoop cluster

Syntax
```

```

Fields

Field Description

`bda_version`

(optional) BDA version installed in the cluster

`bdm_version`

(optional) Big Data Manager version installed in the cluster.

`bds_version`

(optional) Big Data Service version installed in the cluster.

`os_version`

(optional) Oracle Linux version installed in the cluster.

`db_version`

(optional) Cloud SQL query server database version.

`bd_cell_version`

(optional) Cloud SQL cell version.

`csql_cell_version`

(optional) Big Data SQL version.

`time_created`

(required) The time the cluster was created, shown as an RFC 3339 formatted datetime string.

`time_refreshed`

(optional) The time the cluster was automatically or manually refreshed, shown as an RFC 3339 formatted datetime string.

`cloudera_manager_url`

(optional) The URL of Cloudera Manager

`ambari_url`

(optional) The URL of Ambari

`big_data_manager_url`

(optional) The URL of Big Data Manager.

`hue_server_url`

(optional) The URL of the Hue server.

`odh_version`

(optional) Version of the ODH (Oracle Distribution including Apache Hadoop) installed on the cluster.

`jupyter_hub_url`

(optional) The URL of the Jupyterhub.

### DBMS_CLOUD_OCI_BDS_VOLUME_ATTACHMENT_DETAIL_T Type

A detail of the attached block volume.

Syntax
```

```

Fields

Field Description

`volume_attachment_id`

(required) The OCID of the volume attachment.

`volume_size_in_g_bs`

(required) The size of the volume in GBs.

### DBMS_CLOUD_OCI_BDS_VOLUME_ATTACHMENT_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_bds_volume_attachment_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_NODE_T Type

Details about a node.

Syntax
```

```

Fields

Field Description

`instance_id`

(required) The OCID of the underlying Oracle Cloud Infrastructure Compute instance.

`display_name`

(required) The name of the node.

`lifecycle_state`

(required) The state of the node.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'STOPPED', 'STOPPING', 'STARTING'

`node_type`

(required) Cluster node type.

Allowed values are: 'MASTER', 'EDGE', 'UTILITY', 'WORKER', 'COMPUTE_ONLY_WORKER', 'KAFKA_BROKER', 'BURSTING', 'CLOUD_SQL'

`shape`

(required) Shape of the node.

`attached_block_volumes`

(optional) The list of block volumes attached to a given node.

`subnet_id`

(required) The OCID of the subnet in which the node is to be created.

`ip_address`

(required) IP address of the node.

`hostname`

(optional) The fully-qualified hostname (FQDN) of the node.

`image_id`

(optional) The OCID of the image from which the node was created.

`ssh_fingerprint`

(required) The fingerprint of the SSH key used for node access.

`availability_domain`

(required) The name of the availability domain in which the node is running.

`fault_domain`

(required) The name of the fault domain in which the node is running.

`time_created`

(required) The time the node was created, shown as an RFC 3339 formatted datetime string.

`time_updated`

(optional) The time the cluster was updated, shown as an RFC 3339 formatted datetime string.

`ocpus`

(optional) The total number of OCPUs available to the node.

`memory_in_g_bs`

(optional) The total amount of memory available to the node, in gigabytes.

`nvmes`

(optional) The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.

`local_disks_total_size_in_g_bs`

(optional) The aggregate size of all local disks, in gigabytes. If the instance does not have any local disks, this field is null.

`time_maintenance_reboot_due`

(optional) The date and time the instance is expected to be stopped / started, in the format defined by RFC3339.

### DBMS_CLOUD_OCI_BDS_KERBEROS_DETAILS_T Type

Details about the Kerberos principals.

Syntax
```

```

Fields

Field Description

`principal_name`

(required) Name of the Kerberos principal.

`keytab_file`

(required) Location of the keytab file

### DBMS_CLOUD_OCI_BDS_KERBEROS_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_bds_kerberos_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_CLOUD_SQL_DETAILS_T Type

The information about added Cloud SQL capability

Syntax
```

```

Fields

Field Description

`shape`

(required) Shape of the node

`block_volume_size_in_g_bs`

(optional) The size of block volume in GB that needs to be attached to a given node. All the necessary details needed for attachment are managed by service itself.

`is_kerberos_mapped_to_database_users`

(optional) Boolean flag specifying whether or not Kerberos principals are mapped to database users.

`ip_address`

(required) IP address of the Cloud SQL node.

`kerberos_details`

(optional) Details about the Kerberos principals.

### DBMS_CLOUD_OCI_BDS_NODE_TBL Type

Nested table type of dbms_cloud_oci_bds_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_BDS_INSTANCE_T Type

Description of the cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Big Data Service resource.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The name of the cluster.

`lifecycle_state`

(required) The state of the cluster.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'SUSPENDING', 'SUSPENDED', 'RESUMING', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`cluster_version`

(optional) Version of the Hadoop distribution.

Allowed values are: 'CDH5', 'CDH6', 'ODH1', 'ODH0_9', 'ODH2_0'

`is_high_availability`

(required) Boolean flag specifying whether or not the cluster is highly available (HA)

`is_secure`

(required) Boolean flag specifying whether or not the cluster should be set up as secure.

`is_cloud_sql_configured`

(required) Boolean flag specifying whether or not Cloud SQL should be configured.

`is_kafka_configured`

(required) Boolean flag specifying whether or not Kafka should be configured.

`network_config`

(optional)

`cluster_details`

(optional)

`nodes`

(required) The list of nodes in the cluster.

`cloud_sql_details`

(optional)

`created_by`

(optional) The user who created the cluster.

`time_created`

(optional) The time the cluster was created, shown as an RFC 3339 formatted datetime string.

`time_updated`

(optional) The time the cluster was updated, shown as an RFC 3339 formatted datetime string.

`number_of_nodes`

(required) Number of nodes that forming the cluster

`number_of_nodes_requiring_maintenance_reboot`

(optional) Number of nodes that require a maintenance reboot

`bootstrap_script_url`

(optional) pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`kms_key_id`

(optional) The OCID of the Key Management master encryption key.

`cluster_profile`

(optional) Profile of the Big Data Service cluster.

Allowed values are: 'HADOOP_EXTENDED', 'HADOOP', 'HIVE', 'SPARK', 'HBASE', 'TRINO', 'KAFKA'

### DBMS_CLOUD_OCI_BDS_BDS_INSTANCE_SUMMARY_T Type

Summary details of the Big Data Service cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Big Data Service resource.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The name of the cluster.

`lifecycle_state`

(required) The state of the cluster.

`number_of_nodes`

(required) The number of nodes that form the cluster.

`number_of_nodes_requiring_maintenance_reboot`

(optional) Number of nodes that require a maintenance reboot

`cluster_version`

(optional) Version of the Hadoop distribution.

`is_high_availability`

(required) Boolean flag specifying whether or not the cluster is highly available(HA).

`is_secure`

(required) Boolean flag specifying whether or not the cluster should be set up as secure.

`is_cloud_sql_configured`

(required) Boolean flag specifying whether Cloud SQL is configured or not.

`is_kafka_configured`

(required) Boolean flag specifying whether Kafka is configured or not.

`cluster_profile`

(optional) Profile of the Big Data Service cluster.

`time_created`

(required) The time the cluster was created, shown as an RFC 3339 formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_BDS_BDS_METASTORE_CONFIGURATION_T Type

The metastore configuration information.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the metastore configuration

`display_name`

(required) The display name of metastore configuration

`metastore_type`

(required) The type of the metastore in the metastore configuration.

Allowed values are: 'LOCAL', 'EXTERNAL'

`metastore_id`

(optional) The OCID of the Data Catalog metastore. Set only if metastore's type is EXTERNAL.

`bds_api_key_id`

(optional) The ID of BDS API Key used for metastore configuration. Set only if metastore's type is EXTERNAL.

`lifecycle_state`

(required) the lifecycle state of the metastore configuration.

Allowed values are: 'CREATING', 'ACTIVATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'DELETING', 'DELETED'

`time_created`

(required) The time when the configuration was created, shown as an RFC 3339 formatted datetime string.

`time_updated`

(optional) The time when the configuration was updated, shown as an RFC 3339 formatted datetime string.

### DBMS_CLOUD_OCI_BDS_BDS_METASTORE_CONFIGURATION_SUMMARY_T Type

The summary of metastore configuration information.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the metastore configuration

`display_name`

(required) The display name of metastore configuration

`metastore_type`

(required) The type of the metastore in the metastore configuration.

`metastore_id`

(optional) The OCID of the Data Catalog metastore. Set only if metastore's type is EXTERNAL.

`bds_api_key_id`

(optional) The ID of BDS API Key used for metastore configuration. Set only if metastore's type is EXTERNAL.

`lifecycle_state`

(required) the lifecycle state of the metastore configuration.

`time_created`

(required) The time when the configuration was created, shown as an RFC 3339 formatted datetime string.

`time_updated`

(optional) The time when the configuration was updated, shown as an RFC 3339 formatted datetime string.

### DBMS_CLOUD_OCI_BDS_CERTIFICATE_SERVICE_INFO_DETAILS_T Type

Details for certificate service info

Syntax
```

```

Fields

Field Description

`services`

(required) List of services for which TLS/SSL needs to be enabled.

### DBMS_CLOUD_OCI_BDS_HOST_SPECIFIC_CERTIFICATE_DETAILS_T Type

Host specific certificate details

Syntax
```

```

Fields

Field Description

`host_name`

(optional) Name of the host.

`certificate_type`

(optional) Type of certificate self signed or CA signed

Allowed values are: 'CUSTOM_SIGNED', 'SELF_SIGNED'

`time_expiry`

(optional) The time the certificate expires, shown as an RFC 3339 formatted datetime string.

### DBMS_CLOUD_OCI_BDS_HOST_SPECIFIC_CERTIFICATE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_bds_host_specific_certificate_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_CERTIFICATE_SERVICE_INFO_SUMMARY_T Type

List of TLS/SSL information of services

Syntax
```

```

Fields

Field Description

`service`

(required) Name of the service

Allowed values are: 'ZOOKEEPER', 'AMS', 'HDFS', 'YARN', 'MAPREDUCE', 'OOZIE', 'HBASE', 'SPARK', 'HIVE', 'KAFKA', 'FLINK', 'REGISTRY'

`service_certificate_status`

(required) Whether certificate is enabled or disabled

Allowed values are: 'ENABLED', 'DISABLED'

`host_specific_certificate_details`

(required) List of Host specific certificate details

### DBMS_CLOUD_OCI_BDS_CHANGE_BDS_INSTANCE_COMPARTMENT_DETAILS_T Type

Move a Cluster to a Different Compartment

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

### DBMS_CLOUD_OCI_BDS_CHANGE_SHAPE_NODES_T Type

Individual worker nodes groups details.

Syntax
```

```

Fields

Field Description

`worker`

(optional) Change shape of worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`worker_shape_config`

(optional)

`compute_only_worker`

(optional) Change shape of compute only worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`compute_only_worker_shape_config`

(optional)

`master`

(optional) Change shape of master nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`master_shape_config`

(optional)

`utility`

(optional) Change shape of utility nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`utility_shape_config`

(optional)

`cloudsql`

(optional) Change shape of the Cloud SQL node to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`cloudsql_shape_config`

(optional)

`edge`

(optional) Change shape of edge nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`edge_shape_config`

(optional)

`kafka_broker`

(optional) Change shape of Kafka Broker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.

`kafka_broker_shape_config`

(optional)

### DBMS_CLOUD_OCI_BDS_CHANGE_SHAPE_DETAILS_T Type

Resize details specified for individual nodes.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`nodes`

(required)

### DBMS_CLOUD_OCI_BDS_CREATE_BDS_API_KEY_DETAILS_T Type

API key created on user's behalf.

Syntax
```

```

Fields

Field Description

`user_id`

(required) The OCID of the user for whom this new generated API key pair will be created.

`passphrase`

(required) Base64 passphrase used to secure the private key which will be created on user behalf.

`default_region`

(optional) The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.

`key_alias`

(required) User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.

### DBMS_CLOUD_OCI_BDS_CREATE_NODE_DETAILS_T Type

The information about the new node.

Syntax
```

```

Fields

Field Description

`node_type`

(required) The Big Data Service cluster node type.

`shape`

(required) Shape of the node.

`block_volume_size_in_g_bs`

(required) The size of block volume in GB to be attached to a given node. All the details needed for attaching the block volume are managed by service itself.

`subnet_id`

(required) The OCID of the subnet in which the node will be created.

`shape_config`

(optional)

### DBMS_CLOUD_OCI_BDS_CREATE_NODE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_bds_create_node_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_CREATE_BDS_INSTANCE_DETAILS_T Type

The information about the new cluster.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) Name of the Big Data Service cluster.

`cluster_version`

(required) Version of the Hadoop distribution.

`cluster_public_key`

(required) The SSH public key used to authenticate the cluster connection.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`is_high_availability`

(required) Boolean flag specifying whether or not the cluster is highly available (HA).

`is_secure`

(required) Boolean flag specifying whether or not the cluster should be set up as secure.

`network_config`

(optional)

`bootstrap_script_url`

(optional) Pre-authenticated URL of the script in Object Store that is downloaded and executed.

`nodes`

(required) The list of nodes in the Big Data Service cluster.

`kerberos_realm_name`

(optional) The user-defined kerberos realm name.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`kms_key_id`

(optional) The OCID of the Key Management master encryption key.

`cluster_profile`

(optional) Profile of the Big Data Service cluster.

### DBMS_CLOUD_OCI_BDS_CREATE_BDS_METASTORE_CONFIGURATION_DETAILS_T Type

The request body when creating BDS metastore configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the metastore configuration

`metastore_id`

(required) The OCID of the Data Catalog metastore.

`bds_api_key_id`

(required) The ID of BDS Api Key used for Data Catalog metastore integration.

`bds_api_key_passphrase`

(required) Base-64 encoded passphrase of the BDS Api Key.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_TIME_AND_HORIZONTAL_SCALING_CONFIG_T Type

Time of day and horizontal scaling configuration.

Syntax
```

```

Fields

Field Description

`time_recurrence`

(optional) Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.

`target_node_count`

(optional) This value is the desired number of nodes in the cluster.

### DBMS_CLOUD_OCI_BDS_TIME_AND_HORIZONTAL_SCALING_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_bds_time_and_horizontal_scaling_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_DAY_BASED_HORIZONTAL_SCALING_SCHEDULE_DETAILS_T Type

Details of day based horizontal scaling schedule.

Syntax
```

```

`dbms_cloud_oci_bds_day_based_horizontal_scaling_schedule_details_t`is a subtype of the`dbms_cloud_oci_bds_horizontal_scaling_schedule_details_t`type.

Fields

Field Description

`time_and_horizontal_scaling_config`

(optional) Time of day and horizontal scaling configuration.

### DBMS_CLOUD_OCI_BDS_TIME_AND_VERTICAL_SCALING_CONFIG_T Type

Time of day and vertical scaling configuration.

Syntax
```

```

Fields

Field Description

`time_recurrence`

(optional) Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.

`target_shape`

(optional) For nodes with[fixed compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the desired shape of each node. This value is not used for nodes with flexible compute shapes.

`target_ocpus_per_node`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the desired OCPUs count on each node. This value is not used for nodes with fixed compute shapes.

`target_memory_per_node`

(optional) For nodes with[flexible compute shapes](https://docs.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape), this value is the desired memory in GBs on each node. This value is not used for nodes with fixed compute shapes.

### DBMS_CLOUD_OCI_BDS_TIME_AND_VERTICAL_SCALING_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_bds_time_and_vertical_scaling_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_DAY_BASED_VERTICAL_SCALING_SCHEDULE_DETAILS_T Type

Details of day based vertical scaling schedule.

Syntax
```

```

`dbms_cloud_oci_bds_day_based_vertical_scaling_schedule_details_t`is a subtype of the`dbms_cloud_oci_bds_vertical_scaling_schedule_details_t`type.

Fields

Field Description

`time_and_vertical_scaling_config`

(optional) Time of day and vertical scaling configuration

### DBMS_CLOUD_OCI_BDS_DEFAULT_ERROR_T Type

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

### DBMS_CLOUD_OCI_BDS_DISABLE_CERTIFICATE_DETAILS_T Type

The request body info about disable certificate service list.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

`services`

(required) List of services for which certificate needs to be disabled.

### DBMS_CLOUD_OCI_BDS_HOST_CERT_DETAILS_T Type

Details about the host and corresponding certificate.

Syntax
```

```

Fields

Field Description

`host_name`

(required) Fully qualified domain name (FQDN) of the host

`certificate`

(required) Certificate value in string format

`private_key`

(required) Private key of the provided certificate

### DBMS_CLOUD_OCI_BDS_HOST_CERT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_bds_host_cert_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_ENABLE_CERTIFICATE_DETAILS_T Type

The request body info about configure certificate service list.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

`services`

(required) List of services for which certificate needs to be enabled.

`root_certificate`

(optional) Plain text certificate/s in order, separated by new line character. If not provided in request a self-signed root certificate is generated inside the cluster. In case hostCertDetails is provided, root certificate is mandatory.

`host_cert_details`

(optional) List of leaf certificates to use for services on each host. If custom host certificate is provided the root certificate becomes required.

`server_key_password`

(optional) Base-64 encoded password for CA certificate's private key. This value can be empty.

### DBMS_CLOUD_OCI_BDS_EXECUTE_BOOTSTRAP_SCRIPT_DETAILS_T Type

The information about the bootstrap script to be executed.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

`bootstrap_script_url`

(optional) pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed.

### DBMS_CLOUD_OCI_BDS_INSTALL_OS_PATCH_DETAILS_T Type

Os patch details for installing a os patches to a cluster.

Syntax
```

```

Fields

Field Description

`os_patch_version`

(required) The target os patch version.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_INSTALL_PATCH_DETAILS_T Type

The reqeust body while installing a patch to a cluster.

Syntax
```

```

Fields

Field Description

`version`

(required) The version of the patch to be installed.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_METRIC_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type

Details of a metric based horizontal autoscaling policy. In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_bds_metric_based_horizontal_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_auto_scale_policy_details_t`type.

Fields

Field Description

`scale_out_config`

(optional)

`scale_in_config`

(optional)

### DBMS_CLOUD_OCI_BDS_METRIC_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type

Details of a metric based vertical autoscaling policy. In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_bds_metric_based_vertical_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_auto_scale_policy_details_t`type.

Fields

Field Description

`scale_up_config`

(optional)

`scale_down_config`

(optional)

### DBMS_CLOUD_OCI_BDS_OS_PATCH_PACKAGE_SUMMARY_T Type

Summary of a package contained in a os patch.

Syntax
```

```

Fields

Field Description

`package_name`

(required) The package's name.

`target_version`

(optional) The target version of the package.

`update_type`

(required) The action that current package will be executed on the cluster.

Allowed values are: 'INSTALL', 'REMOVE', 'UPDATE'

`related_cv_es`

(required) Related CVEs of the package update.

### DBMS_CLOUD_OCI_BDS_OS_PATCH_PACKAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_bds_os_patch_package_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_OS_PATCH_DETAILS_T Type

Details of an os patch.

Syntax
```

```

Fields

Field Description

`os_patch_version`

(required) Version of the os patch.

`min_bds_version`

(required) Minimum BDS version required to install current OS patch.

`min_compatible_odh_version_map`

(required) Map of major ODH version to minimum ODH version required to install current OS patch. e.g. {ODH0.9: 0.9.1}

`target_packages`

(required) List of summaries of individual target packages.

`release_date`

(required) Released date of the OS patch.

`patch_type`

(required) Type of a specific os patch. REGULAR means standard released os patches. CUSTOM means os patches with some customizations. EMERGENT means os patches with some emergency fixes that should be prioritized.

Allowed values are: 'REGULAR', 'CUSTOM', 'EMERGENT'

### DBMS_CLOUD_OCI_BDS_OS_PATCH_SUMMARY_T Type

Summary of an available os patch to a cluster.

Syntax
```

```

Fields

Field Description

`os_patch_version`

(required) Patch version of the os patch.

`release_date`

(required) The time when the OS patch was released.

### DBMS_CLOUD_OCI_BDS_PATCH_HISTORY_SUMMARY_T Type

Patch history of this cluster.

Syntax
```

```

Fields

Field Description

`version`

(required) The version of the patch.

`lifecycle_state`

(required) The status of this patch.

Allowed values are: 'INSTALLING', 'INSTALLED', 'FAILED'

`time_updated`

(required) The time when the patch history was last updated.

`patch_type`

(required) The type of current patch history. DP - Data Plane patch(This history type is internal available only) ODH - Oracle Distribution of Hadoop patch OS - Operating System patch

Allowed values are: 'ODH', 'OS'

### DBMS_CLOUD_OCI_BDS_PATCH_SUMMARY_T Type

The patch that is currently available for the cluster.

Syntax
```

```

Fields

Field Description

`version`

(required) The version of the patch.

`time_released`

(required) The time when the patch was released.

### DBMS_CLOUD_OCI_BDS_REMOVE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type

The information about the removed autoscale configuration.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

### DBMS_CLOUD_OCI_BDS_REMOVE_CLOUD_SQL_DETAILS_T Type

The information about the Cloud SQL installation that was removed.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

### DBMS_CLOUD_OCI_BDS_REMOVE_KAFKA_DETAILS_T Type

The information about the Kafka installation to be removed. All configured Kafka nodes are considered for removal.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_REMOVE_NODE_DETAILS_T Type

The information about node to be removed.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`is_force_remove_enabled`

(optional) Boolean flag specifying whether or not to force remove node if graceful removal fails.

`node_id`

(required) OCID of the node to be removed.

### DBMS_CLOUD_OCI_BDS_RENEW_CERTIFICATE_DETAILS_T Type

The request body info about renew certificate service list.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

`services`

(optional) List of services for which certificate needs to be renewed. If no services provided renew will happen only for default services - AMBARI,RANGER,HUE,LIVY.

`root_certificate`

(optional) Plain text certificate/s in order, separated by new line character. If not provided in request a self-signed root certificate is generated inside the cluster. In case hostCertDetails is provided, root certificate is mandatory.

`host_cert_details`

(optional) List of leaf certificates to use for services on each host. If custom host certificate is provided the root certificate becomes required.

`server_key_password`

(optional) Base-64 encoded password for CA certificate's private key. This value can be empty.

### DBMS_CLOUD_OCI_BDS_RESTART_NODE_DETAILS_T Type

The information about restarted node.

Syntax
```

```

Fields

Field Description

`node_id`

(required) OCID of the node to be restarted.

### DBMS_CLOUD_OCI_BDS_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type

Details of a schedule based horizontal autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_bds_schedule_based_horizontal_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_auto_scale_policy_details_t`type.

Fields

Field Description

`timezone`

(optional) The time zone of the execution schedule, in IANA time zone database name format

`schedule_details`

(optional) Details of a horizontal scaling schedule.

### DBMS_CLOUD_OCI_BDS_SCHEDULE_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type

Details of a schedule based vertical autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_bds_schedule_based_vertical_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_auto_scale_policy_details_t`type.

Fields

Field Description

`timezone`

(optional) The time zone of the execution schedule, in IANA time zone database name format

`schedule_details`

(optional) Details of a vertical scaling schedule.

### DBMS_CLOUD_OCI_BDS_START_BDS_INSTANCE_DETAILS_T Type

The request body for starting a BDS cluster.

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_STOP_BDS_INSTANCE_DETAILS_T Type

The request body for stopping a BDS cluster.

Syntax
```

```

Fields

Field Description

`is_force_stop_jobs`

(optional) Boolean indicating whether to force stop jobs while stopping cluster. Defaults to false.

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_TEST_BDS_METASTORE_CONFIGURATION_DETAILS_T Type

The reqeust body when testing a BDS metastore configuration

Syntax
```

```

Fields

Field Description

`cluster_admin_password`

(required) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_TEST_BDS_OBJECT_STORAGE_CONNECTION_DETAILS_T Type

Test access to specified Object Storage bucket using the API key.

Syntax
```

```

Fields

Field Description

`object_storage_uri`

(required) An Oracle Cloud Infrastructure URI to which this connection must be attempted. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`passphrase`

(required) Base64 passphrase used to secure the private key which will be created on user behalf.

`object_storage_region`

(optional) The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .

### DBMS_CLOUD_OCI_BDS_UPDATE_AUTO_SCALE_POLICY_DETAILS_T Type

Update details of an autoscaling policy.

Syntax
```

```

Fields

Field Description

`policy_type`

(required) Type of autoscaling policy.

### DBMS_CLOUD_OCI_BDS_UPDATE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type

The information about the autoscale configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.

`is_enabled`

(optional) Whether the autoscale configuration is enabled.

`cluster_admin_password`

(optional) Base-64 encoded password for the cluster (and Cloudera Manager) admin user.

`policy`

(optional)

`policy_details`

(optional)

### DBMS_CLOUD_OCI_BDS_UPDATE_BDS_INSTANCE_DETAILS_T Type

The information about to-be-updated Big Data Service cluster.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name of the cluster.

`bootstrap_script_url`

(optional) Pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed..

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`kms_key_id`

(optional) The OCID of the Key Management master encryption key.

### DBMS_CLOUD_OCI_BDS_UPDATE_BDS_METASTORE_CONFIGURATION_DETAILS_T Type

The request body when updating BDS metastore configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name of the metastore configuration.

`bds_api_key_id`

(optional) The ID of BDS Api Key used for Data Catalog metastore integration. Set only if metastore's type is EXTERNAL.

`bds_api_key_passphrase`

(optional) Base-64 encoded passphrase of the BDS Api Key.

`cluster_admin_password`

(optional) Base-64 encoded password for the cluster admin user.

### DBMS_CLOUD_OCI_BDS_UPDATE_METRIC_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type

Update details of a metric based horizontal autoscaling policy. In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_bds_update_metric_based_horizontal_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_update_auto_scale_policy_details_t`type.

Fields

Field Description

`scale_out_config`

(optional)

`scale_in_config`

(optional)

### DBMS_CLOUD_OCI_BDS_UPDATE_METRIC_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type

Update details of a metric based vertical autoscaling policy. In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_bds_update_metric_based_vertical_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_update_auto_scale_policy_details_t`type.

Fields

Field Description

`scale_up_config`

(optional)

`scale_down_config`

(optional)

### DBMS_CLOUD_OCI_BDS_UPDATE_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type

Update details of a schedule based horizontal autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_bds_update_schedule_based_horizontal_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_update_auto_scale_policy_details_t`type.

Fields

Field Description

`timezone`

(optional) The time zone of the execution schedule, in IANA time zone database name format

`schedule_details`

(optional) Details of a horizontal scaling schedule.

### DBMS_CLOUD_OCI_BDS_UPDATE_SCHEDULE_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type

Update details of a schedule based vertical autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_bds_update_schedule_based_vertical_scaling_policy_details_t`is a subtype of the`dbms_cloud_oci_bds_update_auto_scale_policy_details_t`type.

Fields

Field Description

`timezone`

(optional) The time zone of the execution schedule, in IANA time zone database name format

`schedule_details`

(optional) Details of a vertical scaling schedule.

### DBMS_CLOUD_OCI_BDS_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted remains in the IN_PROGRESS state until work is complete for that resource, at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'FAILED'

`identifier`

(required) The OCID of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_BDS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_bds_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_BDS_WORK_REQUEST_T Type

Description of the work request status.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`operation_type`

(required) The type of this work request.

Allowed values are: 'CREATE_BDS', 'UPDATE_BDS', 'DELETE_BDS', 'ADD_BLOCK_STORAGE', 'ADD_MASTER_NODES', 'ADD_UTILITY_NODES', 'ADD_WORKER_NODES', 'ADD_CLOUD_SQL', 'REMOVE_CLOUD_SQL', 'CHANGE_COMPARTMENT_FOR_BDS', 'CHANGE_SHAPE', 'UPDATE_INFRA', 'RESTART_NODE', 'REMOVE_NODE', 'CREATE_AUTOSCALE_CONFIG', 'UPDATE_AUTOSCALE_CONFIG', 'DELETE_AUTOSCALE_CONFIG', 'AUTOSCALE_CONFIG', 'AUTOSCALE_RUN', 'CREATE_API_KEY', 'DELETE_API_KEY', 'TEST_OBJECT_STORE_CONNECTION', 'CREATE_METASTORE_CONFIG', 'DELETE_METASTORE_CONFIG', 'UPDATE_METASTORE_CONFIG', 'ACTIVATE_METASTORE_CONFIG', 'TEST_METASTORE_CONFIG', 'PATCH_BDS', 'PATCH_ODH', 'PATCH_OS', 'STOP_BDS', 'START_BDS', 'ADD_KAFKA', 'REMOVE_KAFKA', 'EXECUTE_BOOTSTRAP_SCRIPT', 'ODH_SERVICE_CERTIFICATE_UPDATE'

`status`

(required) The status of this work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of this work request completed.

`time_accepted`

(required) The date and time the request was created, shown as an RFC 3339 formatted datetime string.

`time_started`

(optional) The time the request was started, shown as an RFC 3339 formatted datetime string.

`time_finished`

(optional) The time the object was finished, shown as an RFC 3339 formatted datetime string.

### DBMS_CLOUD_OCI_BDS_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured, shown as an RFC 3339 formatted datetime string.

### DBMS_CLOUD_OCI_BDS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written, shown as an RFC 3339 formatted datetime string.

- [BDS Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-A165ED5C-919D-45CF-B1F0-3EFD67B95932)
- [DBMS_CLOUD_OCI_BDS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B1729733-5D22-4C97-A5E2-AC0BD1ED817D)
- [DBMS_CLOUD_OCI_BDS_ACTIVATE_BDS_METASTORE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9943CC94-46C4-4AB1-B997-52AA62F62A20)
- [DBMS_CLOUD_OCI_BDS_ADD_AUTO_SCALE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9F2A148C-F27F-4B8D-BBF0-6890E6E2D08B)
- [DBMS_CLOUD_OCI_BDS_METRIC_THRESHOLD_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B3706F58-A312-4E91-81E7-E5404A2CF7C8)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_METRIC_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-70F8D439-B6F3-4F9B-A73A-713326922DE2)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-16513AFB-267A-4540-AFE0-C9EF7026304B)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-74AEEF31-3ED6-4B8A-892C-72CDD68955F8)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-C29DD83A-4C66-4B21-98E6-75F26423767F)
- [DBMS_CLOUD_OCI_BDS_ADD_AUTO_SCALING_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-1862B0BA-A178-4AD6-BD3D-025D59721B32)
- [DBMS_CLOUD_OCI_BDS_ADD_BLOCK_STORAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-835D7F5C-2027-4D28-8610-9A1038DCB825)
- [DBMS_CLOUD_OCI_BDS_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-453B375D-2E5C-46C9-AE25-3C2AD73F91E4)
- [DBMS_CLOUD_OCI_BDS_ADD_CLOUD_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-BD0A7B30-BAB8-48A0-A6DB-B5BDB11F1256)
- [DBMS_CLOUD_OCI_BDS_ADD_KAFKA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-57931030-881C-41E2-9281-CDDDC385087B)
- [DBMS_CLOUD_OCI_BDS_ADD_MASTER_NODES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-547C385E-460E-487B-8043-8951EC32343D)
- [DBMS_CLOUD_OCI_BDS_METRIC_BASED_HORIZONTAL_SCALE_OUT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9433216C-D2C6-4C30-A456-B9C79888BBFE)
- [DBMS_CLOUD_OCI_BDS_METRIC_BASED_HORIZONTAL_SCALE_IN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-928C7D29-E31C-468C-88A8-6B6C6C021FF2)
- [DBMS_CLOUD_OCI_BDS_ADD_METRIC_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-93418390-2F9F-46C6-9A29-850CD428B733)
- [DBMS_CLOUD_OCI_BDS_METRIC_BASED_VERTICAL_SCALE_UP_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-85BED8D5-1980-48B6-A3EC-11D6231DF094)
- [DBMS_CLOUD_OCI_BDS_METRIC_BASED_VERTICAL_SCALE_DOWN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-78B5627E-4D8B-4024-BCA6-8D0F1450E455)
- [DBMS_CLOUD_OCI_BDS_ADD_METRIC_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-E94F9638-A42A-4E7B-B752-83639FE4F69C)
- [DBMS_CLOUD_OCI_BDS_HORIZONTAL_SCALING_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-2EB03B88-8B68-4330-BE2A-8ACB51128B1C)
- [DBMS_CLOUD_OCI_BDS_HORIZONTAL_SCALING_SCHEDULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-BF0F74FF-51BF-4460-A3A3-25E10E60FA77)
- [DBMS_CLOUD_OCI_BDS_ADD_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9A238A34-37A9-47F8-A8CC-A693C61E4620)
- [DBMS_CLOUD_OCI_BDS_VERTICAL_SCALING_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-CADCFB9E-CA79-456A-AE69-9CE073CB8295)
- [DBMS_CLOUD_OCI_BDS_VERTICAL_SCALING_SCHEDULE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-EC07DE81-D5B4-46FE-8045-C1A780638A1B)
- [DBMS_CLOUD_OCI_BDS_ADD_SCHEDULE_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-8708F368-4E1A-45E1-A50E-DBBEEB3F8320)
- [DBMS_CLOUD_OCI_BDS_ADD_UTILITY_NODES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B23FB9B2-6AF0-45A9-B985-DE22C2B4C8B5)
- [DBMS_CLOUD_OCI_BDS_ADD_WORKER_NODES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-6A4AFE2E-BB87-4201-B5DF-B9F325D89BD9)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-931193D0-66B4-4D98-9669-12271DB3F877)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-D50A9051-6BB2-42F0-8ACB-F164884282A3)
- [DBMS_CLOUD_OCI_BDS_AUTO_SCALING_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-856D02AE-C503-4D68-A017-A5A51BDF6813)
- [DBMS_CLOUD_OCI_BDS_BDS_API_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-77867CD3-AFA3-432F-80ED-3B3CD7A4F8BA)
- [DBMS_CLOUD_OCI_BDS_BDS_API_KEY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-911C2295-4FE0-42B8-83FE-39665B300D64)
- [DBMS_CLOUD_OCI_BDS_NETWORK_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-8A8496E7-9B96-4D97-9EBA-738715F923BA)
- [DBMS_CLOUD_OCI_BDS_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-A957F600-FFD8-4652-8BA7-B8F15F6AA66A)
- [DBMS_CLOUD_OCI_BDS_VOLUME_ATTACHMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-0A4E1753-629D-405D-BED6-95021B5C6BB1)
- [DBMS_CLOUD_OCI_BDS_VOLUME_ATTACHMENT_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-BB0D2FDC-2C39-4326-B5B5-C923973B8EBB)
- [DBMS_CLOUD_OCI_BDS_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-031D8EC9-CBCC-49A2-ACA0-7FC583FA8ECF)
- [DBMS_CLOUD_OCI_BDS_KERBEROS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-1FE190B9-7B43-4EA3-B26A-C46E2FFF6BAD)
- [DBMS_CLOUD_OCI_BDS_KERBEROS_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-231A40FD-82D2-4089-A64F-A3EA022B5918)
- [DBMS_CLOUD_OCI_BDS_CLOUD_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-3D6BE3FB-392B-4816-9607-8F55B2E79442)
- [DBMS_CLOUD_OCI_BDS_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-EF3CCFD8-DAF8-47A1-B7A2-E1EBDD95EA73)
- [DBMS_CLOUD_OCI_BDS_BDS_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-84233CA1-4577-4C02-82E3-1CC259290F8C)
- [DBMS_CLOUD_OCI_BDS_BDS_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-89545013-369D-4113-953F-1FC850945F8D)
- [DBMS_CLOUD_OCI_BDS_BDS_METASTORE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-60AC3160-45C1-4B4F-937A-048B6FFA0C3A)
- [DBMS_CLOUD_OCI_BDS_BDS_METASTORE_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-45E59B01-973A-47C9-AA8C-C619B5DF36E3)
- [DBMS_CLOUD_OCI_BDS_CERTIFICATE_SERVICE_INFO_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-6BB755E2-2DA6-4E93-A198-A252F6C35436)
- [DBMS_CLOUD_OCI_BDS_HOST_SPECIFIC_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-77AE8FFB-987E-49C5-BED3-3CB9DAE4EEE1)
- [DBMS_CLOUD_OCI_BDS_HOST_SPECIFIC_CERTIFICATE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-DFF39D3F-169F-4602-9F52-B410FC3718EF)
- [DBMS_CLOUD_OCI_BDS_CERTIFICATE_SERVICE_INFO_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-8DD8F52C-1F3A-4C73-8F67-5D98EB7B8B30)
- [DBMS_CLOUD_OCI_BDS_CHANGE_BDS_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-29D31C40-A9E6-48B9-ADDA-260A66DA1820)
- [DBMS_CLOUD_OCI_BDS_CHANGE_SHAPE_NODES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-DC1CB356-AA53-4325-8F41-CECB0A8A89A6)
- [DBMS_CLOUD_OCI_BDS_CHANGE_SHAPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-7FA4525A-4AC1-4D51-AF9B-8E18CD45FFCC)
- [DBMS_CLOUD_OCI_BDS_CREATE_BDS_API_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-AB4F32AC-1A36-4E38-BF26-9F9BC2117B16)
- [DBMS_CLOUD_OCI_BDS_CREATE_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-796225B8-6D57-4FE9-9DC9-62104F24EDB5)
- [DBMS_CLOUD_OCI_BDS_CREATE_NODE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-E562C704-2528-44F3-A2BF-4FA3EF60E602)
- [DBMS_CLOUD_OCI_BDS_CREATE_BDS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-4C09C5B1-150E-4B4C-81B7-BBA8E8BDFC21)
- [DBMS_CLOUD_OCI_BDS_CREATE_BDS_METASTORE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-1B1800B0-AED9-4BC3-850C-4FE0D4C17A47)
- [DBMS_CLOUD_OCI_BDS_TIME_AND_HORIZONTAL_SCALING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-91BB54FE-B240-4B02-9790-7D9D03DD8542)
- [DBMS_CLOUD_OCI_BDS_TIME_AND_HORIZONTAL_SCALING_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-1A291C0C-D913-459A-B160-BE3C2F77A236)
- [DBMS_CLOUD_OCI_BDS_DAY_BASED_HORIZONTAL_SCALING_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-EC7BBB24-CF74-45EE-B7A1-85F81E004F34)
- [DBMS_CLOUD_OCI_BDS_TIME_AND_VERTICAL_SCALING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-DF90A17D-7DAE-4437-AF9C-96A63167E3C4)
- [DBMS_CLOUD_OCI_BDS_TIME_AND_VERTICAL_SCALING_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-6FDDD0CE-6D2A-484D-BCC0-92969577CACF)
- [DBMS_CLOUD_OCI_BDS_DAY_BASED_VERTICAL_SCALING_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-727D1B24-3296-45E8-BA80-D306D32D4DBC)
- [DBMS_CLOUD_OCI_BDS_DEFAULT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B6B9EDC4-BAFB-47F7-8C65-1A56C57E5DF7)
- [DBMS_CLOUD_OCI_BDS_DISABLE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9E7DC0DC-9A9A-40F7-B4C4-1DD1D856089F)
- [DBMS_CLOUD_OCI_BDS_HOST_CERT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-4556B30D-3C49-418F-BBA4-6E20D3475AB0)
- [DBMS_CLOUD_OCI_BDS_HOST_CERT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-93C0B2F7-C930-46D5-8A15-FBEE4078DF87)
- [DBMS_CLOUD_OCI_BDS_ENABLE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9D1246D3-3967-418D-9435-4448096B1E84)
- [DBMS_CLOUD_OCI_BDS_EXECUTE_BOOTSTRAP_SCRIPT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-54EFABBA-AC60-476F-94E2-A44CA3348A83)
- [DBMS_CLOUD_OCI_BDS_INSTALL_OS_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B8914DFE-88F9-4943-A7C5-9AE1102941A0)
- [DBMS_CLOUD_OCI_BDS_INSTALL_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-8F86C309-9AB0-4BDE-9EF3-F8F34A6EE0D7)
- [DBMS_CLOUD_OCI_BDS_METRIC_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-0049FDBB-10B8-4660-B032-8905D95ECD00)
- [DBMS_CLOUD_OCI_BDS_METRIC_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-08F43334-DBA7-407C-9375-35EC9E4CB591)
- [DBMS_CLOUD_OCI_BDS_OS_PATCH_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-E2248B1B-EDB1-47FD-BA6D-9AAFDE61F692)
- [DBMS_CLOUD_OCI_BDS_OS_PATCH_PACKAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9519638F-C648-41C3-BF28-F33C910E0BF1)
- [DBMS_CLOUD_OCI_BDS_OS_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-BED6513F-B202-43BE-94FB-CFF70B5C7D2C)
- [DBMS_CLOUD_OCI_BDS_OS_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-53E6AE1D-02FE-4BEB-A60D-C74BDC79C844)
- [DBMS_CLOUD_OCI_BDS_PATCH_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-81735541-6C18-460A-B298-322A2C9DBD68)
- [DBMS_CLOUD_OCI_BDS_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-35829535-BD2C-4297-B5B6-7AD0799FF8E2)
- [DBMS_CLOUD_OCI_BDS_REMOVE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-A7D870ED-A500-4C3C-A32A-ECC9E5A0005C)
- [DBMS_CLOUD_OCI_BDS_REMOVE_CLOUD_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-4D946DD4-1B2C-4652-9E3C-7BA2A4F2CE0E)
- [DBMS_CLOUD_OCI_BDS_REMOVE_KAFKA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-C2E86958-7673-4EED-B115-65762250FA71)
- [DBMS_CLOUD_OCI_BDS_REMOVE_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-178085B6-234A-4555-A21D-E54D58DE92A7)
- [DBMS_CLOUD_OCI_BDS_RENEW_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-033A8861-F2EF-49DA-BA26-FF46D7E2E6A0)
- [DBMS_CLOUD_OCI_BDS_RESTART_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-06011E41-1378-4458-8DE0-D30B13409E38)
- [DBMS_CLOUD_OCI_BDS_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-22E61992-A038-40E3-9CC3-FD445D0F6411)
- [DBMS_CLOUD_OCI_BDS_SCHEDULE_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B8043B7E-7FED-4ECA-A52C-1A2C60F16E2D)
- [DBMS_CLOUD_OCI_BDS_START_BDS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B0FCEA6E-5878-4712-9989-CCF88A539893)
- [DBMS_CLOUD_OCI_BDS_STOP_BDS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-B036242C-E094-477A-827B-2C8AE45C38E9)
- [DBMS_CLOUD_OCI_BDS_TEST_BDS_METASTORE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-6F0F58BF-8B46-4E81-991B-87034662CB47)
- [DBMS_CLOUD_OCI_BDS_TEST_BDS_OBJECT_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-0B23A8B8-9FF7-4359-AE45-A3AE66AFA182)
- [DBMS_CLOUD_OCI_BDS_UPDATE_AUTO_SCALE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-55FE373B-651B-4C3A-8B63-57B9B1C73F3D)
- [DBMS_CLOUD_OCI_BDS_UPDATE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-CA08743B-832C-48B5-ACCF-AB35DD722D14)
- [DBMS_CLOUD_OCI_BDS_UPDATE_BDS_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-04285828-3984-453B-AB87-1D37736BA251)
- [DBMS_CLOUD_OCI_BDS_UPDATE_BDS_METASTORE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-EA03D66F-48A9-4AFC-A601-B175481B8CDD)
- [DBMS_CLOUD_OCI_BDS_UPDATE_METRIC_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-1BD532B7-71D5-4C68-9338-D34BF414516B)
- [DBMS_CLOUD_OCI_BDS_UPDATE_METRIC_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9BCB4196-E21E-444A-9300-B8B6BDD47B7C)
- [DBMS_CLOUD_OCI_BDS_UPDATE_SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-49570B63-E670-497B-929A-18CCD47ED006)
- [DBMS_CLOUD_OCI_BDS_UPDATE_SCHEDULE_BASED_VERTICAL_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-F03BAA8D-07A7-4020-B14D-EF797911CCA3)
- [DBMS_CLOUD_OCI_BDS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-BD6A591E-7B3C-4844-8A29-10E75BEE8B40)
- [DBMS_CLOUD_OCI_BDS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-4D1AFF3D-A525-46D3-8518-B10101B9A130)
- [DBMS_CLOUD_OCI_BDS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-FB4EFA0D-E0C3-420E-A166-21F34B343E42)
- [DBMS_CLOUD_OCI_BDS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-9C21FD9E-251E-4CDA-A478-8BA1917B7914)
- [DBMS_CLOUD_OCI_BDS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/bds_t.html#ADSDK-GUID-80D28001-0D15-4711-9D0B-24AF13AF4A05)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
