# Autoscaling Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#dcoc-content-body)

## Autoscaling Common Types

### DBMS_CLOUD_OCI_AUTOSCALING_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_AUTOSCALING_ACTION_T Type

The action to take when autoscaling is triggered.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of action to take.

Allowed values are: 'CHANGE_COUNT_BY'

`value`

(required) To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of instances), provide a negative value.

### DBMS_CLOUD_OCI_AUTOSCALING_RESOURCE_T Type

A resource that is managed by an autoscaling configuration. The only supported type is `instancePool`. Each instance pool can have one autoscaling configuration.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of resource.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource that is managed by the autoscaling configuration.

### DBMS_CLOUD_OCI_AUTOSCALING_CAPACITY_T Type

Capacity limits for the instance pool.

Syntax
```

```

Fields

Field Description

`l_max`

(optional) For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed to increase to (scale out). For a schedule-based autoscaling policy, this value is not used.

`l_min`

(optional) For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed to decrease to (scale in). For a schedule-based autoscaling policy, this value is not used.

`l_initial`

(optional) For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the limits that you set. For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule that's defined in the autoscaling policy.

### DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_POLICY_T Type

Autoscaling policies define the criteria that trigger autoscaling actions and the actions to take. An autoscaling policy is part of an autoscaling configuration. For more information, see[Autoscaling](https://docs.oracle.com/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm). You can create the following types of autoscaling policies: - **Schedule-based:** Autoscaling events take place at the specific times that you schedule. - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.

Syntax
```

```

Fields

Field Description

`l_capacity`

(optional) The capacity requirements of the autoscaling policy.

`id`

(optional) The ID of the autoscaling policy that is assigned after creation.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`policy_type`

(required) The type of autoscaling policy.

`time_created`

(required) The date and time the autoscaling configuration was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`is_enabled`

(optional) Whether the autoscaling policy is enabled.

### DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_POLICY_TBL Type

Nested table type of dbms_cloud_oci_autoscaling_auto_scaling_policy_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_CONFIGURATION_T Type

An autoscaling configuration lets you dynamically scale the resources in a Compute instance pool. For more information, see[Autoscaling](https://docs.oracle.com/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the autoscaling configuration.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`cool_down_in_seconds`

(optional) For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default. The cooldown period starts when the instance pool reaches the running state. For schedule-based autoscaling policies, this value is not used.

`is_enabled`

(optional) Whether the autoscaling configuration is enabled.

`l_resource`

(required)

`policies`

(required) Autoscaling policy definitions for the autoscaling configuration. An autoscaling policy defines the criteria that trigger autoscaling actions and the actions to take.

`time_created`

(required) The date and time the autoscaling configuration was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`max_resource_count`

(optional) The maximum number of resources to scale out to.

`min_resource_count`

(optional) The minimum number of resources to scale in to.

### DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_CONFIGURATION_SUMMARY_T Type

Summary information for an autoscaling configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the autoscaling configuration.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`cool_down_in_seconds`

(optional) For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default. The cooldown period starts when the instance pool reaches the running state. For schedule-based autoscaling policies, this value is not used.

`is_enabled`

(optional) Whether the autoscaling configuration is enabled.

`l_resource`

(required)

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`time_created`

(required) The date and time the autoscaling configuration was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_POLICY_SUMMARY_T Type

Summary information for an autoscaling policy.

Syntax
```

```

Fields

Field Description

`id`

(required) The ID of the autoscaling policy that is assigned after creation.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`policy_type`

(required) The type of autoscaling policy.

`is_enabled`

(optional) Whether the autoscaling policy is enabled.

### DBMS_CLOUD_OCI_AUTOSCALING_CHANGE_AUTO_SCALING_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the autoscaling configuration to.

### DBMS_CLOUD_OCI_AUTOSCALING_THRESHOLD_T Type

Syntax
```

```

Fields

Field Description

`operator`

(required) The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).

Allowed values are: 'GT', 'GTE', 'LT', 'LTE'

`value`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_METRIC_T Type

Metric and threshold details for triggering an autoscaling action.

Syntax
```

```

Fields

Field Description

`metric_type`

(required)

Allowed values are: 'CPU_UTILIZATION', 'MEMORY_UTILIZATION'

`threshold`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_CONDITION_T Type

A rule that defines a specific autoscaling action to take (scale in or scale out) and the metric that triggers that action.

Syntax
```

```

Fields

Field Description

`action`

(required)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`id`

(optional) ID of the condition that is assigned after creation.

`metric`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_AUTO_SCALING_POLICY_DETAILS_T Type

Creation details for an autoscaling policy. You can create the following types of autoscaling policies: - **Schedule-based:** Autoscaling events take place at the specific times that you schedule. - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold. An autoscaling configuration can either have multiple schedule-based autoscaling policies, or one threshold-based autoscaling policy.

Syntax
```

```

Fields

Field Description

`l_capacity`

(optional) The capacity requirements of the autoscaling policy.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`policy_type`

(required) The type of autoscaling policy.

`is_enabled`

(optional) Whether the autoscaling policy is enabled.

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_AUTO_SCALING_POLICY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_autoscaling_create_auto_scaling_policy_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type

Creation details for an autoscaling configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the autoscaling configuration.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`cool_down_in_seconds`

(optional) For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default. The cooldown period starts when the instance pool reaches the running state. For schedule-based autoscaling policies, this value is not used.

`is_enabled`

(optional) Whether the autoscaling configuration is enabled.

`policies`

(required)

`l_resource`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_CONDITION_DETAILS_T Type

Creation details for a condition in a threshold-based autoscaling policy.

Syntax
```

```

Fields

Field Description

`action`

(required)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`metric`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_EXECUTION_SCHEDULE_T Type

An execution schedule for an autoscaling policy.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of execution schedule.

`timezone`

(required) The time zone for the execution schedule.

Allowed values are: 'UTC'

### DBMS_CLOUD_OCI_AUTOSCALING_RESOURCE_ACTION_T Type

An action that can be executed against a resource.

Syntax
```

```

Fields

Field Description

`action_type`

(optional) The type of resource action.

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_SCHEDULED_POLICY_DETAILS_T Type

Creation details for a schedule-based autoscaling policy. In a schedule-based autoscaling policy, an autoscaling action is triggered at the scheduled execution time.

Syntax
```

```

`dbms_cloud_oci_autoscaling_create_scheduled_policy_details_t`is a subtype of the`dbms_cloud_oci_autoscaling_create_auto_scaling_policy_details_t`type.

Fields

Field Description

`execution_schedule`

(required)

`resource_action`

(optional)

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_CONDITION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_autoscaling_create_condition_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AUTOSCALING_CREATE_THRESHOLD_POLICY_DETAILS_T Type

Creation details for a threshold-based autoscaling policy. In a threshold-based autoscaling policy, an autoscaling action is triggered when a performance metric meets or exceeds a threshold.

Syntax
```

```

`dbms_cloud_oci_autoscaling_create_threshold_policy_details_t`is a subtype of the`dbms_cloud_oci_autoscaling_create_auto_scaling_policy_details_t`type.

Fields

Field Description

`rules`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_CRON_EXECUTION_SCHEDULE_T Type

An autoscaling execution schedule that uses a cron expression.

Syntax
```

```

`dbms_cloud_oci_autoscaling_cron_execution_schedule_t`is a subtype of the`dbms_cloud_oci_autoscaling_execution_schedule_t`type.

Fields

Field Description

`expression`

(required) A cron expression that represents the time at which to execute the autoscaling policy. Cron expressions have this format: `&lt;second&gt; &lt;minute&gt; &lt;hour&gt; &lt;day of month&gt; &lt;month&gt; &lt;day of week&gt; &lt;year&gt;` You can use special characters that are supported with the Quartz cron implementation. You must specify `0` as the value for seconds. Example: `0 15 10 ? * *`

### DBMS_CLOUD_OCI_AUTOSCALING_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_AUTOSCALING_INSTANCE_POOL_RESOURCE_T Type

A Compute instance pool.

Syntax
```

```

`dbms_cloud_oci_autoscaling_instance_pool_resource_t`is a subtype of the`dbms_cloud_oci_autoscaling_resource_t`type.

### DBMS_CLOUD_OCI_AUTOSCALING_RESOURCE_POWER_ACTION_T Type

A power action against a resource.

Syntax
```

```

`dbms_cloud_oci_autoscaling_resource_power_action_t`is a subtype of the`dbms_cloud_oci_autoscaling_resource_action_t`type.

Fields

Field Description

`action`

(required)

Allowed values are: 'STOP', 'START', 'SOFTRESET', 'RESET'

### DBMS_CLOUD_OCI_AUTOSCALING_SCHEDULED_POLICY_T Type

An autoscaling policy that defines execution schedules for an autoscaling configuration.

Syntax
```

```

`dbms_cloud_oci_autoscaling_scheduled_policy_t`is a subtype of the`dbms_cloud_oci_autoscaling_auto_scaling_policy_t`type.

Fields

Field Description

`execution_schedule`

(required) The schedule for executing the autoscaling policy.

`resource_action`

(optional)

### DBMS_CLOUD_OCI_AUTOSCALING_CONDITION_TBL Type

Nested table type of dbms_cloud_oci_autoscaling_condition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AUTOSCALING_THRESHOLD_POLICY_T Type

An autoscaling policy that defines threshold-based rules for an autoscaling configuration.

Syntax
```

```

`dbms_cloud_oci_autoscaling_threshold_policy_t`is a subtype of the`dbms_cloud_oci_autoscaling_auto_scaling_policy_t`type.

Fields

Field Description

`rules`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`is_enabled`

(optional) Whether the autoscaling configuration is enabled.

`cool_down_in_seconds`

(optional)

### DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_AUTO_SCALING_POLICY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`l_capacity`

(optional) The capacity requirements of the autoscaling policy.

`policy_type`

(required) Indicates the type of autoscaling policy.

`is_enabled`

(optional) Whether the autoscaling policy is enabled.

### DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_CONDITION_DETAILS_T Type

Update details for a condition in a threshold-based autoscaling policy.

Syntax
```

```

Fields

Field Description

`action`

(required)

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`metric`

(required)

### DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_SCHEDULED_POLICY_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_autoscaling_update_scheduled_policy_details_t`is a subtype of the`dbms_cloud_oci_autoscaling_update_auto_scaling_policy_details_t`type.

Fields

Field Description

`execution_schedule`

(optional) The schedule for executing the autoscaling policy.

`resource_action`

(optional)

### DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_CONDITION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_autoscaling_update_condition_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_THRESHOLD_POLICY_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_autoscaling_update_threshold_policy_details_t`is a subtype of the`dbms_cloud_oci_autoscaling_update_auto_scaling_policy_details_t`type.

Fields

Field Description

`rules`

(optional)

- [Autoscaling Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-56C0ADF7-8DCA-4B4E-8A11-37F8BB670733)
- [DBMS_CLOUD_OCI_AUTOSCALING_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-F6BCB793-DEF9-47AA-B6E5-C0B3FD9F730F)
- [DBMS_CLOUD_OCI_AUTOSCALING_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-739FC585-F217-49D7-926D-6807F90A1A61)
- [DBMS_CLOUD_OCI_AUTOSCALING_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-598A9410-D49A-480D-ABD6-B07611B5AF09)
- [DBMS_CLOUD_OCI_AUTOSCALING_CAPACITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-46251786-C80E-403F-A921-E112B0524FC2)
- [DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-1583B413-C9CC-4604-B3DC-8593B53E45E8)
- [DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_POLICY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-11DDB110-C386-4B0D-B668-3E0BEB829AD0)
- [DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-7AA2603B-93AC-40CE-B7B9-0E2A707AFE1F)
- [DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-0C1935C4-38FB-4C98-A9E5-71AAF5CEB0B5)
- [DBMS_CLOUD_OCI_AUTOSCALING_AUTO_SCALING_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-0BD1AD4A-3ADA-48F4-95CD-EB75D5022095)
- [DBMS_CLOUD_OCI_AUTOSCALING_CHANGE_AUTO_SCALING_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-DA5FEA4F-2656-4D95-AFA1-65FA8B2A4CC8)
- [DBMS_CLOUD_OCI_AUTOSCALING_THRESHOLD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-E8154BA7-7EA9-4C90-BA05-7097F1A235D7)
- [DBMS_CLOUD_OCI_AUTOSCALING_METRIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-CFF52264-F8D2-4D41-AD93-74EB8585B47A)
- [DBMS_CLOUD_OCI_AUTOSCALING_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-25897FE6-854D-4202-808D-B7A9882FE6F3)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_AUTO_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-A352A9A9-CA03-4E2B-9C3A-1B63D2243E77)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_AUTO_SCALING_POLICY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-B3621DAB-375F-48DD-B57A-0F545D7545DB)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-4407BE33-ED22-4076-8A98-64A8C881259A)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_CONDITION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-4490E543-59E5-49EA-B377-4495F1F31458)
- [DBMS_CLOUD_OCI_AUTOSCALING_EXECUTION_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-8398F760-6960-43DA-81B9-6180A329EAD3)
- [DBMS_CLOUD_OCI_AUTOSCALING_RESOURCE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-1B88C119-CBE4-48DB-AAFD-5EF6D95360A6)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_SCHEDULED_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-F8FB8A6C-6A60-436D-97D0-5D16A6FE4038)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_CONDITION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-94CF75CE-B160-4F74-A758-EC990BCF818B)
- [DBMS_CLOUD_OCI_AUTOSCALING_CREATE_THRESHOLD_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-4295554E-6A8F-4C3E-A79B-49E6BD3DF2A8)
- [DBMS_CLOUD_OCI_AUTOSCALING_CRON_EXECUTION_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-4971FC5F-34D1-4289-9D19-3E5C1BC1C677)
- [DBMS_CLOUD_OCI_AUTOSCALING_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-7533763B-0A2F-4822-BF64-A256683FA665)
- [DBMS_CLOUD_OCI_AUTOSCALING_INSTANCE_POOL_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-74AB6B68-53E4-44E4-9FBB-D3DEA0D8B9FE)
- [DBMS_CLOUD_OCI_AUTOSCALING_RESOURCE_POWER_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-6E191465-3026-4755-9C07-62DB4323AA08)
- [DBMS_CLOUD_OCI_AUTOSCALING_SCHEDULED_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-D1B6E09D-E3D9-4131-A697-FF1E8B4104CF)
- [DBMS_CLOUD_OCI_AUTOSCALING_CONDITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-A4F7FB9F-DD59-4367-A16A-5D5823BA1BDF)
- [DBMS_CLOUD_OCI_AUTOSCALING_THRESHOLD_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-EFE57243-95BC-4D01-A629-ED68D32177A0)
- [DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_AUTO_SCALING_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-4F726217-008E-476F-94FA-53C63E3CA21A)
- [DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_AUTO_SCALING_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-3EC819F6-7C3F-42E5-9C30-7B13D922845B)
- [DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_CONDITION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-D1CD97F0-8B50-4B0E-83EC-36A86F14B0AE)
- [DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_SCHEDULED_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-DDE78F6B-76DD-4CC1-8E24-158A25B31D53)
- [DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_CONDITION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-C0F08553-1855-4386-BBBA-5D760545DD72)
- [DBMS_CLOUD_OCI_AUTOSCALING_UPDATE_THRESHOLD_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/autoscaling_t.html#ADSDK-GUID-B0709A42-E4F1-4664-ABE2-5E9213E587C6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
