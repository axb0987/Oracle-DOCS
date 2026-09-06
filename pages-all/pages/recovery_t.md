# Recovery Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#dcoc-content-body)

## Recovery Common Types

### DBMS_CLOUD_OCI_RECOVERY_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_CHANGE_PROTECTED_DATABASE_COMPARTMENT_DETAILS_T Type

The configuration details required to move a protected database from the existing compartment to a specified compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the protected database should be moved.

### DBMS_CLOUD_OCI_RECOVERY_CHANGE_PROTECTION_POLICY_COMPARTMENT_DETAILS_T Type

The configuration details required to move a protection policy from the existing compartment to a specified compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the Protection Policy should be moved.

### DBMS_CLOUD_OCI_RECOVERY_CHANGE_RECOVERY_SERVICE_SUBNET_COMPARTMENT_DETAILS_T Type

The configuration details required to move a Recovery Service subnet from the existing compartment to a specified compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the Recovery Service subnet should be moved.

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_INPUT_T Type

Parameters to retrieve information about a specific recovery service subnet.

Syntax
```

```

Fields

Field Description

`recovery_service_subnet_id`

(required) The recovery service subnet OCID.

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_INPUT_TBL Type

Nested table type of dbms_cloud_oci_recovery_recovery_service_subnet_input_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_CREATE_PROTECTED_DATABASE_DETAILS_T Type

Describes the parameters required to create a protected database.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The protected database name. You can change the displayName. Avoid entering confidential information.

`db_unique_name`

(required) The dbUniqueName of the protected database in Recovery Service. You cannot change the unique name.

`database_size`

(optional) The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.

Allowed values are: 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'AUTO'

`password`

(required) Password credential which can be used to connect to Protected Database. It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters. The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \"admin\", regardless of casing.

`protection_policy_id`

(required) The OCID of the protection policy associated with the protected database.

`recovery_service_subnets`

(required) List of recovery service subnet resources associated with the protected database.

`database_id`

(optional) The OCID of the protected database.

`compartment_id`

(required) The OCID of the compartment that contains the protected database.

`database_size_in_g_bs`

(optional) The size of the database, in gigabytes.

`change_rate`

(optional) The percentage of data changes that exist in the database between successive incremental backups.

`compression_ratio`

(optional) The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.

`is_redo_logs_shipped`

(optional) The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_CREATE_PROTECTION_POLICY_DETAILS_T Type

Describes the parameters required to create a custom protection policy.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.

`backup_retention_period_in_days`

(required) The maximum number of days to retain backups for a protected database.

`compartment_id`

(required) Compartment Identifier

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_CREATE_RECOVERY_SERVICE_SUBNET_DETAILS_T Type

Describes the parameters required to create a recovery service subnet.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.

`subnet_id`

(required) The OCID of the subnet associated with the recovery service subnet. You can create a single backup network per virtual cloud network (VCN).

`vcn_id`

(required) The OCID of the virtual cloud network (VCN) that contains the recovery service subnet. You can create a single recovery service subnet per VCN.

`compartment_id`

(required) The compartment OCID.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_ERROR_T Type

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

### DBMS_CLOUD_OCI_RECOVERY_FETCH_PROTECTED_DATABASE_CONFIGURATION_DETAILS_T Type

Provides which configuration details to get.

Syntax
```

```

Fields

Field Description

`configuration_type`

(optional) Currently has four config options ALL, TNSNAMES, HOSTS and CABUNDLE. All will return a zipped folder containing the contents of both tnsnames and the certificateChainPem.

Allowed values are: 'CABUNDLE', 'TNSNAMES', 'HOSTS', 'ALL'

### DBMS_CLOUD_OCI_RECOVERY_METRICS_T Type

Backup performance and storage utilization metrics for the protected database.

Syntax
```

```

Fields

Field Description

`backup_space_used_in_g_bs`

(optional) Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.

`backup_space_estimate_in_g_bs`

(optional) The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the protected database.

`unprotected_window_in_seconds`

(optional) This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is available. This is the time we received the last backup or last redo-log shipped.

`db_size_in_g_bs`

(optional) The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the catalog, and does not include archive logs.

`is_redo_logs_enabled`

(optional) The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.

`retention_period_in_days`

(optional) The maximum number of days to retain backups for a protected database.

`current_retention_period_in_seconds`

(optional) Number of seconds backups are currently retained for this database.

### DBMS_CLOUD_OCI_RECOVERY_METRICS_SUMMARY_T Type

