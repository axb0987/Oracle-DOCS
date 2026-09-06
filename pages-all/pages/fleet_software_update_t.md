# Fleet Software Update Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#dcoc-content-body)

## Fleet Software Update Common Types

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ACTIVE_CYCLE_DETAILS_T Type

Active Exadata Fleet Update Cycle resource for this Collection. Object would be null if there is no active Cycle.

Syntax
```

```

Fields

Field Description

`id`

(optional) OCID of the active Exadata Fleet Update Cycle resource.

`display_name`

(optional) Display name of the active Exadata Fleet Update Cycle resource.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_ENTRY_T Type

Details to specify a target to add or remove from a Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) Resource entity type

Allowed values are: 'DATABASE', 'VMCLUSTER', 'CLOUDVMCLUSTER'

`identifier`

(required) Resource identifier OCID

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_target_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ADD_FSU_COLLECTION_TARGETS_DETAILS_T Type

Add Targets to a Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`targets`

(required) List of Targets to add into the Exadata Fleet Update Collection.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_SCHEDULE_DETAILS_T Type

Scheduling related details for the Exadata Fleet Update Action. The specified time should not conflict with existing Exadata Infrastructure maintenance windows. Null scheduleDetails would execute the Exadata Fleet Update Action as soon as possible.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of scheduling strategy to use for Fleet Patching Update Action execution.

Allowed values are: 'START_TIME'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_PROGRESS_DETAILS_T Type

Progress of the Action in execution. If the Exadata Fleet Update Action has not started yet, this will be omitted.

Syntax
```

```

Fields

Field Description

`in_progress_targets`

(optional) Number of targets with jobs in progress.

`completed_targets`

(optional) Number of targets with completed jobs.

`failed_targets`

(optional) Number of targets with failed jobs.

`waiting_targets`

(optional) Number of targets with jobs waiting for batch to execute or for user to resume.

`total_targets`

(optional) Total number of targets impacted by Exadata Fleet Update Action.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_T Type

Exadata Fleet Update Action resource details.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Action.

`display_name`

(optional) Exadata Fleet Update Action display name.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) Type of Exadata Fleet Update Action.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`time_created`

(required) The date and time the Action was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the Action was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the Action was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The date and time the Action was last updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Action.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'UPDATING', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'UNKNOWN', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_ACTION_T Type

Apply Exadata Fleet Update Action details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_apply_action_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_SUMMARY_T Type

Exadata Fleet Update Action summary.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Action.

`display_name`

(optional) Exadata Fleet Update Action display name.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) Type of Exadata Fleet Update Action.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`time_created`

(required) The date and time the Action was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the Action was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the Action was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The date and time the Action was last updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Action.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'UPDATING', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'UNKNOWN', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_ACTION_SUMMARY_T Type

Apply Exadata Fleet Update Action summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_apply_action_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_summary_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_JOB_PROGRESS_DETAILS_T Type

Details about the Exadata Fleet Update Job progress.

Syntax
```

```

Fields

Field Description

`progress_of_operation`

(optional) Percentage of progress against the total to complete the operation.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_T Type

Exadata Fleet Update Job resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Job.

`display_name`

(optional) Exadata Fleet Update Job display name.

`l_type`

(required) Exadata Fleet Update Job type.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`compartment_id`

(required) Compartment Identifier, this will map to the owner Exadata Fleet Update Action resource.

`fsu_action_id`

(required) OCID of the Exadata Fleet Update Action that this job is part of.

`progress`

(optional)

`time_created`

(required) The time the Exadata Fleet Update Job was created. An RFC3339 formatted datetime string.

`time_started`

(optional) The time the Exadata Fleet Update Job started execution. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Exadata Fleet Update Job was updated. An RFC3339 formatted datetime string.

`time_finished`

(optional) The time the Exadata Fleet Update Job completed execution. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Job.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'UNKNOWN', 'TERMINATED', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'WAITING', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_FSU_JOB_T Type

Apply Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_apply_fsu_job_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_t`type.

Fields

Field Description

`fsu_collection_id`

(required) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(required) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_JOB_PROGRESS_T Type

Summary of progress for the Exadata Fleet Update Job.

Syntax
```

```

Fields

Field Description

`progress_of_operation`

(optional) Percentage of progress against the total to complete the operation.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_SUMMARY_T Type

Exadata Fleet Update Job resource.

Syntax
```

```

Fields

Field Description

`id`

(optional) OCID identifier for the Exadata Fleet Update Job.

`display_name`

(optional) Exadata Fleet Update Job display name.

`l_type`

(required) Exadata Fleet Update Job type.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`compartment_id`

(optional) Compartment Identifier, this will map to the owner Exadata Fleet Update Action resource.

`fsu_action_id`

(optional) OCID of the Exadata Fleet Update Action that this job is part of.

`progress`

(optional)

`time_created`

(optional) The time the Exadata Fleet Update Job was created. An RFC3339 formatted datetime string.

`time_started`

(optional) The time the Exadata Fleet Update Job started execution. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Exadata Fleet Update Job was updated. An RFC3339 formatted datetime string.

`time_finished`

(optional) The time the Exadata Fleet Update Job completed execution. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Job.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'UNKNOWN', 'TERMINATED', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'WAITING', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_FSU_JOB_SUMMARY_T Type

Summary of Apply Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_apply_fsu_job_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_summary_t`type.

Fields

Field Description

`fsu_collection_id`

(optional) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(optional) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_BATCHING_STRATEGY_DETAILS_T Type

Batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Supported batching strategies.

Allowed values are: 'SEQUENTIAL', 'FIFTY_FIFTY', 'SERVICE_AVAILABILITY_FACTOR', 'NON_ROLLING'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_ACTION_COMPARTMENT_DETAILS_T Type

Compartment to move the Exadata Fleet Update Action to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_COLLECTION_COMPARTMENT_DETAILS_T Type

Compartment to move the Exadata Fleet Update Collection to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_CYCLE_COMPARTMENT_DETAILS_T Type

Compartment to move the Exadata Fleet Update Cycle to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_DISCOVERY_COMPARTMENT_DETAILS_T Type

Compartment to move the Exadata Fleet Update Discovery to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_ACTION_T Type

Cleanup Exadata Fleet Update Action details. For a 'DB' Collection, Cleanup Action will attempt to remove unused source DBHomes for a completed Maintenance Cycle.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_cleanup_action_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_ACTION_SUMMARY_T Type

Cleanup Exadata Fleet Update Action summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_cleanup_action_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_summary_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_FSU_JOB_T Type

Cleanup Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_cleanup_fsu_job_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_t`type.

Fields

Field Description

`fsu_collection_id`

(required) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(required) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_FSU_JOB_SUMMARY_T Type

Summary of Cleanup Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_cleanup_fsu_job_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_summary_t`type.

Fields

Field Description

`fsu_collection_id`

(optional) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(optional) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_GOAL_VERSION_DETAILS_T Type

Goal version or image details for the Exadata Fleet Update Cycle.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of goal target version specified

Allowed values are: 'VERSION', 'IMAGE_ID'

`home_policy`

(optional) Goal home policy to use when Staging the Goal Version during patching. CREATE_NEW: Create a new DBHome (for Database Collections) for the specified image or version. USE_EXISTING: All database targets in the same VMCluster or CloudVmCluster will be moved to a shared database home. If an existing home for the selected image or version is not found in the VM Cluster for a target database, then a new home will be created. If more than one existing home for the selected image is found, then the home with the least number of databases will be used. If multiple homes have the least number of databases, then a home will be selected at random.

Allowed values are: 'CREATE_NEW', 'USE_EXISTING'

`new_home_prefix`

(optional) Prefix name used for new DB home resources created as part of the Stage Action. Format: &lt;specified_prefix&gt;_&lt;timestamp&gt; If not specified, a default OCI DB home resource will be generated for the new DB home resources created.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_BATCHING_STRATEGY_DETAILS_T Type

Batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Supported batching strategies.

Allowed values are: 'SEQUENTIAL', 'FIFTY_FIFTY', 'SERVICE_AVAILABILITY_FACTOR', 'NON_ROLLING'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_SCHEDULE_DETAILS_T Type

