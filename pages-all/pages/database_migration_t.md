# Database Migrations Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#dcoc-content-body)

## Database Migrations Common Types

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_TARGET_TYPE_TABLESPACE_DETAILS_T Type

Migration tablespace settings.

Syntax
```

```

Fields

Field Description

`target_type`

(required) Type of Database Base Migration Target.

Allowed values are: 'ADB_S_REMAP', 'ADB_D_REMAP', 'ADB_D_AUTOCREATE', 'NON_ADB_REMAP', 'NON_ADB_AUTOCREATE'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADB_DEDICATED_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using auto create feature

Syntax
```

```

`dbms_cloud_oci_database_migration_adb_dedicated_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_target_type_tablespace_details_t`type.

Fields

Field Description

`is_auto_create`

(optional) True to auto-create tablespace in the target Database.

`is_big_file`

(optional) True set tablespace to big file.

`extend_size_in_m_bs`

(optional) Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.

`block_size_in_k_bs`

(optional) Size of Oracle database blocks in KB.

Allowed values are: 'SIZE_8K', 'SIZE_16K'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADB_DEDICATED_REMAP_TARGET_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using remap feature

Syntax
```

```

`dbms_cloud_oci_database_migration_adb_dedicated_remap_target_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADB_SERVERLES_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using remap feature

Syntax
```

```

`dbms_cloud_oci_database_migration_adb_serverles_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped.

Allowed values are: 'DATA'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADMIN_CREDENTIALS_T Type

Database Administrator Credentials details.

Syntax
```

```

Fields

Field Description

`username`

(required) Administrator username

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_REPORT_BUCKET_DETAILS_T Type

Details to access Pre-Migration Advisor report in the specified Object Storage bucket, if any.

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) Name of the bucket containing the Pre-Migration Advisor report.

`namespace`

(required) Object Storage namespace.

`object_name`

(required) Pre-Migration Advisor report object name.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_REPORT_LOCATION_DETAILS_T Type

Details to access Pre-Migration Advisor report.

Syntax
```

```

Fields

Field Description

`object_storage_details`

(optional)

`location_in_source`

(optional) Path in the Source Registered Connection where the Pre-Migration advisor report can be accessed.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_REPORT_T Type

Pre-Migration advisor report details.

Syntax
```

```

Fields

Field Description

`report_location_details`

(optional)

`result`

(required) Pre-Migration advisor result.

Allowed values are: 'FATAL', 'BLOCKER', 'WARNING', 'INFORMATIONAL', 'PASS'

`number_of_fatal`

(required) Number of Fatal results in the advisor report.

`number_of_fatal_blockers`

(required) Number of Fatal Blocker results in the advisor report.

`number_of_warnings`

(required) Number of Warning results in the advisor report.

`number_of_informational_results`

(required) Number of Informational results in the advisor report.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_SETTINGS_T Type

Optional Pre-Migration advisor settings.

Syntax
```

```

Fields

Field Description

`is_skip_advisor`

(optional) True to skip the Pre-Migration Advisor execution. Default is false.

`is_ignore_errors`

(optional) True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_T Type

ODMS Agent Details

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource

`display_name`

(required) ODMS Agent name

`compartment_id`

(required) OCID of the compartment

`stream_id`

(required) The OCID of the Stream

`public_key`

(optional) ODMS Agent public key.

`version`

(required) ODMS Agent version

`time_created`

(required) The time the Agent was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time of the last Agent details update. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the ODMS on-premises Agent.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_SUMMARY_T Type

ODMS Agent Details

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource

`display_name`

(required) ODMS Agent name

`compartment_id`

(required) OCID of the compartment

`stream_id`

(optional) The OCID of the Stream

`version`

(required) ODMS Agent version

`time_created`

(required) The time the Agent was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time of the last Agent details update. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the ODMS on-premises Agent.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_agent_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_COLLECTION_T Type

Results of an Agent search. Contains AgentSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_IMAGE_SUMMARY_T Type

Available ODMS Agent Images.

Syntax
```

```

Fields

Field Description

`version`

(required) ODMS Agent Image version.

`download_url`

(required) URL to download Agent Image of the ODMS Agent.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_IMAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_agent_image_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_IMAGE_COLLECTION_T Type

Results of an ODMS Agent Image search. Contains AgentImageSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_TRANSFER_MEDIUM_DETAILS_V2_T Type

Optional additional properties for dump transfer in source or target host. Default kind is CURL

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the data transfer medium to use for the datapump

Allowed values are: 'DBLINK', 'OBJECT_STORAGE', 'AWS_S3', 'NFS'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AWS_S3_DATA_TRANSFER_MEDIUM_DETAILS_T Type

AWS S3 bucket details used for source Connection resources with RDS_ORACLE type. Only supported for source Connection resources with RDS_ORACLE type.

Syntax
```

```

`dbms_cloud_oci_database_migration_aws_s3_data_transfer_medium_details_t`is a subtype of the`dbms_cloud_oci_database_migration_data_transfer_medium_details_v2_t`type.

Fields

Field Description

`name`

(optional) S3 bucket name.

`l_region`

(optional) AWS region code where the S3 bucket is located. Region code should match the documented available regions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

`access_key_id`

(optional) AWS access key credentials identifier Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

`secret_access_key`

(optional) AWS secret access key credentials Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_AWS_S3_DETAILS_T Type

AWS S3 bucket details used for source Connection resources with RDS_ORACLE type. Only supported for source Connection resources with RDS_ORACLE type.

Syntax
```

```

Fields

Field Description

`name`

(required) S3 bucket name.

`l_region`

(required) AWS region code where the S3 bucket is located. Region code should match the documented available regions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CHANGE_AGENT_COMPARTMENT_DETAILS_T Type

Change Agent compartment details

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the resource to.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CHANGE_CONNECTION_COMPARTMENT_DETAILS_T Type

Change Database Connection compartment details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the resource to.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CHANGE_MIGRATION_COMPARTMENT_DETAILS_T Type

Change Migration compartment details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the resource to.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_OBJECT_T Type

Database objects to include or exclude from migration

Syntax
```

```

Fields

Field Description

`owner`

(required) Owner of the object (regular expression is allowed)

`object_name`

(required) Name of the object (regular expression is allowed)

`l_type`

(optional) Type of object to exclude. If not specified, matching owners and object names of type TABLE would be excluded.

`is_omit_excluded_table_from_replication`

(optional) Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and that are included in the exludeObjects.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_VAULT_DETAILS_T Type

OCI Vault details to store migration and connection credentials secrets

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment where the secret containing the credentials will be created.

`vault_id`

(required) OCID of the vault

`key_id`

(required) OCID of the vault encryption key

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_database_migration_database_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CLONE_MIGRATION_DETAILS_T Type

Details that will override an existing Migration configuration that will be cloned.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Migration Display Name

`compartment_id`

(optional) OCID of the compartment

`agent_id`

(optional) The OCID of the registered on-premises ODMS Agent. Only valid for Offline Logical Migrations.

`source_database_connection_id`

(required) The OCID of the Source Database Connection.

`source_container_database_connection_id`

(optional) The OCID of the Source Container Database Connection. Only used for Online migrations. Only Connections of type Non-Autonomous can be used as source container databases.

`target_database_connection_id`

(required) The OCID of the Target Database Connection.

`exclude_objects`

(optional) Database objects to exclude from migration, cannot be specified alongside 'includeObjects'

`include_objects`

(optional) Database objects to include from migration, cannot be specified alongside 'excludeObjects'

`vault_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECT_DESCRIPTOR_T Type

Connect Descriptor details.

Syntax
```

```

Fields

Field Description

`host`

(optional) Host of the connect descriptor.

`port`

(optional) Port of the connect descriptor.

`database_service_name`

(optional) Database service name.

`connect_string`

(optional) Connect string.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_SSH_DETAILS_T Type

Details of the SSH key that will be used.

Syntax
```

