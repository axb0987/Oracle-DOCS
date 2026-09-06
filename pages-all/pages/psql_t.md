# PSQL Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#dcoc-content-body)

## PSQL Common Types

### DBMS_CLOUD_OCI_PSQL_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_DETAILS_T Type

Information about the database system associated with a backup.

Syntax
```

```

Fields

Field Description

`system_type`

(required) Type of the database system.

`db_version`

(required) The major and minor versions of the database system software.

### DBMS_CLOUD_OCI_PSQL_BACKUP_T Type

Database system backup information.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup.

`display_name`

(required) A user-friendly display name for the backup. Avoid entering confidential information.

`description`

(optional) A description for the backup.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the backup.

`source_type`

(optional) Specifies whether the backup was created manually, or by a management policy.

Allowed values are: 'SCHEDULED', 'MANUAL'

`time_created`

(required) The date and time the backup was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the backup was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the backup.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`retention_period`

(optional) Backup retention period in days.

`backup_size`

(required) The size of the backup, in gigabytes.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup's source database system.

`db_system_details`

(required)

`last_accepted_request_token`

(optional) lastAcceptedRequestToken from MP.

`last_completed_request_token`

(optional) lastCompletedRequestToken from MP.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_PSQL_BACKUP_SUMMARY_T Type

Summary information for a backup.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the backup. Immutable on creation.

`display_name`

(required) A user-friendly display name for the backup. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the backup.

`time_created`

(required) The date and time the backup was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the backup was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the backup.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`source_type`

(optional) Specifies whether the backup was created manually, or by a management policy.

`backup_size`

(optional) The size of the backup, in gigabytes.

`db_system_id`

(optional) The backup's source database system's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`retention_period`

(optional) Backup retention period in days.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_PSQL_BACKUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_psql_backup_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_BACKUP_COLLECTION_T Type

Results of a backup search. Contains the BackupSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of backups.

### DBMS_CLOUD_OCI_PSQL_BACKUP_POLICY_T Type

PostgreSQL database system backup policy.

Syntax
```

```

Fields

Field Description

`kind`

(optional) The kind of backup policy.

Allowed values are: 'DAILY', 'WEEKLY', 'MONTHLY', 'NONE'

`retention_days`

(optional) How many days the data should be stored after the database system deletion.

### DBMS_CLOUD_OCI_PSQL_SOURCE_DETAILS_T Type

The source used to restore the database system.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source descriminator.

Allowed values are: 'BACKUP', 'NONE'

### DBMS_CLOUD_OCI_PSQL_BACKUP_SOURCE_DETAILS_T Type

Restoring to a new database system from the backup. The database system details that are part of the CreateDbSystem request are not required, but if present will override the details from the backup's database system snapshot.

Syntax
```

```

`dbms_cloud_oci_psql_backup_source_details_t`is a subtype of the`dbms_cloud_oci_psql_source_details_t`type.

Fields

Field Description

`backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database system backup.

`is_having_restore_config_overrides`

(optional) Deprecated. Don't use.

### DBMS_CLOUD_OCI_PSQL_CHANGE_BACKUP_COMPARTMENT_DETAILS_T Type

The information used to move a backup to a different compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the backup will be moved.

### DBMS_CLOUD_OCI_PSQL_CHANGE_CONFIGURATION_COMPARTMENT_DETAILS_T Type

The information to move a configuration to a different compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the configuration will be moved.

### DBMS_CLOUD_OCI_PSQL_CHANGE_DB_SYSTEM_COMPARTMENT_DETAILS_T Type

Change database system compartment operation details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the database system should be moved.

### DBMS_CLOUD_OCI_PSQL_CONFIG_OVERRIDES_T Type

Configuration overrides for a PostgreSQL instance.

Syntax
```

```

Fields

Field Description

`config_key`

(required) Configuration variable name.

`overriden_config_value`

(required) User-selected variable value.

### DBMS_CLOUD_OCI_PSQL_CONFIG_PARAMS_T Type

Database configuration.

Syntax
```

```

Fields

Field Description

`config_key`

(required) The configuration variable name.

`default_config_value`

(required) Default value for the configuration variable.

`overriden_config_value`

(optional) User-selected configuration variable value.

`allowed_values`

(required) Range or list of allowed values.

`is_restart_required`

(required) If true, modifying this configuration value will require a restart of the database.

`data_type`

(required) Data type of the variable.

`is_overridable`

(required) Whether the value can be overridden or not.

`description`

(required) Details about the PostgreSQL parameter.

### DBMS_CLOUD_OCI_PSQL_CONFIG_PARAMS_TBL Type

Nested table type of dbms_cloud_oci_psql_config_params_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_CONFIGURATION_DETAILS_T Type

List of configuration details.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ConfigParms object.

### DBMS_CLOUD_OCI_PSQL_CONFIGURATION_T Type

PostgreSQL configuration for a database system.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the configuration. Immutable on creation.

`display_name`

(required) A user-friendly display name for the configuration. Avoid entering confidential information.

`description`

(optional) A description for the configuration.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the configuration.

`time_created`

(required) The date and time that the configuration was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the configuration.

Allowed values are: 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`shape`

(required) The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`

`instance_ocpu_count`

(required) CPU core count.

`instance_memory_size_in_g_bs`

(required) Memory size in gigabytes with 1GB increment.

`db_version`

(required) Version of the PostgreSQL database.

`configuration_details`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_PSQL_CONFIGURATION_SUMMARY_T Type

Summary of the configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration. Immutable on creation.

`display_name`