Scheduling related details for the Exadata Fleet Update Action during create operations. The specified time should not conflict with existing Exadata Infrastructure maintenance windows. Null scheduleDetails for Stage and Apply Actions in Exadata Fleet Update Cycle creation would not create Actions. Null scheduleDetails for CreateAction would execute the Exadata Fleet Update Action as soon as possible.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of scheduling strategy to use for Fleet Patching Update Action execution.

Allowed values are: 'START_TIME'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLONE_FSU_CYCLE_DETAILS_T Type

Details for cloning an existing Exadata Fleet Update Cycle resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Cycle display name.

`compartment_id`

(optional) Compartment Identifier.

`fsu_collection_id`

(optional) OCID identifier for the Collection ID the Exadata Fleet Update Cycle will be assigned to. If not specified, it will be assigned to the same Collection as the source Exadata Fleet Update Cycle.

`goal_version_details`

(required)

`batching_strategy`

(optional)

`stage_action_schedule`

(optional)

`apply_action_schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_DETAILS_T Type

Details of target member of a Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) Resource EntityType for the target in the Exadata Fleet Update Collection.

Allowed values are: 'DATABASE', 'VMCLUSTER', 'CLOUDVMCLUSTER'

`id`

(optional) OCID of the target resource in the Exadata Fleet Update Collection.

`compartment_id`

(optional) Compartment identifier of the target.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLOUD_VM_CLUSTER_TARGET_SUMMARY_T Type

Details of a CloudVmCluster target member of a Exadata Fleet Update Collection. Stored references of the resource documented in https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudVmCluster/

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_cloud_vm_cluster_target_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_target_details_t`type.

Fields

Field Description

`infrastructure_id`

(optional) OCID of the related Exadata Infrastructure or Cloud Exadata Infrastructure resource.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_ACTION_DETAILS_T Type

Exadata Fleet Update Action resource details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Action display name.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) Type of Exadata Fleet Update Action.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_APPLY_ACTION_DETAILS_T Type

Apply Exadata Fleet Update Action creation details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_apply_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_action_details_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_CLEANUP_ACTION_DETAILS_T Type

Cleanup Exadata Fleet Update Action creation details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_cleanup_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_action_details_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FLEET_DISCOVERY_DETAILS_T Type

Supported fleet discovery strategies for DB Collections. If specified on an Update Collection request, this will re-discover the targets of the Collection.

Syntax
```

```

Fields

Field Description

`strategy`

(required) Possible fleet discovery strategies.

Allowed values are: 'SEARCH_QUERY', 'FILTERS', 'TARGET_LIST', 'DISCOVERY_RESULTS'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_COLLECTION_DETAILS_T Type

The information about new Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Collection Identifier.

`l_type`

(required) Collection type. DB: Only Database entity type resources allowed. GI: CloudVMCluster and VMCluster entity type resources allowed.

Allowed values are: 'DB', 'GI'

`service_type`

(required) Exadata service type for the target resource members.

Allowed values are: 'EXACS', 'EXACC'

`compartment_id`

(required) Compartment Identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_DB_FSU_COLLECTION_DETAILS_T Type

Details to create a 'DB' type Exadata Fleet Update Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_db_fsu_collection_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_collection_details_t`type.

Fields

Field Description

`source_major_version`

(required) Database Major Version of targets to be included in the Exadata Fleet Update Collection. https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbVersionSummary/ListDbVersions Only Database targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

Allowed values are: 'DB_11204', 'DB_121', 'DB_122', 'DB_18', 'DB_19'

`fleet_discovery`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FIFTY_FIFTY_BATCHING_STRATEGY_DETAILS_T Type

Fifty-Fifty batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_fifty_fifty_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_batching_strategy_details_t`type.

Fields

Field Description

`is_wait_for_batch_resume`

(optional) True to wait for customer to resume the Apply Action once the first half is done. False to automatically patch the second half.

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_CYCLE_DETAILS_T Type

Exadata Fleet Update Cycle resource creation details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Cycle display name.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) Type of Exadata Fleet Update Cycle.

Allowed values are: 'PATCH'

`fsu_collection_id`

(required) OCID identifier for the Collection ID the Exadata Fleet Update Cycle will be assigned to.

`goal_version_details`

(required)

`batching_strategy`

(optional)

`stage_action_schedule`

(optional)

`apply_action_schedule`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DISCOVERY_DETAILS_T Type

Discovery filter details for search.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Exadata Fleet Update Discovery type.

Allowed values are: 'DB', 'GI'

`service_type`

(required) Exadata service type for the target resource members.

Allowed values are: 'EXACS', 'EXACC'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_DISCOVERY_DETAILS_T Type

The information about new Exadata Fleet Update Discovery resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Collection display name.

`compartment_id`

(required) Compartment Identifier.

`details`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FLEET_DISCOVERY_DETAILS_T Type

Supported fleet discovery strategies for GI Collections. If specified on an Update Collection request, this will re-discover the targets of the Collection.

Syntax
```

```

Fields

Field Description

`strategy`

(required) Possible fleet discovery strategies.

Allowed values are: 'SEARCH_QUERY', 'FILTERS', 'TARGET_LIST', 'DISCOVERY_RESULTS'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_GI_FSU_COLLECTION_DETAILS_T Type

Details to create a 'GI' type Exadata Fleet Update Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_gi_fsu_collection_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_collection_details_t`type.

Fields

Field Description

`source_major_version`

(required) Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Collection. Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

Allowed values are: 'GI_18', 'GI_19'

`fleet_discovery`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_NON_ROLLING_BATCHING_STRATEGY_DETAILS_T Type

Non-rolling batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_non_rolling_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_batching_strategy_details_t`type.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_PATCH_FSU_CYCLE_T Type

Patch Exadata Fleet Update Cycle resource creation details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_patch_fsu_cycle_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_cycle_details_t`type.

Fields

Field Description

`is_ignore_patches`

(optional) Ignore all patches between the source and target homes during patching.

`is_ignore_missing_patches`

(optional) List of patch IDs to ignore.

`max_drain_timeout_in_seconds`

(optional) Service drain timeout specified in seconds.

`is_keep_placement`

(optional) Ensure that services of administrator-managed Oracle RAC or Oracle RAC One databases are running on the same instances before and after the move operation.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_PRECHECK_ACTION_DETAILS_T Type

Precheck Exadata Fleet Update Action creation details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_precheck_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_action_details_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_DETAILS_T Type

Rollback details specified for the action.

Syntax
```

```

Fields

Field Description

`strategy`

(required) Rollback strategy to use. FAILED_JOBS: Rollback and remove targets which had a failure in their last job. LIST_OF_TARGETS: Rollback and remove a specific list of targets.

Allowed values are: 'FAILED_JOBS', 'LIST_OF_TARGETS'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_ROLLBACK_ACTION_DETAILS_T Type

Rollback Exadata Fleet Update Action creation details. This action will attempt to rollback the specified Targets according to strategy to the source target version prior to patching in this Exadata Fleet Update Cycle and remove them from the Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_rollback_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_action_details_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`details`

(required)

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_SEQUENTIAL_BATCHING_STRATEGY_DETAILS_T Type

Sequential batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_sequential_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_batching_strategy_details_t`type.

Fields

Field Description

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_SERVICE_AVAILABILITY_FACTOR_BATCHING_STRATEGY_DETAILS_T Type

Service Availability Factor batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_service_availability_factor_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_batching_strategy_details_t`type.

Fields

Field Description

`percentage`

(optional) Percentage of availability in the service during the Patch operation.

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_STAGE_ACTION_DETAILS_T Type

Stage Exadata Fleet Update Action creation details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_stage_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_fsu_action_details_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_START_TIME_SCHEDULE_DETAILS_T Type

Start time details for the Exadata Fleet Update Action. The specified time should not conflict with existing Exadata Infrastructure maintenance windows. If Stage and Apply Actions are created with a timeToStart specified during Exadata Fleet Update Cycle creation, Apply should be scheduled at least 24 hours after the start time of the Stage Action.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_create_start_time_schedule_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_create_schedule_details_t`type.

Fields

Field Description

`time_to_start`