```

Fields

Field Description

`host`

(required) Name of the host the SSH key is valid for.

`l_user`

(required) SSH user

`sudo_location`

(required) Sudo location

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_PRIVATE_ENDPOINT_DETAILS_T Type

OCI Private Endpoint configuration details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the private endpoint.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN where the Private Endpoint will be bound to.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the customer's subnet where the private endpoint VNIC will reside.

`id`

(optional)[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a previously created Private Endpoint.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_VAULT_DETAILS_T Type

OCI Vault details to store migration and connection credentials secrets

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment where the secret containing the credentials will be created.

`vault_id`

(required) OCID of the vault

`key_id`

(required) OCID of the vault encryption key

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_T Type

Database Connection resource used for migrations.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource

`compartment_id`

(required) OCID of the compartment

`database_type`

(required) Database connection type.

Allowed values are: 'MANUAL', 'AUTONOMOUS', 'USER_MANAGED_OCI'

`manual_database_sub_type`

(optional) Database manual connection subtype. This value can only be specified for manual connections.

Allowed values are: 'ORACLE', 'RDS_ORACLE'

`is_dedicated`

(optional) True if the Autonomous Connection is dedicated. Not provided for Non-Autonomous Connections.

`display_name`

(required) Database Connection display name identifier.

`database_id`

(optional) The OCID of the cloud database.

`connect_descriptor`

(optional)

`credentials_secret_id`

(optional) OCID of the Secret in the OCI vault containing the Database Connection credentials.

`certificate_tdn`

(optional) This name is the distinguished name used while creating the certificate on target database.

`ssh_details`

(optional)

`admin_credentials`

(optional)

`replication_credentials`

(optional)

`private_endpoint`

(optional)

`vault_details`

(optional)

`lifecycle_state`

(required) The current state of the Connection resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`time_created`

(required) The time the Connection resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time of the last Connection resource details update. An RFC3339 formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for Connections.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_SUMMARY_T Type

Database Connection Summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource

`compartment_id`

(required) OCID of the compartment

`database_type`

(required) Database connection type.

Allowed values are: 'MANUAL', 'AUTONOMOUS', 'USER_MANAGED_OCI'

`manual_database_sub_type`

(optional) Database manual connection subtype. This value can only be specified for manual connections.

Allowed values are: 'ORACLE', 'RDS_ORACLE'

`is_dedicated`

(optional) True if the Autonomous Connection is dedicated. Not provided for Non-Autonomous Connections.

`display_name`

(required) Database Connection display name identifier.

`database_id`

(optional) The OCID of the cloud database.

`time_created`

(required) The time the Connection resource was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time of the last Connection resource details update. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Connection resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for Connections.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_connection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_COLLECTION_T Type

Results of a Database Connection search. Contains DatabaseConnectionSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_TARGET_TYPE_TABLESPACE_DETAILS_T Type

Migration tablespace settings.

Syntax
```

```

Fields

Field Description

`target_type`

(required) Type of Database Base Migration Target.

Allowed values are: 'ADB_S_REMAP', 'ADB_D_REMAP', 'ADB_D_AUTOCREATE', 'NON_ADB_REMAP', 'NON_ADB_AUTOCREATE'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADB_DEDICATED_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using auto create feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_adb_dedicated_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_target_type_tablespace_details_t`type.

Fields

Field Description

`is_auto_create`

(optional) True to auto-create tablespace in the target Database.

`is_big_file`

(optional) True set tablespace to big file.

`extend_size_in_m_bs`

(optional) Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.

`block_size_in_k_bs`

(optional) Size of Oracle database blocks in KB.

Allowed values are: 'SIZE_8K', 'SIZE_16K'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADB_DEDICATED_REMAP_TARGET_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using remap feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_adb_dedicated_remap_target_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADB_SERVERLES_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-S target type using remap feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_adb_serverles_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_target_type_tablespace_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADMIN_CREDENTIALS_T Type

Database Administrator Credentials details.

Syntax
```

```

Fields

Field Description

`username`

(required) Administrator username

`password`

(required) Administrator password

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADVISOR_SETTINGS_T Type

Optional Pre-Migration advisor settings.

Syntax
```

```

Fields

Field Description

`is_skip_advisor`

(optional) True to skip the Pre-Migration Advisor execution. Default is false.

`is_ignore_errors`

(optional) True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_AWS_S3_DETAILS_T Type

AWS S3 bucket details used for source Connection resources with RDS_ORACLE type. Only supported for source Connection resources with RDS_ORACLE type.

Syntax
```

```

Fields

Field Description

`name`

(required) S3 bucket name.

`l_region`

(required) AWS region code where the S3 bucket is located. Region code should match the documented available regions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

`access_key_id`

(required) AWS access key credentials identifier Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

`secret_access_key`

(required) AWS secret access key credentials Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_CONNECT_DESCRIPTOR_T Type

Connect Descriptor details. Required for Manual and UserManagerOci connection types. If a Private Endpoint was specified for the Connection, the host should contain a valid IP address.

Syntax
```

```

Fields

Field Description

`host`

(optional) Host or IP address of the connect descriptor. Required if no connectString was specified.

`port`

(optional) Port of the connect descriptor. Required if no connectString was specified.

`database_service_name`

(optional) Database service name. Required if no connectString was specified.

`connect_string`

(optional) Connect String. Required if no host, port nor databaseServiceName were specified. If a Private Endpoint was specified in the Connection, the host entry should be a valid IP address. Supported formats: Easy connect: &lt;host&gt;:&lt;port&gt;/&lt;db_service_name&gt; Long format: (description= (address=(port=&lt;port&gt;)(host=&lt;host&gt;))(connect_data=(service_name=&lt;db_service_name&gt;)))

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_SSH_DETAILS_T Type

Details of the SSH key that will be used. Required for source database Manual and UserManagerOci connection types. Not required for source container database connections.

Syntax
```

```

Fields

Field Description

`host`

(required) Name of the host the SSH key is valid for.

`sshkey`

(required) Private SSH key string.

`l_user`

(required) SSH user

`sudo_location`

(optional) Sudo location

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_PRIVATE_ENDPOINT_T Type

OCI Private Endpoint configuration details. Not required for source container database connections, it will default to the specified Source Database Connection Private Endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the private endpoint.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN where the Private Endpoint will be bound to.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the customer's subnet where the private endpoint VNIC will reside.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_CONNECTION_DETAILS_T Type

Details to create a Database Connection resource.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment

`display_name`

(optional) Database Connection display name identifier.

`database_type`

(required) Database connection type.

Allowed values are: 'MANUAL', 'AUTONOMOUS', 'USER_MANAGED_OCI'

`manual_database_sub_type`

(optional) Database manual connection subtype. This value can only be specified for manual connections.

Allowed values are: 'ORACLE', 'RDS_ORACLE'

`database_id`

(optional) The OCID of the cloud database. Required if the database connection type is Autonomous.

`connect_descriptor`

(optional)

`certificate_tdn`

(optional) This name is the distinguished name used while creating the certificate on target database. Requires a TLS wallet to be specified. Not required for source container database connections.

`tls_wallet`

(optional) cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.

`tls_keystore`

(optional) keystore.jks file contents; base64 encoded String. Requires a TLS wallet to be specified. Not required for source container database connections.

`ssh_details`

(optional)

`admin_credentials`

(required)

`replication_credentials`

(optional)

`private_endpoint`

(optional)

`vault_details`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for Connections.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_HOST_DUMP_TRANSFER_DETAILS_T Type

Optional additional properties for dump transfer in source or target host. Default kind is CURL

Syntax
```

```

Fields

Field Description

`wallet_location`

(optional) Directory path to OCI SSL wallet location on Db server node.

`kind`

(required) Type of dump transfer to use during migration in source or target host. Default kind is CURL

Allowed values are: 'CURL', 'OCI_CLI'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_CURL_TRANSFER_DETAILS_T Type

Optional properties for Curl-based dump transfer in source or target host.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_curl_transfer_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_host_dump_transfer_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATA_PUMP_PARAMETERS_T Type

Optional parameters for Data Pump Export and Import.

Syntax
```

```

Fields

Field Description

`is_cluster`

(optional) Set to false to force Data Pump worker process to run on one instance.

`estimate`

(optional) Estimate size of dumps that will be generated.

Allowed values are: 'BLOCKS', 'STATISTICS'

`table_exists_action`

(optional) IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.

Allowed values are: 'TRUNCATE', 'REPLACE', 'APPEND', 'SKIP'

`exclude_parameters`

(optional) Exclude paratemers for Export and Import.

`import_parallelism_degree`

(optional) Maximum number of worker processes that can be used for a Data Pump Import job. For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.

`export_parallelism_degree`

(optional) Maximum number of worker processes that can be used for a Data Pump Export job.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_METADATA_REMAP_T Type

