# Fusion Apps Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#dcoc-content-body)

## Fusion Apps Common Types

### DBMS_CLOUD_OCI_FUSION_APPS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_ACTION_T Type

Action details

Syntax
```

```

Fields

Field Description

`reference_key`

(optional) Unique identifier of the object that represents the action

`action_type`

(required) Type of action

Allowed values are: 'QUARTERLY_UPGRADE', 'PATCH', 'VERTEX'

`state`

(optional) A string that describes whether the change is applied hot or cold

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'CANCELED'

`description`

(required) A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering confidential information.

### DBMS_CLOUD_OCI_FUSION_APPS_ADMIN_USER_SUMMARY_T Type

IDM admin credentials without password

Syntax
```

```

Fields

Field Description

`username`

(required) Admin username

`email_address`

(required) Admin users email address

`first_name`

(required) Admin users first name

`last_name`

(required) Admin users last name

### DBMS_CLOUD_OCI_FUSION_APPS_ADMIN_USER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_admin_user_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_ADMIN_USER_COLLECTION_T Type

IDM admin credentials without password

Syntax
```

```

Fields

Field Description

`items`

(required) A page of AdminUserSummary objects.

### DBMS_CLOUD_OCI_FUSION_APPS_RULE_CONDITION_T Type

A condition to apply to an access control rule.

Syntax
```

```

Fields

Field Description

`attribute_name`

(required) RuleCondition type

Allowed values are: 'SOURCE_IP_ADDRESS', 'SOURCE_VCN_ID', 'SOURCE_VCN_IP_ADDRESS'

### DBMS_CLOUD_OCI_FUSION_APPS_RULE_T Type

An object that represents an action to apply to a listener.

Syntax
```

```

Fields

Field Description

`action`

(required) Rule type

Allowed values are: 'ALLOW'

### DBMS_CLOUD_OCI_FUSION_APPS_RULE_CONDITION_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_rule_condition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_ALLOW_RULE_T Type

An object that represents the action of configuring an access control rule. Access control rules permit access to application resources based on user-specified match conditions. This rule applies only to HTTP listeners. **NOTES:** * If you do not specify any access control rules, the default rule is to allow all traffic. * If you add access control rules, the load balancer denies any traffic that does not match the rules. * Maximum of two match conditions can be specified in a rule. * You can specify this rule only with the following `RuleCondition` combinations: * `SOURCE_IP_ADDRESS` * `SOURCE_VCN_ID` * `SOURCE_VCN_ID\", \"SOURCE_VCN_IP_ADDRESS`

Syntax
```

```

`dbms_cloud_oci_fusion_apps_allow_rule_t`is a subtype of the`dbms_cloud_oci_fusion_apps_rule_t`type.

Fields

Field Description

`conditions`

(required)

`description`

(optional) A brief description of the access control rule. Avoid entering confidential information. example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`

### DBMS_CLOUD_OCI_FUSION_APPS_CAPABILITIES_T Type

Status of capabilities that can be enabled for an environment family.

Syntax
```

```

Fields

Field Description

`is_data_masking_enabled`

(optional) Indicates whether data masking is enabled for the environment family. When enabled, data masking activities are supported.

`is_break_glass_enabled`

(optional) Indicates whether Break Glass is enabled for the environment family.

`is_byok_enabled`

(optional) Indicates whether customers can use their own encryption keys.

### DBMS_CLOUD_OCI_FUSION_APPS_CHANGE_FUSION_ENVIRONMENT_COMPARTMENT_DETAILS_T Type

Details about the compartment the Fusion environment should move to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FUSION_APPS_CHANGE_FUSION_ENVIRONMENT_FAMILY_COMPARTMENT_DETAILS_T Type

Details about the compartment the environment family should be moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FUSION_APPS_CREATE_DATA_MASKING_ACTIVITY_DETAILS_T Type

The information about current data masking request.

Syntax
```

```

Fields

Field Description

`is_resume_data_masking`

(optional) This allows the Data Safe service to resume the previously failed data masking activity.

### DBMS_CLOUD_OCI_FUSION_APPS_CREATE_FUSION_ENVIRONMENT_ADMIN_USER_DETAILS_T Type

The credentials for the Fusion Applications service administrator.

Syntax
```

```

Fields

Field Description

`username`

(required) The username for the administrator.

`password`

(required) The password for the administrator.

`email_address`

(required) The email address for the administrator.

`first_name`

(required) The administrator's first name.

`last_name`

(required) The administrator's last name.

### DBMS_CLOUD_OCI_FUSION_APPS_MAINTENANCE_POLICY_T Type

The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see[Understanding Environment Maintenance](https://docs.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance).

Syntax
```

```

Fields

Field Description

`monthly_patching_override`

(optional) When \"ENABLED\", the Fusion environment is patched monthly. When \"DISABLED\", the Fusion environment is not patched monthly. This setting overrides the environment family setting. When not set, the environment follows the environment family policy.

Allowed values are: 'ENABLED', 'DISABLED', 'NONE'

`environment_maintenance_override`

(optional) User choice to upgrade both test and prod pods at the same time. Overrides fusion environment families'.

Allowed values are: 'PROD', 'NON_PROD', 'NONE'

### DBMS_CLOUD_OCI_FUSION_APPS_RULE_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_CREATE_FUSION_ENVIRONMENT_DETAILS_T Type

The configuration details of the FusionEnvironment. For more information about these fields, see[Managing Environments](https://docs.oracle.com/iaas/Content/fusion-applications/manage-environment.htm).

Syntax
```