(required) The date and time the Exadata Fleet Update Action is expected to start.[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DATABASE_TARGET_SUMMARY_T Type

Details of a Database target member of a Exadata Fleet Update Collection. Stored references of the resource documented in https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/Database/

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_database_target_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_target_details_t`type.

Fields

Field Description

`db_home_id`

(optional) OCID of the database home.

`vm_cluster_id`

(optional) OCID of the related VM Cluster or Cloud VM Cluster.

`infrastructure_id`

(optional) OCID of the related Exadata Infrastructure or Cloud Exadata Infrastructure resource.

`software_image_id`

(optional) OCID of the Database sofware image.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_T Type

Exadata Fleet Update Collection Resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Collection.

`display_name`

(required) Exadata Fleet Update Collection resource display name.

`l_type`

(required) Exadata Fleet Update Collection type.

Allowed values are: 'DB', 'GI'

`service_type`

(required) Exadata service type for the target resource members.

Allowed values are: 'EXACS', 'EXACC'

`compartment_id`

(required) Compartment Identifier

`active_fsu_cycle`

(optional)

`target_count`

(optional) Number of targets that are members of this Collection.

`time_created`

(required) The time the Exadata Fleet Update Collection was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Exadata Fleet Update Collection was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Collection.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_COLLECTION_T Type

'DB' type Exadata Fleet Update Collection details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_collection_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_collection_t`type.

Fields

Field Description

`source_major_version`

(required) Database Major Version of targets to be included in the Exadata Fleet Update Collection. https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbVersionSummary/ListDbVersions Only Database targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

Allowed values are: 'DB_11204', 'DB_121', 'DB_122', 'DB_18', 'DB_19'

`fleet_discovery`

(required)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FLEET_DISCOVERY_FILTER_T Type

Possible Discovery filters for Database targets.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of filters supported for Database targets discovery.

Allowed values are: 'COMPARTMENT_ID', 'VERSION', 'DB_NAME', 'DB_UNIQUE_NAME', 'DB_HOME_NAME', 'FREEFORM_TAG', 'DEFINED_TAG', 'RESOURCE_ID'

`l_mode`

(optional) INCLUDE or EXCLUDE the filter results in the discovery for DB targets. Supported for 'FSUCOLLECTION' RESOURCE_ID filter only.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_COMPARTMENT_ID_FILTER_T Type

List of Compartments to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_compartment_id_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`identifiers`

(required) List of Compartments OCIDs to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DEFINED_TAG_FILTER_ENTRY_T Type

Defined Tag filter entry.

Syntax
```

```

Fields

Field Description

`namespace`

(required) Defined tag namespace.

`key`

(required) Defined tag key.

`value`

(required) Defined tag value.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DEFINED_TAG_FILTER_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_defined_tag_filter_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_DEFINED_TAGS_FILTER_T Type

Defined tags to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_defined_tags_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`tags`

(required) Defined tags to include in the discovery.

`operator`

(optional) Type of join for each element in this filter.

Allowed values are: 'AND', 'OR'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_DISCOVERY_DETAILS_T Type

'DB' type Exadata Fleet Update Discovery details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_discovery_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_discovery_details_t`type.

Fields

Field Description

`source_major_version`

(required) Database Major Version of targets to be included in the Exadata Fleet Update Discovery results. https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbVersionSummary/ListDbVersions Only Database targets that match the version specified in this value would be added to the Exadata Fleet Update Discovery results.

Allowed values are: 'DB_11204', 'DB_121', 'DB_122', 'DB_18', 'DB_19'

`criteria`

(required)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_DISCOVERY_RESULTS_T Type

Collection built from the results of a Succeeded Fleet Software Update Discovery resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_discovery_results_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_details_t`type.

Fields

Field Description

`fsu_discovery_id`

(required) OCIDs of Fleet Software Update Discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FLEET_DISCOVERY_FILTER_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FILTERS_DISCOVERY_T Type

Collection discovery done from the results of the specified filters.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_filters_discovery_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_details_t`type.

Fields

Field Description

`filters`

(required) Filters to perform the target discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FREEFORM_TAG_FILTER_ENTRY_T Type

Freeform Tag filter entry.

Syntax
```

```

Fields

Field Description

`key`

(required) Freeform tag key.

`value`

(required) Freeform tag value.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FREEFORM_TAG_FILTER_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_freeform_tag_filter_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FREEFORM_TAGS_FILTER_T Type

Freeform tags to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_freeform_tags_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`tags`

(required) Freeform tags to include in the discovery.

`operator`

(optional) Type of join for each element in this filter.

Allowed values are: 'AND', 'OR'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_SUMMARY_T Type

Exadata Fleet Update Collection Resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Collection.

`display_name`

(required) Exadata Fleet Update Collection resource display name.

`l_type`

(required) Exadata Fleet Update Collection type.

Allowed values are: 'DB', 'GI'

`service_type`

(required) Exadata service type for the target resource members.

Allowed values are: 'EXACS', 'EXACC'

`compartment_id`

(required) Compartment Identifier

`active_fsu_cycle`

(optional)

`target_count`

(optional) Number of targets that are members of this Collection.

`time_created`

(required) The time the Exadata Fleet Update Collection was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Exadata Fleet Update Collection was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Collection.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'NEEDS_ATTENTION', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FSU_COLLECTION_SUMMARY_T Type

'DB' type Exadata Fleet Update Collection summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_fsu_collection_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_collection_summary_t`type.

Fields

Field Description

`source_major_version`

(required) Database Major Version of targets to be included in the Exadata Fleet Update Collection. https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbVersionSummary/ListDbVersions Only Database targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

Allowed values are: 'DB_11204', 'DB_121', 'DB_122', 'DB_18', 'DB_19'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_HOME_NAME_FILTER_T Type

Database home name to include in the discovery. '*' Wildcard is allowed for 'startsWith' or 'endsWith' filtering.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_home_name_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`names`

(required) List of Database home names to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_NAME_FILTER_T Type

Database name to include in the discovery. '*' Wildcard is allowed for 'startsWith' or 'endsWith' filtering.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_name_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`names`

(required) List of Database names to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_RESOURCE_ID_FILTER_T Type

Related resource Ids to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_resource_id_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`entity_type`

(required) Type of resource to match in the discovery.

Allowed values are: 'DATABASESOFTWAREIMAGE', 'DBHOME', 'EXADATAINFRASTRUCTURE', 'CLOUDEXADATAINFRASTRUCTURE', 'VMCLUSTER', 'CLOUDVMCLUSTER', 'FSUCOLLECTION'

`identifiers`

(required) Related resource Ids to include in the discovery. All must match the specified entityType.

`operator`

(optional) Type of join for each element in this filter.

Allowed values are: 'AND', 'OR'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_SEARCH_QUERY_DISCOVERY_T Type

Collection discovery done from the results of the specified Search Service query string.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_search_query_discovery_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_details_t`type.

Fields

Field Description

`query`

(required) OCI Search Service query string.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_TARGET_LIST_DISCOVERY_T Type

Collection discovery conformed by the specified list of targets.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_target_list_discovery_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_details_t`type.

Fields

Field Description

`targets`

(required) OCIDs of target database resources to include.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_UNIQUE_NAME_FILTER_T Type

Database unique name to include in the discovery. '*' Wildcard is allowed for 'startsWith' or 'endsWith' filtering.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_unique_name_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`names`

(required) List of Database unique names to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_VERSION_FILTER_T Type

Versions to include in the discovery. These should be under the Source Major Version of the Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_db_version_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_db_fleet_discovery_filter_t`type.

Fields

Field Description

`versions`

(required) List of Version strings to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DISCOVERY_DETAILS_SUMMARY_T Type

Summarized Discovery details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Exadata Fleet Update Discovery type.

Allowed values are: 'DB', 'GI'

`service_type`

(required) Exadata service type for the target resource members.

Allowed values are: 'EXACS', 'EXACC'

`criteria`

(optional) Criteria used for Exadata Fleet Update Discovery.

Allowed values are: 'SEARCH_QUERY', 'FILTERS'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ERROR_T Type

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

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FAILED_JOBS_ROLLBACK_DETAILS_T Type

FAILED_JOBS strategy rollback details. This strategy would only act-upon targets that had a failed job during patching.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_failed_jobs_rollback_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_rollback_details_t`type.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FIFTY_FIFTY_BATCHING_STRATEGY_DETAILS_T Type

Fifty-Fifty batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_fifty_fifty_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_batching_strategy_details_t`type.

Fields

Field Description

`is_wait_for_batch_resume`

(optional) True to wait for customer to resume the Apply Action once the first half is done. False to automatically patch the second half.

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_fsu_action_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_SUMMARY_COLLECTION_T Type

List of FsuActionSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of FsuActionSummary entries.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_fsu_collection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_SUMMARY_COLLECTION_T Type

List of FsuCollectionSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of FsuCollectionSummary entries.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NEXT_ACTION_TO_EXECUTE_DETAILS_T Type

Details of the next Exadata Fleet Update Action to execute in a Maintenance Cycle.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of Exadata Fleet Update Action

Allowed values are: 'STAGE', 'PRECHECK_STAGE', 'PRECHECK_APPLY', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`time_to_start`

(optional) The date and time the Exadata Fleet Update Action is expected to start. Null if no Action has been scheduled.[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NEXT_ACTION_TO_EXECUTE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_next_action_to_execute_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_T Type

Exadata Fleet Update Cycle resource details.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Cycle.

`display_name`

(optional) Exadata Fleet Update Cycle display name.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) Type of Exadata Fleet Update Cycle.

Allowed values are: 'PATCH'

`fsu_collection_id`

(required) OCID identifier for the Collection ID the Exadata Fleet Update Cycle is assigned to.

`collection_type`

(optional) Type of Collection this Exadata Fleet Update Cycle belongs to.

Allowed values are: 'DB', 'GI'

`executing_fsu_action_id`

(optional) OCID identifier for the Action that is currently in execution, if applicable.

`next_action_to_execute`

(optional) In this array all the possible actions will be listed. The first element is the suggested Action.

`last_completed_action`

(optional) The latest Action type that was completed in the Exadata Fleet Update Cycle. No value would indicate that the Cycle has not completed any Action yet.

Allowed values are: 'STAGE', 'PRECHECK_STAGE', 'PRECHECK_APPLY', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`goal_version_details`

(optional)

`batching_strategy`

(optional)

`stage_action_schedule`

(optional)

`apply_action_schedule`

(optional)

`time_created`

(required) The date and time the Exadata Fleet Update Cycle was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) The date and time the Exadata Fleet Update Cycle was updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the Exadata Fleet Update Cycle was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Cycle.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'IN_PROGRESS', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_SUMMARY_T Type

Exadata Fleet Update Cycle Summary.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Cycle.

`display_name`

(optional) Exadata Fleet Update Cycle display name.

`compartment_id`

(required) Compartment Identifier.

`l_type`

(required) Type of Exadata Fleet Update Cycle.

Allowed values are: 'PATCH'

`fsu_collection_id`

(required) OCID identifier for the Collection ID the Exadata Fleet Update Cycle is assigned to.

`collection_type`

(required) Type of Collection this Exadata Fleet Update Cycle belongs to.

Allowed values are: 'DB', 'GI'

`executing_fsu_action_id`

(optional) OCID identifier for the Action that is currently in execution, if applicable.

`next_action_to_execute`

(optional) In this array all the possible actions will be listed. The first element is the suggested Action.

`last_completed_action`

(optional) The latest Action type that was completed in the Exadata Fleet Update Cycle. No value would indicate that the Cycle has not completed any Action yet.

Allowed values are: 'STAGE', 'PRECHECK_STAGE', 'PRECHECK_APPLY', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`goal_version_details`

(required)

`time_created`

(required) The date and time the Exadata Fleet Update Cycle was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) The date and time the Exadata Fleet Update Cycle was updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the Exadata Fleet Update Cycle was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Cycle.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'IN_PROGRESS', 'FAILED', 'NEEDS_ATTENTION', 'SUCCEEDED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_fsu_cycle_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_SUMMARY_COLLECTION_T Type

List of FsuCycleSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of FsuCycleSummary entries.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_T Type

Exadata Fleet Update Discovery resource details.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Discovery.

`display_name`

(required) Exadata Fleet Update Discovery display name.

`compartment_id`

(required) Compartment Identifier.

`details`

(required)

`time_created`

(required) The date and time the Exadata Fleet Update Discovery was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) The date and time the Exadata Fleet Update Discovery was updated, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the Exadata Fleet Update Discovery was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Discovery.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_SUMMARY_T Type

Exadata Fleet Update Discovery Resource.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID identifier for the Exadata Fleet Update Discovery.

`display_name`

(required) Exadata Fleet Update Discovery display name.

`compartment_id`

(required) Compartment Identifier.

`details`

(required)

`time_created`

(required) The time the Exadata Fleet Update Discovery was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Exadata Fleet Update Discovery was updated. An RFC3339 formatted datetime string.

`time_finished`

(optional) The date and time the Exadata Fleet Update Discovery was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`lifecycle_state`

(required) The current state of the Exadata Fleet Update Discovery.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_fsu_discovery_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_SUMMARY_COLLECTION_T Type

List of FleetSoftwareUpdateDiscoverySummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of FleetSoftwareUpdateDiscoverySummary entries.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_fsu_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_COLLECTION_T Type

Results of a Exadata Fleet Update Job Summary listing. Contains FleetSoftwareUpdateJobSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_OUTPUT_SUMMARY_T Type

Job output summary line.

Syntax
```

```

Fields

Field Description

`message`

(required) Job output line.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_OUTPUT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_fsu_job_output_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_OUTPUT_SUMMARY_COLLECTION_T Type

Results of a Exadata Fleet Update Job output listing. Contains FleetSoftwareUpdateJobOutputSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_COLLECTION_T Type

Details to create a 'GI' type Exadata Fleet Update Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_collection_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_collection_t`type.

Fields

Field Description

`source_major_version`

(required) Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Collection. Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

Allowed values are: 'GI_18', 'GI_19'

`fleet_discovery`

(required)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FLEET_DISCOVERY_FILTER_T Type

Possible Discovery filters.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of filters supported for GI targets discovery.

Allowed values are: 'COMPARTMENT_ID', 'VERSION', 'FREEFORM_TAG', 'DEFINED_TAG', 'RESOURCE_ID'

`l_mode`

(optional) INCLUDE or EXCLUDE the filter results in the discovery for GI targets. Supported for 'FSUCOLLECTION' RESOURCE_ID filter only.

Allowed values are: 'INCLUDE', 'EXCLUDE'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_COMPARTMENT_ID_FILTER_T Type

List of Compartments to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_compartment_id_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_filter_t`type.

Fields

Field Description

`identifiers`

(required) List of Compartments OCIDs to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_DEFINED_TAGS_FILTER_T Type

Defined tags to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_defined_tags_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_filter_t`type.

Fields

Field Description

`tags`

(required) Defined tags to include in the discovery.

`operator`

(optional) Type of join for each element in this filter.

Allowed values are: 'AND', 'OR'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_DISCOVERY_DETAILS_T Type

Details to create a 'GI' type Exadata Fleet Update Discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_discovery_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_discovery_details_t`type.

Fields

Field Description

`source_major_version`

(required) Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Discovery results. Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Discovery results.

Allowed values are: 'GI_18', 'GI_19'

`criteria`

(required)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_DISCOVERY_RESULTS_T Type

Collection built from the results of a Succeeded Fleet Software Update Discovery resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_discovery_results_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_details_t`type.

Fields

Field Description

`fsu_discovery_id`

(required) OCIDs of Fleet Software Update Discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FLEET_DISCOVERY_FILTER_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FILTERS_DISCOVERY_T Type

Collection discovery done from the results of the specified filters.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_filters_discovery_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_details_t`type.

Fields

Field Description

`filters`

(required) Filters to perform the target discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FREEFORM_TAGS_FILTER_T Type

Freeform tags to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_freeform_tags_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_filter_t`type.

Fields

Field Description

`tags`

(required) Freeform tags to include in the discovery.

`operator`

(optional) Type of join for each element in this filter.

Allowed values are: 'AND', 'OR'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FSU_COLLECTION_SUMMARY_T Type

'GI' type Exadata Fleet Update Collection summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_fsu_collection_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_collection_summary_t`type.

Fields

Field Description

`source_major_version`

(required) Grid Infrastructure Major Version of targets to be included in the Exadata Fleet Update Collection. Only GI targets that match the version specified in this value would be added to the Exadata Fleet Update Collection.

Allowed values are: 'GI_18', 'GI_19'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_RESOURCE_ID_FILTER_T Type

Related resource Ids to include in the discovery.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_resource_id_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_filter_t`type.

Fields

Field Description

`entity_type`

(required) Type of resource to match in the discovery.

Allowed values are: 'EXADATAINFRASTRUCTURE', 'CLOUDEXADATAINFRASTRUCTURE', 'VMCLUSTER', 'CLOUDVMCLUSTER', 'FSUCOLLECTION'

`identifiers`

(required) Related resource Ids to include in the discovery. All must match the specified entityType.

`operator`

(optional) Type of join for each element in this filter.

Allowed values are: 'AND', 'OR'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_SEARCH_QUERY_DISCOVERY_T Type

Collection discovery done from the results of the specified Search Service query string.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_search_query_discovery_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_details_t`type.

Fields

Field Description

`query`

(required) OCI Search Service query string.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_TARGET_LIST_DISCOVERY_T Type

Collection discovery conformed by the specified list of targets.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_target_list_discovery_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_details_t`type.

Fields

Field Description

`targets`

(required) OCIDs of target resources to include. For EXACC service type Collections only VMClusters are allowed. For EXACS service type Collections only CloudVMClusters are allowed.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_VERSION_FILTER_T Type

Versions to include in the discovery. These should be under the Source Major Version of the Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_gi_version_filter_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_gi_fleet_discovery_filter_t`type.

Fields

Field Description

`versions`

(required) List of Versions strings to include in the discovery.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_IMAGE_ID_FSU_TARGET_DETAILS_T Type

Exadata Fleet Update Cycle Target Image Id details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_image_id_fsu_target_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_goal_version_details_t`type.

Fields

Field Description

`software_image_id`

(required) Target database software image OCID.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_LIST_OF_TARGETS_ROLLBACK_DETAILS_T Type

LIST_OF_TARGETS strategy rollback details. The specified list would only act-upon targets that had a failed job during patching.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_list_of_targets_rollback_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_rollback_details_t`type.

Fields

Field Description

`targets`

(required) OCIDs of targets to rollback.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NON_ROLLING_BATCHING_STRATEGY_DETAILS_T Type

Non-rolling batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_non_rolling_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_batching_strategy_details_t`type.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_BATCHING_STRATEGY_DETAILS_T Type

Batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Supported batching strategies.

Allowed values are: 'SEQUENTIAL', 'FIFTY_FIFTY', 'SERVICE_AVAILABILITY_FACTOR', 'NON_ROLLING', 'NONE'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NONE_BATCHING_STRATEGY_DETAILS_T Type

No batching strategy details. To specify during update Exadata Fleet Update Cycle operation and remove configured batching strategy.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_none_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_batching_strategy_details_t`type.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_SCHEDULE_DETAILS_T Type

Scheduling related details for the Exadata Fleet Update Action. The specified time should not conflict with existing Exadata Infrastructure maintenance windows. 'NONE' type scheduleDetails for UpdateAction would execute the Exadata Fleet Update Action as soon as possible.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of scheduling strategy to use for Fleet Patching Update Action execution.

Allowed values are: 'START_TIME', 'NONE'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NONE_SCHEDULE_DETAILS_T Type

Type used to remove previously stored scheduled details. The Action will be executed as soon as possible after the update completes. Used during Update operations.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_none_schedule_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_schedule_details_t`type.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PATCH_FSU_CYCLE_T Type

Patch Exadata Fleet Update Cycle resource details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_patch_fsu_cycle_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_cycle_t`type.

Fields

Field Description

`is_ignore_patches`

(optional) Ignore all patches between the source and target homes during patching.

`is_ignore_missing_patches`

(optional) List of bug numbers to ignore.

`max_drain_timeout_in_seconds`

(optional) Service drain timeout specified in seconds.

`is_keep_placement`

(optional) Ensure that services of administrator-managed Oracle RAC or Oracle RAC One databases are running on the same instances before and after the move operation.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_ACTION_T Type

Precheck Exadata Fleet Update Action details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_precheck_action_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_ACTION_SUMMARY_T Type

Precheck Exadata Fleet Update Action summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_precheck_action_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_summary_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_FSU_JOB_T Type

Precheck Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_precheck_fsu_job_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_t`type.

Fields

Field Description

`fsu_collection_id`

(required) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(required) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_FSU_JOB_SUMMARY_T Type

Summary of Precheck Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_precheck_fsu_job_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_summary_t`type.

Fields

Field Description

`fsu_collection_id`

(optional) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(optional) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_REMOVE_FSU_COLLECTION_TARGETS_DETAILS_T Type

Remove targets from a Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`removal_strategy`

(required) Strategy to follow for removal of targets: TARGET_IDS: Remove a list of targets

Allowed values are: 'TARGET_IDS'

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_ACTION_T Type

Rollback Exadata Fleet Update Action details. This would rollback the specified targets to the source version before patching and remove them from the Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_rollback_action_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

`details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_ACTION_SUMMARY_T Type

Rollback Exadata Fleet Update Action summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_rollback_action_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_summary_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

`details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_FSU_JOB_T Type

Rolback &amp; Remove Targets Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_rollback_fsu_job_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_t`type.

Fields

Field Description

`fsu_collection_id`

(required) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(required) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_FSU_JOB_SUMMARY_T Type

Summary of Rolback &amp; Remove Targets Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_rollback_fsu_job_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_summary_t`type.

Fields

Field Description

`fsu_collection_id`

(optional) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(optional) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_SEQUENTIAL_BATCHING_STRATEGY_DETAILS_T Type

Sequential batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_sequential_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_batching_strategy_details_t`type.

Fields

Field Description

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_SERVICE_AVAILABILITY_FACTOR_BATCHING_STRATEGY_DETAILS_T Type

Service Availability Factor batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_service_availability_factor_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_batching_strategy_details_t`type.

Fields

Field Description

`percentage`

(optional) Percentage of availability in the service during the Patch operation.

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_ACTION_T Type

Stage Exadata Fleet Update Action details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_stage_action_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_ACTION_SUMMARY_T Type

Stage Exadata Fleet Update Action summary.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_stage_action_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_action_summary_t`type.

Fields

Field Description

`fsu_cycle_id`

(required) OCID identifier for the Exadata Fleet Update Cycle the Action will be part of.

`related_fsu_action_id`

(optional) OCID identifier for the Exadata Fleet Update Action.

`schedule_details`

(optional)

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_FSU_JOB_T Type

Stage Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_stage_fsu_job_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_t`type.

Fields

Field Description

`fsu_collection_id`

(required) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(required) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_FSU_JOB_SUMMARY_T Type

Summary of Stage Exadata Fleet Update Job resource.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_stage_fsu_job_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_job_summary_t`type.

Fields

Field Description

`fsu_collection_id`

(optional) OCID of the Exadata Fleet Update Collection that the job is executing on.

`fsu_cycle_id`

(optional) OCID of the Exadata Fleet Update Cycle that this job is part of.

`target_id`

(optional) OCID of Target resource on which the job is executing the action.

`schedule`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_START_TIME_SCHEDULE_DETAILS_T Type

Start time details for the Exadata Fleet Update Action. The specified time should not conflict with existing Exadata Infrastructure maintenance windows. If Stage and Apply Actions are created with a timeToStart specified during Exadata Fleet Update Cycle creation, Apply should be scheduled at least 24 hours after the start time of the Stage Action.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_start_time_schedule_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_schedule_details_t`type.

Fields

Field Description

`time_to_start`

(required) The date and time the Exadata Fleet Update Action is expected to start.[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_IDS_REMOVE_TARGETS_DETAILS_T Type

Remove a list of targets from a Exadata Fleet Update Collection.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_target_ids_remove_targets_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_remove_fsu_collection_targets_details_t`type.

Fields

Field Description

`targets`

(required) List of target entries to remove from the Exadata Fleet Update Collection.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_PROGRESS_SUMMARY_T Type

Progress details of the executing job for a Database target.

Syntax
```

```

Fields

Field Description

`operation_type`

(optional) Type of operations being executed.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK'

`progress_of_operation`

(optional) Percentage of progress of the operation in execution.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_SUMMARY_T Type

Details of a target member of a Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`target`

(optional)

`current_version`

(optional) Current version of the target

`status`

(optional) Status of the target in the Exadata Fleet Update Collection.

Allowed values are: 'IDLE', 'EXECUTING_JOB', 'JOB_FAILED'

`executing_fsu_job_id`

(optional) Exadata Fleet Update Job OCID executing an action in the target. Null if no job is being executed.

`active_fsu_cycle_id`

(optional) Active Exadata Fleet Update Cycle OCID. Null if no Cycle is active that has this target as member.

`progress`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_target_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_SUMMARY_COLLECTION_T Type

List of TargetSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) List of TargetSummary entries.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_ACTION_DETAILS_T Type