Defines remapping to be applied to objects as they are processed. Refer to[METADATA_REMAP Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of remap. Refer to[METADATA_REMAP Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)

Allowed values are: 'SCHEMA', 'TABLESPACE', 'DATAFILE', 'TABLE'

`old_value`

(required) Specifies the value which needs to be reset.

`new_value`

(required) Specifies the new value that oldValue should be translated into.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DIRECTORY_OBJECT_T Type

Directory object details, used to define either import or export directory objects in Data Pump Settings. Import directory is required for Non-Autonomous target connections. If specified for an autonomous target, it will show an error. Export directory will error if there are database link details specified.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of directory object in database

`path`

(optional) Absolute path of directory on database server

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_METADATA_REMAP_TBL Type

Nested table type of dbms_cloud_oci_database_migration_metadata_remap_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATA_PUMP_SETTINGS_T Type

Optional settings for Data Pump Export and Import jobs

Syntax
```

```

Fields

Field Description

`job_mode`

(optional) Data Pump job mode. Refer to[link text](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4)

Allowed values are: 'FULL', 'SCHEMA', 'TABLE', 'TABLESPACE', 'TRANSPORTABLE'

`data_pump_parameters`

(optional)

`metadata_remaps`

(optional) Defines remapping to be applied to objects as they are processed. Refer to[DATA_REMAP](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-E75AAE6F-4EA6-4737-A752-6B62F5E9D460)

`tablespace_details`

(optional)

`export_directory_object`

(optional)

`import_directory_object`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_OBJECT_STORE_BUCKET_T Type

In lieu of a network database link, OCI Object Storage bucket will be used to store Data Pump dump files for the migration. Additionally, it can be specified alongside a database link data transfer medium.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Namespace name of the object store bucket.

`bucket_name`

(required) Bucket name.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATABASE_LINK_DETAILS_T Type

Optional details for creating a network database link from OCI database to on-premise database.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.

`wallet_bucket`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATA_TRANSFER_MEDIUM_DETAILS_T Type

Data Transfer Medium details for the Migration. If not specified, it will default to Database Link. Only one type of data transfer medium can be specified, except for the case of Amazon RDS Oracle as source, where Object Storage Details along with AwsS3Details are required.

Syntax
```

```

Fields

Field Description

`database_link_details`

(optional)

`object_storage_details`

(optional)

`aws_s3_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DUMP_TRANSFER_DETAILS_T Type

Optional additional properties for dump transfer.

Syntax
```

```

Fields

Field Description

`source`

(optional)

`target`

(optional)

`shared_storage_mount_target_id`

(optional) OCID of the shared storage mount target

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_EXTRACT_T Type

Parameters for GoldenGate Extract processes.

Syntax
```

```

Fields

Field Description

`performance_profile`

(optional) Extract performance.

Allowed values are: 'LOW', 'MEDIUM', 'HIGH'

`long_trans_duration`

(optional) Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_HUB_T Type

Details about Oracle GoldenGate Microservices. Required for online logical migration.

Syntax
```

```

Fields

Field Description

`rest_admin_credentials`

(required)

`source_db_admin_credentials`

(optional)

`source_container_db_admin_credentials`

(optional)

`target_db_admin_credentials`

(optional)

`url`

(required) Oracle GoldenGate Microservices hub's REST endpoint.

`source_microservices_deployment_name`

(optional) Name of GoldenGate Microservices deployment to operate on source database

`target_microservices_deployment_name`

(optional) Name of GoldenGate Microservices deployment to operate on target database

`compute_id`

(optional) OCID of GoldenGate Microservices compute instance.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_REPLICAT_T Type

Parameters for GoldenGate Replicat processes.

Syntax
```

```

Fields

Field Description

`performance_profile`

(optional) Replicat performance.

Allowed values are: 'LOW', 'HIGH'

`map_parallelism`

(optional) Number of threads used to read trail files (valid for Parallel Replicat)

`min_apply_parallelism`

(optional) Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)

`max_apply_parallelism`

(optional) Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_SETTINGS_T Type

Optional settings for GoldenGate Microservices processes

Syntax
```

```

Fields

Field Description

`extract`

(optional)

`replicat`

(optional)

`acceptable_lag`

(optional) ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_DETAILS_T Type

Details about Oracle GoldenGate Microservices. Required for online logical migration.

Syntax
```

```

Fields

Field Description

`hub`

(required)

`settings`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_CREDENTIALS_T Type

Database Credentials details.

Syntax
```

```

Fields

Field Description

`username`

(required) Database username

`password`

(required) Database password

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_SERVICE_DETAILS_T Type

Details about Oracle GoldenGate GGS Deployment.

Syntax
```

```

Fields

Field Description

`source_db_credentials`

(optional)

`source_container_db_credentials`

(optional)

`target_db_credentials`

(optional)

`settings`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_MIGRATION_DETAILS_T Type

Create Migration resource parameters.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Migration type.

Allowed values are: 'ONLINE', 'OFFLINE'

`display_name`

(optional) Migration Display Name

`compartment_id`

(required) OCID of the compartment

`agent_id`

(optional) The OCID of the registered ODMS Agent. Only valid for Offline Logical Migrations.

`source_database_connection_id`

(required) The OCID of the Source Database Connection.

`source_container_database_connection_id`

(optional) The OCID of the Source Container Database Connection. Only used for Online migrations. Only Connections of type Non-Autonomous can be used as source container databases.

`target_database_connection_id`

(required) The OCID of the Target Database Connection.

`data_transfer_medium_details_v2`

(optional)

`data_transfer_medium_details`

(optional)

`dump_transfer_details`

(optional)

`datapump_settings`

(optional)

`advisor_settings`

(optional)

`exclude_objects`

(optional) Database objects to exclude from migration, cannot be specified alongside 'includeObjects'

`include_objects`

(optional) Database objects to include from migration, cannot be specified alongside 'excludeObjects'

`csv_text`

(optional) Database objects to exclude/include from migration in CSV format. The excludeObjects and includeObjects fields will be ignored if this field is not null.

`golden_gate_details`

(optional)

`golden_gate_service_details`

(optional)

`vault_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_NON_ADB_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for NON-ADB target type using auto create feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_non_adb_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_target_type_tablespace_details_t`type.

Fields

Field Description

`is_auto_create`

(optional) True to auto-create tablespace in the target Database.

`is_big_file`

(optional) True set tablespace to big file.

`extend_size_in_m_bs`

(optional) Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.

`block_size_in_k_bs`

(optional) Size of Oracle database blocks in KB.

Allowed values are: 'SIZE_8K', 'SIZE_16K'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_NON_ADB_REMAP_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for NON-ADB target type using remap feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_non_adb_remap_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_OCI_CLI_DUMP_TRANSFER_DETAILS_T Type

Optional dump transfer details for OCI-CLI-based dump transfer in source or target host.

Syntax
```

```

`dbms_cloud_oci_database_migration_create_oci_cli_dump_transfer_details_t`is a subtype of the`dbms_cloud_oci_database_migration_create_host_dump_transfer_details_t`type.

Fields

Field Description

`oci_home`

(required) Path to the OCI CLI installation in the node.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_HOST_DUMP_TRANSFER_DETAILS_T Type

Optional additional properties for dump transfer in source or target host. Default kind is CURL

Syntax
```

```

Fields

Field Description

`wallet_location`

(optional) Directory path to OCI SSL wallet location on Db server node.

`kind`

(required) Type of dump transfer to use during migration in source or target host. Default kind is CURL

Allowed values are: 'CURL', 'OCI_CLI'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_CURL_TRANSFER_DETAILS_T Type

Optional properties for Curl-based dump transfer in source or target host.

Syntax
```

```

`dbms_cloud_oci_database_migration_curl_transfer_details_t`is a subtype of the`dbms_cloud_oci_database_migration_host_dump_transfer_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_PUMP_PARAMETERS_T Type

Optional parameters for Data Pump Export and Import.

Syntax
```

```

Fields

Field Description

`is_cluster`

(optional) Set to false to force Data Pump worker processes to run on one instance.

`estimate`

(optional) Estimate size of dumps that will be generated.

Allowed values are: 'BLOCKS', 'STATISTICS'

`table_exists_action`

(optional) IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.

Allowed values are: 'TRUNCATE', 'REPLACE', 'APPEND', 'SKIP'

`exclude_parameters`

(optional) Exclude paratemers for Export and Import.

`import_parallelism_degree`

(optional) Maximum number of worker processes that can be used for a Data Pump Import job. For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.

`export_parallelism_degree`

(optional) Maximum number of worker processes that can be used for a Data Pump Export job.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DIRECTORY_OBJECT_T Type

Directory object details, used to define either import or export directory objects in Data Pump Settings.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of directory object in database

`path`

(required) Absolute path of directory on database server

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_PUMP_SETTINGS_T Type

Optional settings for Data Pump Export and Import jobs

Syntax
```

```

Fields

Field Description

`job_mode`

(optional) Data Pump job mode. Refer to[Data Pump Export Modes](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4)

Allowed values are: 'FULL', 'SCHEMA', 'TABLE', 'TABLESPACE', 'TRANSPORTABLE'

`data_pump_parameters`

(optional)

`metadata_remaps`

(optional) Defines remapping to be applied to objects as they are processed. Refer to[METADATA_REMAP Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)

`tablespace_details`

(optional)

`export_directory_object`

(optional)

`import_directory_object`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_OBJECT_STORE_BUCKET_T Type

In lieu of a network database link, OCI Object Storage bucket will be used to store Data Pump dump files for the migration. Additionally, it can be specified alongside a database link data transfer medium.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Namespace name of the object store bucket.

`bucket_name`

(required) Bucket name.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_LINK_DETAILS_T Type

Optional details for creating a network database link from OCI database to on-premise database.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.

`wallet_bucket`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_TRANSFER_MEDIUM_DETAILS_T Type

Data Transfer Medium details for the Migration.

Syntax
```

```

Fields

Field Description

`database_link_details`

(optional)

`object_storage_details`

(optional)

`aws_s3_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DB_LINK_DATA_TRANSFER_MEDIUM_DETAILS_T Type

Optional details for creating a network database link from OCI database to on-premise database.

Syntax
```

```

`dbms_cloud_oci_database_migration_db_link_data_transfer_medium_details_t`is a subtype of the`dbms_cloud_oci_database_migration_data_transfer_medium_details_v2_t`type.

Fields

Field Description

`object_storage_bucket`

(optional)

`name`

(optional) Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_RESULT_ERROR_T Type

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

`issue`

(optional) The text describing the root cause of the reported issue

`action`

(optional) The text describing the action required to fix the issue

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DIAGNOSTICS_RESULT_T Type

Result from Database Connection Diagnostic action.

Syntax
```

```

Fields

Field Description

`result_type`

(required) Type of the Result (i.e. Success or Failure).

Allowed values are: 'SUCCEEDED', 'FAILED', 'TIMED_OUT'

`error`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_DUMP_TRANSFER_DETAILS_T Type

Optional additional properties for dump transfer.

Syntax
```

```

Fields

Field Description

`source`

(optional)

`target`

(optional)

`shared_storage_mount_target_id`

(optional) OCID of the shared storage mount target

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_ERROR_T Type

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

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXCLUDED_OBJECT_SUMMARY_T Type

Excluded object summary line.

Syntax
```

```

Fields

Field Description

`owner`

(required) Database object owner.

`object`

(required) Database object name.

`l_type`

(required) Database object type.

`reason_category`

(required) Reason category for object exclusion.

Allowed values are: 'ORACLE_MAINTAINED', 'GG_UNSUPPORTED', 'USER_EXCLUDED', 'MANDATORY_EXCLUDED', 'USER_EXCLUDED_TYPE'

`source_rule`

(optional) Reason for exclusion.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXCLUDED_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_excluded_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXCLUDED_OBJECT_SUMMARY_COLLECTION_T Type

Results of a Job's Exclude objects output listing. Contains ExcludedObjectSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXTRACT_T Type

Parameters for Extract processes.

Syntax
```

```

Fields

Field Description

`performance_profile`

(optional) Extract performance.

Allowed values are: 'LOW', 'MEDIUM', 'HIGH'

`long_trans_duration`

(optional) Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_GGS_DEPLOYMENT_T Type

Details about Oracle GoldenGate GGS Deployment.

Syntax
```

```

Fields

Field Description

`deployment_id`

(required) OCID of a GoldenGate Deployment

`ggs_admin_credentials_secret_id`

(required) OCID of a VaultSecret containing the Admin Credentials for the GGS Deployment

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_HUB_T Type

Details about Oracle GoldenGate Microservices.

Syntax
```

```

Fields

Field Description

`rest_admin_credentials`

(required)

`source_db_admin_credentials`

(required)

`source_container_db_admin_credentials`

(optional)

`target_db_admin_credentials`

(required)

`url`

(required) Oracle GoldenGate hub's REST endpoint.

`source_microservices_deployment_name`

(required) Name of GoldenGate deployment to operate on source database

`target_microservices_deployment_name`

(required) Name of GoldenGate deployment to operate on target database

`compute_id`

(optional) OCID of GoldenGate compute instance.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_REPLICAT_T Type

Parameters for Replicat processes.

Syntax
```

```

Fields

Field Description

`performance_profile`

(optional) Replicat performance.

Allowed values are: 'LOW', 'HIGH'

`map_parallelism`

(optional) Number of threads used to read trail files (valid for Parallel Replicat)

`min_apply_parallelism`

(optional) Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)

`max_apply_parallelism`

(optional) Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_SETTINGS_T Type

Optional settings for Oracle GoldenGate processes

Syntax
```

```

Fields

Field Description

`extract`

(optional)

`replicat`

(optional)

`acceptable_lag`

(optional) ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_DETAILS_T Type

Details about Oracle GoldenGate Microservices.

Syntax
```

```

Fields

Field Description

`hub`

(required)

`settings`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_SERVICE_DETAILS_T Type

Details about Oracle GoldenGate GGS Deployment.

Syntax
```

```

Fields

Field Description

`ggs_deployment`

(optional)

`settings`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_EXTRACT_ENTRY_T Type

Job phase extract message.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of extract.

Allowed values are: 'ERROR'

`message`

(required) Message in entry.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_LOG_LOCATION_BUCKET_DETAILS_T Type

Details to access log file in the specified Object Storage bucket, if any.

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) Name of the bucket containing the log file.

`namespace`

(required) Object Storage namespace.

`object_name`

(required) Log object name.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_EXTRACT_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_phase_extract_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_STATUS_T Type

Job phase status details.

Syntax
```

```

Fields

Field Description

`name`

(required) Phase name

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

`status`

(required) Phase status

Allowed values are: 'PENDING', 'STARTED', 'COMPLETED', 'FAILED'

`duration_in_ms`

(required) Duration of the phase in milliseconds

`is_advisor_report_available`

(optional) True if a Pre-Migration Advisor report is available for this phase. False or null if no report is available.

`issue`

(optional) The text describing the root cause of the reported issue

`action`

(optional) The text describing the action required to fix the issue

`extract`

(optional) Summary of phase status results.

`log_location`

(optional)

`progress`

(optional) Percent progress of job phase.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_STATUS_TBL Type

Nested table type of dbms_cloud_oci_database_migration_phase_status_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_JOB_PROGRESS_RESOURCE_T Type

Progress details of a Migration Job.

Syntax
```

```

Fields

Field Description

`current_status`

(required) Current status of the job.

Allowed values are: 'PENDING', 'STARTED', 'COMPLETED', 'FAILED'

`current_phase`

(required) Current phase of the job.

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

`phases`

(required) List of phase status for the job.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UNSUPPORTED_DATABASE_OBJECT_T Type

Database objects to exclude from migration

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Type of unsupported object

Allowed values are: 'GOLDEN_GATE'

`owner`

(required) Owner of the object (regular expression is allowed)

`object_name`

(required) Name of the object (regular expression is allowed)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UNSUPPORTED_DATABASE_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_database_migration_unsupported_database_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_T Type

Results of a Database Connection search. Contains DatabaseConnectionSummary items.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Migration Job.

`display_name`

(required) Name of the job.

`migration_id`

(required) The OCID of the Migration that this job belongs to.

`l_type`

(required) The job type.

Allowed values are: 'EVALUATION', 'MIGRATION'

`time_created`

(required) The time the Migration Job was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Migration Job was last updated. An RFC3339 formatted datetime string

`progress`

(optional)

`unsupported_objects`

(optional) Database objects not supported.

`lifecycle_state`

(required) The current state of the migration job.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'UNKNOWN', 'TERMINATED', 'FAILED', 'SUCCEEDED', 'WAITING', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_JOB_PROGRESS_SUMMARY_T Type

Summary of the progress of a Migration Job.

Syntax
```

```

Fields

Field Description

`current_phase`

(required) Current phase of the job.

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

`current_status`

(required) Current status of the job.

Allowed values are: 'PENDING', 'STARTED', 'COMPLETED', 'FAILED'

`job_progress`

(required) Job progress percentage (0 - 100)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_SUMMARY_T Type

Job description

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the Migration Job.

`display_name`

(required) Name of the job.

`migration_id`

(required) The OCID of the Migration that this job belongs to.

`l_type`

(required) The job type.

Allowed values are: 'EVALUATION', 'MIGRATION'

`progress`

(optional)

`time_created`

(required) The time the Migration Job was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Migration Job was last updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the migration Deployment.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'UNKNOWN', 'TERMINATED', 'FAILED', 'SUCCEEDED', 'WAITING', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_COLLECTION_T Type

Results of a Job search. Contains JobSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_OUTPUT_SUMMARY_T Type

Job output summary line.

Syntax
```

```

Fields

Field Description

`message`

(required) Job output line.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_OUTPUT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_job_output_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_OUTPUT_SUMMARY_COLLECTION_T Type

Results of a Job output listing. Contains JobOutputSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_T Type

Migration resource

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource

`display_name`

(required) Migration Display Name

`compartment_id`

(required) OCID of the compartment

`l_type`

(required) Migration type.

Allowed values are: 'ONLINE', 'OFFLINE'

`wait_after`

(optional) Name of a migration phase. The Job will wait after executing this phase until the Resume Job endpoint is called.

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

`agent_id`

(optional) The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.

`credentials_secret_id`

(optional) OCID of the Secret in the OCI vault containing the Migration credentials. Used to store GoldenGate administrator user credentials.

`source_database_connection_id`

(required) The OCID of the Source Database Connection.

`source_container_database_connection_id`

(optional) The OCID of the Source Container Database Connection.

`target_database_connection_id`

(required) The OCID of the Target Database Connection.

`executing_job_id`

(optional) OCID of the current ODMS Job in execution for the Migration, if any.

`data_transfer_medium_details_v2`

(optional)

`data_transfer_medium_details`

(optional)

`dump_transfer_details`

(optional)

`datapump_settings`

(optional)

`advisor_settings`

(optional)

`exclude_objects`

(optional) Database objects to exclude from migration. If 'includeObjects' are specified, only exclude object types can be specified with general wildcards (.*) for owner and objectName.

`include_objects`

(optional) Database objects to include from migration.

`golden_gate_service_details`

(optional)

`golden_gate_details`

(optional)

`vault_details`

(optional)

`time_created`

(required) The time the Migration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time of the last Migration details update. An RFC3339 formatted datetime string.

`time_last_migration`

(optional) The time of last Migration. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Migration resource.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'IN_PROGRESS', 'ACCEPTED', 'SUCCEEDED', 'CANCELED', 'WAITING', 'NEEDS_ATTENTION', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional status related to the execution and current state of the Migration.

Allowed values are: 'READY', 'ABORTING', 'VALIDATING', 'VALIDATED', 'WAITING', 'MIGRATING', 'DONE'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_SUMMARY_T Type

Migration resource

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the resource

`display_name`

(required) Migration Display Name

`compartment_id`

(required) OCID of the compartment

`l_type`

(required) Migration type.

Allowed values are: 'ONLINE', 'OFFLINE'

`source_database_connection_id`

(required) The OCID of the Source Database Connection.

`source_container_database_connection_id`

(optional) The OCID of the Source Container Database Connection.

`target_database_connection_id`

(required) The OCID of the Target Database Connection.

`executing_job_id`

(optional) OCID of the current ODMS Job in execution for the Migration, if any.

`agent_id`

(optional) The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.

`vault_details`

(optional)

`time_created`

(required) The time the Migration was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time of the last Migration details update. An RFC3339 formatted datetime string.

`time_last_migration`

(optional) The time of last Migration. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the Migration.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'IN_PROGRESS', 'ACCEPTED', 'SUCCEEDED', 'CANCELED', 'WAITING', 'NEEDS_ATTENTION', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Additional status related to the execution and current state of the Migration.

Allowed values are: 'READY', 'ABORTING', 'VALIDATING', 'VALIDATED', 'WAITING', 'MIGRATING', 'DONE'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_migration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_COLLECTION_T Type

Results of a Migration search. Contains MigrationSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_SUMMARY_T Type

Database objects to include or exclude from migration

Syntax
```

```

Fields

Field Description

`owner`

(required) Owner of the object (regular expression is allowed)

`object_name`

(required) Name of the object (regular expression is allowed)

`l_type`

(optional) Type of object to exclude. If not specified, matching owners and object names of type TABLE would be excluded.

`object_status`

(optional) Object status.

Allowed values are: 'EXCLUDE', 'INCLUDE'

`is_omit_excluded_table_from_replication`

(optional) Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and object status EXCLUDE.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_migration_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_COLLECTION_T Type

Database objects to migrate.

Syntax
```

```

Fields

Field Description

`items`

(required) Database objects to exclude/include from migration

`csv_text`

(optional) Database objects to exclude/include from migration in CSV format. The items field will be ignored if this field is not null.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_TYPE_SUMMARY_T Type

Migration Object Type

Syntax
```

```

Fields

Field Description

`name`

(required) Object type name

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_migration_object_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_TYPE_SUMMARY_COLLECTION_T Type

Results of a Migration Object Type listing. Contains MigrationObjectTypeSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_PHASE_SUMMARY_T Type

Migration Phase Summary of details.

Syntax
```

```

Fields

Field Description

`name`

(required) ODMS Job phase name

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

`recommended_action`

(optional) Action recommended for this phase. If not included in the response, there is no recommended action for the phase.

Allowed values are: 'WAIT'

`supported_actions`

(required) Array of actions for the corresponding phase. Empty array would indicate there is no supported action for the phase.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_PHASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_migration_phase_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_PHASE_COLLECTION_T Type

Results of a Migration Phase search. Contains a collection of valid ODMS Job Phases.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_NFS_DATA_TRANSFER_MEDIUM_DETAILS_T Type

OCI Object Storage bucket will be used to store Data Pump dump files for the migration.

Syntax
```

```

`dbms_cloud_oci_database_migration_nfs_data_transfer_medium_details_t`is a subtype of the`dbms_cloud_oci_database_migration_data_transfer_medium_details_v2_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_NON_ADB_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for NON-ADB target type using auto create feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_non_adb_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_target_type_tablespace_details_t`type.

Fields

Field Description

`is_auto_create`

(optional) True to auto-create tablespace in the target Database.

`is_big_file`

(optional) True set tablespace to big file.

`extend_size_in_m_bs`

(optional) Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.

`block_size_in_k_bs`

(optional) Size of Oracle database blocks in KB.

Allowed values are: 'SIZE_8K', 'SIZE_16K'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_NON_ADB_REMAP_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for NON-ADB target type using remap feature

Syntax
```

```

`dbms_cloud_oci_database_migration_non_adb_remap_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_OBJECT_STORAGE_DATA_TRANSFER_MEDIUM_DETAILS_T Type

OCI Object Storage bucket will be used to store Data Pump dump files for the migration.

Syntax
```

```

`dbms_cloud_oci_database_migration_object_storage_data_transfer_medium_details_t`is a subtype of the`dbms_cloud_oci_database_migration_data_transfer_medium_details_v2_t`type.

Fields

Field Description

`object_storage_bucket`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_OCI_CLI_DUMP_TRANSFER_DETAILS_T Type

Optional dump transfer details for OCI-CLI-based dump transfer in source or target host.

Syntax
```

```

`dbms_cloud_oci_database_migration_oci_cli_dump_transfer_details_t`is a subtype of the`dbms_cloud_oci_database_migration_host_dump_transfer_details_t`type.

Fields

Field Description

`oci_home`

(optional) Path to the OCI CLI installation in the node.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_RESUME_JOB_DETAILS_T Type

Parameters to specify to resume a Migration Job.

Syntax
```

```

Fields

Field Description

`wait_after`

(optional) Name of a migration phase. The Job will wait after executing this phase until Resume Job endpoint is called again.

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_START_MIGRATION_DETAILS_T Type

Parameters to specify to a Migration job operation.

Syntax
```

```

Fields

Field Description

`wait_after`

(optional) Name of a migration phase. The Job will wait after executing this phase until the Resume Job endpoint is called.

Allowed values are: 'ODMS_VALIDATE_TGT', 'ODMS_VALIDATE_SRC', 'ODMS_VALIDATE_PREMIGRATION_ADVISOR', 'ODMS_VALIDATE_GG_HUB', 'ODMS_VALIDATE_GG_SERVICE', 'ODMS_VALIDATE_DATAPUMP_SETTINGS', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC', 'ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT', 'ODMS_VALIDATE_DATAPUMP_SRC', 'ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC', 'ODMS_INITIALIZE_GGS', 'ODMS_VALIDATE', 'ODMS_PREPARE', 'ODMS_INITIAL_LOAD_EXPORT', 'ODMS_DATA_UPLOAD', 'ODMS_INITIAL_LOAD_IMPORT', 'ODMS_POST_INITIAL_LOAD', 'ODMS_PREPARE_REPLICATION_TARGET', 'ODMS_MONITOR_REPLICATION_LAG', 'ODMS_SWITCHOVER', 'ODMS_CLEANUP'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_TARGET_TYPE_TABLESPACE_DETAILS_T Type

Migration tablespace settings.

Syntax
```

```

Fields

Field Description

`target_type`

(required) Type of Database Base Migration Target.

Allowed values are: 'ADB_S_REMAP', 'ADB_D_REMAP', 'ADB_D_AUTOCREATE', 'NON_ADB_REMAP', 'NON_ADB_AUTOCREATE', 'TARGET_DEFAULTS_REMAP', 'TARGET_DEFAULTS_AUTOCREATE'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADB_DEDICATED_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using auto create feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_adb_dedicated_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

Fields

Field Description

`is_auto_create`

(optional) True to auto-create tablespace in the target Database.

`is_big_file`

(optional) True set tablespace to big file.

`extend_size_in_m_bs`

(optional) Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.

`block_size_in_k_bs`

(optional) Size of Oracle database blocks in KB.

Allowed values are: 'SIZE_8K', 'SIZE_16K'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADB_DEDICATED_REMAP_TARGET_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-D target type using remap target.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_adb_dedicated_remap_target_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADB_SERVERLES_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for ADB-S target type using remap feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_adb_serverles_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADMIN_CREDENTIALS_T Type

Database Administrator Credentials details. An empty object would result in the removal of the stored details.

Syntax
```

```

Fields

Field Description

`username`

(optional) Administrator username

`password`

(optional) Administrator password

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADVISOR_SETTINGS_T Type

Optional Pre-Migration advisor settings.

Syntax
```

```

Fields

Field Description

`is_skip_advisor`

(optional) True to skip the Pre-Migration Advisor execution. Default is false.

`is_ignore_errors`

(optional) True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_AGENT_DETAILS_T Type

ODMS Agent Details

Syntax
```

```

Fields

Field Description

`display_name`

(optional) ODMS Agent name

`stream_id`

(optional) The OCID of the Stream

`public_key`

(optional) ODMS Agent public key.

`version`

(optional) ODMS Agent version

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_AWS_S3_DETAILS_T Type

AWS S3 bucket details used for source Connection resources with RDS_ORACLE type. Only supported for source Connection resources with RDS_ORACLE type.

Syntax
```

```

Fields

Field Description

`name`

(optional) S3 bucket name.

`l_region`

(optional) AWS region code where the S3 bucket is located. Region code should match the documented available regions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

`access_key_id`

(optional) AWS access key credentials identifier Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

`secret_access_key`

(optional) AWS secret access key credentials Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_CONNECT_DESCRIPTOR_T Type

Connect Descriptor details. If a Private Endpoint was specified in the Connection, the host entry should be a valid IP address.

Syntax
```

```

Fields

Field Description

`host`

(optional) Host or IP address of the connect descriptor.

`port`

(optional) Port of the connect descriptor.

`database_service_name`

(optional) Database service name.

`connect_string`

(optional) Connect String. If specified, this will override the stored connect descriptor details. If a Private Endpoint was specified in the Connection, the host entry should be a valid IP address. Supported formats: Easy connect: &lt;host&gt;:&lt;port&gt;/&lt;db_service_name&gt; Long format: (description= (address=(port=&lt;port&gt;)(host=&lt;host&gt;))(connect_data=(service_name=&lt;db_service_name&gt;)))

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_SSH_DETAILS_T Type

Details of the SSH key that will be used.

Syntax
```

```

Fields

Field Description

`host`

(optional) Name of the host the SSH key is valid for.

`sshkey`

(optional) Private SSH key string.

`l_user`

(optional) SSH user

`sudo_location`

(optional) Sudo location

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_PRIVATE_ENDPOINT_T Type

OCI Private Endpoint configuration details. An empty object would result in the removal of the stored details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the private endpoint.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN where the Private Endpoint will be bound to.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the customer's subnet where the private endpoint VNIC will reside.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_VAULT_DETAILS_T Type

OCI Vault details to store migration and connection credentials secrets. An empty object would result in the removal of the stored details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) OCID of the compartment where the secret containing the credentials will be created.

