# MySQL Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#dcoc-content-body)

## MySQL Common Types

### DBMS_CLOUD_OCI_MYSQL_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_ADD_HEAT_WAVE_CLUSTER_DETAILS_T Type

Details required to add a HeatWave cluster.

Syntax
```

```

Fields

Field Description

`shape_name`

(required) The shape determines resources to allocate to the HeatWave nodes - CPU cores, memory.

`cluster_size`

(required) The number of analytics-processing nodes provisioned for the HeatWave cluster.

`is_lakehouse_enabled`

(optional) Enable/disable Lakehouse for the HeatWave cluster.

### DBMS_CLOUD_OCI_MYSQL_ANONYMOUS_TRANSACTIONS_HANDLING_T Type

Specifies how the replication channel handles replicated transactions without an identifier, enabling replication from a source that does not use transaction-id-based replication to a replica that does.

Syntax
```

```

Fields

Field Description

`policy`

(required) Specifies how the replication channel handles anonymous transactions.

Allowed values are: 'ERROR_ON_ANONYMOUS', 'ASSIGN_TARGET_UUID', 'ASSIGN_MANUAL_UUID'

### DBMS_CLOUD_OCI_MYSQL_ASSIGN_MANUAL_UUID_HANDLING_T Type

Enables assignment of IDs on the target to anonymous transactions coming from the source. A manually defined UUID is added as a prefix to the ID.

Syntax
```

```

`dbms_cloud_oci_mysql_assign_manual_uuid_handling_t`is a subtype of the`dbms_cloud_oci_mysql_anonymous_transactions_handling_t`type.

Fields

Field Description

`last_configured_log_filename`

(optional) Specifies one of the coordinates (file) at which the replica should begin reading the source's log. As this value specifies the point where replication starts from, it is only used once, when it starts. It is never used again, unless a new UpdateChannel operation modifies it.

`last_configured_log_offset`

(optional) Specifies one of the coordinates (offset) at which the replica should begin reading the source's log. As this value specifies the point where replication starts from, it is only used once, when it starts. It is never used again, unless a new UpdateChannel operation modifies it.

`uuid`

(optional) The UUID that is used as a prefix when generating transaction identifiers for anonymous transactions coming from the source. You can change the UUID later.

### DBMS_CLOUD_OCI_MYSQL_ASSIGN_TARGET_UUID_HANDLING_T Type

Enables assignment of IDs on the target to anonymous transactions coming from the source. The target server UUID is added as a prefix to the ID.

Syntax
```

```

`dbms_cloud_oci_mysql_assign_target_uuid_handling_t`is a subtype of the`dbms_cloud_oci_mysql_anonymous_transactions_handling_t`type.

Fields

Field Description

`last_configured_log_filename`

(optional) Specifies one of the coordinates (file) at which the replica should begin reading the source's log. As this value specifies the point where replication starts from, it is only used once, when it starts. It is never used again, unless a new UpdateChannel operation modifies it.

`last_configured_log_offset`

(optional) Specifies one of the coordinates (offset) at which the replica should begin reading the source's log. As this value specifies the point where replication starts from, it is only used once, when it starts. It is never used again, unless a new UpdateChannel operation modifies it.

### DBMS_CLOUD_OCI_MYSQL_PITR_POLICY_T Type

The PITR policy for the DB System.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) Specifies if PITR is enabled or disabled.

### DBMS_CLOUD_OCI_MYSQL_BACKUP_POLICY_T Type

The Backup policy for the DB System.

Syntax
```

```

Fields

Field Description

`is_enabled`

(required) If automated backups are enabled or disabled.

`window_start_time`

(required) The start of a 30-minute window of time in which daily, automated backups occur. This should be in the format of the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero. At some point in the window, the system may incur a brief service disruption as the backup is performed. If not defined, a window is selected from the following Region-based time-spans: - eu-frankfurt-1: 20:00 - 04:00 UTC - us-ashburn-1: 03:00 - 11:00 UTC - uk-london-1: 06:00 - 14:00 UTC - ap-tokyo-1: 13:00 - 21:00 - us-phoenix-1: 06:00 - 14:00

`retention_in_days`

(required) The number of days automated backups are retained.

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`pitr_policy`

(optional)

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_ENDPOINT_T Type

A particular functional endpoint for access to a DB System, and the properties that apply to it.

Syntax
```

```

Fields

Field Description

`hostname`

(optional) The network address of the DB System.

`ip_address`

(required) The IP address the DB System is configured to listen on.

`port`

(required) The port the MySQL instance listens on.

`port_x`

(required) The network port where to connect to use this endpoint using the X protocol.

`modes`

(optional) The access modes from the client that this endpoint supports.

Allowed values are: 'READ', 'WRITE'

`status`

(optional) The state of the endpoints, as far as it can seen from the DB System. There may be some inconsistency with the actual state of the MySQL service.

Allowed values are: 'ACTIVE', 'INACTIVE', 'UPDATING'

`status_details`

(optional) Additional information about the current endpoint status.

`resource_type`

(optional) The type of endpoint that clients and connectors can connect to.

Allowed values are: 'DBSYSTEM', 'READ_REPLICA', 'LOAD_BALANCER'

`resource_id`

(optional) The OCID of the resource that this endpoint is attached to.

### DBMS_CLOUD_OCI_MYSQL_MAINTENANCE_DETAILS_T Type

The Maintenance Policy for the DB System or Read Replica that this model is included in.

Syntax
```

```

Fields

Field Description

`window_start_time`

(optional) The start time of the maintenance window. This string is of the format: \"{day-of-week} {time-of-day}\". \"{day-of-week}\" is a case-insensitive string like \"mon\", \"tue\", &amp;c. \"{time-of-day}\" is the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero. If you set the read replica maintenance window to \"\" or if not specified, the read replica is set same as the DB system maintenance window.

### DBMS_CLOUD_OCI_MYSQL_DELETION_POLICY_DETAILS_T Type

The Deletion policy for the DB System.

Syntax
```

```

Fields

Field Description

`automatic_backup_retention`

(required) Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.

Allowed values are: 'DELETE', 'RETAIN'

`final_backup`

(required) Specifies whether or not a backup is taken when the DB System is deleted. REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted. SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted.

Allowed values are: 'SKIP_FINAL_BACKUP', 'REQUIRE_FINAL_BACKUP'

`is_delete_protected`

(required) Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_ENDPOINT_TBL Type

Nested table type of dbms_cloud_oci_mysql_db_system_endpoint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SNAPSHOT_T Type

Snapshot of the DbSystem details at the time of the backup

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DB System.

`display_name`

(required) The user-friendly name for the DB System. It does not have to be unique.

`description`

(optional) User-provided data about the DB System.

`compartment_id`

(required) The OCID of the compartment the DB System belongs in.

`subnet_id`

(required) The OCID of the subnet the DB System is associated with.

`availability_domain`

(optional) The Availability Domain where the primary DB System should be located.

`fault_domain`

(optional) The name of the Fault Domain the DB System is located in.

`shape_name`

(optional) The shape of the primary instances of the DB System. The shape determines resources allocated to a DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use (the`LIST_SHAPES`Function operation.

`mysql_version`

(required) Name of the MySQL Version in use for the DB System.

`admin_username`

(optional) The username for the administrative user.

`backup_policy`

(optional)

`configuration_id`

(optional) The OCID of the Configuration to be used for Instances in this DB System.

`data_storage_size_in_g_bs`

(required) Initial size of the data volume in GiBs that will be created and attached.

`hostname_label`

(optional) The hostname for the primary endpoint of the DB System. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\"). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.

`ip_address`

(optional) The IP address the DB System is configured to listen on. A private IP address of the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. This will be a \"dotted-quad\" style IPv4 address.

`port`

(optional) The port for primary endpoint of the DB System to listen on.

`port_x`

(optional) The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.

`is_highly_available`

(optional) Specifies if the DB System is highly available.

`endpoints`

(optional) The network endpoints available for this DB System.

`maintenance`

(required)

`deletion_policy`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`crash_recovery`

(optional) Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled, and whether to enable or disable syncing of the Binary Logs.

Allowed values are: 'ENABLED', 'DISABLED'

`database_management`

(optional) Whether to enable monitoring via the Database Management service.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_MYSQL_BACKUP_T Type

A full or incremental copy of a DB System which can be used to create a new DB System or recover a DB System. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the backup itself

`display_name`

(optional) A user-supplied display name for the backup.

`description`

(optional) A user-supplied description for the backup.

`compartment_id`

(required) The OCID of the compartment.

`time_created`

(required) The time the backup record was created.

`time_updated`

(required) The time at which the backup was updated.

`lifecycle_state`

(required) The state of the backup.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) Additional information about the current lifecycleState.

`backup_type`

(required) The type of backup.

Allowed values are: 'FULL', 'INCREMENTAL'

`creation_type`

(required) Indicates how the backup was created: manually, automatic, or by an Operator.

Allowed values are: 'MANUAL', 'AUTOMATIC', 'OPERATOR'

`db_system_id`

(required) The OCID of the DB System the backup is associated with.

`db_system_snapshot`

(optional)

`backup_size_in_g_bs`

(optional) The size of the backup in base-2 (IEC) gibibytes. (GiB).

`retention_in_days`

(optional) Number of days to retain this backup.

`data_storage_size_in_g_bs`

(optional) Initial size of the data volume in GiBs.

`mysql_version`

(optional) The MySQL server version of the DB System used for backup.

`shape_name`

(optional) The shape of the DB System used for backup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_BACKUP_SUMMARY_T Type

Details of Backups such as OCID, description, backupType, and so on. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the backup.

`display_name`

(optional) A user-supplied display name for the backup.

`description`

(optional) A user-supplied description of the backup.

`time_created`

(required) The time the backup was created.

`lifecycle_state`

(required) The state of the backup.

`backup_type`

(required) The type of backup.

`creation_type`

(required) If the backup was created automatically, or by a manual request.

`db_system_id`

(required) The OCID of the DB System the Backup is associated with.

`compartment_id`

(required) The OCID of the compartment the backup exists in.

`data_storage_size_in_g_bs`

(optional) Size of the data volume in GiBs.

`backup_size_in_g_bs`

(optional) The size of the backup in GiBs.

`retention_in_days`

(optional) Number of days to retain this backup.

`mysql_version`

(optional) The version of the DB System used for backup.

`shape_name`

(optional) The shape of the DB System instance used for backup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CA_CERTIFICATE_T Type