Backup performance and storage utilization metrics for the Protected Database.

Syntax
```

```

Fields

Field Description

`backup_space_used_in_g_bs`

(optional) Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.

`backup_space_estimate_in_g_bs`

(optional) The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the protected database.

`unprotected_window_in_seconds`

(optional) This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is available. This is the time we received the last backup or last redo-log shipped.

`db_size_in_g_bs`

(optional) The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the catalog, and does not include archive logs.

`is_redo_logs_enabled`

(optional) The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.

`retention_period_in_days`

(optional) The maximum number of days to retain backups for a protected database.

`current_retention_period_in_seconds`

(optional) Number of seconds backups are currently retained for this database.

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_DETAILS_T Type

Details of the Recovery Service Subnet.

Syntax
```

```

Fields

Field Description

`recovery_service_subnet_id`

(required) Recovery Service Subnet Identifier.

`lifecycle_state`

(optional) The current state of the Recovery Service Subnet.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_recovery_recovery_service_subnet_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_T Type

A protected database is an Oracle Cloud Database whose backups are managed by Oracle Database Autonomous Recovery Service. Each protected database requires a recovery service subnet and a protection policy to use Recovery Service as the backup destination for centralized backup and recovery

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the protected database.

`display_name`

(optional) The protected database name. You can change the displayName. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment that contains the protected database.

`db_unique_name`

(required) The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.

`vpc_user_name`

(required) The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.

`database_size`

(required) The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.

Allowed values are: 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'AUTO'

`protection_policy_id`

(required) The OCID of the protection policy associated with the protected database.

`recovery_service_subnets`

(required) List of recovery service subnet resources associated with the protected database.

`database_id`

(optional) The OCID of the protected database.

`database_size_in_g_bs`

(optional) The size of the database in GBs, in gigabytes.

`change_rate`

(optional) The percentage of data changes that exist in the database between successive incremental backups.

`compression_ratio`

(optional) The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.

`is_redo_logs_shipped`

(optional) The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional configuration is needed on client side.

`time_created`

(optional) An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'

`time_updated`

(optional) An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'

`lifecycle_state`

(optional) The current state of the Protected Database.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`health`

(optional) Indicates the protection status of the database. Allowed values are: - HEALTHY - WARNING - ALERT A 'HEALTHY' status indicates that Recovery Service can ensure database recovery to any point in time within the entire recovery window. The potential data loss exposure since the last backup is: - Less than 10 seconds, if Real-time data protection is enabled - Less than 70 minutes if Real-time data protection is disabled A 'WARNING' status indicates that Recovery Service can ensure database recovery within the current recovery window - 1 day. The potential data loss exposure since the last backup is: - Greater than 10 seconds, if Real-time data protection is enabled - Greater than 60 minutes, if if Real-time data protection is disabled An 'ALERT' status indicates that Recovery Service cannot recover the database within the current recovery window.

Allowed values are: 'PROTECTED', 'WARNING', 'ALERT'

`is_read_only_resource`

(optional) Indicates whether the protected database is created by Recovery Service or created manually. Set to &lt;b&gt;TRUE&lt;/b&gt; for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource. Set to &lt;b&gt;FALSE&lt;/b&gt; for a user-defined protected database.

`lifecycle_details`

(optional) Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable information for a resource in a Failed state.

`health_details`

(optional) A message describing the current health of the protected database.

`metrics`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_SUMMARY_T Type

A protected database is an Oracle Cloud Database whose backups are managed by Oracle Database Autonomous Recovery Service. Each protected database requires a recovery service subnet and a protection policy to use Recovery Service as the backup destination for centralized backup and recovery. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the protected database.

`display_name`

(optional) The protected database name. You can change the displayName. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment that contains the protected database.

`db_unique_name`

(required) The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.

`vpc_user_name`

(required) The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.

`database_size`

(required) The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.

Allowed values are: 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'AUTO'

`protection_policy_id`

(required) The OCID of the protection policy associated with the protected database.

`recovery_service_subnets`

(optional) List of recovery service subnet resources associated with the protected database.

`database_id`

(optional) The OCID of the protected database.

`time_created`

(optional) An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'

`time_updated`

(optional) An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'

`lifecycle_state`

(optional) The current state of the Protected Database.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`health`

(optional) The health of the Protected Database.

Allowed values are: 'PROTECTED', 'WARNING', 'ALERT'

`lifecycle_details`

(optional) Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable information for a resource in a Failed state.

