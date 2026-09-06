# Database Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#dcoc-content-body)

## Database Common Types

### DBMS_CLOUD_OCI_DATABASE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_ACD_AVM_RESOURCE_STATS_T Type

Resource usage by autonomous container database in a particular VM.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM.

`display_name`

(optional) The user-friendly name for the Autonomous VM. The name does not need to be unique.

`provisioned_cpus`

(optional) CPUs/cores assigned to Autonomous Databases for the ACD instance in given Autonomus VM.

`used_cpus`

(optional) CPUs/cores assigned to the ACD instance in given Autonomous VM. Sum of provisioned, reserved and reclaimable CPUs/ cores to the ACD instance.

`reserved_cpus`

(optional) CPUs/cores reserved for scalability, resilliency and other overheads. This includes failover, autoscaling and idle instance overhead.

`reclaimable_cpus`

(optional) CPUs/cores that continue to be included in the count of OCPUs available to the Autonomous Container Database in given Autonomous VM, even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.

### DBMS_CLOUD_OCI_DATABASE_ACTIVATE_EXADATA_INFRASTRUCTURE_DETAILS_T Type

The activation details for the Exadata Cloud@Customer infrastructure. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`activation_file`

(required) The activation zip file.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_DB_SERVER_DETAILS_T Type

Details of the ExaDB-D DB server. Applies to Exadata Cloud instances only.

Syntax
```

```

Fields

Field Description

`db_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of ExaDB-D DB server.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_DB_SERVER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_cloud_db_server_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_ADD_VIRTUAL_MACHINE_TO_CLOUD_VM_CLUSTER_DETAILS_T Type

Details of adding Virtual Machines to the Cloud VM Cluster. Applies to Exadata Cloud instances only.

Syntax
```

```

Fields

Field Description

`db_servers`

(required) The list of ExaCS DB servers for the cluster to be added.

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_DETAILS_T Type

Details of the Exacc Db server. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`db_server_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of Exacc Db server.

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_db_server_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_ADD_VIRTUAL_MACHINE_TO_VM_CLUSTER_DETAILS_T Type

Details of adding Virtual Machines to the VM Cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`db_servers`

(required) The list of Exacc DB servers for the cluster to be added.

### DBMS_CLOUD_OCI_DATABASE_APP_VERSION_SUMMARY_T Type

The version details specific to an app.

Syntax
```

```

Fields

Field Description

`release_date`

(required) The Autonomous Container Database version release date.

`end_of_support`

(required) The Autonomous Container Database version end of support date.

`supported_app_name`

(required) The name of the supported application.

`is_certified`

(required) Indicates if the image is certified.

### DBMS_CLOUD_OCI_DATABASE_APPLICATION_VIP_T Type

Details of an application virtual IP (VIP) address.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application virtual IP (VIP) address.

`cloud_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster associated with the application virtual IP (VIP) address.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the application virtual IP (VIP) address.

`ip_address`

(optional) The application virtual IP (VIP) address.

`hostname_label`

(required) The hostname of the application virtual IP (VIP) address.

`lifecycle_state`

(required) The current lifecycle state of the application virtual IP (VIP) address.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the application virtual IP (VIP) address.

`time_assigned`

(required) The date and time when the create operation for the application virtual IP (VIP) address completed.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_APPLICATION_VIP_SUMMARY_T Type

Details of an application virtual IP (VIP) address.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application virtual IP (VIP) address.

`cloud_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster associated with the application virtual IP (VIP) address.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the application virtual IP (VIP) address.

`ip_address`

(optional) The application virtual IP (VIP) address.

`hostname_label`

(required) The hostname of the application virtual IP (VIP) address.

`lifecycle_state`

(required) The current lifecycle state of the application virtual IP (VIP) address.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the application virtual IP (VIP) address.

`time_assigned`

(required) The date and time when the create operation for the application virtual IP (VIP) address completed.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_ASSOCIATED_DATABASE_DETAILS_T Type

Databases associated with a backup destination

Syntax
```

```

Fields

Field Description

`id`

(optional) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`db_name`

(optional) The display name of the database that is associated with the backup destination.

### DBMS_CLOUD_OCI_DATABASE_MOUNT_TYPE_DETAILS_T Type

Mount type details for backup destination.

Syntax
```

```

Fields

Field Description

`mount_type`

(required) Mount type for backup destination.

Allowed values are: 'SELF_MOUNT', 'AUTOMATED_MOUNT'

### DBMS_CLOUD_OCI_DATABASE_AUTOMATED_MOUNT_DETAILS_T Type

Used for creating NFS Auto Mount backup destinations for autonomous on ExaCC.

Syntax
```

```

`dbms_cloud_oci_database_automated_mount_details_t`is a subtype of the`dbms_cloud_oci_database_mount_type_details_t`type.

Fields

Field Description

`nfs_server`

(required) IP addresses for NFS Auto mount.

`nfs_server_export`

(required) Specifies the directory on which to mount the file system

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_KEY_HISTORY_ENTRY_T Type

The Autonomous Database[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts)service key management history entry.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the Autonomous Database[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts)service key management history entry.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`time_activated`

(optional) The date and time the kms key activated.

### DBMS_CLOUD_OCI_DATABASE_MONTH_T Type

Month of the year.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the month of the year.

Allowed values are: 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'

### DBMS_CLOUD_OCI_DATABASE_DAY_OF_WEEK_T Type

Day of the week.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the day of the week.

Allowed values are: 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'

### DBMS_CLOUD_OCI_DATABASE_MONTH_TBL Type

Nested table type of dbms_cloud_oci_database_month_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_DAY_OF_WEEK_TBL Type

Nested table type of dbms_cloud_oci_database_day_of_week_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_WINDOW_T Type

The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.

Syntax
```

```

Fields

Field Description

`preference`

(optional) The maintenance window scheduling preference.

Allowed values are: 'NO_PREFERENCE', 'CUSTOM_PREFERENCE'

`patching_mode`

(optional) Cloud Exadata infrastructure node patching method, either \"ROLLING\" or \"NONROLLING\". Default value is ROLLING. *IMPORTANT*: Non-rolling infrastructure patching involves system down time. See[Oracle-Managed Infrastructure Maintenance Updates](https://docs.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle)for more information.

Allowed values are: 'ROLLING', 'NONROLLING'

`is_custom_action_timeout_enabled`

(optional) If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.

`custom_action_timeout_in_mins`

(optional) Determines the amount of time the system will wait before the start of each database server patching operation. Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).

`is_monthly_patching_enabled`

(optional) If true, enables the monthly patching option.

`months`

(optional) Months during the year when maintenance should be performed.

`weeks_of_month`

(optional) Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week. For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2. Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days. Note that this parameter works in conjunction with the daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the week and hours that maintenance will be performed.

`days_of_week`

(optional) Days during the week when maintenance should be performed.

`hours_of_day`

(optional) The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC

`lead_time_in_weeks`

(optional) Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.

### DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_DETAILS_T Type

Backup destination details

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the database backup destination.

Allowed values are: 'NFS', 'RECOVERY_APPLIANCE', 'OBJECT_STORE', 'LOCAL', 'DBRS'

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`vpc_user`

(optional) For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.

`vpc_password`

(optional) For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.

`internet_proxy`

(optional) Proxy URL to connect to object store.

`dbrs_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DBRS policy used for backup.

### DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_backup_destination_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_BACKUP_CONFIG_T Type

Backup options for the Autonomous Container Database.

Syntax
```

```

Fields

Field Description

`backup_destination_details`

(optional) Backup destination details.

`recovery_window_in_days`

(optional) Number of days between the current and the earliest point of recoverability covered by automatic backups. This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window. When the value is updated, it is applied to all existing automatic backups. If the number of specified days is 0 then there will be no backups.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_KEY_HISTORY_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_database_autonomous_database_key_history_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Autonomous Container Database.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-provided name for the Autonomous Container Database.

`db_unique_name`

(optional) **Deprecated.** The `DB_UNIQUE_NAME` value is set by Oracle Cloud Infrastructure. Do not specify a value for this parameter. Specifying a value for this field will cause Terraform operations to fail.

`db_name`

(optional) The Database name for the Autonomous Container Database. The name must be unique within the Cloud Autonomous VM Cluster, starting with an alphabetic character, followed by 1 to 7 alphanumeric characters.

`service_level_agreement_type`

(required) The service level agreement type of the container database. The default is STANDARD.

Allowed values are: 'STANDARD', 'MISSION_CRITICAL', 'AUTONOMOUS_DATAGUARD'

`autonomous_exadata_infrastructure_id`

(optional) **No longer used.** For Autonomous Database on dedicated Exadata infrastructure, the container database is created within a specified `cloudAutonomousVmCluster`.

`autonomous_vm_cluster_id`

(optional) The OCID of the Autonomous VM Cluster.

`infrastructure_type`

(optional) The infrastructure type this resource belongs to.

Allowed values are: 'CLOUD', 'CLOUD_AT_CUSTOMER'

`cloud_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Autonomous Exadata VM Cluster.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`key_history_entry`

(optional) Key History Entry.

`lifecycle_state`

(required) The current state of the Autonomous Container Database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'BACKUP_IN_PROGRESS', 'RESTORING', 'RESTORE_FAILED', 'RESTARTING', 'MAINTENANCE_IN_PROGRESS', 'ROLE_CHANGE_IN_PROGRESS', 'ENABLING_AUTONOMOUS_DATA_GUARD', 'UNAVAILABLE'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the Autonomous Container Database was created.

`time_snapshot_standby_revert`

(optional) The date and time the Autonomous Container Database will be reverted to Standby from Snapshot Standby.

`patch_model`

(required) Database patch model preference.

Allowed values are: 'RELEASE_UPDATES', 'RELEASE_UPDATE_REVISIONS'

`patch_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch applied on the system.

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`maintenance_window`

(optional)

`standby_maintenance_buffer_in_days`

(optional) The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database. This value represents the number of days before scheduled maintenance of the primary database.

`version_preference`

(optional) The next maintenance version preference.

Allowed values are: 'NEXT_RELEASE_UPDATE', 'LATEST_RELEASE_UPDATE'

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`dst_file_version`

(optional) DST Time Zone File version of the Autonomous Container Database.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`role`

(optional) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`availability_domain`

(optional) The availability domain of the Autonomous Container Database.

`db_version`

(optional) Oracle Database version of the Autonomous Container Database.

`backup_config`

(optional)

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) enabled per OCPU or ECPU in the Autonomous VM Cluster.

`available_cpus`

(optional) Sum of CPUs available on the Autonomous VM Cluster + Sum of reclaimable CPUs available in the Autonomous Container Database.&lt;br&gt; For Autonomous Databases on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`total_cpus`

(optional) The number of CPUs allocated to the Autonomous VM cluster.&lt;br&gt; For Autonomous Databases on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`reclaimable_cpus`

(optional) For Autonomous Databases on Dedicated Exadata Infrastructure: - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database. - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`provisionable_cpus`

(optional) An array of CPU values that can be used to successfully provision a single Autonomous Database.\\ For Autonomous Database on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`compute_model`

(optional) The compute model of the Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous Container Database.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous Container Database.

`largest_provisionable_autonomous_database_in_cpus`

(optional) The largest Autonomous Database (CPU) that can be created in a new Autonomous Container Database.

`time_of_last_backup`

(optional) The timestamp of last successful backup. Here NULL value represents either there are no successful backups or backups are not configured for this Autonomous Container Database.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION_T Type

The properties that define Autonomous Data Guard association between two different Autonomous Container Databases.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Autonomous Data Guard created for a given Autonomous Container Database.

`autonomous_container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Container Database that has a relationship with the peer Autonomous Container Database.

`role`

(required) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`lifecycle_state`

(required) The current state of Autonomous Data Guard.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ROLE_CHANGE_IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'FAILED', 'UNAVAILABLE', 'UPDATING'

`lifecycle_details`

(optional) Additional information about the current lifecycleState, if available.

`peer_autonomous_container_database_dataguard_association_id`

(optional) The OCID of the peer Autonomous Container Database-Autonomous Data Guard association.

`peer_autonomous_container_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer Autonomous Container Database.

`peer_role`

(required) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`peer_lifecycle_state`

(optional) The current state of Autonomous Data Guard.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ROLE_CHANGE_IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'FAILED', 'UNAVAILABLE', 'UPDATING'

`protection_mode`

(optional) The protection mode of this Autonomous Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE'

`fast_start_fail_over_lag_limit_in_seconds`

(optional) The lag time for my preference based on data loss tolerance in seconds.

`apply_lag`

(optional) The lag time between updates to the primary Autonomous Container Database and application of the redo data on the standby Autonomous Container Database, as computed by the reporting database. Example: `9 seconds`

`apply_rate`

(optional) The rate at which redo logs are synchronized between the associated Autonomous Container Databases. Example: `180 Mb per second`

`is_automatic_failover_enabled`

(optional) Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association

`transport_lag`

(optional) The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database, as computed by the reporting database. Example: `7 seconds`

`time_last_synced`

(optional) The date and time of the last update to the apply lag, apply rate, and transport lag values.

`time_created`

(optional) The date and time the Autonomous DataGuard association was created.

`time_last_role_changed`

(optional) The date and time when the last role change action happened.

### DBMS_CLOUD_OCI_DATABASE_ACD_AVM_RESOURCE_STATS_TBL Type

Nested table type of dbms_cloud_oci_database_acd_avm_resource_stats_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_RESOURCE_USAGE_T Type

Associated autonomous container databases usages.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Container Database.

`display_name`

(required) The user-friendly name for the Autonomous Container Database. The name does not need to be unique.

`reclaimable_cpus`

(optional) CPUs / cores reclaimable or released to cluster on Autonomous Container Database restart.

`available_cpus`

(optional) CPUs / cores available for ADB provisioning or scaling in the Autonomous Container Database.

`largest_provisionable_autonomous_database_in_cpus`

(optional) Largest provisionable ADB in the Autonomous Container Database.

`provisioned_cpus`

(optional) CPUs / cores assigned to ADBs in the Autonomous Container Database.

`reserved_cpus`

(optional) CPUs / cores reserved for scalability, resilliency and other overheads. This includes failover, autoscaling and idle instance overhead.

`used_cpus`

(optional) CPUs / cores assigned to the Autonomous Container Database. Sum of provisioned, reserved and reclaimable CPUs/ cores.

`provisionable_cpus`

(optional) Valid list of provisionable CPUs / cores for ADB creation.

`autonomous_container_database_vm_usage`

(optional) List of autonomous container database resource usage per autonomous virtual machine.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_SUMMARY_T Type

An Autonomous Container Database is a container database service that enables the customer to host one or more databases within the container database. A basic container database runs on a single Autonomous Exadata Infrastructure from an availability domain without the Extreme Availability features enabled.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Autonomous Container Database.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-provided name for the Autonomous Container Database.

`db_unique_name`

(optional) **Deprecated.** The `DB_UNIQUE_NAME` value is set by Oracle Cloud Infrastructure. Do not specify a value for this parameter. Specifying a value for this field will cause Terraform operations to fail.

`db_name`

(optional) The Database name for the Autonomous Container Database. The name must be unique within the Cloud Autonomous VM Cluster, starting with an alphabetic character, followed by 1 to 7 alphanumeric characters.

`service_level_agreement_type`

(required) The service level agreement type of the container database. The default is STANDARD.

Allowed values are: 'STANDARD', 'MISSION_CRITICAL', 'AUTONOMOUS_DATAGUARD'

`autonomous_exadata_infrastructure_id`

(optional) **No longer used.** For Autonomous Database on dedicated Exadata infrastructure, the container database is created within a specified `cloudAutonomousVmCluster`.

`autonomous_vm_cluster_id`

(optional) The OCID of the Autonomous VM Cluster.

`infrastructure_type`

(optional) The infrastructure type this resource belongs to.

Allowed values are: 'CLOUD', 'CLOUD_AT_CUSTOMER'

`cloud_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Autonomous Exadata VM Cluster.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`key_history_entry`

(optional) Key History Entry.

`lifecycle_state`

(required) The current state of the Autonomous Container Database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'BACKUP_IN_PROGRESS', 'RESTORING', 'RESTORE_FAILED', 'RESTARTING', 'MAINTENANCE_IN_PROGRESS', 'ROLE_CHANGE_IN_PROGRESS', 'ENABLING_AUTONOMOUS_DATA_GUARD', 'UNAVAILABLE'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the Autonomous Container Database was created.

`time_snapshot_standby_revert`

(optional) The date and time the Autonomous Container Database will be reverted to Standby from Snapshot Standby.

`patch_model`

(required) Database patch model preference.

Allowed values are: 'RELEASE_UPDATES', 'RELEASE_UPDATE_REVISIONS'

`patch_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch applied on the system.

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`maintenance_window`

(optional)

`standby_maintenance_buffer_in_days`

(optional) The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database. This value represents the number of days before scheduled maintenance of the primary database.

`version_preference`

(optional) The next maintenance version preference.

Allowed values are: 'NEXT_RELEASE_UPDATE', 'LATEST_RELEASE_UPDATE'

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`dst_file_version`

(optional) DST Time Zone File version of the Autonomous Container Database.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`role`

(optional) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`availability_domain`

(optional) The availability domain of the Autonomous Container Database.

`db_version`

(optional) Oracle Database version of the Autonomous Container Database.

`backup_config`

(optional)

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) enabled per OCPU or ECPU in the Autonomous VM Cluster.

`available_cpus`

(optional) Sum of CPUs available on the Autonomous VM Cluster + Sum of reclaimable CPUs available in the Autonomous Container Database.&lt;br&gt; For Autonomous Databases on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`total_cpus`

(optional) The number of CPUs allocated to the Autonomous VM cluster.&lt;br&gt; For Autonomous Databases on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`reclaimable_cpus`

(optional) For Autonomous Databases on Dedicated Exadata Infrastructure: - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database. - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`provisionable_cpus`

(optional) An array of CPU values that can be used to successfully provision a single Autonomous Database.\\ For Autonomous Database on Dedicated Exadata Infrastructure, the CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`compute_model`

(optional) The compute model of the Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous Container Database.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous Container Database.

`largest_provisionable_autonomous_database_in_cpus`

(optional) The largest Autonomous Database (CPU) that can be created in a new Autonomous Container Database.

`time_of_last_backup`

(optional) The timestamp of last successful backup. Here NULL value represents either there are no successful backups or backups are not configured for this Autonomous Container Database.

### DBMS_CLOUD_OCI_DATABASE_APP_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_app_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_VERSION_SUMMARY_T Type

The supported Autonomous Database version.

Syntax
```

```

Fields

Field Description

`version`

(required) A valid Oracle Database version for provisioning an Autonomous Container Database.

`details`

(optional) A URL that points to a detailed description of the Autonomous Container Database version.

`supported_apps`

(required) The list of applications supported for the given version.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATA_WAREHOUSE_CONNECTION_STRINGS_T Type

**Deprecated.** For information about connection strings to connect to an Oracle Autonomous Data Warehouse, see`AUTONOMOUS_DATABASE_CONNECTION_STRINGS`Function.

Syntax
```

```

Fields

Field Description

`high`

(optional) The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.

`medium`

(optional) The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.

`low`

(optional) The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.

`all_connection_strings`

(optional) Returns all connection strings that can be used to connect to the Autonomous Data Warehouse.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATA_WAREHOUSE_T Type

**Deprecated.** See`AUTONOMOUS_DATABASE`Type for reference information about Autonomous Databases with the warehouse workload type.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Data Warehouse.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current state of the database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'UNAVAILABLE', 'RESTORE_IN_PROGRESS', 'BACKUP_IN_PROGRESS', 'SCALE_IN_PROGRESS', 'AVAILABLE_NEEDS_ATTENTION', 'UPDATING'

`lifecycle_details`

(optional) Information about the current lifecycle state.

`db_name`

(required) The database name.

`cpu_core_count`

(required) The number of CPU cores to be made available to the database.

`data_storage_size_in_t_bs`

(required) The quantity of data in the database, in terabytes.

`time_created`

(optional) The date and time the database was created.

`display_name`

(optional) The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.

`service_console_url`

(optional) The URL of the Service Console for the Data Warehouse.

`connection_strings`

(optional) The connection string used to connect to the Data Warehouse. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Data Warehouse for the password value.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`db_version`

(optional) A valid Oracle Database version for Autonomous Data Warehouse.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATA_WAREHOUSE_SUMMARY_T Type

**Deprecated.** See`AUTONOMOUS_DATABASE`Function for reference information about Autonomous Databases with the warehouse workload type. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Data Warehouse.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current state of the database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'UNAVAILABLE', 'RESTORE_IN_PROGRESS', 'BACKUP_IN_PROGRESS', 'SCALE_IN_PROGRESS', 'AVAILABLE_NEEDS_ATTENTION', 'UPDATING'

`lifecycle_details`

(optional) Information about the current lifecycle state.

`db_name`

(required) The database name.

`cpu_core_count`

(required) The number of CPU cores to be made available to the database.

`data_storage_size_in_t_bs`

(required) The quantity of data in the database, in terabytes.

`time_created`

(optional) The date and time the database was created.

`display_name`

(optional) The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.

`service_console_url`

(optional) The URL of the Service Console for the Data Warehouse.

`connection_strings`

(optional) The connection string used to connect to the Data Warehouse. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Data Warehouse for the password value.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`db_version`

(optional) A valid Oracle Database version for Autonomous Data Warehouse.

### DBMS_CLOUD_OCI_DATABASE_LONG_TERM_BACK_UP_SCHEDULE_DETAILS_T Type

Details for the long-term backup schedule.

Syntax
```

```

Fields

Field Description

`repeat_cadence`

(optional) The frequency of the long-term backup schedule

Allowed values are: 'ONE_TIME', 'WEEKLY', 'MONTHLY', 'YEARLY'

`time_of_backup`

(optional) The timestamp for the long-term backup schedule. For a MONTHLY cadence, months having fewer days than the provided date will have the backup taken on the last day of that month.

`retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`is_disabled`

(optional) Indicates if the long-term backup schedule should be deleted. The default value is `FALSE`.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_BACKUP_CONFIG_T Type

Autonomous Database configuration details for storing[manual backups](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/backup-restore.html#GUID-9035DFB8-4702-4CEB-8281-C2A303820809)in the[Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)service.

Syntax
```

```

Fields

Field Description

`manual_backup_bucket_name`

(optional) Name of[Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)bucket to use for storing manual backups.

`manual_backup_type`

(optional) The manual backup destination type.

Allowed values are: 'NONE', 'OBJECT_STORE'

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRING_PROFILE_T Type

The connection string profile to allow clients to group, filter and select connection string values based on structured metadata.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name for the connection.

`value`

(required) Connection string value.

`consumer_group`

(optional) Consumer group used by the connection.

Allowed values are: 'HIGH', 'MEDIUM', 'LOW', 'TP', 'TPURGENT'

`protocol`

(required) Protocol used by the connection.

Allowed values are: 'TCP', 'TCPS'

`tls_authentication`

(optional) Specifies whether the TLS handshake is using one-way (`SERVER`) or mutual (`MUTUAL`) authentication.

Allowed values are: 'SERVER', 'MUTUAL'

`host_format`

(required) Host format used in connection string.

Allowed values are: 'FQDN', 'IP'

`session_mode`

(required) Specifies whether the listener performs a direct hand-off of the session, or redirects the session. In RAC deployments where SCAN is used, sessions are redirected to a Node VIP. Use `DIRECT` for direct hand-offs. Use `REDIRECT` to redirect the session.

Allowed values are: 'DIRECT', 'REDIRECT'

`syntax_format`

(required) Specifies whether the connection string is using the long (`LONG`), Easy Connect (`EZCONNECT`), or Easy Connect Plus (`EZCONNECTPLUS`) format. Autonomous Database Serverless instances always use the long format.

Allowed values are: 'LONG', 'EZCONNECT', 'EZCONNECTPLUS'

`is_regional`

(optional) True for a regional connection string, applicable to cross-region DG only.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRING_PROFILE_TBL Type

Nested table type of dbms_cloud_oci_database_database_connection_string_profile_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CONNECTION_STRINGS_T Type

Connection strings to connect to an Oracle Autonomous Database. Example output for connection strings. See`DATABASE_CONNECTION_STRING_PROFILE`Function for additional details: \"connectionStrings\": { \"allConnectionStrings\": { \"HIGH\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_high.adwc.oraclecloud.com\", \"LOW\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_low.adwc.oraclecloud.com\", \"MEDIUM\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_medium.adwc.oraclecloud.com\" }, \"profiles\": [ { \"displayName\": \"databasename_high\", \"value\": \"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=unique_id_databasename_high.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=\"CN=adwc.uscom-east-1.oraclecloud.com,OU=Oracle BMCS US,O=Oracle Corporation,L=Redwood City,ST=California,C=US\")))\", \"consumerGroup\": \"HIGH\", \"protocol\": \"TCPS\", \"tlsAuthentication\": \"MUTUAL\", \"hostFormat\": \"FQDN\", \"sessionMode\": \"DIRECT\", \"syntaxFormat\": \"LONG\" }, { \"displayName\": \"databasename_low\", \"value\": \"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=unique_id_databasename_low.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=\"CN=adwc.uscom-east-1.oraclecloud.com,OU=Oracle BMCS US,O=Oracle Corporation,L=Redwood City,ST=California,C=US\")))\", \"consumerGroup\": \"LOW\", \"protocol\": \"TCPS\", \"tlsAuthentication\": \"MUTUAL\", \"hostFormat\": \"FQDN\", \"sessionMode\": \"DIRECT\", \"syntaxFormat\": \"LONG\" }, { \"displayName\": \"databasename_medium\", \"value\": \"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=unique_id_databasename_medium.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=\"CN=adwc.uscom-east-1.oraclecloud.com,OU=Oracle BMCS US,O=Oracle Corporation,L=Redwood City,ST=California,C=US\")))\", \"consumerGroup\": \"MEDIUM\", \"protocol\": \"TCPS\", \"tlsAuthentication\": \"MUTUAL\", \"hostFormat\": \"FQDN\", \"sessionMode\": \"DIRECT\", \"syntaxFormat\": \"LONG\" } ], \"dedicated\": null, \"high\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_high.adwc.oraclecloud.com\", \"low\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_low.adwc.oraclecloud.com\", \"medium\": \"adb.region.oraclecloud.com:1522/unique_id_databasename_medium.adwc.oraclecloud.com\" }

Syntax
```

```

Fields

Field Description

`high`

(optional) The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.

`medium`

(optional) The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.

`low`

(optional) The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.

`dedicated`

(optional) The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.

`all_connection_strings`

(optional) Returns all connection strings that can be used to connect to the Autonomous Database.

`profiles`

(optional) A list of connection string profiles to allow clients to group, filter and select connection string values based on structured metadata.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CONNECTION_URLS_T Type

The URLs for accessing Oracle Application Express (APEX) and SQL Developer Web with a browser from a Compute instance within your VCN or that has a direct connection to your VCN. Note that these URLs are provided by the console only for databases on[dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html). Example: `{\"sqlDevWebUrl\": \"https://&lt;hostname&gt;/ords...\", \"apexUrl\", \"https://&lt;hostname&gt;/ords...\"}`

Syntax
```

```

Fields

Field Description

`sql_dev_web_url`

(optional) Oracle SQL Developer Web URL.

`apex_url`

(optional) Oracle Application Express (APEX) URL.

`machine_learning_user_management_url`

(optional) Oracle Machine Learning user management URL.

`graph_studio_url`

(optional) The URL of the Graph Studio for the Autonomous Database.

`mongo_db_url`

(optional) The URL of the MongoDB API for the Autonomous Database.

`machine_learning_notebook_url`

(optional) The URL of the Oracle Machine Learning (OML) Notebook for the Autonomous Database.

`ords_url`

(optional) The Oracle REST Data Services (ORDS) URL of the Web Access for the Autonomous Database.

`database_transforms_url`

(optional) The URL of the Database Transforms for the Autonomous Database.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_APEX_T Type

Oracle APEX Application Development is a low-code development platform that enables you to build scalable, secure enterprise apps, with world-class features. Autonomous Database with the APEX workload type is optimized to support APEX development.

Syntax
```

```

Fields

Field Description

`apex_version`

(optional) The Oracle APEX Application Development version.

`ords_version`

(optional) The Oracle REST Data Services (ORDS) version.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_STANDBY_SUMMARY_T Type

Autonomous Data Guard standby database details.

Syntax
```

```

Fields

Field Description

`lag_time_in_seconds`

(optional) The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine the potential data loss in the event of a failover.

`lifecycle_state`

(optional) The current state of the Autonomous Database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'UNAVAILABLE', 'RESTORE_IN_PROGRESS', 'RESTORE_FAILED', 'BACKUP_IN_PROGRESS', 'SCALE_IN_PROGRESS', 'AVAILABLE_NEEDS_ATTENTION', 'UPDATING', 'MAINTENANCE_IN_PROGRESS', 'RESTARTING', 'RECREATING', 'ROLE_CHANGE_IN_PROGRESS', 'UPGRADING', 'INACCESSIBLE', 'STANDBY'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_data_guard_role_changed`

(optional) The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.

`time_disaster_recovery_role_changed`

(optional) The date and time the Disaster Recovery role was switched for the standby Autonomous Database.

### DBMS_CLOUD_OCI_DATABASE_CUSTOMER_CONTACT_T Type

Customer contact information that will be used by Oracle to provide notifications needed by database and infrastructure administrators.

Syntax
```

```

Fields

Field Description

`email`

(optional) The email address used by Oracle to send notifications regarding databases and infrastructure.

### DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SUMMARY_T Type

The configuration details for resource pool

Syntax
```

```

Fields

Field Description

`pool_size`

(optional) Resource pool size.

`is_disabled`

(optional) Indicates if the resource pool should be deleted for the Autonomous Database.

### DBMS_CLOUD_OCI_DATABASE_SCHEDULED_OPERATION_DETAILS_T Type

Details of scheduled operation.

Syntax
```

```

Fields

Field Description

`day_of_week`

(required)

`scheduled_start_time`

(optional) auto start time. value must be of ISO-8601 format \"HH:mm\"

`scheduled_stop_time`

(optional) auto stop time. value must be of ISO-8601 format \"HH:mm\"

### DBMS_CLOUD_OCI_DATABASE_DATABASE_TOOL_T Type

Summary of database tools of autonomous database.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of database tool.

Allowed values are: 'APEX', 'DATABASE_ACTIONS', 'GRAPH_STUDIO', 'OML', 'DATA_TRANSFORMS', 'ORDS', 'MONGODB_API'

`is_enabled`

(optional) Indicates whether tool is enabled.

`compute_count`

(optional) Compute used by database tools.

`max_idle_time_in_minutes`

(optional) The max idle time, in minutes, after which the VM used by database tools will be terminated.

### DBMS_CLOUD_OCI_DATABASE_DISASTER_RECOVERY_CONFIGURATION_T Type

Configurations of a Disaster Recovery.

Syntax
```

```

Fields

Field Description

`disaster_recovery_type`

(optional) Indicates the disaster recovery (DR) type of the Autonomous Database Serverless instance. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

Allowed values are: 'ADG', 'BACKUP_BASED'

`time_snapshot_standby_enabled_till`

(optional) Time and date stored as an RFC 3339 formatted timestamp string. For example, 2022-01-01T12:00:00.000Z would set a limit for the snapshot standby to be converted back to a cross-region standby database.

`is_snapshot_standby`

(optional) Indicates if user wants to convert to a snapshot standby. For example, true would set a standby database to snapshot standby database. False would set a snapshot standby database back to regular standby database.

### DBMS_CLOUD_OCI_DATABASE_CUSTOMER_CONTACT_TBL Type

Nested table type of dbms_cloud_oci_database_customer_contact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_SCHEDULED_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_scheduled_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_DATABASE_TOOL_TBL Type

Nested table type of dbms_cloud_oci_database_database_tool_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_T Type

An Oracle Autonomous Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current state of the Autonomous Database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'UNAVAILABLE', 'RESTORE_IN_PROGRESS', 'RESTORE_FAILED', 'BACKUP_IN_PROGRESS', 'SCALE_IN_PROGRESS', 'AVAILABLE_NEEDS_ATTENTION', 'UPDATING', 'MAINTENANCE_IN_PROGRESS', 'RESTARTING', 'RECREATING', 'ROLE_CHANGE_IN_PROGRESS', 'UPGRADING', 'INACCESSIBLE', 'STANDBY'

`lifecycle_details`

(optional) Information about the current lifecycle state.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`kms_key_lifecycle_details`

(optional) KMS key lifecycle details.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`db_name`

(required) The database name.

`character_set`

(optional) The character set for the autonomous database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS

`ncharacter_set`

(optional) The national character set for the autonomous database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.

`in_memory_percentage`

(optional) The percentage of the System Global Area(SGA) assigned to In-Memory tables in Autonomous Database.

`in_memory_area_in_g_bs`

(optional) The area assigned to In-Memory tables in Autonomous Database.

`next_long_term_backup_time_stamp`

(optional) The date and time when the next long-term backup would be created.

`long_term_backup_schedule`

(optional)

`is_free_tier`

(optional) Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isLocalDataGuardEnabled

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`time_reclamation_of_free_autonomous_database`

(optional) The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the database will automatically be put into the STOPPED state.

`time_deletion_of_free_autonomous_database`

(optional) The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and without activity until this time, it will be deleted.

`backup_config`

(optional)

`key_history_entry`

(optional) Key History Entry.

`cpu_core_count`

(optional) The number of OCPU cores to be made available to the database. When the ECPU is selected, the value for cpuCoreCount is 0. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. **Note:** This parameter cannot be used with the `ocpuCount` parameter.

`local_adg_auto_failover_max_data_loss_limit`

(optional) Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard

`compute_model`

(optional) The compute model of the Autonomous Database. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value.

Allowed values are: 'ECPU', 'OCPU'

`compute_count`

(optional) The compute amount available to the database. Minimum and maximum values depend on the compute model and whether the database is an Autonomous Database Serverless instance or an Autonomous Database on Dedicated Exadata Infrastructure. For an Autonomous Database Serverless instance, the 'ECPU' compute model requires values in multiples of two. Required when using the `computeModel` parameter. When using `cpuCoreCount` parameter, it is an error to specify computeCount to a non-null value.

`backup_retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`total_backup_storage_size_in_g_bs`

(optional) The backup storage to the database.

`ocpu_count`

(optional) The number of OCPU cores to be made available to the database. The following points apply: - For Autonomous Databases on Dedicated Exadata Infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Database Serverless instances.) - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure. For Autonomous Databases on Dedicated Exadata Infrastructure, the maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html)for shape details. **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

`provisionable_cpus`

(optional) An array of CPU values that an Autonomous Database can be scaled to.

`data_storage_size_in_t_bs`

(required) The quantity of data in the database, in terabytes.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) enabled per OCPU or ECPU.

`data_storage_size_in_g_bs`

(optional) The quantity of data in the database, in gigabytes.

`used_data_storage_size_in_g_bs`

(optional) The storage space consumed by Autonomous Database in GBs.

`infrastructure_type`

(optional) The infrastructure type this resource belongs to.

Allowed values are: 'CLOUD', 'CLOUD_AT_CUSTOMER'

`is_dedicated`

(optional) True if the database uses[dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).

`autonomous_container_database_id`

(optional) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_created`

(optional) The date and time the Autonomous Database was created.

`display_name`

(optional) The user-friendly name for the Autonomous Database. The name does not have to be unique.

`service_console_url`

(optional) The URL of the Service Console for the Autonomous Database.

`connection_strings`

(optional) The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.

`connection_urls`

(optional)

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`used_data_storage_size_in_t_bs`

(optional) The amount of storage that has been used, in terabytes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the resource is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. - For Autonomous Database, setting this will disable public secure access to the database. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`private_endpoint`

(optional) The private endpoint for the resource.

`private_endpoint_label`

(optional) The resource's private endpoint label. Setting this to an empty string, after the creation of the private endpoint database, changes the private endpoint database to a public endpoint database. This setting cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`private_endpoint_ip`

(optional) The private endpoint Ip address for the resource.

`db_version`

(optional) A valid Oracle Database version for Autonomous Database.

`is_preview`

(optional) Indicates if the Autonomous Database version is a preview version.

`db_workload`

(optional) The Autonomous Database workload type. The following values are valid: - OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`is_access_control_enabled`

(optional) Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional, if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone. This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.

`whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`are_primary_whitelisted_ips_used`

(optional) This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled. It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby. It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.

`standby_whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`apex_details`

(optional) Information about Oracle APEX Application Development.

`is_auto_scaling_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database CPU core count.

`data_safe_status`

(optional) Status of the Data Safe registration for this Autonomous Database.

Allowed values are: 'REGISTERING', 'REGISTERED', 'DEREGISTERING', 'NOT_REGISTERED', 'FAILED'

`operations_insights_status`

(optional) Status of Operations Insights for this Autonomous Database.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`database_management_status`

(optional) Status of Database Management for this Autonomous Database.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`time_maintenance_begin`

(optional) The date and time when maintenance will begin.

`time_maintenance_end`

(optional) The date and time when maintenance will end.

`is_refreshable_clone`

(optional) Indicates if the Autonomous Database is a refreshable clone. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`time_of_last_refresh`

(optional) The date and time when last refresh happened.

`time_of_last_refresh_point`

(optional) The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the refresh point is not included in the refresh.

`time_of_next_refresh`

(optional) The date and time of next refresh.

`open_mode`

(optional) Indicates the Autonomous Database mode. The database can be opened in `READ_ONLY` or `READ_WRITE` mode. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'READ_ONLY', 'READ_WRITE'

`refreshable_status`

(optional) The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous Database.

Allowed values are: 'REFRESHING', 'NOT_REFRESHING'

`refreshable_mode`

(optional) The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

Allowed values are: 'AUTOMATIC', 'MANUAL'

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that was cloned to create the current Autonomous Database.

`permission_level`

(optional) The Autonomous Database permission level. Restricted mode allows access only by admin users. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'RESTRICTED', 'UNRESTRICTED'

`time_of_last_switchover`

(optional) The timestamp of the last switchover operation for the Autonomous Database.

`time_of_last_failover`

(optional) The timestamp of the last failover operation.

`is_data_guard_enabled`

(optional) **Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`failed_data_recovery_in_seconds`

(optional) Indicates the number of seconds of data loss for a Data Guard failover.

`standby_db`

(optional) **Deprecated** Autonomous Data Guard standby database details.

`is_local_data_guard_enabled`

(optional) Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`is_remote_data_guard_enabled`

(optional) Indicates whether the Autonomous Database has Cross Region Data Guard enabled. Not applicable to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`local_standby_db`

(optional)

`role`

(optional) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`available_upgrade_versions`

(optional) List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

`supported_regions_to_clone_to`

(optional) The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.

`customer_contacts`

(optional) Customer Contacts.

`time_local_data_guard_enabled`

(optional) The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.

`dataguard_region_type`

(optional) The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Database Serverless, Autonomous Data Guard associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby regions in Autonomous Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database administrative operations may be available only in the primary region of the Autonomous Data Guard association, and cannot be performed when the database using the primary role is operating in a remote Autonomous Data Guard standby region.

Allowed values are: 'PRIMARY_DG_REGION', 'REMOTE_STANDBY_DG_REGION'

`time_data_guard_role_changed`

(optional) The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the \"primary\" role in the primary Data Guard region, or database located in the remote Data Guard standby region.

`peer_db_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for Autonomous Database Serverless instances, standby databases located in the same region as the source primary database do not have OCIDs.

`is_mtls_connection_required`

(optional) Specifies if the Autonomous Database requires mTLS connections. This may not be updated in parallel with any of the following: licenseModel, databaseEdition, cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, whitelistedIps, openMode, permissionLevel, db-workload, privateEndpointLabel, nsgIds, customerContacts, dbVersion, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier. Service Change: The default value of the isMTLSConnectionRequired attribute will change from true to false on July 1, 2023 in the following APIs: - CreateAutonomousDatabase - GetAutonomousDatabase - UpdateAutonomousDatabase Details: Prior to the July 1, 2023 change, the isMTLSConnectionRequired attribute default value was true. This applies to Autonomous Database Serverless. Does this impact me? If you use or maintain custom scripts or Terraform scripts referencing the CreateAutonomousDatabase, GetAutonomousDatabase, or UpdateAutonomousDatabase APIs, you want to check, and possibly modify, the scripts for the changed default value of the attribute. Should you choose not to leave your scripts unchanged, the API calls containing this attribute will continue to work, but the default value will switch from true to false. How do I make this change? Using either OCI SDKs or command line tools, update your custom scripts to explicitly set the isMTLSConnectionRequired attribute to true.

`time_of_joining_resource_pool`

(optional) The time the member joined the resource pool.

`resource_pool_leader_id`

(optional) The unique identifier for leader autonomous database OCID[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_pool_summary`

(optional)

`is_reconnect_clone_enabled`

(optional) Indicates if the refreshable clone can be reconnected to its source database.

`time_until_reconnect_clone_enabled`

(optional) The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected to its source database.

`autonomous_maintenance_schedule_type`

(optional) The maintenance schedule type of the Autonomous Database Serverless. An EARLY maintenance schedule follows a schedule applying patches prior to the REGULAR schedule. A REGULAR maintenance schedule follows the normal cycle

Allowed values are: 'EARLY', 'REGULAR'

`scheduled_operations`

(optional) The list of scheduled operations. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`is_auto_scaling_for_storage_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.

`allocated_storage_size_in_t_bs`

(optional) The amount of storage currently allocated for the database tables and billed for, rounded up. When auto-scaling is not enabled, this value is equal to the `dataStorageSizeInTBs` value. You can compare this value to the `actualUsedDataStorageSizeInTBs` value to determine if a manual shrink operation is appropriate for your allocated storage. **Note:** Auto-scaling does not automatically decrease allocated storage when data is deleted from the database.

`actual_used_data_storage_size_in_t_bs`

(optional) The current amount of storage in use for user and system data, in terabytes (TB).

`max_cpu_core_count`

(optional) The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.

`database_edition`

(optional) The Oracle Database Edition that applies to the Autonomous databases.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`db_tools_details`

(optional) The list of database tools details. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, isLocalDataGuardEnabled, or isFreeTier.

`local_disaster_recovery_type`

(optional) Indicates the local disaster recovery (DR) type of the Autonomous Database Serverless instance. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

`disaster_recovery_region_type`

(optional) The disaster recovery (DR) region type of the Autonomous Database. For Autonomous Database Serverless instances, DR associations have designated primary and standby regions. These region types do not change when the database changes roles. The standby region in DR associations can be the same region as the primary region, or they can be in a remote regions. Some database administration operations may be available only in the primary region of the DR association, and cannot be performed when the database using the primary role is operating in a remote region.

Allowed values are: 'PRIMARY', 'REMOTE'

`time_disaster_recovery_role_changed`

(optional) The date and time the Disaster Recovery role was switched for the standby Autonomous Database.

`remote_disaster_recovery_configuration`

(optional)

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_BACKUP_T Type

An Autonomous Database backup.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database backup.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`autonomous_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database.

`display_name`

(required) The user-friendly name for the backup. The name does not have to be unique.

`l_type`

(required) The type of backup.

Allowed values are: 'INCREMENTAL', 'FULL', 'LONGTERM'

`is_automatic`

(required) Indicates whether the backup is user-initiated or automatic.

`time_started`

(optional) The date and time the backup started.

`time_ended`

(optional) The date and time the backup completed.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`database_size_in_t_bs`

(optional) The size of the database in terabytes at the time the backup was taken.

`lifecycle_state`

(required) The current state of the backup.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`is_restorable`

(optional) Indicates whether the backup can be used to restore the associated Autonomous Database.

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`time_available_till`

(optional) Timestamp until when the backup will be available

`db_version`

(optional) A valid Oracle Database version for Autonomous Database.

`size_in_t_bs`

(optional) The backup size in terrabytes (TB).

`backup_destination_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_BACKUP_SUMMARY_T Type

An Autonomous Database backup. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database backup.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`autonomous_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database.

`display_name`

(required) The user-friendly name for the backup. The name does not have to be unique.

`l_type`

(required) The type of backup.

Allowed values are: 'INCREMENTAL', 'FULL', 'LONGTERM'

`is_automatic`

(required) Indicates whether the backup is user-initiated or automatic.

`time_started`

(optional) The date and time the backup started.

`time_ended`

(optional) The date and time the backup completed.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`database_size_in_t_bs`

(optional) The size of the database in terabytes at the time the backup was taken.

`lifecycle_state`

(required) The current state of the backup.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`is_restorable`

(optional) Indicates whether the backup can be used to restore the associated Autonomous Database.

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`time_available_till`

(optional) Timestamp until when the backup will be available

`db_version`

(optional) A valid Oracle Database version for Autonomous Database.

`size_in_t_bs`

(optional) The backup size in terrabytes (TB).

`backup_destination_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CHARACTER_SETS_T Type

The Oracle Autonomous Database supported character sets. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(optional) A valid Oracle character set.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CONSOLE_TOKEN_DETAILS_T Type

The token that allows the OCI Console to access the Autonomous Database Service Console.

Syntax
```

```

Fields

Field Description

`token`

(optional) The token that allows the OCI Console to access the Autonomous Transaction Processing Service Console.

`login_url`

(optional) The login URL that allows the OCI Console to access the Autonomous Transaction Processing Service Console.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_DATAGUARD_ASSOCIATION_T Type

The properties that define dataguard association between two different Autonomous Databases. Note that Autonomous Databases inherit DataGuard association from parent Autonomous Container Database. No actions can be taken on AutonomousDatabaseDataguardAssociation, usage is strictly informational.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Autonomous Dataguard created for Autonomous Container Database where given Autonomous Database resides in.

`autonomous_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database that has a relationship with the peer Autonomous Database.

`role`

(required) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`lifecycle_state`

(required) The current state of Autonomous Data Guard.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ROLE_CHANGE_IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'FAILED', 'UNAVAILABLE', 'UPDATING'

`lifecycle_details`

(optional) Additional information about the current lifecycleState, if available.

`peer_role`

(required) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`peer_autonomous_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer Autonomous Database.

`peer_autonomous_database_life_cycle_state`

(optional) The current state of Autonomous Data Guard.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'ROLE_CHANGE_IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'FAILED', 'UNAVAILABLE', 'UPDATING'

`protection_mode`

(optional) The protection mode of this Autonomous Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE'

`apply_lag`

(optional) The lag time between updates to the primary database and application of the redo data on the standby database, as computed by the reporting database. Example: `9 seconds`

`apply_rate`

(optional) The rate at which redo logs are synced between the associated databases. Example: `180 Mb per second`

`is_automatic_failover_enabled`

(optional) Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association

`transport_lag`

(optional) The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database, as computed by the reporting database. Example: `7 seconds`

`time_last_synced`

(optional) The date and time of the last update to the apply lag, apply rate, and transport lag values.

`time_created`

(optional) The date and time the Data Guard association was created.

`time_last_role_changed`

(optional) The date and time when the last role change action happened.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_MANUAL_REFRESH_DETAILS_T Type

Details of manual refresh for an Autonomous Database refreshable clone.

Syntax
```

```

Fields

Field Description

`time_refresh_cutoff`

(optional) The timestamp to which the Autonomous Database refreshable clone will be refreshed. Changes made in the primary database after this timestamp are not part of the data refresh.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_SUMMARY_T Type

An Oracle Autonomous Database. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current state of the Autonomous Database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'UNAVAILABLE', 'RESTORE_IN_PROGRESS', 'RESTORE_FAILED', 'BACKUP_IN_PROGRESS', 'SCALE_IN_PROGRESS', 'AVAILABLE_NEEDS_ATTENTION', 'UPDATING', 'MAINTENANCE_IN_PROGRESS', 'RESTARTING', 'RECREATING', 'ROLE_CHANGE_IN_PROGRESS', 'UPGRADING', 'INACCESSIBLE', 'STANDBY'

`lifecycle_details`

(optional) Information about the current lifecycle state.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`kms_key_lifecycle_details`

(optional) KMS key lifecycle details.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`db_name`

(required) The database name.

`character_set`

(optional) The character set for the autonomous database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS

`ncharacter_set`

(optional) The national character set for the autonomous database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.

`in_memory_percentage`

(optional) The percentage of the System Global Area(SGA) assigned to In-Memory tables in Autonomous Database.

`in_memory_area_in_g_bs`

(optional) The area assigned to In-Memory tables in Autonomous Database.

`next_long_term_backup_time_stamp`

(optional) The date and time when the next long-term backup would be created.

`long_term_backup_schedule`

(optional)

`is_free_tier`

(optional) Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isLocalDataGuardEnabled

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`time_reclamation_of_free_autonomous_database`

(optional) The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the database will automatically be put into the STOPPED state.

`time_deletion_of_free_autonomous_database`

(optional) The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and without activity until this time, it will be deleted.

`backup_config`

(optional)

`key_history_entry`

(optional) Key History Entry.

`cpu_core_count`

(optional) The number of OCPU cores to be made available to the database. When the ECPU is selected, the value for cpuCoreCount is 0. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. **Note:** This parameter cannot be used with the `ocpuCount` parameter.

`local_adg_auto_failover_max_data_loss_limit`

(optional) Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard

`compute_model`

(optional) The compute model of the Autonomous Database. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value.

Allowed values are: 'ECPU', 'OCPU'

`compute_count`

(optional) The compute amount available to the database. Minimum and maximum values depend on the compute model and whether the database is an Autonomous Database Serverless instance or an Autonomous Database on Dedicated Exadata Infrastructure. For an Autonomous Database Serverless instance, the 'ECPU' compute model requires values in multiples of two. Required when using the `computeModel` parameter. When using `cpuCoreCount` parameter, it is an error to specify computeCount to a non-null value.

`backup_retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`total_backup_storage_size_in_g_bs`

(optional) The backup storage to the database.

`ocpu_count`

(optional) The number of OCPU cores to be made available to the database. The following points apply: - For Autonomous Databases on Dedicated Exadata Infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Database Serverless instances.) - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure. For Autonomous Databases on Dedicated Exadata Infrastructure, the maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html)for shape details. **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

`provisionable_cpus`

(optional) An array of CPU values that an Autonomous Database can be scaled to.

`data_storage_size_in_t_bs`

(required) The quantity of data in the database, in terabytes.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) enabled per OCPU or ECPU.

`data_storage_size_in_g_bs`

(optional) The quantity of data in the database, in gigabytes.

`used_data_storage_size_in_g_bs`

(optional) The storage space consumed by Autonomous Database in GBs.

`infrastructure_type`

(optional) The infrastructure type this resource belongs to.

Allowed values are: 'CLOUD', 'CLOUD_AT_CUSTOMER'

`is_dedicated`

(optional) True if the database uses[dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).

`autonomous_container_database_id`

(optional) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`time_created`

(optional) The date and time the Autonomous Database was created.

`display_name`

(optional) The user-friendly name for the Autonomous Database. The name does not have to be unique.

`service_console_url`

(optional) The URL of the Service Console for the Autonomous Database.

`connection_strings`

(optional) The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.

`connection_urls`

(optional)

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`used_data_storage_size_in_t_bs`

(optional) The amount of storage that has been used, in terabytes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the resource is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. - For Autonomous Database, setting this will disable public secure access to the database. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`private_endpoint`

(optional) The private endpoint for the resource.

`private_endpoint_label`

(optional) The resource's private endpoint label. Setting this to an empty string, after the creation of the private endpoint database, changes the private endpoint database to a public endpoint database. This setting cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`private_endpoint_ip`

(optional) The private endpoint Ip address for the resource.

`db_version`

(optional) A valid Oracle Database version for Autonomous Database.

`is_preview`

(optional) Indicates if the Autonomous Database version is a preview version.

`db_workload`

(optional) The Autonomous Database workload type. The following values are valid: - OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`is_access_control_enabled`

(optional) Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional, if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone. This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.

`whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`are_primary_whitelisted_ips_used`

(optional) This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled. It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby. It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.

`standby_whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`apex_details`

(optional) Information about Oracle APEX Application Development.

`is_auto_scaling_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database CPU core count.

`data_safe_status`

(optional) Status of the Data Safe registration for this Autonomous Database.

Allowed values are: 'REGISTERING', 'REGISTERED', 'DEREGISTERING', 'NOT_REGISTERED', 'FAILED'

`operations_insights_status`

(optional) Status of Operations Insights for this Autonomous Database.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`database_management_status`

(optional) Status of Database Management for this Autonomous Database.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`time_maintenance_begin`

(optional) The date and time when maintenance will begin.

`time_maintenance_end`

(optional) The date and time when maintenance will end.

`is_refreshable_clone`

(optional) Indicates if the Autonomous Database is a refreshable clone. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`time_of_last_refresh`

(optional) The date and time when last refresh happened.

`time_of_last_refresh_point`

(optional) The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the refresh point is not included in the refresh.

`time_of_next_refresh`

(optional) The date and time of next refresh.

`open_mode`

(optional) Indicates the Autonomous Database mode. The database can be opened in `READ_ONLY` or `READ_WRITE` mode. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'READ_ONLY', 'READ_WRITE'

`refreshable_status`

(optional) The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous Database.

Allowed values are: 'REFRESHING', 'NOT_REFRESHING'

`refreshable_mode`

(optional) The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

Allowed values are: 'AUTOMATIC', 'MANUAL'

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that was cloned to create the current Autonomous Database.

`permission_level`

(optional) The Autonomous Database permission level. Restricted mode allows access only by admin users. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'RESTRICTED', 'UNRESTRICTED'

`time_of_last_switchover`

(optional) The timestamp of the last switchover operation for the Autonomous Database.

`time_of_last_failover`

(optional) The timestamp of the last failover operation.

`is_data_guard_enabled`

(optional) **Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`failed_data_recovery_in_seconds`

(optional) Indicates the number of seconds of data loss for a Data Guard failover.

`standby_db`

(optional) **Deprecated** Autonomous Data Guard standby database details.

`is_local_data_guard_enabled`

(optional) Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`is_remote_data_guard_enabled`

(optional) Indicates whether the Autonomous Database has Cross Region Data Guard enabled. Not applicable to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`local_standby_db`

(optional)

`role`

(optional) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`available_upgrade_versions`

(optional) List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

`supported_regions_to_clone_to`

(optional) The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.

`customer_contacts`

(optional) Customer Contacts.

`time_local_data_guard_enabled`

(optional) The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.

`dataguard_region_type`

(optional) The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Database Serverless, Autonomous Data Guard associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby regions in Autonomous Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database administrative operations may be available only in the primary region of the Autonomous Data Guard association, and cannot be performed when the database using the primary role is operating in a remote Autonomous Data Guard standby region.

Allowed values are: 'PRIMARY_DG_REGION', 'REMOTE_STANDBY_DG_REGION'

`time_data_guard_role_changed`

(optional) The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the \"primary\" role in the primary Data Guard region, or database located in the remote Data Guard standby region.

`peer_db_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for Autonomous Database Serverless instances, standby databases located in the same region as the source primary database do not have OCIDs.

`is_mtls_connection_required`

(optional) Specifies if the Autonomous Database requires mTLS connections. This may not be updated in parallel with any of the following: licenseModel, databaseEdition, cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, whitelistedIps, openMode, permissionLevel, db-workload, privateEndpointLabel, nsgIds, customerContacts, dbVersion, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier. Service Change: The default value of the isMTLSConnectionRequired attribute will change from true to false on July 1, 2023 in the following APIs: - CreateAutonomousDatabase - GetAutonomousDatabase - UpdateAutonomousDatabase Details: Prior to the July 1, 2023 change, the isMTLSConnectionRequired attribute default value was true. This applies to Autonomous Database Serverless. Does this impact me? If you use or maintain custom scripts or Terraform scripts referencing the CreateAutonomousDatabase, GetAutonomousDatabase, or UpdateAutonomousDatabase APIs, you want to check, and possibly modify, the scripts for the changed default value of the attribute. Should you choose not to leave your scripts unchanged, the API calls containing this attribute will continue to work, but the default value will switch from true to false. How do I make this change? Using either OCI SDKs or command line tools, update your custom scripts to explicitly set the isMTLSConnectionRequired attribute to true.

`time_of_joining_resource_pool`

(optional) The time the member joined the resource pool.

`resource_pool_leader_id`

(optional) The unique identifier for leader autonomous database OCID[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_pool_summary`

(optional)

`is_reconnect_clone_enabled`

(optional) Indicates if the refreshable clone can be reconnected to its source database.

`time_until_reconnect_clone_enabled`

(optional) The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected to its source database.

`autonomous_maintenance_schedule_type`

(optional) The maintenance schedule type of the Autonomous Database Serverless. An EARLY maintenance schedule follows a schedule applying patches prior to the REGULAR schedule. A REGULAR maintenance schedule follows the normal cycle

Allowed values are: 'EARLY', 'REGULAR'

`scheduled_operations`

(optional) The list of scheduled operations. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`is_auto_scaling_for_storage_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.

`allocated_storage_size_in_t_bs`

(optional) The amount of storage currently allocated for the database tables and billed for, rounded up. When auto-scaling is not enabled, this value is equal to the `dataStorageSizeInTBs` value. You can compare this value to the `actualUsedDataStorageSizeInTBs` value to determine if a manual shrink operation is appropriate for your allocated storage. **Note:** Auto-scaling does not automatically decrease allocated storage when data is deleted from the database.

`actual_used_data_storage_size_in_t_bs`

(optional) The current amount of storage in use for user and system data, in terabytes (TB).

`max_cpu_core_count`

(optional) The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.

`database_edition`

(optional) The Oracle Database Edition that applies to the Autonomous databases.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION'

`db_tools_details`

(optional) The list of database tools details. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, isLocalDataGuardEnabled, or isFreeTier.

`local_disaster_recovery_type`

(optional) Indicates the local disaster recovery (DR) type of the Autonomous Database Serverless instance. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

`disaster_recovery_region_type`

(optional) The disaster recovery (DR) region type of the Autonomous Database. For Autonomous Database Serverless instances, DR associations have designated primary and standby regions. These region types do not change when the database changes roles. The standby region in DR associations can be the same region as the primary region, or they can be in a remote regions. Some database administration operations may be available only in the primary region of the DR association, and cannot be performed when the database using the primary role is operating in a remote region.

Allowed values are: 'PRIMARY', 'REMOTE'

`time_disaster_recovery_role_changed`

(optional) The date and time the Disaster Recovery role was switched for the standby Autonomous Database.

`remote_disaster_recovery_configuration`

(optional)

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_WALLET_T Type

The Autonomous Database wallet details.

Syntax
```

```

Fields

Field Description

`lifecycle_state`

(optional) The current lifecycle state of the Autonomous Database wallet.

Allowed values are: 'ACTIVE', 'UPDATING'

`time_rotated`

(optional) The date and time the wallet was last rotated.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DB_PREVIEW_VERSION_SUMMARY_T Type

The Autonomous Database preview version. Note that preview version software is only available for[Autonomous Database Serverless instances](https://docs.oracle.com/en/cloud/paas/autonomous-database/shared/index.html).

Syntax
```

```

Fields

Field Description

`version`

(required) A valid Autonomous Database preview version.

`time_preview_begin`

(optional) The date and time when the preview version availability begins.

`time_preview_end`

(optional) The date and time when the preview version availability ends.

`db_workload`

(optional) The Autonomous Database workload type. The following values are valid: - OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`details`

(optional) A URL that points to a detailed description of the preview version.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DB_VERSION_SUMMARY_T Type

The supported Autonomous Database version.

Syntax
```

```

Fields

Field Description

`version`

(required) A valid Oracle Database version for Autonomous Database.

`db_workload`

(optional) The Autonomous Database workload type. The following values are valid: - OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`is_dedicated`

(optional) True if the database uses[dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).

`details`

(optional) A URL that points to a detailed description of the Autonomous Database version.

`is_free_tier_enabled`

(optional) True if this version of the Oracle Database software can be used for Always-Free Autonomous Databases.

`is_paid_enabled`

(optional) True if this version of the Oracle Database software has payments enabled.

`is_default_for_free`

(optional) True if this version of the Oracle Database software's default is free.

`is_default_for_paid`

(optional) True if this version of the Oracle Database software's default is paid.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Autonomous Exadata Infrastructure.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-friendly name for the Autonomous Exadata Infrastructure.

`availability_domain`

(required) The name of the availability domain that the Autonomous Exadata Infrastructure is located in.

`subnet_id`

(required) The OCID of the subnet the Autonomous Exadata Infrastructure is associated with. **Subnet Restrictions:** - For Autonomous Databases with Autonomous Exadata Infrastructure, do not use a subnet that overlaps with 192.168.128.0/20 These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`shape`

(required) The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage).

`hostname`

(required) The host name for the Autonomous Exadata Infrastructure node.

`domain`

(required) The domain name for the Autonomous Exadata Infrastructure.

`lifecycle_state`

(required) The current lifecycle state of the Autonomous Exadata Infrastructure.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the Autonomous Exadata Infrastructure.

`license_model`

(optional) The Oracle license model that applies to all databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`time_created`

(optional) The date and time the Autonomous Exadata Infrastructure was created.

`maintenance_window`

(required)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`scan_dns_name`

(optional) The FQDN of the DNS record for the SCAN IP addresses that are associated with the Autonomous Exadata Infrastructure.

`zone_id`

(optional) The OCID of the zone the Autonomous Exadata Infrastructure is associated with.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_SHAPE_SUMMARY_T Type

The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the shape used for the Autonomous Exadata Infrastructure.

`available_core_count`

(required) The maximum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.

`minimum_core_count`

(optional) The minimum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.

`core_count_increment`

(optional) The increment in which core count can be increased or decreased.

`minimum_node_count`

(optional) The minimum number of nodes available for the shape.

`maximum_node_count`

(optional) The maximum number of nodes available for the shape.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_SUMMARY_T Type

**Deprecated** These APIs are deprecated with the introduction of the Autonomous Exadata VM Cluster resource and a shift to a common Exadata Infrastructure resource for all Exadata Cloud-based services, including Autonomous Database on dedicated Exadata infrastructure. For more details, see[Latest Resource Model](https://docs.oracle.com/en/cloud/paas/autonomous-database/flddd/#articletitle). Infrastructure that enables the running of multiple Autonomous Databases within a dedicated DB system. For more information about Autonomous Exadata Infrastructure, see[Oracle Autonomous Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the ListAvailabilityDomains operation in the Identity service API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Autonomous Exadata Infrastructure.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-friendly name for the Autonomous Exadata Infrastructure.

`availability_domain`

(required) The name of the availability domain that the Autonomous Exadata Infrastructure is located in.

`subnet_id`

(required) The OCID of the subnet the Autonomous Exadata Infrastructure is associated with. **Subnet Restrictions:** - For Autonomous Databases with Autonomous Exadata Infrastructure, do not use a subnet that overlaps with 192.168.128.0/20 These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`shape`

(required) The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage).

`hostname`

(required) The host name for the Autonomous Exadata Infrastructure node.

`domain`

(required) The domain name for the Autonomous Exadata Infrastructure.

`lifecycle_state`

(required) The current lifecycle state of the Autonomous Exadata Infrastructure.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the Autonomous Exadata Infrastructure.

`license_model`

(optional) The Oracle license model that applies to all databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`time_created`

(optional) The date and time the Autonomous Exadata Infrastructure was created.

`maintenance_window`

(required)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`scan_dns_name`

(optional) The FQDN of the DNS record for the SCAN IP addresses that are associated with the Autonomous Exadata Infrastructure.

`zone_id`

(optional) The OCID of the zone the Autonomous Exadata Infrastructure is associated with.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_PATCH_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`description`

(required) The text describing this patch package.

`l_type`

(required) The type of patch. BUNDLE is one example.

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically can contain additional displayable text.

`lifecycle_state`

(optional) The current state of the patch as a result of lastAction.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time that the patch was released.

`version`

(required) The version of this patch package.

`patch_model`

(optional) Database patching model preference. See[My Oracle Support note 2285040.1](https://support.oracle.com/epmos/faces/DocumentDisplay)for information on the Release Update (RU) and Release Update Revision (RUR) patching models.

Allowed values are: 'RELEASE_UPDATES', 'RELEASE_UPDATE_REVISIONS'

`quarter`

(optional) First month of the quarter in which the patch was released.

`year`

(optional) Year in which the patch was released.

`autonomous_patch_type`

(optional) Maintenance run type, either \"QUARTERLY\" or \"TIMEZONE\".

Allowed values are: 'QUARTERLY', 'TIMEZONE'

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_PATCH_SUMMARY_T Type

A patch for an Autonomous Exadata Infrastructure or Autonomous Container Database. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`description`

(required) The text describing this patch package.

`l_type`

(required) The type of patch. BUNDLE is one example.

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically can contain additional displayable text.

`lifecycle_state`

(optional) The current state of the patch as a result of lastAction.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time that the patch was released.

`version`

(required) The version of this patch package.

`patch_model`

(optional) Database patching model preference. See[My Oracle Support note 2285040.1](https://support.oracle.com/epmos/faces/DocumentDisplay)for information on the Release Update (RU) and Release Update Revision (RUR) patching models.

Allowed values are: 'RELEASE_UPDATES', 'RELEASE_UPDATE_REVISIONS'

`quarter`

(optional) First month of the quarter in which the patch was released.

`year`

(optional) Year in which the patch was released.

`autonomous_patch_type`

(optional) Maintenance run type, either \"QUARTERLY\" or \"TIMEZONE\".

Allowed values are: 'QUARTERLY', 'TIMEZONE'

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VIRTUAL_MACHINE_T Type

Autonomous Virtual Machine details.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Virtual Machine.

`vm_name`

(optional) The name of the Autonomous Virtual Machine.

`db_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db server associated with the Autonomous Virtual Machine.

`db_server_display_name`

(optional) The display name of the dbServer associated with the Autonomous Virtual Machine.

`cpu_core_count`

(optional) The number of CPU cores enabled on the Autonomous Virtual Machine.

`memory_size_in_g_bs`

(optional) The allocated memory in GBs on the Autonomous Virtual Machine.

`db_node_storage_size_in_g_bs`

(optional) The allocated local node storage in GBs on the Autonomous Virtual Machine.

`lifecycle_state`

(required) The current state of the Autonomous Virtual Machine.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`client_ip_address`

(optional) Client IP Address.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM Cluster associated with the Autonomous Virtual Machine.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`cloud_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Autonomous VM Cluster associated with the Autonomous Virtual Machine.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VIRTUAL_MACHINE_SUMMARY_T Type

Details of the Autonomous Virtual Machine.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Virtual Machine.

`vm_name`

(optional) The name of the Autonomous Virtual Machine.

`db_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db server associated with the Autonomous Virtual Machine.

`db_server_display_name`

(optional) The display name of the dbServer associated with the Autonomous Virtual Machine.

`cpu_core_count`

(optional) The number of CPU cores enabled on the Autonomous Virtual Machine.

`memory_size_in_g_bs`

(optional) The allocated memory in GBs on the Autonomous Virtual Machine.

`db_node_storage_size_in_g_bs`

(optional) The allocated local node storage in GBs on the Autonomous Virtual Machine.

`lifecycle_state`

(required) The current state of the Autonomous Virtual Machine.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`client_ip_address`

(optional) Client IP Address.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM Cluster associated with the Autonomous Virtual Machine.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`cloud_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Autonomous VM Cluster associated with the Autonomous Virtual Machine.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_T Type

Details of the Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the Autonomous VM cluster was created.

`lifecycle_state`

(required) The current state of the Autonomous VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_zone`

(optional) The time zone to use for the Autonomous VM cluster. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`vm_cluster_network_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.

`cpus_enabled`

(optional) The number of enabled CPU cores.

`compute_model`

(optional) The compute model of the Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`ocpus_enabled`

(optional) The number of enabled OCPU cores.

`available_cpus`

(optional) The numnber of CPU cores available.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) to be enabled per OCPU or ECPU.

`cpu_core_count_per_node`

(optional) The number of CPU cores enabled per VM cluster node.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size allocated for Autonomous Databases, in TBs.

`maintenance_window`

(optional)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`cpu_percentage`

(optional) The percentage of total number of CPUs used in an Autonomous VM Cluster.

`autonomous_data_storage_percentage`

(optional) The percentage of the data storage used for the Autonomous Databases in an Autonomous VM Cluster.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`total_autonomous_data_storage_in_t_bs`

(optional) The total data disk group size for Autonomous Databases, in TBs.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`provisionable_autonomous_container_databases`

(optional) The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`provisioned_autonomous_container_databases`

(optional) The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.

`non_provisionable_autonomous_container_databases`

(optional) The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The total data storage allocated in TBs

`data_storage_size_in_g_bs`

(optional) The total data storage allocated in GBs.

`available_data_storage_size_in_t_bs`

(optional) **Deprecated.** Use `availableAutonomousDataStorageSizeInTBs` for Autonomous Databases' data storage availability in TBs.

`node_count`

(optional) The number of nodes in the Autonomous VM Cluster.

`license_model`

(optional) The Oracle license model that applies to the Autonomous VM cluster. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`reclaimable_cpus`

(optional) For Autonomous Databases on Dedicated Exadata Infrastructure: - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database. - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`available_container_databases`

(optional) The number of Autonomous Container Databases that can be created with the currently available local storage.

`available_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size available for Autonomous Databases, in TBs.

`scan_listener_port_tls`

(optional) The SCAN Listener TLS port number. Default value is 2484.

`scan_listener_port_non_tls`

(optional) The SCAN Listener Non TLS port number. Default value is 1521.

`is_mtls_enabled`

(optional) Enable mutual TLS(mTLS) authentication for database while provisioning a VMCluster. Default is TLS.

`time_database_ssl_certificate_expires`

(optional) The date and time of the Database SSL certificate expiration.

`time_ords_certificate_expires`

(optional) The date and time of the ORDS certificate expiration.

`exadata_storage_in_t_bs_lowest_scaled_value`

(optional) The lowest value to which exadataStorage in TBs can be scaled down.

`cpus_lowest_scaled_value`

(optional) The lowest value to which cpus can be scaled down.

`max_acds_lowest_scaled_value`

(optional) The lowest value to which ACDs can be scaled down.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_T Type

Unallocated resource details of the AVM

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`un_allocated_adb_storage_in_t_bs`

(required) Total unallocated autonomous data storage in the AVM in TBs.

### DBMS_CLOUD_OCI_DATABASE_AVM_ACD_RESOURCE_STATS_T Type

Associated autonomous container databases usages.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Container Database.

`display_name`

(required) The user-friendly name for the Autonomous Container Database. The name does not need to be unique.

`provisioned_cpus`

(optional) CPUs/cores assigned to Autonomous Databases in the ACD instances.

`available_cpus`

(optional) The number of CPU cores available.

`used_cpus`

(optional) CPUs/cores assigned to the ACD instance. Sum of provisioned, reserved and reclaimable CPUs/ cores to the ACD instance.

`reserved_cpus`

(optional) CPUs/cores reserved for scalability, resilliency and other overheads. This includes failover, autoscaling and idle instance overhead.

`reclaimable_cpus`

(optional) CPUs/cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.

### DBMS_CLOUD_OCI_DATABASE_AVM_ACD_RESOURCE_STATS_TBL Type

Nested table type of dbms_cloud_oci_database_avm_acd_resource_stats_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_RESOURCE_USAGE_T Type

Autonomous VM usage statistics.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM Cluster.

`display_name`

(required) The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.

`used_cpus`

(optional) The number of CPU cores alloted to the Autonomous Container Databases in an Cloud Autonomous VM cluster.

`available_cpus`

(optional) The number of CPU cores available.

`reclaimable_cpus`

(optional) CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`autonomous_container_database_usage`

(optional) Associated Autonomous Container Database Usages.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_RESOURCE_USAGE_TBL Type

Nested table type of dbms_cloud_oci_database_autonomous_vm_resource_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE_T Type

Autonomous VM Cluster usage details, including the Autonomous Container Databases usage.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM cluster.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size allocated for Autonomous Databases, in TBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created.

`available_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size available for Autonomous Databases, in TBs.

`used_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size used for Autonomous Databases, in TBs.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.

`exadata_storage_in_t_bs`

(optional) Total exadata storage allocated for the Autonomous VM Cluster. DATA + RECOVERY + SPARSE + any overhead in TBs.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) to be enabled per each CPU core.

`total_cpus`

(optional) The number of CPU cores enabled on the Autonomous VM cluster.

`used_cpus`

(optional) The number of CPU cores alloted to the Autonomous Container Databases in an Autonomous VM cluster.

`available_cpus`

(optional) The number of CPU cores available.

`reclaimable_cpus`

(optional) CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`provisionable_autonomous_container_databases`

(optional) The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`provisioned_autonomous_container_databases`

(optional) The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.

`non_provisionable_autonomous_container_databases`

(optional) The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`autonomous_vm_resource_usage`

(optional) List of autonomous vm cluster resource usages.

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_SUMMARY_T Type

Details of the Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the Autonomous VM cluster was created.

`lifecycle_state`

(required) The current state of the Autonomous VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_zone`

(optional) The time zone to use for the Autonomous VM cluster. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`vm_cluster_network_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.

`cpus_enabled`

(optional) The number of enabled CPU cores.

`compute_model`

(optional) The compute model of the Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`ocpus_enabled`

(optional) The number of enabled OCPU cores.

`available_cpus`

(optional) The numnber of CPU cores available.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) to be enabled per OCPU or ECPU.

`cpu_core_count_per_node`

(optional) The number of CPU cores enabled per VM cluster node.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size allocated for Autonomous Databases, in TBs.

`maintenance_window`

(optional)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`cpu_percentage`

(optional) The percentage of total number of CPUs used in an Autonomous VM Cluster.

`autonomous_data_storage_percentage`

(optional) The percentage of the data storage used for the Autonomous Databases in an Autonomous VM Cluster.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`total_autonomous_data_storage_in_t_bs`

(optional) The total data disk group size for Autonomous Databases, in TBs.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`provisionable_autonomous_container_databases`

(optional) The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`provisioned_autonomous_container_databases`

(optional) The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.

`non_provisionable_autonomous_container_databases`

(optional) The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The total data storage allocated in TBs

`data_storage_size_in_g_bs`

(optional) The total data storage allocated in GBs.

`available_data_storage_size_in_t_bs`

(optional) **Deprecated.** Use `availableAutonomousDataStorageSizeInTBs` for Autonomous Databases' data storage availability in TBs.

`node_count`

(optional) The number of nodes in the Autonomous VM Cluster.

`license_model`

(optional) The Oracle license model that applies to the Autonomous VM cluster. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`reclaimable_cpus`

(optional) For Autonomous Databases on Dedicated Exadata Infrastructure: - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database. - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`available_container_databases`

(optional) The number of Autonomous Container Databases that can be created with the currently available local storage.

`available_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size available for Autonomous Databases, in TBs.

`scan_listener_port_tls`

(optional) The SCAN Listener TLS port number. Default value is 2484.

`scan_listener_port_non_tls`

(optional) The SCAN Listener Non TLS port number. Default value is 1521.

`is_mtls_enabled`

(optional) Enable mutual TLS(mTLS) authentication for database while provisioning a VMCluster. Default is TLS.

`time_database_ssl_certificate_expires`

(optional) The date and time of the Database SSL certificate expiration.

`time_ords_certificate_expires`

(optional) The date and time of the ORDS certificate expiration.

`exadata_storage_in_t_bs_lowest_scaled_value`

(optional) The lowest value to which exadataStorage in TBs can be scaled down.

`cpus_lowest_scaled_value`

(optional) The lowest value to which cpus can be scaled down.

`max_acds_lowest_scaled_value`

(optional) The lowest value to which ACDs can be scaled down.

### DBMS_CLOUD_OCI_DATABASE_BACKUP_T Type

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`display_name`

(optional) The user-friendly name for the backup. The name does not have to be unique.

`l_type`

(optional) The type of backup.

Allowed values are: 'INCREMENTAL', 'FULL', 'VIRTUAL_FULL'

`time_started`

(optional) The date and time the backup started.

`time_ended`

(optional) The date and time the backup was completed.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`availability_domain`

(optional) The name of the availability domain where the database backup is stored.

`lifecycle_state`

(optional) The current state of the backup.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'RESTORING', 'CANCELING', 'CANCELED'

`database_edition`

(optional) The Oracle Database edition of the DB system from which the database backup was taken.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`database_size_in_g_bs`

(optional) The size of the database in gigabytes at the time the backup was taken.

`shape`

(optional) Shape of the backup's source database.

`version`

(optional) Version of the backup's source database

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

### DBMS_CLOUD_OCI_DATABASE_ASSOCIATED_DATABASE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_associated_database_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_T Type

Backup destination details.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`display_name`

(optional) The user-provided name of the backup destination.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`l_type`

(optional) Type of the backup destination.

Allowed values are: 'NFS', 'RECOVERY_APPLIANCE'

`associated_databases`

(optional) List of databases associated with the backup destination.

`connection_string`

(optional) For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.

`vpc_users`

(optional) For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.

`local_mount_point_path`

(optional) The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.

`nfs_mount_type`

(optional) NFS Mount type for backup destination.

Allowed values are: 'SELF_MOUNT', 'AUTOMATED_MOUNT'

`nfs_server`

(optional) Host names or IP addresses for NFS Auto mount.

`nfs_server_export`

(optional) Specifies the directory on which to mount the file system

`lifecycle_state`

(optional) The current lifecycle state of the backup destination.

Allowed values are: 'ACTIVE', 'FAILED', 'DELETED'

`time_created`

(optional) The date and time the backup destination was created.

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically contains additional displayable text

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_SUMMARY_T Type

Backup destination details, including the list of databases using the backup destination.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`display_name`

(optional) The user-provided name of the backup destination.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`l_type`

(optional) Type of the backup destination.

Allowed values are: 'NFS', 'RECOVERY_APPLIANCE'

`associated_databases`

(optional) List of databases associated with the backup destination.

`connection_string`

(optional) For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.

`vpc_users`

(optional) For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.

`local_mount_point_path`

(optional) The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.

`nfs_mount_type`

(optional) NFS Mount type for backup destination.

Allowed values are: 'SELF_MOUNT', 'AUTOMATED_MOUNT'

`nfs_server`

(optional) Host names or IP addresses for NFS Auto mount.

`nfs_server_export`

(optional) Specifies the directory on which to mount the file system

`lifecycle_state`

(optional) The current lifecycle state of the backup destination.

Allowed values are: 'ACTIVE', 'FAILED', 'DELETED'

`time_created`

(optional) The date and time the backup destination was created.

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically contains additional displayable text

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_BACKUP_SUMMARY_T Type

A database backup. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`display_name`

(optional) The user-friendly name for the backup. The name does not have to be unique.

`l_type`

(optional) The type of backup.

Allowed values are: 'INCREMENTAL', 'FULL', 'VIRTUAL_FULL'

`time_started`

(optional) The date and time the backup started.

`time_ended`

(optional) The date and time the backup was completed.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`availability_domain`

(optional) The name of the availability domain where the database backup is stored.

`lifecycle_state`

(optional) The current state of the backup.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'RESTORING', 'CANCELING', 'CANCELED'

`database_edition`

(optional) The Oracle Database edition of the DB system from which the database backup was taken.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`database_size_in_g_bs`

(optional) The size of the database in gigabytes at the time the backup was taken.

`shape`

(optional) Shape of the backup's source database.

`version`

(optional) Version of the backup's source database

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_AUTONOMOUS_VM_CLUSTER_COMPARTMENT_DETAILS_T Type

The configuration details for moving the Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the Autonomous VM cluster to.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_CLOUD_AUTONOMOUS_VM_CLUSTER_COMPARTMENT_DETAILS_T Type

The configuration details for moving the cloud Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_CLOUD_EXADATA_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type

The configuration details for moving the cloud Exadata infrastructure resource to another compartment. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_CLOUD_VM_CLUSTER_COMPARTMENT_DETAILS_T Type

The configuration details for moving the cloud VM cluster to another compartment. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_COMPARTMENT_DETAILS_T Type

The configuration details for moving the resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the resource to.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_DATAGUARD_ROLE_DETAILS_T Type

The configuration details for change Autonomous Container Database Dataguard role

Syntax
```

```

Fields

Field Description

`role`

(required) The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY', 'BACKUP_COPY', 'SNAPSHOT_STANDBY'

`autonomous_container_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`connection_strings_type`

(optional) type of connection strings when converting database to snapshot mode

Allowed values are: 'SNAPSHOT_SERVICES', 'PRIMARY_SERVICES'

### DBMS_CLOUD_OCI_DATABASE_CHANGE_DISASTER_RECOVERY_CONFIGURATION_DETAILS_T Type

Details to update the cross-region disaster recovery (DR) details of the standby Autonomous Database Serverless instance.

Syntax
```

```

Fields

Field Description

`disaster_recovery_type`

(optional) Indicates the disaster recovery (DR) type of the Autonomous Database Serverless instance. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

Allowed values are: 'ADG', 'BACKUP_BASED'

`time_snapshot_standby_enabled_till`

(optional) Time and date stored as an RFC 3339 formatted timestamp string. For example, 2022-01-01T12:00:00.000Z would set a limit for the snapshot standby to be converted back to a cross-region standby database.

`is_snapshot_standby`

(optional) Indicates if user wants to convert to a snapshot standby. For example, true would set a standby database to snapshot standby database. False would set a snapshot standby database back to regular standby database.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_EXADATA_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type

The configuration details for moving the resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the resource to.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_KEY_STORE_COMPARTMENT_DETAILS_T Type

The configuration details for moving the key store.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the key store to.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_KEY_STORE_TYPE_DETAILS_T Type

Request details to change the source of the encryption key for the database.

Syntax
```

```

Fields

Field Description

`key_store_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

### DBMS_CLOUD_OCI_DATABASE_CHANGE_VM_CLUSTER_COMPARTMENT_DETAILS_T Type

The configuration details for moving the VM cluster.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the VM cluster to.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_T Type

Details of the cloud Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Autonomous VM cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`description`

(optional) User defined description of the cloud Autonomous VM cluster.

`availability_domain`

(required) The name of the availability domain that the cloud Autonomous VM cluster is located in.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the cloud Autonomous VM Cluster is associated with. **Subnet Restrictions:** - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`last_update_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance update history. This value is updated when a maintenance update starts.

`lifecycle_state`

(required) The current state of the cloud Autonomous VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`display_name`

(required) The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the cloud Autonomous VM cluster was created.

`time_updated`

(optional) The last date and time that the cloud Autonomous VM cluster was updated.

`cluster_time_zone`

(optional) The time zone of the Cloud Autonomous VM Cluster.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`hostname`

(optional) The hostname for the cloud Autonomous VM cluster.

`domain`

(optional) The domain name for the cloud Autonomous VM cluster.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

`shape`

(optional) The model name of the Exadata hardware running the cloud Autonomous VM cluster.

`node_count`

(optional) The number of database servers in the cloud VM cluster.

`data_storage_size_in_t_bs`

(optional) The total data storage allocated, in terabytes (TB).

`data_storage_size_in_g_bs`

(optional) The total data storage allocated, in gigabytes (GB).

`cpu_core_count`

(optional) The number of CPU cores on the cloud Autonomous VM cluster.

`ocpu_count`

(optional) The number of CPU cores on the cloud Autonomous VM cluster. Only 1 decimal place is allowed for the fractional part.

`compute_model`

(optional) The compute model of the Cloud Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`is_mtls_enabled_vm_cluster`

(optional) Enable mutual TLS(mTLS) authentication for database at time of provisioning a VMCluster. This is applicable to database TLS Certificates only. Default is TLS

`cpu_core_count_per_node`

(optional) The number of CPU cores enabled per VM cluster node.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`maintenance_window`

(optional)

`scan_listener_port_tls`

(optional) The SCAN Listenenr TLS port. Default is 2484.

`scan_listener_port_non_tls`

(optional) The SCAN Listener Non TLS port. Default is 1521.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`time_database_ssl_certificate_expires`

(optional) The date and time of Database SSL certificate expiration.

`time_ords_certificate_expires`

(optional) The date and time of ORDS certificate expiration.

`available_cpus`

(optional) CPU cores available for allocation to Autonomous Databases.

`reclaimable_cpus`

(optional) For Autonomous Databases on Dedicated Exadata Infrastructure: - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database. - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`available_container_databases`

(optional) The number of Autonomous Container Databases that can be created with the currently available local storage.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created with the allocated local storage.

`available_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size available for Autonomous Databases, in TBs.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size allocated for Autonomous Databases, in TBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) enabled per OCPU or ECPU.

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`cpu_percentage`

(optional) The percentage of total number of CPUs used in an Autonomous VM Cluster.

`autonomous_data_storage_percentage`

(optional) The percentage of the data storage used for the Autonomous Databases in an Autonomous VM Cluster.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`total_cpus`

(optional) The total number of CPUs in an Autonomous VM Cluster.

`total_autonomous_data_storage_in_t_bs`

(optional) The total data disk group size for Autonomous Databases, in TBs.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`provisionable_autonomous_container_databases`

(optional) The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`provisioned_autonomous_container_databases`

(optional) The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.

`non_provisionable_autonomous_container_databases`

(optional) The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`exadata_storage_in_t_bs_lowest_scaled_value`

(optional) The lowest value to which exadataStorage in TBs can be scaled down.

`ocpus_lowest_scaled_value`

(optional) The lowest value to which ocpus can be scaled down.

`max_acds_lowest_scaled_value`

(optional) The lowest value to which ACDs can be scaled down.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_T Type

Unallocated resource details of the Cloud Autonomous VM Cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Exadata infrastructure.

`un_allocated_adb_storage_in_t_bs`

(required) Total unallocated autonomous data storage in the Cloud Autonomous VM Cluster in TBs.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE_T Type

Cloud Autonomous VM Cluster usage details, including the Autonomous Container Databases usage.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Autonomous VM cluster.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size allocated for Autonomous Databases, in TBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created.

`available_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size available for Autonomous Databases, in TBs.

`used_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size used for Autonomous Databases, in TBs.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) to be enabled per each CPU core.

`exadata_storage_in_t_bs`

(optional) Total exadata storage allocated for the Autonomous VM Cluster. DATA + RECOVERY + SPARSE + any overhead in TBs.

`total_cpus`

(optional) The number of CPU cores enabled on the Cloud Autonomous VM cluster.

`used_cpus`

(optional) The number of CPU cores alloted to the Autonomous Container Databases in an Cloud Autonomous VM cluster.

`available_cpus`

(optional) The number of CPU cores available.

`reclaimable_cpus`

(optional) CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`provisionable_autonomous_container_databases`

(optional) The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`provisioned_autonomous_container_databases`

(optional) The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.

`non_provisionable_autonomous_container_databases`

(optional) The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`autonomous_vm_resource_usage`

(optional) List of Autonomous VM resource usages.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_SUMMARY_T Type

Details of the cloud Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Autonomous VM cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`description`

(optional) User defined description of the cloud Autonomous VM cluster.

`availability_domain`

(required) The name of the availability domain that the cloud Autonomous VM cluster is located in.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the cloud Autonomous VM Cluster is associated with. **Subnet Restrictions:** - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`last_update_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance update history. This value is updated when a maintenance update starts.

`lifecycle_state`

(required) The current state of the cloud Autonomous VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`display_name`

(required) The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the cloud Autonomous VM cluster was created.

`time_updated`

(optional) The last date and time that the cloud Autonomous VM cluster was updated.

`cluster_time_zone`

(optional) The time zone of the Cloud Autonomous VM Cluster.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`hostname`

(optional) The hostname for the cloud Autonomous VM cluster.

`domain`

(optional) The domain name for the cloud Autonomous VM cluster.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

`shape`

(optional) The model name of the Exadata hardware running the cloud Autonomous VM cluster.

`node_count`

(optional) The number of database servers in the cloud VM cluster.

`data_storage_size_in_t_bs`

(optional) The total data storage allocated, in terabytes (TB).

`data_storage_size_in_g_bs`

(optional) The total data storage allocated, in gigabytes (GB).

`cpu_core_count`

(optional) The number of CPU cores on the cloud Autonomous VM cluster.

`ocpu_count`

(optional) The number of CPU cores on the cloud Autonomous VM cluster. Only 1 decimal place is allowed for the fractional part.

`compute_model`

(optional) The compute model of the Cloud Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`is_mtls_enabled_vm_cluster`

(optional) Enable mutual TLS(mTLS) authentication for database at time of provisioning a VMCluster. This is applicable to database TLS Certificates only. Default is TLS

`cpu_core_count_per_node`

(optional) The number of CPU cores enabled per VM cluster node.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`maintenance_window`

(optional)

`scan_listener_port_tls`

(optional) The SCAN Listenenr TLS port. Default is 2484.

`scan_listener_port_non_tls`

(optional) The SCAN Listener Non TLS port. Default is 1521.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`time_database_ssl_certificate_expires`

(optional) The date and time of Database SSL certificate expiration.

`time_ords_certificate_expires`

(optional) The date and time of ORDS certificate expiration.

`available_cpus`

(optional) CPU cores available for allocation to Autonomous Databases.

`reclaimable_cpus`

(optional) For Autonomous Databases on Dedicated Exadata Infrastructure: - These are the CPUs that continue to be included in the count of CPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available CPUs at its parent Autonomous VM Cluster level by restarting the Autonomous Container Database. - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model.

`available_container_databases`

(optional) The number of Autonomous Container Databases that can be created with the currently available local storage.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created with the allocated local storage.

`available_autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size available for Autonomous Databases, in TBs.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size allocated for Autonomous Databases, in TBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) enabled per OCPU or ECPU.

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`cpu_percentage`

(optional) The percentage of total number of CPUs used in an Autonomous VM Cluster.

`autonomous_data_storage_percentage`

(optional) The percentage of the data storage used for the Autonomous Databases in an Autonomous VM Cluster.

`provisioned_cpus`

(optional) The number of CPUs provisioned in an Autonomous VM Cluster.

`total_cpus`

(optional) The total number of CPUs in an Autonomous VM Cluster.

`total_autonomous_data_storage_in_t_bs`

(optional) The total data disk group size for Autonomous Databases, in TBs.

`reserved_cpus`

(optional) The number of CPUs reserved in an Autonomous VM Cluster.

`provisionable_autonomous_container_databases`

(optional) The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`provisioned_autonomous_container_databases`

(optional) The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.

`non_provisionable_autonomous_container_databases`

(optional) The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.

`exadata_storage_in_t_bs_lowest_scaled_value`

(optional) The lowest value to which exadataStorage in TBs can be scaled down.

`ocpus_lowest_scaled_value`

(optional) The lowest value to which ocpus can be scaled down.

`max_acds_lowest_scaled_value`

(optional) The lowest value to which ACDs can be scaled down.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_DATABASE_MANAGEMENT_CONFIG_T Type

The configuration of the Database Management service.

Syntax
```

```

Fields

Field Description

`management_status`

(required) The status of the Database Management service.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'UPDATING', 'FAILED_ENABLING', 'FAILED_DISABLING', 'FAILED_UPDATING'

`management_type`

(required) The Database Management type.

Allowed values are: 'BASIC', 'ADVANCED'

### DBMS_CLOUD_OCI_DATABASE_CLOUD_EXADATA_INFRASTRUCTURE_T Type

Details of the cloud Exadata infrastructure resource. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current lifecycle state of the cloud Exadata infrastructure resource.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`display_name`

(required) The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.

`shape`

(required) The model name of the cloud Exadata infrastructure resource.

`availability_domain`

(required) The name of the availability domain that the cloud Exadata infrastructure resource is located in.

`compute_count`

(optional) The number of compute servers for the cloud Exadata infrastructure.

`storage_count`

(optional) The number of storage servers for the cloud Exadata infrastructure.

`total_storage_size_in_g_bs`

(optional) The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).

`available_storage_size_in_g_bs`

(optional) The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).

`cpu_count`

(optional) The total number of CPU cores allocated.

`max_cpu_count`

(optional) The total number of CPU cores available.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`max_memory_in_g_bs`

(optional) The total memory available in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`max_db_node_storage_in_g_bs`

(optional) The total local node storage available in GBs.

`data_storage_size_in_t_bs`

(optional) Size, in terabytes, of the DATA disk group.

`max_data_storage_in_t_bs`

(optional) The total available DATA disk group size.

`additional_storage_count`

(optional) The requested number of additional storage servers for the Exadata infrastructure.

`activated_storage_count`

(optional) The requested number of additional storage servers activated for the Exadata infrastructure.

`time_created`

(optional) The date and time the cloud Exadata infrastructure resource was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`maintenance_window`

(optional)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`customer_contacts`

(optional) The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource. Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators. Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.

`storage_server_version`

(optional) The software version of the storage servers (cells) in the cloud Exadata infrastructure. Example: 20.1.15

`db_server_version`

(optional) The software version of the database servers (dom0) in the cloud Exadata infrastructure. Example: 20.1.15

`monthly_storage_server_version`

(optional) The monthly software version of the storage servers (cells) in the cloud Exadata infrastructure. Example: 20.1.15

`monthly_db_server_version`

(optional) The monthly software version of the database servers (dom0) in the cloud Exadata infrastructure. Example: 20.1.15

### DBMS_CLOUD_OCI_DATABASE_CLOUD_EXADATA_INFRASTRUCTURE_SUMMARY_T Type

Details of the cloud Exadata infrastructure resource. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current lifecycle state of the cloud Exadata infrastructure resource.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`display_name`

(required) The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.

`shape`

(required) The model name of the cloud Exadata infrastructure resource.

`availability_domain`

(required) The name of the availability domain that the cloud Exadata infrastructure resource is located in.

`compute_count`

(optional) The number of compute servers for the cloud Exadata infrastructure.

`storage_count`

(optional) The number of storage servers for the cloud Exadata infrastructure.

`total_storage_size_in_g_bs`

(optional) The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).

`available_storage_size_in_g_bs`

(optional) The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).

`cpu_count`

(optional) The total number of CPU cores allocated.

`max_cpu_count`

(optional) The total number of CPU cores available.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`max_memory_in_g_bs`

(optional) The total memory available in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`max_db_node_storage_in_g_bs`

(optional) The total local node storage available in GBs.

`data_storage_size_in_t_bs`

(optional) Size, in terabytes, of the DATA disk group.

`max_data_storage_in_t_bs`

(optional) The total available DATA disk group size.

`additional_storage_count`

(optional) The requested number of additional storage servers for the Exadata infrastructure.

`activated_storage_count`

(optional) The requested number of additional storage servers activated for the Exadata infrastructure.

`time_created`

(optional) The date and time the cloud Exadata infrastructure resource was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`maintenance_window`

(optional)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`customer_contacts`

(optional) The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource. Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators. Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.

`storage_server_version`

(optional) The software version of the storage servers (cells) in the cloud Exadata infrastructure. Example: 20.1.15

`db_server_version`

(optional) The software version of the database servers (dom0) in the cloud Exadata infrastructure. Example: 20.1.15

`monthly_storage_server_version`

(optional) The monthly software version of the storage servers (cells) in the cloud Exadata infrastructure. Example: 20.1.15

`monthly_db_server_version`

(optional) The monthly software version of the database servers (dom0) in the cloud Exadata infrastructure. Example: 20.1.15

### DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_cloud_autonomous_vm_cluster_resource_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_CLOUD_EXADATA_INFRASTRUCTURE_UNALLOCATED_RESOURCES_T Type

Details of unallocated resources of the Cloud Exadata infrastructure. Applies to Cloud Exadata infrastructure instances only.

Syntax
```

```

Fields

Field Description

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cloud Exadata infrastructure.

`cloud_exadata_infrastructure_display_name`

(required) The user-friendly name for the Cloud Exadata infrastructure. The name does not need to be unique.

`local_storage_in_gbs`

(optional) The minimum amount of unallocated storage available across all nodes in the infrastructure.

`ocpus`

(optional) The minimum amount of unallocated ocpus available across all nodes in the infrastructure.

`memory_in_g_bs`

(optional) The minimum amount of unallocated memory available across all nodes in the infrastructure.

`exadata_storage_in_t_bs`

(optional) Total unallocated exadata storage in the infrastructure in TBs.

`cloud_autonomous_vm_clusters`

(optional) The list of Cloud Autonomous VM Clusters on the Infrastructure and their associated unallocated resources details.

### DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_T Type

The IORM configuration settings for the database.

Syntax
```

```

Fields

Field Description

`db_name`

(optional) The database name. For the default `DbPlan`, the `dbName` is `default`.

`l_share`

(optional) The relative priority of this database.

`flash_cache_limit`

(optional) The flash cache limit for this database. This value is internally configured based on the share value assigned to the database.

### DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_database_db_iorm_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_EXADATA_IORM_CONFIG_T Type

The IORM settings of the Exadata DB system.

Syntax
```

```

Fields

Field Description

`lifecycle_state`

(optional) The current state of IORM configuration for the Exadata DB system.

Allowed values are: 'BOOTSTRAPPING', 'ENABLED', 'DISABLED', 'UPDATING', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current `lifecycleState`.

`objective`

(optional) The current value for the IORM objective. The default is `AUTO`.

Allowed values are: 'LOW_LATENCY', 'HIGH_THROUGHPUT', 'BALANCED', 'AUTO', 'BASIC'

`db_plans`

(optional) An array of IORM settings for all the database in the Exadata DB system.

### DBMS_CLOUD_OCI_DATABASE_DATA_COLLECTION_OPTIONS_T Type

Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.

Syntax
```

```

Fields

Field Description

`is_diagnostics_events_enabled`

(optional) Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection allows you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced service and proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster provisioning. You can also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.

`is_health_monitoring_enabled`

(optional) Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling health monitoring allows Oracle to collect diagnostic data and share it with its operations and support personnel. You may also receive notifications for some events. Collecting health diagnostics enables Oracle to provide proactive support and enhanced service for your system. Optionally enable health monitoring while provisioning a system. You can also disable or enable health monitoring anytime using the `UpdateVmCluster`, `UpdateCloudVmCluster` or `updateDbsystem` API.

`is_incident_logs_enabled`

(optional) Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling incident logs collection allows Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces, and use them to diagnose issues and resolve them. Optionally enable incident logs collection while provisioning a system. You can also disable or enable incident logs collection anytime using the `UpdateVmCluster`, `updateCloudVmCluster` or `updateDbsystem` API.

### DBMS_CLOUD_OCI_DATABASE_CLOUD_VM_CLUSTER_T Type

Details of the cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`iorm_config_cache`

(optional)

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain that the cloud Exadata infrastructure resource is located in.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the cloud VM cluster. **Subnet Restrictions:** - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`backup_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup network subnet associated with the cloud VM cluster. **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`last_update_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance update history entry. This value is updated when a maintenance update starts.

`shape`

(required) The model name of the Exadata hardware running the cloud VM cluster.

`listener_port`

(optional) The port number configured for the listener on the cloud VM cluster.

`lifecycle_state`

(required) The current state of the cloud VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`node_count`

(optional) The number of nodes in the cloud VM cluster.

`storage_size_in_g_bs`

(optional) The storage allocation for the disk group, in gigabytes (GB).

`display_name`

(required) The user-friendly name for the cloud VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the cloud VM cluster was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_zone`

(optional) The time zone of the cloud VM cluster. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`hostname`

(required) The hostname for the cloud VM cluster.

`domain`

(required) The domain name for the cloud VM cluster.

`cpu_core_count`

(required) The number of CPU cores enabled on the cloud VM cluster.

`ocpu_count`

(optional) The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.

`memory_size_in_g_bs`

(optional) The memory to be allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage to be allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated in TBs.

`db_servers`

(optional) The list of DB servers.

`cluster_name`

(optional) The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`data_storage_percentage`

(optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See[Storage Configuration](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm#Exadata)in the Exadata documentation for details on the impact of the configuration settings on storage.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

`is_sparse_diskgroup_enabled`

(optional) If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.

`gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`system_version`

(optional) Operating system version of the image.

`ssh_public_keys`

(required) The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.

`license_model`

(optional) The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`disk_redundancy`

(optional) The type of redundancy configured for the cloud Vm cluster. NORMAL is 2-way redundancy. HIGH is 3-way redundancy.

Allowed values are: 'HIGH', 'NORMAL'

`scan_ip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.

`vip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual IP (VIP) addresses associated with the cloud VM cluster. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.

`scan_dns_record_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`scan_dns_name`

(optional) The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.

`zone_id`

(optional) The OCID of the zone the cloud VM cluster is associated with.

`scan_listener_port_tcp`

(optional) The TCP Single Client Access Name (SCAN) port. The default port is 1521.

`scan_listener_port_tcp_ssl`

(optional) The TCPS Single Client Access Name (SCAN) port. The default port is 2484.

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CLOUD_VM_CLUSTER_SUMMARY_T Type

Details of the cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(required) The name of the availability domain that the cloud Exadata infrastructure resource is located in.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the cloud VM cluster. **Subnet Restrictions:** - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`backup_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup network subnet associated with the cloud VM cluster. **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`last_update_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance update history entry. This value is updated when a maintenance update starts.

`shape`

(required) The model name of the Exadata hardware running the cloud VM cluster.

`listener_port`

(optional) The port number configured for the listener on the cloud VM cluster.

`lifecycle_state`

(required) The current state of the cloud VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`node_count`

(optional) The number of nodes in the cloud VM cluster.

`storage_size_in_g_bs`

(optional) The storage allocation for the disk group, in gigabytes (GB).

`display_name`

(required) The user-friendly name for the cloud VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the cloud VM cluster was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_zone`

(optional) The time zone of the cloud VM cluster. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`hostname`

(required) The hostname for the cloud VM cluster.

`domain`

(required) The domain name for the cloud VM cluster.

`cpu_core_count`

(required) The number of CPU cores enabled on the cloud VM cluster.

`ocpu_count`

(optional) The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.

`memory_size_in_g_bs`

(optional) The memory to be allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage to be allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated in TBs.

`db_servers`

(optional) The list of DB servers.

`cluster_name`

(optional) The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`data_storage_percentage`

(optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See[Storage Configuration](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm#Exadata)in the Exadata documentation for details on the impact of the configuration settings on storage.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

`is_sparse_diskgroup_enabled`

(optional) If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.

`gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`system_version`

(optional) Operating system version of the image.

`ssh_public_keys`

(required) The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.

`license_model`

(optional) The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`disk_redundancy`

(optional) The type of redundancy configured for the cloud Vm cluster. NORMAL is 2-way redundancy. HIGH is 3-way redundancy.

Allowed values are: 'HIGH', 'NORMAL'

`scan_ip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.

`vip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual IP (VIP) addresses associated with the cloud VM cluster. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.

`scan_dns_record_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`scan_dns_name`

(optional) The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.

`zone_id`

(optional) The OCID of the zone the cloud VM cluster is associated with.

`scan_listener_port_tcp`

(optional) The TCP Single Client Access Name (SCAN) port. The default port is 1521.

`scan_listener_port_tcp_ssl`

(optional) The TCPS Single Client Access Name (SCAN) port. The default port is 2484.

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_COMPLETE_EXTERNAL_BACKUP_JOB_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`tde_wallet_path`

(optional) If the database being backed up is TDE enabled, this will be the path to the associated TDE wallet in Object Storage.

`cf_backup_handle`

(optional) The handle of the control file backup.

`spf_backup_handle`

(optional) The handle of the spfile backup.

`sql_patches`

(optional) The list of SQL patches that need to be applied to the backup during the restore.

`data_size`

(optional) The size of the data in the database, in megabytes.

`redo_size`

(optional) The size of the redo in the database, in megabytes.

### DBMS_CLOUD_OCI_DATABASE_COMPUTE_PERFORMANCE_SUMMARY_T Type

Parameters detailing the compute performance for a specified DB system shape.

Syntax
```

```

Fields

Field Description

`cpu_core_count`

(required) The number of OCPU cores available.

`memory_in_g_bs`

(required) The amount of memory allocated for the VMDB System.

`network_bandwidth_in_gbps`

(required) The network bandwidth of the VMDB system in gbps.

`network_iops`

(required) IOPS for the VMDB System.

`network_throughput_in_mbps`

(required) Network throughput for the VMDB System.

### DBMS_CLOUD_OCI_DATABASE_CONFIGURE_AUTONOMOUS_DATABASE_VAULT_KEY_DETAILS_T Type

Configuration details for the Autonomous Database[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts)key.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`is_using_oracle_managed_keys`

(optional) True if disable Customer Managed Keys and use Oracle Managed Keys.

### DBMS_CLOUD_OCI_DATABASE_CONFIGURE_SAAS_ADMIN_USER_DETAILS_T Type

Details to update SaaS administrative user configuration.

Syntax
```

```

Fields

Field Description

`password`

(optional) A strong password for SaaS administrative user. The password must be a minimum of nine (9) characters and contain a minimum of two (2) uppercase, two (2) lowercase, two (2) numbers, and two (2) special characters from _ (underscore), \\# (hashtag), or - (dash).

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`secret_version_number`

(optional) The version of the vault secret. If no version is specified, the latest version will be used.

`duration`

(optional) How long, in hours, the SaaS administrative user will stay enabled. If no duration is specified, the default value 1 will be used.

`is_enabled`

(optional) Indicates if the SaaS administrative user is enabled for the Autonomous Database.

`access_type`

(optional) The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.

Allowed values are: 'READ_ONLY', 'READ_WRITE', 'ADMIN'

`time_saas_admin_user_enabled`

(optional) The date and time the SaaS administrative user was enabled at, for the Autonomous Database.

### DBMS_CLOUD_OCI_DATABASE_CONSOLE_CONNECTION_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the console connection.

`compartment_id`

(required) The OCID of the compartment to contain the console connection.

`db_node_id`

(required) The OCID of the database node.

`connection_string`

(required) The SSH connection string for the console connection.

`fingerprint`

(required) The SSH public key fingerprint for the console connection.

`service_host_key_fingerprint`

(optional) The SSH public key's fingerprint for the console connection service host.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`lifecycle_details`

(optional) Information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the console connection.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED'

### DBMS_CLOUD_OCI_DATABASE_CONSOLE_CONNECTION_SUMMARY_T Type

The `InstanceConsoleConnection` API provides you with console access to dbnode enabling you to troubleshoot malfunctioning dbnode.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the console connection.

`compartment_id`

(required) The OCID of the compartment to contain the console connection.

`db_node_id`

(required) The OCID of the database node.

`connection_string`

(required) The SSH connection string for the console connection.

`fingerprint`

(required) The SSH public key fingerprint for the console connection.

`service_host_key_fingerprint`

(optional) The SSH public key's fingerprint for the console connection service host.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`lifecycle_details`

(optional) Information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the console connection.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED'

### DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_T Type

The details of the Db Node console history.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the console history.

`compartment_id`

(required) The OCID of the compartment containing the console history.

`db_node_id`

(required) The OCID of the database node.

`display_name`

(optional) The user-friendly name for the console history. The name does not need to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`lifecycle_state`

(required) The current state of the console history.

Allowed values are: 'REQUESTED', 'GETTING_HISTORY', 'SUCCEEDED', 'FAILED', 'DELETED', 'DELETING'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the console history was created.

### DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_SUMMARY_T Type

The details of the Db Node console history.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the console history.

`compartment_id`

(required) The OCID of the compartment containing the console history.

`db_node_id`

(required) The OCID of the database node.

`display_name`

(optional) The user-friendly name for the console history. The name does not need to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`lifecycle_state`

(required) The current state of the console history.

Allowed values are: 'REQUESTED', 'GETTING_HISTORY', 'SUCCEEDED', 'FAILED', 'DELETED', 'DELETING'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the console history was created.

### DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_console_history_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_COLLECTION_T Type

Results of the Db Node console history lists. Contains ConsoleHistorySummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Db Node console histories.

### DBMS_CLOUD_OCI_DATABASE_CONVERT_TO_PDB_TARGET_BASE_T Type

Details of the container database in which the converted pluggable database will be located.

Syntax
```

```

Fields

Field Description

`target`

(optional) The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database. - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.

Allowed values are: 'NEW_DATABASE'

### DBMS_CLOUD_OCI_DATABASE_CONVERT_TO_PDB_DETAILS_T Type

Details for converting a non-container database to pluggable database.

Syntax
```

```

Fields

Field Description

`action`

(required) The operations used to convert a non-container database to a pluggable database. - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database. - Use `CONVERT` to convert a non-container database into a pluggable database. - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API. - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.

Allowed values are: 'PRECHECK', 'CONVERT', 'SYNC', 'SYNC_ROLLBACK'

`convert_to_pdb_target_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CONVERT_TO_REGULAR_PLUGGABLE_DATABASE_DETAILS_T Type

Parameters for converting Refreshable Clone Pluggable Database into Regular Pluggable Database.

Syntax
```

```

Fields

Field Description

`should_create_pdb_backup`

(optional) Indicates whether to take Pluggable Database Backup after the operation.

`container_database_admin_password`

(optional) The DB system administrator password of the Container Database.

`tde_wallet_password`

(optional) The existing TDE wallet password of the Container Database.

### DBMS_CLOUD_OCI_DATABASE_CREATE_APPLICATION_VIP_DETAILS_T Type

Details to create an application virtual IP (VIP) address on a cloud VM cluster.

Syntax
```

```

Fields

Field Description

`hostname_label`

(required) The hostname of the application virtual IP (VIP) address.

`db_node_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB node associated with the application virtual IP (VIP) address.

`cloud_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster associated with the application virtual IP (VIP) address.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the application virtual IP (VIP) address.

`ip_address`

(optional) The application virtual IP (VIP) address.

### DBMS_CLOUD_OCI_DATABASE_PEER_AUTONOMOUS_CONTAINER_DATABASE_BACKUP_CONFIG_T Type

Backup options for the standby Autonomous Container Database.

Syntax
```

```

Fields

Field Description

`backup_destination_details`

(optional) Backup destination details.

`recovery_window_in_days`

(optional) Number of days between the current and the earliest point of recoverability covered by automatic backups. This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window. When the value is updated, it is applied to all existing automatic backups. If the number of specified days is 0 then there will be no backups.

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION_DETAILS_T Type

Create Autonomous Dataguard Association to an existing Autonomous Container Database

Syntax
```

```

Fields

Field Description

`peer_autonomous_container_database_display_name`

(required) The display name for the peer Autonomous Container Database.

`peer_autonomous_container_database_compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the standby Autonomous Container Database will be created.

`peer_cloud_autonomous_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer cloud Autonomous Exadata VM Cluster.

`peer_autonomous_container_database_backup_config`

(optional)

`is_automatic_failover_enabled`

(optional) Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association

`protection_mode`

(required) The protection mode of this Autonomous Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE'

`fast_start_fail_over_lag_limit_in_seconds`

(optional) The lag time for my preference based on data loss tolerance in seconds.

`standby_maintenance_buffer_in_days`

(optional) The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database. This value represents the number of days before scheduled maintenance of the primary database.

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_CONTAINER_DATABASE_DETAILS_T Type

Describes the required parameters for the creation of an Autonomous Container Database.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The display name for the Autonomous Container Database.

`db_unique_name`

(optional) **Deprecated.** The `DB_UNIQUE_NAME` value is set by Oracle Cloud Infrastructure. Do not specify a value for this parameter. Specifying a value for this field will cause Terraform operations to fail.

`db_name`

(optional) The Database name for the Autonomous Container Database. The name must be unique within the Cloud Autonomous VM Cluster, starting with an alphabetic character, followed by 1 to 7 alphanumeric characters.

`service_level_agreement_type`

(optional) The service level agreement type of the Autonomous Container Database. The default is STANDARD. For an autonomous dataguard Autonomous Container Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.

Allowed values are: 'STANDARD', 'AUTONOMOUS_DATAGUARD'

`autonomous_exadata_infrastructure_id`

(optional) **No longer used.** This parameter is no longer used for Autonomous Database on dedicated Exadata infrasture. Specify a `cloudAutonomousVmClusterId` instead. Using this parameter will cause the operation to fail.

`db_version`

(optional) The base version for the Autonomous Container Database.

`peer_autonomous_exadata_infrastructure_id`

(optional) *No longer used.* This parameter is no longer used for Autonomous Database on dedicated Exadata infrasture. Specify a `peerCloudAutonomousVmClusterId` instead. Using this parameter will cause the operation to fail.

`peer_autonomous_container_database_display_name`

(optional) The display name for the peer Autonomous Container Database.

`protection_mode`

(optional) The protection mode of this Autonomous Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE'

`fast_start_fail_over_lag_limit_in_seconds`

(optional) The lag time for my preference based on data loss tolerance in seconds.

`is_automatic_failover_enabled`

(optional) Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association

`peer_cloud_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer cloud Autonomous Exadata VM Cluster.

`peer_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer Autonomous VM cluster for Autonomous Data Guard. Required to enable Data Guard.

`peer_autonomous_container_database_compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the standby Autonomous Container Database will be created.

`peer_autonomous_container_database_backup_config`

(optional)

`peer_db_unique_name`

(optional) **Deprecated.** The `DB_UNIQUE_NAME` of the peer Autonomous Container Database in a Data Guard association is set by Oracle Cloud Infrastructure. Do not specify a value for this parameter. Specifying a value for this field will cause Terraform operations to fail.

`autonomous_vm_cluster_id`

(optional) The OCID of the Autonomous VM Cluster.

`cloud_autonomous_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Autonomous Exadata VM Cluster.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Autonomous Container Database.

`patch_model`

(required) Database Patch model preference.

Allowed values are: 'RELEASE_UPDATES', 'RELEASE_UPDATE_REVISIONS'

`maintenance_window_details`

(optional)

`standby_maintenance_buffer_in_days`

(optional) The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database. This value represents the number of days before scheduled maintenance of the primary database.

`version_preference`

(optional) The next maintenance version preference.

Allowed values are: 'NEXT_RELEASE_UPDATE', 'LATEST_RELEASE_UPDATE'

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`backup_config`

(optional)

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_BACKUP_DETAILS_T Type

Details to create an Oracle Autonomous Database backup. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the backup. The name does not have to be unique.

`autonomous_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database backup.

`retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`is_long_term_backup`

(optional) Indicates whether the backup is long-term

`backup_destination_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_BASE_T Type

Details to create an Oracle Autonomous Database. **Notes:** - To specify OCPU core count, you must use either `ocpuCount` or `cpuCoreCount`. You cannot use both parameters at the same time. - To specify a storage allocation, you must use either `dataStorageSizeInGBs` or `dataStorageSizeInTBs`. - See the individual parameter discriptions for more information on the OCPU and storage value parameters. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment of the Autonomous Database.

`character_set`

(optional) The character set for the autonomous database. The default is AL32UTF8. Allowed values for an Autonomous Database Serverless instance as as returned by[List Autonomous Database Character Sets](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/autonomous-character-set-selection.html)For an Autonomous Database on dedicated infrastructure, the allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS

`ncharacter_set`

(optional) The character set for the Autonomous Database. The default is AL32UTF8. Use[List Autonomous Database Character Sets](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/autonomous-character-set-selection.html)to list the allowed values for an Autonomous Database Serverless instance. For an Autonomous Database on dedicated Exadata infrastructure, the allowed values are: AL16UTF16 or UTF8.

`db_name`

(optional) The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy. It is required in all cases except when creating a cross-region Autonomous Data Guard standby instance or a cross-region disaster recovery standby instance.

`cpu_core_count`

(optional) The number of OCPU cores to be made available to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. **Note:** This parameter cannot be used with the `ocpuCount` parameter.

`backup_retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`compute_model`

(optional) The compute model of the Autonomous Database. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value.

Allowed values are: 'ECPU', 'OCPU'

`compute_count`

(optional) The compute amount available to the database. Minimum and maximum values depend on the compute model and whether the database is an Autonomous Database Serverless instance or an Autonomous Database on Dedicated Exadata Infrastructure, the 'ECPU' compute model requires values in multiples of two. Required when using the `computeModel` parameter. When using `cpuCoreCount` parameter, it is an error to specify computeCount to a non-null value.

`ocpu_count`

(optional) The number of OCPU cores to be made available to the database. The following points apply: - For Autonomous Databases on Dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Database Serverless instances.) - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to an Autonomous Database Serverless instance or an Autonomous Database on Dedicated Exadata Infrastructure. For Autonomous Databases on Dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

`db_workload`

(optional) The Autonomous Database workload type. The following values are valid: - OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`data_storage_size_in_t_bs`

(optional) The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. For Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. A full Exadata service is allocated when the Autonomous Database size is set to the upper limit (384 TB). **Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter.

`data_storage_size_in_g_bs`

(optional) The size, in gigabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. The maximum storage value is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. **Notes** - This parameter is only supported for dedicated Exadata infrastructure. - This parameter cannot be used with the `dataStorageSizeInTBs` parameter.

`is_free_tier`

(optional) Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isLocalDataGuardEnabled

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`admin_password`

(optional) **Important** The `adminPassword` or `secretId` must be specified for all Autonomous Databases except for refreshable clones. The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. This cannot be used in conjunction with with OCI vault secrets (secretId).

`display_name`

(optional) The user-friendly name for the Autonomous Database. The name does not have to be unique.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`is_preview_version_with_service_terms_accepted`

(optional) If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for Autonomous Database Serverless instances.

`is_auto_scaling_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`.

`is_dedicated`

(optional) True if the database is on[dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).

`autonomous_container_database_id`

(optional) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`in_memory_percentage`

(optional) The percentage of the System Global Area(SGA) assigned to In-Memory tables in Autonomous Database.

`is_access_control_enabled`

(optional) Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional, if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone. This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.

`whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`are_primary_whitelisted_ips_used`

(optional) This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled. It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby. It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.

`standby_whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`is_data_guard_enabled`

(optional) **Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`is_local_data_guard_enabled`

(optional) Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the resource is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. - For Autonomous Database, setting this will disable public secure access to the database. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`private_endpoint_label`

(optional) The resource's private endpoint label. Setting this to an empty string, after the creation of the private endpoint database, changes the private endpoint database to a public endpoint database. This setting cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`private_endpoint_ip`

(optional) The private endpoint Ip address for the resource.

`db_version`

(optional) A valid Oracle Database version for Autonomous Database.

`source`

(optional) The source of the database: Use `NONE` for creating a new Autonomous Database. Use `DATABASE` for creating a new Autonomous Database by cloning an existing Autonomous Database. Use `CROSS_REGION_DATAGUARD` to create a standby Data Guard database in another region. For[Autonomous Database Serverless instances](https://docs.oracle.com/en/cloud/paas/autonomous-database/shared/index.html), the following cloning options are available: Use `BACKUP_FROM_ID` for creating a new Autonomous Database from a specified backup. Use `BACKUP_FROM_TIMESTAMP` for creating a point-in-time Autonomous Database clone using backups. For more information, see[Cloning and Moving an Autonomous Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/clone-autonomous-database.html#GUID-D771796F-5081-4CFB-A7FF-0F893EABD7BC).

Allowed values are: 'NONE', 'DATABASE', 'BACKUP_FROM_ID', 'BACKUP_FROM_TIMESTAMP', 'CLONE_TO_REFRESHABLE', 'CROSS_REGION_DATAGUARD', 'CROSS_REGION_DISASTER_RECOVERY'

`customer_contacts`

(optional) Customer Contacts.

`is_mtls_connection_required`

(optional) Specifies if the Autonomous Database requires mTLS connections. This may not be updated in parallel with any of the following: licenseModel, databaseEdition, cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, whitelistedIps, openMode, permissionLevel, db-workload, privateEndpointLabel, nsgIds, customerContacts, dbVersion, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier. Service Change: The default value of the isMTLSConnectionRequired attribute will change from true to false on July 1, 2023 in the following APIs: - CreateAutonomousDatabase - GetAutonomousDatabase - UpdateAutonomousDatabase Details: Prior to the July 1, 2023 change, the isMTLSConnectionRequired attribute default value was true. This applies to Autonomous Database Serverless. Does this impact me? If you use or maintain custom scripts or Terraform scripts referencing the CreateAutonomousDatabase, GetAutonomousDatabase, or UpdateAutonomousDatabase APIs, you want to check, and possibly modify, the scripts for the changed default value of the attribute. Should you choose not to leave your scripts unchanged, the API calls containing this attribute will continue to work, but the default value will switch from true to false. How do I make this change? Using either OCI SDKs or command line tools, update your custom scripts to explicitly set the isMTLSConnectionRequired attribute to true.

`resource_pool_leader_id`

(optional) The unique identifier for leader autonomous database OCID[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_pool_summary`

(optional)

`autonomous_maintenance_schedule_type`

(optional) The maintenance schedule type of the Autonomous Database Serverless. An EARLY maintenance schedule follows a schedule applying patches prior to the REGULAR schedule. A REGULAR maintenance schedule follows the normal cycle

Allowed values are: 'EARLY', 'REGULAR'

`scheduled_operations`

(optional) The list of scheduled operations. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`is_auto_scaling_for_storage_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.

`max_cpu_core_count`

(optional) The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.

`database_edition`

(optional) The Oracle Database Edition that applies to the Autonomous databases.

`db_tools_details`

(optional) The list of database tools details. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, isLocalDataGuardEnabled, or isFreeTier.

`secret_id`

(optional) The OCI vault secret [/Content/General/Concepts/identifiers.htm]OCID. This cannot be used in conjunction with adminPassword.

`secret_version_number`

(optional) The version of the vault secret. If no version is specified, the latest version will be used.

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_CLONE_DETAILS_T Type

Details to create an Oracle Autonomous Database by cloning an existing Autonomous Database.

Syntax
```

```

`dbms_cloud_oci_database_create_autonomous_database_clone_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

Fields

Field Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that you will clone to create a new Autonomous Database.

`clone_type`

(required) The Autonomous Database clone type.

Allowed values are: 'FULL', 'METADATA'

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_DETAILS_T Type

Details to create an Oracle Autonomous Database.

Syntax
```

```

`dbms_cloud_oci_database_create_autonomous_database_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_FROM_BACKUP_DETAILS_T Type

Details to create an Oracle Autonomous Database by cloning from a backup of an existing Autonomous Database.

Syntax
```

```

`dbms_cloud_oci_database_create_autonomous_database_from_backup_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

Fields

Field Description

`autonomous_database_backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database Backup that you will clone to create a new Autonomous Database.

`clone_type`

(required) The Autonomous Database clone type.

Allowed values are: 'FULL', 'METADATA'

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_FROM_BACKUP_TIMESTAMP_DETAILS_T Type

Details to create a point-in-time clone of an Oracle Autonomous Database by specifying a timestamp. Point-in-time clones use backups as the source of the data for the clone.

Syntax
```

```

`dbms_cloud_oci_database_create_autonomous_database_from_backup_timestamp_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

Fields

Field Description

`autonomous_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that you will clone to create a new Autonomous Database.

`l_timestamp`

(optional) The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.

`clone_type`

(required) The Autonomous Database clone type.

Allowed values are: 'FULL', 'METADATA'

`use_latest_available_backup_time_stamp`

(optional) Clone from latest available backup timestamp.

### DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type

Details for the create Autonomous VM cluster operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.

`exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`vm_cluster_network_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`time_zone`

(optional) The time zone to use for the Autonomous VM cluster. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the Autonomous VM cluster. If false, database backup on local Exadata storage is not available in the Autonomous VM cluster.

`license_model`

(optional) The Oracle license model that applies to the Autonomous VM cluster. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created.

`cpu_core_count_per_node`

(optional) The number of CPU cores to enable per VM cluster node.

`compute_model`

(optional) The compute model of the Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) to be enabled per OCPU or ECPU.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated for Autonomous Databases, in TBs.

`maintenance_window_details`

(optional)

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`scan_listener_port_tls`

(optional) The SCAN Listener TLS port number. Default value is 2484.

`scan_listener_port_non_tls`

(optional) The SCAN Listener Non TLS port number. Default value is 1521.

`is_mtls_enabled`

(optional) Enable mutual TLS(mTLS) authentication for database while provisioning a VMCluster. Default is TLS.

### DBMS_CLOUD_OCI_DATABASE_CREATE_BACKUP_DESTINATION_DETAILS_T Type

Details for creating a backup destination.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-provided name of the backup destination.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`l_type`

(required) Type of the backup destination.

Allowed values are: 'NFS', 'RECOVERY_APPLIANCE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_BACKUP_DETAILS_T Type

Details for creating a database backup. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`display_name`

(required) The user-friendly name for the backup. The name does not have to be unique.

### DBMS_CLOUD_OCI_DATABASE_CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type

Details for the create cloud Autonomous VM cluster operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`description`

(optional) User defined description of the cloud Autonomous VM cluster.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the cloud Autonomous VM Cluster is associated with.

`display_name`

(required) The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

`total_container_databases`

(optional) The total number of Autonomous Container Databases that can be created.

`cpu_core_count_per_node`

(optional) The number of CPU cores to be enabled per VM cluster node.

`memory_per_oracle_compute_unit_in_g_bs`

(optional) The amount of memory (in GBs) to be enabled per OCPU or ECPU.

`autonomous_data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated for Autonomous Databases, in TBs.

`cluster_time_zone`

(optional) The time zone to use for the Cloud Autonomous VM cluster. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`compute_model`

(optional) The compute model of the Cloud Autonomous VM Cluster.

Allowed values are: 'ECPU', 'OCPU'

`is_mtls_enabled_vm_cluster`

(optional) Enable mutual TLS(mTLS) authentication for database at time of provisioning a VMCluster. This is applicable to database TLS Certificates only. Default is TLS

`db_servers`

(optional) The list of database servers.

`maintenance_window_details`

(optional)

`scan_listener_port_tls`

(optional) The SCAN Listener TLS port. Default is 2484.

`scan_listener_port_non_tls`

(optional) The SCAN Listener Non TLS port. Default is 1521.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_CLOUD_EXADATA_INFRASTRUCTURE_DETAILS_T Type

Request to create cloud Exadata infrastructure. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain where the cloud Exadata infrastructure is located.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.

`shape`

(required) The shape of the cloud Exadata infrastructure resource.

`compute_count`

(optional) The number of compute servers for the cloud Exadata infrastructure.

`storage_count`

(optional) The number of storage servers for the cloud Exadata infrastructure.

`maintenance_window`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`customer_contacts`

(optional) Customer contacts.

### DBMS_CLOUD_OCI_DATABASE_CREATE_CLOUD_VM_CLUSTER_DETAILS_T Type

Details for the create cloud VM cluster operation. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet associated with the cloud VM cluster.

`backup_subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup network subnet associated with the cloud VM cluster.

`cpu_core_count`

(required) The number of CPU cores to enable for a cloud VM cluster. Valid values depend on the specified shape: - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

`ocpu_count`

(optional) The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.

`memory_size_in_g_bs`

(optional) The memory to be allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage to be allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated in TBs.

`db_servers`

(optional) The list of DB servers.

`cluster_name`

(optional) The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`data_storage_percentage`

(optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See[Storage Configuration](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm#Exadata)in the Exadata documentation for details on the impact of the configuration settings on storage.

`display_name`

(required) The user-friendly name for the cloud VM cluster. The name does not need to be unique.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure resource.

`hostname`

(required) The hostname for the cloud VM cluster. The hostname must begin with an alphabetic character, and can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata systems. The maximum length of the combined hostname and domain is 63 characters. **Note:** The hostname must be unique within the subnet. If it is not unique, the cloud VM Cluster will fail to provision.

`domain`

(optional) A domain name used for the cloud VM cluster. If the Oracle-provided internet and VCN resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted. Applies to Exadata Cloud Service instances only.

`ssh_public_keys`

(required) The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.

`license_model`

(optional) The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`is_sparse_diskgroup_enabled`

(optional) If true, the sparse disk group is configured for the cloud VM cluster. If false, the sparse disk group is not created.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.

`time_zone`

(optional) The time zone to use for the cloud VM cluster. For details, see[Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`scan_listener_port_tcp`

(optional) The TCP Single Client Access Name (SCAN) port. The default port is 1521.

`scan_listener_port_tcp_ssl`

(optional) The TCPS Single Client Access Name (SCAN) port. The default port is 2484.

`private_zone_id`

(optional) The private zone id in which DNS records need to be created.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`gi_version`

(required) A valid Oracle Grid Infrastructure (GI) software version.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

`system_version`

(optional) Operating system version of the image.

### DBMS_CLOUD_OCI_DATABASE_CREATE_CONSOLE_CONNECTION_DETAILS_T Type

The details for creating a Db node console connection. The Db node console connection is created in the same compartment as the dbNode.

Syntax
```

```

Fields

Field Description

`public_key`

(required) The SSH public key used to authenticate the console connection.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_CONSOLE_HISTORY_DETAILS_T Type

The details for creating a Db node console history. The Db node console history is created in the same compartment as the dbNode.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the console history. The name does not need to be unique.

### DBMS_CLOUD_OCI_DATABASE_CREATE_CROSS_REGION_AUTONOMOUS_DATABASE_DATA_GUARD_DETAILS_T Type

Details to create an Autonomous Data Guard association for an existing Autonomous Database where the standby is in a different (remote) region from the source primary database. *IMPORTANT* Note the following for creating standby databases in cross-region Autonomous Data Guard associations: - To create your standby database in a region different from the region of the primary, use the API endpoint of the region in which the standby will be located. For example, if the primary database is in the IAD region, and you want to create the standby in the PHX region, make the API call using the PHX endpoint (https://database.us-phoenix-1.oraclecloud.com). See[API Endpoints](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs)for the list of Database Service API endpoints. - In the request to create the standby database, the `sourceId` value should be the OCID of the primary database. The following parameters are optional for the cross-region standby database. If included in the request, these parameters contain the same values as the source Autonomous Database: - customerContacts - scheduledOperations - isAutoScalingForStorageEnabled - definedTags - freeformTags - licenseModel - whitelistedIps - isMtlsConnectionRequired - dbName - adminPassword - cpuCoreCount - dataStorageSizeInTB - dbVersion Example I - Creating a cross-region standby with required parameters only, with OCPU: `{ \"compartmentId\": \"ocid.compartment.oc1..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"cpuCoreCount\": 1, \"dbName\": \"adatabasedb1\", \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"dataStorageSizeInTBs\": 1, \"source\": \"CROSS_REGION_DATAGUARD\", \"adminPassword\" : \"&lt;var&gt;&amp;lt;password&amp;gt;&lt;/var&gt;\", }` Example II - Creating a cross-region standby that specifies optional parameters in addition to the required parameters, with ECPU: `{ \"compartmentId\": \"ocid.compartment.oc1..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"computeModel\": \"ECPU\", \"computeCount\": 2, \"dbName\": \"adatabasedb1\", \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"dataStorageSizeInTBs\": 1, \"source\": \"CROSS_REGION_DATAGUARD\", \"adminPassword\" : \"&lt;var&gt;&amp;lt;password&amp;gt;&lt;/var&gt;\", \"dbVersion\": \"19c\", \"licenseModel\": \"LICENSE_INCLUDED\", \"isAutoScalingForStorageEnabled\": \"true\" }`

Syntax
```

```

`dbms_cloud_oci_database_create_cross_region_autonomous_database_data_guard_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

Fields

Field Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that will be used to create a new standby database for the Data Guard association.

### DBMS_CLOUD_OCI_DATABASE_CREATE_CROSS_REGION_DISASTER_RECOVERY_DETAILS_T Type

The following are the details necessary to create a disaster recovery (DR) association for an existing Autonomous Database with a standby in a remote region. *IMPORTANT* For creating a standby databases in a cross-region DR association: - To create the standby database in a remote region, use the API endpoint in the region where the standby is located. For example, if the primary database is in the IAD region and the standby is in the PHX region, make the API call using the PHX endpoint (https://database.us-phoenix-1.oraclecloud.com). See API Endpoints for the list of Database Service API endpoints. - To create the request in the standby database, the sourceId value must be the OCID of the primary database. The following parameters are required for the cross-region standby database and must contain the same values as the source Autonomous Database: - remoteDisasterRecoveryType The following parameters are optional for the cross-region standby database. If included in the request, these parameters must contain the same values as the source Autonomous Database: - dbName - dbVersion - ecpuCount - dataStorageSizeInTB - customerContacts - scheduledOperations - isAutoScalingForStorageEnabled - definedTags - freeformTags - licenseModel - whitelistedIps - isMtlsConnectionRequired Example I - Creating a cross-region standby with required parameters only: `{ \"compartmentId\": \"ocid.compartment.oc1..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"source\": \"CROSS_REGION_DISASTER_RECOVERY\", \"remoteDisasterRecoveryType\": \"BACKUP_BASED\" }` Example II - Creating a cross-region standby that specifies optional parameters in addition to the required parameters: `{ \"compartmentId\": \"ocid.compartment.oc1..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"ecpuCount\": 2, \"dbName\": \"adatabasedb1\", \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..&lt;var&gt;&amp;lt;unique_ID&amp;gt;&lt;/var&gt;\", \"dataStorageSizeInTBs\": 1, \"source\": \"CROSS_REGION_DISASTER_RECOVERY\", \"adminPassword\" : \"&lt;var&gt;&amp;lt;password&amp;gt;&lt;/var&gt;\", \"dbVersion\": \"19c\", \"licenseModel\": \"LICENSE_INCLUDED\", \"isAutoScalingForStorageEnabled\": \"true\", \"remoteDisasterRecoveryType\": \"BACKUP_BASED\" }`

Syntax
```

```

`dbms_cloud_oci_database_create_cross_region_disaster_recovery_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

Fields

Field Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that will be used to create a new standby database for the DR association.

`remote_disaster_recovery_type`

(required) Indicates the cross-region disaster recovery (DR) type of the standby Autonomous Database Serverless instance. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_DETAILS_T Type

The configuration details for creating a Data Guard association between databases. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`database_admin_password`

(required) A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation. The password must contain no fewer than nine characters and include: * At least two uppercase characters. * At least two lowercase characters. * At least two numeric characters. * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only. **The password MUST be the same as the primary admin password.**

`protection_mode`

(required) The protection mode to set up between the primary and standby databases. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation. **IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE', 'MAXIMUM_PROTECTION'

`transport_type`

(required) The redo transport type to use for this Data Guard association. Valid values depend on the specified `protectionMode`: * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC For more information, see[Redo Transport Services](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)in the Oracle Data Guard documentation. **IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.

Allowed values are: 'SYNC', 'ASYNC', 'FASTSYNC'

`creation_type`

(required) Specifies whether to create the peer database in an existing DB system or in a new DB system.

`is_active_data_guard_enabled`

(optional) True if active Data Guard is enabled.

`peer_db_unique_name`

(optional) Specifies the `DB_UNIQUE_NAME` of the peer database to be created.

`peer_sid_prefix`

(optional) Specifies a prefix for the `Oracle SID` of the database to be created.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_TO_EXISTING_DB_SYSTEM_DETAILS_T Type

The configuration details for creating a Data Guard association for a bare metal or Exadata DB system database. For these types of DB system databases, the `creationType` should be `ExistingDbSystem`. A standby database will be created in the DB system you specify. To create a Data Guard association for a database in a virtual machine DB system, use the`CREATE_DATA_GUARD_ASSOCIATION_WITH_NEW_DB_SYSTEM_DETAILS`Function subtype instead.

Syntax
```

```

`dbms_cloud_oci_database_create_data_guard_association_to_existing_db_system_details_t`is a subtype of the`dbms_cloud_oci_database_create_data_guard_association_details_t`type.

Fields

Field Description

`peer_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system in which to create the standby database. You must supply this value if creationType is `ExistingDbSystem`.

`peer_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB home in which to create the standby database. You must supply this value to create standby database with an existing DB home

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_TO_EXISTING_VM_CLUSTER_DETAILS_T Type

The configuration details for creating a Data Guard association for a ExaCC Vmcluster database. For these types of vm cluster databases, the `creationType` should be `ExistingVmCluster`. A standby database will be created in the VM cluster you specify.

Syntax
```

```

`dbms_cloud_oci_database_create_data_guard_association_to_existing_vm_cluster_details_t`is a subtype of the`dbms_cloud_oci_database_create_data_guard_association_details_t`type.

Fields

Field Description

`peer_vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Cluster in which to create the standby database. You must supply this value if creationType is `ExistingVmCluster`.

`peer_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB home in which to create the standby database. You must supply this value to create standby database with an existing DB home

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_WITH_NEW_DB_SYSTEM_DETAILS_T Type

The configuration details for creating a Data Guard association for a virtual machine DB system database. For this type of DB system database, the `creationType` should be `NewDbSystem`. A new DB system will be launched to create the standby database. To create a Data Guard association for a database in a bare metal or Exadata DB system, use the`CREATE_DATA_GUARD_ASSOCIATION_TO_EXISTING_DB_SYSTEM_DETAILS`Function subtype instead.

Syntax
```

```

`dbms_cloud_oci_database_create_data_guard_association_with_new_db_system_details_t`is a subtype of the`dbms_cloud_oci_database_create_data_guard_association_details_t`type.

Fields

Field Description

`display_name`

(optional) The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.

`availability_domain`

(optional) The name of the availability domain that the standby database DB system will be located in. For example- \"Uocm:PHX-AD-1\".

`shape`

(optional) The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system. Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system. To get a list of all shapes, use the`LIST_DB_SYSTEM_SHAPES`Function operation.

`cpu_core_count`

(optional) The number of OCPU cores available for AMD-based virtual machine DB systems.

`storage_volume_performance_mode`

(optional) The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See[Block Volume Performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm)for more information.

Allowed values are: 'BALANCED', 'HIGH_PERFORMANCE'

`node_count`

(optional) The number of nodes to launch for the DB system of the standby in the Data Guard association. For a 2-node RAC virtual machine DB system, specify either 1 or 2. If you do not supply this parameter, the default is the node count of the primary DB system.

`subnet_id`

(optional) The OCID of the subnet the DB system is associated with. **Subnet Restrictions:** - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28 These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`hostname`

(optional) The hostname for the DB node.

`time_zone`

(optional) The time zone of the dataguard standby DB system. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`fault_domains`

(optional) A Fault Domain is a grouping of hardware and infrastructure within an availability domain. Fault Domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or maintenance that affects one Fault Domain does not affect DB systems in other Fault Domains. If you do not specify the Fault Domain, the system selects one for you. To change the Fault Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain. If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into. The system assigns your nodes automatically to the Fault Domains you specify so that no Fault Domain contains more than one node. To get a list of Fault Domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`private_ip`

(optional) The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will be auto-assigned with an available IPv4 address from the subnet.

`license_model`

(optional) The Oracle license model that applies to all the databases on the dataguard standby DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`db_system_freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`db_system_defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`database_freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`database_defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_BASE_T Type

Details for creating a database. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`db_home_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`db_version`

(optional) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`source`

(required) The source of the database: Use `NONE` for creating a new database. Use `DB_BACKUP` for creating a new database by restoring from a backup. The default is `NONE`.

Allowed values are: 'NONE', 'DB_BACKUP'

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

### DBMS_CLOUD_OCI_DATABASE_DB_BACKUP_CONFIG_T Type

Backup Options To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`auto_backup_enabled`

(optional) If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.

`recovery_window_in_days`

(optional) Number of days between the current and the earliest point of recoverability covered by automatic backups. This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window. When the value is updated, it is applied to all existing automatic backups.

`auto_backup_window`

(optional) Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive). Example: `SLOT_TWO`

Allowed values are: 'SLOT_ONE', 'SLOT_TWO', 'SLOT_THREE', 'SLOT_FOUR', 'SLOT_FIVE', 'SLOT_SIX', 'SLOT_SEVEN', 'SLOT_EIGHT', 'SLOT_NINE', 'SLOT_TEN', 'SLOT_ELEVEN', 'SLOT_TWELVE'

`auto_full_backup_window`

(optional) Time window selected for initiating full backup for the database system. There are twelve available two-hour time windows. If no option is selected, the value is null and a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive). Example: `SLOT_TWO`

Allowed values are: 'SLOT_ONE', 'SLOT_TWO', 'SLOT_THREE', 'SLOT_FOUR', 'SLOT_FIVE', 'SLOT_SIX', 'SLOT_SEVEN', 'SLOT_EIGHT', 'SLOT_NINE', 'SLOT_TEN', 'SLOT_ELEVEN', 'SLOT_TWELVE'

`auto_full_backup_day`

(optional) Day of the week the full backup should be applied on the database system. If no option is selected, the value is null and we will default to Sunday.

Allowed values are: 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'

`run_immediate_full_backup`

(optional) If set to true, configures automatic full backups in the local region (the region of the DB system) for the first backup run immediately.

`backup_destination_details`

(optional) Backup destination details.

`backup_deletion_policy`

(optional) This defines when the backups will be deleted. - IMMEDIATE option keep the backup for predefined time i.e 72 hours and then delete permanently... - RETAIN will keep the backups as per the policy defined for database backups.

Allowed values are: 'DELETE_IMMEDIATELY', 'DELETE_AFTER_RETENTION_PERIOD'

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_DETAILS_T Type

Details for creating a database. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`db_name`

(required) The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the Oracle Database being backed up.

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`pdb_name`

(optional) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.

`admin_password`

(required) A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`tde_wallet_password`

(optional) The optional password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.

`character_set`

(optional) The character set for the database. The default is AL32UTF8. Allowed values are: AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS

`ncharacter_set`

(optional) The national character set for the database. The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.

`db_workload`

(optional) **Deprecated.** The dbWorkload field has been deprecated for Exadata Database Service on Dedicated Infrastructure, Exadata Database Service on Cloud@Customer, and Base Database Service. Support for this attribute will end in November 2023. You may choose to update your custom scripts to exclude the dbWorkload attribute. After November 2023 if you pass a value to the dbWorkload attribute, it will be ignored. The database workload type.

Allowed values are: 'OLTP', 'DSS'

`db_backup_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`sid_prefix`

(optional) Specifies a prefix for the `Oracle SID` of the database to be created.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_ANOTHER_DATABASE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`backup_tde_password`

(optional) The password to open the TDE wallet.

`admin_password`

(required) A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the Oracle Database being backed up.

`db_name`

(optional) The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.

`time_stamp_for_point_in_time_recovery`

(optional) The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to create the database.

`pluggable_databases`

(optional) The list of pluggable databases that needs to be restored into new database.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_BACKUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`backup_id`

(required) The backup[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`backup_tde_password`

(optional) The password to open the TDE wallet.

`admin_password`

(required) A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the Oracle Database being backed up.

`db_name`

(optional) The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.

`sid_prefix`

(optional) Specifies a prefix for the `Oracle SID` of the database to be created.

`pluggable_databases`

(optional) The list of pluggable databases that needs to be restored into new database.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_BACKUP_T Type

Details for creating a database by restoring from a database backup. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_database_create_database_from_backup_t`is a subtype of the`dbms_cloud_oci_database_create_database_base_t`type.

Fields

Field Description

`database`

(required)

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_DB_SYSTEM_DETAILS_T Type

Details for creating a database by restoring from a source database system. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`admin_password`

(required) A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`db_name`

(optional) The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.

`db_domain`

(optional) The database domain. In a distributed database system, DB_DOMAIN specifies the logical location of the database within the network structure.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the Oracle Database.

`db_backup_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_SOFTWARE_IMAGE_DETAILS_T Type

Parameters for creating a database software image in the specified compartment. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment the database software image belongs in.

`database_version`

(optional) The database version with which the database software image is to be built.

`display_name`

(required) The user-friendly name for the database software image. The name does not have to be unique.

`image_shape_family`

(optional) To what shape the image is meant for.

Allowed values are: 'VM_BM_SHAPE', 'EXADATA_SHAPE', 'EXACC_SHAPE'

`image_type`

(optional) The type of software image. Can be grid or database.

Allowed values are: 'GRID_IMAGE', 'DATABASE_IMAGE'

`patch_set`

(optional) The PSU or PBP or Release Updates. To get a list of supported versions, use the`LIST_DB_VERSIONS`Function operation.

`database_software_image_one_off_patches`

(optional) List of one-off patches for Database Homes.

`ls_inventory`

(optional) The output from the OPatch lsInventory command, which is passed as a string.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`source_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_BASE_T Type

Details for creating a Database Home. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-provided name of the Database Home.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`source`

(optional) The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.

Allowed values are: 'NONE', 'DB_BACKUP', 'DATABASE', 'VM_CLUSTER_BACKUP', 'VM_CLUSTER_NEW'

`is_desupported_version`

(optional) If true, the customer acknowledges that the specified Oracle Database software is an older release that is not currently supported by OCI.

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_DETAILS_T Type

Details for creating a Database Home. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-provided name of the Database Home.

`db_version`

(required) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`database`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_FROM_BACKUP_DETAILS_T Type

Details for creating a Database Home if you are creating a database by restoring from a database backup. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-provided name of the Database Home.

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image to be used to restore a database.

`database`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_FROM_DATABASE_DETAILS_T Type

Details for creating a Database Home if you are creating a database by restoring from a database backup. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-provided name of the Database Home.

`database`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_FROM_DB_SYSTEM_DETAILS_T Type

Details for creating a Database Home if you are cloning a database from a another database system. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-provided name of the Database Home.

`database`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_DB_SYSTEM_ID_DETAILS_T Type

Note that a valid `dbSystemId` value must be supplied for the `CreateDbHomeWithDbSystemId` API operation to successfully complete.

Syntax
```

```

`dbms_cloud_oci_database_create_db_home_with_db_system_id_details_t`is a subtype of the`dbms_cloud_oci_database_create_db_home_base_t`type.

Fields

Field Description

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`db_version`

(optional) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`database`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_DB_SYSTEM_ID_FROM_BACKUP_DETAILS_T Type

Note that a valid `dbSystemId` value must be supplied for the `CreateDbHomeWithDbSystemIdFromBackup` API operation to successfully complete.

Syntax
```

```

`dbms_cloud_oci_database_create_db_home_with_db_system_id_from_backup_details_t`is a subtype of the`dbms_cloud_oci_database_create_db_home_base_t`type.

Fields

Field Description

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`database`

(required)

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_DB_SYSTEM_ID_FROM_DATABASE_DETAILS_T Type

Note that a valid `dbSystemId` value must be supplied for the `CreateDbHomeWithDbSystemIdFromDatabase` API operation to successfully complete.

Syntax
```

```

`dbms_cloud_oci_database_create_db_home_with_db_system_id_from_database_details_t`is a subtype of the`dbms_cloud_oci_database_create_db_home_base_t`type.

Fields

Field Description

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`database`

(required)

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_VM_CLUSTER_ID_DETAILS_T Type

Note that a valid `vmClusterId` value must be supplied for the `CreateDbHomeWithVmClusterId` API operation to successfully complete.

Syntax
```

```

`dbms_cloud_oci_database_create_db_home_with_vm_cluster_id_details_t`is a subtype of the`dbms_cloud_oci_database_create_db_home_base_t`type.

Fields

Field Description

`vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`db_version`

(optional) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`database`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_VM_CLUSTER_ID_FROM_BACKUP_DETAILS_T Type

Note that a valid `vmClusterId` value must be supplied for the `CreateDbHomeWithVmClusterIdFromBackup` API operation to successfully complete.

Syntax
```

```

`dbms_cloud_oci_database_create_db_home_with_vm_cluster_id_from_backup_details_t`is a subtype of the`dbms_cloud_oci_database_create_db_home_base_t`type.

Fields

Field Description

`vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`database`

(required)

### DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_CONTACT_T Type

Contact details for Exadata Infrastructure.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Exadata Infrastructure contact.

`phone_number`

(optional) The phone number for the Exadata Infrastructure contact.

`email`

(required) The email for the Exadata Infrastructure contact.

`is_primary`

(required) If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.

`is_contact_mos_validated`

(optional) If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure contact is not a valid MOS contact.

### DBMS_CLOUD_OCI_DATABASE_NETWORK_BONDING_MODE_DETAILS_T Type

Details of bonding mode for Client and Backup and DR networks of an Exadata infrastructure.

Syntax
```

```

Fields

Field Description

`client_network_bonding_mode`

(optional) The network bonding mode for the Exadata infrastructure.

Allowed values are: 'ACTIVE_BACKUP', 'LACP'

`backup_network_bonding_mode`

(optional) The network bonding mode for the Exadata infrastructure.

Allowed values are: 'ACTIVE_BACKUP', 'LACP'

`dr_network_bonding_mode`

(optional) The network bonding mode for the Exadata infrastructure.

Allowed values are: 'ACTIVE_BACKUP', 'LACP'

### DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_CONTACT_TBL Type

Nested table type of dbms_cloud_oci_database_exadata_infrastructure_contact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXADATA_INFRASTRUCTURE_DETAILS_T Type

Request to create Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only. See`CREATE_CLOUD_EXADATA_INFRASTRUCTURE_DETAILS`Function for information on creating a cloud Exadata infrastructure resource in an Exadata Cloud Service instance.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the Exadata infrastructure. The name does not need to be unique.

`shape`

(required) The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.

`time_zone`

(required) The time zone of the Exadata infrastructure. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`cloud_control_plane_server1`

(required) The IP address for the first control plane server.

`cloud_control_plane_server2`

(required) The IP address for the second control plane server.

`netmask`

(required) The netmask for the control plane network.

`gateway`

(required) The gateway for the control plane network.

`admin_network_cidr`

(required) The CIDR block for the Exadata administration network.

`infini_band_network_cidr`

(required) The CIDR block for the Exadata InfiniBand interconnect.

`corporate_proxy`

(optional) The corporate network proxy for access to the control plane network. Oracle recommends using an HTTPS proxy when possible for enhanced security.

`contacts`

(optional) The list of contacts for the Exadata infrastructure.

`maintenance_window`

(optional)

`storage_count`

(optional) The number of storage servers for the Exadata infrastructure.

`compute_count`

(optional) The number of compute servers for the Exadata infrastructure.

`is_multi_rack_deployment`

(optional) Indicates if deployment is Multi-Rack or not.

`multi_rack_configuration_file`

(optional) The base64 encoded Multi-Rack configuration json file.

`dns_server`

(required) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp_server`

(required) The list of NTP server IP addresses. Maximum of 3 allowed.

`is_cps_offline_report_enabled`

(optional) Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status themselves and fix problems on their end, saving time and frustration for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata infrastructure provisioning. You can also disable or enable it at any time using the UpdateExadatainfrastructure API.

`network_bonding_mode_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_BACKUP_JOB_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The targeted availability domain for the backup.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where this backup should be created.

`display_name`

(required) A user-friendly name for the backup. This name does not have to be unique.

`db_version`

(required) A valid Oracle Database version.

`db_name`

(required) The name of the database from which the backup is being taken.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the Oracle Database being backed up.

`pdb_name`

(optional) The pluggable database name.

`external_database_identifier`

(required) The `DBID` of the Oracle Database being backed up.

`character_set`

(required) The character set for the database.

`ncharacter_set`

(required) The national character set for the database.

`database_mode`

(required) The mode (single instance or RAC) of the database being backed up.

Allowed values are: 'SI', 'RAC'

`database_edition`

(required) The Oracle Database edition to use for creating a database from this standalone backup. Note that 2-node RAC DB systems require Enterprise Edition - Extreme Performance.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS_T Type

Details for creating an external container database resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS_T Type

Details for creating an external database connector resource.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function. The name does not have to be unique.

`connector_type`

(optional) The type of connector used by the external database resource.

Allowed values are: 'MACS'

`external_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database resource.

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_DATABASE_DETAILS_BASE_T Type

Details for creating an external database.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRING_T Type

The Oracle Database connection string.

Syntax
```

```

Fields

Field Description

`hostname`

(required) The host name of the database.

`port`

(required) The port used to connect to the database.

`service`

(required) The name of the service alias used to connect to the database.

`protocol`

(required) The protocol used to connect to the database.

Allowed values are: 'TCP', 'TCPS'

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_CREDENTIALS_T Type

Credentials used to connect to the database. Currently only the `DETAILS` type is supported for creating MACS connector crendentials.

Syntax
```

```

Fields

Field Description

`credential_type`

(optional) The type of credential used to connect to the database.

Allowed values are: 'NAME_REFERENCE', 'DETAILS', 'SSL_DETAILS'

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_MACS_CONNECTOR_DETAILS_T Type

Details for creating a resource used to connect to an external Oracle Database using the[Management Agent cloud service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html).

Syntax
```

```

`dbms_cloud_oci_database_create_external_macs_connector_details_t`is a subtype of the`dbms_cloud_oci_database_create_external_database_connector_details_t`type.

Fields

Field Description

`connection_string`

(required)

`connection_credentials`

(required)

`connector_agent_id`

(required) The ID of the agent used for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_NON_CONTAINER_DATABASE_DETAILS_T Type

Details for creating an external non-container database resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS_T Type

Details for creating an external pluggable database resource.

Syntax
```

```

Fields

Field Description

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the the non-container database that was converted to a pluggable database to create this resource.

`external_container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function that contains the specified`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_KEY_STORE_TYPE_DETAILS_T Type

Key store type details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of key store.

Allowed values are: 'ORACLE_KEY_VAULT'

### DBMS_CLOUD_OCI_DATABASE_CREATE_KEY_STORE_DETAILS_T Type

Details for the create key store operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the key store. The name does not need to be unique.

`type_details`

(required)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_MAINTENANCE_RUN_DETAILS_T Type

Details to schedule Maintenance Run with Latest Release Update along TimeZone File Update for the specified resource.

Syntax
```

```

Fields

Field Description

`target_resource_id`

(required) The ID of the target resource for which the maintenance run should be created.

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`time_scheduled`

(required) The date and time that update should be scheduled.

`patching_mode`

(optional) Cloud Exadata infrastructure node patching method, either \"ROLLING\" or \"NONROLLING\". Default value is ROLLING. *IMPORTANT*: Non-rolling infrastructure patching involves system down time. See[Oracle-Managed Infrastructure Maintenance Updates](https://docs.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle)for more information.

Allowed values are: 'ROLLING', 'NONROLLING'

`patch_type`

(required) Patch type, either \"QUARTERLY\" or \"TIMEZONE\".

Allowed values are: 'QUARTERLY', 'TIMEZONE'

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Maintenance Run.

### DBMS_CLOUD_OCI_DATABASE_CREATE_NFS_BACKUP_DESTINATION_DETAILS_T Type

Used for creating NFS backup destinations.

Syntax
```

```

`dbms_cloud_oci_database_create_nfs_backup_destination_details_t`is a subtype of the`dbms_cloud_oci_database_create_backup_destination_details_t`type.

Fields

Field Description

`local_mount_point_path`

(optional) **Deprecated.** The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes. This field is deprecated. Use the mountTypeDetails field instead to specify the mount type for NFS.

`mount_type_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CREATE_NEW_DATABASE_DETAILS_T Type

Details for creating a new database. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

`dbms_cloud_oci_database_create_new_database_details_t`is a subtype of the`dbms_cloud_oci_database_create_database_base_t`type.

Fields

Field Description

`database`

(required)

### DBMS_CLOUD_OCI_DATABASE_CREATE_ONEOFF_PATCH_DETAILS_T Type

Data to create the one-off patch for the specificed database version.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) One-off patch name.

`db_version`

(required) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`release_update`

(required) The PSU or PBP or Release Updates. To get a list of supported versions, use the`LIST_DB_VERSIONS`Function operation.

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_CREATION_TYPE_DETAILS_T Type

The Pluggable Database creation type. Use `LOCAL_CLONE_PDB` for creating a new PDB using Local Clone on Source Pluggable Database. This will Clone and starts a pluggable database (PDB) in the same database (CDB) as the source PDB. The source PDB must be in the `READ_WRITE` openMode to perform the clone operation. Use `REMOTE_CLONE_PDB` for creating a new PDB using Remote Clone on Source Pluggable Database. This will Clone a pluggable database (PDB) to a different database from the source PDB. The cloned PDB will be started upon completion of the clone operation. The source PDB must be in the `READ_WRITE` openMode when performing the clone. For Exadata Cloud@Customer instances, the source pluggable database (PDB) must be on the same Exadata Infrastructure as the target container database (CDB) to create a remote clone. Use `RELOCATE_PDB` for relocating the Pluggable Database from Source CDB and creating it in target CDB. This will relocate a pluggable database (PDB) to a different database from the source PDB. The source PDB must be in the `READ_WRITE` openMode when performing the relocate.

Syntax
```

```

Fields

Field Description

`creation_type`

(required) The Pluggable Database creation type.

Allowed values are: 'LOCAL_CLONE_PDB', 'REMOTE_CLONE_PDB', 'RELOCATE_PDB'

### DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_DETAILS_T Type

Parameters for creating a pluggable database in a specified container database (CDB). Additional option `pdbCreationTypeDetails` can be used for creating Pluggable Database using different operations, e.g. LocalClone, Remote Clone, Relocate. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`pdb_name`

(required) The name for the pluggable database (PDB). The name is unique in the context of a`DATABASE`Type. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.

`container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CDB

`pdb_admin_password`

(optional) A strong password for PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`tde_wallet_password`

(optional) The existing TDE wallet password of the CDB.

`should_pdb_admin_account_be_locked`

(optional) The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it. If true, the pluggable database will be locked and user cannot login to it.

`container_database_admin_password`

(optional) The DB system administrator password of the Container Database.

`should_create_pdb_backup`

(optional) Indicates whether to take Pluggable Database Backup after the operation.

`pdb_creation_type_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_FROM_LOCAL_CLONE_DETAILS_T Type

Specifies the creation type Local Clone.

Syntax
```

```

`dbms_cloud_oci_database_create_pluggable_database_from_local_clone_details_t`is a subtype of the`dbms_cloud_oci_database_create_pluggable_database_creation_type_details_t`type.

Fields

Field Description

`source_pluggable_database_id`

(required) The OCID of the Source Pluggable Database.

### DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_FROM_RELOCATE_DETAILS_T Type

Specifies the creation type Relocate. Additional input 'dblinkUsername` and `dblinkUserPassword` can be provided for Relocate Operation. If not provided, Backend will create a temporary user to perform Relocate operation.

Syntax
```

```

`dbms_cloud_oci_database_create_pluggable_database_from_relocate_details_t`is a subtype of the`dbms_cloud_oci_database_create_pluggable_database_creation_type_details_t`type.

Fields

Field Description

`dblink_username`

(optional) The name of the DB link user.

`dblink_user_password`

(optional) The DB link user password.

`source_pluggable_database_id`

(required) The OCID of the Source Pluggable Database.

`source_container_database_admin_password`

(required) The DB system administrator password of the source Container Database.

### DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_REFRESHABLE_CLONE_DETAILS_T Type

Parameters for creating Pluggable Database Refreshable Clone. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`is_refreshable_clone`

(optional) Indicates whether Pluggable Database is a refreshable clone.

### DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_FROM_REMOTE_CLONE_DETAILS_T Type

Specifies the creation type Remote Clone. Additional input 'dblinkUsername` and `dblinkUserPassword` can be provided for RemoteClone/Create RefreshableClone Operation. If not provided, Backend will create a temporary user to perform RemoteClone operation. It is a required input parameter in case of creating Refreshable Clone PDB.

Syntax
```

```

`dbms_cloud_oci_database_create_pluggable_database_from_remote_clone_details_t`is a subtype of the`dbms_cloud_oci_database_create_pluggable_database_creation_type_details_t`type.

Fields

Field Description

`dblink_username`

(optional) The name of the DB link user.

`dblink_user_password`

(optional) The DB link user password.

`source_pluggable_database_id`

(required) The OCID of the Source Pluggable Database.

`source_container_database_admin_password`

(required) The DB system administrator password of the source Container Database.

`refreshable_clone_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_CREATE_RECOVERY_APPLIANCE_BACKUP_DESTINATION_DETAILS_T Type

Used for creating Recovery Appliance backup destinations.

Syntax
```

```

`dbms_cloud_oci_database_create_recovery_appliance_backup_destination_details_t`is a subtype of the`dbms_cloud_oci_database_create_backup_destination_details_t`type.

Fields

Field Description

`connection_string`

(required) The connection string for connecting to the Recovery Appliance.

`vpc_users`

(required) The Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.

### DBMS_CLOUD_OCI_DATABASE_CREATE_REFRESHABLE_AUTONOMOUS_DATABASE_CLONE_DETAILS_T Type

Details to create an Oracle Autonomous Database refreshable clone.

Syntax
```

```

`dbms_cloud_oci_database_create_refreshable_autonomous_database_clone_details_t`is a subtype of the`dbms_cloud_oci_database_create_autonomous_database_base_t`type.

Fields

Field Description

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source Autonomous Database that you will clone to create a new Autonomous Database.

`refreshable_mode`

(optional) The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

Allowed values are: 'AUTOMATIC', 'MANUAL'

### DBMS_CLOUD_OCI_DATABASE_CREATE_VM_CLUSTER_DETAILS_T Type

Details for the create Exadata VM cluster operation. Applies to Exadata Cloud@Customer instances only. For details on the create cloud Exadata VM cluster operation used with Exadata Cloud Service instances, see`CREATE_CLOUD_VM_CLUSTER_DETAILS`Function

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the VM cluster. The name does not need to be unique.

`exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`cpu_core_count`

(required) The number of CPU cores to enable for the VM cluster.

`ocpu_count`

(optional) The number of OCPU cores to enable for the VM cluster. Only one decimal place is allowed for the fractional part.

`memory_size_in_g_bs`

(optional) The memory to be allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage to be allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated in TBs.

`data_storage_size_in_g_bs`

(optional) The data disk group size to be allocated in GBs.

`ssh_public_keys`

(required) The public key portion of one or more key pairs used for SSH access to the VM cluster.

`vm_cluster_network_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`license_model`

(optional) The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`is_sparse_diskgroup_enabled`

(optional) If true, the sparse disk group is configured for the VM cluster. If false, the sparse disk group is not created.

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.

`time_zone`

(optional) The time zone to use for the VM cluster. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`gi_version`

(required) The Oracle Grid Infrastructure software version for the VM cluster.

`db_servers`

(optional) The list of Db server.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

`system_version`

(optional) Operating system version of the image.

### DBMS_CLOUD_OCI_DATABASE_DATA_GUARD_ASSOCIATION_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Data Guard association.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the reporting database.

`role`

(required) The role of the reporting database in this Data Guard association.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY'

`lifecycle_state`

(required) The current state of the Data Guard association.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'UPGRADING'

`lifecycle_details`

(optional) Additional information about the current lifecycleState, if available.

`peer_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system containing the associated peer database.

`peer_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home containing the associated peer database.

`peer_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated peer database.

`peer_data_guard_association_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer database's Data Guard association.

`peer_role`

(required) The role of the peer database in this Data Guard association.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY'

`apply_lag`

(optional) The lag time between updates to the primary database and application of the redo data on the standby database, as computed by the reporting database. Example: `9 seconds`

`apply_rate`

(optional) The rate at which redo logs are synced between the associated databases. Example: `180 Mb per second`

`protection_mode`

(required) The protection mode of this Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE', 'MAXIMUM_PROTECTION'

`transport_type`

(optional) The redo transport type used by this Data Guard association. For more information, see[Redo Transport Services](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)in the Oracle Data Guard documentation.

Allowed values are: 'SYNC', 'ASYNC', 'FASTSYNC'

`time_created`

(optional) The date and time the Data Guard association was created.

`is_active_data_guard_enabled`

(optional) True if active Data Guard is enabled.

### DBMS_CLOUD_OCI_DATABASE_DATA_GUARD_ASSOCIATION_SUMMARY_T Type

The properties that define a Data Guard association. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about endpoints and signing API requests, see[About the API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). For information about available SDKs and tools, see[SDKS and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Data Guard association.

`database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the reporting database.

`role`

(required) The role of the reporting database in this Data Guard association.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY'

`lifecycle_state`

(required) The current state of the Data Guard association.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'UPGRADING'

`lifecycle_details`

(optional) Additional information about the current lifecycleState, if available.

`peer_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system containing the associated peer database.

`peer_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home containing the associated peer database.

`peer_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated peer database.

`peer_data_guard_association_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the peer database's Data Guard association.

`peer_role`

(required) The role of the peer database in this Data Guard association.

Allowed values are: 'PRIMARY', 'STANDBY', 'DISABLED_STANDBY'

`apply_lag`

(optional) The lag time between updates to the primary database and application of the redo data on the standby database, as computed by the reporting database. Example: `9 seconds`

`apply_rate`

(optional) The rate at which redo logs are synced between the associated databases. Example: `180 Mb per second`

`protection_mode`

(required) The protection mode of this Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE', 'MAXIMUM_PROTECTION'

`transport_type`

(optional) The redo transport type used by this Data Guard association. For more information, see[Redo Transport Services](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)in the Oracle Data Guard documentation.

Allowed values are: 'SYNC', 'ASYNC', 'FASTSYNC'

`time_created`

(optional) The date and time the Data Guard association was created.

`is_active_data_guard_enabled`

(optional) True if active Data Guard is enabled.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRINGS_T Type

Connection strings to connect to an Oracle Database.

Syntax
```

```

Fields

Field Description

`cdb_default`

(optional) Host name based CDB Connection String.

`cdb_ip_default`

(optional) IP based CDB Connection String.

`all_connection_strings`

(optional) All connection strings to use to connect to the Database.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`character_set`

(optional) The character set for the database.

`ncharacter_set`

(optional) The national character set for the database.

`db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`db_name`

(required) The database name.

`pdb_name`

(optional) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.

`db_workload`

(optional) **Deprecated.** The dbWorkload field has been deprecated for Exadata Database Service on Dedicated Infrastructure, Exadata Database Service on Cloud@Customer, and Base Database Service. Support for this attribute will end in November 2023. You may choose to update your custom scripts to exclude the dbWorkload attribute. After November 2023 if you pass a value to the dbWorkload attribute, it will be ignored. The database workload type.

`db_unique_name`

(required) A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby databases). The unique name cannot be changed.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'BACKUP_IN_PROGRESS', 'UPGRADING', 'CONVERTING', 'TERMINATING', 'TERMINATED', 'RESTORE_FAILED', 'FAILED'

`time_created`

(optional) The date and time the database was created.

`last_backup_timestamp`

(optional) The date and time when the latest database backup was created.

`last_backup_duration_in_seconds`

(optional) The duration when the latest database backup created.

`last_failed_backup_timestamp`

(optional) The date and time when the latest database backup failed.

`db_backup_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`connection_strings`

(optional) The Connection strings used to connect to the Oracle Database.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`source_database_point_in_time_recovery_timestamp`

(optional) Point in time recovery timeStamp of the source database at which cloned database system is cloned from the source database system, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`is_cdb`

(optional) True if the database is a container database.

`database_management_config`

(optional)

`sid_prefix`

(optional) Specifies a prefix for the `Oracle SID` of the database to be created.

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_CREDENTAILS_BY_NAME_T Type

Existing named credential used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_database_connection_credentails_by_name_t`is a subtype of the`dbms_cloud_oci_database_database_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(required) The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_CREDENTIALS_BY_DETAILS_T Type

User information to connect to the database. Required when performing the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function operation. *IMPORTANT*: Not supported for the`UPDATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function operation.

Syntax
```

```

`dbms_cloud_oci_database_database_connection_credentials_by_details_t`is a subtype of the`dbms_cloud_oci_database_database_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(optional) The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

`username`

(required) The username that will be used to connect to the database.

`password`

(required) The password that will be used to connect to the database.

`role`

(required) The role of the user that will be connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

### DBMS_CLOUD_OCI_DATABASE_DATABASE_CREDENTIAL_DETAILS_T Type

Data for the credential used to connect to the database.

Syntax
```

```

Fields

Field Description

`user_name`

(required) The name of the Oracle Database user that will be used to connect to the database.

`password_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

### DBMS_CLOUD_OCI_DATABASE_DATABASE_MANAGEMENT_CONFIG_T Type

The configuration of the Database Management service.

Syntax
```

```

Fields

Field Description

`database_management_status`

(required) The status of the Database Management service.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`database_management_connection_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

`license_model`

(optional) The Oracle license model that applies to the external database.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_DATABASE_SOFTWARE_IMAGE_T Type

Database software images are created by specifying a patch set, one-off patches and patches for the database home (listed by `ls inventory`).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database software image.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_version`

(required) The database version with which the database software image is to be built.

`display_name`

(required) The user-friendly name for the database software image. The name does not have to be unique.

`lifecycle_state`

(required) The current state of the database software image.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'DELETING', 'DELETED', 'FAILED', 'TERMINATING', 'TERMINATED', 'UPDATING'

`lifecycle_details`

(optional) Detailed message for the lifecycle state.

`time_created`

(required) The date and time the database software image was created.

`image_type`

(required) The type of software image. Can be grid or database.

Allowed values are: 'GRID_IMAGE', 'DATABASE_IMAGE'

`image_shape_family`

(required) To what shape the image is meant for.

Allowed values are: 'VM_BM_SHAPE', 'EXADATA_SHAPE', 'EXACC_SHAPE'

`patch_set`

(required) The PSU or PBP or Release Updates. To get a list of supported versions, use the`LIST_DB_VERSIONS`Function operation.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`database_software_image_included_patches`

(optional) List of one-off patches for Database Homes.

`included_patches_summary`

(optional) The patches included in the image and the version of the image.

`database_software_image_one_off_patches`

(optional) List of one-off patches for Database Homes.

`ls_inventory`

(optional) The output from the OPatch lsInventory command, which is passed as a string.

`is_upgrade_supported`

(optional) True if this Database software image is supported for Upgrade.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_SOFTWARE_IMAGE_SUMMARY_T Type

The Database service supports the creation of database software images for use in creating and patching DB systems and databases. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database software image.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`database_version`

(required) The database version with which the database software image is to be built.

`display_name`

(required) The user-friendly name for the database software image. The name does not have to be unique.

`lifecycle_state`

(required) The current state of the database software image.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'DELETING', 'DELETED', 'FAILED', 'TERMINATING', 'TERMINATED', 'UPDATING'

`lifecycle_details`

(optional) Detailed message for the lifecycle state.

`time_created`

(required) The date and time the database software image was created.

`image_type`

(required) The type of software image. Can be grid or database.

Allowed values are: 'GRID_IMAGE', 'DATABASE_IMAGE'

`image_shape_family`

(required) To what shape the image is meant for.

Allowed values are: 'VM_BM_SHAPE', 'EXADATA_SHAPE', 'EXACC_SHAPE'

`patch_set`

(required) The PSU or PBP or Release Updates. To get a list of supported versions, use the`LIST_DB_VERSIONS`Function operation.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`database_software_image_included_patches`

(optional) List of one-off patches for Database Homes.

`included_patches_summary`

(optional) The patches included in the image and the version of the image.

`database_software_image_one_off_patches`

(optional) List of one-off patches for Database Homes.

`ls_inventory`

(optional) The output from the OPatch lsInventory command, which is passed as a string.

`is_upgrade_supported`

(optional) True if this Database software image is supported for Upgrade.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_SSL_CONNECTION_CREDENTIALS_T Type

Ssl connection credential details used to connect to the database.

Syntax
```

```

`dbms_cloud_oci_database_database_ssl_connection_credentials_t`is a subtype of the`dbms_cloud_oci_database_database_connection_credentials_t`type.

Fields

Field Description

`l_credential_name`

(optional) The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters. The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for the \".\" character that separates the \"x\" and \"y\" portions of the name. *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already using the name. For example: inventorydb.abc112233445566778899

`username`

(required) The username that will be used to connect to the database.

`password`

(required) The password that will be used to connect to the database.

`role`

(required) The role of the user that will be connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

`ssl_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

### DBMS_CLOUD_OCI_DATABASE_DATABASE_SUMMARY_T Type

An Oracle Database on a bare metal or virtual machine DB system. For more information, see[Bare Metal and Virtual Machine DB Systems](https://docs.oracle.com/iaas/Content/Database/Concepts/overview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`character_set`

(optional) The character set for the database.

`ncharacter_set`

(optional) The national character set for the database.

`db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`db_name`

(required) The database name.

`pdb_name`

(optional) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.

`db_workload`

(optional) **Deprecated.** The dbWorkload field has been deprecated for Exadata Database Service on Dedicated Infrastructure, Exadata Database Service on Cloud@Customer, and Base Database Service. Support for this attribute will end in November 2023. You may choose to update your custom scripts to exclude the dbWorkload attribute. After November 2023 if you pass a value to the dbWorkload attribute, it will be ignored. The database workload type.

`db_unique_name`

(required) A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby databases). The unique name cannot be changed.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'BACKUP_IN_PROGRESS', 'UPGRADING', 'CONVERTING', 'TERMINATING', 'TERMINATED', 'RESTORE_FAILED', 'FAILED'

`time_created`

(optional) The date and time the database was created.

`last_backup_timestamp`

(optional) The date and time when the latest database backup was created.

`last_backup_duration_in_seconds`

(optional) The duration when the latest database backup created.

`last_failed_backup_timestamp`

(optional) The date and time when the latest database backup failed.

`db_backup_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`connection_strings`

(optional) The Connection strings used to connect to the Oracle Database.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`source_database_point_in_time_recovery_timestamp`

(optional) Point in time recovery timeStamp of the source database at which cloned database system is cloned from the source database system, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

`is_cdb`

(optional) True if the database is a container database.

`database_management_config`

(optional)

`sid_prefix`

(optional) Specifies a prefix for the `Oracle SID` of the database to be created.

`key_store_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`key_store_wallet_name`

(optional) The wallet name for Oracle Key Vault.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_HISTORY_ENTRY_T Type

The Database service supports the upgrade history of databases. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database upgrade history.

`action`

(required) The database upgrade action.

Allowed values are: 'PRECHECK', 'UPGRADE', 'ROLLBACK'

`source`

(optional) The source of the Oracle Database software to be used for the upgrade. - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home. - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database. - Use `DB_SOFTWARE_IMAGE` to specify a[database software image](https://docs.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm)to upgrade the database.

Allowed values are: 'DB_HOME', 'DB_VERSION', 'DB_SOFTWARE_IMAGE'

`lifecycle_state`

(required) Status of database upgrade history SUCCEEDED|IN_PROGRESS|FAILED.

Allowed values are: 'SUCCEEDED', 'FAILED', 'IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`target_db_version`

(optional) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`target_database_software_image_id`

(optional) the database software image used for upgrading database.

`target_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`source_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`time_started`

(required) The date and time when the database upgrade started.

`time_ended`

(optional) The date and time when the database upgrade ended.

`options`

(optional) Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: \"-upgradeTimezone false -keepEvents\"

### DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_HISTORY_ENTRY_SUMMARY_T Type

The Database service supports the upgrade history of databases. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database upgrade history.

`action`

(required) The database upgrade action.

Allowed values are: 'PRECHECK', 'UPGRADE', 'ROLLBACK'

`source`

(optional) The source of the Oracle Database software to be used for the upgrade. - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home. - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database. - Use `DB_SOFTWARE_IMAGE` to specify a[database software image](https://docs.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm)to upgrade the database.

Allowed values are: 'DB_HOME', 'DB_VERSION', 'DB_SOFTWARE_IMAGE'

`lifecycle_state`

(required) Status of database upgrade history SUCCEEDED|IN_PROGRESS|FAILED.

Allowed values are: 'SUCCEEDED', 'FAILED', 'IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`target_db_version`

(optional) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`target_database_software_image_id`

(optional) the database software image used for upgrading database.

`target_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`source_db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`time_started`

(required) The date and time when the database upgrade started.

`time_ended`

(optional) The date and time when the database upgrade ended.

`options`

(optional) Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: \"-upgradeTimezone false -keepEvents\"

### DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_SOURCE_BASE_T Type

Details for the database upgrade source.

Syntax
```

```

Fields

Field Description

`source`

(optional) The source of the Oracle Database software to be used for the upgrade. - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home. - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database. - Use `DB_SOFTWARE_IMAGE` to specify a[database software image](https://docs.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm)to upgrade the database.

Allowed values are: 'DB_HOME', 'DB_VERSION', 'DB_SOFTWARE_IMAGE'

`options`

(optional) Additional upgrade options supported by DBUA(Database Upgrade Assistant). Example: \"-upgradeTimezone false -keepEvents\"

### DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_WITH_DATABASE_SOFTWARE_IMAGE_DETAILS_T Type

Details of the database software image to be used to upgrade a database.

Syntax
```

```

`dbms_cloud_oci_database_database_upgrade_with_database_software_image_details_t`is a subtype of the`dbms_cloud_oci_database_database_upgrade_source_base_t`type.

Fields

Field Description

`database_software_image_id`

(required) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image to be used to upgrade a database.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_WITH_DB_HOME_DETAILS_T Type

Details of Database Home to be used to upgrade a database.

Syntax
```

```

`dbms_cloud_oci_database_database_upgrade_with_db_home_details_t`is a subtype of the`dbms_cloud_oci_database_database_upgrade_source_base_t`type.

Fields

Field Description

`db_home_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

### DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_WITH_DB_VERSION_DETAILS_T Type

Details of the Oracle Database software version number for upgrading a database.

Syntax
```

```

`dbms_cloud_oci_database_database_upgrade_with_db_version_details_t`is a subtype of the`dbms_cloud_oci_database_database_upgrade_source_base_t`type.

Fields

Field Description

`db_version`

(required) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

### DBMS_CLOUD_OCI_DATABASE_DB_HOME_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-provided name for the Database Home. The name does not need to be unique.

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation is started.

`lifecycle_state`

(required) The current state of the Database Home.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`db_version`

(required) The Oracle Database version.

`db_home_location`

(required) The location of the Oracle Database Home.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the Database Home was created.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

### DBMS_CLOUD_OCI_DATABASE_DB_HOME_FROM_AGENT_RESOURCE_ID_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-provided name for the Database Home. The name does not need to be unique.

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation is started.

`lifecycle_state`

(required) The current state of the Database Home.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`db_version`

(required) The Oracle Database version.

`db_home_location`

(required) The location of the Oracle Database Home.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the Database Home was created.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

### DBMS_CLOUD_OCI_DATABASE_DB_HOME_SUMMARY_T Type

A directory where Oracle Database software is installed. A bare metal or Exadata DB system can have multiple Database Homes and each Database Home can run a different supported version of Oracle Database. A virtual machine DB system can have only one Database Home. For more information, see[Bare Metal and Virtual Machine DB Systems](https://docs.oracle.com/iaas/Content/Database/Concepts/overview.htm)and[Exadata DB Systems](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-provided name for the Database Home. The name does not need to be unique.

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation is started.

`lifecycle_state`

(required) The current state of the Database Home.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`db_version`

(required) The Oracle Database version.

`db_home_location`

(required) The location of the Oracle Database Home.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(optional) The date and time the Database Home was created.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`database_software_image_id`

(optional) The database software image[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)

### DBMS_CLOUD_OCI_DATABASE_DB_NODE_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database node.

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

`backup_vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup VNIC.

`host_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host IP address associated with the database node. Use this OCID with either the`GET_PRIVATE_IP`Function or the`GET_PUBLIC_IP_BY_PRIVATE_IP_ID`Function API to get the IP address needed to make a database connection. **Note:** Applies only to Exadata Cloud Service.

`backup_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup IP address associated with the database node. Use this OCID with either the`GET_PRIVATE_IP`Function or the`GET_PUBLIC_IP_BY_PRIVATE_IP_ID`Function API to get the IP address needed to make a database connection. **Note:** Applies only to Exadata Cloud Service.

`vnic2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second VNIC. **Note:** Applies only to Exadata Cloud Service.

`backup_vnic2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second backup VNIC. **Note:** Applies only to Exadata Cloud Service.

`lifecycle_state`

(required) The current state of the database node.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'FAILED'

`hostname`

(optional) The host name for the database node.

`fault_domain`

(optional) The name of the Fault Domain the instance is contained in.

`time_created`

(required) The date and time that the database node was created.

`software_storage_size_in_gb`

(optional) The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.

`maintenance_type`

(optional) The type of database node maintenance.

Allowed values are: 'VMDB_REBOOT_MIGRATION'

`time_maintenance_window_start`

(optional) Start date and time of maintenance window.

`time_maintenance_window_end`

(optional) End date and time of maintenance window.

`additional_details`

(optional) Additional information about the planned maintenance.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`lifecycle_details`

(optional) Information about the current lifecycle state.

`cpu_core_count`

(optional) The number of CPU cores enabled on the Db node.

`memory_size_in_g_bs`

(optional) The allocated memory in GBs on the Db node.

`db_node_storage_size_in_g_bs`

(optional) The allocated local node storage in GBs on the Db node.

`db_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exacc Db server associated with the database node.

### DBMS_CLOUD_OCI_DATABASE_DB_NODE_SUMMARY_T Type

A server where Oracle Database software is running. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database node.

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`vnic_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VNIC.

`backup_vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup VNIC.

`host_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the host IP address associated with the database node. Use this OCID with either the`GET_PRIVATE_IP`Function or the`GET_PUBLIC_IP_BY_PRIVATE_IP_ID`Function API to get the IP address needed to make a database connection. **Note:** Applies only to Exadata Cloud Service.

`backup_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup IP address associated with the database node. Use this OCID with either the`GET_PRIVATE_IP`Function or the`GET_PUBLIC_IP_BY_PRIVATE_IP_ID`Function API to get the IP address needed to make a database connection. **Note:** Applies only to Exadata Cloud Service.

`vnic2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second VNIC. **Note:** Applies only to Exadata Cloud Service.

`backup_vnic2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second backup VNIC. **Note:** Applies only to Exadata Cloud Service.

`lifecycle_state`

(required) The current state of the database node.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'STOPPING', 'STOPPED', 'STARTING', 'TERMINATING', 'TERMINATED', 'FAILED'

`hostname`

(optional) The host name for the database node.

`fault_domain`

(optional) The name of the Fault Domain the instance is contained in.

`time_created`

(required) The date and time that the database node was created.

`software_storage_size_in_gb`

(optional) The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.

`maintenance_type`

(optional) The type of database node maintenance.

Allowed values are: 'VMDB_REBOOT_MIGRATION'

`time_maintenance_window_start`

(optional) Start date and time of maintenance window.

`time_maintenance_window_end`

(optional) End date and time of maintenance window.

`additional_details`

(optional) Additional information about the planned maintenance.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`lifecycle_details`

(optional) Information about the current lifecycle state.

`cpu_core_count`

(optional) The number of CPU cores enabled on the Db node.

`memory_size_in_g_bs`

(optional) The allocated memory in GBs on the Db node.

`db_node_storage_size_in_g_bs`

(optional) The allocated local node storage in GBs on the Db node.

`db_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exacc Db server associated with the database node.

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_PATCHING_DETAILS_T Type

The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.

Syntax
```

```

Fields

Field Description

`estimated_patch_duration`

(optional) Estimated time, in minutes, to patch one database server.

`patching_status`

(optional) The status of the patching operation.

Allowed values are: 'SCHEDULED', 'MAINTENANCE_IN_PROGRESS', 'FAILED', 'COMPLETE'

`time_patching_started`

(optional) The time when the patching operation started.

`time_patching_ended`

(optional) The time when the patching operation ended.

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_T Type

Details of the Exacc Db server resource. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exacc Db server.

`display_name`

(optional) The user-friendly name for the Db server. The name does not need to be unique.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`cpu_core_count`

(optional) The number of CPU cores enabled on the Db server.

`memory_size_in_g_bs`

(optional) The allocated memory in GBs on the Db server.

`db_node_storage_size_in_g_bs`

(optional) The allocated local node storage in GBs on the Db server.

`vm_cluster_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Clusters associated with the Db server.

`autonomous_vm_cluster_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM Clusters associated with the Db server.

`autonomous_virtual_machine_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Virtual Machines associated with the Db server.

`db_node_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db nodes associated with the Db server.

`shape`

(optional) The shape of the Db server. The shape determines the amount of CPU, storage, and memory resources available.

`lifecycle_state`

(optional) The current state of the Db server.

Allowed values are: 'CREATING', 'AVAILABLE', 'UNAVAILABLE', 'DELETING', 'DELETED', 'MAINTENANCE_IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`max_cpu_count`

(optional) The total number of CPU cores available.

`max_memory_in_g_bs`

(optional) The total memory available in GBs.

`max_db_node_storage_in_g_bs`

(optional) The total local node storage available in GBs.

`time_created`

(optional) The date and time that the Db Server was created.

`db_server_patching_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_HISTORY_SUMMARY_T Type

Details of a database server maintenance history.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the database server.

`display_name`

(optional) The user-friendly name for the database server. The name does not need to be unique.

`db_server_patching_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_SUMMARY_T Type

Details of the Exadata Cloud@Customer Db server.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exacc Db server.

`display_name`

(optional) The user-friendly name for the Db server. The name does not need to be unique.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`cpu_core_count`

(optional) The number of CPU cores enabled on the Db server.

`memory_size_in_g_bs`

(optional) The allocated memory in GBs on the Db server.

`db_node_storage_size_in_g_bs`

(optional) The allocated local node storage in GBs on the Db server.

`vm_cluster_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM Clusters associated with the Db server.

`autonomous_vm_cluster_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous VM Clusters associated with the Db server.

`autonomous_virtual_machine_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Virtual Machines associated with the Db server.

`db_node_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db nodes associated with the Db server.

`shape`

(optional) The shape of the Db server. The shape determines the amount of CPU, storage, and memory resources available.

`lifecycle_state`

(optional) The current state of the Db server.

Allowed values are: 'CREATING', 'AVAILABLE', 'UNAVAILABLE', 'DELETING', 'DELETED', 'MAINTENANCE_IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`max_cpu_count`

(optional) The total number of CPU cores available.

`max_memory_in_g_bs`

(optional) The total memory available in GBs.

`max_db_node_storage_in_g_bs`

(optional) The total local node storage available in GBs.

`time_created`

(optional) The date and time that the Db Server was created.

`db_server_patching_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_OPTIONS_T Type

The DB system options.

Syntax
```

```

Fields

Field Description

`storage_management`

(optional) The storage option used in DB system. ASM - Automatic storage management LVM - Logical Volume management

Allowed values are: 'ASM', 'LVM'

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_T Type

Syntax
```

```

Fields

Field Description

`iorm_config_cache`

(optional)

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`availability_domain`

(required) The name of the availability domain that the DB system is located in.

`fault_domains`

(optional) List of the Fault Domains in which this DB system is provisioned.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the DB system is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`backup_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems. **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`memory_size_in_g_bs`

(optional) Memory allocated to the DB system, in gigabytes.

`storage_volume_performance_mode`

(optional) The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See[Block Volume Performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm)for more information.

Allowed values are: 'BALANCED', 'HIGH_PERFORMANCE'

`shape`

(required) The shape of the DB system. The shape determines resources to allocate to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, storage, and memory

`db_system_options`

(optional)

`ssh_public_keys`

(required) The public key portion of one or more key pairs used for SSH access to the DB system.

`time_zone`

(optional) The time zone of the DB system. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`hostname`

(required) The hostname for the DB system.

`domain`

(required) The domain name for the DB system.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`version`

(optional) The Oracle Database version of the DB system.

`os_version`

(optional) The most recent OS Patch Version applied on the DB system.

`cpu_core_count`

(required) The number of CPU cores enabled on the DB system.

`cluster_name`

(optional) The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`data_storage_percentage`

(optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.

`database_edition`

(required) The Oracle Database edition that applies to all the databases on the DB system.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation starts.

`listener_port`

(optional) The port number configured for the listener on the DB system.

`lifecycle_state`

(required) The current state of the DB system.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MIGRATED', 'MAINTENANCE_IN_PROGRESS', 'NEEDS_ATTENTION', 'UPGRADING'

`time_created`

(optional) The date and time the DB system was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`disk_redundancy`

(optional) The type of redundancy configured for the DB system. NORMAL is 2-way redundancy. HIGH is 3-way redundancy.

Allowed values are: 'HIGH', 'NORMAL'

`sparse_diskgroup`

(optional) True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.

`scan_ip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Single Client Access Name (SCAN) IP addresses associated with the DB system. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.

`vip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual IP (VIP) addresses associated with the DB system. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.

`scan_dns_record_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DNS record for the SCAN IP addresses that are associated with the DB system.

`scan_dns_name`

(optional) The FQDN of the DNS record for the SCAN IP addresses that are associated with the DB system.

`zone_id`

(optional) The OCID of the zone the DB system is associated with.

`data_storage_size_in_g_bs`

(optional) The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.

`reco_storage_size_in_gb`

(optional) The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.

`node_count`

(optional) The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.

`license_model`

(optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`maintenance_window`

(optional)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`source_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`point_in_time_data_disk_clone_timestamp`

(optional) The point in time for a cloned database system when the data disks were cloned from the source database system, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_COMPUTE_PERFORMANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_compute_performance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_COMPUTE_PERFORMANCE_SUMMARY_T Type

Representation of disk performance detail parameters.

Syntax
```

```

Fields

Field Description

`shape`

(required) The shape of the DB system.

`compute_performance_list`

(required) List of Compute performance details for the specified DB system shape.

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_SHAPE_SUMMARY_T Type

The shape of the DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the shape used for the DB system.

`shape_family`

(optional) The family of the shape used for the DB system.

`shape_type`

(optional) The shape type for the virtual machine DB system. Shape type is determined by CPU hardware. Valid values are `AMD` , `INTEL`, `INTEL_FLEX_X9` or `AMPERE_FLEX_A1`.

Allowed values are: 'AMD', 'INTEL', 'INTEL_FLEX_X9', 'AMPERE_FLEX_A1'

`shape`

(optional) Deprecated. Use `name` instead of `shape`.

`available_core_count`

(required) The maximum number of CPU cores that can be enabled on the DB system for this shape.

`minimum_core_count`

(optional) The minimum number of CPU cores that can be enabled on the DB system for this shape.

`core_count_increment`

(optional) The discrete number by which the CPU core count for this shape can be increased or decreased.

`min_storage_count`

(optional) The minimum number of Exadata storage servers available for the Exadata infrastructure.

`max_storage_count`

(optional) The maximum number of Exadata storage servers available for the Exadata infrastructure.

`available_data_storage_per_server_in_t_bs`

(optional) The maximum data storage available per storage server for this shape. Only applicable to ExaCC Elastic shapes.

`available_memory_per_node_in_g_bs`

(optional) The maximum memory available per database node for this shape. Only applicable to ExaCC Elastic shapes.

`available_db_node_per_node_in_g_bs`

(optional) The maximum Db Node storage available per database node for this shape. Only applicable to ExaCC Elastic shapes.

`min_core_count_per_node`

(optional) The minimum number of CPU cores that can be enabled per node for this shape.

`available_memory_in_g_bs`

(optional) The maximum memory that can be enabled for this shape.

`min_memory_per_node_in_g_bs`

(optional) The minimum memory that need be allocated per node for this shape.

`available_db_node_storage_in_g_bs`

(optional) The maximum Db Node storage that can be enabled for this shape.

`min_db_node_storage_per_node_in_g_bs`

(optional) The minimum Db Node storage that need be allocated per node for this shape.

`available_data_storage_in_t_bs`

(optional) The maximum DATA storage that can be enabled for this shape.

`min_data_storage_in_t_bs`

(optional) The minimum data storage that need be allocated for this shape.

`minimum_node_count`

(optional) The minimum number of compute servers available for this shape.

`maximum_node_count`

(optional) The maximum number of compute servers available for this shape.

`available_core_count_per_node`

(optional) The maximum number of CPU cores per database node that can be enabled for this shape. Only applicable to the flex Exadata shape, ExaCC Elastic shapes and VM Flex shapes.

### DBMS_CLOUD_OCI_DATABASE_DISK_PERFORMANCE_DETAILS_T Type

Representation of disk performance detail parameters.

Syntax
```

```

Fields

Field Description

`disk_iops`

(required) Disk IOPS in thousands.

`disk_throughput_in_mbps`

(required) Disk Throughput in Mbps.

### DBMS_CLOUD_OCI_DATABASE_STORAGE_PERFORMANCE_DETAILS_T Type

Representation of storage performance detail parameters.

Syntax
```

```

Fields

Field Description

`size_in_g_bs`

(required) Size in GBs.

`balanced_disk_performance`

(required)

`high_disk_performance`

(required)

### DBMS_CLOUD_OCI_DATABASE_STORAGE_PERFORMANCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_storage_performance_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_STORAGE_PERFORMANCE_SUMMARY_T Type

Representation of storage performance summary per shapeType .

Syntax
```

```

Fields

Field Description

`shape_type`

(required) ShapeType of the DbSystems INTEL , AMD, INTEL_FLEX_X9 or AMPERE_FLEX_A1

Allowed values are: 'AMD', 'INTEL', 'INTEL_FLEX_X9', 'AMPERE_FLEX_A1'

`data_storage_performance_list`

(required) List of storage performance for the DATA disks

`reco_storage_performance_list`

(required) List of storage performance for the RECO disks

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_SUMMARY_T Type

The Database Service supports several types of DB systems, ranging in size, price, and performance. For details about each type of system, see[Bare Metal and Virtual Machine DB Systems](https://docs.oracle.com/iaas/Content/Database/Concepts/overview.htm). **Note:** Deprecated for Exadata Cloud Service instances using the new[resource model](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model). To provision and manage new Exadata Cloud Service systems, use the`CLOUD_EXADATA_INFRASTRUCTURE`Type and`CLOUD_VM_CLUSTER`Type. See[Exadata Cloud Service](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm)for more information on Exadata systems. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity Service API. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the DB system. The name does not have to be unique.

`availability_domain`

(required) The name of the availability domain that the DB system is located in.

`fault_domains`

(optional) List of the Fault Domains in which this DB system is provisioned.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the DB system is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`backup_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems. **Subnet Restriction:** See the subnet restrictions information for **subnetId**.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`memory_size_in_g_bs`

(optional) Memory allocated to the DB system, in gigabytes.

`storage_volume_performance_mode`

(optional) The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See[Block Volume Performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm)for more information.

Allowed values are: 'BALANCED', 'HIGH_PERFORMANCE'

`shape`

(required) The shape of the DB system. The shape determines resources to allocate to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, storage, and memory

`db_system_options`

(optional)

`ssh_public_keys`

(required) The public key portion of one or more key pairs used for SSH access to the DB system.

`time_zone`

(optional) The time zone of the DB system. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`hostname`

(required) The hostname for the DB system.

`domain`

(required) The domain name for the DB system.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`version`

(optional) The Oracle Database version of the DB system.

`os_version`

(optional) The most recent OS Patch Version applied on the DB system.

`cpu_core_count`

(required) The number of CPU cores enabled on the DB system.

`cluster_name`

(optional) The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`data_storage_percentage`

(optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.

`database_edition`

(required) The Oracle Database edition that applies to all the databases on the DB system.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation starts.

`listener_port`

(optional) The port number configured for the listener on the DB system.

`lifecycle_state`

(required) The current state of the DB system.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MIGRATED', 'MAINTENANCE_IN_PROGRESS', 'NEEDS_ATTENTION', 'UPGRADING'

`time_created`

(optional) The date and time the DB system was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`disk_redundancy`

(optional) The type of redundancy configured for the DB system. NORMAL is 2-way redundancy. HIGH is 3-way redundancy.

Allowed values are: 'HIGH', 'NORMAL'

`sparse_diskgroup`

(optional) True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.

`scan_ip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Single Client Access Name (SCAN) IP addresses associated with the DB system. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.

`vip_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual IP (VIP) addresses associated with the DB system. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.

`scan_dns_record_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DNS record for the SCAN IP addresses that are associated with the DB system.

`scan_dns_name`

(optional) The FQDN of the DNS record for the SCAN IP addresses that are associated with the DB system.

`zone_id`

(optional) The OCID of the zone the DB system is associated with.

`data_storage_size_in_g_bs`

(optional) The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.

`reco_storage_size_in_gb`

(optional) The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.

`node_count`

(optional) The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.

`license_model`

(optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`maintenance_window`

(optional)

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`source_db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`point_in_time_data_disk_clone_timestamp`

(optional) The point in time for a cloned database system when the data disks were cloned from the source database system, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_UPGRADE_HISTORY_ENTRY_T Type

The record of an OS upgrade action on a DB system. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the upgrade history entry.

`action`

(required) The operating system upgrade action.

Allowed values are: 'PRECHECK', 'ROLLBACK', 'UPDATE_SNAPSHOT_RETENTION_DAYS', 'UPGRADE'

`new_gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`old_gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`old_os_version`

(optional) A valid Oracle Software (OS) version eg. Oracle Linux Server release 8

`new_os_version`

(optional) A valid Oracle Software (OS) version eg. Oracle Linux Server release 8

`snapshot_retention_period_in_days`

(required) The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.

`lifecycle_state`

(required) The current state of the action.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically contains additional displayable text.

`time_started`

(required) The date and time when the upgrade action started.

`time_ended`

(optional) The date and time when the upgrade action completed

### DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_UPGRADE_HISTORY_ENTRY_SUMMARY_T Type

The summary for the record of an OS upgrade action on a DB system.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the upgrade history entry.

`action`

(required) The operating system upgrade action.

Allowed values are: 'PRECHECK', 'ROLLBACK', 'UPDATE_SNAPSHOT_RETENTION_DAYS', 'UPGRADE'

`new_gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`old_gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`old_os_version`

(optional) A valid Oracle Software (OS) version eg. Oracle Linux Server release 8

`new_os_version`

(optional) A valid Oracle Software (OS) version eg. Oracle Linux Server release 8

`snapshot_retention_period_in_days`

(required) The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.

`lifecycle_state`

(required) The current state of the action.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically contains additional displayable text.

`time_started`

(required) The date and time when the upgrade action started.

`time_ended`

(optional) The date and time when the upgrade action completed

### DBMS_CLOUD_OCI_DATABASE_DB_VERSION_SUMMARY_T Type

The Oracle Database software version. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`version`

(required) A valid Oracle Database version.

`is_latest_for_major_version`

(optional) True if this version of the Oracle Database software is the latest version for a release.

`supports_pdb`

(optional) True if this version of the Oracle Database software supports pluggable databases.

`is_preview_db_version`

(optional) True if this version of the Oracle Database software is the preview version.

`is_upgrade_supported`

(optional) True if this version of the Oracle Database software is supported for Upgrade.

### DBMS_CLOUD_OCI_DATABASE_DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE_DETAILS_T Type

Details to deregister an Autonomous Database with Data Safe.

Syntax
```

```

Fields

Field Description

`pdb_admin_password`

(required) The admin password provided during the creation of the database. This password is between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.

### DBMS_CLOUD_OCI_DATABASE_DOWNLOAD_ONEOFF_PATCH_T Type

Data to download one-off patch.

Syntax
```

```

Fields

Field Description

`access_uri`

(required) URI to download one-off patch.

`time_created`

(required) The date and time one-off patch URI was created.

`time_expires`

(required) The date and time until which the one-off patch URI will be available for download.

### DBMS_CLOUD_OCI_DATABASE_DR_SCAN_DETAILS_T Type

The Single Client Access Name (SCAN) details for Disaster recovery network.

Syntax
```

```

Fields

Field Description

`hostname`

(required) The Disaster recovery SCAN hostname.

`scan_listener_port_tcp`

(required) The Disaster recovery SCAN TCPIP port. Default is 1521.

`ips`

(required) The list of Disaster recovery SCAN IP addresses. Three addresses should be provided.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_DATABASE_MANAGEMENT_DETAILS_T Type

Data to enable the Database Management service for the database.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`private_end_point_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`management_type`

(optional) The Database Management type.

Allowed values are: 'BASIC', 'ADVANCED'

`service_name`

(required) The name of the Oracle Database service that will be used to connect to the database.

`protocol`

(optional) Protocol used by the database connection.

Allowed values are: 'TCP', 'TCPS'

`port`

(optional) The port used to connect to the database.

`ssl_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`role`

(optional) The role of the user that will be connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_CONTAINER_DATABASE_DATABASE_MANAGEMENT_DETAILS_T Type

Details to enable Database Management on an external container database.

Syntax
```

```

Fields

Field Description

`license_model`

(required) The Oracle license model that applies to the external database.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_CONTAINER_DATABASE_STACK_MONITORING_DETAILS_T Type

Details to enable Stack Monitoring on the external container database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_DATABASE_MANAGEMENT_DETAILS_BASE_T Type

Details to enable Database Management on an external database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_DATABASE_OPERATIONS_INSIGHTS_DETAILS_BASE_T Type

Details to enable Operations Insights on the external database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_DATABASE_STACK_MONITORING_DETAILS_BASE_T Type

Details to enable Stack Monitoring on the external database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_DATABASE_MANAGEMENT_DETAILS_T Type

Details to enable Database Management on an external non-container database.

Syntax
```

```

Fields

Field Description

`license_model`

(required) The Oracle license model that applies to the external database.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_OPERATIONS_INSIGHTS_DETAILS_T Type

Details to enable Operations Insights on the external non-container database

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_STACK_MONITORING_DETAILS_T Type

Details to enable Stack Monitoring on the external non-container database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_PLUGGABLE_DATABASE_DATABASE_MANAGEMENT_DETAILS_T Type

Details to enable Database Management on an external pluggable database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_PLUGGABLE_DATABASE_OPERATIONS_INSIGHTS_DETAILS_T Type

Details to enable Operations Insights on the external pluggable database

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_PLUGGABLE_DATABASE_STACK_MONITORING_DETAILS_T Type

Details to enable Stack Monitoring on the external pluggable database.

Syntax
```

```

Fields

Field Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_ENABLE_PLUGGABLE_DATABASE_MANAGEMENT_DETAILS_T Type

Data to enable the Database Management service for the pluggable database.

Syntax
```

```

Fields

Field Description

`credential_details`

(required)

`private_end_point_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`service_name`

(required) The name of the Oracle Database service that will be used to connect to the database.

`protocol`

(optional) Protocol used by the database connection.

Allowed values are: 'TCP', 'TCPS'

`port`

(optional) The port used to connect to the pluggable database.

`ssl_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`role`

(optional) The role of the user that will be connecting to the pluggable database.

Allowed values are: 'SYSDBA', 'NORMAL'

### DBMS_CLOUD_OCI_DATABASE_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DATABASE_ESTIMATED_PATCHING_TIME_T Type

The estimated total time required in minutes for all patching operations (database server, storage server, and network switch patching).

Syntax
```

```

Fields

Field Description

`total_estimated_patching_time`

(optional) The estimated total time required in minutes for all patching operations.

`estimated_db_server_patching_time`

(optional) The estimated time required in minutes for database server patching.

`estimated_storage_server_patching_time`

(optional) The estimated time required in minutes for storage server patching.

`estimated_network_switches_patching_time`

(optional) The estimated time required in minutes for network switch patching.

### DBMS_CLOUD_OCI_DATABASE_EXADATA_DB_SYSTEM_MIGRATION_SUMMARY_T Type

Information about the Exadata DB system migration. The migration is used to move the Exadata Cloud Service instance from the DB system resource model to the new cloud Exadata infrastructure resource model.

Syntax
```

```

Fields

Field Description

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`cloud_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

### DBMS_CLOUD_OCI_DATABASE_EXADATA_DB_SYSTEM_MIGRATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_exadata_db_system_migration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_EXADATA_DB_SYSTEM_MIGRATION_T Type

Information about the Exadata DB system migration. The migration is used to move the Exadata Cloud Service instance from the DB system resource model to the new cloud Exadata infrastructure resource model.

Syntax
```

```

Fields

Field Description

`db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`cloud_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster.

`cloud_exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud Exadata infrastructure.

`additional_migrations`

(optional) The details of addtional resources related to the migration.

### DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_T Type

ExadataInfrastructure

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current lifecycle state of the Exadata infrastructure.

Allowed values are: 'CREATING', 'REQUIRES_ACTIVATION', 'ACTIVATING', 'ACTIVE', 'ACTIVATION_FAILED', 'FAILED', 'UPDATING', 'DELETING', 'DELETED', 'DISCONNECTED', 'MAINTENANCE_IN_PROGRESS', 'WAITING_FOR_CONNECTIVITY'

`display_name`

(required) The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.

`shape`

(required) The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.

`time_zone`

(optional) The time zone of the Exadata infrastructure. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`cpus_enabled`

(optional) The number of enabled CPU cores.

`max_cpu_count`

(optional) The total number of CPU cores available.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`max_memory_in_g_bs`

(optional) The total memory available in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`max_db_node_storage_in_g_bs`

(optional) The total local node storage available in GBs.

`data_storage_size_in_t_bs`

(optional) Size, in terabytes, of the DATA disk group.

`max_data_storage_in_t_bs`

(optional) The total available DATA disk group size.

`rack_serial_number`

(optional) The serial number for the Exadata infrastructure.

`storage_count`

(optional) The number of Exadata storage servers for the Exadata infrastructure.

`additional_storage_count`

(optional) The requested number of additional storage servers for the Exadata infrastructure.

`activated_storage_count`

(optional) The requested number of additional storage servers activated for the Exadata infrastructure.

`compute_count`

(optional) The number of compute servers for the Exadata infrastructure.

`is_multi_rack_deployment`

(optional) Indicates if deployment is Multi-Rack or not.

`multi_rack_configuration_file`

(optional) The base64 encoded Multi-Rack configuration json file.

`additional_compute_count`

(optional) The requested number of additional compute servers for the Exadata infrastructure.

`additional_compute_system_model`

(optional) Oracle Exadata System Model specification. The system model determines the amount of compute or storage server resources available for use. For more information, please see[System and Shape Configuration Options]](https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)

Allowed values are: 'X7', 'X8', 'X8M', 'X9M', 'X10M'

`cloud_control_plane_server1`

(optional) The IP address for the first control plane server.

`cloud_control_plane_server2`

(optional) The IP address for the second control plane server.

`netmask`

(optional) The netmask for the control plane network.

`gateway`

(optional) The gateway for the control plane network.

`admin_network_cidr`

(optional) The CIDR block for the Exadata administration network.

`infini_band_network_cidr`

(optional) The CIDR block for the Exadata InfiniBand interconnect.

`corporate_proxy`

(optional) The corporate network proxy for access to the control plane network.

`dns_server`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp_server`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`time_created`

(optional) The date and time the Exadata infrastructure was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`csi_number`

(optional) The CSI Number of the Exadata infrastructure.

`contacts`

(optional) The list of contacts for the Exadata infrastructure.

`maintenance_slo_status`

(optional) A field to capture ‘Maintenance SLO Status’ for the Exadata infrastructure with values ‘OK’, ‘DEGRADED’. Default is ‘OK’ when the infrastructure is provisioned.

Allowed values are: 'OK', 'DEGRADED'

`maintenance_window`

(optional)

`storage_server_version`

(optional) The software version of the storage servers (cells) in the Exadata infrastructure.

`db_server_version`

(optional) The software version of the database servers (dom0) in the Exadata infrastructure.

`monthly_db_server_version`

(optional) The monthly software version of the database servers (dom0) in the Exadata infrastructure.

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`is_cps_offline_report_enabled`

(optional) Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status themselves and fix problems on their end, saving time and frustration for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata infrastructure provisioning. You can also disable or enable it at any time using the UpdateExadatainfrastructure API.

`network_bonding_mode_details`

(optional)

`availability_domain`

(optional) The name of the availability domain that the Exadata infrastructure is located in.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_SUMMARY_T Type

Details of the Exadata Cloud@Customer infrastructure. Applies to Exadata Cloud@Customer instances only. See`CLOUD_EXADATA_INFRASTRUCTURE_SUMMARY`Function for details of the cloud Exadata infrastructure resource used by Exadata Cloud Service instances.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`lifecycle_state`

(required) The current lifecycle state of the Exadata infrastructure.

Allowed values are: 'CREATING', 'REQUIRES_ACTIVATION', 'ACTIVATING', 'ACTIVE', 'ACTIVATION_FAILED', 'FAILED', 'UPDATING', 'DELETING', 'DELETED', 'DISCONNECTED', 'MAINTENANCE_IN_PROGRESS', 'WAITING_FOR_CONNECTIVITY'

`display_name`

(required) The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.

`shape`

(required) The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.

`time_zone`

(optional) The time zone of the Exadata infrastructure. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`cpus_enabled`

(optional) The number of enabled CPU cores.

`max_cpu_count`

(optional) The total number of CPU cores available.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`max_memory_in_g_bs`

(optional) The total memory available in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`max_db_node_storage_in_g_bs`

(optional) The total local node storage available in GBs.

`data_storage_size_in_t_bs`

(optional) Size, in terabytes, of the DATA disk group.

`max_data_storage_in_t_bs`

(optional) The total available DATA disk group size.

`rack_serial_number`

(optional) The serial number for the Exadata infrastructure.

`storage_count`

(optional) The number of Exadata storage servers for the Exadata infrastructure.

`additional_storage_count`

(optional) The requested number of additional storage servers for the Exadata infrastructure.

`activated_storage_count`

(optional) The requested number of additional storage servers activated for the Exadata infrastructure.

`compute_count`

(optional) The number of compute servers for the Exadata infrastructure.

`is_multi_rack_deployment`

(optional) Indicates if deployment is Multi-Rack or not.

`multi_rack_configuration_file`

(optional) The base64 encoded Multi-Rack configuration json file.

`additional_compute_count`

(optional) The requested number of additional compute servers for the Exadata infrastructure.

`additional_compute_system_model`

(optional) Oracle Exadata System Model specification. The system model determines the amount of compute or storage server resources available for use. For more information, please see[System and Shape Configuration Options]](https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)

Allowed values are: 'X7', 'X8', 'X8M', 'X9M', 'X10M'

`cloud_control_plane_server1`

(optional) The IP address for the first control plane server.

`cloud_control_plane_server2`

(optional) The IP address for the second control plane server.

`netmask`

(optional) The netmask for the control plane network.

`gateway`

(optional) The gateway for the control plane network.

`admin_network_cidr`

(optional) The CIDR block for the Exadata administration network.

`infini_band_network_cidr`

(optional) The CIDR block for the Exadata InfiniBand interconnect.

`corporate_proxy`

(optional) The corporate network proxy for access to the control plane network.

`dns_server`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp_server`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`time_created`

(optional) The date and time the Exadata infrastructure was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`csi_number`

(optional) The CSI Number of the Exadata infrastructure.

`contacts`

(optional) The list of contacts for the Exadata infrastructure.

`maintenance_slo_status`

(optional) A field to capture ‘Maintenance SLO Status’ for the Exadata infrastructure with values ‘OK’, ‘DEGRADED’. Default is ‘OK’ when the infrastructure is provisioned.

Allowed values are: 'OK', 'DEGRADED'

`maintenance_window`

(optional)

`storage_server_version`

(optional) The software version of the storage servers (cells) in the Exadata infrastructure.

`db_server_version`

(optional) The software version of the database servers (dom0) in the Exadata infrastructure.

`monthly_db_server_version`

(optional) The monthly software version of the database servers (dom0) in the Exadata infrastructure.

`last_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last maintenance run.

`next_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the next maintenance run.

`is_cps_offline_report_enabled`

(optional) Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status themselves and fix problems on their end, saving time and frustration for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata infrastructure provisioning. You can also disable or enable it at any time using the UpdateExadatainfrastructure API.

`network_bonding_mode_details`

(optional)

`availability_domain`

(optional) The name of the availability domain that the Exadata infrastructure is located in.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_autonomous_vm_cluster_resource_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_UN_ALLOCATED_RESOURCES_T Type

Un allocated resources details of the Exadata Cloud@Customer infrastructure. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`display_name`

(required) The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.

`local_storage_in_gbs`

(optional) The minimum amount of un allocated storage that is available across all nodes in the infrastructure.

`ocpus`

(optional) The minimum amount of un allocated ocpus that is available across all nodes in the infrastructure.

`memory_in_g_bs`

(optional) The minimum amount of un allocated memory that is available across all nodes in the infrastructure.

`exadata_storage_in_t_bs`

(optional) Total unallocated exadata storage in the infrastructure in TBs.

`autonomous_vm_clusters`

(optional) The list of Autonomous VM Clusters on the Infra and their associated unallocated resources details

### DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_UPDATE_DETAIL_T Type

Details of the IORM configuration settings update request.

Syntax
```

```

Fields

Field Description

`db_name`

(optional) The database name. For the default `DbPlan`, the `dbName` is `default`.

`l_share`

(optional) The relative priority of this database.

### DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_UPDATE_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_database_db_iorm_config_update_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_EXADATA_IORM_CONFIG_UPDATE_DETAILS_T Type

IORM Setting details for this Exadata System to be updated

Syntax
```

```

Fields

Field Description

`objective`

(optional) Value for the IORM objective Default is \"Auto\"

Allowed values are: 'LOW_LATENCY', 'HIGH_THROUGHPUT', 'BALANCED', 'AUTO', 'BASIC'

`db_plans`

(optional) Array of IORM Setting for all the database in this Exadata DB System

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_BACKUP_JOB_T Type

Provides all the details that apply to an external backup job.

Syntax
```

```

Fields

Field Description

`backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated backup resource.

`provisioning`

(required) An indicator for the provisioning state of the resource. If `TRUE`, the resource is still being provisioned.

`swift_path`

(required) The Swift path to use as a destination for the standalone backup.

`bucket_name`

(required) The name of the Swift compartment bucket where the backup should be stored.

`tag`

(required) The tag for RMAN to apply to the backup.

`user_name`

(required) The Swift user name to use for transferring the standalone backup to the designated Swift compartment bucket.

`swift_password`

(optional) The auth token to use for access to the Swift compartment bucket that will store the standalone backup. For information about auth tokens, see[Working with Auth Tokens](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#two).

### DBMS_CLOUD_OCI_DATABASE_STACK_MONITORING_CONFIG_T Type

The configuration of Stack Monitoring for the external database.

Syntax
```

```

Fields

Field Description

`stack_monitoring_status`

(required) The status of Stack Monitoring.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`stack_monitoring_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_CONTAINER_DATABASE_T Type

An Oracle Cloud Infrastructure resource that allows you to manage an external container database.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_CONTAINER_DATABASE_SUMMARY_T Type

An Oracle Cloud Infrastructure resource that allows you to manage an external Oracle container database.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_DATABASE_BASE_T Type

A resource that allows you to manage an Oracle Database located outside of Oracle Cloud using Oracle Cloud Infrastructure's Console and APIs.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_DATABASE_CONNECTOR_T Type

An Oracle Cloud Infrastructure resource used to connect to an external Oracle Database. This resource stores the database connection string, user credentials, and related details that allow you to manage your external database using the Oracle Cloud Infrastructure Console and API interfaces.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

`lifecycle_state`

(required) The current lifecycle state of the external database connector resource.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external connector was created.

`connector_type`

(required) The type of connector used by the external database resource.

Allowed values are: 'MACS'

`external_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database resource.

`connection_status`

(required) The status of connectivity to the external database.

`time_connection_status_last_updated`

(required) The date and time the connectionStatus of this external connector was last updated.

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_DATABASE_CONNECTOR_SUMMARY_T Type

An Oracle Cloud Infrastructure resource used to connect to an external Oracle Database. This resource stores the database connection string, user credentials, and related details that allow you to manage your external database using the Oracle Cloud Infrastructure Console and API interfaces.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

`lifecycle_state`

(required) The current lifecycle state of the external database connector resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_created`

(required) The date and time the external connector was created.

`connector_type`

(required) The type of connector used by the external database resource.

Allowed values are: 'MACS'

`external_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database resource.

`connection_status`

(required) The status of connectivity to the external database.

`time_connection_status_last_updated`

(required) The date and time the `connectionStatus` of this external connector was last updated.

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_MACS_CONNECTOR_T Type

An Oracle Cloud Infrastructure resource that uses the[Management Agent cloud service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html)to connect to an external Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_external_macs_connector_t`is a subtype of the`dbms_cloud_oci_database_external_database_connector_t`type.

Fields

Field Description

`connection_string`

(required)

`connection_credentials`

(required)

`connector_agent_id`

(required) The ID of the agent used for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_MACS_CONNECTOR_SUMMARY_T Type

An Oracle Cloud Infrastructure resource that uses the[Management Agent cloud service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html)to connect to an external Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_external_macs_connector_summary_t`is a subtype of the`dbms_cloud_oci_database_external_database_connector_summary_t`type.

Fields

Field Description

`connection_string`

(required)

`connection_credentials`

(required)

`connector_agent_id`

(required) The ID of the agent used for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_OPERATIONS_INSIGHTS_CONFIG_T Type

The configuration of Operations Insights for the external database

Syntax
```

```

Fields

Field Description

`operations_insights_status`

(required) The status of Operations Insights

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'NOT_ENABLED', 'FAILED_ENABLING', 'FAILED_DISABLING'

`operations_insights_connector_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function.

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_NON_CONTAINER_DATABASE_T Type

an external Oracle non-container database.

Syntax
```

```

Fields

Field Description

`operations_insights_config`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_NON_CONTAINER_DATABASE_SUMMARY_T Type

An Oracle Cloud Infrastructure external non-container database resource. This resource is used to manage a non-container database located outside of Oracle Cloud.

Syntax
```

```

Fields

Field Description

`operations_insights_config`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_PLUGGABLE_DATABASE_T Type

an external Oracle pluggable database.

Syntax
```

```

Fields

Field Description

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the the non-container database that was converted to a pluggable database to create this resource.

`external_container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function that contains the specified`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource.

`operations_insights_config`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_EXTERNAL_PLUGGABLE_DATABASE_SUMMARY_T Type

An Oracle Cloud Infrastructure resource that allows you to manage an external pluggable database.

Syntax
```

```

Fields

Field Description

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the the non-container database that was converted to a pluggable database to create this resource.

`external_container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function that contains the specified`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource.

`operations_insights_config`

(optional)

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure external database resource.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`lifecycle_state`

(required) The current state of the Oracle Cloud Infrastructure external database resource.

Allowed values are: 'PROVISIONING', 'NOT_CONNECTED', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED'

`time_created`

(required) The date and time the database was created.

`db_unique_name`

(optional) The `DB_UNIQUE_NAME` of the external database.

`db_id`

(optional) The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.

`database_version`

(optional) The Oracle Database version.

`database_edition`

(optional) The Oracle Database edition.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`time_zone`

(optional) The time zone of the external database. It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name, depending on how the time zone value was specified when the database was created / last altered.

`character_set`

(optional) The character set of the external database.

`ncharacter_set`

(optional) The national character of the external database.

`db_packs`

(optional) The database packs licensed for the external Oracle Database.

`database_configuration`

(optional) The Oracle Database configuration

Allowed values are: 'RAC', 'SINGLE_INSTANCE'

`database_management_config`

(optional)

`stack_monitoring_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_FAILOVER_DATA_GUARD_ASSOCIATION_DETAILS_T Type

The Data Guard association failover parameters.

Syntax
```

```

Fields

Field Description

`database_admin_password`

(required) The DB system administrator password.

### DBMS_CLOUD_OCI_DATABASE_FLEX_COMPONENT_SUMMARY_T Type

The Flex Components for a DB system. The Flex Component determines resources to allocate to the DB system - CPU cores, memory and storage for Flex shapes. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the Flex Component used for the DB system.

`minimum_core_count`

(optional) The minimum number of CPU cores that can be enabled on the DB Server for this Flex Component.

`available_core_count`

(optional) The maximum number of CPU cores that can ben enabled on the DB Server for this Flex Component.

`available_db_storage_in_g_bs`

(optional) The maximum storage that can be enabled on the Storage Server for this Flex Component.

### DBMS_CLOUD_OCI_DATABASE_FLEX_COMPONENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_flex_component_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_FLEX_COMPONENT_COLLECTION_T Type

Results of a FlexComponent lists. Contains FlexComponentSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required)

### DBMS_CLOUD_OCI_DATABASE_GENERATE_AUTONOMOUS_DATABASE_WALLET_DETAILS_T Type

Details to create and download an Oracle Autonomous Database wallet.

Syntax
```

```

Fields

Field Description

`generate_type`

(optional) The type of wallet to generate. **Serverless instance usage:** * `SINGLE` - used to generate a wallet for a single database * `ALL` - used to generate wallet for all databases in the region **Dedicated Exadata infrastructure usage:** Value must be `NULL` if attribute is used.

Allowed values are: 'ALL', 'SINGLE'

`password`

(required) The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.

`is_regional`

(optional) True when requesting regional connection strings in PDB connect info, applicable to cross-region DG only.

### DBMS_CLOUD_OCI_DATABASE_INFO_FOR_NETWORK_GEN_DETAILS_T Type

Parameters for generation of the client or backup network in a VM cluster network in an Exadata Cloud@Customer system.

Syntax
```

```

Fields

Field Description

`network_type`

(required) The network type.

Allowed values are: 'CLIENT', 'BACKUP', 'DISASTER_RECOVERY'

`vlan_id`

(required) The network VLAN ID.

`cidr`

(required) The cidr for the network.

`gateway`

(required) The network gateway.

`netmask`

(required) The network netmask.

`domain`

(required) The network domain name.

`prefix`

(required) The network domain name.

### DBMS_CLOUD_OCI_DATABASE_INFO_FOR_NETWORK_GEN_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_info_for_network_gen_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_GENERATE_RECOMMENDED_NETWORK_DETAILS_T Type

Generates a recommended VM cluster network configuration for an Exadata Cloud@Customer system. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the VM cluster network. The name does not need to be unique.

`db_servers`

(optional) The list of Db server Ids to configure network.

`scan_listener_port_tcp`

(optional) The SCAN TCPIP port. Default is 1521.

`scan_listener_port_tcp_ssl`

(optional) The SCAN TCPIP SSL port. Default is 2484.

`dr_scan_listener_port_tcp`

(optional) The DR SCAN TCPIP port. Default is 1521.

`networks`

(required) List of parameters for generation of the client and backup networks.

`dns`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_GI_VERSION_SUMMARY_T Type

The Oracle Grid Infrastructure (GI) version. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`version`

(required) A valid Oracle Grid Infrastructure (GI) software version.

### DBMS_CLOUD_OCI_DATABASE_INFRASTRUCTURE_TARGET_VERSION_T Type

Infrastructure target version details.

Syntax
```

```

Fields

Field Description

`target_db_version_history_entry`

(required) The history entry of the target system software version for the database server patching operation.

`target_storage_version_history_entry`

(required) The history entry of the target storage cell system software version for the storage cell patching operation.

`target_resource_type`

(optional) The resource type of the target Exadata infrastructure resource that will receive the system software update.

Allowed values are: 'EXADATA_DB_SYSTEM', 'CLOUD_EXADATA_INFRASTRUCTURE', 'EXACC_INFRASTRUCTURE'

`target_resource_id`

(optional) The OCID of the target Exadata Infrastructure resource that will receive the maintenance update.

### DBMS_CLOUD_OCI_DATABASE_INFRASTRUCTURE_TARGET_VERSION_SUMMARY_T Type

The target Exadata Infrastructure system software version for an infrastructure resource. Applies to Exadata Cloud@Customer and Exadata Cloud instances only. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`target_db_version_history_entry`

(required) The history entry of the target system software version for the database server patching operation.

`target_storage_version_history_entry`

(required) The history entry of the target storage cell system software version for the storage cell patching operation.

`target_resource_type`

(optional) The resource type of the target Exadata infrastructure resource that will receive the system software update.

Allowed values are: 'EXADATA_DB_SYSTEM', 'CLOUD_EXADATA_INFRASTRUCTURE', 'EXACC_INFRASTRUCTURE'

`target_resource_id`

(optional) The OCID of the target Exadata Infrastructure resource that will receive the maintenance update.

### DBMS_CLOUD_OCI_DATABASE_KEY_STORE_ASSOCIATED_DATABASE_DETAILS_T Type

The databases associated with a key store

Syntax
```

```

Fields

Field Description

`id`

(optional) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`db_name`

(optional) The name of the database that is associated with the key store.

### DBMS_CLOUD_OCI_DATABASE_KEY_STORE_ASSOCIATED_DATABASE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_key_store_associated_database_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_KEY_STORE_T Type

A key store to connect to an on-premise encryption key appliance like Oracle Key Vault.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the key store. The name does not need to be unique.

`time_created`

(optional) The date and time that the key store was created.

`lifecycle_state`

(required) The current state of the key store.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`type_details`

(required)

`associated_databases`

(optional) List of databases associated with the key store.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_KEY_STORE_SUMMARY_T Type

Details of the Key Store.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the key store. The name does not need to be unique.

`time_created`

(optional) The date and time that the key store was created.

`lifecycle_state`

(required) The current state of the key store.

Allowed values are: 'ACTIVE', 'DELETED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`type_details`

(required)

`associated_databases`

(optional) List of databases associated with the key store.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_KEY_STORE_TYPE_FROM_ORACLE_KEY_VAULT_DETAILS_T Type

Details for Oracle Key Vault

Syntax
```

```

`dbms_cloud_oci_database_key_store_type_from_oracle_key_vault_details_t`is a subtype of the`dbms_cloud_oci_database_key_store_type_details_t`type.

Fields

Field Description

`connection_ips`

(required) The list of Oracle Key Vault connection IP addresses.

`admin_username`

(required) The administrator username to connect to Oracle Key Vault

`vault_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

### DBMS_CLOUD_OCI_DATABASE_LAUNCH_AUTONOMOUS_EXADATA_INFRASTRUCTURE_DETAILS_T Type

Describes the input parameters to launch a new Autonomous Exadata Infrastructure.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment the Autonomous Exadata Infrastructure belongs in.

`display_name`

(optional) The user-friendly name for the Autonomous Exadata Infrastructure. It does not have to be unique.

`availability_domain`

(required) The availability domain where the Autonomous Exadata Infrastructure is located.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the Autonomous Exadata Infrastructure is associated with. **Subnet Restrictions:** - For Autonomous Exadata Infrastructures, do not use a subnet that overlaps with 192.168.128.0/20 These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`shape`

(required) The shape of the Autonomous Exadata Infrastructure. The shape determines resources allocated to the Autonomous Exadata Infrastructure (CPU cores, memory and storage). To get a list of shapes, use the ListDbSystemShapes operation.

`domain`

(optional) A domain name used for the Autonomous Exadata Infrastructure. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.

`license_model`

(optional) The Oracle license model that applies to all the databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`maintenance_window_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_BASE_T Type

Parameters for provisioning a bare metal, virtual machine, or Exadata DB system. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment the DB system belongs in.

`fault_domains`

(optional) A Fault Domain is a grouping of hardware and infrastructure within an availability domain. Fault Domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or maintenance that affects one Fault Domain does not affect DB systems in other Fault Domains. If you do not specify the Fault Domain, the system selects one for you. To change the Fault Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain. If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into. The system assigns your nodes automatically to the Fault Domains you specify so that no Fault Domain contains more than one node. To get a list of Fault Domains, use the`LIST_FAULT_DOMAINS`Function operation in the Identity and Access Management Service API. Example: `FAULT-DOMAIN-1`

`display_name`

(optional) The user-friendly name for the DB system. The name does not have to be unique.

`availability_domain`

(required) The availability domain where the DB system is located.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the DB system is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.

`backup_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems. **Subnet Restrictions:** See the subnet restrictions information for **subnetId**.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`shape`

(required) The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage To get a list of shapes, use the`LIST_DB_SYSTEM_SHAPES`Function operation.

`time_zone`

(optional) The time zone to use for the DB system. For details, see[DB System Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`db_system_options`

(optional)

`storage_volume_performance_mode`

(optional) The block storage volume performance level. Valid values are `BALANCED` and `HIGH_PERFORMANCE`. See[Block Volume Performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm)for more information.

Allowed values are: 'BALANCED', 'HIGH_PERFORMANCE'

`sparse_diskgroup`

(optional) If true, Sparse Diskgroup is configured for Exadata dbsystem. If False, Sparse diskgroup is not configured.

`ssh_public_keys`

(required) The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.

`hostname`

(required) The hostname for the DB system. The hostname must begin with an alphabetic character, and can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata DB systems. The maximum length of the combined hostname and domain is 63 characters. **Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.

`domain`

(optional) A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.

`cpu_core_count`

(required) The number of CPU cores to enable for a bare metal or Exadata DB system or AMD VMDB Systems. The valid values depend on the specified shape: - BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368. - VM.Standard.E4.Flex - Specify any thing from 1 to 64. This parameter is not used for INTEL virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see[Virtual Machine DB Systems](https://docs.oracle.com/iaas/Content/Database/Concepts/overview.htm#virtualmachine)

`cluster_name`

(optional) The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`data_storage_percentage`

(optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.

`initial_data_storage_size_in_gb`

(optional) Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.

`kms_key_id`

(optional) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`node_count`

(optional) The number of nodes to launch for a 2-node RAC virtual machine DB system. Specify either 1 or 2.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`source`

(optional) The source of the database: Use `NONE` for creating a new database. Use `DB_BACKUP` for creating a new database by restoring from a backup. Use `DATABASE` for creating a new database from an existing database, including archive redo log data. The default is `NONE`.

Allowed values are: 'NONE', 'DB_BACKUP', 'DATABASE', 'DB_SYSTEM'

`private_ip`

(optional) A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_DETAILS_T Type

Used for creating a new DB system. Does not use backups or an existing database for the creation of the initial database.

Syntax
```

```

`dbms_cloud_oci_database_launch_db_system_details_t`is a subtype of the`dbms_cloud_oci_database_launch_db_system_base_t`type.

Fields

Field Description

`db_home`

(required)

`database_edition`

(required) The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`disk_redundancy`

(optional) The type of redundancy configured for the DB system. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.

Allowed values are: 'HIGH', 'NORMAL'

`license_model`

(optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`maintenance_window_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_FROM_BACKUP_DETAILS_T Type

Used for creating a new DB system from a database backup.

Syntax
```

```

`dbms_cloud_oci_database_launch_db_system_from_backup_details_t`is a subtype of the`dbms_cloud_oci_database_launch_db_system_base_t`type.

Fields

Field Description

`db_home`

(required)

`database_edition`

(required) The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`disk_redundancy`

(optional) The type of redundancy configured for the DB system. NORMAL 2-way redundancy, recommended for test and development systems. HIGH is 3-way redundancy, recommended for production systems.

Allowed values are: 'HIGH', 'NORMAL'

`license_model`

(optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_FROM_DATABASE_DETAILS_T Type

Used for creating a new DB system from a database, including archived redo log data.

Syntax
```

```

`dbms_cloud_oci_database_launch_db_system_from_database_details_t`is a subtype of the`dbms_cloud_oci_database_launch_db_system_base_t`type.

Fields

Field Description

`db_home`

(required)

`database_edition`

(required) The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

Allowed values are: 'STANDARD_EDITION', 'ENTERPRISE_EDITION', 'ENTERPRISE_EDITION_HIGH_PERFORMANCE', 'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'

`disk_redundancy`

(optional) The type of redundancy configured for the DB system. NORMAL 2-way redundancy, recommended for test and development systems. HIGH is 3-way redundancy, recommended for production systems.

Allowed values are: 'HIGH', 'NORMAL'

`license_model`

(optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_FROM_DB_SYSTEM_DETAILS_T Type

Used for creating a new database system by cloning an existing DB system.

Syntax
```

```

`dbms_cloud_oci_database_launch_db_system_from_db_system_details_t`is a subtype of the`dbms_cloud_oci_database_launch_db_system_base_t`type.

Fields

Field Description

`source_db_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DB system.

`db_home`

(required)

`license_model`

(optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

### DBMS_CLOUD_OCI_DATABASE_LOCAL_CLONE_PLUGGABLE_DATABASE_DETAILS_T Type

**Deprecated.** Use`CREATE_PLUGGABLE_DATABASE_DETAILS`Function for Pluggable Database LocalClone Operation. Parameters for cloning a pluggable database (PDB) within the same database (CDB). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`cloned_pdb_name`

(required) The name for the pluggable database (PDB). The name is unique in the context of a`DATABASE`Type. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.

`pdb_admin_password`

(optional) A strong password for PDB Admin of the newly cloned PDB. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`target_tde_wallet_password`

(optional) The existing TDE wallet password of the target CDB.

`should_pdb_admin_account_be_locked`

(optional) The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it. If true, the pluggable database will be locked and user cannot login to it.

### DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_T Type

Details of a maintenance run.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the maintenance run.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-friendly name for the maintenance run.

`description`

(optional) Description of the maintenance run.

`lifecycle_state`

(required) The current state of the maintenance run. For Autonomous Database Serverless instances, valid states are IN_PROGRESS, SUCCEEDED, and FAILED.

Allowed values are: 'SCHEDULED', 'IN_PROGRESS', 'SUCCEEDED', 'SKIPPED', 'FAILED', 'UPDATING', 'DELETING', 'DELETED', 'CANCELED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_scheduled`

(required) The date and time the maintenance run is scheduled to occur.

`time_started`

(optional) The date and time the maintenance run starts.

`time_ended`

(optional) The date and time the maintenance run was completed.

`target_resource_type`

(optional) The type of the target resource on which the maintenance run occurs.

Allowed values are: 'AUTONOMOUS_EXADATA_INFRASTRUCTURE', 'AUTONOMOUS_CONTAINER_DATABASE', 'EXADATA_DB_SYSTEM', 'CLOUD_EXADATA_INFRASTRUCTURE', 'EXACC_INFRASTRUCTURE', 'AUTONOMOUS_VM_CLUSTER', 'AUTONOMOUS_DATABASE', 'CLOUD_AUTONOMOUS_VM_CLUSTER'

`target_resource_id`

(optional) The ID of the target resource on which the maintenance run occurs.

`maintenance_type`

(optional) Maintenance type.

Allowed values are: 'PLANNED', 'UNPLANNED'

`patch_id`

(optional) The unique identifier of the patch. The identifier string includes the patch type, the Oracle Database version, and the patch creation date (using the format YYMMDD). For example, the identifier `ru_patch_19.9.0.0_201030` is used for an RU patch for Oracle Database 19.9.0.0 that was released October 30, 2020.

`maintenance_subtype`

(optional) Maintenance sub-type.

Allowed values are: 'QUARTERLY', 'HARDWARE', 'CRITICAL', 'INFRASTRUCTURE', 'DATABASE', 'ONEOFF', 'SECURITY_MONTHLY', 'TIMEZONE'

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`peer_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance run for the Autonomous Data Guard association's peer container database.

`patching_mode`

(optional) Cloud Exadata infrastructure node patching method, either \"ROLLING\" or \"NONROLLING\". Default value is ROLLING. *IMPORTANT*: Non-rolling infrastructure patching involves system down time. See[Oracle-Managed Infrastructure Maintenance Updates](https://docs.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle)for more information.

Allowed values are: 'ROLLING', 'NONROLLING'

`patch_failure_count`

(optional) Contain the patch failure count.

`target_db_server_version`

(optional) The target software version for the database server patching operation.

`target_storage_server_version`

(optional) The target Cell version that is to be patched to.

`is_custom_action_timeout_enabled`

(optional) If true, enables the configuration of a custom action timeout (waiting period) between database servers patching operations.

`custom_action_timeout_in_mins`

(optional) Determines the amount of time the system will wait before the start of each database server patching operation. Specify a number of minutes, from 15 to 120.

`current_custom_action_timeout_in_mins`

(optional) Extend current custom action timeout between the current database servers during waiting state, from 0 (zero) to 30 minutes.

`patching_status`

(optional) The status of the patching operation.

Allowed values are: 'PATCHING', 'WAITING', 'SCHEDULED'

`patching_start_time`

(optional) The time when the patching operation started.

`patching_end_time`

(optional) The time when the patching operation ended.

`estimated_patching_time`

(optional)

`current_patching_component`

(optional) The name of the current infrastruture component that is getting patched.

`estimated_component_patching_start_time`

(optional) The estimated start time of the next infrastruture component patching operation.

### DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_SUMMARY_T Type

Details of a maintenance run.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the maintenance run.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-friendly name for the maintenance run.

`description`

(optional) Description of the maintenance run.

`lifecycle_state`

(required) The current state of the maintenance run. For Autonomous Database Serverless instances, valid states are IN_PROGRESS, SUCCEEDED, and FAILED.

Allowed values are: 'SCHEDULED', 'IN_PROGRESS', 'SUCCEEDED', 'SKIPPED', 'FAILED', 'UPDATING', 'DELETING', 'DELETED', 'CANCELED'

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_scheduled`

(required) The date and time the maintenance run is scheduled to occur.

`time_started`

(optional) The date and time the maintenance run starts.

`time_ended`

(optional) The date and time the maintenance run was completed.

`target_resource_type`

(optional) The type of the target resource on which the maintenance run occurs.

Allowed values are: 'AUTONOMOUS_EXADATA_INFRASTRUCTURE', 'AUTONOMOUS_CONTAINER_DATABASE', 'EXADATA_DB_SYSTEM', 'CLOUD_EXADATA_INFRASTRUCTURE', 'EXACC_INFRASTRUCTURE', 'AUTONOMOUS_VM_CLUSTER', 'AUTONOMOUS_DATABASE', 'CLOUD_AUTONOMOUS_VM_CLUSTER'

`target_resource_id`

(optional) The ID of the target resource on which the maintenance run occurs.

`maintenance_type`

(optional) Maintenance type.

Allowed values are: 'PLANNED', 'UNPLANNED'

`patch_id`

(optional) The unique identifier of the patch. The identifier string includes the patch type, the Oracle Database version, and the patch creation date (using the format YYMMDD). For example, the identifier `ru_patch_19.9.0.0_201030` is used for an RU patch for Oracle Database 19.9.0.0 that was released October 30, 2020.

`maintenance_subtype`

(optional) Maintenance sub-type.

Allowed values are: 'QUARTERLY', 'HARDWARE', 'CRITICAL', 'INFRASTRUCTURE', 'DATABASE', 'ONEOFF', 'SECURITY_MONTHLY', 'TIMEZONE'

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`peer_maintenance_run_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance run for the Autonomous Data Guard association's peer container database.

`patching_mode`

(optional) Cloud Exadata infrastructure node patching method, either \"ROLLING\" or \"NONROLLING\". Default value is ROLLING. *IMPORTANT*: Non-rolling infrastructure patching involves system down time. See[Oracle-Managed Infrastructure Maintenance Updates](https://docs.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle)for more information.

Allowed values are: 'ROLLING', 'NONROLLING'

`patch_failure_count`

(optional) Contain the patch failure count.

`target_db_server_version`

(optional) The target software version for the database server patching operation.

`target_storage_server_version`

(optional) The target Cell version that is to be patched to.

`is_custom_action_timeout_enabled`

(optional) If true, enables the configuration of a custom action timeout (waiting period) between database servers patching operations.

`custom_action_timeout_in_mins`

(optional) Determines the amount of time the system will wait before the start of each database server patching operation. Specify a number of minutes, from 15 to 120.

`current_custom_action_timeout_in_mins`

(optional) Extend current custom action timeout between the current database servers during waiting state, from 0 (zero) to 30 minutes.

`patching_status`

(optional) The status of the patching operation.

Allowed values are: 'PATCHING', 'WAITING', 'SCHEDULED'

`patching_start_time`

(optional) The time when the patching operation started.

`patching_end_time`

(optional) The time when the patching operation ended.

`estimated_patching_time`

(optional)

`current_patching_component`

(optional) The name of the current infrastruture component that is getting patched.

`estimated_component_patching_start_time`

(optional) The estimated start time of the next infrastruture component patching operation.

### DBMS_CLOUD_OCI_DATABASE_DB_SERVER_HISTORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_db_server_history_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_HISTORY_T Type

Details of a maintenance run history.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the maintenance run history.

`maintenance_run_details`

(optional)

`db_servers_history_details`

(optional) List of database server history details.

### DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_HISTORY_SUMMARY_T Type

Details of a maintenance run history.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the maintenance run history.

`maintenance_run_details`

(optional)

`db_servers_history_details`

(optional) List of database server history details.

### DBMS_CLOUD_OCI_DATABASE_MIGRATE_VAULT_KEY_DETAILS_T Type

Details for replacing existing Oracle-managed keys with customer-managed[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)keys and vice-versa is not supported.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(required) The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`kms_key_version_id`

(optional) The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.

`vault_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`tde_wallet_password`

(optional) The existing TDE wallet password of the database.

`admin_password`

(optional) The existing admin password of the database.

### DBMS_CLOUD_OCI_DATABASE_MODIFY_DATABASE_MANAGEMENT_DETAILS_T Type

Data to update one or more attributes of the Database Management configuration for the database.

Syntax
```

```

Fields

Field Description

`credential_details`

(optional)

`private_end_point_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`management_type`

(optional) The Database Management type.

Allowed values are: 'BASIC', 'ADVANCED'

`service_name`

(optional) The name of the Oracle Database service that will be used to connect to the database.

`protocol`

(optional) Protocol used by the database connection.

Allowed values are: 'TCP', 'TCPS'

`port`

(optional) The port used to connect to the database.

`ssl_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`role`

(optional) The role of the user that will be connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

### DBMS_CLOUD_OCI_DATABASE_MODIFY_PLUGGABLE_DATABASE_MANAGEMENT_DETAILS_T Type

Data to update one or more attributes of the Database Management configuration for the pluggable database.

Syntax
```

```

Fields

Field Description

`credential_details`

(optional)

`private_end_point_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`service_name`

(optional) The name of the Oracle Database service that will be used to connect to the database.

`protocol`

(optional) Protocol used by the database connection.

Allowed values are: 'TCP', 'TCPS'

`port`

(optional) The port used to connect to the database.

`ssl_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`role`

(optional) The role of the user that will be connecting to the database.

Allowed values are: 'SYSDBA', 'NORMAL'

### DBMS_CLOUD_OCI_DATABASE_NODE_DETAILS_T Type

Node details associated with a network.

Syntax
```

```

Fields

Field Description

`hostname`

(required) The node host name.

`ip`

(required) The node IP address.

`vip_hostname`

(optional) The node virtual IP (VIP) host name.

`vip`

(optional) The node virtual IP (VIP) address.

`lifecycle_state`

(optional) The current state of the VM cluster network nodes. CREATING - The resource is being created REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated. VALIDATING - The resource is being validated and not available to use. VALIDATED - The resource is validated and is available for consumption by VM cluster. VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected. UPDATING - The resource is being updated and not available to use. ALLOCATED - The resource is currently being used by VM cluster. TERMINATING - The resource is being deleted and not available to use. TERMINATED - The resource is deleted and unavailable. FAILED - The resource is in a failed state due to validation or other errors.

Allowed values are: 'CREATING', 'REQUIRES_VALIDATION', 'VALIDATING', 'VALIDATED', 'VALIDATION_FAILED', 'UPDATING', 'ALLOCATED', 'TERMINATING', 'TERMINATED', 'FAILED'

`db_server_id`

(optional) The Db server associated with the node.

### DBMS_CLOUD_OCI_DATABASE_WORKLOAD_TYPE_T Type

The number of consumed OCPUs, by database workload type.

Syntax
```

```

Fields

Field Description

`atp`

(optional) The total number of OCPU cores in use for Autonomous Transaction Processing databases in the infrastructure instance.

`adw`

(optional) The total number of OCPU cores in use for Autonomous Data Warehouse databases in the infrastructure instance.

### DBMS_CLOUD_OCI_DATABASE_OCP_US_T Type

The details of the available and consumed CPU cores of the Autonomous Exadata Infrastructure instance, including consumption by database workload type.

Syntax
```

```

Fields

Field Description

`total_cpu`

(optional) The total number of OCPUs in the Autonomous Exadata Infrastructure instance.

`consumed_cpu`

(optional) The total number of consumed OCPUs in the Autonomous Exadata Infrastructure instance.

`by_workload_type`

(optional)

### DBMS_CLOUD_OCI_DATABASE_ONEOFF_PATCH_T Type

One-off patches are created by specifying a database version, releaseUpdate and one-off patch number.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the one-off patch.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) One-off patch name.

`db_version`

(required) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`release_update`

(required) The PSU or PBP or Release Updates. To get a list of supported versions, use the`LIST_DB_VERSIONS`Function operation.

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`size_in_k_bs`

(optional) The size of one-off patch in kilobytes.

`lifecycle_state`

(required) The current state of the one-off patch.

Allowed values are: 'CREATING', 'AVAILABLE', 'UPDATING', 'INACTIVE', 'FAILED', 'EXPIRED', 'DELETING', 'DELETED', 'TERMINATING', 'TERMINATED'

`lifecycle_details`

(optional) Detailed message for the lifecycle state.

`sha256_sum`

(optional) SHA-256 checksum of the one-off patch.

`time_updated`

(optional) The date and time one-off patch was updated.

`time_created`

(required) The date and time one-off patch was created.

`time_of_expiration`

(optional) The date and time until which the one-off patch will be available for download.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_ONEOFF_PATCH_SUMMARY_T Type

An Oracle one-off patch for a specified database version. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the one-off patch.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) One-off patch name.

`db_version`

(required) A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`release_update`

(required) The PSU or PBP or Release Updates. To get a list of supported versions, use the`LIST_DB_VERSIONS`Function operation.

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`size_in_k_bs`

(optional) The size of one-off patch in kilobytes.

`lifecycle_state`

(required) The current state of the one-off patch.

Allowed values are: 'CREATING', 'AVAILABLE', 'UPDATING', 'INACTIVE', 'FAILED', 'EXPIRED', 'DELETING', 'DELETED', 'TERMINATING', 'TERMINATED'

`lifecycle_details`

(optional) Detailed message for the lifecycle state.

`sha256_sum`

(optional) SHA-256 checksum of the one-off patch.

`time_updated`

(optional) The date and time one-off patch was updated.

`time_created`

(required) The date and time one-off patch was created.

`time_of_expiration`

(optional) The date and time until which the one-off patch will be available for download.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_PATCH_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`description`

(required) The text describing this patch package.

`last_action`

(optional) Action that is currently being performed or was completed last.

Allowed values are: 'APPLY', 'PRECHECK'

`available_actions`

(optional) Actions that can possibly be performed using this patch.

Allowed values are: 'APPLY', 'PRECHECK'

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically can contain additional displayable text.

`lifecycle_state`

(optional) The current state of the patch as a result of lastAction.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time that the patch was released.

`version`

(required) The version of this patch package.

### DBMS_CLOUD_OCI_DATABASE_PATCH_DETAILS_T Type

The details about what actions to perform and using what patch to the specified target. This is part of an update request that is applied to a version field on the target such as DB system, Database Home, etc.

Syntax
```

```

Fields

Field Description

`patch_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`database_software_image_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database software image.

`action`

(optional) The action to perform on the patch.

Allowed values are: 'APPLY', 'PRECHECK'

### DBMS_CLOUD_OCI_DATABASE_PATCH_HISTORY_ENTRY_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch history entry.

`patch_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`action`

(optional) The action being performed or was completed.

Allowed values are: 'APPLY', 'PRECHECK'

`lifecycle_state`

(required) The current state of the action.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically contains additional displayable text.

`time_started`

(required) The date and time when the patch action started.

`time_ended`

(optional) The date and time when the patch action completed

`patch_type`

(optional) The type of Patch operation.

Allowed values are: 'OS', 'DB', 'GI'

### DBMS_CLOUD_OCI_DATABASE_PATCH_HISTORY_ENTRY_SUMMARY_T Type

The record of a patch action on a specified target.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch history entry.

`patch_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`action`

(optional) The action being performed or was completed.

Allowed values are: 'APPLY', 'PRECHECK'

`lifecycle_state`

(required) The current state of the action.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically contains additional displayable text.

`time_started`

(required) The date and time when the patch action started.

`time_ended`

(optional) The date and time when the patch action completed

`patch_type`

(optional) The type of Patch operation.

Allowed values are: 'OS', 'DB', 'GI'

### DBMS_CLOUD_OCI_DATABASE_PATCH_SUMMARY_T Type

A Patch for a DB system or DB Home. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`description`

(required) The text describing this patch package.

`last_action`

(optional) Action that is currently being performed or was completed last.

Allowed values are: 'APPLY', 'PRECHECK'

`available_actions`

(optional) Actions that can possibly be performed using this patch.

Allowed values are: 'APPLY', 'PRECHECK'

`lifecycle_details`

(optional) A descriptive text associated with the lifecycleState. Typically can contain additional displayable text.

`lifecycle_state`

(optional) The current state of the patch as a result of lastAction.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time that the patch was released.

`version`

(required) The version of this patch package.

### DBMS_CLOUD_OCI_DATABASE_PDB_CONVERSION_HISTORY_ENTRY_T Type

Details of operations performed to convert a non-container database to pluggable database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database conversion history.

`action`

(required) The operations used to convert a non-container database to a pluggable database. - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database. - Use `CONVERT` to convert a non-container database into a pluggable database. - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API. - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.

Allowed values are: 'PRECHECK', 'CONVERT', 'SYNC', 'SYNC_ROLLBACK'

`target`

(optional) The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database. - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.

Allowed values are: 'NEW_DATABASE'

`source_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`target_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`cdb_name`

(required) The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.

`lifecycle_state`

(required) Status of an operation performed during the conversion of a non-container database to a pluggable database.

Allowed values are: 'SUCCEEDED', 'FAILED', 'IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state for the conversion operation.

`time_started`

(required) The date and time when the database conversion operation started.

`time_ended`

(optional) The date and time when the database conversion operation ended.

`additional_cdb_params`

(optional) Additional container database parameter.

### DBMS_CLOUD_OCI_DATABASE_PDB_CONVERSION_HISTORY_ENTRY_SUMMARY_T Type

Details of operations performed to convert a non-container database to pluggable database.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database conversion history.

`action`

(required) The operations used to convert a non-container database to a pluggable database. - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database. - Use `CONVERT` to convert a non-container database into a pluggable database. - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API. - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.

Allowed values are: 'PRECHECK', 'CONVERT', 'SYNC', 'SYNC_ROLLBACK'

`target`

(optional) The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database. - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.

Allowed values are: 'NEW_DATABASE'

`source_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`target_database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`cdb_name`

(required) The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.

`lifecycle_state`

(required) Status of an operation performed during the conversion of a non-container database to a pluggable database.

Allowed values are: 'SUCCEEDED', 'FAILED', 'IN_PROGRESS'

`lifecycle_details`

(optional) Additional information about the current lifecycle state for the conversion operation.

`time_started`

(required) The date and time when the database conversion operation started.

`time_ended`

(optional) The date and time when the database conversion operation ended.

`additional_cdb_params`

(optional) Additional container database parameter.

### DBMS_CLOUD_OCI_DATABASE_PDB_CONVERSION_TO_NEW_DATABASE_DETAILS_T Type

Details of the new container database in which the converted pluggable database will be located.

Syntax
```

```

`dbms_cloud_oci_database_pdb_conversion_to_new_database_details_t`is a subtype of the`dbms_cloud_oci_database_convert_to_pdb_target_base_t`type.

Fields

Field Description

`cdb_name`

(required) The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.

`cdb_admin_password`

(required) A strong password for SYS, SYSTEM, and the plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.

`pdb_admin_password`

(optional) A strong password for plugbable database ADMIN user of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.

`cdb_tde_wallet_password`

(optional) The password to open the TDE wallet of the container database after conversion. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.

`non_cdb_tde_wallet_password`

(required) The existing TDE wallet password of the non-container database.

`additional_cdb_params`

(optional) Additional container database parameters. Example: \"_pdb_name_case_sensitive=true\"

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_CONNECTION_STRINGS_T Type

Connection strings to connect to an Oracle Pluggable Database.

Syntax
```

```

Fields

Field Description

`pdb_default`

(optional) A host name-based PDB connection string.

`pdb_ip_default`

(optional) An IP-based PDB connection string.

`all_connection_strings`

(optional) All connection strings to use to connect to the pluggable database.

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_MANAGEMENT_CONFIG_T Type

The configuration of the Pluggable Database Management service.

Syntax
```

```

Fields

Field Description

`management_status`

(required) The status of the Pluggable Database Management service.

Allowed values are: 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'UPDATING', 'FAILED_ENABLING', 'FAILED_DISABLING', 'FAILED_UPDATING'

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_REFRESHABLE_CLONE_CONFIG_T Type

Pluggable Database Refreshable Clone Configuration.

Syntax
```

```

Fields

Field Description

`is_refreshable_clone`

(optional) Indicates whether the Pluggable Database is a refreshable clone.

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_NODE_LEVEL_DETAILS_T Type

Pluggable Database Node Level Details.

Syntax
```

```

Fields

Field Description

`node_name`

(required) The Node name of the Database Instance.

`open_mode`

(required) The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle Database software).

Allowed values are: 'READ_ONLY', 'READ_WRITE', 'MOUNTED', 'MIGRATE'

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_NODE_LEVEL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_pluggable_database_node_level_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_T Type

A pluggable database (PDB) is portable collection of schemas, schema objects, and non-schema objects that appears to an Oracle client as a non-container database. To use a PDB, it needs to be plugged into a CDB. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to a tenancy administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pluggable database.

`container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CDB.

`pdb_name`

(required) The name for the pluggable database (PDB). The name is unique in the context of a`DATABASE`Type. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.

`lifecycle_state`

(required) The current state of the pluggable database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'UPDATING', 'FAILED', 'RELOCATING', 'RELOCATED', 'REFRESHING', 'RESTORE_IN_PROGRESS', 'RESTORE_FAILED', 'BACKUP_IN_PROGRESS', 'DISABLED'

`lifecycle_details`

(optional) Detailed message for the lifecycle state.

`time_created`

(required) The date and time the pluggable database was created.

`connection_strings`

(optional)

`open_mode`

(required) **Deprecated.** Use`PLUGGABLE_DATABASE_NODE_LEVEL_DETAILS`Function for OpenMode details. The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle Database software).

Allowed values are: 'READ_ONLY', 'READ_WRITE', 'MOUNTED', 'MIGRATE'

`is_restricted`

(optional) The restricted mode of the pluggable database. If a pluggable database is opened in restricted mode, the user needs both create a session and have restricted session privileges to connect to it.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`pluggable_database_management_config`

(optional)

`refreshable_clone_config`

(optional)

`pdb_node_level_details`

(optional) Pluggable Database Node Level Details. Example: [{\"nodeName\" : \"node1\", \"openMode\" : \"READ_WRITE\"}, {\"nodeName\" : \"node2\", \"openMode\" : \"READ_ONLY\"}]

### DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_SUMMARY_T Type

A pluggable database (PDB) is portable collection of schemas, schema objects, and non-schema objects that appears to an Oracle client as a non-container database. To use a PDB, it needs to be plugged into a CDB. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to a tenancy administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the pluggable database.

`container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the CDB.

`pdb_name`

(required) The name for the pluggable database (PDB). The name is unique in the context of a`DATABASE`Type. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.

`lifecycle_state`

(required) The current state of the pluggable database.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'TERMINATING', 'TERMINATED', 'UPDATING', 'FAILED', 'RELOCATING', 'RELOCATED', 'REFRESHING', 'RESTORE_IN_PROGRESS', 'RESTORE_FAILED', 'BACKUP_IN_PROGRESS', 'DISABLED'

`lifecycle_details`

(optional) Detailed message for the lifecycle state.

`time_created`

(required) The date and time the pluggable database was created.

`connection_strings`

(optional)

`open_mode`

(required) **Deprecated.** Use`PLUGGABLE_DATABASE_NODE_LEVEL_DETAILS`Function for OpenMode details. The mode that pluggable database is in. Open mode can only be changed to READ_ONLY or MIGRATE directly from the backend (within the Oracle Database software).

Allowed values are: 'READ_ONLY', 'READ_WRITE', 'MOUNTED', 'MIGRATE'

`is_restricted`

(optional) The restricted mode of the pluggable database. If a pluggable database is opened in restricted mode, the user needs both create a session and have restricted session privileges to connect to it.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`pluggable_database_management_config`

(optional)

`refreshable_clone_config`

(optional)

`pdb_node_level_details`

(optional) Pluggable Database Node Level Details. Example: [{\"nodeName\" : \"node1\", \"openMode\" : \"READ_WRITE\"}, {\"nodeName\" : \"node2\", \"openMode\" : \"READ_ONLY\"}]

### DBMS_CLOUD_OCI_DATABASE_REFRESHABLE_CLONE_SUMMARY_T Type

An Autonomous Database refreshable clone

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database.

`l_region`

(required) The name of the region where the refreshable clone exists.

### DBMS_CLOUD_OCI_DATABASE_REFRESHABLE_CLONE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_refreshable_clone_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_REFRESHABLE_CLONE_COLLECTION_T Type

A list of Autonomous Database RefreshableClone containing RefreshableCloneSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required)

### DBMS_CLOUD_OCI_DATABASE_REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE_DETAILS_T Type

Details for registering an Autonomous Database with Data Safe.

Syntax
```

```

Fields

Field Description

`pdb_admin_password`

(required) The admin password provided during the creation of the database. This password is between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.

### DBMS_CLOUD_OCI_DATABASE_REINSTATE_DATA_GUARD_ASSOCIATION_DETAILS_T Type

The Data Guard association reinstate parameters.

Syntax
```

```

Fields

Field Description

`database_admin_password`

(required) The DB system administrator password.

### DBMS_CLOUD_OCI_DATABASE_REMOTE_CLONE_PLUGGABLE_DATABASE_DETAILS_T Type

**Deprecated.** Use`CREATE_PLUGGABLE_DATABASE_DETAILS`Function for Pluggable Database RemoteClone Operation. Parameters for cloning a pluggable database (PDB) in a remote database (CDB). A remote CDB is one that does not contain the source PDB. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`target_container_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target CDB

`source_container_db_admin_password`

(required) The DB system administrator password of the source CDB.

`cloned_pdb_name`

(required) The name for the pluggable database (PDB). The name is unique in the context of a`DATABASE`Type. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. The pluggable database name should not be same as the container database name.

`pdb_admin_password`

(optional) A strong password for PDB Admin of the newly cloned PDB. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.

`target_tde_wallet_password`

(optional) The existing TDE wallet password of the target CDB.

`should_pdb_admin_account_be_locked`

(optional) The locked mode of the pluggable database admin account. If false, the user needs to provide the PDB Admin Password to connect to it. If true, the pluggable database will be locked and user cannot login to it.

### DBMS_CLOUD_OCI_DATABASE_REMOVE_VIRTUAL_MACHINE_FROM_CLOUD_VM_CLUSTER_DETAILS_T Type

Details of removing Virtual Machines from the Cloud VM Cluster. Applies to Exadata Cloud instances only.

Syntax
```

```

Fields

Field Description

`db_servers`

(required) The list of ExaDB-D DB server for the cluster to be removed.

### DBMS_CLOUD_OCI_DATABASE_REMOVE_VIRTUAL_MACHINE_FROM_VM_CLUSTER_DETAILS_T Type

Details of removing Virtual Machines from the VM Cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`db_servers`

(required) The list of Exacc DB servers for the cluster to be removed.

### DBMS_CLOUD_OCI_DATABASE_NODE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_node_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_VM_NETWORK_DETAILS_T Type

Details of the client or backup networks in an Exadata VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`vlan_id`

(optional) The network VLAN ID.

`network_type`

(required) The network type.

Allowed values are: 'CLIENT', 'BACKUP', 'DISASTER_RECOVERY'

`netmask`

(optional) The network netmask.

`gateway`

(optional) The network gateway.

`domain_name`

(optional) The network domain name.

`nodes`

(required) The list of node details.

### DBMS_CLOUD_OCI_DATABASE_VM_NETWORK_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_vm_network_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_RESIZE_VM_CLUSTER_NETWORK_DETAILS_T Type

Details of Db server network nodes to extend or shrink the VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`action`

(required) Actions that can be performed on the VM cluster network. ADD_DBSERVER_NETWORK - Provide Db server network details of network nodes to be added to the VM cluster network. REMOVE_DBSERVER_NETWORK - Provide Db server network details of network nodes to be removed from the VM cluster network.

Allowed values are: 'ADD_DBSERVER_NETWORK', 'REMOVE_DBSERVER_NETWORK'

`vm_networks`

(required) Details of the client and backup networks.

### DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SHAPE_SUMMARY_T Type

An Autonomous Database Resource Pool. This object provides all the information related to the resource pool.

Syntax
```

```

Fields

Field Description

`shape`

(required) Predefined shape of the resource pool.

### DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SHAPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_resource_pool_shape_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SHAPE_COLLECTION_T Type

Results of an Autonomous Database resouce pool shape collection that contains ResourcePoolShapeSummary items.

Syntax
```

```

Fields

Field Description

`items`

(optional) List of Autonomous Database resource pools Shapes.

### DBMS_CLOUD_OCI_DATABASE_RESTORE_AUTONOMOUS_DATABASE_DETAILS_T Type

Details to restore an Oracle Autonomous Database.

Syntax
```

```

Fields

Field Description

`l_timestamp`

(required) The time to restore the database to.

`database_scn`

(optional) Restores using the backup with the System Change Number (SCN) specified.

`latest`

(optional) Restores to the last known good state with the least possible data loss.

### DBMS_CLOUD_OCI_DATABASE_RESTORE_DATABASE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`database_scn`

(optional) Restores using the backup with the System Change Number (SCN) specified. This field is applicable for both use cases - Restoring Container Database or Restoring specific Pluggable Database.

`l_timestamp`

(optional) Restores to the timestamp specified.

`latest`

(optional) Restores to the last known good state with the least possible data loss.

`pluggable_database_name`

(optional) Restores only the Pluggable Database (if specified) using the inputs provided in request.

### DBMS_CLOUD_OCI_DATABASE_ROTATE_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS_DETAILS_T Type

The details for configuring the SSL certificates on Autonomous VM Cluster

Syntax
```

```

Fields

Field Description

`certificate_generation_type`

(required) Specify SYSTEM to use Oracle-managed certificates. Specify BYOC when you want to bring your own certificate.

Allowed values are: 'SYSTEM', 'BYOC'

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate to use.

`certificate_authority_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate authority.

`ca_bundle_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate bundle.

### DBMS_CLOUD_OCI_DATABASE_ROTATE_AUTONOMOUS_VM_CLUSTER_SSL_CERTS_DETAILS_T Type

Details for configuring the ORDS certificates on Autonomous Exadata VM Cluster

Syntax
```

```

Fields

Field Description

`certificate_generation_type`

(required) Specify SYSTEM to use Oracle-managed certificates. Specify BYOC when you want to bring your own certificate.

Allowed values are: 'SYSTEM', 'BYOC'

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate to use.

`certificate_authority_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate authority.

`ca_bundle_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate bundle.

### DBMS_CLOUD_OCI_DATABASE_ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS_DETAILS_T Type

The details for configuring the ORDS certificates on Cloud Autonomous VM Cluster

Syntax
```

```

Fields

Field Description

`certificate_generation_type`

(required) Specify SYSTEM to use Oracle-managed certificates. Specify BYOC when you want to bring your own certificate.

Allowed values are: 'SYSTEM', 'BYOC'

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate to use.

`certificate_authority_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate authority.

`ca_bundle_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate bundle.

### DBMS_CLOUD_OCI_DATABASE_ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_SSL_CERTS_DETAILS_T Type

The details for configuring the SSL certificates on Cloud Autonomous VM Cluster

Syntax
```

```

Fields

Field Description

`certificate_generation_type`

(required) Specify SYSTEM to use Oracle-managed certificates. Specify BYOC when you want to bring your own certificate.

Allowed values are: 'SYSTEM', 'BYOC'

`certificate_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate to use.

`certificate_authority_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate authority.

`ca_bundle_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the certificate bundle.

### DBMS_CLOUD_OCI_DATABASE_SAAS_ADMIN_USER_CONFIGURATION_T Type

SaaS administrative user configuration.

Syntax
```

```

Fields

Field Description

`password`

(optional) A strong password for SaaS administrative user. The password must be a minimum of nine (9) characters and contain a minimum of two (2) uppercase, two (2) lowercase, two (2) numbers, and two (2) special characters from _ (underscore), \\# (hashtag), or - (dash).

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Cloud Infrastructure[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`secret_version_number`

(optional) The version of the vault secret. If no version is specified, the latest version will be used.

`duration`

(optional) How long, in hours, the SaaS administrative user will stay enabled. If no duration is specified, the default value 1 will be used.

`is_enabled`

(optional) Indicates if the SaaS administrative user is enabled for the Autonomous Database.

`access_type`

(optional) The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.

Allowed values are: 'READ_ONLY', 'READ_WRITE', 'ADMIN'

`time_saas_admin_user_enabled`

(optional) The date and time the SaaS administrative user was enabled at, for the Autonomous Database.

### DBMS_CLOUD_OCI_DATABASE_SAAS_ADMIN_USER_STATUS_T Type

SaaS administrative user status.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Indicates if the SaaS administrative user is enabled for the Autonomous Database.

`access_type`

(optional) The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.

Allowed values are: 'READ_ONLY', 'READ_WRITE', 'ADMIN'

`time_saas_admin_user_enabled`

(optional) The date and time the SaaS administrative user was enabled at, for the Autonomous Database.

### DBMS_CLOUD_OCI_DATABASE_SCAN_DETAILS_T Type

The Single Client Access Name (SCAN) details.

Syntax
```

```

Fields

Field Description

`hostname`

(required) The SCAN hostname.

`port`

(optional) **Deprecated.** This field is deprecated. You may use 'scanListenerPortTcp' to specify the port. The SCAN TCPIP port. Default is 1521.

`scan_listener_port_tcp`

(optional) The SCAN TCPIP port. Default is 1521.

`scan_listener_port_tcp_ssl`

(optional) The SCAN TCPIP SSL port. Default is 2484.

`ips`

(required) The list of SCAN IP addresses. Three addresses should be provided.

### DBMS_CLOUD_OCI_DATABASE_SELF_MOUNT_DETAILS_T Type

Used for creating NFS Self mount backup destinations for non-autonomous ExaCC.

Syntax
```

```

`dbms_cloud_oci_database_self_mount_details_t`is a subtype of the`dbms_cloud_oci_database_mount_type_details_t`type.

Fields

Field Description

`local_mount_point_path`

(required) The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.

### DBMS_CLOUD_OCI_DATABASE_SWITCHOVER_DATA_GUARD_ASSOCIATION_DETAILS_T Type

The Data Guard association switchover parameters.

Syntax
```

```

Fields

Field Description

`database_admin_password`

(required) The DB system administrator password.

### DBMS_CLOUD_OCI_DATABASE_SYSTEM_VERSION_SUMMARY_T Type

List of compatible Exadata system versions for a given shape and GI version.

Syntax
```

```

Fields

Field Description

`shape`

(required) Exadata shape.

`gi_version`

(required) Grid Infrastructure version.

`system_versions`

(optional) Compatible Exadata system versions for a given shape and GI version.

### DBMS_CLOUD_OCI_DATABASE_SYSTEM_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_system_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_SYSTEM_VERSION_COLLECTION_T Type

Results of the System version lists. Contains SystemVersionSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of System versions.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`description`

(required) Details of the maintenance update package.

`last_action`

(optional) The previous update action performed.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`available_actions`

(optional) The possible actions performed by the update operation on the infrastructure components.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of cloud VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`lifecycle_state`

(optional) The current state of the maintenance update. Dependent on value of `lastAction`.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time the maintenance update was released.

`version`

(required) The version of the maintenance update package.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_CONTAINER_DATABASE_DATA_GUARD_ASSOCIATION_DETAILS_T Type

The configuration details for updating a Autonomous Container DatabaseData Guard association for a Autonomous Container Database.

Syntax
```

```

Fields

Field Description

`is_automatic_failover_enabled`

(optional) Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association

`protection_mode`

(optional) The protection mode of this Autonomous Data Guard association. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE'

`fast_start_fail_over_lag_limit_in_seconds`

(optional) The lag time for my preference based on data loss tolerance in seconds.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_CONTAINER_DATABASE_DETAILS_T Type

Describes the modification parameters for the Autonomous Container Database.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name for the Autonomous Container Database.

`patch_model`

(optional) Database Patch model preference.

Allowed values are: 'RELEASE_UPDATES', 'RELEASE_UPDATE_REVISIONS'

`maintenance_window_details`

(optional)

`standby_maintenance_buffer_in_days`

(optional) The scheduling detail for the quarterly maintenance window of the standby Autonomous Container Database. This value represents the number of days before schedlued maintenance of the primary database.

`version_preference`

(optional) The next maintenance version preference.

Allowed values are: 'NEXT_RELEASE_UPDATE', 'LATEST_RELEASE_UPDATE'

`is_dst_file_update_enabled`

(optional) Indicates if an automatic DST Time Zone file update is enabled for the Autonomous Container Database. If enabled along with Release Update, patching will be done in a Non-Rolling manner.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`backup_config`

(optional)

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_DATABASE_BACKUP_DETAILS_T Type

Details for updating the Autonomous Database backup. **Warning:** Oracle recommends avoiding using confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`retention_period_in_days`

(optional) Retention period, in days, for long-term backups

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_DATABASE_DETAILS_T Type

Details to update an Oracle Autonomous Database. **Notes** - To specify OCPU core count, you must use either `ocpuCount` or `cpuCoreCount`. You cannot use both parameters at the same time. - To specify a storage allocation, you must use either `dataStorageSizeInGBs` or `dataStorageSizeInTBs`. - See the individual parameter discriptions for more information on the OCPU and storage value parameters. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`backup_retention_period_in_days`

(optional) Retention period, in days, for long-term backups

`compute_model`

(optional) The compute model of the Autonomous Database. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value.

Allowed values are: 'ECPU', 'OCPU'

`in_memory_percentage`

(optional) The percentage of the System Global Area(SGA) assigned to In-Memory tables in Autonomous Database.

`local_adg_auto_failover_max_data_loss_limit`

(optional) Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard

`cpu_core_count`

(optional) The number of CPUs to be made available to the Autonomous Database.&lt;br&gt; For Autonomous Databases on Dedicated Exadata Infrastructure: - The CPU type (OCPUs or ECPUs) is determined by the parent Autonomous Exadata VM Cluster's compute model. - It is suggested to use 'computeCount' parameter if you want to use fractional value to provision less than 1 core. **Note:** This parameter cannot be used with the `ocpuCount` or `computeCount` parameter. This cannot be updated in parallel with any of the following: licenseModel, databaseEdition, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`long_term_backup_schedule`

(optional)

`compute_count`

(optional) The compute amount available to the database. Minimum and maximum values depend on the compute model and whether the database is an Autonomous Database Serverless instance or an Autonomous Database on Dedicated Exadata Infrastructure. For an Autonomous Database Serverless instance, the ECPU compute model requires values in multiples of two. Required when using the computeModel parameter. When using the cpuCoreCount parameter, computeCount must be null. This cannot be updated in parallel with any of the following: licenseModel, databaseEdition, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`ocpu_count`

(optional) The number of OCPU cores to be made available to the Autonomous Database. For Autonomous Databases on Dedicated Exadata Infrastructure, you can specify a fractional value for this parameter. Fractional values are not supported for Autonomous Database Serverless instances. To provision less than 1 core, enter a fractional value in an increment of 0.1. To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available to the infrastructure shape. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. Likewise, you can provision 2 cores or 3 cores, but not 2.5 cores. The maximum number of cores is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html)for shape details. **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

`data_storage_size_in_t_bs`

(optional) The size, in terabytes, of the data volume that will be created and attached to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. A full Exadata service is allocated when the Autonomous Database size is set to the upper limit (384 TB). **Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter. This cannot be updated in parallel with any of the following: licenseModel, databaseEdition, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`data_storage_size_in_g_bs`

(optional) Applies to dedicated Exadata infrastructure only. The size, in gigabytes, of the data volume that will be created and attached to the database. The maximum storage value depends on the system shape. See[Characteristics of Infrastructure Shapes](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbde/index.html#articletitle)for shape details. **Note:** This parameter cannot be used with the `dataStorageSizeInTBs` parameter.

`display_name`

(optional) The user-friendly name for the Autonomous Database. The name does not have to be unique. The display name can only be updated for Autonomous Databases using dedicated Exadata Infrastructure. This parameter may not be updated in parallel with dbVersion.

`is_free_tier`

(optional) Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isLocalDataGuardEnabled

`admin_password`

(optional) The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours. This cannot be used in conjunction with with OCI vault secrets (secretId). This cannot be updated in parallel with any of the following: licenseModel, dbEdition, whitelistedIps, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, or isFreeTier.

`db_name`

(optional) New name for this Autonomous Database. For Autonomous Databases on Dedicated Exadata Infrastructure, the name must begin with an alphabetic character, and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. For Autonomous Database Serverless instances, the name must begin with an alphabetic character, and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`db_workload`

(optional) The Autonomous Database workload type. The following values are valid: - OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

Allowed values are: 'OLTP', 'DW', 'AJD', 'APEX'

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`is_access_control_enabled`

(optional) Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional, if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone. This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.

`whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`are_primary_whitelisted_ips_used`

(optional) This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled. `TRUE` if the Autonomous Database has Data Guard and Access Control enabled, and the Autonomous Database uses the primary's IP access control list (ACL) for standby. `FALSE` if the Autonomous Database has Data Guard and Access Control enabled, and the Autonomous Database uses a different IP access control list (ACL) for standby compared to primary.

`standby_whitelisted_ips`

(optional) The client IP access control list (ACL). This feature is available for[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. For Autonomous Database Serverless, this is an array of CIDR (classless inter-domain routing) notations for a subnet or VCN OCID (virtual cloud network Oracle Cloud ID). Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.&lt;unique_id&gt;\",\"ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1\",\"ocid1.vcn.oc1.sea.&lt;unique_id2&gt;;1.1.0.0/16\"]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR notations. Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]` For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`is_auto_scaling_enabled`

(optional) Indicates whether auto scaling is enabled for the Autonomous Database OCPU core count. Setting to `TRUE` enables auto scaling. Setting to `FALSE` disables auto scaling. The default value is true. Auto scaling is only available for[Autonomous Database Serverless instances](https://docs.oracle.com/en/cloud/paas/autonomous-database/shared/index.html).

`is_refreshable_clone`

(optional) Indicates if the Autonomous Database is a refreshable clone. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`refreshable_mode`

(optional) The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

Allowed values are: 'AUTOMATIC', 'MANUAL'

`is_local_data_guard_enabled`

(optional) Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable when creating a cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure. To create a local standby, set to `TRUE`. To delete a local standby, set to `FALSE`. For more information on using Autonomous Data Guard on an Autonomous Database Serverless instance (local and cross-region) , see[About Standby Databases](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-data-guard-about.html#GUID-045AD017-8120-4BDC-AF58-7430FFE28D2B). This cannot be updated in parallel with any of the following: isMTLSRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`is_data_guard_enabled`

(optional) ** Deprecated. ** Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable when creating a cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure. To create a local standby, set to `TRUE`. To delete a local standby, set to `FALSE`. For more information on using Autonomous Data Guard on an Autonomous Database Serverless instance (local and cross-region) , see[About Standby Databases](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-data-guard-about.html#GUID-045AD017-8120-4BDC-AF58-7430FFE28D2B). To delete a cross-region standby database, provide the `peerDbId` for the standby database in a remote region, and set `isDataGuardEnabled` to `FALSE`.

`peer_db_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Data Guard standby database located in a different (remote) region from the source primary Autonomous Database. To create or delete a local (in-region) standby, see the `isDataGuardEnabled` parameter.

`db_version`

(optional) A valid Oracle Database version for Autonomous Database.

`open_mode`

(optional) Indicates the Autonomous Database mode. The database can be opened in `READ_ONLY` or `READ_WRITE` mode. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'READ_ONLY', 'READ_WRITE'

`permission_level`

(optional) The Autonomous Database permission level. Restricted mode allows access only by admin users. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'RESTRICTED', 'UNRESTRICTED'

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the resource is associated with. **Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. - For Autonomous Database, setting this will disable public secure access to the database. These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.

`private_endpoint_label`

(optional) The resource's private endpoint label. Setting this to an empty string, after the creation of the private endpoint database, changes the private endpoint database to a public endpoint database. This setting cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`private_endpoint_ip`

(optional) The private endpoint Ip address for the resource.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`customer_contacts`

(optional) Customer Contacts. Setting this to an empty list removes all customer contacts of an Oracle This cannot be updated in parallel with any of the following: isMTLSConnectionRequired, scheduledOperations, or dbToolsDetails.

`is_mtls_connection_required`

(optional) Specifies if the Autonomous Database requires mTLS connections. This may not be updated in parallel with any of the following: licenseModel, databaseEdition, cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, whitelistedIps, openMode, permissionLevel, db-workload, privateEndpointLabel, nsgIds, customerContacts, dbVersion, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier. Service Change: The default value of the isMTLSConnectionRequired attribute will change from true to false on July 1, 2023 in the following APIs: - CreateAutonomousDatabase - GetAutonomousDatabase - UpdateAutonomousDatabase Details: Prior to the July 1, 2023 change, the isMTLSConnectionRequired attribute default value was true. This applies to Autonomous Database Serverless. Does this impact me? If you use or maintain custom scripts or Terraform scripts referencing the CreateAutonomousDatabase, GetAutonomousDatabase, or UpdateAutonomousDatabase APIs, you want to check, and possibly modify, the scripts for the changed default value of the attribute. Should you choose not to leave your scripts unchanged, the API calls containing this attribute will continue to work, but the default value will switch from true to false. How do I make this change? Using either OCI SDKs or command line tools, update your custom scripts to explicitly set the isMTLSConnectionRequired attribute to true.

`resource_pool_leader_id`

(optional) The unique identifier for leader autonomous database OCID[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resource_pool_summary`

(optional)

`scheduled_operations`

(optional) The list of scheduled operations. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.

`is_auto_scaling_for_storage_enabled`

(optional) Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.

`max_cpu_core_count`

(optional) The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.

`database_edition`

(optional) The Oracle Database Edition that applies to the Autonomous databases. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

`db_tools_details`

(optional) The list of database tools details. This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, isLocalDataGuardEnabled, or isFreeTier.

`secret_id`

(optional) The OCI vault secret [/Content/General/Concepts/identifiers.htm]OCID. This cannot be used in conjunction with adminPassword.

`secret_version_number`

(optional) The version of the vault secret. If no version is specified, the latest version will be used.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_DATABASE_WALLET_DETAILS_T Type

Details to update an Autonomous Database wallet.

Syntax
```

```

Fields

Field Description

`should_rotate`

(optional) Indicates whether to rotate the wallet or not. If `false`, the wallet will not be rotated. The default is `false`.

`grace_period`

(optional) The number of hours that the old wallet can be used after it has been rotated. The old wallet will no longer be valid after the number of hours in the wallet rotation grace period has passed. During the grace period, both the old wallet and the current wallet can be used.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_DETAILS_T Type

Describes the modification parameters for the Autonomous Exadata Infrastructure.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name is a user-friendly name for the Autonomous Exadata Infrastructure. The display name does not have to be unique.

`maintenance_window_details`

(optional)

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type

Details for updating the Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`maintenance_window_details`

(optional)

`license_model`

(optional) The Oracle license model that applies to the Autonomous VM cluster. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`autonomous_data_storage_size_in_t_bs`

(optional) The new scaled up/down value for autonomous data storage in TBs for Autonomous VM cluster.

`cpu_core_count_per_node`

(optional) The new scaled up/down value for cpus per Autonomous VM cluster per node.

`total_container_databases`

(optional) The new scaled up/down value for maxACD count for Autonomous VM cluster.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_BACKUP_DESTINATION_DETAILS_T Type

For a RECOVERY_APPLIANCE backup destination, used to update the connection string and/or the list of VPC users. For an NFS backup destination, there are 2 mount types - Self mount used for non-autonomous ExaCC and automated mount used for autonomous on ExaCC.

Syntax
```

```

Fields

Field Description

`vpc_users`

(optional) For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.

`connection_string`

(optional) For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.

`local_mount_point_path`

(optional) The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.

`nfs_mount_type`

(optional) NFS Mount type for backup destination.

Allowed values are: 'SELF_MOUNT', 'AUTOMATED_MOUNT'

`nfs_server`

(optional) IP addresses for NFS Auto mount.

`nfs_server_export`

(optional) Specifies the directory on which to mount the file system

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_CLOUD_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type

Details for updating the cloud Autonomous VM cluster.

Syntax
```

```

Fields

Field Description

`description`

(optional) User defined description of the cloud Autonomous VM cluster.

`display_name`

(optional) The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.

`maintenance_window_details`

(optional)

`autonomous_data_storage_size_in_t_bs`

(optional) The new scaled up/down value for exadata storage in TBs for cloud autonomous VM cluster.

`cpu_core_count_per_node`

(optional) The new scaled up/down value for ocpus for cloud autonomous VM cluster per node.

`total_container_databases`

(optional) The new scaled up/down value for maxACD count for cloud autonomous VM cluster.

`license_model`

(optional) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Oracle Database service. Note that when provisioning an[Autonomous Database on dedicated Exadata infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), this attribute must be null. It is already set at the Autonomous Exadata Infrastructure level. When provisioning an[Autonomous Database Serverless]](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)database, if a value is not specified, the system defaults the value to `BRING_YOUR_OWN_LICENSE`. This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_CLOUD_EXADATA_INFRASTRUCTURE_DETAILS_T Type

Updates the cloud Exadata infrastructure. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the cloud Exadata infrastructure. The name does not need to be unique.

`maintenance_window`

(optional)

`compute_count`

(optional) The number of compute servers for the cloud Exadata infrastructure.

`storage_count`

(optional) The number of storage servers for the cloud Exadata infrastructure.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`customer_contacts`

(optional) Customer contacts. Setting this to an empty list removes all customer contact information (email addresses) for the specified OCI Database service resource.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DETAILS_T Type

Details specifying which maintenance update to apply to the cloud VM cluster and which actions are to be performed by the maintenance update. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`update_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`update_action`

(optional) The update action.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

### DBMS_CLOUD_OCI_DATABASE_UPDATE_CLOUD_VM_CLUSTER_DETAILS_T Type

Details for updating the cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the cloud VM cluster. The name does not need to be unique.

`cpu_core_count`

(optional) The number of CPU cores to enable for the cloud VM cluster.

`ocpu_count`

(optional) The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.

`memory_size_in_g_bs`

(optional) The memory to be allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage to be allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated in TBs.

`license_model`

(optional) The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE. Applies to Exadata Cloud Service instances only.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`ssh_public_keys`

(optional) The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.

`update_details`

(optional)

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`compute_nodes`

(optional) The list of compute servers to be added to the cloud VM cluster.

`storage_size_in_g_bs`

(optional) The disk group size to be allocated in GBs.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_UPDATE_CONSOLE_CONNECTION_DETAILS_T Type

The details for updating a Db node console connection.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_CONSOLE_HISTORY_DETAILS_T Type

The details for updating a Db node console history.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(optional) The user-friendly name for the console history. The name does not need to be unique.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DATA_GUARD_ASSOCIATION_DETAILS_T Type

The configuration details for updating a Data Guard association for a database. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`database_admin_password`

(optional) A strong password for the 'SYS', 'SYSTEM', and 'PDB Admin' users to apply during standby creation. The password must contain no fewer than nine characters and include: * At least two uppercase characters. * At least two lowercase characters. * At least two numeric characters. * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only. **The password MUST be the same as the primary admin password.**

`protection_mode`

(optional) The protection mode for the Data Guard association's primary and standby database. For more information, see[Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)in the Oracle Data Guard documentation.

Allowed values are: 'MAXIMUM_AVAILABILITY', 'MAXIMUM_PERFORMANCE', 'MAXIMUM_PROTECTION'

`transport_type`

(optional) The redo transport type to use for this Data Guard association. Valid values depend on the specified 'protectionMode': * MAXIMUM_AVAILABILITY - Use SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - Use ASYNC * MAXIMUM_PROTECTION - Use SYNC For more information, see[Redo Transport Services](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)in the Oracle Data Guard documentation.

Allowed values are: 'SYNC', 'ASYNC', 'FASTSYNC'

`is_active_data_guard_enabled`

(optional) True if active Data Guard is enabled. Update this parameter to change the Data Guard setting.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DATABASE_DETAILS_T Type

Details to update a database. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`db_backup_config`

(optional)

`db_home_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Home.

`new_admin_password`

(optional) A new strong password for SYS, SYSTEM, and the plugbable database ADMIN user. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.

`old_tde_wallet_password`

(optional) The existing TDE wallet password. You must provide the existing password in order to set a new TDE wallet password.

`new_tde_wallet_password`

(optional) The new password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, \\#, or -.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DATABASE_SOFTWARE_IMAGE_DETAILS_T Type

Describes the parameters for updating the Database Software Image

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the database software image. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DB_HOME_DETAILS_T Type

Describes the modification parameters for the Database Home.

Syntax
```

```

Fields

Field Description

`db_version`

(optional)

`one_off_patches`

(optional) List of one-off patches for Database Homes.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DB_NODE_DETAILS_T Type

The details for updating a Db node.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_DB_SYSTEM_DETAILS_T Type

Describes the parameters for updating the DB system. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`cpu_core_count`

(optional) The new number of CPU cores to set for the DB system. Not applicable for INTEL based virtual machine DB systems.

`version`

(optional)

`ssh_public_keys`

(optional) The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.

`data_storage_size_in_g_bs`

(optional) The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.

`reco_storage_size_in_g_bs`

(optional) The size, in gigabytes, to scale the attached RECO storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for the software volume. Applies only to virtual machine DB systems.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`shape`

(optional) The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory To get a list of shapes, use the`LIST_DB_SYSTEM_SHAPES`Function operation.

`nsg_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

`backup_network_nsg_ids`

(optional) A list of the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

`license_model`

(optional) The Oracle Database license model that applies to all databases on the DB system. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`maintenance_window_details`

(optional)

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXADATA_INFRASTRUCTURE_DETAILS_T Type

Updates the Exadata infrastructure. Applies to Exadata Cloud@Customer instances only. See`UPDATE_CLOUD_EXADATA_INFRASTRUCTURE_DETAILS`Function for information on updating Exadata Cloud Service cloud Exadata infrastructure resources.

Syntax
```

```

Fields

Field Description

`cloud_control_plane_server1`

(optional) The IP address for the first control plane server.

`cloud_control_plane_server2`

(optional) The IP address for the second control plane server.

`netmask`

(optional) The netmask for the control plane network.

`gateway`

(optional) The gateway for the control plane network.

`admin_network_cidr`

(optional) The CIDR block for the Exadata administration network.

`infini_band_network_cidr`

(optional) The CIDR block for the Exadata InfiniBand interconnect.

`corporate_proxy`

(optional) The corporate network proxy for access to the control plane network.

`contacts`

(optional) The list of contacts for the Exadata infrastructure.

`maintenance_window`

(optional)

`additional_storage_count`

(optional) The requested number of additional storage servers for the Exadata infrastructure.

`is_multi_rack_deployment`

(optional) Indicates if deployment is Multi-Rack or not.

`multi_rack_configuration_file`

(optional) The base64 encoded Multi-Rack configuration json file.

`additional_compute_count`

(optional) The requested number of additional compute servers for the Exadata infrastructure.

`additional_compute_system_model`

(optional) Oracle Exadata System Model specification. The system model determines the amount of compute or storage server resources available for use. For more information, please see[System and Shape Configuration Options]](https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-system-config-options.html#GUID-9E090174-5C57-4EB1-9243-B470F9F10D6B)

Allowed values are: 'X7', 'X8', 'X8M', 'X9M', 'X10M'

`dns_server`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp_server`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`time_zone`

(optional) The time zone of the Exadata infrastructure. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`is_cps_offline_report_enabled`

(optional) Indicates whether cps offline diagnostic report is enabled for this Exadata infrastructure. This will allow a customer to quickly check status themselves and fix problems on their end, saving time and frustration for both Oracle and the customer when they find the CPS in a disconnected state.You can enable offline diagnostic report during Exadata infrastructure provisioning. You can also disable or enable it at any time using the UpdateExadatainfrastructure API.

`network_bonding_mode_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_CONTAINER_DATABASE_DETAILS_T Type

Details for updating an external container database. This API is not currently supported.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS_T Type

Details for updating an external database connector.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`display_name`

(optional) The user-friendly name for the`CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS`Function. The name does not have to be unique.

`connector_type`

(optional) The type of connector used by the external database resource.

Allowed values are: 'MACS'

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_DATABASE_DETAILS_BASE_T Type

Details for updating an external database. This API is not currently supported.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_MACS_CONNECTOR_DETAILS_T Type

Details for updating an external[Management Agent cloud service (MACS)](https://docs.oracle.com/iaas/management-agents/index.html)database connection.

Syntax
```

```

`dbms_cloud_oci_database_update_external_macs_connector_details_t`is a subtype of the`dbms_cloud_oci_database_update_external_database_connector_details_t`type.

Fields

Field Description

`connection_string`

(optional)

`connection_credentials`

(optional)

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_NON_CONTAINER_DATABASE_DETAILS_T Type

Details for updating an external non-container database. This API is not currently supported.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS_T Type

Details for updating an external pluggable database. This API is not currently supported.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The user-friendly name for the external database. The name does not have to be unique.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_HISTORY_ENTRY_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update history entry.

`update_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`update_action`

(optional) The update action.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of cloud VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_state`

(required) The current lifecycle state of the maintenance update operation.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`time_started`

(required) The date and time when the maintenance update action started.

`time_completed`

(optional) The date and time when the maintenance update action completed.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_HISTORY_ENTRY_SUMMARY_T Type

The record of an maintenance update action on a specified cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update history entry.

`update_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`update_action`

(optional) The update action.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of cloud VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_state`

(required) The current lifecycle state of the maintenance update operation.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`time_started`

(required) The date and time when the maintenance update action started.

`time_completed`

(optional) The date and time when the maintenance update action completed.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_KEY_STORE_DETAILS_T Type

Details for updating the key store.

Syntax
```

```

Fields

Field Description

`type_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_MAINTENANCE_RUN_DETAILS_T Type

Describes the modification parameters for the maintenance run.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) If `FALSE`, skips the maintenance run.

`time_scheduled`

(optional) The scheduled date and time of the maintenance run to update.

`is_patch_now_enabled`

(optional) If set to `TRUE`, starts patching immediately.

`patch_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch to be applied in the maintenance run.

`patching_mode`

(optional) Cloud Exadata infrastructure node patching method, either \"ROLLING\" or \"NONROLLING\". Default value is ROLLING. *IMPORTANT*: Non-rolling infrastructure patching involves system down time. See[Oracle-Managed Infrastructure Maintenance Updates](https://docs.oracle.com/iaas/Content/Database/Concepts/examaintenance.htm#Oracle)for more information.

Allowed values are: 'ROLLING', 'NONROLLING'

`is_custom_action_timeout_enabled`

(optional) If true, enables the configuration of a custom action timeout (waiting period) between database servers patching operations.

`custom_action_timeout_in_mins`

(optional) Determines the amount of time the system will wait before the start of each database server patching operation. Specify a number of minutes from 15 to 120.

`current_custom_action_timeout_in_mins`

(optional) The current custom action timeout between the current database servers during waiting state in addition to custom action timeout, from 0 (zero) to 30 minutes.

`is_resume_patching`

(optional) If true, then the patching is resumed and the next component will be patched immediately.

`target_db_server_version`

(optional) The target database server system software version for the patching operation.

`target_storage_server_version`

(optional) The target storage cell system software version for the patching operation.

### DBMS_CLOUD_OCI_DATABASE_UPDATE_ONEOFF_PATCH_DETAILS_T Type

Data to update the one-off patch.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_PLUGGABLE_DATABASE_DETAILS_T Type

Details for updating a pluggable database (PDB). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPDATE_SUMMARY_T Type

A maintenance update for a cloud VM cluster. Applies to Exadata Cloud Service instances only. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`description`

(required) Details of the maintenance update package.

`last_action`

(optional) The previous update action performed.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`available_actions`

(optional) The possible actions performed by the update operation on the infrastructure components.

Allowed values are: 'ROLLING_APPLY', 'NON_ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of cloud VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`lifecycle_state`

(optional) The current state of the maintenance update. Dependent on value of `lastAction`.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time the maintenance update was released.

`version`

(required) The version of the maintenance update package.

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_DETAILS_T Type

Details specifying which maintenance update to apply to the VM Cluster and which action is to be performed by the maintenance update. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`update_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`update_action`

(optional) The update action to perform.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

### DBMS_CLOUD_OCI_DATABASE_UPDATE_VM_CLUSTER_DETAILS_T Type

Details for updating the VM cluster. Applies to Exadata Cloud@Customer instances only. For details on updating a cloud VM cluster in an Exadata Cloud Service instance, see`UPDATE_CLOUD_VM_CLUSTER_DETAILS`Function

Syntax
```

```

Fields

Field Description

`cpu_core_count`

(optional) The number of CPU cores to enable for the VM cluster.

`ocpu_count`

(optional) The number of OCPU cores to enable for the VM cluster. Only 1 decimal place is allowed for the fractional part.

`memory_size_in_g_bs`

(optional) The memory to be allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage to be allocated in GBs.

`data_storage_size_in_t_bs`

(optional) The data disk group size to be allocated in TBs.

`data_storage_size_in_g_bs`

(optional) The data disk group size to be allocated in GBs.

`license_model`

(optional) The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`ssh_public_keys`

(optional) The public key portion of one or more key pairs used for SSH access to the VM cluster.

`version`

(optional)

`update_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_SCAN_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_scan_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_DR_SCAN_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_dr_scan_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_UPDATE_VM_CLUSTER_NETWORK_DETAILS_T Type

Details for an Exadata VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`scans`

(optional) The SCAN details.

`dns`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`vm_networks`

(optional) Details of the client and backup networks.

`dr_scans`

(optional) The SCAN details for DR network

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_UPGRADE_DATABASE_DETAILS_T Type

Details for upgrading a database to a specific Oracle Database version.

Syntax
```

```

Fields

Field Description

`action`

(required) The database upgrade action.

Allowed values are: 'PRECHECK', 'UPGRADE', 'ROLLBACK'

`database_upgrade_source_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_UPGRADE_DB_SYSTEM_DETAILS_T Type

Details for upgrading the operating system and Oracle Grid Infrastructure (GI) of a DB system.

Syntax
```

```

Fields

Field Description

`action`

(required) The operating system upgrade action.

Allowed values are: 'PRECHECK', 'ROLLBACK', 'UPDATE_SNAPSHOT_RETENTION_DAYS', 'UPGRADE'

`snapshot_retention_period_in_days`

(optional) The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.

`new_gi_version`

(optional) A valid Oracle Grid Infrastructure (GI) software version.

`new_os_version`

(optional) A valid Oracle Software (OS) version eg. Oracle Linux Server release 8

`is_snapshot_retention_days_force_updated`

(optional) If true, rollback time is updated even if operating system upgrade history contains errors.

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_T Type

Details of the VM cluster resource. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation starts.

`lifecycle_state`

(optional) The current state of the VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`display_name`

(optional) The user-friendly name for the Exadata Cloud@Customer VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the VM cluster was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_zone`

(optional) The time zone of the Exadata infrastructure. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`is_sparse_diskgroup_enabled`

(optional) If true, sparse disk group is configured for the VM cluster. If false, sparse disk group is not created.

`vm_cluster_network_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`cpus_enabled`

(optional) The number of enabled CPU cores.

`ocpus_enabled`

(optional) The number of enabled OCPU cores.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`data_storage_size_in_t_bs`

(optional) Size, in terabytes, of the DATA disk group.

`data_storage_size_in_g_bs`

(optional) Size of the DATA disk group in GBs.

`shape`

(optional) The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.

`gi_version`

(optional) The Oracle Grid Infrastructure software version for the VM cluster.

`system_version`

(optional) Operating system version of the image.

`ssh_public_keys`

(optional) The public key portion of one or more key pairs used for SSH access to the VM cluster.

`license_model`

(optional) The Oracle license model that applies to the VM cluster. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`db_servers`

(optional) The list of Db server.

`availability_domain`

(optional) The name of the availability domain that the VM cluster is located in.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_NETWORK_T Type

The VM cluster network.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated VM Cluster.

`display_name`

(optional) The user-friendly name for the VM cluster network. The name does not need to be unique.

`scans`

(optional) The SCAN details.

`dns`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`vm_networks`

(optional) Details of the client and backup networks.

`dr_scans`

(optional) The SCAN details for DR network

`lifecycle_state`

(optional) The current state of the VM cluster network. CREATING - The resource is being created REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated. VALIDATING - The resource is being validated and not available to use. VALIDATED - The resource is validated and is available for consumption by VM cluster. VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected. UPDATING - The resource is being updated and not available to use. ALLOCATED - The resource is is currently being used by VM cluster. TERMINATING - The resource is being deleted and not available to use. TERMINATED - The resource is deleted and unavailable. FAILED - The resource is in a failed state due to validation or other errors. NEEDS_ATTENTION - The resource is in needs attention state as some of it's child nodes are not validated and unusable by VM cluster.

Allowed values are: 'CREATING', 'REQUIRES_VALIDATION', 'VALIDATING', 'VALIDATED', 'VALIDATION_FAILED', 'UPDATING', 'ALLOCATED', 'TERMINATING', 'TERMINATED', 'FAILED', 'NEEDS_ATTENTION'

`time_created`

(optional) The date and time when the VM cluster network was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_NETWORK_DETAILS_T Type

Details for an Exadata VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(required) The user-friendly name for the Exadata Cloud@Customer VM cluster network. The name does not need to be unique.

`scans`

(required) The SCAN details.

`dns`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`vm_networks`

(required) Details of the client and backup networks.

`dr_scans`

(optional) The SCAN details for DR network

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_NETWORK_SUMMARY_T Type

Details of the VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated VM Cluster.

`display_name`

(optional) The user-friendly name for the VM cluster network. The name does not need to be unique.

`scans`

(optional) The SCAN details.

`dns`

(optional) The list of DNS server IP addresses. Maximum of 3 allowed.

`ntp`

(optional) The list of NTP server IP addresses. Maximum of 3 allowed.

`vm_networks`

(optional) Details of the client and backup networks.

`dr_scans`

(optional) The SCAN details for DR network

`lifecycle_state`

(optional) The current state of the VM cluster network. CREATING - The resource is being created REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated. VALIDATING - The resource is being validated and not available to use. VALIDATED - The resource is validated and is available for consumption by VM cluster. VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected. UPDATING - The resource is being updated and not available to use. ALLOCATED - The resource is is currently being used by VM cluster. TERMINATING - The resource is being deleted and not available to use. TERMINATED - The resource is deleted and unavailable. FAILED - The resource is in a failed state due to validation or other errors. NEEDS_ATTENTION - The resource is in needs attention state as some of it's child nodes are not validated and unusable by VM cluster.

Allowed values are: 'CREATING', 'REQUIRES_VALIDATION', 'VALIDATING', 'VALIDATED', 'VALIDATION_FAILED', 'UPDATING', 'ALLOCATED', 'TERMINATING', 'TERMINATED', 'FAILED', 'NEEDS_ATTENTION'

`time_created`

(optional) The date and time when the VM cluster network was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_SUMMARY_T Type

Details of the Exadata Cloud@Customer VM cluster.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`last_patch_history_entry_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last patch history. This value is updated as soon as a patch operation starts.

`lifecycle_state`

(optional) The current state of the VM cluster.

Allowed values are: 'PROVISIONING', 'AVAILABLE', 'UPDATING', 'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'

`display_name`

(optional) The user-friendly name for the Exadata Cloud@Customer VM cluster. The name does not need to be unique.

`time_created`

(optional) The date and time that the VM cluster was created.

`lifecycle_details`

(optional) Additional information about the current lifecycle state.

`time_zone`

(optional) The time zone of the Exadata infrastructure. For details, see[Exadata Infrastructure Time Zones](https://docs.oracle.com/iaas/Content/Database/References/timezones.htm).

`is_local_backup_enabled`

(optional) If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.

`exadata_infrastructure_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata infrastructure.

`is_sparse_diskgroup_enabled`

(optional) If true, sparse disk group is configured for the VM cluster. If false, sparse disk group is not created.

`vm_cluster_network_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster network.

`cpus_enabled`

(optional) The number of enabled CPU cores.

`ocpus_enabled`

(optional) The number of enabled OCPU cores.

`memory_size_in_g_bs`

(optional) The memory allocated in GBs.

`db_node_storage_size_in_g_bs`

(optional) The local node storage allocated in GBs.

`data_storage_size_in_t_bs`

(optional) Size, in terabytes, of the DATA disk group.

`data_storage_size_in_g_bs`

(optional) Size of the DATA disk group in GBs.

`shape`

(optional) The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.

`gi_version`

(optional) The Oracle Grid Infrastructure software version for the VM cluster.

`system_version`

(optional) Operating system version of the image.

`ssh_public_keys`

(optional) The public key portion of one or more key pairs used for SSH access to the VM cluster.

`license_model`

(optional) The Oracle license model that applies to the VM cluster. The default is LICENSE_INCLUDED.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`db_servers`

(optional) The list of Db server.

`availability_domain`

(optional) The name of the availability domain that the VM cluster is located in.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

`data_collection_options`

(optional)

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_T Type

A maintenance update for a VM cluster. Applies to Exadata Cloud@Customer instances only. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`description`

(required) Details of the maintenance update package.

`last_action`

(optional) The update action performed most recently using this maintenance update.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`available_actions`

(optional) The possible actions that can be performed using this maintenance update.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`lifecycle_state`

(optional) The current state of the maintenance update. Dependent on value of `lastAction`.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time the maintenance update was released.

`version`

(required) The version of the maintenance update package.

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_HISTORY_ENTRY_T Type

The record of a maintenance update action performed on a specified VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update history entry.

`update_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`update_action`

(optional) The update action performed using this maintenance update.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_state`

(required) The current lifecycle state of the maintenance update operation.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`time_started`

(required) The date and time when the maintenance update action started.

`time_completed`

(optional) The date and time when the maintenance update action completed.

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_HISTORY_ENTRY_SUMMARY_T Type

The record of a maintenance update action performed on a specified VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update history entry.

`update_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`update_action`

(optional) The update action performed using this maintenance update.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_state`

(required) The current lifecycle state of the maintenance update operation.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`time_started`

(required) The date and time when the maintenance update action started.

`time_completed`

(optional) The date and time when the maintenance update action completed.

### DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_SUMMARY_T Type

A maintenance update for a VM cluster. Applies to Exadata Cloud@Customer instances only. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`description`

(required) Details of the maintenance update package.

`last_action`

(optional) The update action performed most recently using this maintenance update.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`available_actions`

(optional) The possible actions that can be performed using this maintenance update.

Allowed values are: 'ROLLING_APPLY', 'PRECHECK', 'ROLLBACK'

`update_type`

(required) The type of VM cluster maintenance update.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_details`

(optional) Descriptive text providing additional details about the lifecycle state.

`lifecycle_state`

(optional) The current state of the maintenance update. Dependent on value of `lastAction`.

Allowed values are: 'AVAILABLE', 'SUCCESS', 'IN_PROGRESS', 'FAILED'

`time_released`

(required) The date and time the maintenance update was released.

`version`

(required) The version of the maintenance update package.

- [Database Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BB5A6CAC-78DD-4855-8270-F682E6D823B6)
- [DBMS_CLOUD_OCI_DATABASE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-FBCDC125-DFB0-4F8A-AB8F-54A2D4BFDFDA)
- [DBMS_CLOUD_OCI_DATABASE_ACD_AVM_RESOURCE_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BBFA96B8-5049-4ECB-A172-95885AA5C3C4)
- [DBMS_CLOUD_OCI_DATABASE_ACTIVATE_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-13DC6E8F-1E6C-4B9C-A7F7-06DD1137C12C)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_DB_SERVER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D8F9F27C-5F0A-4B1A-AFFC-447C5BB0BFA6)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_DB_SERVER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-156460AC-9AFF-4E8C-829A-A131ACE0E48D)
- [DBMS_CLOUD_OCI_DATABASE_ADD_VIRTUAL_MACHINE_TO_CLOUD_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2E562297-48E7-4BB0-B81E-BF6D80043808)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-714FF169-FB2D-41F7-A6E2-4256864718F5)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3C0B9B74-C248-403A-B0F3-4222F4B62A01)
- [DBMS_CLOUD_OCI_DATABASE_ADD_VIRTUAL_MACHINE_TO_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8B02D157-826C-4B0C-9E07-03FDBF86B262)
- [DBMS_CLOUD_OCI_DATABASE_APP_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-59B69B69-F6F4-4B67-B61C-3C48CED8A501)
- [DBMS_CLOUD_OCI_DATABASE_APPLICATION_VIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CDD3AB5F-4323-4742-8DC1-02F89FD7CF91)
- [DBMS_CLOUD_OCI_DATABASE_APPLICATION_VIP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6E19143E-CEC2-4060-8559-EF39FE74CD7F)
- [DBMS_CLOUD_OCI_DATABASE_ASSOCIATED_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-145398A7-F238-4F01-91D2-7583899610EE)
- [DBMS_CLOUD_OCI_DATABASE_MOUNT_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A4C1C2C5-B29E-49B9-B324-BBB0DA90ECE8)
- [DBMS_CLOUD_OCI_DATABASE_AUTOMATED_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BBF30288-986C-44A6-9B08-8F50919D60B2)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_KEY_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7779A1EE-EBC1-4E66-8515-9D7F4CF2CCB6)
- [DBMS_CLOUD_OCI_DATABASE_MONTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F9F962C6-DCC3-4360-9EF7-ACFE87C9C537)
- [DBMS_CLOUD_OCI_DATABASE_DAY_OF_WEEK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E1211729-5A6D-44A3-8031-97A74D6E6F02)
- [DBMS_CLOUD_OCI_DATABASE_MONTH_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D9ED4E4E-7EC3-4DFB-A7D9-7D26247F3C0B)
- [DBMS_CLOUD_OCI_DATABASE_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-FCD87FE7-AB18-43ED-AD7E-A3B06E530343)
- [DBMS_CLOUD_OCI_DATABASE_DAY_OF_WEEK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-240DCA3A-869F-4A0B-B0FE-F9C051E29C99)
- [DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_WINDOW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7BC6F84E-872B-4D19-9CBB-C76B9D1AC2CC)
- [DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B55EED48-F3B3-41A1-8D81-495EA154337D)
- [DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8474CB80-E05A-41D7-B8CF-6D7E74B89724)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_BACKUP_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1660D93E-185A-4BA7-8DBB-5CECF1807BA3)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_KEY_HISTORY_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CC14044B-EF54-43AE-A959-E8E59637F6D0)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EC259117-31F1-4D83-BF61-8E5626995E7D)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-42814777-3B44-46E6-971E-4A1FA365EEDB)
- [DBMS_CLOUD_OCI_DATABASE_ACD_AVM_RESOURCE_STATS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-31E81091-5B78-4EF2-9A18-FC155CB07E4C)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_RESOURCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-44CB291B-6DB7-4F45-AFC8-24FF0EA494E0)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-ABF4C439-A011-463B-AED1-256A53BE9C7E)
- [DBMS_CLOUD_OCI_DATABASE_APP_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CCE4F102-A3C6-4E6B-BF09-CAD32D80DCD7)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_CONTAINER_DATABASE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9EB6E019-FEC7-43CC-8462-B7B09F8223DA)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATA_WAREHOUSE_CONNECTION_STRINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F5DCF57C-CFF6-457C-AFD1-1B7EE92196BC)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATA_WAREHOUSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2727A234-D177-463D-A65B-1562F5A9D430)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATA_WAREHOUSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-352E6CE7-BBF4-45D7-9F34-F3F060D062F9)
- [DBMS_CLOUD_OCI_DATABASE_LONG_TERM_BACK_UP_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2283152A-4B31-485D-820E-76F0E86EB2BC)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_BACKUP_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2A7CC61C-A4AA-4427-9124-E2CF788F0AA8)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRING_PROFILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-929C8351-616D-4542-BFF7-E2AF2CEC0772)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRING_PROFILE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-47ECBF44-D362-4753-97BD-E3DDB5D0AA45)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CONNECTION_STRINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-90C08CC1-F01D-4F39-883D-8D482CE47E89)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CONNECTION_URLS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BDC323D8-6577-416C-AE06-8C466E6C1307)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_APEX_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3D0F6198-9930-4E2E-8A0D-66740B9441B1)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_STANDBY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0EBBE964-03D4-430F-B38A-E85D3099F0F7)
- [DBMS_CLOUD_OCI_DATABASE_CUSTOMER_CONTACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A9080AE5-FFF7-4878-B8EB-06434DA1A447)
- [DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4726A90E-B491-44EC-B98F-55A3B9949D89)
- [DBMS_CLOUD_OCI_DATABASE_SCHEDULED_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-61DA89FD-935E-48DF-B7B1-988BEE1E5C16)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_TOOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0517416D-8D15-450E-8B20-D7F83F4E95A3)
- [DBMS_CLOUD_OCI_DATABASE_DISASTER_RECOVERY_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D646FC20-ED4F-4C69-B52D-BF3509E3602A)
- [DBMS_CLOUD_OCI_DATABASE_CUSTOMER_CONTACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1E25A670-7BBF-4E5F-9EED-8E78FB6D8EB0)
- [DBMS_CLOUD_OCI_DATABASE_SCHEDULED_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-31D9EBD4-70B4-4879-BC69-AC5EE9C59516)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_TOOL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F4927D81-E664-4757-A774-E92C2860407A)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-76B52173-ADC2-4B43-AA8C-160A764A7CDE)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3694A06A-A09A-44D6-8198-123F78FE5D7D)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_BACKUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-23F0E1B7-23A0-4087-BE95-D7C3D120C38F)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CHARACTER_SETS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D3C4821B-0260-4223-B6BA-99CFA571E188)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_CONSOLE_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-08409BB3-289A-490E-9EEC-F88F11658B1C)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_DATAGUARD_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B33D9138-0667-4725-9AF3-DB70F09CB3CF)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_MANUAL_REFRESH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B56A682C-1859-454F-A928-FB33A8A77CFB)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F92B77D4-12FE-4751-AC33-1DE3CA9A4A08)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DATABASE_WALLET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B544D7D8-1264-470D-B17C-3B0495FEF15F)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DB_PREVIEW_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A5498EA0-D2CB-450A-BBF8-553869F2108D)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_DB_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9DF21848-D114-456E-BE7D-19688418D830)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7BFE90DF-A09C-43ED-93AE-C74474D0DB7F)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A5BA2E94-76B8-4DE1-9870-8E741CDDAC9D)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-90BD6B41-5601-4E4A-98A2-4FBD54A8E50B)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_PATCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-FEF77C0D-6AD1-4B19-BCF9-30DC4A23C61F)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9926D9E6-06AA-4F01-AA67-C926D2DFF155)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VIRTUAL_MACHINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-378598BB-E7AC-46C1-81D5-F21C364FFB77)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VIRTUAL_MACHINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E526F7E4-69D8-4052-A3F2-8A2EA1226951)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-72C528CB-88D0-4BE9-AFD2-ECB5CD0A4101)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-96C1B552-CF0D-4547-A827-722A3FDE9C76)
- [DBMS_CLOUD_OCI_DATABASE_AVM_ACD_RESOURCE_STATS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-48A0A5FF-C770-4F2A-8A6A-D751423019BA)
- [DBMS_CLOUD_OCI_DATABASE_AVM_ACD_RESOURCE_STATS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DDC6F846-A906-4B72-9B31-02B2BFA8C23E)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_RESOURCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0B3EC504-AFCB-44D5-A2B8-7BC3481ED9ED)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_RESOURCE_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3A6A013F-5F65-4ABD-83AD-C02FC536EBBF)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7587D535-A7B6-4DAD-A29B-977669B93FBF)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-08977090-33E3-4B96-94A9-41E6845AE4E8)
- [DBMS_CLOUD_OCI_DATABASE_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AF8B2F00-9027-4013-BA87-57B478738F57)
- [DBMS_CLOUD_OCI_DATABASE_ASSOCIATED_DATABASE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-97D3FC04-4D07-4575-BB93-21C5F4C054B2)
- [DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-94776688-B1C7-4F2D-896F-7C2AFA9B7F40)
- [DBMS_CLOUD_OCI_DATABASE_BACKUP_DESTINATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A39251BA-4BDC-4BD8-A600-BE28B7B0C445)
- [DBMS_CLOUD_OCI_DATABASE_BACKUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-612C6D49-42ED-49DF-9E8A-F4DEC9A326CF)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_AUTONOMOUS_VM_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6C801BF0-7F88-4E55-93E5-B8130077D95C)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_CLOUD_AUTONOMOUS_VM_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-37229851-6003-481D-9AEF-81309BC45FA5)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_CLOUD_EXADATA_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4B9D0614-3D31-4C95-A105-9A5D4DDC2021)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_CLOUD_VM_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CAD7FD88-0A15-431F-B46D-6F03A4EB906F)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CDA3083E-07C4-407F-92A3-D2BAC4B1D884)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_DATAGUARD_ROLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-098FD4C8-2283-4D4E-BE03-E393AA8A4606)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_DISASTER_RECOVERY_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-887C08FB-69DD-420C-AF4F-EB69D2247248)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_EXADATA_INFRASTRUCTURE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F376D374-990D-4B8A-A814-F7EC95F40EC3)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_KEY_STORE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D1567CA4-E0EB-4AE5-B4A0-C24D10FA87C8)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_KEY_STORE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-61201D96-1BF9-4B7C-A75D-3217D51298C6)
- [DBMS_CLOUD_OCI_DATABASE_CHANGE_VM_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EA5D3ED4-D89E-42FC-A7DE-8462A41DFC9F)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-618C5424-3B87-4E05-B534-EE4415C9AA55)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-43DC1FE6-1D38-45CC-BA7A-E082E0140CFC)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AA22C4F5-693C-4D2E-9577-AD9367761C3D)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EF4D3D2A-9976-4915-BEFE-8E8EEC74BC0E)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_DATABASE_MANAGEMENT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-10888266-2588-4303-AB55-7B983986523C)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_EXADATA_INFRASTRUCTURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-749FAB83-E5F2-40EA-ACB0-94BA4DDCC368)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_EXADATA_INFRASTRUCTURE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C83CB868-776E-4CD8-9B8F-7DB64E01D04C)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-03D5B74E-1323-43AA-B490-FEC21E8FCAB1)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_EXADATA_INFRASTRUCTURE_UNALLOCATED_RESOURCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6F2CBE8E-B6D1-4699-AD98-4BCF92C784D6)
- [DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0080B562-2428-40A3-BE26-A9CB9E101987)
- [DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3608A78F-84A9-4303-B65F-B626124F2480)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_IORM_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B7E8F22F-0339-4F75-AF4A-417968DAFA3B)
- [DBMS_CLOUD_OCI_DATABASE_DATA_COLLECTION_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E3ED79C7-A020-4172-A398-8210E3A91E10)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_VM_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-71B8EA83-5955-44E2-94B2-8994150D1927)
- [DBMS_CLOUD_OCI_DATABASE_CLOUD_VM_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AF4B4EB5-C2C2-4F69-A334-9C0A9964EF42)
- [DBMS_CLOUD_OCI_DATABASE_COMPLETE_EXTERNAL_BACKUP_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1B093050-D672-4B44-A5AA-F4CF1ACB3CC3)
- [DBMS_CLOUD_OCI_DATABASE_COMPUTE_PERFORMANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5B82BDEA-E8DC-460B-AA07-13086D390926)
- [DBMS_CLOUD_OCI_DATABASE_CONFIGURE_AUTONOMOUS_DATABASE_VAULT_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EA763CB8-4D9E-4067-9102-0F96EDF3BF15)
- [DBMS_CLOUD_OCI_DATABASE_CONFIGURE_SAAS_ADMIN_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-617D0E83-9C04-428A-BB2F-0C73678BE0B7)
- [DBMS_CLOUD_OCI_DATABASE_CONSOLE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-469EB0B8-2B91-4503-9CE5-ED1D587B0029)
- [DBMS_CLOUD_OCI_DATABASE_CONSOLE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AC608151-D3A7-4C72-9B62-845ED8FCEDEB)
- [DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EAFE1B0F-1329-4659-91F6-1109E4D30B67)
- [DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-86120AB3-8E73-4F3C-9E77-1F53E22E0AA2)
- [DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CD6CD462-D98A-4751-A983-9F62F8CC90A2)
- [DBMS_CLOUD_OCI_DATABASE_CONSOLE_HISTORY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7D374B2E-DE39-4877-9A57-E9595EB97734)
- [DBMS_CLOUD_OCI_DATABASE_CONVERT_TO_PDB_TARGET_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5C009E15-F404-4E50-A727-E3367D37DD14)
- [DBMS_CLOUD_OCI_DATABASE_CONVERT_TO_PDB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A61EBE6F-15BD-412F-BDC5-A04F3726F417)
- [DBMS_CLOUD_OCI_DATABASE_CONVERT_TO_REGULAR_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9D804F03-0632-45F7-92EB-D10982B43C00)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_APPLICATION_VIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7C403FDD-D8B2-4974-8EB3-37B2ACEF129B)
- [DBMS_CLOUD_OCI_DATABASE_PEER_AUTONOMOUS_CONTAINER_DATABASE_BACKUP_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-502AFEC7-614E-4414-9F19-52EB1DC3F60A)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-FFF39A1D-68F9-45F5-A3B6-667FE73AA34E)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_CONTAINER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-109AC7EB-0FF4-402B-8695-2CA026B09952)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-85D6A48F-6F7B-47DF-A98D-61AB50543B72)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2B2914B5-45A4-48DA-B632-1CD3043066ED)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_CLONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BB11F391-9727-47BD-8394-41CABCC2E0FA)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1FEBD0D3-E0D6-477C-AAB3-23C47D1618E4)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-65134E70-4A87-4D19-9172-743300DCE3D8)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_DATABASE_FROM_BACKUP_TIMESTAMP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8B09E0CE-F2C6-4630-B30D-66CC8937E830)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E2F543C1-88B2-4AED-9F55-6E5619A5D99B)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_BACKUP_DESTINATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-89919E64-BA8A-432C-B9F6-4BE2032BB018)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-76361A5D-DFF4-4543-9194-09ED63C8C907)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B33DA721-5717-4423-9ED5-AD32EAA7F5B7)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CLOUD_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C3232D42-335F-4E15-AFAE-225A9BC555BB)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CLOUD_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CB02E510-3931-460D-8824-5EE30E792214)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CONSOLE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D2A0A1BB-0101-43EE-A3CA-932788D491AA)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CONSOLE_HISTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-808FB2E2-FBB1-4931-822B-4C8F258E1AEC)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CROSS_REGION_AUTONOMOUS_DATABASE_DATA_GUARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-62EF2C09-DA50-4ED0-8588-81AFB21D531C)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_CROSS_REGION_DISASTER_RECOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-66148FF0-EDCD-4797-85F5-32590E395CDB)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-06F04D41-77D5-4DAF-8BF8-7F48D5EBEF0F)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_TO_EXISTING_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9AA90758-59DE-43CB-906B-E60FF6BF395F)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_TO_EXISTING_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-81C44F26-FDB6-439A-8968-8889E452FEAF)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATA_GUARD_ASSOCIATION_WITH_NEW_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1F9F153B-830C-4FA8-A3A9-8B91CCE48B31)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-17B95922-CB0B-4377-8B7B-06400947A170)
- [DBMS_CLOUD_OCI_DATABASE_DB_BACKUP_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-62EE61C5-EAF1-400B-B65F-B5995A3E8D02)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B527BF1D-A8B9-457E-BBB4-583B7BB797C4)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_ANOTHER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-FE4E0544-703D-40DD-8962-C0072DE7241A)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D7F41143-B5A1-45AC-ADCA-A79A0B948047)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AFD4E2F2-D4D8-40AE-B191-0EF6A59229FF)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_FROM_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B4F51E8A-7763-4781-8465-9FE7D2B0127E)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DATABASE_SOFTWARE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-034BA6FA-1330-42D7-8149-7EC5B5272E33)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-13D420E8-0D72-4EED-ADE9-887CF2180088)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BB59DE51-F65C-4C39-A2B2-8835FE0C1889)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-31C83E7E-2C18-48C9-A2A3-7AE3E37022AF)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_FROM_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-282DFEE2-4F34-4936-A25A-9856BCBC1F63)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_FROM_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B8C65FA7-EBFC-4ABA-8AFA-AB69A52AA850)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_DB_SYSTEM_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-03F66D42-9590-4601-B433-2B989F2CBD98)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_DB_SYSTEM_ID_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-43F35F88-CEB3-4A45-927C-CCA83D689462)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_DB_SYSTEM_ID_FROM_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DAD2B739-C957-416D-9096-98C7C0621943)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_VM_CLUSTER_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5D4FF1FF-CA75-4C25-A11E-2A071AF255DB)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_DB_HOME_WITH_VM_CLUSTER_ID_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C4E38763-732F-4B0A-A817-FCC5AF849D0D)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_CONTACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4A67559B-A14B-4E8C-A2C1-720189FCC334)
- [DBMS_CLOUD_OCI_DATABASE_NETWORK_BONDING_MODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B63D6B7F-DC02-4E7E-ACFF-BA2A4CD404F4)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_CONTACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5CA7039F-0556-4E89-8F91-4E21BD4980E0)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-657C7147-7B1B-4BFA-A30A-2ED21C377D00)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_BACKUP_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E86000DD-F310-4C9E-A29E-BCEE5841FA6F)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DAF0D86E-11EF-4B5F-9BB1-0A168FB33A54)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-83B09434-302D-4310-A9AD-08808821B178)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_DATABASE_DETAILS_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CABF9947-4596-48C7-9F7A-BA5928575719)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C81B5CF1-01EA-42E8-9E7B-2E7C8AD6F5A4)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EB11618D-F68A-4D01-B489-88AE1CAC6402)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_MACS_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1B01FC40-A25C-4519-A258-BB06C153ED20)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_NON_CONTAINER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AD9DE632-56A3-428A-820A-F37B5FF4FCD7)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BAAE5BA0-BB5C-4D59-B457-AC11938D4935)
- [DBMS_CLOUD_OCI_DATABASE_KEY_STORE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7DD8CED7-D418-4A1D-91F1-F33D858E0512)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_KEY_STORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7796FAAB-C67A-473F-AD20-96A3D2CB465F)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_MAINTENANCE_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8A7968CE-3371-49CA-84BD-0A9AADFCC31B)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_NFS_BACKUP_DESTINATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2DA8AF04-856D-49FD-9CF6-58ED417387EA)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_NEW_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2B6139A7-BE8B-49A3-9A51-FE5A877AB671)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_ONEOFF_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EB1B3BD5-DA3C-4EBB-A942-80593648D606)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_CREATION_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8C458B67-FEC5-4160-AE23-7E8F84E85AB2)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4DC80381-C27C-4337-968C-050546FD497E)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_FROM_LOCAL_CLONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6AC66FC9-8907-45B0-BD45-474E790DA042)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_FROM_RELOCATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3CBCD883-627E-4B00-9A27-67AFCA4753E7)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_REFRESHABLE_CLONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F2746730-EF6B-4433-A1BA-635EC155A9B0)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_PLUGGABLE_DATABASE_FROM_REMOTE_CLONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-10505AC8-966F-42AC-B4D8-E142495D8085)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_RECOVERY_APPLIANCE_BACKUP_DESTINATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9CA6D649-6E16-4C65-B361-1799889BF4AB)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_REFRESHABLE_AUTONOMOUS_DATABASE_CLONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CA2BF667-FBA7-4A6E-9E08-DD38C805FA06)
- [DBMS_CLOUD_OCI_DATABASE_CREATE_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7D8C3099-1F03-4C7B-BBC9-74810A1BA5EB)
- [DBMS_CLOUD_OCI_DATABASE_DATA_GUARD_ASSOCIATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1D7275C5-E102-4DEC-8FBD-2FB93ECBB156)
- [DBMS_CLOUD_OCI_DATABASE_DATA_GUARD_ASSOCIATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-ABAE278F-7872-471D-AB57-8250E030CF9D)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_STRINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D8B8A66A-0C11-4B60-ACE6-5C78FC8F697B)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-85BD8B8A-46B3-422F-B6B9-EF7B5F53F593)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_CREDENTAILS_BY_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F91A7428-9AC6-4602-8388-BD533AF1A5DB)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CONNECTION_CREDENTIALS_BY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-723DB8FC-602C-4DBE-A3B5-43C77EA31C53)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AE39F988-DC05-4CB8-8A48-D7DDA66BB98B)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_MANAGEMENT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E2C6E3B9-5F77-496A-9D9E-F353CB0D7AE8)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_SOFTWARE_IMAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C557BBC2-D468-499E-ACB3-43B6783099CB)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_SOFTWARE_IMAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5179EF3E-3193-49F6-8097-49FB32A78E74)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_SSL_CONNECTION_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5D714D82-67E6-41F0-BAA4-DF841A8BC00B)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-79BDD016-1878-4A94-838E-D7CBDD77DBEF)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E4CA67CF-EDFC-4EAD-9FFF-577B76B4D815)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_HISTORY_ENTRY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C3CDB7B6-0FAE-48E3-A08A-D73B03C44FCA)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_SOURCE_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BE4EE568-1904-4EDF-A25D-8D92B567727C)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_WITH_DATABASE_SOFTWARE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4773EC46-CD8A-4CB2-A973-CB6C0F22CE50)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_WITH_DB_HOME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6A287AD4-FA66-4A50-B8D3-67B237D8AF8D)
- [DBMS_CLOUD_OCI_DATABASE_DATABASE_UPGRADE_WITH_DB_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2B9CB740-54A6-4423-8EB4-7D3FB43D6988)
- [DBMS_CLOUD_OCI_DATABASE_DB_HOME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EE4F380F-8531-4E9A-827E-DD2AB813E710)
- [DBMS_CLOUD_OCI_DATABASE_DB_HOME_FROM_AGENT_RESOURCE_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3E5C05C0-DE71-4BDE-9B5D-A2E5B540560E)
- [DBMS_CLOUD_OCI_DATABASE_DB_HOME_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A8B4EAC3-623C-459B-97E1-D3E2A11A2764)
- [DBMS_CLOUD_OCI_DATABASE_DB_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-53AE7F00-4427-4AD3-8BCC-32756E743D72)
- [DBMS_CLOUD_OCI_DATABASE_DB_NODE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5D7C1795-A3D4-47CE-9152-254AE4D54EEC)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_PATCHING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-39F14C82-B283-485A-913F-475BC1816BD9)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A30E9BB9-C900-43E1-B760-F40A1BFA8A2C)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B9414549-36EC-4FA2-9E2D-E1B10462B42A)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DA43BC7A-3551-4006-B3AF-0D397E050444)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-881C4816-9BC6-4AFC-925A-6F78108461AC)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-771AF4B0-EC6F-4ED1-93BA-34123AFF16E1)
- [DBMS_CLOUD_OCI_DATABASE_COMPUTE_PERFORMANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-EEC2E70A-9573-4B2A-A286-69B51DBADC5A)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_COMPUTE_PERFORMANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-367794BA-7C96-46C2-B350-BABC8BF3E9D5)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CB205BF0-7752-445D-8320-FEB368249E2F)
- [DBMS_CLOUD_OCI_DATABASE_DISK_PERFORMANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B8870294-18FD-4C73-9408-69F6E0A561BD)
- [DBMS_CLOUD_OCI_DATABASE_STORAGE_PERFORMANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-62215EB8-4897-4DCF-B941-34DEAE089C38)
- [DBMS_CLOUD_OCI_DATABASE_STORAGE_PERFORMANCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-536BA6CC-41A4-4795-ACB9-48174A1479A1)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_STORAGE_PERFORMANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-64EDF83B-04D4-45A8-A439-0E9C3A6871F2)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E8294CDB-4A44-437C-93F5-F06989B1B2D5)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_UPGRADE_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-140AEE15-1C6D-454E-BD7D-15FAA80D603F)
- [DBMS_CLOUD_OCI_DATABASE_DB_SYSTEM_UPGRADE_HISTORY_ENTRY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2BB9244E-C1C0-47D1-AC95-8C71FED83F0C)
- [DBMS_CLOUD_OCI_DATABASE_DB_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2DB1310E-D2F4-4ABA-9816-972862EF5D50)
- [DBMS_CLOUD_OCI_DATABASE_DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0385B94E-36C4-4A19-9DAA-59C510AF728A)
- [DBMS_CLOUD_OCI_DATABASE_DOWNLOAD_ONEOFF_PATCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F7A7E523-7712-4B10-BF32-342A29A19413)
- [DBMS_CLOUD_OCI_DATABASE_DR_SCAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-64397D90-A4AA-467F-BA4A-25059E33B581)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BE02581B-3E07-43A9-B35A-7646C5F920FB)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_CONTAINER_DATABASE_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4D350241-F377-4F5F-830A-DC20391754CE)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_CONTAINER_DATABASE_STACK_MONITORING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-53402C19-3D3E-4119-9C13-60F50E6C9EBF)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_DATABASE_MANAGEMENT_DETAILS_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4F813636-65DC-426F-B818-26395C68CCFE)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_DATABASE_OPERATIONS_INSIGHTS_DETAILS_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-26B29BD3-E6D3-41BA-9F38-A2A965CBA1C2)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_DATABASE_STACK_MONITORING_DETAILS_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D2F2304C-63A6-498E-AE17-CDC62A5046D7)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-24A5578D-172C-44D7-A91D-71B3FBC40D9E)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_OPERATIONS_INSIGHTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DC58B979-EBE0-4206-8A1A-AA38FDB792FE)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_STACK_MONITORING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C89A838D-9A1E-40FE-9B90-FC904365DDE2)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_PLUGGABLE_DATABASE_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0BE921F9-99E9-45C6-A2BD-AE56CCF91493)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_PLUGGABLE_DATABASE_OPERATIONS_INSIGHTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-13B48609-4F9E-4577-B4D8-91A2D291300D)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_EXTERNAL_PLUGGABLE_DATABASE_STACK_MONITORING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CA259619-0E69-4952-BC4C-606F34B94840)
- [DBMS_CLOUD_OCI_DATABASE_ENABLE_PLUGGABLE_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-839E4943-6351-42E1-AA37-E208ADC8A2D6)
- [DBMS_CLOUD_OCI_DATABASE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7C81E96D-DAF7-4BA7-922A-7EFB15D769D4)
- [DBMS_CLOUD_OCI_DATABASE_ESTIMATED_PATCHING_TIME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AF133739-0FD2-4E1A-8170-9D7F8E96D909)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_DB_SYSTEM_MIGRATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-852E59D1-9706-4E16-A09A-A6C2222B2CFA)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_DB_SYSTEM_MIGRATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-65432BF0-164A-4768-BF2E-97D19D3EDF91)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_DB_SYSTEM_MIGRATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1FC571CB-BCEB-479D-8240-4C8EC6C14FF4)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BB71410D-5EB7-492E-A5C8-75BC9A7BE601)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-084621C9-F6DE-494E-970B-F18B1D996AD5)
- [DBMS_CLOUD_OCI_DATABASE_AUTONOMOUS_VM_CLUSTER_RESOURCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3555276D-E84B-4F4A-8B20-D8E8E9A91491)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_INFRASTRUCTURE_UN_ALLOCATED_RESOURCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-575E7356-9E57-4AFD-8FE3-F1BBBEB660B0)
- [DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_UPDATE_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BCC1AA21-2511-43F2-9F85-177B40DFB1B6)
- [DBMS_CLOUD_OCI_DATABASE_DB_IORM_CONFIG_UPDATE_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-43F935B6-F5FE-4A6E-986E-1F31C1B2BFBC)
- [DBMS_CLOUD_OCI_DATABASE_EXADATA_IORM_CONFIG_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-130DD0EC-3C58-4BCE-963F-5D6229F566F9)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_BACKUP_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CF5CB4E8-CD5E-4BAE-A687-FD58384941DB)
- [DBMS_CLOUD_OCI_DATABASE_STACK_MONITORING_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-43115692-58F7-4826-B7FA-1600F51F63F9)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_CONTAINER_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8B3719B8-02B4-4A74-B33B-EF45B931B784)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_CONTAINER_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4451F1DF-331A-413C-A6C0-CEC08028D9D5)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_DATABASE_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0050DC4D-F215-4FCE-8993-F0088FD7BA70)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_DATABASE_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D3ED88B3-499F-4D93-823A-A32884441E0A)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_DATABASE_CONNECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-ED90931D-DB97-4398-B71C-92B437D3996D)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_MACS_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F3B0E595-E071-4CFC-A20B-C19CE36B5F87)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_MACS_CONNECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A25E8FCB-9EF5-4380-8B08-670BB69A5868)
- [DBMS_CLOUD_OCI_DATABASE_OPERATIONS_INSIGHTS_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7CB3EF11-D676-45A2-829F-1FDA3F2B4BCF)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_NON_CONTAINER_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-815F4868-0A8A-40A3-B7E2-6BD687069522)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_NON_CONTAINER_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-370C6F0F-9298-4744-9916-2FD12D1CA3F0)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_PLUGGABLE_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CAAB030C-1E33-49AF-BEF3-338671D146F9)
- [DBMS_CLOUD_OCI_DATABASE_EXTERNAL_PLUGGABLE_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0D9816E0-7E16-48F8-AE46-0FF4F847B7E2)
- [DBMS_CLOUD_OCI_DATABASE_FAILOVER_DATA_GUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1722EA13-494A-428F-A3EC-DC8FEE9E9A3E)
- [DBMS_CLOUD_OCI_DATABASE_FLEX_COMPONENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A6783D95-CD47-4167-946A-42545BB95EAA)
- [DBMS_CLOUD_OCI_DATABASE_FLEX_COMPONENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7E76133D-D97D-47AD-A19A-FE4BC780E79B)
- [DBMS_CLOUD_OCI_DATABASE_FLEX_COMPONENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D55AC5F4-63DF-4649-8A97-07370DDD5791)
- [DBMS_CLOUD_OCI_DATABASE_GENERATE_AUTONOMOUS_DATABASE_WALLET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CF904263-85AE-4ECB-8854-EB60E07B3C1B)
- [DBMS_CLOUD_OCI_DATABASE_INFO_FOR_NETWORK_GEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1928E1EE-ECB5-4069-A148-B4553DBBC3AD)
- [DBMS_CLOUD_OCI_DATABASE_INFO_FOR_NETWORK_GEN_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E5FEDEF7-6DFB-4107-AB4E-2342429FBC5F)
- [DBMS_CLOUD_OCI_DATABASE_GENERATE_RECOMMENDED_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0113BEFC-FD4C-44F5-ACA2-66A3E4015E25)
- [DBMS_CLOUD_OCI_DATABASE_GI_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AFA35EBD-17B5-4BB0-95D8-7A342F3F8BE7)
- [DBMS_CLOUD_OCI_DATABASE_INFRASTRUCTURE_TARGET_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1B679BF4-E256-4C05-87F3-1DD192443FA0)
- [DBMS_CLOUD_OCI_DATABASE_INFRASTRUCTURE_TARGET_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9EE04BFB-D1B6-469F-9022-0A88CB3C82E5)
- [DBMS_CLOUD_OCI_DATABASE_KEY_STORE_ASSOCIATED_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6878D2FD-9357-42D3-B584-104BE11B27CB)
- [DBMS_CLOUD_OCI_DATABASE_KEY_STORE_ASSOCIATED_DATABASE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-94C3D2FE-CABE-4E99-91FF-55FFD7514E19)
- [DBMS_CLOUD_OCI_DATABASE_KEY_STORE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E13199B2-6F5D-4478-BCA3-245923BE30FD)
- [DBMS_CLOUD_OCI_DATABASE_KEY_STORE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1BB5B250-8912-4D7C-BA60-4C51E1FA4012)
- [DBMS_CLOUD_OCI_DATABASE_KEY_STORE_TYPE_FROM_ORACLE_KEY_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2D1D3205-8A51-4890-953F-7C0BE9E07E78)
- [DBMS_CLOUD_OCI_DATABASE_LAUNCH_AUTONOMOUS_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-7A8E3B19-D780-42CD-94B3-F3B231B7DB2F)
- [DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-347EDD18-80E9-4945-9114-EAE782A2614E)
- [DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DED774C9-796C-4795-8513-CD757112CE1C)
- [DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-56E1588E-400D-4A13-A13E-A413EAC541B6)
- [DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_FROM_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F866CD5E-D5DB-43DF-80A4-2F251310EB1F)
- [DBMS_CLOUD_OCI_DATABASE_LAUNCH_DB_SYSTEM_FROM_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4E6DBDFE-B24C-44D0-8EBE-DB7DFB9C2A74)
- [DBMS_CLOUD_OCI_DATABASE_LOCAL_CLONE_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2A98C4E5-4757-4A02-A98A-39748116F00D)
- [DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-252DEA15-C87F-4D0F-B952-2541A4E6A5B2)
- [DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1BD94684-9A3E-41A8-905D-54B06933B667)
- [DBMS_CLOUD_OCI_DATABASE_DB_SERVER_HISTORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-04AC2BA4-D34C-4E7C-8F81-14473B513C4A)
- [DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_HISTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-568DBEE5-4606-4340-87F9-593B261B6BD5)
- [DBMS_CLOUD_OCI_DATABASE_MAINTENANCE_RUN_HISTORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9452813A-5ADD-40E2-8729-467744D79332)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATE_VAULT_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AED15C6C-6DA4-4170-AE3D-885099A27D8C)
- [DBMS_CLOUD_OCI_DATABASE_MODIFY_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-82D7B21C-7D3A-4890-86AF-F1C0C39F56EB)
- [DBMS_CLOUD_OCI_DATABASE_MODIFY_PLUGGABLE_DATABASE_MANAGEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-531A049F-55EA-435A-B369-C57571C80AB8)
- [DBMS_CLOUD_OCI_DATABASE_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3DE60481-9DD9-4684-9FB3-A6407076EBC3)
- [DBMS_CLOUD_OCI_DATABASE_WORKLOAD_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BBD87292-9827-4E94-93A1-7E04812283FD)
- [DBMS_CLOUD_OCI_DATABASE_OCP_US_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2E26F031-605D-4133-928D-2C96DFE1750B)
- [DBMS_CLOUD_OCI_DATABASE_ONEOFF_PATCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DF0CB8E4-07F1-4039-A2FF-87D35E3BC9DB)
- [DBMS_CLOUD_OCI_DATABASE_ONEOFF_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8EDF0DD9-94FA-40CD-B8D6-CBB46262E82C)
- [DBMS_CLOUD_OCI_DATABASE_PATCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F3FE26C4-1381-4AC6-8E97-3148DCDC856C)
- [DBMS_CLOUD_OCI_DATABASE_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9EAB7342-6E77-4251-8A50-5D7645EF3B5C)
- [DBMS_CLOUD_OCI_DATABASE_PATCH_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-AF4071B1-D931-4DF8-80FB-2D212D6D1710)
- [DBMS_CLOUD_OCI_DATABASE_PATCH_HISTORY_ENTRY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BCCF9644-D80D-40C6-916A-CD1720DF2D4F)
- [DBMS_CLOUD_OCI_DATABASE_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F78407B8-D7DB-4F47-ACEE-39FFD20020E5)
- [DBMS_CLOUD_OCI_DATABASE_PDB_CONVERSION_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C0E560C1-BEAD-4778-922A-BBCA27B513F5)
- [DBMS_CLOUD_OCI_DATABASE_PDB_CONVERSION_HISTORY_ENTRY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2E5803BE-391D-463E-BE00-C986448914D2)
- [DBMS_CLOUD_OCI_DATABASE_PDB_CONVERSION_TO_NEW_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-24EFF51A-DC7C-42E4-81DE-44B991DC0C3A)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_CONNECTION_STRINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-13D6CBED-9591-4E1A-BC6E-9D9345E60798)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_MANAGEMENT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-34F0B873-9CBE-4CB7-94FE-9362DB951F92)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_REFRESHABLE_CLONE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1A0D7623-2CAE-4F8E-B8BD-16492121C648)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_NODE_LEVEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6C122F6F-0666-4DE6-8294-76948364A4D6)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_NODE_LEVEL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-021C7BDE-5BE0-44F2-A9A6-69BA92D03D6E)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8FDF6D85-1300-4503-9438-83AB506B8FD4)
- [DBMS_CLOUD_OCI_DATABASE_PLUGGABLE_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-CDEB2214-4D16-46D1-83E8-50361907FB5D)
- [DBMS_CLOUD_OCI_DATABASE_REFRESHABLE_CLONE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A575959A-124F-40C9-9239-C4C398DB165D)
- [DBMS_CLOUD_OCI_DATABASE_REFRESHABLE_CLONE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B0D674DB-C841-4534-8DF3-B6AD34AE5BD2)
- [DBMS_CLOUD_OCI_DATABASE_REFRESHABLE_CLONE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-31A89666-7519-47C8-9720-5B94EA66B4C5)
- [DBMS_CLOUD_OCI_DATABASE_REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-85957893-C51D-41E3-BF0F-3F71963D260F)
- [DBMS_CLOUD_OCI_DATABASE_REINSTATE_DATA_GUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E7EB26CA-10C3-403C-A34E-40245FE884EF)
- [DBMS_CLOUD_OCI_DATABASE_REMOTE_CLONE_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E44A5FDF-345E-4FD5-9B49-D8204E192FE6)
- [DBMS_CLOUD_OCI_DATABASE_REMOVE_VIRTUAL_MACHINE_FROM_CLOUD_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-91AE94E8-C71E-458E-8873-B2A62248AE40)
- [DBMS_CLOUD_OCI_DATABASE_REMOVE_VIRTUAL_MACHINE_FROM_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-618E575C-71D3-4E0A-810D-403EE93385EE)
- [DBMS_CLOUD_OCI_DATABASE_NODE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2A76BC14-AFDB-4B33-85E1-6D6D326B7B2E)
- [DBMS_CLOUD_OCI_DATABASE_VM_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-17D3CAE3-0E04-40B6-9656-E85799FAE71F)
- [DBMS_CLOUD_OCI_DATABASE_VM_NETWORK_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F521D208-1497-4F0B-889A-5207594946F6)
- [DBMS_CLOUD_OCI_DATABASE_RESIZE_VM_CLUSTER_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A4129BCB-F56A-47DA-A87E-AA835523782B)
- [DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F1EBB76F-2430-4816-AC78-1025C4C10308)
- [DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SHAPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-08F05401-050F-4F63-8E99-2BD919BF3288)
- [DBMS_CLOUD_OCI_DATABASE_RESOURCE_POOL_SHAPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-57BDF381-A18F-4ADB-9707-19A388A82B9B)
- [DBMS_CLOUD_OCI_DATABASE_RESTORE_AUTONOMOUS_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-12C4258C-8ECA-4E22-B9C5-2320D5FFB777)
- [DBMS_CLOUD_OCI_DATABASE_RESTORE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5CB020E3-328B-4805-B2DF-3C3C21D80579)
- [DBMS_CLOUD_OCI_DATABASE_ROTATE_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4E2F06C5-BD25-4DE6-BC54-73EF937C74EC)
- [DBMS_CLOUD_OCI_DATABASE_ROTATE_AUTONOMOUS_VM_CLUSTER_SSL_CERTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-DA2F6335-13A4-4797-87D9-D880AE8F019B)
- [DBMS_CLOUD_OCI_DATABASE_ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-66B41581-7444-4A8C-BA49-64DAA12D616D)
- [DBMS_CLOUD_OCI_DATABASE_ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_SSL_CERTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F04B2DDC-0C73-43A3-AF40-45B623CE03A8)
- [DBMS_CLOUD_OCI_DATABASE_SAAS_ADMIN_USER_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F291F141-9011-4062-A9F2-4EA0A3D25A7C)
- [DBMS_CLOUD_OCI_DATABASE_SAAS_ADMIN_USER_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-97BFB33C-7426-4411-B822-48522CC6A49F)
- [DBMS_CLOUD_OCI_DATABASE_SCAN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4C1279B6-97B8-4BF5-93A2-8D3C68CB5C0F)
- [DBMS_CLOUD_OCI_DATABASE_SELF_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6E96ABF4-B074-4C47-B978-48FE1E0BB3BD)
- [DBMS_CLOUD_OCI_DATABASE_SWITCHOVER_DATA_GUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5B2508FF-65DA-46E0-B4BD-1955336126EC)
- [DBMS_CLOUD_OCI_DATABASE_SYSTEM_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0A1F5BAD-643B-4A89-B73B-0C3BCD498EB9)
- [DBMS_CLOUD_OCI_DATABASE_SYSTEM_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B68BF656-E793-468D-B52A-665AE9D1D10A)
- [DBMS_CLOUD_OCI_DATABASE_SYSTEM_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-4519DA64-87B4-4F0C-86CD-122EB9323018)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F97B8DBF-F682-40F4-9640-84034CAC2716)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_CONTAINER_DATABASE_DATA_GUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BAE397DD-16A1-4FB0-92D7-766A5FBB8B6F)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_CONTAINER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-BBC3B8C8-D658-4861-AC1B-6090EA5D167D)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_DATABASE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-8B25793B-5A62-4582-8531-F7201AC6C23B)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0C5E7EBF-C33C-4C79-927C-0DF83D9F96BE)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_DATABASE_WALLET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2EE744AF-B2CC-4D67-B0CF-B1E42E562EDF)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E33C7A08-ACB9-461A-83F7-4B322B41B395)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5F626747-B555-484E-9FCF-7D0A6334E8CA)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_BACKUP_DESTINATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-57A0FD00-86E4-460D-8109-5B8935722EEA)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_CLOUD_AUTONOMOUS_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-03CC9B8B-D573-4A7C-8AE3-997DF2E012F2)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_CLOUD_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F2F9FE37-C762-4C09-9D5B-0A3CA3E8ECEE)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C8F07D78-BF04-4E2E-94DD-2AD60BFA635E)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_CLOUD_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0D734C18-1217-4408-918E-625B8C8B0F64)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_CONSOLE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2A513DF9-57D9-4903-BA28-518C48150BF3)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_CONSOLE_HISTORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-16B497D8-5B20-4F3D-909F-C665CF062414)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DATA_GUARD_ASSOCIATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-E3BD6266-8079-4C29-89BA-FEE8660DA741)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-05E2E726-89EF-40F3-87ED-BD83CFCD1D0C)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DATABASE_SOFTWARE_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-13715D18-1790-421B-8E2E-2EB7B4075225)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DB_HOME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0F454E33-589A-4C54-BDA2-3934A7493FBF)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DB_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F54C963F-2615-4ACE-BE56-ECCF17CD0952)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A7E0DBCB-B7EA-451B-A1E0-731446B09AA4)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXADATA_INFRASTRUCTURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-247D6790-745F-4186-8990-12EFEA8F5435)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_CONTAINER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-B3C01113-310A-4146-8D67-519114583448)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_DATABASE_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0609943B-3A03-40EE-B39D-9666F790FECB)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_DATABASE_DETAILS_BASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-C7E8913E-83A5-44CA-829A-5DB482E993E7)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_MACS_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D9307EA5-81C0-4D31-9ABE-B81C720E3C5A)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_NON_CONTAINER_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A0468237-9088-4489-99E1-DC0D5A4FD389)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-D964E75D-80B2-455D-9122-AF64803FCCC5)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-290421F5-ECFB-4E42-8EC6-16B1B8A209C1)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_HISTORY_ENTRY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3398AE53-5647-44E3-AF8C-8003B8F19C69)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_KEY_STORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A960D406-3D39-4183-ABFF-D7415F6D84FF)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_MAINTENANCE_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-3F819C26-2E2D-400D-B741-194967DF8A87)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_ONEOFF_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-23776565-B0DA-483B-B7C7-AED4E064E0C8)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_PLUGGABLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1231977B-DA3F-4FB0-8744-E4F9EC75B7D9)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-0F28D4DB-32C1-4E9C-8BB0-97FAC25920DC)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6FAEC538-82B5-4B85-9B82-016BC73E575F)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_VM_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1F4D879B-AF58-4A59-A343-428A11AB317E)
- [DBMS_CLOUD_OCI_DATABASE_SCAN_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-149A3430-A159-429C-9EE5-0AE6CFE361B7)
- [DBMS_CLOUD_OCI_DATABASE_DR_SCAN_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-9145F05C-463A-4C37-A323-3D7417B99F56)
- [DBMS_CLOUD_OCI_DATABASE_UPDATE_VM_CLUSTER_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-837688CD-9B66-4CF8-BDDA-CF600BEB7F84)
- [DBMS_CLOUD_OCI_DATABASE_UPGRADE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-384F3DBA-CAD3-4073-B566-805E25ECFA57)
- [DBMS_CLOUD_OCI_DATABASE_UPGRADE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-6480E33C-05B8-42DD-B71C-0FDC4F297FFC)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-37BB3673-1D4E-467B-8ACD-DA03AB3A7313)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_NETWORK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-00610E00-F229-4E03-8BC1-BDE10790BAA6)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-40DAB0B3-E909-4DEB-ABAD-7921AFDF36A8)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_NETWORK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-1A31A70B-AE82-442A-B1ED-7DC95EABACCE)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-A431076C-6B85-4155-9F23-39E34ADD3894)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-5A541A7A-F358-4734-A4EC-943F48999D5F)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_HISTORY_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-F510E0D7-A381-4325-B173-719C8D093A62)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_HISTORY_ENTRY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-2B1996E4-ADFF-4FF5-95D4-2A92DAF6F783)
- [DBMS_CLOUD_OCI_DATABASE_VM_CLUSTER_UPDATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_t.html#ADSDK-GUID-583DD1B7-CDF3-45B5-8051-45F1CFF8FD8B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