`vault_id`

(optional) OCID of the vault

`key_id`

(optional) OCID of the vault encryption key

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_CONNECTION_DETAILS_T Type

Details to update in a Database Connection resource.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Database Connection display name identifier.

`database_id`

(optional) The OCID of the cloud database.

`connect_descriptor`

(optional)

`certificate_tdn`

(optional) This name is the distinguished name used while creating the certificate on target database. Not required for source container database connections.

`tls_wallet`

(optional) cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.

`tls_keystore`

(optional) keystore.jks file contents; base64 encoded String. Not required for source container database connections.

`ssh_details`

(optional)

`admin_credentials`

(optional)

`replication_credentials`

(optional)

`private_endpoint`

(optional)

`vault_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for Connections.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_HOST_DUMP_TRANSFER_DETAILS_T Type

Optional additional properties for dump transfer in source or target host. Default kind is CURL

Syntax
```

```

Fields

Field Description

`wallet_location`

(optional) Directory path to OCI SSL wallet location on Db server node.

`kind`

(required) Type of dump transfer to use during migration in source or target host. Default kind is CURL

Allowed values are: 'CURL', 'OCI_CLI'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_CURL_TRANSFER_DETAILS_T Type

Optional properties for Curl-based dump transfer in source or target host.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_curl_transfer_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_host_dump_transfer_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATA_PUMP_PARAMETERS_T Type

Optional parameters for Data Pump Export and Import. If an empty object is specified, the stored Data Pump Parameter details will be removed.

Syntax
```