`health_details`

(optional) A message describing the current health of the protected database.

`is_read_only_resource`

(optional) Indicates whether the protected database is created by Recovery Service or created manually. Set to &lt;b&gt;TRUE&lt;/b&gt; for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource. Set to &lt;b&gt;FALSE&lt;/b&gt; for a user-defined protected database.

`metrics`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_recovery_protected_database_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_COLLECTION_T Type

Results of a protected database search operation. The results contain protected database summary and metadata information.

Syntax
```

```

Fields

Field Description

`items`

(required) List of protected databases.

### DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_T Type

The details of a protection policy.A policy defines the exact number of days to retain protected database backups created by Recovery Service. Each protected database must be associated with one protection policy. You can use Oracle-defined protection policies or create custom policies to suit your internal backup storage regulation demands.

Syntax
```

```

Fields

Field Description

`id`

(required) The protection policy OCID.

`display_name`

(optional) A user provided name for the protection policy.

`compartment_id`

(required) The OCID of the compartment that contains the protection policy.

`backup_retention_period_in_days`

(required) The maximum number of days to retain backups for a protected database. Specify a period ranging from a minimum 14 days to a maximum 95 days. For example, specify the value 55 if you want to retain backups for 55 days.

`is_predefined_policy`

(required) Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.

`time_created`

(optional) An RFC3339 formatted datetime string that indicates the created time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.

`time_updated`

(optional) An RFC3339 formatted datetime string that indicates the updated time for the protection policy. For example: '2020-05-22T21:10:29.600Z'.

`lifecycle_state`

(optional) The current state of the protection policy. Allowed values are: - CREATING - UPDATING - ACTIVE - DELETING - DELETED - FAILED

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_SUMMARY_T Type

Recovery Service enables policy driven backup storage management. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The protection policy OCID.

`display_name`

(optional) A user provided name for the protection policy.

`compartment_id`

(required) The OCID of the compartment that contains the protection policy.

`backup_retention_period_in_days`

(required) The maximum number of days to retain backups for a protected database.

`is_predefined_policy`

(required) Set to TRUE if the policy is Oracle-defined, and FALSE for a user-defined custom policy. You can modify only the custom policies.

`time_created`

(optional) The time the Protection Policy was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Protection Policy was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the Protection Policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Detailed description about the current lifecycle state of the protection policy. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_recovery_protection_policy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_COLLECTION_T Type

Results of a Protection Policy search. Contains both Protection Policy Summary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of ProtectionPolicies.

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_T Type

The details of a recovery service subnet. Recovery service subnets allows Recovery Service to access protected databases in each VCN. Each recovery service subnet uses a single private endpoint on a subnet of your choice within a VCN. The private endpoint need not be on the same subnet as the Oracle Cloud Database, although, it must be on a subnet that can communicate with the Oracle Cloud Database.

Syntax
```

```

Fields

Field Description

`id`

(required) The recovery service subnet OCID.

`display_name`

(optional) A user-provided name for the recovery service subnet.

`compartment_id`

(required) The compartment OCID.

`vcn_id`

(required) VCN Identifier.

`subnet_id`

(required) The OCID of the subnet used as the recovery service subnet.

`time_created`

(optional) An RFC3339 formatted datetime string that indicates the last created time for a recovery service subnet. For example: '2020-05-22T21:10:29.600Z'.

`time_updated`

(optional) An RFC3339 formatted datetime string that indicates the last updated time for a recovery service subnet. For example: '2020-05-22T21:10:29.600Z'.

`lifecycle_state`

(optional) The current state of the recovery service subnet. Allowed values are: - CREATING - UPDATING - ACTIVE - DELETING - DELETED - FAILED

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Detailed description about the current lifecycle state of the recovery service subnet. For example, it can be used to provide actionable information for a resource in a Failed state

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_SUMMARY_T Type