```

Fields

Field Description

`display_name`

(required) FusionEnvironment Identifier can be renamed.

`maintenance_policy`

(optional)

`compartment_id`

(required) The unique identifier (OCID) of the compartment where the Fusion Environment is located.

`fusion_environment_family_id`

(required) The unique identifier (OCID) of the Fusion Environment Family that the Fusion Environment belongs to.

`fusion_environment_type`

(required) The type of environment. Valid values are Production, Test, or Development.

`kms_key_id`

(optional) byok kms keyId

`dns_prefix`

(optional) DNS prefix.

`additional_language_packs`

(optional) Language packs.

`rules`

(optional) Rules.

`create_fusion_environment_admin_user_details`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_FAMILY_MAINTENANCE_POLICY_T Type

The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see[Understanding Environment Maintenance](https://docs.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance).

Syntax
```

```

Fields

Field Description

`quarterly_upgrade_begin_times`

(optional) The quarterly maintenance month group schedule of the Fusion environment family.

`is_monthly_patching_enabled`

(optional) When True, monthly patching is enabled for the environment family.

`concurrent_maintenance`

(optional) Option to upgrade both production and non-production environments at the same time. When set to PROD both types of environnments are upgraded on the production schedule. When set to NON_PROD both types of environments are upgraded on the non-production schedule.

Allowed values are: 'PROD', 'NON_PROD', 'DISABLED'

### DBMS_CLOUD_OCI_FUSION_APPS_CREATE_FUSION_ENVIRONMENT_FAMILY_DETAILS_T Type

The information about new FusionEnvironmentFamily.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.

`family_maintenance_policy`

(optional)

`compartment_id`

(required) The OCID of the compartment where the environment family is located.

`subscription_ids`

(required) The list of the IDs of the applications subscriptions that are associated with the environment family.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_CREATE_REFRESH_ACTIVITY_DETAILS_T Type

The information about current refresh.

Syntax
```

```

Fields

Field Description

`source_fusion_environment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source environment

`time_scheduled_start`

(optional) Current time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_FUSION_APPS_CREATE_SERVICE_ATTACHMENT_DETAILS_T Type

Information about the service attachment to be created.

Syntax
```

```

Fields

Field Description

`service_instance_type`

(required) Type of the ServiceInstance being attached.

`service_instance_id`

(required) The service instance OCID of the instance being attached

### DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_T Type

Details of data masking activity.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`fusion_environment_id`

(required) Fusion Environment Identifier.

`lifecycle_state`

(required) The current state of the DataMaskingActivity.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELED'

`time_masking_start`

(required) The time the data masking activity started. An RFC3339 formatted datetime string.

`time_masking_finish`

(required) The time the data masking activity ended. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_SUMMARY_T Type

Summary of the data masking activity.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`lifecycle_state`

(required) The current state of the data masking activity Scheduled, In progress , Failed, Completed

`time_masking_start`

(required) The time the data masking activity started. An RFC3339 formatted datetime string.

`time_masking_finish`

(required) The time the data masking activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_data_masking_activity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_COLLECTION_T Type

Results of data masking activities on a given Fusion Environment.

Syntax
```

```

Fields

Field Description

`items`

(required) A page of data masking activity objects.

### DBMS_CLOUD_OCI_FUSION_APPS_ENVIRONMENT_ROLE_T Type

Describes the role of the FA Environment.

Syntax
```

```

Fields

Field Description

`current_role`

(optional) The current role of the environment

Allowed values are: 'PRIMARY', 'STANDBY'

`standby_environment_region`

(optional) Region the standby environment is in

`standby_environment_id`

(optional) Fusion Environment ID of the standby environment

### DBMS_CLOUD_OCI_FUSION_APPS_ERROR_T Type

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

### DBMS_CLOUD_OCI_FUSION_APPS_QUARTERLY_UPGRADE_BEGIN_TIMES_T Type

Determines the quarterly upgrade begin times (monthly maintenance group schedule ) of the Fusion environment.

Syntax
```

```

Fields

Field Description

`override_type`

(optional) Determines if the maintenance schedule of the Fusion environment is inherited from the Fusion environment family.

Allowed values are: 'OVERRIDDEN', 'INHERITED'

`begin_times_value`

(optional) The frequency and month when maintenance occurs for the Fusion environment.

### DBMS_CLOUD_OCI_FUSION_APPS_GET_MAINTENANCE_POLICY_DETAILS_T Type

The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see[Understanding Environment Maintenance](https://docs.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance).

Syntax
```

```

Fields

Field Description

`quarterly_upgrade_begin_times`

(optional)

`monthly_patching_override`

(optional) Whether the Fusion environment will be updated monthly or updated on the quarterly cycle. This setting overrides the monthly patching setting of its Fusion environment family.

`environment_maintenance_override`

(optional) User choice to upgrade both production and non-production environments at the same time. Overrides the Fusion environment family setting.

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_DETAILS_T Type

Describes a refresh of a fusion environment

Syntax
```

```

Fields

Field Description

`source_fusion_environment_id`

(required) The source environment id for the last refresh

`time_finished`

(required) The time of when the last refresh finish

`time_of_restoration_point`

(required) The point of time of the latest DB backup for the last refresh

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_T Type

Description of FusionEnvironment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) FusionEnvironment Identifier, can be renamed

`maintenance_policy`

(optional)

`time_upcoming_maintenance`

(optional) The next maintenance for this environment

`compartment_id`

(required) Compartment Identifier

`fusion_environment_family_id`

(optional) FusionEnvironmentFamily Identifier

`subscription_ids`