```

Fields

Field Description

`is_cluster`

(optional) Set to false to force Data Pump worker processes to run on one instance.

`estimate`

(optional) Estimate size of dumps that will be generated.

Allowed values are: 'BLOCKS', 'STATISTICS'

`table_exists_action`

(optional) IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.

Allowed values are: 'TRUNCATE', 'REPLACE', 'APPEND', 'SKIP'

`exclude_parameters`

(optional) Exclude paratemers for Export and Import. If specified, the stored list will be replaced.

`import_parallelism_degree`

(optional) Maximum number of worker processes that can be used for a Data Pump Import job. For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.

`export_parallelism_degree`

(optional) Maximum number of worker processes that can be used for a Data Pump Export job.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DIRECTORY_OBJECT_T Type

Directory object details, used to define either import or export directory objects in Data Pump Settings. Import directory is required for Non-Autonomous target connections. If specified for an autonomous target, it will show an error. Export directory will error if there are database link details specified. If an empty object is specified, the stored Directory Object details will be removed.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of directory object in database

`path`

(optional) Absolute path of directory on database server

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATA_PUMP_SETTINGS_T Type

Optional settings for Data Pump Export and Import jobs

Syntax
```

```

Fields

Field Description

`job_mode`

(optional) Data Pump job mode. Refer to[Data Pump Export Modes](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4)

Allowed values are: 'FULL', 'SCHEMA', 'TABLE', 'TABLESPACE', 'TRANSPORTABLE'

`data_pump_parameters`

(optional)

`metadata_remaps`

(optional) Defines remappings to be applied to objects as they are processed. Refer to[METADATA_REMAP Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)If specified, the list will be replaced entirely. Empty list will remove stored Metadata Remap details.

`tablespace_details`

(optional)

`export_directory_object`

(optional)

`import_directory_object`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_OBJECT_STORE_BUCKET_T Type

OCI Object Storage bucket details.

Syntax
```