(required) A user-friendly display name for the configuration. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the configuration.

`time_created`

(required) The date and time the configuration was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the configuration.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`shape`

(required) The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`

`db_version`

(required) Version of the PostgreSQL database.

`instance_ocpu_count`

(required) CPU core count.

`instance_memory_size_in_g_bs`

(required) Memory size in gigabytes with 1GB increment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_PSQL_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_psql_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_CONFIGURATION_COLLECTION_T Type

Results of a configuration search. Contains the ConfigurationSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of configurations.

### DBMS_CLOUD_OCI_PSQL_ENDPOINT_T Type

Information about the database instance node endpoint.

Syntax
```

```

Fields

Field Description

`fqdn`

(required) The FQDN of the endpoint.

`ip_address`

(required) The IP address of the endpoint.

`port`

(required) The port address of the endpoint.

### DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_ENDPOINT_T Type

The database instance node endpoint information.

Syntax
```

```

Fields

Field Description

`db_instance_id`

(required) Unique identifier of the database instance node.

`endpoint`

(required)

### DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_ENDPOINT_TBL Type

Nested table type of dbms_cloud_oci_psql_db_instance_endpoint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_CONNECTION_DETAILS_T Type

Database system connection information. Used to connect to PostgreSQL instance(s).

Syntax
```

```

Fields

Field Description

`ca_certificate`

(required) The CA certificate to be used by the PosgreSQL client to connect to the database. The CA certificate is used to authenticate the server identity. It is issued by PostgreSQL Service Private CA.

`primary_db_endpoint`

(required)

`instance_endpoints`

(required) The list of database instance node endpoints in the database system.

### DBMS_CLOUD_OCI_PSQL_CREATE_BACKUP_DETAILS_T Type

The information to create a new backup.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name for the backup. Avoid entering confidential information.

`description`

(optional) A description for the backup.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the backup.

`db_system_id`

(required) The ID of the database system.

`retention_period`

(optional) Backup retention period in days.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_PSQL_CONFIG_OVERRIDES_TBL Type

Nested table type of dbms_cloud_oci_psql_config_overrides_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_DB_CONFIGURATION_OVERRIDE_COLLECTION_T Type

Configuration overrides for a PostgreSQL instance.

Syntax
```

```

Fields

Field Description

`items`

(required) List of configuration overridden values.

### DBMS_CLOUD_OCI_PSQL_CREATE_CONFIGURATION_DETAILS_T Type

The information to create a new configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name for the configuration. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the configuration.

`description`

(optional) Details about the configuration set.

`shape`

(required) The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`

`db_version`

(required) Version of the PostgreSQL database.

`instance_ocpu_count`

(required) CPU core count.

`instance_memory_size_in_g_bs`

(required) Memory size in gigabytes with 1GB increment.

`db_configuration_overrides`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_PSQL_CREATE_DB_INSTANCE_DETAILS_T Type

Information about the new database instance node.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of the database instance node. Avoid entering confidential information.

`description`

(optional) A user-provided description of the database instance node.

`private_ip`

(optional) Private IP in customer subnet that will be assigned to the database instance node. This value is optional. If the IP is not provided, the IP will be chosen from the available IP addresses in the specified subnet.

### DBMS_CLOUD_OCI_PSQL_STORAGE_DETAILS_T Type

Storage details of the database system.

Syntax
```

```

Fields

Field Description

`system_type`

(required) Type of the database system.

`is_regionally_durable`

(required) Specifies if the block volume used for the database system is regional or AD-local. If not specified, it will be set to false. If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified. If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.

`availability_domain`

(optional) Specifies the availability domain of AD-local storage. If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified. If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.

### DBMS_CLOUD_OCI_PSQL_PASSWORD_DETAILS_T Type

Details for the database system password. Password can be passed as `VaultSecretPasswordDetails` or `PlainTextPasswordDetails`.

Syntax
```

```

Fields

Field Description

`password_type`

(required) The password type.

Allowed values are: 'PLAIN_TEXT', 'VAULT_SECRET'

### DBMS_CLOUD_OCI_PSQL_CREDENTIALS_T Type

Initial database system credentials that the database system will be provisioned with. The password details are not visible on any subsequent operation, such as GET /dbSystems/{dbSystemId}.

Syntax
```

```

Fields

Field Description

`username`

(required) The database system administrator username.

`password_details`

(required)

### DBMS_CLOUD_OCI_PSQL_NETWORK_DETAILS_T Type

Network details for the database system.

Syntax
```

```

Fields

Field Description

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the customer subnet associated with the database system.

`primary_db_endpoint_private_ip`

(optional) Private IP in customer subnet. The value is optional. If the IP is not provided, the IP will be chosen from the available IP addresses from the specified subnet.

`nsg_ids`