Exadata Fleet Update Action resource details to update.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of Exadata Fleet Update Action to update. Specifying this option will not change the Action type.

Allowed values are: 'STAGE', 'PRECHECK', 'APPLY', 'ROLLBACK_AND_REMOVE_TARGET', 'CLEANUP'

`display_name`

(optional) Exadata Fleet Update Action display name.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_APPLY_ACTION_DETAILS_T Type

Apply Exadata Fleet Update Action update details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_apply_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_fsu_action_details_t`type.

Fields

Field Description

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_CLEANUP_ACTION_DETAILS_T Type

Cleanup Exadata Fleet Update Action update details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_cleanup_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_fsu_action_details_t`type.

Fields

Field Description

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FIFTY_FIFTY_BATCHING_STRATEGY_DETAILS_T Type

Fifty-Fifty batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_fifty_fifty_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_batching_strategy_details_t`type.

Fields

Field Description

`is_wait_for_batch_resume`

(optional) True to wait for customer to resume the Apply Action once the first half is done. False to automatically patch the second half.

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_COLLECTION_DETAILS_T Type

The information to Update Exadata Fleet Update Collection.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Collection display name.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_CYCLE_DETAILS_T Type

Update Exadata Fleet Update Cycle resource details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Exadata Fleet Update Cycle display name.

`l_type`

(required) Type of Exadata Fleet Update Cycle to update. This will not change the Maintenance Cycle type, it is to define the set of properties that can be updated depending on the Cycle type. Type value should match the Maintenance Cycle type.

Allowed values are: 'PATCH'

`goal_version_details`

(optional)

`batching_strategy`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_DISCOVERY_DETAILS_T Type

The information to Update Exadata Fleet Update Discovery resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Fleet Software Update Collection display name.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_JOB_DETAILS_T Type

Update Exadata Fleet Update Job Details.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name of the job.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_NON_ROLLING_BATCHING_STRATEGY_DETAILS_T Type

Non-rolling batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_non_rolling_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_batching_strategy_details_t`type.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_PATCH_FSU_CYCLE_T Type