```

Fields

Field Description

`namespace_name`

(optional) Namespace name of the object store bucket.

`bucket_name`

(optional) Bucket name.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATABASE_LINK_DETAILS_T Type

Optional details for updating a network database link from OCI database to on-premise database.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.

`wallet_bucket`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATA_TRANSFER_MEDIUM_DETAILS_T Type

Data Transfer Medium details for the Migration. Only one type of data transfer medium can be specified, except for the case of Amazon RDS Oracle as source, where Object Storage Details along with AwsS3Details are required. If an empty object is specified, the stored Data Transfer Medium details will be removed.

Syntax
```

```

Fields

Field Description

`database_link_details`

(optional)

`object_storage_details`

(optional)

`aws_s3_details`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DUMP_TRANSFER_DETAILS_T Type

Optional additional properties for dump transfer.

Syntax
```

```

Fields

Field Description

`source`

(optional)

`target`

(optional)

`shared_storage_mount_target_id`

(optional) OCID of the shared storage mount target

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_EXTRACT_T Type

Parameters for Extract processes. If an empty object is specified, the stored Extract details will be removed.

Syntax
```

```

Fields

Field Description

`performance_profile`

(optional) Extract performance.

Allowed values are: 'LOW', 'MEDIUM', 'HIGH'

`long_trans_duration`

(optional) Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_HUB_T Type

Details about Oracle GoldenGate Microservices.

Syntax
```

```

Fields

Field Description

`rest_admin_credentials`

(optional)

`source_db_admin_credentials`

(optional)

`source_container_db_admin_credentials`

(optional)

`target_db_admin_credentials`

(optional)

`url`

(optional) Oracle GoldenGate hub's REST endpoint.

`source_microservices_deployment_name`

(optional) Name of GoldenGate deployment to operate on source database

`target_microservices_deployment_name`

(optional) Name of GoldenGate deployment to operate on target database

`compute_id`

(optional) OCID of GoldenGate compute instance. An empty value will remove the stored computeId.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_REPLICAT_T Type

Parameters for Replicat processes. If an empty object is specified, the stored Replicat details will be removed.

Syntax
```

```

Fields

Field Description

`performance_profile`

(optional) Replicat performance.

Allowed values are: 'LOW', 'HIGH'

`map_parallelism`

(optional) Number of threads used to read trail files (valid for Parallel Replicat)

`min_apply_parallelism`

(optional) Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)

`max_apply_parallelism`

(optional) Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_SETTINGS_T Type

Optional settings for Oracle GoldenGate processes If an empty object is specified, the stored GoldenGate Settings details will be removed.

Syntax
```

```

Fields

Field Description

`extract`

(optional)

`replicat`

(optional)

`acceptable_lag`

(optional) ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_DETAILS_T Type

Details about Oracle GoldenGate Microservices. If an empty object is specified, the stored Golden Gate details will be removed.

Syntax
```

```

Fields

Field Description

`hub`

(optional)

`settings`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_SERVICE_DETAILS_T Type

Details about the Oracle GoldenGate Microservices. If an empty object is specified, the stored Golden Gate details will be removed.

Syntax
```

```

Fields

Field Description

`source_db_credentials`

(optional)

`source_container_db_credentials`

(optional)

`target_db_credentials`

(optional)

`settings`

(optional)

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_JOB_DETAILS_T Type

Update Job Details

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

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_MIGRATION_DETAILS_T Type

Update Migration resource parameters.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Migration type.

Allowed values are: 'ONLINE', 'OFFLINE'

`display_name`

(optional) Migration Display Name

`agent_id`

(optional) The OCID of the registered ODMS Agent.

`source_database_connection_id`

(optional) The OCID of the Source Database Connection.

`source_container_database_connection_id`

(optional) The OCID of the Source Container Database Connection. Only used for Online migrations. Only Connections of type Non-Autonomous can be used as source container databases. An empty value would remove the stored Connection ID.

`target_database_connection_id`

(optional) The OCID of the Target Database Connection.

`data_transfer_medium_details_v2`

(optional)

`data_transfer_medium_details`

(optional)

`dump_transfer_details`

(optional)

`datapump_settings`

(optional)

`advisor_settings`

(optional)

`exclude_objects`

(optional) Database objects to exclude from migration, cannot be specified alongside 'includeObjects'. If specified, the list will be replaced entirely. Empty list will remove stored excludeObjects details.

`include_objects`

(optional) Database objects to include from migration, cannot be specified alongside 'excludeObjects'. If specified, the list will be replaced entirely. Empty list will remove stored includeObjects details.

`golden_gate_service_details`

(optional)

`golden_gate_details`

(optional)

`vault_details`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_NON_ADB_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for NON-ADB target type using auto create feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_non_adb_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

Fields

Field Description

`is_auto_create`

(optional) True to auto-create tablespace in the target Database.

`is_big_file`

(optional) True set tablespace to big file.

`extend_size_in_m_bs`

(optional) Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.

`block_size_in_k_bs`

(optional) Size of Oracle database blocks in KB.

Allowed values are: 'SIZE_8K', 'SIZE_16K'

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_NON_ADB_REMAP_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for NON-ADB target type using remap feature.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_non_adb_remap_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

Fields

Field Description

`remap_target`

(optional) Name of tablespace at target to which the source database tablespace need to be remapped.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_OCI_CLI_DUMP_TRANSFER_DETAILS_T Type

Optional dump transfer details for OCI-CLI-based dump transfer in source or target host.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_oci_cli_dump_transfer_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_host_dump_transfer_details_t`type.