(optional) List of subscription IDs.

`fusion_environment_type`

(required) Type of the FusionEnvironment.

Allowed values are: 'PRODUCTION', 'TEST', 'DEVELOPMENT'

`kms_key_id`

(optional) BYOK key id

`kms_key_info`

(optional) BYOK key info

`domain_id`

(optional) The IDCS domain created for the fusion instance

`idcs_domain_url`

(optional) The IDCS Domain URL

`applied_patch_bundles`

(optional) Patch bundle names

`version`

(optional) Version of Fusion Apps used by this environment

`public_url`

(optional) Public URL

`dns_prefix`

(optional) DNS prefix

`additional_language_packs`

(optional) Language packs

`lockbox_id`

(optional) The lockbox Id of this fusion environment. If there's no lockbox id, this field will be null

`is_break_glass_enabled`

(optional) If it's true, then the Break Glass feature is enabled

`refresh`

(optional)

`rules`

(optional) Network Access Control Rules

`time_created`

(optional) The time the the FusionEnvironment was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the FusionEnvironment was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the ServiceInstance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`system_name`

(optional) Environment Specific Guid/ System Name

`environment_role`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_SUMMARY_T Type

Summary of the internal FA Environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) FusionEnvironment Identifier, can be renamed

`time_upcoming_maintenance`

(optional) The next maintenance for this environment

`maintenance_policy`

(optional)

`compartment_id`

(required) Compartment Identifier

`fusion_environment_family_id`

(optional) FusionEnvironmentFamily Identifier

`subscription_ids`

(optional) List of subscription IDs.

`applied_patch_bundles`

(optional) Patch bundle names

`fusion_environment_type`

(required) Type of the FusionEnvironment.

`version`

(optional) Version of Fusion Apps used by this environment

`public_url`

(optional) Public URL

`dns_prefix`

(optional) DNS prefix

`additional_language_packs`

(optional) Language packs

`lockbox_id`

(optional) The lockbox Id of this fusion environment. If there's no lockbox id, this field will be null

`is_break_glass_enabled`

(optional) If it's true, then the Break Glass feature is enabled

`time_created`

(optional) The time the the FusionEnvironment was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the FusionEnvironment was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the FusionEnvironment.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_fusion_environment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_COLLECTION_T Type

Results of a fusion environment search.

Syntax
```

```

Fields

Field Description

`items`

(required) A page of FusionEnvironmentSummary objects.

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_T Type