(optional) List of customer Network Security Group[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with the database system.

### DBMS_CLOUD_OCI_PSQL_MANAGEMENT_POLICY_DETAILS_T Type

PostgreSQL database system management policy update details.

Syntax
```

```

Fields

Field Description

`maintenance_window_start`

(optional) The start of the maintenance window.

`backup_policy`

(optional)

### DBMS_CLOUD_OCI_PSQL_CREATE_DB_INSTANCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_psql_create_db_instance_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_CREATE_DB_SYSTEM_DETAILS_T Type

The information about new database system.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly display name for the database system. Avoid entering confidential information.

`description`

(optional) A user-provided description of a database system.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the database system.

`system_type`

(optional) Type of the database system.

`db_version`

(required) Version of database system software.

`config_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration associated with the database system.

`storage_details`

(required)

`shape`

(required) The name of the shape for the database instance node. Use the /shapes API for accepted shapes. Example: `VM.Standard.E4.Flex`

`instance_ocpu_count`

(optional) The total number of OCPUs available to each database instance node.

`instance_memory_size_in_g_bs`

(optional) The total amount of memory available to each database instance node, in gigabytes.

`instance_count`

(optional) Count of database instances nodes to be created in the database system.

`instances_details`

(optional) Details of database instances nodes to be created. This parameter is optional. If specified, its size must match `instanceCount`.

`credentials`

(optional)

`network_details`

(required)

`management_policy`

(optional)

`source`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_PSQL_DAILY_BACKUP_POLICY_T Type

Daily backup policy.

Syntax
```

```

`dbms_cloud_oci_psql_daily_backup_policy_t`is a subtype of the`dbms_cloud_oci_psql_backup_policy_t`type.

Fields

Field Description

`backup_start`

(required) Hour of the day when the backup starts.

### DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_T Type

Information about a database instance node.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the database instance node. Immutable on creation.

`display_name`

(optional) A user-friendly display name for the database instance node. Avoid entering confidential information.

`description`

(optional) Description of the database instance node.

`availability_domain`

(required) The availability domain in which the database instance node is located.

`lifecycle_state`

(required) The current state of the database instance node.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`time_created`

(required) The date and time that the database instance node was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time that the database instance node was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_PSQL_MANAGEMENT_POLICY_T Type

PostgreSQL database system management policy.

Syntax
```

```

Fields

Field Description

`maintenance_window_start`

(required) The start of the maintenance window.

`backup_policy`

(required)

### DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_TBL Type

Nested table type of dbms_cloud_oci_psql_db_instance_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_T Type

Information about a database system.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the database system. Immutable on creation.

`display_name`

(required) A user-friendly display name for the database system. Avoid entering confidential information.

`description`

(optional) A description of the database system.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the database system.

`time_created`

(required) The date and time that the database system was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time that the database system was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the database system.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`admin_username`

(optional) The database system administrator username.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`system_type`

(required) Type of the database system.

Allowed values are: 'OCI_OPTIMIZED_STORAGE'

`db_version`

(required) The major and minor versions of the database system software.

`config_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration associated with the database system.

`shape`

(required) The name of the shape for the database instance. Example: `VM.Standard.E4.Flex`

`instance_ocpu_count`

(required) The total number of OCPUs available to each database instance node.

`instance_memory_size_in_g_bs`

(required) The total amount of memory available to each database instance node, in gigabytes.

`instance_count`

(optional) Count of instances, or nodes, in the database system.

`instances`

(optional) The list of instances, or nodes, in the database system.

`storage_details`

(required)

`network_details`

(required)

`management_policy`

(required)

`source`

(optional)

### DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_SUMMARY_T Type

Summary information about a database system.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the database system. Immutable on creation.

`display_name`

(required) A user-friendly display name for the database system. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the database system.

`time_created`

(required) The date and time that the database system was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time that the database system was updated, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the database system.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`system_type`

(required) Type of the database system.

`instance_count`

(required) Count of database instances, or nodes, in the database system.

`shape`

(optional) The name of the shape for the database instance node. Example: `VM.Standard.E4.Flex`

`instance_ocpu_count`

(required) The total number of OCPUs available to each database instance node.

`instance_memory_size_in_g_bs`

(required) The total amount of memory available to each database instance node, in gigabytes.

`db_version`

(required) Version of database system software.

`config_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration associated with the database system.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_psql_db_system_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_COLLECTION_T Type

Results of a database system search. Contains both DbSystemSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of database systems.

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIG_PARAMS_T Type

Default database configuration.

Syntax
```

```

Fields

Field Description

`config_key`

(required) The configuration variable name.

`default_config_value`

(required) Default value for the variable.

`allowed_values`

(required) Range or list of allowed values.

`is_restart_required`

(required) If true, modifying this configuration value will require a restart.

`data_type`

(required) Data type of the variable.

`is_overridable`

(required) Whether the value can be overridden or not.

`description`

(required) Details about the PostgreSQL variable.

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIG_PARAMS_TBL Type

Nested table type of dbms_cloud_oci_psql_default_config_params_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_DETAILS_T Type

List of default configuration values for databases.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ConfigParms object.

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_T Type

Default configurations for PostgreSQL database systems.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the configuration.

`display_name`

(required) A user-friendly display name for the configuration.

`description`

(optional) A description for the configuration.

`time_created`

(required) The date and time that the configuration was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the configuration.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`shape`

(required) The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`

`instance_ocpu_count`

(required) CPU core count. Minimum value is 1.

`instance_memory_size_in_g_bs`

(required) Memory size in gigabytes with 1GB increment.

`db_version`

(required) Version of the PostgreSQL database.

`configuration_details`

(required)

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_SUMMARY_T Type

Summary of the configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) A unique identifier for the configuration.

`display_name`

(required) A user-friendly display name for the configuration.

`time_created`

(required) The date and time that the configuration was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state of the configuration.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`shape`

(required) The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`

`db_version`

(required) Version of the PostgreSQL database.

`instance_ocpu_count`

(required) CPU core count. Minimum value is 1.

`instance_memory_size_in_g_bs`

(required) Memory size in gigabytes with 1GB increment.

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_psql_default_configuration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_COLLECTION_T Type

Results of a configuration search. Contains the ConfigurationSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of configurations.

### DBMS_CLOUD_OCI_PSQL_ERROR_T Type

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

### DBMS_CLOUD_OCI_PSQL_FAILOVER_DB_SYSTEM_DETAILS_T Type

Database system failover information.

Syntax
```