Fields

Field Description

`oci_home`

(required) Path to the OCI CLI installation in the node.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_TARGET_DEFAULTS_AUTO_CREATE_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for TARGET_DEFAULTS_AUTOCREATE target type. The service will compute the targetType that corresponds to the targetDatabaseConnectionId type, and set the corresponding default values. When target type is ADB_D or NON_ADB the default will be set to auto-create feature ADB_D_AUTOCREATE or NON_ADB_AUTOCREATE.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_target_defaults_auto_create_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_TARGET_DEFAULTS_REMAP_TABLESPACE_DETAILS_T Type

Migration tablespace settings valid for TARGET_DEFAULTS_REMAP target type. The service will compute the targetType that corresponds to the targetDatabaseConnectionId type, and set the corresponding default values. When target type is ADB_S, ADB_D or NON_ADB the default will be set to remap feature ADB_S_REMAP, ADB_D_REMAP or NON_ADB_REMAP.

Syntax
```

```

`dbms_cloud_oci_database_migration_update_target_defaults_remap_tablespace_details_t`is a subtype of the`dbms_cloud_oci_database_migration_update_target_type_tablespace_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_RESOURCE_T Type

A resource that is created or operated on by an asynchronous operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The way in which this resource was affected by the operation that spawned the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS'

`entity_type`

(required) The resource type the work request affects.

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier for the resource.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_database_migration_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_AGENT', 'DELETE_AGENT', 'CREATE_MIGRATION', 'CLONE_MIGRATION', 'DELETE_MIGRATION', 'UPDATE_MIGRATION', 'START_MIGRATION', 'VALIDATE_MIGRATION', 'CREATE_CONNECTION', 'DELETE_CONNECTION', 'UPDATE_CONNECTION'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources that are affected by this work request.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this work request.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_COLLECTION_T Type

Results of a Work Request search. Contains WorkRequestSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm)

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_database_migration_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a Work Request search. Contains WorkRequestError items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_database_migration_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a Work Request search. Contains WorkRequestLogEntry items.

Syntax
```