Details of a Fusion environment family. An environment family is a logical grouping of environments. The environment family defines a set of characteristics that are shared across the environments to allow consistent management and maintenance across your production, test, and development environments. For more information, see[Planning an Environment Family](https://docs.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the environment family. Can't be changed after creation.

`display_name`

(required) A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.

`family_maintenance_policy`

(optional)

`compartment_id`

(required) The OCID of the compartment where the environment family is located.

`subscription_ids`

(required) The list of the IDs of the applications subscriptions that are associated with the environment family.

`is_subscription_update_needed`

(optional) When set to True, a subscription update is required for the environment family.

`time_created`

(optional) The time the the FusionEnvironmentFamily was created. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the FusionEnvironmentFamily.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`system_name`

(optional) Environment Specific Guid/ System Name

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_SUMMARY_T Type

Summary information for a Fusion environment family.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the environment family. Can't be changed after creation.

`display_name`

(required) A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.

`family_maintenance_policy`

(optional)

`compartment_id`

(required) The OCID of the compartment where the environment family is located.

`subscription_ids`

(required) The list of the IDs of the applications subscriptions that are associated with the environment family.

`is_subscription_update_needed`

(optional) When set to True, a subscription update is required for the environment family.

`time_created`

(optional) The time the the FusionEnvironmentFamily was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the FusionEnvironmentFamily was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the FusionEnvironmentFamily.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_fusion_environment_family_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_COLLECTION_T Type

Results of a Fusion environment family search.

Syntax
```

```

Fields

Field Description

`items`

(required) A page of FusionEnvironmentFamilySummary objects.

### DBMS_CLOUD_OCI_FUSION_APPS_LIMIT_AND_USAGE_T Type

The limit and usage for a specific environment type, for example, production, development, or test.

Syntax
```

```

Fields

Field Description

`limit`

(required) The limit of current environment.

`usage`

(required) The usage of current environment.

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_LIMITS_AND_USAGE_T Type

Details of EnvironmentLimits.

Syntax
```

```

Fields

Field Description

`production_limit_and_usage`

(required)

`test_limit_and_usage`

(required)

`development_limit_and_usage`

(required)

### DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_STATUS_T Type

The health status of the Fusion Applications environment. For more information, see[Environment Status](https://docs.oracle.com/iaas/Content/fusion-applications/manage-environment.htm#environment-status).

Syntax
```

```

Fields

Field Description

`status`

(required) The data plane status of FusionEnvironment.

Allowed values are: 'AVAILABLE', 'UNAVAILABLE', 'NOT_APPLICABLE', 'MAINTENANCE_IN_PROGRESS', 'REFRESH_IN_PROGRESS', 'UNKNOWN'

### DBMS_CLOUD_OCI_FUSION_APPS_KMS_KEY_INFO_T Type

kmsKeyInfo

Syntax
```

```

Fields

Field Description

`active_key_id`

(optional) current BYOK keyId facp is using

`active_key_version`

(optional) current key version facp is using

`scheduled_key_id`

(optional) scheduled keyId to be updated

`scheduled_key_version`

(optional) scheduled key version to be updated.

`current_key_lifecycle_state`

(optional) current key lifeCycleState

`scheduled_lifecycle_state`

(optional) scheduled key lifeCycle state to be updated.

`scheduled_key_status`

(optional) the scheduled key status

Allowed values are: 'SCHEDULING', 'UPDATING', 'FAILED', 'NONE'

### DBMS_CLOUD_OCI_FUSION_APPS_PATCH_ACTION_T Type

Monthly patch details.

Syntax
```

```

`dbms_cloud_oci_fusion_apps_patch_action_t`is a subtype of the`dbms_cloud_oci_fusion_apps_action_t`type.

Fields

Field Description

`l_mode`

(optional) A string that describeds whether the change is applied hot or cold

Allowed values are: 'HOT', 'COLD'

`category`

(optional) patch artifact category

Allowed values are: 'MONTHLY', 'WEEKLY', 'ONEOFF'

`artifact`

(optional) patch bundle name

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ISSUE_DETAILS_T Type

Details of refresh failure or validation failure that needs to be investigated.

Syntax
```

```

Fields

Field Description

`refresh_issues`

(optional) Detail reasons of refresh failure or validation failure that needs to be shown to customer.

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ISSUE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_refresh_issue_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_T Type

An environment refresh copies data from a source environment to a target environment, making a copy of the source environment onto the target environment. For more information, see[Refreshing an Environment](https://docs.oracle.com/iaas/Content/fusion-applications/refresh-environment.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the refresh activity. Can't be changed after creation.

`display_name`

(required) A friendly name for the refresh activity. Can be changed later.

`source_fusion_environment_id`

(required) The OCID of the Fusion environment that is the source environment for the refresh.

`time_of_restoration_point`

(optional) The date and time of the most recent source environment backup used for the environment refresh.

`lifecycle_state`

(required) The current state of the refreshActivity.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELED'

`service_availability`

(required) Service availability / impact during refresh activity execution up down

Allowed values are: 'AVAILABLE', 'UNAVAILABLE'

`time_scheduled_start`

(required) The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.

`time_expected_finish`

(required) The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.

`time_finished`

(optional) The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.

`time_accepted`

(optional) The time the refresh activity record was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the refresh activity record was updated. An RFC3339 formatted datetime string.

`refresh_issue_details_list`

(optional) Details of refresh investigation information, each item represents a different issue.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

Allowed values are: 'NONE', 'ROLLBACKACCEPTED', 'ROLLBACKINPROGRESS', 'ROLLBACKSUCCEEDED', 'ROLLBACKFAILED'

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_SUMMARY_T Type

Summary of the refresh activity.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier (OCID) of the refresh activity. Can't be changed after creation.

`display_name`

(required) A friendly name for the refresh activity. Can be changed later.

`source_fusion_environment_id`

(required) The OCID of the Fusion environment that is the source environment for the refresh.

`time_of_restoration_point`

(optional) The date and time of the most recent source environment backup used for the environment refresh.

`lifecycle_state`

(required) The current state of the refresh activity. Valid values are Scheduled, In progress , Failed, Completed.

`time_scheduled_start`

(required) The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.

`time_expected_finish`

(required) The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.

`time_finished`

(optional) The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.

`service_availability`

(required) Service availability / impact during refresh activity execution, up down

`time_accepted`

(optional) The time the refresh activity record was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the refresh activity record was updated. An RFC3339 formatted datetime string.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`refresh_issue_details_list`

(optional) Details of refresh investigation information, each item represents a different issue.

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_refresh_activity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_COLLECTION_T Type

Results of a refresh activity search.

Syntax
```

```

Fields

Field Description

`items`

(required) A page of refresh activity objects.

### DBMS_CLOUD_OCI_FUSION_APPS_RESET_FUSION_ENVIRONMENT_PASSWORD_DETAILS_T Type

IDM admin credentials

Syntax
```

```

Fields

Field Description

`password`

(required) Admin password

### DBMS_CLOUD_OCI_FUSION_APPS_ACTION_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_action_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_T Type

Details of scheduled activity.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) scheduled activity display name, can be renamed.

`run_cycle`

(required) run cadence.

Allowed values are: 'QUARTERLY', 'MONTHLY', 'ONEOFF', 'VERTEX'

`fusion_environment_id`

(required) FAaaS Environment Identifier.

`lifecycle_state`

(required) The current state of the scheduledActivity.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELED'

`actions`

(optional) List of actions

`service_availability`

(required) Service availability / impact during scheduled activity execution up down

Allowed values are: 'AVAILABLE', 'UNAVAILABLE'

`time_scheduled_start`

(required) Current time the scheduled activity is scheduled to start. An RFC3339 formatted datetime string.

`time_expected_finish`

(required) Current time the scheduled activity is scheduled to end. An RFC3339 formatted datetime string.

`time_finished`

(optional) The time the scheduled activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.

`delay_in_hours`

(optional) Cumulative delay hours

`time_created`

(optional) The time the scheduled activity record was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the scheduled activity record was updated. An RFC3339 formatted datetime string.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

Allowed values are: 'NONE', 'ROLLBACKACCEPTED', 'ROLLBACKINPROGRESS', 'ROLLBACKSUCCEEDED', 'ROLLBACKFAILED'

`scheduled_activity_phase`

(required) A property describing the phase of the scheduled activity.

Allowed values are: 'PRE_MAINTENANCE', 'MAINTENANCE', 'POST_MAINTENANCE'

`scheduled_activity_association_id`

(required) The unique identifier that associates a scheduled activity with others in one complete maintenance. For example, with ZDT, a complete upgrade maintenance includes 5 scheduled activities - PREPARE, EXECUTE, POST, PRE_MAINTENANCE, and POST_MAINTENANCE. All of them share the same unique identifier - scheduledActivityAssociationId.

### DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_SUMMARY_T Type

Summary of the scheduled activity for a Fusion environment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`display_name`

(required) A friendly name for the scheduled activity. Can be changed later.

`run_cycle`

(required) The run cadence of this scheduled activity. Valid values are Quarterly, Monthly, OneOff, and Vertex.

`fusion_environment_id`

(required) The OCID of the Fusion environment for the scheduled activity.

`lifecycle_state`

(required) The current state of the scheduled activity. Valid values are Scheduled, In progress , Failed, Completed.

`actions`

(optional) List of actions

`time_scheduled_start`

(required) Current time the scheduled activity is scheduled to start. An RFC3339 formatted datetime string.

`time_expected_finish`

(required) Current time the scheduled activity is scheduled to end. An RFC3339 formatted datetime string.

`time_finished`

(optional) The time the scheduled activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.

`delay_in_hours`

(optional) Cumulative delay hours

`service_availability`

(required) Service availability / impact during scheduled activity execution, up down

`time_accepted`

(optional) The time the scheduled activity record was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the scheduled activity record was updated. An RFC3339 formatted datetime string.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`scheduled_activity_phase`

(required) A property describing the phase of the scheduled activity.

`scheduled_activity_association_id`

(required) The unique identifier that associates a scheduled activity with others in one complete maintenance. For example, with ZDT, a complete upgrade maintenance includes 5 scheduled activities - PREPARE, EXECUTE, POST, PRE_MAINTENANCE, and POST_MAINTENANCE. All of them share the same unique identifier - scheduledActivityAssociationId.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_scheduled_activity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_COLLECTION_T Type

Results of a scheduled activity search.

Syntax
```

```

Fields

Field Description

`items`

(required) A page of scheduled activity objects.

### DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_T Type

Description of ServiceAttachment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`compartment_id`

(optional) Compartment Identifier

`service_instance_id`

(optional) The ID of the service instance created that can be used to identify this on the service control plane

`display_name`

(required) Service Attachment Display name, can be renamed

`service_instance_type`

(required) Type of the serviceInstance.

Allowed values are: 'DIGITAL_ASSISTANT', 'INTEGRATION_CLOUD', 'ANALYTICS_WAREHOUSE', 'VBCS', 'VISUAL_BUILDER_STUDIO'

`service_url`

(optional) Public URL

`time_created`

(optional) The time the the ServiceInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the ServiceInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the ServiceInstance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_sku_based`

(required) Whether this service is provisioned due to the customer being subscribed to a specific SKU

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_SUMMARY_T Type

Summary of the ServiceInstance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`display_name`

(required) ServiceInstance Identifier, can be renamed

`service_instance_type`

(required) Type of the service.

`service_instance_id`

(optional) The ID of the service instance created that can be used to identify this on the service control plane

`service_url`

(optional) Service URL of the instance

`time_created`

(optional) The time the service instance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the serivce instance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the ServiceInstance.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`is_sku_based`

(required) Whether this service is provisioned due to the customer being subscribed to a specific SKU

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_service_attachment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_COLLECTION_T Type

List of service attachments for a fusion instance.

Syntax
```

```

Fields

Field Description

`items`

(required) A page of FusionEnvironmentFamilySummary objects.

### DBMS_CLOUD_OCI_FUSION_APPS_SOURCE_IP_ADDRESS_CONDITION_T Type

An access control rule condition that requires a match on the specified source IP address or address range.

Syntax
```

```

`dbms_cloud_oci_fusion_apps_source_ip_address_condition_t`is a subtype of the`dbms_cloud_oci_fusion_apps_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) An IPv4 or IPv6 address range that the source IP address of an incoming packet must match. The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y or x:x::x/y) strings. Specify 0.0.0.0/0 or ::/0 to match all incoming traffic. example: \"192.168.0.0/16\"