```

Fields

Field Description

`ad`

(optional) The preferred AD for regions with three availability domains. This parameter is optional. If not set, the AD will be chosen based on availability.

`db_instance_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database instance node. This parameter is optional. If not set, an existing database instance node will be chosen based on availability.

### DBMS_CLOUD_OCI_PSQL_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_MONTHLY_BACKUP_POLICY_T Type

Monthly backup policy.

Syntax
```

```

`dbms_cloud_oci_psql_monthly_backup_policy_t`is a subtype of the`dbms_cloud_oci_psql_backup_policy_t`type.

Fields

Field Description

`backup_start`

(required) Hour of the day when backup starts.

`days_of_the_month`

(required) Day of the month when the backup should start. To ensure that the backup runs monthly, the latest day of the month that you can use to schedule a backup is the the 28th day.

### DBMS_CLOUD_OCI_PSQL_NONE_BACKUP_POLICY_T Type

No backup policy.

Syntax
```

```

`dbms_cloud_oci_psql_none_backup_policy_t`is a subtype of the`dbms_cloud_oci_psql_backup_policy_t`type.

### DBMS_CLOUD_OCI_PSQL_NONE_SOURCE_DETAILS_T Type

This is used to create new database system or update without restoring from backup.

Syntax
```

```

`dbms_cloud_oci_psql_none_source_details_t`is a subtype of the`dbms_cloud_oci_psql_source_details_t`type.

### DBMS_CLOUD_OCI_PSQL_OCI_OPTIMIZED_STORAGE_DETAILS_T Type

Storage details of the database system.

Syntax
```

```

`dbms_cloud_oci_psql_oci_optimized_storage_details_t`is a subtype of the`dbms_cloud_oci_psql_storage_details_t`type.

Fields

Field Description

`iops`

(optional) Guaranteed input/output storage requests per second (IOPS) available to the database system.

### DBMS_CLOUD_OCI_PSQL_PATCH_INSTRUCTION_T Type

A single instruction to be included as part of Patch request content.

Syntax
```

```

Fields

Field Description

`operation`

(required)

Allowed values are: 'REQUIRE', 'PROHIBIT', 'REPLACE', 'INSERT', 'REMOVE', 'MOVE', 'MERGE'

`selection`