The CA certificate of the server used for VERIFY_IDENTITY and VERIFY_CA ssl modes.

Syntax
```

```

Fields

Field Description

`certificate_type`

(required) The type of CA certificate.

Allowed values are: 'PEM'

### DBMS_CLOUD_OCI_MYSQL_CHANGE_BACKUP_COMPARTMENT_DETAILS_T Type

OCID of the target compartment for DB System Backup change compartment request.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the target compartment.

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_SOURCE_T Type

Parameters detailing how to provision the source for the given Channel.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The specific source identifier.

Allowed values are: 'MYSQL'

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_TARGET_T Type

Details about the Channel target.

Syntax
```

```

Fields

Field Description

`target_type`

(required) The specific target identifier.

Allowed values are: 'DBSYSTEM'

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_T Type

A Channel connecting a DB System to an external entity.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Channel.

`compartment_id`

(required) The OCID of the compartment.

`display_name`

(required) The user-friendly name for the Channel. It does not have to be unique.

`is_enabled`

(required) Whether the Channel has been enabled by the user.

`source`

(required)

`target`

(required)

`description`

(optional) User provided description of the Channel.

`lifecycle_state`

(required) The state of the Channel.

Allowed values are: 'CREATING', 'ACTIVE', 'NEEDS_ATTENTION', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the state of the Channel.

`time_created`

(required) The date and time the Channel was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(required) The time the Channel was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_FILTER_T Type

Replication filter rule for a channel.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the filter rule. For details on each type, see[Replication Filtering Rules](https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html)

Allowed values are: 'REPLICATE_DO_DB', 'REPLICATE_IGNORE_DB', 'REPLICATE_DO_TABLE', 'REPLICATE_IGNORE_TABLE', 'REPLICATE_WILD_DO_TABLE', 'REPLICATE_WILD_IGNORE_TABLE', 'REPLICATE_REWRITE_DB'

`value`