### DBMS_CLOUD_OCI_FUSION_APPS_SOURCE_VCN_ID_CONDITION_T Type

An access control rule condition that requires a match on the specified source VCN OCID.

Syntax
```

```

`dbms_cloud_oci_fusion_apps_source_vcn_id_condition_t`is a subtype of the`dbms_cloud_oci_fusion_apps_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) The OCID of the originating VCN that an incoming packet must match. You can use this condition in conjunction with `SourceVcnIpAddressCondition`. **NOTE:** If you define this condition for a rule without a `SourceVcnIpAddressCondition`, this condition matches all incoming traffic in the specified VCN.

### DBMS_CLOUD_OCI_FUSION_APPS_SOURCE_VCN_IP_ADDRESS_CONDITION_T Type

An access control rule condition that requires a match on the specified source VCN and IP address range. This condition must be used only in conjunction with `SourceVcnIdCondition`.

Syntax
```

```

`dbms_cloud_oci_fusion_apps_source_vcn_ip_address_condition_t`is a subtype of the`dbms_cloud_oci_fusion_apps_rule_condition_t`type.

Fields

Field Description

`attribute_value`

(required) An IPv4 address range that the original client IP address (in the context of the specified VCN) of an incoming packet must match. The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y) strings. Specify 0.0.0.0/0 to match all incoming traffic in the customer VCN.

### DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_SKU_T Type

SKU information.

Syntax
```