```

Fields

Field Description

`items`

(required) Items in collection.

- [Database Migrations Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-2FB56B9A-D1C7-46FA-BD4B-E3A189B07C26)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0653B3CA-0907-42A7-A481-17D01910A605)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_TARGET_TYPE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-30FACCAE-8DA7-4BE9-A334-3FF2A81EA487)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADB_DEDICATED_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-B3E9F820-6F8B-48C1-9F96-500BAF83E69A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADB_DEDICATED_REMAP_TARGET_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D3206CD5-97F7-494C-A487-7E01EF78D4A2)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADB_SERVERLES_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C8C5DD31-D749-4B64-84B2-30D17B507DD1)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADMIN_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-82AE3350-F9DA-4F59-BF4E-164A9D895F43)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_REPORT_BUCKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4106FBBF-344C-4C7F-9740-0F2CDCE6E6A3)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_REPORT_LOCATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-AF6D8202-5BB5-4364-8D88-251F208083BE)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_REPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D3D71FF2-BEB8-4113-92AD-39CD1B77018C)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ADVISOR_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-DECF1D93-9A93-48BB-B465-FCC00F9EC991)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-CEE6AA3A-2162-4671-B9C2-4A5F6F493279)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-FB2C81AD-610B-4E2D-8D67-42679911B56E)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-59EC0425-2166-4EBC-B3E9-99C7088B1FD6)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-EA939587-4ECA-46C6-A1DF-7F4D84015138)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_IMAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-8A78C5F6-A0F5-4181-96F7-995DA346E2D4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_IMAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-40E2DDD3-BE4D-4BDF-B21B-96DC05F41D8B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AGENT_IMAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-08B65612-FD92-458B-8171-6921E30D6DA9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_TRANSFER_MEDIUM_DETAILS_V2_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-74179EC7-71B9-4710-8246-EB3AC5BAA2D4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AWS_S3_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-3B8000BC-299C-497A-B1F8-E67DB07DC093)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_AWS_S3_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-5F86736D-4CBB-4EDC-B32D-347D7D651B16)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CHANGE_AGENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0F7664A5-B111-4C0B-94E0-7ED7B6C83E61)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CHANGE_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-42FBA136-BEC7-413F-A148-902DB2CD425A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CHANGE_MIGRATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9861096D-2B12-4B2B-AE5F-40FE3AD50880)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A5E381BD-FA21-41D3-9E49-ECD32149EC79)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-822371A7-B0FE-4157-8A85-3DDAFEC8F1CE)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C8064C7C-E57A-4860-8D43-3E3BC527F564)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CLONE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C47D124D-D52D-4C34-A75B-3D0C34DBB784)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECT_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4EB0F891-56C5-45D9-9343-15068ADC03F8)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_SSH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-99E73A6B-1206-4959-9453-B3B6CBB7E07F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-DFE31DD4-BE08-493B-90F1-24532FF09B8D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-7736E4B6-9C57-4BAA-9066-4C9FB52DAD96)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C4FCD689-CFB9-44E7-AADB-86BE122CB292)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-BED9E72E-A3CF-4A14-915D-9EF5A09F74C9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6B9BEAAB-F4E4-4B33-B348-920EDB179066)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0D80A22D-3765-4B69-86CB-0DF895E08BE4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_TARGET_TYPE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0D8030E7-115D-491C-9DFD-B11B0601C80F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADB_DEDICATED_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-B87750E1-DC7D-447E-90D3-C970A3D46316)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADB_DEDICATED_REMAP_TARGET_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9EA0FDD2-5938-4678-A46E-000B119F0D02)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADB_SERVERLES_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-11E7CBF9-0B9D-4AAE-9689-8B97448C1832)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADMIN_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C141CEEC-E45F-4881-8BBC-19DCE9BB0A76)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_ADVISOR_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-1E936BB4-0B71-4688-AE88-D15607B149AA)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_AWS_S3_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-3A7D3767-AFA4-46E2-8D67-4880AE0DC840)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_CONNECT_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9C915EA0-4D19-4634-9EA0-F4FC7AD523E0)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_SSH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-ED9AEEEB-4FF9-4C55-B8ED-5E5FAC59DDE8)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4D02669A-01EE-443E-AF20-8BBDA4575D61)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4FBFCDC1-C476-49F7-993C-04B6AF60AB5F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_HOST_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9BC43F02-BF6B-4807-BDF1-78EA9742122B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_CURL_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D25D0135-7D26-4CBF-AB26-ADF09A90A000)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATA_PUMP_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A05726D6-CFFF-479E-8AD2-4D47388C6831)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_METADATA_REMAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4A57F399-475A-4CEF-A373-ACE952761A9E)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DIRECTORY_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A32E224C-8007-4A19-8676-1D80156D2002)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_METADATA_REMAP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-E00EC55D-C879-4776-9D66-B2A5B559A546)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATA_PUMP_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6AC35E70-204E-40AC-AA47-DE26AABE45B0)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_OBJECT_STORE_BUCKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-90B17AC8-04D1-456F-AAD4-9274FCC748F4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATABASE_LINK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-B5FC40FE-30F3-4E0D-AF10-2866FD3AF70A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-854BD713-DF63-412E-92F9-48EC35A3DB47)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-22316247-5B1F-483F-ADF4-81FC9061492F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_EXTRACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-131FCF49-B4DC-447F-916B-D5D9B8CB4670)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_HUB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-36E7BE5D-4765-4F30-8072-760C9B01FBF7)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_REPLICAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-DA528731-0F30-4BB7-AEE4-C06D666F312A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-312CECB8-4166-4534-B027-346E5A4E3282)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-5DAC584F-76FF-43FD-9C11-4633B5CD8A60)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-2E3430B5-A445-4BF0-A7C8-675A646F9AD4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_GOLDEN_GATE_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-DEEB0530-1DB5-4F8C-80E0-1C9AA26153AC)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-E527F896-29C2-41EE-9331-D0E26602DE10)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_NON_ADB_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-028F2A2E-3B40-44F5-AAB1-0CF8CC400D20)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_NON_ADB_REMAP_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-FE6A4131-32C2-426E-94AD-70848BCFBC1D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CREATE_OCI_CLI_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-777FEFE7-F442-462E-AA17-D7B64F51F025)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_HOST_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-35D7EE2F-7D81-4DDC-9DEF-FF5B7FB3308F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_CURL_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-12496DAF-20AD-4774-9707-51D87746DD22)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_PUMP_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D77EB62C-47BB-44FC-9CBE-565EE24CE369)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DIRECTORY_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-58975DBB-C569-4D89-8EAF-6B7755E5920A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_PUMP_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9F37EB0B-63CB-445D-9592-868D1B8B99B5)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_OBJECT_STORE_BUCKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-28385D88-6FB5-4CEF-B16A-A19A478C4635)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATABASE_LINK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-2E277298-45F8-4E52-BA16-626557027C22)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C86ECF3D-CEEC-4C60-BC46-D2DF774DE91F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DB_LINK_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-5CE8F64D-DFD6-44E7-AE91-4A13587D6E20)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_RESULT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-CF527FA7-434D-4B86-AA8C-62F784637D4F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DIAGNOSTICS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-FB785D65-0C79-4EBB-8010-BF4F6F989028)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-1CB95D67-9550-4455-8B08-882F23DA4A33)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-B9785488-6F84-4F5A-95F7-879A7B67794C)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXCLUDED_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A8FAE711-175D-44BC-A2AA-1F09F7868AF9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXCLUDED_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-96EEB4A4-F8CC-4241-83FD-3277D79817E1)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXCLUDED_OBJECT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-74749376-3795-4FF3-A4BD-AA581AE78331)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_EXTRACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D8D81813-6180-4F0C-9DD2-3FA723133CC1)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_GGS_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-AE181C83-66C9-4E02-BF21-CC32DB99B470)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_HUB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-94106D8D-11FD-486C-A33E-517EF9F3A88F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_REPLICAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-78A387CC-B55A-4A34-B17F-18AA983D021F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-77ABFB63-572C-4886-A1EF-2401DE91B71D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4DDAEE75-612F-45DC-894B-B3E3F4D3DE10)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_GOLDEN_GATE_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-CF311835-3714-472F-B942-4E842A053764)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_EXTRACT_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-25F96FD6-C0D6-460D-B483-BBD5276DD351)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_LOG_LOCATION_BUCKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-8617CB3C-CE09-4CB7-8074-9F8F25DA522D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_EXTRACT_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D80B0C07-F1E4-43CC-A502-FD0808592A28)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-08B36EA8-F2BD-4B5C-AB95-A39C0265992B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_PHASE_STATUS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-65ED3640-0DC4-46F5-B92C-3FE92E3557ED)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_JOB_PROGRESS_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-95F5D8C2-BC71-476D-9E97-DCE7B441056F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UNSUPPORTED_DATABASE_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D34BC9CE-0258-45A6-ADA3-D6BD669B22F4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UNSUPPORTED_DATABASE_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-7D57303C-FC07-4D28-9729-4A4FD1CAC7FD)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A80BFD23-A806-4C37-BB3C-28D7BBFFE77D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_JOB_PROGRESS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-DD1B904B-905A-4770-A4A8-2583386B47D9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-12F7BE6C-D1A2-40B0-8DB1-24663FCF0402)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-E01450AA-AE57-4590-BD87-FEB5A23C735A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-456394E9-35F1-4C03-8225-377BB59DEADB)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_OUTPUT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-64571CFC-D89D-4398-9843-A9D0250D4F64)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_OUTPUT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A120CC50-82ED-4DDE-8ABD-9308E4819EC6)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_JOB_OUTPUT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-56C5D091-AED8-437D-94DD-4FF97494C14C)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-5D2169D0-EAF3-496D-84CD-C4D98A4EA1E0)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-59BE0F4F-CEA8-4181-BD93-B04167B5716B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D107DD1A-74FE-4A38-B800-C348E2A12943)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-66F82C79-3251-459E-BFE2-34FC4ECE065B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-197C7306-2B33-44A0-85B1-4A372621344B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-EB3F1EB0-78C6-4F70-A512-E4469C822296)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-90859AC8-B90B-48C0-B298-B0EF3296A6E3)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-96915E86-607A-4621-8506-0DC2941765C9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C577C87B-E2E6-42DD-BD6A-4B2469D25BD9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_OBJECT_TYPE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-EEB89308-8745-4E2F-AC57-65C8A14C3678)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_PHASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-EE38D561-3A05-4309-8A5C-20D8F12313C7)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_PHASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-09014A25-73D5-4A0A-A148-58430885FDC6)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_MIGRATION_PHASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-7C27EE48-B529-4E21-8DD3-2EC31FBCEF4B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_NFS_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6661E827-E0B3-498F-B70A-3955390692D7)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_NON_ADB_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-8EA23C4C-71A9-46AC-9465-3F975B960728)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_NON_ADB_REMAP_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-90DF17E5-6E44-4BAD-8F75-760FB66275B9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_OBJECT_STORAGE_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D33654C6-6CD5-4E59-AF7D-BBDABCC2F495)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_OCI_CLI_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0C0BC3D2-6DF5-4EB0-882E-C6874FF12AA3)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_RESUME_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-54C15AE7-4F0D-483C-888A-DDB526FC3D70)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_START_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-FB19829F-BE3E-44F7-8015-74D6A37BED53)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_TARGET_TYPE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A4A36944-141D-4451-BAF3-B2FAF2F12927)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADB_DEDICATED_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-39FE840F-985B-4AF4-B413-FB1407C3360C)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADB_DEDICATED_REMAP_TARGET_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-8A629A28-FB13-4465-89E7-8C2D0249FB35)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADB_SERVERLES_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C0A6979A-6A17-4808-A84D-8DA29F37DE3F)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADMIN_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-FE8E5B22-C5E8-4FCB-8CF0-E79408793DD1)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_ADVISOR_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6B1CAA50-19DC-4173-A19B-B84DB0E3B4E6)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_AGENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-7EE0C95A-9203-40EC-8E35-B6A7CE546075)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_AWS_S3_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-630A94DF-DF96-46C9-899B-6C529D2D9566)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_CONNECT_DESCRIPTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-5F063D2D-858B-497E-ADED-D3DF9216F5D5)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_SSH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-7D1F0CBA-7347-4F59-9324-F89042B4FEEB)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-2457D03C-4A2E-44E6-BD2E-8EFE5058B0EB)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C0975310-B83A-4958-8579-A03DD78781FA)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-2D7431F5-3BEA-418C-BF54-3C2B83BE2AAC)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_HOST_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-53197FEC-D5CE-4B4D-A1D3-876B5BBF4DC9)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_CURL_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-460DD56F-770A-41BC-9EBF-DDF02E8721AA)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATA_PUMP_PARAMETERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-57C8C176-75BF-4577-B6EB-0933FE9901CD)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DIRECTORY_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-C51E3197-4C17-468A-93DD-87CBC5A23AD0)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATA_PUMP_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A38BA2C6-E333-410A-AC2F-8E924195F88D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_OBJECT_STORE_BUCKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-8886A7AF-F49B-4D73-AA21-0A60588BD300)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATABASE_LINK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D74F68F3-9304-449F-B4E3-D0B3A4BDDA90)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DATA_TRANSFER_MEDIUM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-7DEF34BC-2BBC-4504-83F4-26F74C487F20)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0E926EB1-0ADC-4B43-B7E7-2DD5864F8C68)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_EXTRACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6799A71D-C621-4F4F-A8D2-AB4FC9FDA838)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_HUB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-1902A2BB-8E0E-443B-9B72-CCD9881D8252)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_REPLICAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-B006F0E0-810B-4762-A877-30590797646A)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-5E74801F-08C0-4BA7-A871-8FFBE6299BDB)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-0433050E-2658-4561-A375-06D6D21C76EB)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_GOLDEN_GATE_SERVICE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-46C543E4-9CB9-4769-BD01-CD2D5091EFAC)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-2D0D7CCB-5B9E-4DCF-B503-5CBB7708715B)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-306A9F5F-E11F-490C-BFD6-623DFF3AC8CA)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_NON_ADB_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-DD8F62FC-E03D-475E-B0C1-3E93D9CD85C2)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_NON_ADB_REMAP_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-934F578F-8A61-4B2E-848E-2B3524E5D881)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_OCI_CLI_DUMP_TRANSFER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9E977EEF-47B8-470A-AA8E-DC75F4C24676)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_TARGET_DEFAULTS_AUTO_CREATE_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6EED861B-86CB-4163-AD3C-0C40B1AAEEE0)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_UPDATE_TARGET_DEFAULTS_REMAP_TABLESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A7C4D671-DFEC-4ACF-AD11-C9C5BAE7EABA)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-6E5E9337-E294-46AD-BA47-4768EA0162F8)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-254D35D5-D5CC-48A5-A3DB-62441E0D051E)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-1B621375-6684-42C7-9DFC-CB18B1F1BE9E)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-A248EB1D-98AE-4A8B-A5AE-EF831C7A1AA4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-4925D3FF-E246-4B07-ACC2-1B66151EEFE4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-E1E1A441-D564-4E1D-9F87-6E8D0E47BEF4)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-F69A4E16-B340-4E10-A0DC-03DBC189576E)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-D3D4EEC5-B1C9-4214-A92E-C0B740FBE439)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9F0A7E71-481C-425C-B538-E40307BC3DC3)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-8ECE251A-247D-4894-8272-9F73EB7E8F5D)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-11EA8733-72ED-4574-BB2B-D84196BC55B0)
- [DBMS_CLOUD_OCI_DATABASE_MIGRATION_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_migration_t.html#ADSDK-GUID-9CC905F8-96D3-4CF9-A019-C6B376C66DE8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