Each Recovery Service subnet uses a single private endpoint on a subnet of your choice within a VCN. The private endpoint need not be on the same subnet as the Oracle Cloud Database, although, it must be on a subnet that can communicate with the Oracle Cloud Database. To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see Getting Started with Policies. For information about access control and compartments, see[Overview of the Identity Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The recovery service subnet OCID.

`display_name`

(optional) A user-provided name for the recovery service subnet.

`compartment_id`

(required) The compartment OCID.

`vcn_id`

(required) The OCID of the virtual cloud network (VCN) associated with the recovery service subnet. You can create a single recovery service subnet per VCN.

`subnet_id`

(required) The OCID of the subnet associated with the recovery service subnet. You can create a single backup network per virtual cloud network (VCN).

`time_created`

(optional) An RFC3339 formatted datetime string that indicates the last created time for a recovery service subnet. For example: '2020-05-22T21:10:29.600Z'.

`time_updated`

(optional) An RFC3339 formatted datetime string that indicates the last updated time for a recovery service subnet. For example: '2020-05-22T21:10:29.600Z'.

`lifecycle_state`

(optional) The current state of the recovery service subnet. Allowed values are: - CREATING - UPDATING - ACTIVE - DELETING - DELETED - FAILED

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Detailed description about the current lifecycle state of the recovery service subnet. For example, it can be used to provide actionable information for a resource in a Failed state

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_recovery_recovery_service_subnet_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_COLLECTION_T Type

Results of a recovery service subnet search operation. The results contain recovery service subnet summary and metadata information.

Syntax
```

```

Fields

Field Description

`items`

(required) List of recovery service subnet resources.

### DBMS_CLOUD_OCI_RECOVERY_UPDATE_PROTECTED_DATABASE_DETAILS_T Type

Describes the parameters required to update a protected database.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The protected database name. You can change the displayName. Avoid entering confidential information.

`database_size`

(optional) The size of the database is allowed to be decreased. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.

Allowed values are: 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'AUTO'

`database_size_in_g_bs`

(optional) The size of the database, in gigabytes.

`password`

(optional) Password credential which can be used to connect to Protected Database. It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters. The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \"admin\", regardless of casing. Password must not be same as current passsword.

`protection_policy_id`

(optional) The OCID of the protection policy associated with the protected database.

`recovery_service_subnets`

(optional) List of recovery service subnet resources associated with the protected database.

`is_redo_logs_shipped`

(optional) The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service. Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional configuration is needed on client side.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_UPDATE_PROTECTION_POLICY_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.

`backup_retention_period_in_days`

(optional) The maximum number of days to retain backups for a protected database.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_UPDATE_RECOVERY_SERVICE_SUBNET_DETAILS_T Type

Describes the parameters required to update a recovery service subnet.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-provided name for the recovery service subnet. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_RESOURCE_T Type

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

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_recovery_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_PROTECTED_DATABASE', 'UPDATE_PROTECTED_DATABASE', 'DELETE_PROTECTED_DATABASE', 'MOVE_PROTECTED_DATABASE', 'CREATE_PROTECTION_POLICY', 'UPDATE_PROTECTION_POLICY', 'DELETE_PROTECTION_POLICY', 'MOVE_PROTECTION_POLICY', 'CREATE_RECOVERY_SERVICE_SUBNET', 'UPDATE_RECOVERY_SERVICE_SUBNET', 'DELETE_RECOVERY_SERVICE_SUBNET', 'MOVE_RECOVERY_SERVICE_SUBNET'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

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

(optional) The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_recovery_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_recovery_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_PROTECTED_DATABASE', 'UPDATE_PROTECTED_DATABASE', 'DELETE_PROTECTED_DATABASE', 'MOVE_PROTECTED_DATABASE', 'CREATE_PROTECTION_POLICY', 'UPDATE_PROTECTION_POLICY', 'DELETE_PROTECTION_POLICY', 'MOVE_PROTECTION_POLICY', 'CREATE_RECOVERY_SERVICE_SUBNET', 'UPDATE_RECOVERY_SERVICE_SUBNET', 'DELETE_RECOVERY_SERVICE_SUBNET', 'MOVE_RECOVERY_SERVICE_SUBNET'

`status`

(required) The status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The completed percentage of the operation tracked by the work request.

`time_accepted`

(required) The date and time the request was accepted, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29. The precision for this time object is in milliseconds.

`time_started`

(optional) The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29. The precision for this time object is in milliseconds.

`time_finished`

(optional) The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29. The precision for this time object is in milliseconds.

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_recovery_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Recovery Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-4195DB00-919D-44B6-99E9-465F9AE0A2D0)
- [DBMS_CLOUD_OCI_RECOVERY_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-5C5F836F-C1B3-474A-8ACC-EDB508CB5D86)
- [DBMS_CLOUD_OCI_RECOVERY_CHANGE_PROTECTED_DATABASE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-6E696ADB-DED2-4EBD-B6C9-6C82C1B21254)
- [DBMS_CLOUD_OCI_RECOVERY_CHANGE_PROTECTION_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-29EE206C-CC57-4392-9DCF-3F75B28FACA4)
- [DBMS_CLOUD_OCI_RECOVERY_CHANGE_RECOVERY_SERVICE_SUBNET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-910E3B22-E4EE-4A1C-AA6C-A00F7192D78E)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_INPUT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-8AD0677A-15AF-4711-BD45-83E3293C2F7E)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_INPUT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-4AFF7591-E729-43D9-9A74-118E8DB7D37F)
- [DBMS_CLOUD_OCI_RECOVERY_CREATE_PROTECTED_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-AA4C96A2-1503-479C-BA6E-056180F852DF)
- [DBMS_CLOUD_OCI_RECOVERY_CREATE_PROTECTION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-71B59193-0FBC-4AAF-861D-18FE6668B1DB)
- [DBMS_CLOUD_OCI_RECOVERY_CREATE_RECOVERY_SERVICE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-BA3C8535-E05A-4A76-AB47-EFA2CFA2BD0E)
- [DBMS_CLOUD_OCI_RECOVERY_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-33E583C5-3A25-4D15-A48A-C7FDEED03C87)
- [DBMS_CLOUD_OCI_RECOVERY_FETCH_PROTECTED_DATABASE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-ABC1B513-5200-47E4-A4C0-D623542111A7)
- [DBMS_CLOUD_OCI_RECOVERY_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-0C37695B-9F06-4BDA-97E2-1466C29CA321)
- [DBMS_CLOUD_OCI_RECOVERY_METRICS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-30EC8F6E-AB91-4613-8BC0-786847DC8863)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-2954F2F0-E4D7-4DE8-9753-ED5207D2FA4A)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-2843CC42-96DE-4D4C-B4CD-C3185F4CF4E9)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-E9DF720F-19B0-49BD-A5CD-53B6078BEE5C)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-30B6DA83-BCA0-4D3A-9DDF-CCB735744A2F)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-93E19F8D-42DC-453D-B249-981A4BCA9BBF)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTED_DATABASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-32CB5D60-8AA7-4130-B8E0-B0CF8E023A79)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-09300202-C60A-44B8-9B5C-740D4FCC75A7)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-083DFC49-55A5-4BA7-B65F-4BC70C575081)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-F1F7B8F7-41BB-4677-BC4C-967BC1F36C13)
- [DBMS_CLOUD_OCI_RECOVERY_PROTECTION_POLICY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-6385BAA9-ACB3-4C1C-A81C-337CB540277D)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-8FF58C04-7469-4F4B-BF29-EC5D83DDB628)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-B089D773-E84A-4894-B978-8E8946CE3324)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-C18AC456-24C9-4104-AD4E-C7D3A73150DB)
- [DBMS_CLOUD_OCI_RECOVERY_RECOVERY_SERVICE_SUBNET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-5C613467-AB01-4708-BF1F-3A5B6A2A5F6A)
- [DBMS_CLOUD_OCI_RECOVERY_UPDATE_PROTECTED_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-49F3226D-7D8B-48D9-9DBA-873106336FDA)
- [DBMS_CLOUD_OCI_RECOVERY_UPDATE_PROTECTION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-03487320-5081-4857-AC15-D26F99B506DF)
- [DBMS_CLOUD_OCI_RECOVERY_UPDATE_RECOVERY_SERVICE_SUBNET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-69ECCB98-2F1B-4816-9DF8-DE8687C924A9)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-BAFAC8F1-CE73-4DBE-BCB8-3527DA378CD6)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-ED28021B-54AD-469D-A9DD-4255D3C0E27B)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-F611F3BA-03A7-4C5B-A396-2D30C373B033)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-A29A9D71-44FA-4994-94E2-3B9E55A61A48)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-CBF23810-292A-48AA-812B-FEC524071A40)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-4D5570B4-3573-4FAF-9E4D-4D8117E5C1E3)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-FD3FF4DC-71D4-41F3-BB65-F9C00B76CB6D)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-EAB99189-58BE-4F57-9C04-60F287314397)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-E722A78D-694C-4B05-9448-844B78B6DAC5)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-59FCAE2A-E16D-43E9-A635-1DD78F3A1AE9)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-B2E3D869-D3A3-4331-8CE9-032E6730B7A2)
- [DBMS_CLOUD_OCI_RECOVERY_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/recovery_t.html#ADSDK-GUID-F04701CA-C563-4B4E-8649-1F1F56EF761A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