```

Fields

Field Description

`sku`

(required) Stock keeping unit id.

`license_part_description`

(optional) Description of the covered product belonging to this Sku.

`metric_name`

(optional) Base metric for billing the service.

`quantity`

(required) Quantity of the stock units.

`description`

(optional) Description of the stock units.

### DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_SKU_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_subscription_sku_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_T Type

Subscription information for compartmentId. Only root compartments are allowed.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the subscription details for particular root compartment or tenancy.

`classic_subscription_id`

(required) Subscription id.

`service_name`

(required) The type of subscription, such as 'CLOUDCM'/'SAAS'/'CRM', etc.

`skus`

(required) Stock keeping unit.

### DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_subscription_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_DETAIL_T Type

Detail for the FusionEnvironmentFamily subscription.

Syntax
```

```

Fields

Field Description

`subscriptions`

(required) List of subscriptions.

### DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_T Type

one available refresh time.

Syntax
```

```

Fields

Field Description

`time_available_for_refresh`

(required) refresh time.

### DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_SUMMARY_T Type

one available refresh time.

Syntax
```

```

Fields

Field Description

`time_available_for_refresh`

(required) refresh time.

### DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_time_available_for_refresh_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_COLLECTION_T Type

The available refresh times for a fusion environment

Syntax
```

```

Fields

Field Description

`items`

(required) A list of available refresh time objects.

### DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_FAMILY_MAINTENANCE_POLICY_DETAILS_T Type

The editable settings of the policy that specifies the maintenance and upgrade preferences for an environment.

Syntax
```

```

Fields

Field Description

`is_monthly_patching_enabled`

(optional) Whether the Fusion environment receives monthly patching.

`concurrent_maintenance`

(optional) Whether production and non-production environments are upgraded concurrently.

### DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_FUSION_ENVIRONMENT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) FusionEnvironment Identifier, can be renamed

`kms_key_id`

(optional) byok kms keyId

`maintenance_policy`

(optional)

`additional_language_packs`

(optional) Language packs

`rules`

(optional) Network access control rules to limit internet traffic that can access the environment. For more information, see`ALLOW_RULE`Function.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_FUSION_ENVIRONMENT_FAMILY_DETAILS_T Type

The details of the Fusion environment family to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.

`family_maintenance_policy`

(optional)

`subscription_ids`

(optional) The list of the IDs of the applications subscriptions that are associated with the environment family.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_REFRESH_ACTIVITY_DETAILS_T Type

The information about scheduled refresh.

Syntax
```

```

Fields

Field Description

`time_scheduled_start`

(optional) Time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_FUSION_APPS_UPGRADE_ACTION_T Type

Quarterly upgrade details.

Syntax
```

```

`dbms_cloud_oci_fusion_apps_upgrade_action_t`is a subtype of the`dbms_cloud_oci_fusion_apps_action_t`type.

Fields

Field Description

`version`

(optional) name of the repo

`qualifier`

(optional) month qualifier

### DBMS_CLOUD_OCI_FUSION_APPS_VERIFY_SERVICE_ATTACHMENT_DETAILS_T Type

Information about the service attachment to be verified.

Syntax
```

```

Fields

Field Description

`service_instance_type`

(required) Type of the ServiceInstance being attached.

`service_instance_id`

(required) The service instance OCID of the instance being attached

### DBMS_CLOUD_OCI_FUSION_APPS_VERTEX_ACTION_T Type

Vertex update action

Syntax
```