Update Patch Exadata Fleet Update Cycle resource details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_patch_fsu_cycle_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_fsu_cycle_details_t`type.

Fields

Field Description

`is_ignore_patches`

(optional) Ignore all patches between the source and target homes during patching.

`is_ignore_missing_patches`

(optional) List of patch IDs to ignore. An empty array removes the previously stored patch IDs in the Maintenance Cycle properties.

`max_drain_timeout_in_seconds`

(optional) Service drain timeout specified in seconds.

`is_keep_placement`

(optional) Ensure that services of administrator-managed Oracle RAC or Oracle RAC One databases are running on the same instances before and after the move operation.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_PRECHECK_ACTION_DETAILS_T Type

Precheck Exadata Fleet Update Action update details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_precheck_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_fsu_action_details_t`type.

Fields

Field Description

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_ROLLBACK_ACTION_DETAILS_T Type

Rollback Exadata Fleet Update Action update details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_rollback_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_fsu_action_details_t`type.

Fields

Field Description

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_SEQUENTIAL_BATCHING_STRATEGY_DETAILS_T Type

Sequential batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_sequential_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_batching_strategy_details_t`type.

Fields

Field Description

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_SERVICE_AVAILABILITY_FACTOR_BATCHING_STRATEGY_DETAILS_T Type