(required) The body of the filter rule. This can represent a database, a table, or a database pair (represented as \"db1-&gt;db2\"). For more information, see[Replication Filtering Rules](https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html).

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_SOURCE_MYSQL_T Type

Core properties of a Mysql Channel source.

Syntax
```

```

`dbms_cloud_oci_mysql_channel_source_mysql_t`is a subtype of the`dbms_cloud_oci_mysql_channel_source_t`type.

Fields

Field Description

`hostname`

(required) The network address of the MySQL instance.

`port`

(required) The port the source MySQL instance listens on.

`username`

(required) The name of the replication user on the source MySQL instance. The username has a maximum length of 96 characters. For more information, please see the[MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)

`ssl_mode`

(required) The SSL mode of the Channel.

Allowed values are: 'VERIFY_IDENTITY', 'VERIFY_CA', 'REQUIRED', 'DISABLED'

`ssl_ca_certificate`

(optional)

`anonymous_transactions_handling`

(optional)

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_SUMMARY_T Type

Summary of a Channel.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Channel.

`compartment_id`

(required) The OCID of the compartment.

`is_enabled`

(required) Whether the Channel has been enabled by the user.

`source`

(required)

`target`

(required)

`lifecycle_state`

(required) The state of the Channel.

`lifecycle_details`

(optional) A message describing the state of the Channel.

`display_name`

(required) The user-friendly name for the Channel. It does not have to be unique.

`time_created`

(required) The date and time the Channel was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(required) The time the Channel was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_FILTER_TBL Type

Nested table type of dbms_cloud_oci_mysql_channel_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_TARGET_DB_SYSTEM_T Type

Core properties of a DB System Channel target.

Syntax
```

```

`dbms_cloud_oci_mysql_channel_target_db_system_t`is a subtype of the`dbms_cloud_oci_mysql_channel_target_t`type.

Fields

Field Description

`db_system_id`

(required) The OCID of the source DB System.

`channel_name`

(required) The case-insensitive name that identifies the replication channel. Channel names must follow the rules defined for[MySQL identifiers](https://dev.mysql.com/doc/refman/8.0/en/identifiers.html). The names of non-Deleted Channels must be unique for each DB System.

`applier_username`

(required) The username for the replication applier of the target MySQL DB System.

`filters`

(optional) Replication filter rules to be applied at the DB System Channel target.

`tables_without_primary_key_handling`

(required) Specifies how a replication channel handles the creation and alteration of tables that do not have a primary key.

Allowed values are: 'RAISE_ERROR', 'ALLOW', 'GENERATE_IMPLICIT_PRIMARY_KEY'

`delay_in_seconds`

(required) Specifies the amount of time, in seconds, that the channel waits before applying a transaction received from the source.

### DBMS_CLOUD_OCI_MYSQL_INITIALIZATION_VARIABLES_T Type

User-defined service variables set only at DB system initialization. These variables cannot be changed later at runtime.

Syntax
```

```

Fields

Field Description

`lower_case_table_names`

(optional) Represents the MySQL server system variable lower_case_table_names (https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_lower_case_table_names). lowerCaseTableNames controls case-sensitivity of tables and schema names and how they are stored in the DB System. Valid values are: - CASE_SENSITIVE - (default) Table and schema name comparisons are case-sensitive and stored as specified. (lower_case_table_names=0) - CASE_INSENSITIVE_LOWERCASE - Table and schema name comparisons are not case-sensitive and stored in lowercase. (lower_case_table_names=1)

Allowed values are: 'CASE_SENSITIVE', 'CASE_INSENSITIVE_LOWERCASE'

### DBMS_CLOUD_OCI_MYSQL_CONFIGURATION_VARIABLES_T Type

User-defined service variables.

Syntax
```

```

Fields

Field Description

`completion_type`

(optional) (\"completion_type\")

Allowed values are: 'NO_CHAIN', 'CHAIN', 'RELEASE'

`big_tables`

(optional) If enabled, the server stores all temporary tables on disk rather than in memory. bigTables corresponds to the MySQL server variable[big_tables](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_big_tables).

`connection_memory_chunk_size`

(optional) Set the chunking size for updates to the global memory usage counter Global_connection_memory. connectionMemoryChunkSize corresponds to the MySQL system variable[connection_memory_chunk_size](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_chunk_size).

`connection_memory_limit`

(optional) Set the maximum amount of memory that can be used by a single user connection. connectionMemoryLimit corresponds to the MySQL system variable[connection_memory_limit](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_limit).

`default_authentication_plugin`

(optional) (\"default_authentication_plugin\")

Allowed values are: 'mysql_native_password', 'sha256_password', 'caching_sha2_password'

`global_connection_memory_limit`

(optional) Set the total amount of memory that can be used by all user connections. globalConnectionMemoryLimit corresponds to the MySQL system variable[global_connection_memory_limit](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_global_connection_memory_limit).

`global_connection_memory_tracking`

(optional) Determines whether the MySQL server calculates Global_connection_memory. globalConnectionMemoryTracking corresponds to the MySQL system variable[global_connection_memory_tracking](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_global_connection_memory_tracking).

`transaction_isolation`

(optional) (\"transaction_isolation\")

Allowed values are: 'READ-UNCOMMITTED', 'READ-COMMITED', 'READ-COMMITTED', 'REPEATABLE-READ', 'SERIALIZABLE'

`innodb_ft_server_stopword_table`

(optional) (\"innodb_ft_server_stopword_table\")

`mandatory_roles`

(optional) (\"mandatory_roles\")

`autocommit`

(optional) (\"autocommit\")

`foreign_key_checks`

(optional) (\"foreign_key_checks\")

`group_replication_consistency`

(optional) - EVENTUAL: Both RO and RW transactions do not wait for preceding transactions to be applied before executing. A RW transaction does not wait for other members to apply a transaction. This means that a transaction could be externalized on one member before the others. This also means that in the event of a primary failover, the new primary can accept new RO and RW transactions before the previous primary transactions are all applied. RO transactions could result in outdated values, RW transactions could result in a rollback due to conflicts. - BEFORE_ON_PRIMARY_FAILOVER: New RO or RW transactions with a newly elected primary that is applying backlog from the old primary are held (not applied) until any backlog has been applied. This ensures that when a primary failover happens, intentionally or not, clients always see the latest value on the primary. This guarantees consistency, but means that clients must be able to handle the delay in the event that a backlog is being applied. Usually this delay should be minimal, but does depend on the size of the backlog. - BEFORE: A RW transaction waits for all preceding transactions to complete before being applied. A RO transaction waits for all preceding transactions to complete before being executed. This ensures that this transaction reads the latest value by only affecting the latency of the transaction. This reduces the overhead of synchronization on every RW transaction, by ensuring synchronization is used only on RO transactions. This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER. - AFTER: A RW transaction waits until its changes have been applied to all of the other members. This value has no effect on RO transactions. This mode ensures that when a transaction is committed on the local member, any subsequent transaction reads the written value or a more recent value on any group member. Use this mode with a group that is used for predominantly RO operations to ensure that applied RW transactions are applied everywhere once they commit. This could be used by your application to ensure that subsequent reads fetch the latest data which includes the latest writes. This reduces the overhead of synchronization on every RO transaction, by ensuring synchronization is used only on RW transactions. This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER. - BEFORE_AND_AFTER: A RW transaction waits for 1) all preceding transactions to complete before being applied and 2) until its changes have been applied on other members. A RO transaction waits for all preceding transactions to complete before execution takes place. This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER.

Allowed values are: 'EVENTUAL', 'BEFORE_ON_PRIMARY_FAILOVER', 'BEFORE', 'AFTER', 'BEFORE_AND_AFTER'

`innodb_ft_enable_stopword`

(optional) (\"innodb_ft_enable_stopword\")

`innodb_log_writer_threads`

(optional) Enables dedicated log writer threads for writing redo log records from the log buffer to the system buffers and flushing the system buffers to the redo log files. This is the MySQL variable \"innodb_log_writer_threads\". For more information, please see the[MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_writer_threads)

`local_infile`

(optional) (\"local_infile\")

`mysql_firewall_mode`

(optional) (\"mysql_firewall_mode\")

`mysqlx_enable_hello_notice`

(optional) (\"mysqlx_enable_hello_notice\") DEPRECATED -- variable should not be settable and will be ignored

`sql_require_primary_key`

(optional) (\"sql_require_primary_key\")

`sql_warnings`

(optional) (\"sql_warnings\")

`binlog_expire_logs_seconds`

(optional) Sets the binary log expiration period in seconds. binlogExpireLogsSeconds corresponds to the MySQL binary logging system variable[binlog_expire_logs_seconds](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds).

`binlog_row_metadata`

(optional) Configures the amount of table metadata added to the binary log when using row-based logging. binlogRowMetadata corresponds to the MySQL binary logging system variable[binlog_row_metadata](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_metadata).

Allowed values are: 'FULL', 'MINIMAL'

`binlog_row_value_options`

(optional) When set to PARTIAL_JSON, this enables use of a space-efficient binary log format for updates that modify only a small portion of a JSON document. binlogRowValueOptions corresponds to the MySQL binary logging system variable[binlog_row_value_options](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_value_options).

`binlog_transaction_compression`

(optional) Enables compression for transactions that are written to binary log files on this server. binlogTransactionCompression corresponds to the MySQL binary logging system variable[binlog_transaction_compression](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_transaction_compression).

`innodb_buffer_pool_size`

(optional) The size (in bytes) of the buffer pool, that is, the memory area where InnoDB caches table and index data. innodbBufferPoolSize corresponds to the MySQL server system variable[innodb_buffer_pool_size](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size). The default and maximum values depend on the amount of RAM provisioned by the shape.

`innodb_ft_result_cache_limit`

(optional) (\"innodb_ft_result_cache_limit\")

`max_binlog_cache_size`

(optional) Sets the size of the transaction cache. maxBinlogCacheSize corresponds to the MySQL server system variable[max_binlog_cache_size](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_max_binlog_cache_size).

`max_connect_errors`

(optional) (\"max_connect_errors\")

`max_heap_table_size`

(optional) This variable sets the maximum size to which user-created MEMORY tables are permitted to grow. maxHeapTableSize corresponds to the MySQL system variable[max_heap_table_size](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_heap_table_size)

`max_connections`

(optional) (\"max_connections\")

`max_prepared_stmt_count`

(optional) (\"max_prepared_stmt_count\")

`connect_timeout`

(optional) The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake. connectTimeout corresponds to the MySQL system variable[connect_timeout](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_connect_timeout)Increasing the connect_timeout value might help if clients frequently encounter errors of the form \"Lost connection to MySQL server at 'XXX', system error: errno\".

`cte_max_recursion_depth`

(optional) (\"cte_max_recursion_depth\")

`generated_random_password_length`

(optional) (\"generated_random_password_length\") DEPRECATED -- variable should not be settable and will be ignored

`information_schema_stats_expiry`

(optional) (\"information_schema_stats_expiry\")

`innodb_buffer_pool_dump_pct`

(optional) Specifies the percentage of the most recently used pages for each buffer pool to read out and dump. innodbBufferPoolDumpPct corresponds to the MySQL InnoDB system variable[innodb_buffer_pool_dump_pct](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_dump_pct). The range is 1 to 100. The default value is 25. For example, if there are 4 buffer pools with 100 pages each, and innodb_buffer_pool_dump_pct is set to 25, the 25 most recently used pages from each buffer pool are dumped.

`innodb_buffer_pool_instances`

(optional) (\"innodb_buffer_pool_instances\")

`innodb_ddl_buffer_size`

(optional) innodbDdlBufferSize corresponds to the MySQL system variable[innodb_ddl_buffer_size]](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_ddl_buffer_size)

`innodb_ddl_threads`

(optional) innodbDdlThreads corresponds to the MySQL system variable[innodb_ddl_threads]](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_ddl_threads)

`innodb_ft_max_token_size`

(optional) (\"innodb_ft_max_token_size\")

`innodb_ft_min_token_size`

(optional) (\"innodb_ft_min_token_size\")

`innodb_ft_num_word_optimize`

(optional) (\"innodb_ft_num_word_optimize\")

`innodb_lock_wait_timeout`

(optional) (\"innodb_lock_wait_timeout\")

`innodb_max_purge_lag`

(optional) The desired maximum purge lag in terms of transactions. InnoDB maintains a list of transactions that have index records delete-marked by UPDATE or DELETE operations. The length of the list is the purge lag. If this value is exceeded, a delay is imposed on INSERT, UPDATE, and DELETE operations to allow time for purge to catch up. The default value is 0, which means there is no maximum purge lag and no delay. innodbMaxPurgeLag corresponds to the MySQL server system variable[innodb_max_purge_lag](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag).

`innodb_max_purge_lag_delay`

(optional) The maximum delay in microseconds for the delay imposed when the innodb_max_purge_lag threshold is exceeded. The specified innodb_max_purge_lag_delay value is an upper limit on the delay period. innodbMaxPurgeLagDelay corresponds to the MySQL server system variable[innodb_max_purge_lag_delay](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag_delay).

`interactive_timeout`

(optional) The number of seconds the server waits for activity on an interactive connection before closing it. interactiveTimeout corresponds to the MySQL system variable.[interactive_timeout](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_interactive_timeout)

`innodb_stats_persistent_sample_pages`

(optional) The number of index pages to sample when estimating cardinality and other statistics for an indexed column, such as those calculated by ANALYZE TABLE. innodbStatsPersistentSamplePages corresponds to the MySQL InnoDB system variable[innodb_stats_persistent_sample_pages](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_stats_persistent_sample_pages)innodb_stats_persistent_sample_pages only applies when innodb_stats_persistent is enabled for a table; when innodb_stats_persistent is disabled, innodb_stats_transient_sample_pages applies instead.

`innodb_stats_transient_sample_pages`

(optional) The number of index pages to sample when estimating cardinality and other statistics for an indexed column, such as those calculated by[ANALYZE TABLE](https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html). innodbStatsTransientSamplePages corresponds to the MySQL InnoDB system variable[innodb_stats_transient_sample_pages](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_stats_transient_sample_pages)innodb_stats_transient_sample_pages only applies when innodb_stats_persistent is disabled for a table; when innodb_stats_persistent is enabled, innodb_stats_persistent_sample_pages applies instead. innodb_stats_persistent is ON by default and cannot be changed. It is possible to override it using the STATS_PERSISTENT clause of the[CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)and[ALTER TABLE](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)statements.

`max_allowed_packet`

(optional) The maximum size of one packet or any generated/intermediate string. This is the mysql variable \"max_allowed_packet\".

`max_execution_time`

(optional) (\"max_execution_time\")

`mysqlx_connect_timeout`

(optional) The number of seconds X Plugin waits for the first packet to be received from newly connected clients. mysqlxConnectTimeout corresponds to the MySQL X Plugin system variable[mysqlx_connect_timeout](https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_connect_timeout)

`mysqlx_document_id_unique_prefix`

(optional) (\"mysqlx_document_id_unique_prefix\") DEPRECATED -- variable should not be settable and will be ignored

`mysqlx_idle_worker_thread_timeout`

(optional) (\"mysqlx_idle_worker_thread_timeout\") DEPRECATED -- variable should not be settable and will be ignored

`mysqlx_interactive_timeout`

(optional) The number of seconds to wait for interactive clients to timeout. mysqlxInteractiveTimeout corresponds to the MySQL X Plugin system variable.[mysqlx_interactive_timeout](https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_interactive_timeout)

`mysqlx_max_allowed_packet`

(optional) The maximum size of network packets that can be received by X Plugin. This is the mysql variable \"mysqlx_max_allowed_packet\".

`mysqlx_min_worker_threads`

(optional) (\"mysqlx_min_worker_threads\") DEPRECATED -- variable should not be settable and will be ignored

`mysqlx_read_timeout`

(optional) The number of seconds that X Plugin waits for blocking read operations to complete. After this time, if the read operation is not successful, X Plugin closes the connection and returns a warning notice with the error code ER_IO_READ_ERROR to the client application. mysqlxReadTimeout corresponds to the MySQL X Plugin system variable[mysqlx_read_timeout](https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_read_timeout)

`mysqlx_wait_timeout`

(optional) The number of seconds that X Plugin waits for activity on a connection. mysqlxWaitTimeout corresponds to the MySQL X Plugin system variable.[mysqlx_wait_timeout](https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_wait_timeout)

`mysqlx_write_timeout`

(optional) The number of seconds that X Plugin waits for blocking write operations to complete. After this time, if the write operation is not successful, X Plugin closes the connection. mysqlxReadmysqlxWriteTimeoutTimeout corresponds to the MySQL X Plugin system variable[mysqlx_write_timeout](https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_write_timeout)

`net_read_timeout`

(optional) The number of seconds to wait for more data from a connection before aborting the read. netReadTimeout corresponds to the MySQL system variable[net_read_timeout](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_read_timeout)

`net_write_timeout`

(optional) The number of seconds to wait for a block to be written to a connection before aborting the write. netWriteTimeout corresponds to the MySQL system variable[net_write_timeout](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_write_timeout)

`parser_max_mem_size`

(optional) (\"parser_max_mem_size\")

`query_alloc_block_size`

(optional) (\"query_alloc_block_size\") DEPRECATED -- variable should not be settable and will be ignored

`query_prealloc_size`

(optional) (\"query_prealloc_size\") DEPRECATED -- variable should not be settable and will be ignored

`regexp_time_limit`

(optional) regexpTimeLimit corresponds to the MySQL system variable[regexp_time_limit]](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_regexp_time_limit)

`sql_mode`

(optional) (\"sql_mode\")

`tmp_table_size`

(optional) The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables. tmp_table_size corresponds to the MySQL system variable[tmp_table_size](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size)

`mysqlx_deflate_default_compression_level`

(optional) Set the default compression level for the deflate algorithm. (\"mysqlx_deflate_default_compression_level\")

`mysqlx_deflate_max_client_compression_level`

(optional) Limit the upper bound of accepted compression levels for the deflate algorithm. (\"mysqlx_deflate_max_client_compression_level\")

`mysqlx_lz4_max_client_compression_level`

(optional) Limit the upper bound of accepted compression levels for the lz4 algorithm. (\"mysqlx_lz4_max_client_compression_level\")

`mysqlx_lz4_default_compression_level`

(optional) Set the default compression level for the lz4 algorithm. (\"mysqlx_lz4_default_compression_level\")

`mysqlx_zstd_max_client_compression_level`

(optional) Limit the upper bound of accepted compression levels for the zstd algorithm. (\"mysqlx_zstd_max_client_compression_level\")

`mysqlx_zstd_default_compression_level`

(optional) Set the default compression level for the zstd algorithm. (\"mysqlx_zstd_default_compression_level\")

`mysql_zstd_default_compression_level`

(optional) DEPRECATED -- typo of mysqlx_zstd_default_compression_level. variable will be ignored.

`sort_buffer_size`

(optional) Each session that must perform a sort allocates a buffer of this size. sortBufferSize corresponds to the MySQL system variable[sort_buffer_size](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_sort_buffer_size)

`wait_timeout`

(optional) The number of seconds the server waits for activity on a noninteractive connection before closing it. waitTimeout corresponds to the MySQL system variable.[wait_timeout](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout)

`thread_pool_dedicated_listeners`

(optional) Controls whether the thread pool uses dedicated listener threads. If enabled, a listener thread in each thread group is dedicated to the task of listening for network events from clients, ensuring that the maximum number of query worker threads is no more than the value specified by threadPoolMaxTransactionsLimit. threadPoolDedicatedListeners corresponds to the MySQL Database Service-specific system variable thread_pool_dedicated_listeners.

`thread_pool_max_transactions_limit`

(optional) Limits the maximum number of open transactions to the defined value. The default value is 0, which enforces no limit. threadPoolMaxTransactionsLimit corresponds to the MySQL Database Service-specific system variable thread_pool_max_transactions_limit.

`time_zone`

(optional) Initializes the time zone for each client that connects. This corresponds to the MySQL System Variable \"time_zone\". The values can be given in one of the following formats, none of which are case-sensitive: - As a string indicating an offset from UTC of the form [H]H:MM, prefixed with a + or -, such as '+10:00', '-6:00', or '+05:30'. The permitted range is '-13:59' to '+14:00', inclusive. - As a named time zone, as defined by the \"IANA Time Zone database\", such as 'Europe/Helsinki', 'US/Eastern', 'MET', or 'UTC'.

### DBMS_CLOUD_OCI_MYSQL_CONFIGURATION_T Type

The set of MySQL variables to be used when deploying a MySQL Database Service DB System.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Configuration.

`compartment_id`

(required) OCID of the Compartment the Configuration exists in.

`description`

(optional) User-provided data about the Configuration.

`display_name`

(optional) The display name of the Configuration.

`shape_name`

(required) The name of the associated Shape.

`l_type`

(required) The Configuration type, DEFAULT or CUSTOM.

Allowed values are: 'DEFAULT', 'CUSTOM'

`time_created`

(required) The date and time the Configuration was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(required) The date and time the Configuration was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`lifecycle_state`

(required) The current state of the Configuration.

Allowed values are: 'ACTIVE', 'DELETED'

`init_variables`

(optional)

`variables`

(required)

`parent_configuration_id`

(optional) The OCID of the Configuration from which this Configuration is \"derived\". This is entirely a metadata relationship. There is no relation between the values in this Configuration and its parent.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CONFIGURATION_SUMMARY_T Type

The general details of a Configuration such as its id, displayName, type, and shape association.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Configuration.

`compartment_id`

(required) OCID of the Compartment the Configuration exists in.

`description`

(optional) User-provided data about the Configuration.

`display_name`

(optional) The display name of the Configuration.

`shape_name`

(required) The name of the associated Shape.

`l_type`

(required) The Configuration type, DEFAULT or CUSTOM

`lifecycle_state`

(required) The current state of the Configuration.

`time_created`

(optional) The date and time the Configuration was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The date and time the Configuration was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CREATE_BACKUP_DETAILS_T Type

Complete information for a Backup.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-supplied display name for the backup.

`description`

(optional) A user-supplied description for the backup.

`backup_type`

(optional) The type of backup.

Allowed values are: 'FULL', 'INCREMENTAL'

`db_system_id`

(required) The OCID of the DB System the Backup is associated with.

`retention_in_days`

(optional) Number of days to retain this backup.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CREATE_BACKUP_POLICY_DETAILS_T Type

Backup policy as optionally used for DB System Creation.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Specifies if automatic backups are enabled.

`window_start_time`

(optional) The start of a 30-minute window of time in which daily, automated backups occur. This should be in the format of the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero. At some point in the window, the system may incur a brief service disruption as the backup is performed.

`retention_in_days`

(optional) Number of days to retain an automatic backup.

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`pitr_policy`

(optional)

### DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_SOURCE_DETAILS_T Type

Parameters detailing how to provision the source for the given Channel.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The specific source identifier.

### DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_TARGET_DETAILS_T Type

Parameters detailing how to provision the target for the given Channel.

Syntax
```

```

Fields

Field Description

`target_type`

(required) The specific target identifier.

### DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_DETAILS_T Type

Details required to create a Channel.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment.

`display_name`

(optional) The user-friendly name for the Channel. It does not have to be unique.

`is_enabled`

(optional) Whether the Channel should be enabled upon creation. If set to true, the Channel will be asynchronously started as a result of the create Channel operation.

`source`

(required)

`target`

(required)

`description`

(optional) User provided information about the Channel.

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_SOURCE_FROM_MYSQL_DETAILS_T Type

Parameters detailing how to provision the source endpoint that is a MySQL Server. Typically a MySQL Server that is not managed by the MySQL Database Service.

Syntax
```

```

`dbms_cloud_oci_mysql_create_channel_source_from_mysql_details_t`is a subtype of the`dbms_cloud_oci_mysql_create_channel_source_details_t`type.

Fields

Field Description

`hostname`

(required) The network address of the MySQL instance.

`port`

(optional) The port the source MySQL instance listens on.

`username`

(required) The name of the replication user on the source MySQL instance. The username has a maximum length of 96 characters. For more information, please see the[MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)

`password`

(required) The password for the replication user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.

`ssl_mode`

(required) The SSL mode of the Channel.

`ssl_ca_certificate`

(optional)

`anonymous_transactions_handling`

(optional)

### DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_TARGET_FROM_DB_SYSTEM_DETAILS_T Type

Parameters detailing how to provision the target endpoint that is a DB System.

Syntax
```

```

`dbms_cloud_oci_mysql_create_channel_target_from_db_system_details_t`is a subtype of the`dbms_cloud_oci_mysql_create_channel_target_details_t`type.

Fields

Field Description

`db_system_id`

(required) The OCID of the target DB System.

`channel_name`

(optional) The case-insensitive name that identifies the replication channel. Channel names must follow the rules defined for[MySQL identifiers](https://dev.mysql.com/doc/refman/8.0/en/identifiers.html). The names of non-Deleted Channels must be unique for each DB System.

`applier_username`

(optional) The username for the replication applier of the target MySQL DB System.

`filters`

(optional) Replication filter rules to be applied at the DB System Channel target.

`tables_without_primary_key_handling`

(optional) Specifies how a replication channel handles the creation and alteration of tables that do not have a primary key. The default value is set to ALLOW.

`delay_in_seconds`

(optional) Specifies the amount of time, in seconds, that the channel waits before applying a transaction received from the source.

### DBMS_CLOUD_OCI_MYSQL_CREATE_CONFIGURATION_DETAILS_T Type

The details required to create a new Configuration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment.

`description`

(optional) User-provided data about the Configuration.

`display_name`

(optional) The display name of the Configuration.

`shape_name`

(required) The name of the associated Shape.

`init_variables`

(optional)

`variables`

(optional)

`parent_configuration_id`

(optional) The OCID of the Configuration from which the new Configuration is derived. The values in CreateConfigurationDetails.variables supersede the variables of the parent Configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_DETAILS_T Type

Parameters detailing how to provision the initial data of the system.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The specific source identifier.

Allowed values are: 'NONE', 'BACKUP', 'PITR', 'IMPORTURL'

### DBMS_CLOUD_OCI_MYSQL_CREATE_MAINTENANCE_DETAILS_T Type

The Maintenance Policy for the DB System or Read Replica that this model is included in.

Syntax
```

```

Fields

Field Description

`window_start_time`

(required) The start of the 2 hour maintenance window. This string is of the format: \"{day-of-week} {time-of-day}\". \"{day-of-week}\" is a case-insensitive string like \"mon\", \"tue\", &amp;c. \"{time-of-day}\" is the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero. If you set the read replica maintenance window to \"\" or if not specified, the read replica is set same as the DB system maintenance window.

### DBMS_CLOUD_OCI_MYSQL_CREATE_DELETION_POLICY_DETAILS_T Type

Policy for how the DB System and related resources should be handled at the time of its deletion.

Syntax
```

```

Fields

Field Description

`automatic_backup_retention`

(optional) Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.

Allowed values are: 'DELETE', 'RETAIN'

`final_backup`

(optional) Specifies whether or not a backup is taken when the DB System is deleted. REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted. SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted.

Allowed values are: 'SKIP_FINAL_BACKUP', 'REQUIRE_FINAL_BACKUP'

`is_delete_protected`

(optional) Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.

### DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_DETAILS_T Type

Details required to create a DB System.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the DB System. It does not have to be unique.

`description`

(optional) User-provided data about the DB System.

`compartment_id`

(required) The OCID of the compartment.

`is_highly_available`

(optional) Specifies if the DB System is highly available. When creating a DB System with High Availability, three instances are created and placed according to your region- and subnet-type. The secondaries are placed automatically in the other two availability or fault domains. You can choose the preferred location of your primary instance, only.

`availability_domain`

(optional) The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the availability domain in which the DB System is placed.

`fault_domain`

(optional) The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the fault domain in which the DB System is placed.

`configuration_id`

(optional) The OCID of the Configuration to be used for this DB System.

`shape_name`

(required) The name of the shape. The shape determines the resources allocated - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the`LIST_SHAPES`Function operation.

`mysql_version`

(optional) The specific MySQL version identifier.

`subnet_id`

(required) The OCID of the subnet the DB System is associated with.

`admin_username`

(optional) The username for the administrative user.

`admin_password`

(optional) The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.

`data_storage_size_in_g_bs`

(optional) Initial size of the data volume in GBs that will be created and attached. Keep in mind that this only specifies the size of the database data volume, the log volume for the database will be scaled appropriately with its shape.

`hostname_label`

(optional) The hostname for the primary endpoint of the DB System. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\"). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.

`ip_address`

(optional) The IP address the DB System is configured to listen on. A private IP address of your choice to assign to the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a \"dotted-quad\" style IPv4 address.

`port`

(optional) The port for primary endpoint of the DB System to listen on.

`port_x`

(optional) The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.

`backup_policy`

(optional)

`source`

(optional)

`maintenance`

(optional)

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`deletion_policy`

(optional)

`crash_recovery`

(optional) Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled, and whether to enable or disable syncing of the Binary Logs.

Allowed values are: 'ENABLED', 'DISABLED'

`database_management`

(optional) Whether to enable monitoring via the Database Management service.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_FROM_BACKUP_DETAILS_T Type

Use the backupId to specify from which backup the new DB System will be created.

Syntax
```

```

`dbms_cloud_oci_mysql_create_db_system_source_from_backup_details_t`is a subtype of the`dbms_cloud_oci_mysql_create_db_system_source_details_t`type.

Fields

Field Description

`backup_id`

(required) The OCID of the backup to be used as the source for the new DB System.

### DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_FROM_NONE_DETAILS_T Type

Creation of a DbSystem from no particular source.

Syntax
```

```

`dbms_cloud_oci_mysql_create_db_system_source_from_none_details_t`is a subtype of the`dbms_cloud_oci_mysql_create_db_system_source_details_t`type.

### DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_FROM_PITR_DETAILS_T Type

DB System OCID to perform a point in time recovery to the current point in time. DB System OCID and recovery point to perform a point in time recovery to the specified recovery point.

Syntax
```

```

`dbms_cloud_oci_mysql_create_db_system_source_from_pitr_details_t`is a subtype of the`dbms_cloud_oci_mysql_create_db_system_source_details_t`type.

Fields

Field Description

`db_system_id`

(required) The OCID of the DB System from which a backup shall be selected to be restored when creating the new DB System. Use this together with recovery point to perform a point in time recovery operation.

`recovery_point`

(optional) The date and time, as per RFC 3339, of the change up to which the new DB System shall be restored to, using a backup and logs from the original DB System. In case no point in time is specified, then this new DB System shall be restored up to the latest change recorded for the original DB System.

### DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_IMPORT_FROM_URL_DETAILS_T Type

An Object Storage PAR from which to import the DB System initial data.

Syntax
```

```

`dbms_cloud_oci_mysql_create_db_system_source_import_from_url_details_t`is a subtype of the`dbms_cloud_oci_mysql_create_db_system_source_details_t`type.

Fields

Field Description

`source_url`

(required) The Pre-Authenticated Request (PAR) of a bucket/prefix or PAR of a @.manifest.json object from the Object Storage. Check[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for information related to PAR creation. Please create PAR with \"Permit object reads\" access type and \"Enable Object Listing\" permission when using a bucket/prefix PAR. Please create PAR with \"Permit object reads\" access type when using a @.manifest.json object PAR.

### DBMS_CLOUD_OCI_MYSQL_REPLICA_OVERRIDES_T Type

By default a read replica inherits the MySQL version, shape, and configuration of the source DB system. If you want to override any of these, provide values in the properties, mysqlVersion, shapeName, and configurationId. If you set a property value to \"\", then the value is inherited from its source DB system.

Syntax
```

```

Fields

Field Description

`mysql_version`

(optional) The MySQL version to be used by the read replica.

`shape_name`

(optional) The shape to be used by the read replica. The shape determines the resources allocated: CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes. To get a list of shapes, use the`LIST_SHAPES`Function operation.

`configuration_id`

(optional) The OCID of the Configuration to be used by the read replica.

### DBMS_CLOUD_OCI_MYSQL_CREATE_REPLICA_DETAILS_T Type

Details required to create a read replica.

Syntax
```

```

Fields

Field Description

`db_system_id`

(required) The OCID of the DB System the read replica is associated with.

`display_name`

(optional) The user-friendly name for the read replica. It does not have to be unique.

`description`

(optional) User provided description of the read replica.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_delete_protected`

(optional) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete protected themselves.

`replica_overrides`

(optional)

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_PLACEMENT_T Type

The availability domain and fault domain a DB System is placed in.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain in which the DB System is placed.

`fault_domain`

(optional) The fault domain in which the DB System is placed.

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_SUMMARY_T Type

A summary of a HeatWave cluster.

Syntax
```

```

Fields

Field Description

`shape_name`

(required) The shape determines resources to allocate to the HeatWave nodes - CPU cores, memory.

`cluster_size`

(required) The number of analytics-processing compute instances, of the specified shape, in the HeatWave cluster.

`is_lakehouse_enabled`

(optional) Lakehouse enabled status for the HeatWave cluster.

`lifecycle_state`

(required) The current state of the MySQL HeatWave cluster.

`time_created`

(required) The date and time the HeatWave cluster was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(required) The time the HeatWave cluster was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_T Type

Parameters detailing how to provision the initial data of the DB System.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The specific source identifier.

Allowed values are: 'NONE', 'BACKUP', 'PITR', 'IMPORTURL'

### DBMS_CLOUD_OCI_MYSQL_POINT_IN_TIME_RECOVERY_DETAILS_T Type

Point-in-time Recovery details like earliest and latest recovery time point for the DB System.

Syntax
```

```

Fields

Field Description

`time_earliest_recovery_point`

(required) Earliest recovery time point for the DB System, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_latest_recovery_point`

(required) Latest recovery time point for the DB System, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_MYSQL_CHANNEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_mysql_channel_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_T Type

A DB System is the core logical unit of MySQL Database Service.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DB System.

`display_name`

(required) The user-friendly name for the DB System. It does not have to be unique.

`description`

(optional) User-provided data about the DB System.

`compartment_id`

(required) The OCID of the compartment the DB System belongs in.

`subnet_id`

(required) The OCID of the subnet the DB System is associated with.

`is_highly_available`

(optional) Specifies if the DB System is highly available.

`current_placement`

(optional)

`is_heat_wave_cluster_attached`

(optional) If the DB System has a HeatWave Cluster attached.

`heat_wave_cluster`

(optional)

`availability_domain`

(optional) The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the availability domain in which the DB System is placed.

`fault_domain`

(optional) The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the fault domain in which the DB System is placed.

`shape_name`

(optional) The shape of the primary instances of the DB System. The shape determines resources allocated to a DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use (the`LIST_SHAPES`Function operation.

`mysql_version`

(required) Name of the MySQL Version in use for the DB System.

`backup_policy`

(optional)

`source`

(optional)

`configuration_id`

(optional) The OCID of the Configuration to be used for Instances in this DB System.

`data_storage_size_in_g_bs`

(required) Initial size of the data volume in GiBs that will be created and attached.

`hostname_label`

(optional) The hostname for the primary endpoint of the DB System. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\"). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.

`ip_address`

(optional) The IP address the DB System is configured to listen on. A private IP address of the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. This will be a \"dotted-quad\" style IPv4 address.

`port`

(optional) The port for primary endpoint of the DB System to listen on.

`port_x`

(optional) The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.

`endpoints`

(optional) The network endpoints available for this DB System.

`channels`

(optional) A list with a summary of all the Channels attached to the DB System.

`lifecycle_state`

(required) The current state of the DB System.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycleState.

`maintenance`

(required)

`deletion_policy`

(required)

`time_created`

(required) The date and time the DB System was created.

`time_updated`

(required) The time the DB System was last updated.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`crash_recovery`

(optional) Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled, and whether to enable or disable syncing of the Binary Logs.

Allowed values are: 'ENABLED', 'DISABLED'

`point_in_time_recovery_details`

(optional)

`database_management`

(optional) Whether to enable monitoring via the Database Management service.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_FROM_BACKUP_T Type

From which backup this DB System was created.

Syntax
```

```

`dbms_cloud_oci_mysql_db_system_source_from_backup_t`is a subtype of the`dbms_cloud_oci_mysql_db_system_source_t`type.

Fields

Field Description

`backup_id`

(required) The OCID of the backup to be used as the source for the new DB System.

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_FROM_NONE_T Type

A DB System created from no particular external source.

Syntax
```

```

`dbms_cloud_oci_mysql_db_system_source_from_none_t`is a subtype of the`dbms_cloud_oci_mysql_db_system_source_t`type.

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_FROM_PITR_T Type

DB System OCID to perform a point in time recovery to the current point in time. DB System OCID and recovery point to perform a point in time recovery to the specified recovery point.

Syntax
```

```

`dbms_cloud_oci_mysql_db_system_source_from_pitr_t`is a subtype of the`dbms_cloud_oci_mysql_db_system_source_t`type.

Fields

Field Description

`db_system_id`

(required) The OCID of the DB System from which a backup shall be selected to be restored when creating the new DB System. Use this together with recovery point to perform a point in time recovery operation.

`recovery_point`

(optional) The date and time, as per RFC 3339, of the change up to which the new DB System shall be restored to, using a backup and logs from the original DB System. In case no point in time is specified, then this new DB System shall be restored up to the latest change recorded for the original DB System.

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_IMPORT_FROM_URL_T Type

An Object Storage PAR from which to import the DB System initial data.

Syntax
```

```

`dbms_cloud_oci_mysql_db_system_source_import_from_url_t`is a subtype of the`dbms_cloud_oci_mysql_db_system_source_t`type.

### DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SUMMARY_T Type

A summary of a DB System.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the DB System.

`display_name`

(required) The user-friendly name for the DB System. It does not have to be unique.

`description`

(optional) User-provided data about the DB System.

`compartment_id`

(optional) The OCID of the compartment the DB System belongs in.

`is_highly_available`

(optional) Specifies if the DB System is highly available.

`current_placement`

(optional)

`is_heat_wave_cluster_attached`

(optional) If the DB System has a HeatWave Cluster attached.

`heat_wave_cluster`

(optional)

`availability_domain`

(optional) The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the availability domain in which the DB System is placed.

`fault_domain`

(optional) The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the fault domain in which the DB System is placed.

`endpoints`

(optional) The network endpoints available for this DB System.

`lifecycle_state`

(required) The current state of the DB System.

`mysql_version`

(required) Name of the MySQL Version in use for the DB System.

`time_created`

(required) The date and time the DB System was created.

`time_updated`

(required) The time the DB System was last updated.

`deletion_policy`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`backup_policy`

(optional)

`shape_name`

(optional) The shape of the primary instances of the DB System. The shape determines resources allocated to a DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use (the`LIST_SHAPES`Function operation.

`crash_recovery`

(optional) Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled, and whether to enable or disable syncing of the Binary Logs.

Allowed values are: 'ENABLED', 'DISABLED'

`database_management`

(optional) Whether to enable monitoring via the Database Management service.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_MYSQL_ERROR_T Type

Sorry.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_MYSQL_ERROR_ON_ANONYMOUS_HANDLING_T Type

Disables assignment of IDs to anonymous transactions coming from the source. Use this policy when the transaction identifiers are enabled in the source of the replication channel.

Syntax
```

```

`dbms_cloud_oci_mysql_error_on_anonymous_handling_t`is a subtype of the`dbms_cloud_oci_mysql_anonymous_transactions_handling_t`type.

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_NODE_T Type

A HeatWave node is a compute host that is part of a HeatWave cluster.

Syntax
```

```

Fields

Field Description

`node_id`

(required) The ID of the node within MySQL HeatWave cluster.

`lifecycle_state`

(required) The current state of the MySQL HeatWave node.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(optional) The date and time the MySQL HeatWave node was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The date and time the MySQL HeatWave node was updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_NODE_TBL Type

Nested table type of dbms_cloud_oci_mysql_heat_wave_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_T Type

A HeatWave cluster is a database accelerator for a DB System.

Syntax
```

```

Fields

Field Description

`db_system_id`

(required) The OCID of the parent DB System this HeatWave cluster is attached to.

`shape_name`

(required) The shape determines resources to allocate to the HeatWave nodes - CPU cores, memory.

`cluster_size`

(required) The number of analytics-processing compute instances, of the specified shape, in the HeatWave cluster.

`is_lakehouse_enabled`

(optional) Lakehouse enabled status for the HeatWave cluster.

`cluster_nodes`

(required) A HeatWave node is a compute host that is part of a HeatWave cluster.

`lifecycle_state`

(required) The current state of the HeatWave cluster.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional information about the current lifecycleState.

`time_created`

(required) The date and time the HeatWave cluster was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(required) The time the HeatWave cluster was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_TABLE_MEMORY_ESTIMATE_T Type

Estimated memory footprint for a MySQL user table when loaded to the HeatWave cluster memory.

Syntax
```

```

Fields

Field Description

`table_name`

(required) The table name.

`to_load_column_count`

(required) The number of columns to be loaded to HeatWave cluster memory. These columns contribute to the analytical memory footprint.

`varlen_column_count`

(required) The number of variable-length columns to be loaded to HeatWave cluster memory. These columns contribute to the analytical memory footprint.

`estimated_row_count`

(required) The estimated number of rows in the table. This number was used to derive the analytical memory footprint.

`analytical_footprint_in_mbs`

(required) The estimated memory footprint of the table in MBs when loaded to HeatWave cluster memory (null if the table cannot be loaded to the HeatWave cluster).

`error_comment`

(required) Error comment (empty string if no errors occured).

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_TABLE_MEMORY_ESTIMATE_TBL Type

Nested table type of dbms_cloud_oci_mysql_heat_wave_cluster_table_memory_estimate_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_SCHEMA_MEMORY_ESTIMATE_T Type

Schema with estimated memory footprints for each MySQL user table of the schema when loaded to HeatWave cluster memory.

Syntax
```

```

Fields

Field Description

`schema_name`

(required) The name of the schema.

`per_table_estimates`

(required) Estimated memory footprints for MySQL user tables of the schema when loaded to HeatWave cluster memory.

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_SCHEMA_MEMORY_ESTIMATE_TBL Type

Nested table type of dbms_cloud_oci_mysql_heat_wave_cluster_schema_memory_estimate_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_MEMORY_ESTIMATE_T Type

HeatWave cluster memory estimate that can be used to determine a suitable HeatWave cluster size. For each MySQL user table the estimated memory footprint when the table is loaded to the HeatWave cluster memory is returned.

Syntax
```

```

Fields

Field Description

`db_system_id`

(required) The OCID of the DB System the HeatWave cluster memory estimate is associated with.

`status`

(required) Current status of the Work Request generating the HeatWave cluster memory estimate.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`time_created`

(required) The date and time that the Work Request to generate the HeatWave cluster memory estimate was issued, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc333).

`time_updated`

(required) The date and time that the HeatWave cluster memory estimate was generated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc333).

`table_schemas`

(required) Collection of schemas with estimated memory footprints for MySQL user tables of each schema when loaded to HeatWave cluster memory.

### DBMS_CLOUD_OCI_MYSQL_PEM_CA_CERTIFICATE_T Type

The CA certificate in PEM format.

Syntax
```

```

`dbms_cloud_oci_mysql_pem_ca_certificate_t`is a subtype of the`dbms_cloud_oci_mysql_ca_certificate_t`type.

Fields

Field Description

`contents`

(required) The string containing the CA certificate in PEM format.

### DBMS_CLOUD_OCI_MYSQL_REPLICA_T Type

A DB System read replica.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the read replica.

`db_system_id`

(required) The OCID of the DB System the read replica is associated with.

`compartment_id`

(required) The OCID of the compartment that contains the read replica.

`display_name`

(required) The user-friendly name for the read replica. It does not have to be unique.

`description`

(optional) User provided description of the read replica.

`lifecycle_state`

(required) The state of the read replica.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'NEEDS_ATTENTION', 'FAILED'

`lifecycle_details`

(optional) A message describing the state of the read replica.

`time_created`

(required) The date and time the read replica was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The time the read replica was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`mysql_version`

(required) The MySQL version currently in use by the read replica.

`availability_domain`

(optional) The name of the Availability Domain the read replica is located in.

`fault_domain`

(optional) The name of the Fault Domain the read replica is located in.

`ip_address`

(required) The IP address the read replica is configured to listen on.

`port`

(required) The port the read replica is configured to listen on.

`port_x`

(required) The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_delete_protected`

(optional) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete protected themselves.

`shape_name`

(optional) The shape currently in use by the read replica. The shape determines the resources allocated: CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes. To get a list of shapes, use the`LIST_SHAPES`Function operation.

`configuration_id`

(optional) The OCID of the Configuration currently in use by the read replica.

`replica_overrides`

(optional)

### DBMS_CLOUD_OCI_MYSQL_REPLICA_SUMMARY_T Type

Summary of the read replica.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the read replica.

`db_system_id`

(required) The OCID of the DB System the read replica is associated with.

`compartment_id`

(required) The OCID of the compartment that contains the read replica.

`display_name`

(required) The user-friendly name for the read replica. It does not have to be unique.

`description`

(optional) User provided description of the read replica.

`lifecycle_state`

(required) The state of the read replica.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'NEEDS_ATTENTION', 'FAILED'

`lifecycle_details`

(optional) A message describing the state of the read replica.

`time_created`

(required) The date and time the read replica was created, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The time the read replica was last updated, as described by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`mysql_version`

(required) The MySQL version currently in use by the read replica.

`availability_domain`

(optional) The name of the Availability Domain the read replica is located in.

`fault_domain`

(optional) The name of the Fault Domain the read replica is located in.

`ip_address`

(required) The IP address the read replica is configured to listen on.

`port`

(required) The port the read replica is configured to listen on.

`port_x`

(required) The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_delete_protected`

(optional) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete protected themselves.

`shape_name`

(optional) The shape currently in use by the read replica. The shape determines the resources allocated: CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes. To get a list of shapes, use the`LIST_SHAPES`Function operation.

`configuration_id`

(optional) The OCID of the Configuration currently in use by the read replica.

`replica_overrides`

(optional)

### DBMS_CLOUD_OCI_MYSQL_RESTART_DB_SYSTEM_DETAILS_T Type

DB System restart parameters.

Syntax
```

```

Fields

Field Description

`shutdown_type`

(required) The InnoDB shutdown mode to use, following the option \"[innodb_fast_shutdown](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_fast_shutdown)\".

Allowed values are: 'IMMEDIATE', 'FAST', 'SLOW'

### DBMS_CLOUD_OCI_MYSQL_SHAPE_SUMMARY_T Type

The shape of the DB System. The shape determines resources to allocate to the DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. For a description of shapes, see[DB System Shape Options](https://docs.oracle.com/iaas/mysql-database/doc/db-systems.html#GUID-E2A83218-9700-4A49-B55D-987867D81871).

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the shape used for the DB System.

`cpu_core_count`

(required) The number of CPU Cores the Instance provides. These are \"OCPU\"s.

`memory_size_in_g_bs`

(required) The amount of RAM the Instance provides. This is an IEC base-2 number.

`is_supported_for`

(optional) What service features the shape is supported for.

Allowed values are: 'DBSYSTEM', 'HEATWAVECLUSTER'

### DBMS_CLOUD_OCI_MYSQL_STOP_DB_SYSTEM_DETAILS_T Type

DB System shutdown parameters.

Syntax
```

```

Fields

Field Description

`shutdown_type`

(required) The InnoDB shutdown mode to use, following the option \"[innodb_fast_shutdown](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_fast_shutdown)\".

Allowed values are: 'IMMEDIATE', 'FAST', 'SLOW'

### DBMS_CLOUD_OCI_MYSQL_UPDATE_BACKUP_DETAILS_T Type

The Backup metadata which can be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-supplied display name for the backup.

`description`

(optional) A user-supplied description for the backup.

`retention_in_days`

(optional) The number of days backups are retained.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_UPDATE_BACKUP_POLICY_DETAILS_T Type

Backup Policy as optionally used for DB System update.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Specifies if automatic backups are enabled.

`window_start_time`

(optional) The start of a 30-minute window of time in which daily, automated backups occur. This should be in the format of the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero. At some point in the window, the system may incur a brief service disruption as the backup is performed.

`retention_in_days`

(optional) Number of days to retain an automatic backup.

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`pitr_policy`

(optional)

### DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_SOURCE_DETAILS_T Type

Parameters detailing how to provision the source for the given Channel.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The specific source identifier.

### DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_TARGET_DETAILS_T Type

Parameters detailing how to provision the target for the given Channel.

Syntax
```

```

Fields

Field Description

`target_type`

(required) The specific targetType identifier.

### DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_DETAILS_T Type

Details required to update a Channel

Syntax
```

```

Fields

Field Description

`source`

(optional)

`target`

(optional)

`display_name`

(optional) The user-friendly name for the Channel. It does not have to be unique.

`is_enabled`

(optional) Whether the Channel should be enabled or disabled. Enabling a previously disabled Channel will cause the Channel to be started. Conversely, disabling a previously enabled Channel will stop the Channel. Both operations are executed asynchronously.

`description`

(optional) User provided description of the Channel.

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_SOURCE_FROM_MYSQL_DETAILS_T Type

Parameters detailing how to provision the source endpoint that is a MySQL Server. Typically a MySQL Server that is not managed by the MySQL Database Service.

Syntax
```

```

`dbms_cloud_oci_mysql_update_channel_source_from_mysql_details_t`is a subtype of the`dbms_cloud_oci_mysql_update_channel_source_details_t`type.

Fields

Field Description

`hostname`

(optional) The network address of the MySQL instance.

`port`

(optional) The port the source MySQL instance listens on.

`username`

(optional) The name of the replication user on the source MySQL instance. The username has a maximum length of 96 characters. For more information, please see the[MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)

`password`

(optional) The password for the replication user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.

`ssl_mode`

(optional) The SSL mode of the Channel.

`ssl_ca_certificate`

(optional)

`anonymous_transactions_handling`

(optional)

### DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_TARGET_FROM_DB_SYSTEM_DETAILS_T Type

Parameters detailing how to provision the target endpoint that is a DB System.

Syntax
```

```

`dbms_cloud_oci_mysql_update_channel_target_from_db_system_details_t`is a subtype of the`dbms_cloud_oci_mysql_update_channel_target_details_t`type.

Fields

Field Description

`channel_name`

(optional) The case-insensitive name that identifies the replication channel. Channel names must follow the rules defined for[MySQL identifiers](https://dev.mysql.com/doc/refman/8.0/en/identifiers.html). The names of non-Deleted Channels must be unique for each DB System.

`applier_username`

(optional) The username for the replication applier of the target MySQL DB System.

`filters`

(optional) Replication filter rules to be applied at the DB System Channel target.

`tables_without_primary_key_handling`

(optional) Specifies how a replication channel handles the creation and alteration of tables that do not have a primary key.

`delay_in_seconds`

(optional) Specifies the amount of time, in seconds, that the channel waits before applying a transaction received from the source.

### DBMS_CLOUD_OCI_MYSQL_UPDATE_CONFIGURATION_DETAILS_T Type

The details required to update a Configuration.

Syntax
```

```

Fields

Field Description

`description`

(optional) User-provided data about the Configuration.

`display_name`

(optional) A new display name for the Configuration.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MYSQL_UPDATE_MAINTENANCE_DETAILS_T Type

The Maintenance Policy for the DB System or Read Replica that this model is included in.

Syntax
```

```

Fields

Field Description

`window_start_time`

(optional) The start of the 2 hour maintenance window. This string is of the format: \"{day-of-week} {time-of-day}\". \"{day-of-week}\" is a case-insensitive string like \"mon\", \"tue\", &amp;c. \"{time-of-day}\" is the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero. If you set the read replica maintenance window to \"\", the read replica is set same as the DB system maintenance window. If not specific by the user, there will be no changes to the maintenace window.

### DBMS_CLOUD_OCI_MYSQL_UPDATE_DELETION_POLICY_DETAILS_T Type

Policy for how the DB System and related resources should be handled at the time of its deletion.

Syntax
```

```

Fields

Field Description

`automatic_backup_retention`

(optional) Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.

Allowed values are: 'DELETE', 'RETAIN'

`final_backup`

(optional) Specifies whether or not a backup is taken when the DB System is deleted. REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted. SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted.

Allowed values are: 'SKIP_FINAL_BACKUP', 'REQUIRE_FINAL_BACKUP'

`is_delete_protected`

(optional) Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.

### DBMS_CLOUD_OCI_MYSQL_UPDATE_DB_SYSTEM_DETAILS_T Type

Details required to update a DB System.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the DB System. It does not have to be unique.

`description`

(optional) User-provided data about the DB System.

`subnet_id`

(optional) The OCID of the subnet the DB System is associated with.

`is_highly_available`

(optional) Specifies if the DB System is highly available. Set to true to enable high availability. Two secondary MySQL instances are created and placed in the unused availability or fault domains, depending on your region and subnet type. Set to false to disable high availability. The secondary MySQL instances are removed and the MySQL instance in the preferred location is used.

`availability_domain`

(optional) The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the availability domain in which the DB System is placed.

`fault_domain`

(optional) The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance. In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains and the MySQL instance in that domain is promoted to the primary instance. This redirection does not affect the IP address of the DB System in any way. For a standalone DB System, this defines the fault domain in which the DB System is placed.

`shape_name`

(optional) The shape of the DB System. The shape determines resources allocated to the DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the`LIST_SHAPES`Function operation. Changes in Shape will result in a downtime as the MySQL DB System is migrated to the new Compute instance.

`mysql_version`

(optional) The specific MySQL version identifier.

`configuration_id`

(optional) The OCID of the Configuration to be used for Instances in this DB System.

`admin_username`

(optional) The username for the administrative user for the MySQL Instance.

`admin_password`

(optional) The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.

`data_storage_size_in_g_bs`

(optional) Expands the DB System's storage to the specified value. Only supports values larger than the current DB System's storage size. DB Systems with an initial storage size of 400 GB or less can be expanded up to 32 TB. DB Systems with an initial storage size between 401-800 GB can be expanded up to 64 TB. DB Systems with an initial storage size between 801-1200 GB can be expanded up to 96 TB. DB Systems with an initial storage size of 1201 GB or more can be expanded up to 128 TB. It is not possible to decrease data storage size.

`hostname_label`

(optional) The hostname for the primary endpoint of the DB System. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\"). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.

`ip_address`

(optional) The IP address the DB System should be configured to listen on the provided subnet. It must be a free private IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a \"dotted-quad\" style IPv4 address.

`port`

(optional) The port for primary endpoint of the DB System to listen on.

`port_x`

(optional) The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.

`backup_policy`

(optional)

`maintenance`

(optional)

`freeform_tags`

(optional) Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`deletion_policy`

(optional)

`crash_recovery`

(optional) Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled, and whether to enable or disable syncing of the Binary Logs.

Allowed values are: 'ENABLED', 'DISABLED'

`database_management`

(optional) Whether to enable monitoring via the Database Management service.

Allowed values are: 'ENABLED', 'DISABLED'

### DBMS_CLOUD_OCI_MYSQL_UPDATE_HEAT_WAVE_CLUSTER_DETAILS_T Type

Details about the HeatWave cluster properties to be updated.

Syntax
```

```

Fields

Field Description

`shape_name`

(optional) A change to the shape of the nodes in the HeatWave cluster will result in the entire cluster being torn down and re-created with Compute instances of the new Shape. This may result in significant downtime for the analytics capability while the HeatWave cluster is re-provisioned.

`cluster_size`

(optional) A change to the number of nodes in the HeatWave cluster will result in the entire cluster being torn down and re-created with the new cluster of nodes. This may result in a significant downtime for the analytics capability while the HeatWave cluster is re-provisioned.

`is_lakehouse_enabled`

(optional) Enable/disable Lakehouse for the HeatWave cluster.

### DBMS_CLOUD_OCI_MYSQL_UPDATE_REPLICA_DETAILS_T Type

Details required to update a read replica.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The user-friendly name for the read replica. It does not have to be unique.

`description`

(optional) User provided description of the read replica.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_delete_protected`

(optional) Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow. Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If the DB System is delete protected, read replicas can still be deleted individually if they are not delete protected themselves.

`replica_overrides`

(optional)

### DBMS_CLOUD_OCI_MYSQL_VERSION_T Type

A supported MySQL Version.

Syntax
```

```

Fields

Field Description

`version`

(optional) The specific version identifier

`description`

(optional) A link to a page describing the version.

### DBMS_CLOUD_OCI_MYSQL_VERSION_TBL Type

Nested table type of dbms_cloud_oci_mysql_version_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_VERSION_SUMMARY_T Type

A summary of the supported MySQL Versions families, and a list of their supported minor versions.

Syntax
```

```

Fields

Field Description

`version_family`

(optional) A descriptive summary of a group of versions.

`versions`

(required) The list of supported MySQL Versions.

### DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path the user can do a GET on to access the resource.

### DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_mysql_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_T Type

The status of an asynchronous task in the system.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the work request.

`operation_type`

(required) the original operation ID requested

Allowed values are: 'CREATE_DBSYSTEM', 'UPDATE_DBSYSTEM', 'DELETE_DBSYSTEM', 'START_DBSYSTEM', 'STOP_DBSYSTEM', 'RESTART_DBSYSTEM', 'ADD_HEATWAVE_CLUSTER', 'UPDATE_HEATWAVE_CLUSTER', 'DELETE_HEATWAVE_CLUSTER', 'START_HEATWAVE_CLUSTER', 'STOP_HEATWAVE_CLUSTER', 'RESTART_HEATWAVE_CLUSTER', 'GENERATE_HEATWAVE_CLUSTER_MEMORY_ESTIMATE', 'CREATE_REPLICA', 'UPDATE_REPLICA', 'DELETE_REPLICA', 'CREATE_CHANNEL', 'UPDATE_CHANNEL', 'RESUME_CHANNEL', 'RESET_CHANNEL', 'DELETE_CHANNEL'

`status`

(required) Current status of the work request

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

### DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_SUMMARY_T Type

The status of an asynchronous task in the system.

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the work request.

`operation_type`

(required) the original operation ID requested

Allowed values are: 'CREATE_DBSYSTEM', 'UPDATE_DBSYSTEM', 'DELETE_DBSYSTEM', 'START_DBSYSTEM', 'STOP_DBSYSTEM', 'RESTART_DBSYSTEM', 'ADD_HEATWAVE_CLUSTER', 'UPDATE_HEATWAVE_CLUSTER', 'DELETE_HEATWAVE_CLUSTER', 'START_HEATWAVE_CLUSTER', 'STOP_HEATWAVE_CLUSTER', 'RESTART_HEATWAVE_CLUSTER', 'GENERATE_HEATWAVE_CLUSTER_MEMORY_ESTIMATE', 'CREATE_REPLICA', 'UPDATE_REPLICA', 'DELETE_REPLICA', 'CREATE_CHANNEL', 'UPDATE_CHANNEL', 'RESUME_CHANNEL', 'RESET_CHANNEL', 'DELETE_CHANNEL'

`status`

(required) Current status of the work request

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

- [MySQL Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-BA1F38E0-29D8-4EE6-A41F-BCEE60EB830D)
- [DBMS_CLOUD_OCI_MYSQL_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-CB55BFEE-710D-45AD-9388-8EA9113234C6)
- [DBMS_CLOUD_OCI_MYSQL_ADD_HEAT_WAVE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-5809DCD1-9E07-4DEA-B4CB-5E91C71935AE)
- [DBMS_CLOUD_OCI_MYSQL_ANONYMOUS_TRANSACTIONS_HANDLING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-1E0649E2-A7DF-4A81-BDF5-77C5E1A15730)
- [DBMS_CLOUD_OCI_MYSQL_ASSIGN_MANUAL_UUID_HANDLING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-E73B028A-3BA0-4CAF-9A8B-4DC7E3562068)
- [DBMS_CLOUD_OCI_MYSQL_ASSIGN_TARGET_UUID_HANDLING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3C40C7A4-8F60-4106-B72F-626A511B8212)
- [DBMS_CLOUD_OCI_MYSQL_PITR_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3A3F4790-DD62-4543-B47D-46CD6894A2F6)
- [DBMS_CLOUD_OCI_MYSQL_BACKUP_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-FFF051A1-C71F-4161-8A44-1B599237C8A0)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3BC18B2D-754B-46E3-AA0A-0D9A040A67B4)
- [DBMS_CLOUD_OCI_MYSQL_MAINTENANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3878187C-0F74-4015-9368-9BC575A65DB4)
- [DBMS_CLOUD_OCI_MYSQL_DELETION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-ED8AD340-EEE1-4D56-A509-DD25032D301D)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_ENDPOINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-8D63C6D6-FC98-4A12-87EA-3C68FA3C1C32)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SNAPSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-C4B21F0B-C02D-4F98-A216-3E6E688442FD)
- [DBMS_CLOUD_OCI_MYSQL_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-30709AEA-C5F4-4041-B6BF-9067591B7C77)
- [DBMS_CLOUD_OCI_MYSQL_BACKUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-D9175725-C580-42CF-82E7-A04B899DE4E7)
- [DBMS_CLOUD_OCI_MYSQL_CA_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-367324DD-FBE8-4E7B-ABF6-A9B6ACA66673)
- [DBMS_CLOUD_OCI_MYSQL_CHANGE_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-48D2A89C-4AE9-4ED6-A4BF-3C19FC77B769)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-8158EA67-F22F-47F9-B099-2B9DB75D4264)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-992DA7C7-4C92-4902-9678-0222C8EF66B8)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-9E87D566-93BC-40BE-B7DF-3983FAFB6996)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-C52AF3FD-43C3-4952-AFD9-2750F70E60D1)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_SOURCE_MYSQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-A1F6CF31-1242-4ADF-B7A0-3AB4AC4A2C9D)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-B366BF61-DF8A-4CDD-9310-2912249315F7)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-09E098B4-F59E-4DA0-B884-2CA6195C488F)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_TARGET_DB_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-F336B84A-3FB0-45A9-8970-B23490F00F89)
- [DBMS_CLOUD_OCI_MYSQL_INITIALIZATION_VARIABLES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-C334ADE2-D911-4FE5-A428-644EF97812D2)
- [DBMS_CLOUD_OCI_MYSQL_CONFIGURATION_VARIABLES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-2C4164E0-9DB4-434E-AEC0-CCFCC723EBB3)
- [DBMS_CLOUD_OCI_MYSQL_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-43941B51-E6DB-4E83-AD01-90BBCDC374C1)
- [DBMS_CLOUD_OCI_MYSQL_CONFIGURATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-74009217-95D1-4981-8077-25834667C2C9)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-B0CC0080-2C06-4AEB-8474-CF54F7294950)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_BACKUP_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-41429585-1E0A-4FF0-ABB8-F01239360825)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-441ED989-3420-43CA-B556-7F5A4AB61C53)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-26F66AE9-5809-41E9-942A-A8BD92BDBA0A)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-0B8B22F9-B18B-4DE1-91AF-312CCE561A32)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_SOURCE_FROM_MYSQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-FE2BF0C3-84F4-42FF-9689-8C3DAD2F3C0D)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_CHANNEL_TARGET_FROM_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-0EF25B1A-D042-4C08-9E83-083658F37786)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-9BFBD57E-E7BF-4F0B-9446-99829A0629E1)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3836D28D-6162-483A-B39A-3E29038106B5)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_MAINTENANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-D985A882-1520-4A25-8648-D9B9F15ED411)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DELETION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-BAF38E97-8BBF-4A94-952C-29EA0F022905)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-FF45DA45-A6ED-4099-9903-30E9BFC9D347)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_FROM_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-B3106118-23C7-4DDF-A2B7-E4ED7496A777)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_FROM_NONE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-32B050BB-04FC-402A-8A6A-ED7B5C80B50E)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_FROM_PITR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-C2B7BBF0-9167-4740-946D-E41CA33461E7)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_DB_SYSTEM_SOURCE_IMPORT_FROM_URL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-91A0A866-DB75-46A9-A3CD-35D721B1E0C8)
- [DBMS_CLOUD_OCI_MYSQL_REPLICA_OVERRIDES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-9C78BC69-79BA-465E-8588-BF6D51D9D137)
- [DBMS_CLOUD_OCI_MYSQL_CREATE_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-E4A265F2-6F67-4287-A267-2A93455883E2)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_PLACEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-CE65785F-416A-46DB-ADE2-057EEE6781F8)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-58C77715-29DA-42F5-9D0D-2D25E9F8BF8D)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-A985A417-1488-464B-ABAE-783974608BAF)
- [DBMS_CLOUD_OCI_MYSQL_POINT_IN_TIME_RECOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-B585E1EA-7050-4689-BA42-24711A95830E)
- [DBMS_CLOUD_OCI_MYSQL_CHANNEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-D4AD4F8B-856E-44E2-B94B-3BE13DE4F143)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-2BBC4309-1B45-48E1-A489-B2436D364946)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_FROM_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-A62A5F31-1852-483D-B2CC-3FB3D53C0ACA)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_FROM_NONE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-BD828BE8-6A0D-4811-AA2C-C2009F1490AB)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_FROM_PITR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-98B0B5DF-ECB9-40CF-BB2E-DBB8D6D0C27B)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SOURCE_IMPORT_FROM_URL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-2C6C407E-6D4D-4114-ACBB-013F258A7B53)
- [DBMS_CLOUD_OCI_MYSQL_DB_SYSTEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-48EF61C5-CD78-4196-B289-B14749A8F905)
- [DBMS_CLOUD_OCI_MYSQL_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-1F6F7DD8-10D7-45DE-A222-72C8DC95ADDC)
- [DBMS_CLOUD_OCI_MYSQL_ERROR_ON_ANONYMOUS_HANDLING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-A379A8DC-88E0-4567-9453-8D9272E5313B)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-446A8D28-6AD3-4AF8-941D-4F0AD148FE5A)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-AA763EE9-DA8B-4449-BF4F-FE4F42C46287)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-27A0F370-562E-4533-B7FC-8985C164A52B)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_TABLE_MEMORY_ESTIMATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-5EBA2ACA-1206-4465-9CF6-487C30824072)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_TABLE_MEMORY_ESTIMATE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-8C4873BB-3884-4975-B4BA-4A7E894D0164)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_SCHEMA_MEMORY_ESTIMATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-45491E5E-3B6D-4754-A288-83236986E683)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_SCHEMA_MEMORY_ESTIMATE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-34C14EC0-238C-494D-8E0A-CFA06EFC2973)
- [DBMS_CLOUD_OCI_MYSQL_HEAT_WAVE_CLUSTER_MEMORY_ESTIMATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-6726CA36-C7E2-43D1-84AB-06F202D6AA66)
- [DBMS_CLOUD_OCI_MYSQL_PEM_CA_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-276F5F22-9B3B-47E1-97BF-6E90717DB33A)
- [DBMS_CLOUD_OCI_MYSQL_REPLICA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-40660F85-44A2-4F1A-995D-BE31DE0331A2)
- [DBMS_CLOUD_OCI_MYSQL_REPLICA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-2EFDB248-CDD5-4F1E-A0F2-23AB15A92442)
- [DBMS_CLOUD_OCI_MYSQL_RESTART_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-BDD28FE5-173D-4971-835D-E9EDC7BE181C)
- [DBMS_CLOUD_OCI_MYSQL_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-7347390B-E9EE-4117-970B-31305770E3B0)
- [DBMS_CLOUD_OCI_MYSQL_STOP_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-18A72ABB-FF98-4ED5-8432-9555656DC77C)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-EB1C0FF0-EE10-4468-B52A-CCC2A708A19B)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_BACKUP_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-D82F7B19-16C8-495A-A13A-E2ED051B722A)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-0B963408-ABB9-4A86-B604-B9A363259412)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-42470308-4238-4466-B26B-0DD6429AC87B)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-94A959EA-E19C-421C-A5AC-C79532CA81DA)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_SOURCE_FROM_MYSQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-00DAFEDA-CBF4-48B7-8977-2976866D9C78)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_CHANNEL_TARGET_FROM_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-8A26E316-2BEC-481D-9899-01EDCD60805A)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-D83D7878-E9F4-4CAB-8E92-06332E859BB9)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_MAINTENANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-E8901B1F-2DBA-4093-9829-1A010E088AFE)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_DELETION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-45DB50E6-467C-456A-ABE8-B3B3416E793E)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_DB_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-1C5B0EFD-16A5-4A3F-8BF3-8454B4BF4834)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_HEAT_WAVE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3C0A1B74-CD94-441E-8834-21BE746DFAA2)
- [DBMS_CLOUD_OCI_MYSQL_UPDATE_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-5E6CC058-3CC3-47B2-94BA-97D2A8B0129E)
- [DBMS_CLOUD_OCI_MYSQL_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-25D2F05A-7BF8-4E52-A865-03923462BAD4)
- [DBMS_CLOUD_OCI_MYSQL_VERSION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-44B10C4D-8E79-43D0-8A69-EE7688E55988)
- [DBMS_CLOUD_OCI_MYSQL_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-082760A3-4620-49A4-87D4-A2CCA0168E1F)
- [DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-E186D223-B3ED-46DB-94DE-CC9A809BE12A)
- [DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-C071CC23-6D3B-46A8-834A-A9B677B23DBC)
- [DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-CCCB6543-92AE-4EB9-8D59-5E1C4F78919D)
- [DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-4C140524-60F1-43FA-B4DF-7FE1CDAF30ED)
- [DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-3827B151-1197-42F0-A901-E0189A1B5ABD)
- [DBMS_CLOUD_OCI_MYSQL_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/mysql_t.html#ADSDK-GUID-E4663DE5-6306-457F-962F-8F1501F653AB)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