```

`dbms_cloud_oci_fusion_apps_vertex_action_t`is a subtype of the`dbms_cloud_oci_fusion_apps_action_t`type.

Fields

Field Description

`artifact`

(optional) patch that delivered the vertex update prerequisite

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_RESOURCE_T Type

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

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Possible operation types.

Allowed values are: 'CREATE_FUSION_ENVIRONMENT', 'UPDATE_FUSION_ENVIRONMENT', 'RESET_FUSION_ENVIRONMENT_ADMIN_PASSWORD', 'SCALE_FUSION_ENVIRONMENT', 'ARCHIVE_FUSION_ENVIRONMENT', 'RESTORE_FUSION_ENVIRONMENT', 'CREATE_SERVICE_INSTANCE', 'UPDATE_SERVICE_INSTANCE', 'DETACH_SERVICE_INSTANCE', 'ADD_USER', 'REMOVE_USER', 'DELETE_FUSION_ENVIRONMENT', 'CHANGE_FUSION_ENVIRONMENT_COMPARTMENT', 'UPGRADE_FUSION_ENVIRONMENT', 'CREATE_FUSION_ENVIRONMENT_FAMILY', 'DELETE_FUSION_ENVIRONMENT_FAMILY', 'UPDATE_FUSION_ENVIRONMENT_FAMILY', 'CHANGE_FUSION_ENVIRONMENT_FAMILY_COMPARTMENT', 'REFRESH_FUSION_ENVIRONMENT', 'EXECUTE_COLD_PATCH', 'DATA_MASK_FUSION_ENVIRONMENT'

`status`

(required) Possible operation status.

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

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_ERROR_T Type

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

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_LOG_ENTRY_T Type

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

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Possible operation types.

`status`

(required) Possible operation status.

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

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_fusion_apps_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Fusion Apps Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-6BBDB3DE-F17D-44D5-8296-35217B510271)
- [DBMS_CLOUD_OCI_FUSION_APPS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-7D7E8D90-D5C1-4F28-B5BE-DEBB1ABFD098)
- [DBMS_CLOUD_OCI_FUSION_APPS_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-0D6A638F-4994-4725-A2DC-F19553A39E9C)
- [DBMS_CLOUD_OCI_FUSION_APPS_ADMIN_USER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-F10B3E43-EAE6-4BC3-ACDA-A9350F3FE179)
- [DBMS_CLOUD_OCI_FUSION_APPS_ADMIN_USER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-682332C4-6296-41D8-BF00-A0046A46000A)
- [DBMS_CLOUD_OCI_FUSION_APPS_ADMIN_USER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-CD373354-3450-4972-8F13-08E61DD68C2C)
- [DBMS_CLOUD_OCI_FUSION_APPS_RULE_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-77ADD311-DAA0-4547-9118-140468687CD1)
- [DBMS_CLOUD_OCI_FUSION_APPS_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-910CE080-70A3-4ADE-963F-B6BD780D4388)
- [DBMS_CLOUD_OCI_FUSION_APPS_RULE_CONDITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-E3D67D9E-E2C1-40EC-B67E-29EC2D452574)
- [DBMS_CLOUD_OCI_FUSION_APPS_ALLOW_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-D049C87C-D2FD-4431-A8CE-540453907E5A)
- [DBMS_CLOUD_OCI_FUSION_APPS_CAPABILITIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-926C463B-6FA1-4A6F-92FE-A8D2868A984E)
- [DBMS_CLOUD_OCI_FUSION_APPS_CHANGE_FUSION_ENVIRONMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-B348631A-4E42-4C29-8C93-8C36484C085E)
- [DBMS_CLOUD_OCI_FUSION_APPS_CHANGE_FUSION_ENVIRONMENT_FAMILY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-6A6F58AB-A6B6-404B-9391-AB1B4B6A7839)
- [DBMS_CLOUD_OCI_FUSION_APPS_CREATE_DATA_MASKING_ACTIVITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-70977FFF-A8D6-4562-AD2E-731832B3C52A)
- [DBMS_CLOUD_OCI_FUSION_APPS_CREATE_FUSION_ENVIRONMENT_ADMIN_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-5E19E589-B807-4E0D-81B3-5155442ED947)
- [DBMS_CLOUD_OCI_FUSION_APPS_MAINTENANCE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-FB967C3D-793A-43AA-B476-E3BFEE1822A9)
- [DBMS_CLOUD_OCI_FUSION_APPS_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-F6CF8C00-0047-445F-B6D0-903E586763D5)
- [DBMS_CLOUD_OCI_FUSION_APPS_CREATE_FUSION_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-3AC9386E-62F4-4763-B699-DA240947125A)
- [DBMS_CLOUD_OCI_FUSION_APPS_FAMILY_MAINTENANCE_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-84A63F42-1D64-4F3D-9FD9-C2B68CDBA94D)
- [DBMS_CLOUD_OCI_FUSION_APPS_CREATE_FUSION_ENVIRONMENT_FAMILY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-C46E5491-7227-44D3-8162-91A44B5D8CAA)
- [DBMS_CLOUD_OCI_FUSION_APPS_CREATE_REFRESH_ACTIVITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-E21EA4D2-6CB0-45B8-9A70-0EF3A8061624)
- [DBMS_CLOUD_OCI_FUSION_APPS_CREATE_SERVICE_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-1A83195D-9405-42DC-965C-896744F5A30E)
- [DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-05A2BDDC-43C2-45A4-8C13-A3EEDDB1FDA3)
- [DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-F66211AD-B3B6-4B9E-ADF9-C89202B109E3)
- [DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-D66B87B2-FD7D-428E-AE15-A8481BF7BF90)
- [DBMS_CLOUD_OCI_FUSION_APPS_DATA_MASKING_ACTIVITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-E16849C3-411B-42E4-9F85-7081696AD9C6)
- [DBMS_CLOUD_OCI_FUSION_APPS_ENVIRONMENT_ROLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-E0AB3FD9-A638-4482-B768-96500F4B2C09)
- [DBMS_CLOUD_OCI_FUSION_APPS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-AB24311D-1459-4A68-B9D5-3C566C24F3F0)
- [DBMS_CLOUD_OCI_FUSION_APPS_QUARTERLY_UPGRADE_BEGIN_TIMES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-9D05A566-D935-404E-9F22-DAEA99335F40)
- [DBMS_CLOUD_OCI_FUSION_APPS_GET_MAINTENANCE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-F9E30AF6-59FA-4F1D-92C8-72AD1B2F853E)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-836DFEBE-4FAD-4C0C-A593-BC64516E096D)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-50E08B5D-A20E-46A5-B918-D3330E7C7366)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-BEB37504-9161-422D-B753-82DBCFC396FB)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-EE21238D-4F70-4192-B344-353DFDDF2AD1)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-BBE259CA-9DCD-476F-AD48-988C1A3D76CB)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-2FF86908-81C5-494D-8B81-4CEF20D32410)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-A6066E2F-9850-4486-B298-85593D31392E)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-859EF5CD-AF35-43D1-9356-786A97915C91)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-03F4D36C-7B36-46E9-B688-AC2A5B51D0A8)
- [DBMS_CLOUD_OCI_FUSION_APPS_LIMIT_AND_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-791813A1-B3BE-472C-98DD-14C42376EED1)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_FAMILY_LIMITS_AND_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-0398081C-4F15-454F-9F8B-40DFB3613A1D)
- [DBMS_CLOUD_OCI_FUSION_APPS_FUSION_ENVIRONMENT_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-3ED3260F-9F59-428D-8DC0-4E7125140386)
- [DBMS_CLOUD_OCI_FUSION_APPS_KMS_KEY_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-A824DC26-6D44-483C-A590-756838011CFE)
- [DBMS_CLOUD_OCI_FUSION_APPS_PATCH_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-7CEB4F17-00E2-4AB6-80A9-E9BABE120CDD)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ISSUE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-B7C03D74-241A-490C-B51D-8865BE4121CD)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ISSUE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-60D794BC-7564-405C-9BFB-FEC4D5E34E76)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-CDE7095F-933D-4B5E-9201-D8BAA1989CC5)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-103BB6EE-65F9-4502-8589-05152BC9CC87)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-406BA916-6940-4A12-8372-E4CA268F31F2)
- [DBMS_CLOUD_OCI_FUSION_APPS_REFRESH_ACTIVITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-24025068-C43E-407F-96A5-97627A460360)
- [DBMS_CLOUD_OCI_FUSION_APPS_RESET_FUSION_ENVIRONMENT_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-1368F317-BD59-46FC-B81D-8A341E44F336)
- [DBMS_CLOUD_OCI_FUSION_APPS_ACTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-A44D6050-B14F-46EF-9E76-7E065F7E3ACC)
- [DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-C14BE677-9333-43DC-B762-5EAD4BEAEDB0)
- [DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-A4B2C235-A7B0-49D3-A75E-603D55625CD5)
- [DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-A1FE120C-6382-490E-A391-4D9F815DC78E)
- [DBMS_CLOUD_OCI_FUSION_APPS_SCHEDULED_ACTIVITY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-7A4E061E-3F2E-4F1D-A678-B05254976C64)
- [DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-677BB9DA-7F72-451C-B080-095AC50DFE75)
- [DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-BE7A1E3B-A62B-418D-A625-F651D1586819)
- [DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-65EB9D83-12F3-4F84-9897-2C352ED11CFA)
- [DBMS_CLOUD_OCI_FUSION_APPS_SERVICE_ATTACHMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-76962E7F-C0B5-417E-9902-1D4C1ED4CBEB)
- [DBMS_CLOUD_OCI_FUSION_APPS_SOURCE_IP_ADDRESS_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-3ADEB5AD-791C-4577-9F0B-5D0594803A76)
- [DBMS_CLOUD_OCI_FUSION_APPS_SOURCE_VCN_ID_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-6812D4EB-2BB5-4505-B926-6C7A1A7347DD)
- [DBMS_CLOUD_OCI_FUSION_APPS_SOURCE_VCN_IP_ADDRESS_CONDITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-17EADD92-B5F1-4DCB-AF42-A50C22DE5B48)
- [DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_SKU_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-726822B6-67FA-4AC7-8F52-9073AC47CCBA)
- [DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_SKU_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-E8C0B7F8-F9A2-4E72-9D09-529F6D20D5D0)
- [DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-3BBB8C2C-4513-46E5-AA33-99A71AB78890)
- [DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-3DE5008A-BF96-4C97-8BAE-C87EA2DFF202)
- [DBMS_CLOUD_OCI_FUSION_APPS_SUBSCRIPTION_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-DD41E145-2C93-45BC-887D-E6FB7D50D2CD)
- [DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-EEDEC68B-5142-48D0-BBD4-AB5E4BE55EE8)
- [DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-64FF4CD6-CD63-44EB-965B-9E47E7260A16)
- [DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-F7ADB0E6-B7D0-4BD6-8A06-EB0C09999E7C)
- [DBMS_CLOUD_OCI_FUSION_APPS_TIME_AVAILABLE_FOR_REFRESH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-868B4CB3-9A89-437B-9CA5-480F1C10768A)
- [DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_FAMILY_MAINTENANCE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-2AB5BF9F-BB3E-4102-9D4A-15D63F2816F4)
- [DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_FUSION_ENVIRONMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-5969FE1C-D610-4E5B-B5B8-6E2877400416)
- [DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_FUSION_ENVIRONMENT_FAMILY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-4AF504A5-E8D4-48EA-822A-FBAA3ADE0E83)
- [DBMS_CLOUD_OCI_FUSION_APPS_UPDATE_REFRESH_ACTIVITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-C6CAF811-6C07-4DCF-9D26-B2F8609A8A71)
- [DBMS_CLOUD_OCI_FUSION_APPS_UPGRADE_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-357DD7D7-C402-4CBB-AC62-76DB2306D39C)
- [DBMS_CLOUD_OCI_FUSION_APPS_VERIFY_SERVICE_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-86F94F0C-A9E4-4C2F-963D-06D4B92766C2)
- [DBMS_CLOUD_OCI_FUSION_APPS_VERTEX_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-69319A32-C050-4ECC-9F17-9BAE8BCE7EB2)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-312C6719-A785-4F04-9DC7-4074E5C25F9B)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-0E41C319-5769-43F2-BF05-F5281E458A71)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-DBC811B8-4E5F-401B-B062-7231C87469EB)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-07DB5EE1-8F39-447F-8656-833628212CF9)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-A5CD030F-5613-47E8-8FDC-686D9E3DEF0B)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-867AB44B-6245-4BCF-8B45-ECF9EDFAFD0C)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-96DC7DBD-EEB7-432A-A583-65B754B4FDEE)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-7984B2AB-02F4-403D-8072-254B2F16F4B6)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-DF1AF81D-FEA3-4318-9B2E-0D872CD7AA51)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-B5C78E9E-742F-4357-B5FB-56ED806E063F)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-42ACE650-910A-4459-A741-3C53A46FDB00)
- [DBMS_CLOUD_OCI_FUSION_APPS_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/fusion_apps_t.html#ADSDK-GUID-DA3C73A8-2D18-4903-B899-0236CC03D96E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