Service Availability Factor batching strategy details to use during PRECHECK and APPLY Cycle Actions.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_service_availability_factor_batching_strategy_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_batching_strategy_details_t`type.

Fields

Field Description

`percentage`

(optional) Percentage of availability in the service during the Patch operation.

`is_force_rolling`

(optional) True to force rolling patching.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_STAGE_ACTION_DETAILS_T Type

Stage Exadata Fleet Update Action update details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_stage_action_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_fsu_action_details_t`type.

Fields

Field Description

`schedule_details`

(optional)

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_START_TIME_SCHEDULE_DETAILS_T Type

Start time details for the Exadata Fleet Update Action. The specified time should not conflict with existing Exadata Infrastructure maintenance windows. If Stage and Apply Actions are created with a timeToStart specified during Exadata Fleet Update Cycle creation, Apply should be scheduled at least 24 hours after the start time of the Stage Action.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_update_start_time_schedule_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_update_schedule_details_t`type.

Fields

Field Description

`time_to_start`

(required) The date and time the Exadata Fleet Update Action is expected to start.[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_VERSION_FSU_TARGET_DETAILS_T Type

Exadata Fleet Update Cycle Target version string details.

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_version_fsu_target_details_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_fsu_goal_version_details_t`type.

Fields

Field Description

`version`

(required) Target DB or GI version string for the Exadata Fleet Update Cycle.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_VM_CLUSTER_TARGET_SUMMARY_T Type

Details of a VmCluster target member of a Exadata Fleet Update Collection. Stored references of the resource documented in https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/VmCluster/

Syntax
```

```

`dbms_cloud_oci_fleet_software_update_vm_cluster_target_summary_t`is a subtype of the`dbms_cloud_oci_fleet_software_update_target_details_t`type.

Fields

Field Description

`infrastructure_id`

(optional) OCID of the related Exadata Infrastructure or Cloud Exadata Infrastructure resource.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_T Type