(required) The set of values to which the operation applies as a[JMESPath expression](https://jmespath.org/specification.html)for evaluation against the context resource. An operation fails if the selection yields an exception, except as otherwise specified. Note that comparisons involving non-primitive values (objects or arrays) are not supported and will always evaluate to false.

### DBMS_CLOUD_OCI_PSQL_PATCH_INSTRUCTION_TBL Type

Nested table type of dbms_cloud_oci_psql_patch_instruction_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_PATCH_DB_SYSTEM_DETAILS_T Type

For adding read replica database instances, the operation is INSERT and value object to specify is #/definitions/CreateDbInstanceDetails. For removing read replica database instances, the operation is REMOVE and value object needs to be an array of dbInstanceId's.

Syntax
```

```

Fields

Field Description

`items`

(optional) List of patch instructions.

### DBMS_CLOUD_OCI_PSQL_PATCH_INSERT_INSTRUCTION_T Type

An operation that inserts a value into an array, shifting array items as necessary and handling NOT_FOUND exceptions by creating the implied containing structure.

Syntax
```

```

`dbms_cloud_oci_psql_patch_insert_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

Fields

Field Description

`value`

(required) A value to be inserted into the target.

`selected_item`

(optional) A selection to be evaluated against the array for identifying a particular reference item within it, with the same format and semantics as `selection`.

`position`

(optional) Where to insert the value, relative to the first item matched by `selectedItem`. If `selectedItem` is unspecified, then \"BEFORE\" specifies insertion at the first position in an array and \"AFTER\" specifies insertion at the last position. If `selectedItem` is specified but results in an empty selection, then both values specify insertion at the last position.

Allowed values are: 'BEFORE', 'AFTER'

### DBMS_CLOUD_OCI_PSQL_PATCH_MERGE_INSTRUCTION_T Type

An operation that recursively updates items of the selection, or adding the value if the selection is empty. If the value is not an object, it is used directly, otherwise each key-value member is used to create or update a member of the same name in the target and the same process is applied recursively for each object-typed value (similar to[RFC 7396](https://tools.ietf.org/html/rfc7396#section-2)JSON Merge Patch, except that null values are copied rather than transformed into deletions). NOT_FOUND exceptions are handled by creating the implied containing structure. To avoid referential errors if an item's descendant is also in the selection, items of the selection are processed in order of decreasing depth.

Syntax
```

```

`dbms_cloud_oci_psql_patch_merge_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

Fields

Field Description

`value`

(optional) A value to be merged into the target.

### DBMS_CLOUD_OCI_PSQL_PATCH_MOVE_INSTRUCTION_T Type

An operation that \"puts\" values from elsewhere in the target, functionally equivalent to a single add and then a remove. The first item of the selection is replaced, or created if the selection is empty. NOT_FOUND exceptions in the selection are handled by creating the implied containing structure. This operation fails if the `from` selection yields any exceptions, or if an item is moved to any of its descendants.

Syntax
```

```

`dbms_cloud_oci_psql_patch_move_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

Fields

Field Description

`l_from`

(required) The selection that is to be moved, with the same format and semantics as `selection`.

`position`

(optional) Where to insert the value in an array, relative to the first item in the selection. If there is no such item, then \"BEFORE\" specifies insertion at the first position in an array and \"AFTER\" specifies insertion at the last position. If the first item in the selection is not the child of an array, then this field has no effect.

Allowed values are: 'AT', 'BEFORE', 'AFTER'

### DBMS_CLOUD_OCI_PSQL_PATCH_PROHIBIT_INSTRUCTION_T Type

A precondition operation that requires a selection to be empty, or optionally to be non-empty but include no item with a specified value (useful for asserting that a value does not exist before attempting to create it, avoiding accidental update). It fails if value is provided and the selection includes an item matching it, or if value is not provided and the selection is not empty, but ignores NOT_FOUND exceptions.

Syntax
```

```

`dbms_cloud_oci_psql_patch_prohibit_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

Fields

Field Description

`value`

(optional) A value to be compared against each item of the selection. If this value is an object, then it matches any item that would be unaffected by applying this value as a merge operation. Otherwise, it matches any item to which it is equal according to the rules of[JSON Schema](https://tools.ietf.org/html/draft-handrews-json-schema-00#section-4.2.3).

### DBMS_CLOUD_OCI_PSQL_PATCH_REMOVE_INSTRUCTION_T Type

An operation that deletes items, ignoring NOT_FOUND exceptions. To avoid referential errors if an item's descendant is also in the selection, items of the selection are processed in order of decreasing depth.

Syntax
```

```

`dbms_cloud_oci_psql_patch_remove_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

### DBMS_CLOUD_OCI_PSQL_PATCH_REPLACE_INSTRUCTION_T Type

An operation that \"puts\" a value, replacing every item of the selection with it, or creating it if the selection is empty. NOT_FOUND exceptions are handled by creating the implied containing structure (but note that this may put the target in an invalid state, which can be prevented by use of precondition operations). To avoid referential errors if an item's descendant is also in the selection, items of the selection are processed in order of decreasing depth.

Syntax
```

```

`dbms_cloud_oci_psql_patch_replace_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

Fields

Field Description

`value`

(required) A value to be added into the target.

### DBMS_CLOUD_OCI_PSQL_PATCH_REQUIRE_INSTRUCTION_T Type

A precondition operation that requires a selection to be non-empty, and optionally to include an item with a specified value (useful for asserting that a value exists before attempting to update it, avoiding accidental creation). It fails if the selection is empty, or if value is provided and no item of the selection matches it.

Syntax
```

```

`dbms_cloud_oci_psql_patch_require_instruction_t`is a subtype of the`dbms_cloud_oci_psql_patch_instruction_t`type.

Fields

Field Description

`value`

(optional) A value to be compared against each item of the selection. If this value is an object, then it matches any item that would be unaffected by applying this value as a merge operation. Otherwise, it matches any item to which it is equal according to the rules of[JSON Schema](https://tools.ietf.org/html/draft-handrews-json-schema-00#section-4.2.3).

### DBMS_CLOUD_OCI_PSQL_PLAIN_TEXT_PASSWORD_DETAILS_T Type

Details for in-line database system password.

Syntax
```

```

`dbms_cloud_oci_psql_plain_text_password_details_t`is a subtype of the`dbms_cloud_oci_psql_password_details_t`type.

Fields

Field Description

`password`

(required) The database system password.

### DBMS_CLOUD_OCI_PSQL_PRIMARY_DB_INSTANCE_DETAILS_T Type

The primary database instance node details.

Syntax
```

```

Fields

Field Description

`db_instance_id`

(required) A unique identifier for the primary database instance node.

### DBMS_CLOUD_OCI_PSQL_RESET_MASTER_USER_PASSWORD_DETAILS_T Type

Password detail that will be used to reset the database system's master user. These details are not visible on any subsequent operation, such as GET /dbSystems/{dbSystemId}.

Syntax
```

```

Fields

Field Description

`password_details`

(required)

### DBMS_CLOUD_OCI_PSQL_RESTART_DB_INSTANCE_IN_DB_SYSTEM_DETAILS_T Type

Database instance node restart parameters.

Syntax
```

```

Fields

Field Description

`db_instance_id`

(required) A unique identifier for the database instance, or node.

`restart_type`

(required) The restart type for the database instance.

Allowed values are: 'NORMAL', 'NODE_REBOOT'

### DBMS_CLOUD_OCI_PSQL_RESTORE_DB_SYSTEM_DETAILS_T Type

Backup details to restore the database system.

Syntax
```

```

Fields

Field Description

`backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database system backup.

`ad`

(optional) The desired AD for regions with three ADs. This parameter is optional. If not set, the AD is chosen based on the database system's current AD.

### DBMS_CLOUD_OCI_PSQL_SHAPE_SUMMARY_T Type

Summary of the database system shape.

Syntax
```

```

Fields

Field Description

`id`

(optional) A unique identifier for the shape.

`shape`

(required) The name of the Compute VM shape. Example: `VM.Standard.E4.Flex`

`ocpu_count`

(required) The number of OCPUs.

`memory_size_in_g_bs`

(required) The amount of memory in gigabytes.

### DBMS_CLOUD_OCI_PSQL_SHAPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_psql_shape_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_SHAPE_COLLECTION_T Type

The list of shapes that can be used to create a database system.

Syntax
```

```

Fields

Field Description

`items`

(required) List of supported shapes.

### DBMS_CLOUD_OCI_PSQL_UPDATE_BACKUP_DETAILS_T Type

The backup information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the backup. Avoid entering confidential information.

`description`

(optional) A description for the backup.

`retention_period`

(optional) Backup retention period in days.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_PSQL_UPDATE_CONFIGURATION_DETAILS_T Type

The information to update a configuration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the configuration. Avoid entering confidential information.

`description`

(optional) Details about the configuration set.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_PSQL_UPDATE_DB_CONFIG_PARAMS_T Type

Configuration for the PostgreSQL database instance.

Syntax
```

```

Fields

Field Description

`apply_config`

(optional) Whether a configuration update requires a restart of the database instance or a reload of the configuration. Some configuration changes require a restart of database instances to be applied.

Allowed values are: 'RESTART', 'RELOAD'

`config_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration.

### DBMS_CLOUD_OCI_PSQL_UPDATE_DB_SYSTEM_DB_INSTANCE_DETAILS_T Type

Database instance node update parameters.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name of the database instance node. Avoid entering confidential information.

`description`

(optional) A user-provided description of the database instance node.

### DBMS_CLOUD_OCI_PSQL_UPDATE_STORAGE_DETAILS_PARAMS_T Type

Storage details of the database system.

Syntax
```

```

Fields

Field Description

`iops`

(optional) Guaranteed input/output storage requests per second (IOPS) available to the database system. Only valid for `OCI_OPTIMIZED_STORAGE` database system type.

### DBMS_CLOUD_OCI_PSQL_UPDATE_DB_SYSTEM_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the database system. Avoid entering confidential information.

`description`

(optional) A user-provided description of the database system.

`db_configuration_params`

(optional)

`management_policy`

(optional)

`storage_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_PSQL_VAULT_SECRET_PASSWORD_DETAILS_T Type

Secret details for the database system password.

Syntax
```

```

`dbms_cloud_oci_psql_vault_secret_password_details_t`is a subtype of the`dbms_cloud_oci_psql_password_details_t`type.

Fields

Field Description

`secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret where the password is stored.

`secret_version`

(required) The secret version of the stored password.

### DBMS_CLOUD_OCI_PSQL_WEEKLY_BACKUP_POLICY_T Type

Weekly backup policy.

Syntax
```

```

`dbms_cloud_oci_psql_weekly_backup_policy_t`is a subtype of the`dbms_cloud_oci_psql_backup_policy_t`type.

Fields

Field Description

`days_of_the_week`

(required) The day of the week that the backup starts.

Allowed values are: 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'

`backup_start`

(required) Hour of the day when the backup starts.

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type that the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_psql_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_POSTGRESQL_DB_SYSTEM', 'UPDATE_POSTGRESQL_DB_SYSTEM', 'DELETE_POSTGRESQL_DB_SYSTEM', 'MOVE_POSTGRESQL_DB_SYSTEM', 'CREATE_POSTGRESQL_DB_SYSTEM_BACKUP', 'UPDATE_POSTGRESQL_DB_SYSTEM_BACKUP', 'DELETE_POSTGRESQL_DB_SYSTEM_BACKUP', 'MOVE_POSTGRESQL_DB_SYSTEM_BACKUP'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the request was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable[code](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm)for the error that occured.

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_psql_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request errors.

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_psql_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work request log entries.

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_POSTGRESQL_DB_SYSTEM', 'UPDATE_POSTGRESQL_DB_SYSTEM', 'DELETE_POSTGRESQL_DB_SYSTEM', 'MOVE_POSTGRESQL_DB_SYSTEM', 'CREATE_POSTGRESQL_DB_SYSTEM_BACKUP', 'UPDATE_POSTGRESQL_DB_SYSTEM_BACKUP', 'DELETE_POSTGRESQL_DB_SYSTEM_BACKUP', 'MOVE_POSTGRESQL_DB_SYSTEM_BACKUP'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the request was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_psql_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of work requests.

- [PSQL Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-2F9266A1-A690-41DD-875E-E5128615473C)
- [DBMS_CLOUD_OCI_PSQL_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-FA985B1C-CC9C-4EC1-B19E-3AB194BF0C66)
- [DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-F5E74FF5-F650-45B7-80A1-D7E542D6B18B)
- [DBMS_CLOUD_OCI_PSQL_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-6A65BA0C-B5E7-493E-9AD9-58B840703048)
- [DBMS_CLOUD_OCI_PSQL_BACKUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-BF51364C-AF6C-4DA7-9B9E-3022A3408C87)
- [DBMS_CLOUD_OCI_PSQL_BACKUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-30106994-4761-4B55-B089-037875E13C36)
- [DBMS_CLOUD_OCI_PSQL_BACKUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-ECC9D02B-C3EE-4C4B-A523-2C12CF8D37F9)
- [DBMS_CLOUD_OCI_PSQL_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-9068CD9D-A832-4340-B13F-35C8BF6A2900)
- [DBMS_CLOUD_OCI_PSQL_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-F9CDA2FA-F586-4351-B369-61B00EF4DF9D)
- [DBMS_CLOUD_OCI_PSQL_BACKUP_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-6470E579-E8F4-4D0C-B08A-83B7E7B83464)
- [DBMS_CLOUD_OCI_PSQL_CHANGE_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-40CB84E6-1288-487C-BF97-7DC566E6F6F0)
- [DBMS_CLOUD_OCI_PSQL_CHANGE_CONFIGURATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-A88BED59-A6FA-4336-A5FE-AEFE77AD621F)
- [DBMS_CLOUD_OCI_PSQL_CHANGE_DB_SYSTEM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-027694AA-F379-4ACC-ACDC-CEC909884484)
- [DBMS_CLOUD_OCI_PSQL_CONFIG_OVERRIDES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-9CF058EA-D923-4837-81E9-0FB3FEDCAD7D)
- [DBMS_CLOUD_OCI_PSQL_CONFIG_PARAMS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DAB33BD0-3A1D-4544-B984-AC435FEFD543)
- [DBMS_CLOUD_OCI_PSQL_CONFIG_PARAMS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-D1B80932-18B6-429D-A789-A8E40785BB86)
- [DBMS_CLOUD_OCI_PSQL_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-1FFD5994-81F2-4F65-B4B3-77EBEDF31030)
- [DBMS_CLOUD_OCI_PSQL_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-717FA06E-A63B-438B-9C62-36D2FBE321F1)
- [DBMS_CLOUD_OCI_PSQL_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-BDD5B53E-2D61-41D0-B082-6068AD4A0DB1)
- [DBMS_CLOUD_OCI_PSQL_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-A4AAE9DB-BA39-466C-B27E-5608D19E170B)
- [DBMS_CLOUD_OCI_PSQL_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-9BD3F534-5BFB-49AB-8AC2-252E4CBC7867)
- [DBMS_CLOUD_OCI_PSQL_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-CDDE70CA-D8E4-4DAE-A28A-62EF0449371C)
- [DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-F2CB9735-3468-438A-B59C-C37C52325F02)
- [DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_ENDPOINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-99C78FE1-AD16-4669-A4F1-C40A6B1E3AE6)
- [DBMS_CLOUD_OCI_PSQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-765D2C46-F01F-4425-AEA9-7D9766E15294)
- [DBMS_CLOUD_OCI_PSQL_CREATE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-38087B15-CA51-4D44-8B46-22B02D08C3B3)
- [DBMS_CLOUD_OCI_PSQL_CONFIG_OVERRIDES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-C39BF2F1-899C-4875-ADB4-13729CD3C4FD)
- [DBMS_CLOUD_OCI_PSQL_DB_CONFIGURATION_OVERRIDE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-BBF8A581-481E-4867-A235-771CEC86FD91)
- [DBMS_CLOUD_OCI_PSQL_CREATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-96D041BF-6A05-43D6-BB06-443C969BDB5F)
- [DBMS_CLOUD_OCI_PSQL_CREATE_DB_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-E03636E3-7B4F-4802-B70D-050495C9E722)
- [DBMS_CLOUD_OCI_PSQL_STORAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-6B717479-56B6-43D6-9D52-E82D1211CA34)
- [DBMS_CLOUD_OCI_PSQL_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-48156CC4-7B08-4E65-BE8C-4DB6A35D5A95)
- [DBMS_CLOUD_OCI_PSQL_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-AFD2D7F4-FE05-4B80-8C42-62039BD156C9)
- [DBMS_CLOUD_OCI_PSQL_NETWORK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-FB4963A8-5BEC-4E0F-A46B-C138846F9D15)
- [DBMS_CLOUD_OCI_PSQL_MANAGEMENT_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-BA8C70A1-F81E-41EB-8A54-74B96726EA4F)
- [DBMS_CLOUD_OCI_PSQL_CREATE_DB_INSTANCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-C1E56578-2018-455A-BFE0-2BCB17610BD4)
- [DBMS_CLOUD_OCI_PSQL_CREATE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-0DC70EBC-3EF6-4095-A0FF-FA3686944239)
- [DBMS_CLOUD_OCI_PSQL_DAILY_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-8B9DFF27-CAC9-4E71-9933-BEA3DBDB1259)
- [DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-77DD4AC3-A8C6-4191-91F8-482412D0F687)
- [DBMS_CLOUD_OCI_PSQL_MANAGEMENT_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-7FC09DCA-F10F-47CD-A74A-53CA8A6A5908)
- [DBMS_CLOUD_OCI_PSQL_DB_INSTANCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-984C8661-17C4-4B2D-8B45-4554726DAD16)
- [DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DED02D54-DE1E-4517-B30C-533BA671E01C)
- [DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-1D3D1306-01E0-4020-B88A-CEADF6B5C8E7)
- [DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-9AA8F479-64E6-43AB-8208-0D98A0E11BDD)
- [DBMS_CLOUD_OCI_PSQL_DB_SYSTEM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DAB3D631-C6B8-4169-91EA-3ABCE14354AF)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIG_PARAMS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-77E80D0C-E3F5-46B2-B294-91B7FE37292B)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIG_PARAMS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-1373960B-053F-441F-A93A-86EEC92794F8)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-33F428C3-17D8-4AF2-BDCE-66853D474AB2)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-C4374676-9999-41C2-8047-2C8A7CE029E3)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-0EC58AA7-0495-4E16-9CAF-1C8CCD7C9144)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-B80436EF-525B-4649-AF81-A557F4499D2F)
- [DBMS_CLOUD_OCI_PSQL_DEFAULT_CONFIGURATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DC16D65F-A418-43EB-89A4-D677A7EE8F85)
- [DBMS_CLOUD_OCI_PSQL_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-08E08D38-2DBE-4158-8636-0599DA87CCDE)
- [DBMS_CLOUD_OCI_PSQL_FAILOVER_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-0D070C4B-4CED-442C-B6FC-C27E2EEDE613)
- [DBMS_CLOUD_OCI_PSQL_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-8065FC16-C27C-4B5D-896D-90D0C77F62EA)
- [DBMS_CLOUD_OCI_PSQL_MONTHLY_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-5C2804AD-37CC-4D9A-A242-A9CF60376557)
- [DBMS_CLOUD_OCI_PSQL_NONE_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-F8293A46-3737-40BF-88A5-A4C4FC7E5B4C)
- [DBMS_CLOUD_OCI_PSQL_NONE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-264D7664-53F6-4803-9FB3-E3C592E6AD8A)
- [DBMS_CLOUD_OCI_PSQL_OCI_OPTIMIZED_STORAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-C016CC2A-052B-4623-A244-10A3750B504E)
- [DBMS_CLOUD_OCI_PSQL_PATCH_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-D354A3A3-07A4-496A-9E7B-B1C9FF19D44C)
- [DBMS_CLOUD_OCI_PSQL_PATCH_INSTRUCTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-F23FD360-66F4-48AD-91E0-1917C9BBBE9E)
- [DBMS_CLOUD_OCI_PSQL_PATCH_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-80707937-F9EE-4D8C-AD68-F1BC8A8F7434)
- [DBMS_CLOUD_OCI_PSQL_PATCH_INSERT_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-E0B4B81F-8CA5-4EB0-B836-6FB94F36E032)
- [DBMS_CLOUD_OCI_PSQL_PATCH_MERGE_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-8623980B-6516-4241-AAE6-97A176018C84)
- [DBMS_CLOUD_OCI_PSQL_PATCH_MOVE_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-38D7C469-1614-4720-AF89-EECC9FD4BBAF)
- [DBMS_CLOUD_OCI_PSQL_PATCH_PROHIBIT_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-994846F3-7FD3-46E2-8CC2-3AC6AD130508)
- [DBMS_CLOUD_OCI_PSQL_PATCH_REMOVE_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-F2018CB9-CCAB-41AD-B9EC-87A65CD54CD0)
- [DBMS_CLOUD_OCI_PSQL_PATCH_REPLACE_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-846CE6DA-0803-49C4-B69B-7457AA9B29D5)
- [DBMS_CLOUD_OCI_PSQL_PATCH_REQUIRE_INSTRUCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DAA26115-5557-4787-8586-DBB5466C6552)
- [DBMS_CLOUD_OCI_PSQL_PLAIN_TEXT_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-EF1B7C14-A9C8-4A80-AF9B-8896456BD1C0)
- [DBMS_CLOUD_OCI_PSQL_PRIMARY_DB_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-7577164E-2B77-4FAD-942D-6114BECAD25C)
- [DBMS_CLOUD_OCI_PSQL_RESET_MASTER_USER_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-D43FA49D-EB06-4E87-8A80-46D97127DB9B)
- [DBMS_CLOUD_OCI_PSQL_RESTART_DB_INSTANCE_IN_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-CF35BF83-EE2F-427D-8FEC-D7D195CB487E)
- [DBMS_CLOUD_OCI_PSQL_RESTORE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-16BDD849-21B7-4233-8FBE-F1BF0497CB82)
- [DBMS_CLOUD_OCI_PSQL_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-8B1C6B00-BA41-49F0-AD7F-1593F3C5585D)
- [DBMS_CLOUD_OCI_PSQL_SHAPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-8A9D9B73-25CB-4552-A235-1A6BC9664079)
- [DBMS_CLOUD_OCI_PSQL_SHAPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-18456AA3-3B99-4156-8774-D47C9BD06CCB)
- [DBMS_CLOUD_OCI_PSQL_UPDATE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-04CD6A28-FB0B-4228-A33E-3A9B9277A4E8)
- [DBMS_CLOUD_OCI_PSQL_UPDATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-55E2F0EE-4473-4876-9BC5-C7CA5FF142A5)
- [DBMS_CLOUD_OCI_PSQL_UPDATE_DB_CONFIG_PARAMS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-804071B8-6BC9-48C7-BA56-AD8BB90CA5A5)
- [DBMS_CLOUD_OCI_PSQL_UPDATE_DB_SYSTEM_DB_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-A78C8098-86CB-4ADF-B695-8D83A5C0EA3B)
- [DBMS_CLOUD_OCI_PSQL_UPDATE_STORAGE_DETAILS_PARAMS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-66F3C149-D32C-4653-BAA9-D975668007E1)
- [DBMS_CLOUD_OCI_PSQL_UPDATE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-05BD1F2D-FB2C-4DAA-AD0D-8EC31B2BB6DD)
- [DBMS_CLOUD_OCI_PSQL_VAULT_SECRET_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DF3E2046-D446-4A28-B982-A13FE18AA021)
- [DBMS_CLOUD_OCI_PSQL_WEEKLY_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-66F02976-6B40-440D-B856-0C9D36E75051)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-32ABDEE8-588A-4373-A5B6-419C4FA519F0)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-0329000A-99BD-4F3F-943A-EB8CE234BDB8)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-9D2C13EA-42A6-49A4-BDC2-B8ED35B9937D)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-4B57A68B-C9C7-45EA-8019-902534F8BCF8)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-A58E0AC2-E6FF-4829-9AC6-E4DC9B29C80E)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-95A4D62F-A1EF-4232-A950-0F32F1BDDC97)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-28B163D7-2D96-4B39-8F9F-D6E5C57B8E8C)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-0BF50ADE-8F8C-415C-8248-BE25B855481A)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-DAF22C8B-8924-444F-BB1D-410F01448BA0)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-C7F594D4-20C8-4615-9B90-C627B7388274)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-4E6F733A-9A5C-45ED-B320-4DE5FC99E172)
- [DBMS_CLOUD_OCI_PSQL_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/psql_t.html#ADSDK-GUID-8112940C-67D6-4A85-BBA4-87C546B94D4B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