A description of workrequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_DISCOVERY', 'DELETE_DISCOVERY', 'CREATE_COLLECTION', 'UPDATE_COLLECTION', 'DELETE_COLLECTION', 'MOVE_COLLECTION', 'ADD_TARGETS_TO_COLLECTION', 'REMOVE_TARGETS_IN_COLLECTION', 'CREATE_MAINTENANCE_CYCLE', 'UPDATE_MAINTENANCE_CYCLE', 'DELETE_MAINTENANCE_CYCLE', 'MOVE_MAINTENANCE_CYCLE', 'CLONE_MAINTENANCE_CYCLE', 'CREATE_ACTION', 'UPDATE_ACTION', 'DELETE_ACTION', 'MOVE_ACTION', 'PATCH_ACTION', 'CLEANUP_ACTION', 'ROLLBACK_AND_REMOVE_ACTION', 'APPLY_ACTION', 'PRECHECK_ACTION', 'STAGE_ACTION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_DISCOVERY', 'DELETE_DISCOVERY', 'CREATE_COLLECTION', 'UPDATE_COLLECTION', 'DELETE_COLLECTION', 'MOVE_COLLECTION', 'ADD_TARGETS_TO_COLLECTION', 'REMOVE_TARGETS_IN_COLLECTION', 'CREATE_MAINTENANCE_CYCLE', 'UPDATE_MAINTENANCE_CYCLE', 'DELETE_MAINTENANCE_CYCLE', 'MOVE_MAINTENANCE_CYCLE', 'CLONE_MAINTENANCE_CYCLE', 'CREATE_ACTION', 'UPDATE_ACTION', 'DELETE_ACTION', 'MOVE_ACTION', 'PATCH_ACTION', 'CLEANUP_ACTION', 'ROLLBACK_AND_REMOVE_ACTION', 'APPLY_ACTION', 'PRECHECK_ACTION', 'STAGE_ACTION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fleet_software_update_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Fleet Software Update Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-85BB166E-BE74-4F5F-8D18-AA0FE7EA512C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-2267DF90-D009-4DAB-8015-CC9E570A4C91)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ACTIVE_CYCLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-DE5BE16D-DBC7-4115-B2E0-7A8E57B3D862)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-311C3375-A5B6-4359-896F-915D5308AD4B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-7E8C50A1-F9D6-46C4-A5A1-8AC44BA58CB9)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ADD_FSU_COLLECTION_TARGETS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-B1B63D7A-4743-4CAC-A336-B287B8165276)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-B83F9A15-4C8D-498F-9284-58BD9BF39D6B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_PROGRESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1D22777D-5BC6-4743-A853-8CFC417BA4DA)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6BAAE1B5-35B1-4D88-97F0-F49420D9F1A7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-361110A5-6D8D-4983-9E40-1FCB89AE426B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-14721E4D-F5B3-4103-ABE9-62850959860A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1725EA78-9A85-4B34-A52B-8122EABEA6E8)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_JOB_PROGRESS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-699471F9-ED2B-4540-AF5E-C0EF8025E2DF)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-F1E4AFB7-760F-4080-B2AC-E0B2FC4269D1)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_FSU_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-664D27D0-FDAC-4F2F-942C-46F80D14E83E)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_JOB_PROGRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-35C086BA-4EF2-4E15-BF8C-427C1C80D7B0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-ACCA38C2-11F0-433E-8872-CEA31C3369CE)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_APPLY_FSU_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-645ADFC3-FFEA-4125-B65C-5159162060D7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1A107C55-FE4E-4A21-941A-1F1E7C8A3186)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_ACTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-52F493F3-92EF-4FF8-9936-9237489886CE)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_COLLECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-7DEDC252-75B5-4C6C-A169-E0B5FCB1BA07)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_CYCLE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0FA0D2F6-96E1-4A7B-B782-69A3F7BC68CF)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CHANGE_FSU_DISCOVERY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-BD6D94D6-D912-422E-AA02-CAFFB24A7964)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0C47B18C-E274-4D7F-84FE-8DE8C31F0E14)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-5ED3AE91-8589-4A07-88FE-3BAD43F955A6)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_FSU_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-DAF22764-1FA0-4EB2-97EB-51087967C3FC)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLEANUP_FSU_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-935AE3BB-1EC4-4690-8537-5E5D86E02578)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_GOAL_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-24147397-9B6B-4501-9928-24F16FE91007)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-599CFB57-89CD-4681-B13A-4149D9B4E5C0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E735944F-4DE9-431B-9289-D9BF58DF8EAA)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLONE_FSU_CYCLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-FE6E87A6-4FA3-48A0-BD86-98B569FE159B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-797B6A64-FF86-4518-B8BD-5F3572B05699)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CLOUD_VM_CLUSTER_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4053B15E-9457-4FE6-8D10-BDB7FA06455F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D41CE073-3DA0-4BCC-891F-1DFB8C2D54E7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_APPLY_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-82427F39-CA2A-45BE-8FEF-90DAFD4EA143)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_CLEANUP_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-69F8B213-CFEB-4EEE-8E73-6C4D69ECF48F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FLEET_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-17016585-29C2-416C-AE47-1B9318721077)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_COLLECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-C1BFB57C-4725-4F3D-A9B6-5C555614C77E)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_DB_FSU_COLLECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-521FDC07-FD05-4719-80C1-3D2C58BE9624)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FIFTY_FIFTY_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1EA4EA84-0B84-4159-9358-E81607FE4B63)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_CYCLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-FA30A178-6684-463B-84A8-E4B2DF022A10)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0A602DA6-8F7C-4232-B91C-4349B6A3FFBF)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_FSU_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-65F92294-0E4F-4204-A80C-D3192F60325B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FLEET_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-82719065-2E31-4334-9B4C-00ACC12AE1CB)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_GI_FSU_COLLECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-DA01C38D-1AEF-4C48-B4A5-019724323C01)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_NON_ROLLING_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-83AF18FB-707F-45F7-9F46-D745831FED59)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_PATCH_FSU_CYCLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6B9BB229-1881-496B-99F7-0D88FD9148BF)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_PRECHECK_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-805C4B0F-BCA8-4E3F-BFD2-05B4364843BB)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-163256DF-0E24-4712-95EE-B05211A551A7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_ROLLBACK_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-B7509277-A322-4CBD-8629-1061344C9E9E)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_SEQUENTIAL_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-63F25C2F-BDFB-4C43-91F1-A8B270706C69)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_SERVICE_AVAILABILITY_FACTOR_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6E218534-1E5D-4EF8-A8E1-239C9852836C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_STAGE_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D0CEF965-3A18-41AD-9EF8-F33EC198479B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_CREATE_START_TIME_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-F52E9754-E69D-460A-8076-11825C28E40C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DATABASE_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4EFFB89B-6F66-4FF9-979F-4F2AC32E6E0A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-71B4FEE0-23CF-4C04-AFE4-800766A193F9)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4FEBFD0A-32D6-47E6-88C1-89B041D3FE87)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FLEET_DISCOVERY_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-5E5A0D82-2A0E-465E-B269-FC8ECFFDBAA2)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_COMPARTMENT_ID_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-10094339-335A-4370-8C57-BF79BA1FE5D9)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DEFINED_TAG_FILTER_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-135D1D9B-551B-4CF9-8401-5D92B3FA7488)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DEFINED_TAG_FILTER_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0902CE35-4CDE-41DC-8164-6F6B4D4E12D1)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_DEFINED_TAGS_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-29E865CE-591E-41A5-92B5-B1A86D61E63A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-A926CD74-473E-4CAB-A9F2-0DD7EFEED718)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_DISCOVERY_RESULTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-9A5931E1-77F8-4751-A55A-D99FB61E884D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FLEET_DISCOVERY_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6AFC7567-1ADD-4162-9400-E0A035A55A18)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FILTERS_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-9FE83CC6-3877-426D-A6CA-1652F9CED87A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FREEFORM_TAG_FILTER_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-30C371F7-4CCB-4AE2-BD8A-A9F5FC31D555)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FREEFORM_TAG_FILTER_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-50B85E36-D8F0-4F66-B52E-CE13C48F4096)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FREEFORM_TAGS_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D0643B5B-CB6F-4134-8A48-325301E3B7DC)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-DF098700-0D9A-4925-9D5B-B5B53321D50F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_FSU_COLLECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1C50585A-C4B2-4B21-B030-1CF42994BF23)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_HOME_NAME_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-73C87F8F-8BCF-4C1E-A85E-16331B6234D8)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_NAME_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-577000D8-5992-4C62-B38E-7BB4AD89A90B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_RESOURCE_ID_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E83FE7AD-1134-4E89-B6D0-B03BBBFBF5BD)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_SEARCH_QUERY_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-608F8E3D-8F33-49B2-AA4F-4CD230184B34)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_TARGET_LIST_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1C89FD9F-8620-47DF-8B75-1538BC66C3F6)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_UNIQUE_NAME_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-AB0675ED-1335-4961-950E-4CB793293973)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DB_VERSION_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-5F29AA16-A98F-4AA1-8094-D36D063333F5)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_DISCOVERY_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-151948C7-BFFB-4036-ACA7-033A48DB38B7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4C622669-8BF9-483F-AABD-D093B053CD41)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FAILED_JOBS_ROLLBACK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-FD9FC3FA-0BD5-458E-B793-FFE05B1EFF7B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FIFTY_FIFTY_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-8D5DFCEC-C055-48E4-BE78-B33F82EFF157)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-462263A3-799C-46C0-964D-71FF51383AB6)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_ACTION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E3511EF6-4F2C-4BC9-9888-4259AA8B28F0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-059C69A8-9E32-4D11-B5A1-6BAA8D705641)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_COLLECTION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-37B613C8-7B9B-4163-9127-4C2642FB205D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NEXT_ACTION_TO_EXECUTE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-773F3BF5-7DE8-4578-B34F-4487123272F6)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NEXT_ACTION_TO_EXECUTE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-09528AC2-A062-47DB-B361-A14BB37903F2)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-29032A8D-3D2A-4122-90D7-A12B16526405)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-19DEAF92-BD09-4551-8FCD-AE04EF4489E2)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E0E02D71-EFE8-4E27-9B6C-621C11563CB9)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_CYCLE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4E7F0887-00D3-4DD6-B3AA-7939C470C2AB)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-A7758454-A70B-4D5F-A08A-47720792E66D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1784A802-0CB5-449D-85CB-ACD50D9C84ED)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D59A8B21-524F-402D-AE16-F4FEC8098D3D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_DISCOVERY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-EF78AF32-12A7-4AC4-A14F-E8B7F8E17020)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-C4EF3EEE-A6CE-4E0A-BE8E-8AE0D2D71BE5)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-3C9C28D7-E94E-46BF-88C5-2A5055BC4D6F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_OUTPUT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-ED91B40B-6528-4047-ACA1-64859970F295)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_OUTPUT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-986DBE59-CB7B-419E-80CD-E2F5EBF17516)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_FSU_JOB_OUTPUT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-56D5488A-5547-48B7-8B9B-B902ED5D3DEC)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-2E9BBF6A-E05F-43D8-9347-6184895C4B1A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FLEET_DISCOVERY_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-15F51AD3-5498-4766-B8B4-6CAF36AE6C30)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_COMPARTMENT_ID_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-B8E3E414-7EFE-49B0-911C-8105B5ADC96F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_DEFINED_TAGS_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-81AD58B4-BC50-4657-BCCB-32A61317F101)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-EADBC8FE-6B66-48E6-9C4B-368592074D5A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_DISCOVERY_RESULTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-5EF2D24D-3E65-4854-B1EC-BC4AEF3513F1)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FLEET_DISCOVERY_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-831A8DA1-2179-4EDA-9870-DE3C1223D537)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FILTERS_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E9856BA3-1845-4CEB-B2AC-7FF042821A86)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FREEFORM_TAGS_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-F394C070-CF80-462C-BEDC-614E9DDD200B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_FSU_COLLECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D03B6618-E3AA-4A74-9244-AF1EDD775EA9)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_RESOURCE_ID_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6F05B3B9-4D4F-4108-98D6-E7BEF6C23845)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_SEARCH_QUERY_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E7EEAFFD-9180-4FCE-93BB-299A4547662B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_TARGET_LIST_DISCOVERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-25846E6B-3656-44E0-9F4C-2550DD762180)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_GI_VERSION_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-A77CDB71-CD8F-4DE9-BB8A-44CFFA9993A4)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_IMAGE_ID_FSU_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-513146E1-0EC3-46C0-A208-CF07F24A3AA0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_LIST_OF_TARGETS_ROLLBACK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E0965FDD-D020-4571-A1B1-578AEE5765EC)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NON_ROLLING_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-55697E58-2E51-4D3C-BB7F-BAC8C5E10F6D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-85B21942-E5D8-4710-A52B-4F89D7B89377)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NONE_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E627E02B-62AA-41D3-8AFC-5F5218B8449A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6DD852CD-AE87-400B-8EF1-2D1E3D9DAB02)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_NONE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-8627A402-CECB-4B88-A0EB-A0557CC64A62)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PATCH_FSU_CYCLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-79462DB6-0041-4564-9678-F5B73232CDC1)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0975F13F-361D-437D-9ECA-0612DAB24AB0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-8DE3C145-4115-4DFD-8328-8CC832E9E8C0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_FSU_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-5F1852AF-139D-4D99-9728-D3D874EC2BF8)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_PRECHECK_FSU_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-B4AB4F26-45F5-4826-970C-9D868B744B49)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_REMOVE_FSU_COLLECTION_TARGETS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-49D7EA83-34EF-4458-9C05-22A019B9438E)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-FF18E37E-6221-4C39-B191-2A1069355BF7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1BB3424B-AD0B-4BB0-BA7E-3BE02849D23D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_FSU_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D8339DAA-9C6B-4A72-8D02-1A4A3DAB765C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_ROLLBACK_FSU_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4AE1FD49-4FA1-403F-B9A8-2F9C85335A0A)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_SEQUENTIAL_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-8D476A8D-0059-44CB-B3BD-6885FF9AAC39)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_SERVICE_AVAILABILITY_FACTOR_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-091375F7-DF5D-4B51-BBEB-A4F6F9CC5D6C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-B388B1B4-0809-4A10-8520-944A3AC10C10)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_ACTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0705C0DA-A678-49C7-BCE1-1988658564CB)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_FSU_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-12036762-A2CC-44F1-A544-7A68E78313DC)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_STAGE_FSU_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-560029F0-A33F-4F8C-ADFE-8D6D9C4286E7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_START_TIME_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-A38884EF-5BF5-45F5-864A-E28AC7ABB597)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_IDS_REMOVE_TARGETS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-13BF575E-8C27-488C-B963-81075AC2877C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_PROGRESS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-7591A3C1-4725-454B-AEB6-60634BECCDD7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-882BEE20-DE67-4159-8A6C-F67CAA1076F0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-C84FAE44-4AAA-4EB6-A0DA-02380CF07385)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_TARGET_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D150EF69-D951-4FEC-94B5-74073C38B799)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-3FCAA2F8-8DD4-4B28-BF4D-36509B05D18C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_APPLY_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-C8D3FD68-92AF-49CA-8691-2779A568F593)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_CLEANUP_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4DF2050E-ABF6-4615-86E3-D6C22DED4C9B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FIFTY_FIFTY_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-9D91E269-77D1-43A1-BE7E-A043BAC9E3F0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_COLLECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-ED54C560-AB64-445D-A9F3-41514419DEC7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_CYCLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-ED757296-602A-4575-8BB5-91B8F8B04125)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-79FF6FE2-ABDA-4B1C-B307-1238AF427DAD)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_FSU_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-4E633F44-6F82-41FF-A292-CAFAFAA937EB)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_NON_ROLLING_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-C5E302BD-897A-495C-89FC-FFD1CE0D4612)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_PATCH_FSU_CYCLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D464D151-BCCE-4BD7-89F7-C576CDBB266E)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_PRECHECK_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-E09F0247-C4BA-4B5D-8FA2-BD8B058676D3)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_ROLLBACK_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-1D845E2D-EEB8-4FC7-8D45-BE041F2F7461)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_SEQUENTIAL_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-F694016D-3E96-4225-823E-080E8EBFE7F3)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_SERVICE_AVAILABILITY_FACTOR_BATCHING_STRATEGY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-134F73A1-8D7F-499A-B32D-1D24DF69DB3D)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_STAGE_ACTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-CB70801D-9281-42AD-901C-0004C456FA4F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_UPDATE_START_TIME_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0914E142-E390-43C3-B5A1-EE54E2FC795C)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_VERSION_FSU_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-23137741-84B9-4C88-9F79-5047644A1831)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_VM_CLUSTER_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-0896B6A9-6581-4FED-AC73-4B00F483297F)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-AD757ED2-1818-4838-AAF6-0A4E793B3300)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-86605EC6-2059-4201-B1FE-2E864CEA48D8)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-9B0D1BF0-78DD-4ABE-9754-74CA13DA2EF0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D86C4ABD-29BC-4691-BBE8-FBF1C5B737B8)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-44CD79ED-77C9-49AF-B21B-22D7F4D391E7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-951E1F39-B87D-4475-9E31-8A3805B150B0)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-12868A8A-C2F9-477D-9ECE-F980E4385FD7)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-6BFC3587-7937-4C72-BE21-2F419D61C9EF)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-D8462C2F-0176-4EF6-B417-EDE449902190)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-BADB29BE-635B-4B77-BDC7-E18DB228F42B)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-19E5D479-59F5-4508-B0B3-B15C77285362)
- [DBMS_CLOUD_OCI_FLEET_SOFTWARE_UPDATE_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fleet_software_update_t.html#ADSDK-GUID-F46FE910-EF97-453A-8B54-C757A0D97FAD)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
