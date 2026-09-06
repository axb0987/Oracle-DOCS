# Resource Manager Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#dcoc-content-body)

## Resource Manager Common Types

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_ADVANCED_OPTIONS_T Type

Specifies advanced options for Terraform commands. These options are not necessary for normal usage of Terraform.

Syntax
```

```

Fields

Field Description

`is_refresh_required`

(optional) Specifies whether to refresh the state for each resource before running the job (operation). Refreshing the state can affect performance. Consider setting to `false` if the configuration includes several resources. Used with the following operations: `PLAN`, `APPLY`, `DESTROY`.

`parallelism`

(optional) Limits the number of concurrent Terraform operations when[walking the graph](https://www.terraform.io/docs/internals/graph.html#walking-the-graph). Use this parameter to help debug Terraform issues or to accomplish certain special use cases. A higher value might cause resources to be throttled. Used with the following operations: `PLAN`, `APPLY`, `DESTROY`.

`detailed_log_level`

(optional) Enables detailed logs at the specified verbosity for running the job (operation).

Allowed values are: 'ERROR', 'WARN', 'INFO', 'DEBUG', 'TRACE'

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OPERATION_DETAILS_T Type

Job details that are specific to the operation type.

Syntax
```

```

Fields

Field Description

`operation`

(required) Terraform-specific operation to execute.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_JOB_OPERATION_DETAILS_T Type

Job details that are specific to apply operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_apply_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`execution_plan_strategy`

(required) Specifies the source of the execution plan to apply. Use `AUTO_APPROVED` to run the job without an execution plan.

Allowed values are: 'FROM_PLAN_JOB_ID', 'FROM_LATEST_PLAN_JOB', 'AUTO_APPROVED'

`execution_plan_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the plan job that contains the execution plan used for this job, or `null` if no execution plan was used.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OPERATION_DETAILS_SUMMARY_T Type

A summary of job details that is specific to the operation type.

Syntax
```

```

Fields

Field Description

`operation`

(required) Terraform-specific operation to execute.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_JOB_OPERATION_DETAILS_SUMMARY_T Type

Job details that are specific to apply operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_apply_job_operation_details_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_summary_t`type.

Fields

Field Description

`execution_plan_strategy`

(required) Specifies the source of the execution plan to apply. Use `AUTO_APPROVED` to run the job without an execution plan.

`execution_plan_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the plan job that contains the execution plan used for this job, or `null` if no execution plan was used.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_JOB_PLAN_RESOLUTION_T Type

Deprecated. Use the property `executionPlanStrategy` in `jobOperationDetails` instead.

Syntax
```

```

Fields

Field Description

`plan_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that specifies the most recently executed plan job.

`is_use_latest_job_id`

(optional) Specifies whether to use the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the most recently run plan job. `True` if using the latest job[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be a plan job that completed successfully.

`is_auto_approved`

(optional) Specifies whether to use the configuration directly, without reference to a Plan job. `True` if using the configuration directly. Note that it is not necessary for a Plan job to have run successfully.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_ROLLBACK_JOB_OPERATION_DETAILS_T Type

Job details that are specific to an apply rollback job. For more information about apply rollback jobs, see[Creating an Apply Rollback Job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm).

Syntax
```

```

`dbms_cloud_oci_resource_manager_apply_rollback_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`execution_plan_rollback_strategy`

(required) Specifies the source of the execution plan for rollback to apply. Use `AUTO_APPROVED` to run the job without an execution plan for rollback.

Allowed values are: 'FROM_PLAN_ROLLBACK_JOB_ID', 'FROM_LATEST_PLAN_ROLLBACK_JOB_ID', 'AUTO_APPROVED'

`execution_plan_rollback_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a plan rollback job, for use when specifying `\"FROM_PLAN_ROLLBACK_JOB_ID\"` as the `executionPlanRollbackStrategy`.

`target_rollback_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a successful apply job, for use when specifying `\"AUTO_APPROVED\"` as the `executionPlanRollbackStrategy`.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_ROLLBACK_JOB_OPERATION_DETAILS_SUMMARY_T Type

Job details that are specific to an apply rollback job. For more information about apply rollback jobs, see[Creating an Apply Rollback Job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm).

Syntax
```

```

`dbms_cloud_oci_resource_manager_apply_rollback_job_operation_details_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_summary_t`type.

Fields

Field Description

`execution_plan_rollback_strategy`

(required) Specifies the source of the execution plan for rollback to apply. Use `AUTO_APPROVED` to run the job without an execution plan for rollback.

`execution_plan_rollback_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a plan rollback job, for use when specifying `\"FROM_PLAN_ROLLBACK_JOB_ID\"` as the `executionPlanRollbackStrategy`.

`target_rollback_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a successful apply job, for use when specifying `\"AUTO_APPROVED\"` as the `executionPlanRollbackStrategy`.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_ASSOCIATED_RESOURCE_SUMMARY_T Type

Summary information for a resource associated with a stack or job.

Syntax
```

```

Fields

Field Description

`resource_id`

(optional) Unique identifier for the resource.

`resource_name`

(optional) Name of the resource.

`resource_type`

(optional) Resource type. For more information about resource types supported for the Oracle Cloud Infrastructure (OCI) provider, see[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).

`attributes`

(optional) Resource attribute values. Each value is represented as a key-value pair. Example: `{\"state\": \"AVAILABLE\"}`

`time_created`

(optional) The date and time when the stack was created. Format is defined by RFC3339. Example: `2022-07-25T21:10:29.600Z`

`l_region`

(optional) Resource region. For information about regions, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Example: `us-phoenix-1`

`resource_address`

(optional) Terraform resource address.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_ASSOCIATED_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_associated_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_ASSOCIATED_RESOURCES_COLLECTION_T Type

The list of associated resources for the indicated stack or job.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of resources associated with a stack or job.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIG_SOURCE_T Type

Information about the Terraform configuration.

Syntax
```

```

Fields

Field Description

`config_source_type`

(required) The type of configuration source to use for the Terraform configuration.

Allowed values are: 'BITBUCKET_CLOUD_CONFIG_SOURCE', 'BITBUCKET_SERVER_CONFIG_SOURCE', 'COMPARTMENT_CONFIG_SOURCE', 'DEVOPS_CONFIG_SOURCE', 'GIT_CONFIG_SOURCE', 'OBJECT_STORAGE_CONFIG_SOURCE', 'ZIP_UPLOAD'

`working_directory`

(optional) File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see[File Structure (Terraform Configurations for Resource Manager)](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#filestructure).

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_CONFIG_SOURCE_T Type

Metadata about the Bitbucket Cloud configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_cloud_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Bitbucket Cloud configuration source.

`repository_url`

(required) The URL of the Bitbucket Cloud repository for the configuration source.

`branch_name`

(optional) The name of the branch in the Bitbucket Cloud repository for the configuration source.

`workspace_id`

(required) The id of the workspace in Bitbucket Cloud for the configuration source

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIG_SOURCE_RECORD_T Type

Information about the Terraform configuration.

Syntax
```

```

Fields

Field Description

`config_source_record_type`

(required) The type of configuration source to use for the Terraform configuration.

Allowed values are: 'BITBUCKET_CLOUD_CONFIG_SOURCE', 'BITBUCKET_SERVER_CONFIG_SOURCE', 'COMPARTMENT_CONFIG_SOURCE', 'DEVOPS_CONFIG_SOURCE', 'GIT_CONFIG_SOURCE', 'OBJECT_STORAGE_CONFIG_SOURCE', 'ZIP_UPLOAD'

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_CONFIG_SOURCE_RECORD_T Type

Metadata about the Bitbucket Cloud configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_cloud_config_source_record_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_record_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Bitbucket Cloud configuration source.

`repository_url`

(required) The URL of the Bitbucket Cloud repository.

`branch_name`

(optional) The name of the branch within the Bitbucket Cloud repository.

`workspace_id`

(required) The id of the workspace in Bitbucket Cloud for the configuration source.

`commit_id`

(optional) The unique identifier (SHA-1 hash) of the individual change to the Bitbucket Cloud repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_SERVER_CONFIG_DETAILS_T Type

Details about a private endpoint associated with the configuration source provider.

Syntax
```

```

Fields

Field Description

`private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a private endpoint associated with the configuration source provider.

`certificate_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a certificate associated with the configuration source provider.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_T Type

The properties that define a configuration source provider. For more information, see[Managing Configuration Source Providers](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm).

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration source provider.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the configuration source provider is located.

`display_name`

(optional) Human-readable display name for the configuration source provider.

`description`

(optional) Description of the configuration source provider.

`time_created`

(optional) The date and time when the configuration source provider was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current lifecycle state of the configuration source provider. For more information about configuration source provider lifecycle states in Resource Manager, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__CSPStates).

Allowed values are: 'ACTIVE'

`config_source_provider_type`

(required) The type of configuration source provider. The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud. The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab. The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.

Allowed values are: 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD', 'BITBUCKET_SERVER_ACCESS_TOKEN', 'GITLAB_ACCESS_TOKEN', 'GITHUB_ACCESS_TOKEN'

`private_server_config_details`

(optional)

`username`

(optional) Username which is used to authorize the user.

`secret_id`

(optional) Secret ocid which is used to authorize the user.

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_T Type

The properties that define a configuration source provider of the type `BITBUCKET_CLOUD_USERNAME_APPPASSWORD`. This type corresponds to a configuration source provider in Bitbucket cloud that is authenticated with a username and app password.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_cloud_username_app_password_configuration_source_provider_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Bitbucket cloud service endpoint. Example: `https://bitbucket.org/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type

Summary information for a configuration source provider.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the configuration source provider.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the configuration source provider is located.

`display_name`

(optional) Human-readable display name for the configuration source provider.

`description`

(optional) General description of the configuration source provider.

`time_created`

(optional) The date and time when the configuration source provider was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) Current state of the specified configuration source provider. For more information about configuration source provider lifecycle states in Resource Manager, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__CSPStates). Allowable values: - ACTIVE

`config_source_provider_type`

(required) The type of configuration source provider. The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud. The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab. The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.

`private_server_config_details`

(optional)

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type

Summary information for a configuration source provider of the type `BITBUCKET_CLOUD_USERNAME_APPPASSWORD`. This type corresponds to a configuration source provider in Bitbucket cloud that is authenticated with a username and app password.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_cloud_username_app_password_configuration_source_provider_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_summary_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Bitbucket cloud service endpoint. Example: `https://bitbucket.org/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_T Type

The properties that define a configuration source provider of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a configuration source provider in Bitbucket server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_server_access_token_configuration_source_provider_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Bitbucket server service endpoint. Example: `https://bitbucket.org/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type

Summary information for a configuration source provider of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a configuration source provider in Bitbucket server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_server_access_token_configuration_source_provider_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_summary_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Bitbucket server service endpoint. Example: `https://bitbucket.org/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_CONFIG_SOURCE_T Type

Metadata about the Bitbucket Server configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_server_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Bitbucket Server configuration source.

`repository_url`

(required) The URL of the Bitbucket Server repository for the configuration source.

`branch_name`

(optional) The name of the branch in the Bitbucket Server repository for the configuration source.

`project_id`

(optional) Unique identifier for a Bitbucket Server project.

`repository_id`

(optional) Bitbucket Server repository identifier, usually identified as &lt;repository&gt;.git.

`clone_url`

(optional) The clone URL of Bitbucket Server configuration source.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_CONFIG_SOURCE_RECORD_T Type

Metadata about the Bitbucket Server configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_bitbucket_server_config_source_record_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_record_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Bitbucket Server configuration source.

`repository_url`

(required) The URL of the Bitbucket Server repository.

`branch_name`

(optional) The name of the branch within the Bitbucket Server repository.

`commit_id`

(optional) The unique identifier (SHA-1 hash) of the individual change to the Bitbucket Server repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CANCELLATION_DETAILS_T Type

Cancellation details for a job.

Syntax
```

```

Fields

Field Description

`is_forced`

(optional) Indicates whether a forced cancellation was requested for the job while it was running. A forced cancellation can result in an incorrect state file. For example, the state file might not reflect the exact state of the provisioned resources.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_CONFIGURATION_SOURCE_PROVIDER_COMPARTMENT_DETAILS_T Type

Compartment details for moving a configuration source provider.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the configuration source provider to.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

Compartment details for moving a private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the private endpoint to.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_STACK_COMPARTMENT_DETAILS_T Type

Compartment details for moving a stack.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the Stack should be moved.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_TEMPLATE_COMPARTMENT_DETAILS_T Type

Compartment details for moving a template.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the configuration source provider to.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_COMPARTMENT_CONFIG_SOURCE_T Type

Compartment to use for creating the stack. The new stack will include definitions for supported resource types in this compartment.

Syntax
```

```

`dbms_cloud_oci_resource_manager_compartment_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to use for creating the stack. The new stack will include definitions for supported resource types in this compartment.

`l_region`

(required) The region to use for creating the stack. The new stack will include definitions for supported resource types in this region.

`services_to_discover`

(optional) Filter for[services to use with Resource Discovery](https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services). For example, \"database\" limits resource discovery to resource types within the Database service. The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level otherwise). If not specified, then all services at the scope of the given compartment OCID are used.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_configuration_source_provider_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_COLLECTION_T Type

Collection of configuration source providers.

Syntax
```

```

Fields

Field Description

`items`

(optional) Collection of configuration source providers.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_JOB_OPERATION_DETAILS_T Type

Job details that are specific to the operation type.

Syntax
```

```

Fields

Field Description

`operation`

(required) Terraform-specific operation to execute.

`is_provider_upgrade_required`

(optional) Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see[Dependency Lock File (terraform.io)](https://www.terraform.io/language/files/dependency-lock).

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_APPLY_JOB_OPERATION_DETAILS_T Type

Job details that are specific to apply operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_apply_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`execution_plan_strategy`

(optional) Specifies the source of the execution plan to apply. Use `AUTO_APPROVED` to run the job without an execution plan.

`execution_plan_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a plan job, for use when specifying `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_APPLY_ROLLBACK_JOB_OPERATION_DETAILS_T Type

Job details that are specific to an apply rollback job. For more information about apply rollback jobs, see[Creating an Apply Rollback Job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm).

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_apply_rollback_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`execution_plan_rollback_strategy`

(required) Specifies the source of the execution plan for rollback to apply. Use `AUTO_APPROVED` to run the job without an execution plan for rollback job.

`execution_plan_rollback_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a plan rollback job, for use when specifying `\"FROM_PLAN_ROLLBACK_JOB_ID\"` as the `executionPlanRollbackStrategy`.

`target_rollback_job_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a successful apply job, for use when specifying `\"AUTO_APPROVED\"` as the `executionPlanRollbackStrategy`.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_CONFIG_SOURCE_DETAILS_T Type

Creation details for a configuration source used with the stack.

Syntax
```

```

Fields

Field Description

`config_source_type`

(required) Specifies the `configSourceType` for uploading the Terraform configuration.

`working_directory`

(optional) File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see[File Structure (Terraform Configurations for Resource Manager)](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#filestructure).

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_CLOUD_CONFIG_SOURCE_DETAILS_T Type

Creation details for a Bitbucket Cloud configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_bitbucket_cloud_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Bitbucket Cloud configuration source.

`repository_url`

(required) The URL of the Bitbucket Cloud repository for the configuration source.

`branch_name`

(optional) The name of the branch in the Bitbucket Cloud repository for the configuration source.

`workspace_id`

(required) The id of the workspace in Bitbucket Cloud for the configuration source

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Creation details for a configuration source provider.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the configuration source provider.

`display_name`

(optional) Human-readable name of the configuration source provider. Avoid entering confidential information.

`description`

(optional) Description of the configuration source provider. Avoid entering confidential information.

`config_source_provider_type`

(required) The type of configuration source provider. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab. The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub. The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud. The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server.

`private_server_config_details`

(optional)

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Creation details for a configuration source provider of the type `BITBUCKET_CLOUD_USERNAME_appPASSWORD`. This type corresponds to a configuration source provider in Bitbucket that is authenticated with a username and app password.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_bitbucket_cloud_username_app_password_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_configuration_source_provider_details_t`type.

Fields

Field Description

`api_endpoint`

(required) The Bitbucket cloud service endpoint. Example: `https://bitbucket.org/`

`username`

(required) The username for the user of the Bitbucket cloud repository.

`secret_id`

(required) The secret ocid which is used to authorize the user.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

The details for creating a configuration source provider of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a configuration source provider in Bitbucket server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_bitbucket_server_access_token_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_configuration_source_provider_details_t`type.

Fields

Field Description

`secret_id`

(required) The secret ocid which is used to authorize the user.

`api_endpoint`

(required) The Bitbucket Server service endpoint Example: `https://bitbucket.org/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_SERVER_CONFIG_SOURCE_DETAILS_T Type

Creation details for a Bitbucket Server configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_bitbucket_server_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Bitbucket Server configuration source.

`repository_url`

(required) The URL of the Bitbucket Server repository.

`branch_name`

(optional) The name of the branch within the Bitbucket Server repository.

`project_id`

(optional) Unique identifier for a Bitbucket Server project.

`repository_id`

(optional) Bitbucket Server repository identifier, usually identified as &lt;repository&gt;.git.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_COMPARTMENT_CONFIG_SOURCE_DETAILS_T Type

Creation details for a configuration source based on the specified compartment.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_compartment_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to use for creating the stack. The new stack will include definitions for supported resource types in scope of the specified compartment OCID (tenancy level for root compartment, compartment level otherwise).

`l_region`

(required) The region to use for creating the stack. The new stack will include definitions for supported resource types in this region.

`services_to_discover`

(optional) Filter for[services to use with Resource Discovery](https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services). For example, \"database\" limits resource discovery to resource types within the Database service. The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level otherwise). If not specified, then all services at the scope of the given compartment OCID are used.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_DESTROY_JOB_OPERATION_DETAILS_T Type

Job details that are specific to destroy operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_destroy_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`execution_plan_strategy`

(required) Specifies the source of the execution plan to apply. Currently, only `AUTO_APPROVED` is allowed, which indicates that the job will be run without an execution plan.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_DEV_OPS_CONFIG_SOURCE_DETAILS_T Type

Creation details for a[DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm)configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_dev_ops_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`PROJECT`Type.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`REPOSITORY`Type.

`branch_name`

(optional) The name of the branch that contains the Terraform configuration.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_GIT_CONFIG_SOURCE_DETAILS_T Type

Creation details for configuration Git information.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_git_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Git configuration source.

`repository_url`

(optional) The URL of the Git repository.

`branch_name`

(optional) The name of the branch within the Git repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Creation details for a configuration source provider of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_github_access_token_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_configuration_source_provider_details_t`type.

Fields

Field Description

`api_endpoint`

(required) The GitHub service endpoint. Example: `https://github.com/`

`access_token`

(required) The personal access token to be configured on the GitHub repository. Avoid entering confidential information.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Creation details for a configuration source provider of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_gitlab_access_token_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_configuration_source_provider_details_t`type.

Fields

Field Description

`api_endpoint`

(required) The Git service endpoint. Example: `https://gitlab.com`

`access_token`

(required) The personal access token to be configured on the GitLab repository. Avoid entering confidential information.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_IMPORT_TF_STATE_JOB_OPERATION_DETAILS_T Type

Job details that are specific to import Terraform state operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_import_tf_state_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_job_operation_details_t`type.

Fields

Field Description

`tf_state_base64_encoded`

(required) Base64-encoded state file

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_JOB_DETAILS_T Type

Creation details for a job for running inside the specified stack.

Syntax
```

```

Fields

Field Description

`stack_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack that is associated with the current job.

`display_name`

(optional) Description of the job.

`operation`

(optional) Terraform-specific operation to execute.

`job_operation_details`

(optional)

`apply_job_plan_resolution`

(optional)

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_OBJECT_STORAGE_CONFIG_SOURCE_DETAILS_T Type

Creation details for an Object Storage bucket that contains Terraform configuration files.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_object_storage_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`l_region`

(required) The name of the bucket's region. Example: `us-phoenix-1`

`namespace`

(required) The Object Storage namespace that contains the bucket.

`bucket_name`

(required) The name of the bucket that contains the Terraform configuration files.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_PLAN_JOB_OPERATION_DETAILS_T Type

Job details that are specific to plan operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_plan_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_PLAN_ROLLBACK_JOB_OPERATION_DETAILS_T Type

Job details that are specific to a plan rollback job. For more information about plan rollback jobs, see[Creating a Plan Rollback Job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm).

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_plan_rollback_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`target_rollback_job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a successful apply job to use for the plan rollback job.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_PRIVATE_ENDPOINT_DETAILS_T Type

Creation details for a private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this private endpoint.

`display_name`

(required) The private endpoint display name. Avoid entering confidential information.

`description`

(optional) Description of the private endpoint. Avoid entering confidential information.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN for the private endpoint.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet within the VCN for the private endpoint.

`dns_zones`

(optional) DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.

`nsg_id_list`

(optional) The[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of[network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for the private endpoint. Order does not matter.

`is_used_with_configuration_source_provider`

(optional) When `true`, allows the private endpoint to be used with a configuration source provider.

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CUSTOM_TERRAFORM_PROVIDER_T Type

Location information about custom Terraform providers for a stack. For more information, see[Custom Providers](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#features__custom-providers). Note: Older stacks must be explicitly updated to use Terraform Registry (`isThirdPartyProviderExperienceEnabled=true`). See`UPDATE_STACK`Function. For more information, see[Using Terraform Registry with Older Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm).

Syntax
```

```

Fields

Field Description

`l_region`

(required) The name of the region that contains the bucket you want. For information about regions, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Example: `us-phoenix-1`

`namespace`

(required) The Object Storage namespace that contains the bucket you want. For information about Object Storage namespaces, see[Understanding Object Storage Namespaces](https://docs.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm).

`bucket_name`

(required) The name of the bucket that contains the binary files for the custom Terraform providers. For information about buckets, see[Managing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm).

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_STACK_DETAILS_T Type

Creation details for a stack.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the compartment in which the stack resides.

`display_name`

(optional) The stack's display name.

`description`

(optional) Description of the stack.

`config_source`

(required)

`custom_terraform_provider`

(optional)

`variables`

(optional) Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`

`terraform_version`

(optional) The version of Terraform to use with the stack. Example: `0.12.x`

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_STACK_TEMPLATE_CONFIG_SOURCE_DETAILS_T Type

Creation details for a template to use as the source of the Terraform configuration.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_stack_template_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`template_id`

(required)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_TEMPLATE_CONFIG_SOURCE_DETAILS_T Type

Creation details for a configuration source used for a template.

Syntax
```

```

Fields

Field Description

`template_config_source_type`

(required) Specifies the `configSourceType` for uploading the Terraform configuration.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_TEMPLATE_DETAILS_T Type

Creation details for a template.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this template.

`display_name`

(required) The template's display name. Avoid entering confidential information.

`description`

(required) Description of the template. Avoid entering confidential information.

`long_description`

(optional) Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.

`logo_file_base64_encoded`

(optional) Base64-encoded logo to use as the template icon. Template icon file requirements: PNG format, 50 KB maximum, 110 x 110 pixels.

`template_config_source`

(required)

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_TEMPLATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type

Creation details for a zip file used for a template.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_template_zip_upload_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_template_config_source_details_t`type.

Fields

Field Description

`zip_file_base64_encoded`

(required)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type

Creation details for a Terraform configuration zip file.

Syntax
```

```

`dbms_cloud_oci_resource_manager_create_zip_upload_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_create_config_source_details_t`type.

Fields

Field Description

`zip_file_base64_encoded`

(required)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_DESTROY_JOB_OPERATION_DETAILS_T Type

Job details that are specific to destroy operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_destroy_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`execution_plan_strategy`

(required) Specifies the source of the execution plan to apply. Currently, only `AUTO_APPROVED` is allowed, which indicates that the job will be run without an execution plan.

Allowed values are: 'AUTO_APPROVED'

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_DESTROY_JOB_OPERATION_DETAILS_SUMMARY_T Type

Job details that are specific to destroy operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_destroy_job_operation_details_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_summary_t`type.

Fields

Field Description

`execution_plan_strategy`

(required) Specifies the source of the execution plan to apply. Currently, only `AUTO_APPROVED` is allowed, which indicates that the job will be run without an execution plan.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_DETECT_STACK_DRIFT_DETAILS_T Type

Details for detecting drift in a stack.

Syntax
```

```

Fields

Field Description

`resource_addresses`

(optional) The list of resources in the specified stack to detect drift for. Each resource is identified by a resource address, which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index. For example, the resource address for the fourth Compute instance with the name \"test_instance\" is oci_core_instance.test_instance[3]. For more details and examples of resource addresses, see the Terraform documentation at [Resource spec](https://www.terraform.io/docs/internals/resource-addressing.html#examples).

`is_provider_upgrade_required`

(optional) Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see[Dependency Lock File (terraform.io)](https://www.terraform.io/language/files/dependency-lock).

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_DEV_OPS_CONFIG_SOURCE_T Type

Metadata about the[DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm)configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_dev_ops_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`PROJECT`Type.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`REPOSITORY`Type.

`branch_name`

(optional) The name of the branch that contains the Terraform configuration.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_DEV_OPS_CONFIG_SOURCE_RECORD_T Type

Metadata about the[DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm)configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_dev_ops_config_source_record_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_record_t`type.

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`PROJECT`Type.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`REPOSITORY`Type.

`branch_name`

(required) The name of the branch that contains the Terraform configuration.

`commit_id`

(optional) The unique identifier (SHA-1 hash) of the individual change to the DevOps repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_ERROR_T Type

Error that occurs during the execution of a job.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. For more information, see[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_FAILURE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) Job failure reason.

Allowed values are: 'INTERNAL_SERVICE_ERROR', 'TERRAFORM_EXECUTION_ERROR', 'TERRAFORM_CONFIG_UNZIP_FAILED', 'INVALID_WORKING_DIRECTORY', 'JOB_TIMEOUT', 'TERRAFORM_CONFIG_VIRUS_FOUND', 'TERRAFORM_GIT_CLONE_FAILURE', 'TERRAFORM_GIT_CHECKOUT_FAILURE', 'TERRAFORM_OBJECT_STORAGE_CONFIG_SOURCE_EMPTY_BUCKET', 'TERRAFORM_OBJECT_STORAGE_CONFIG_SOURCE_NO_TF_FILE_PRESENT', 'TERRAFORM_OBJECT_STORAGE_CONFIG_SOURCE_UNSUPPORTED_OBJECT_SIZE', 'CUSTOM_TERRAFORM_PROVIDER_BUCKET_NOT_FOUND', 'CUSTOM_TERRAFORM_PROVIDER_UNSUPPORTED_OBJECT_SIZE'

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_GIT_CONFIG_SOURCE_T Type

Metadata about the Git configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_git_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Git configuration source.

`repository_url`

(optional) The URL of the Git repository for the configuration source.

`branch_name`

(optional) The name of the branch in the Git repository for the configuration source.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_GIT_CONFIG_SOURCE_RECORD_T Type

Metadata about the Git configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_git_config_source_record_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_record_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Git configuration source.

`repository_url`

(optional) The URL of the Git repository.

`branch_name`

(optional) The name of the branch within the Git repository.

`commit_id`

(optional) The unique identifier (SHA-1 hash) of the individual change to the Git repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_T Type

The properties that define a configuration source provider of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_github_access_token_configuration_source_provider_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_t`type.

Fields

Field Description

`api_endpoint`

(optional) The GitHub service endpoint. Example: `https://github.com/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type

Summary information for a configuration source provider of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_github_access_token_configuration_source_provider_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_summary_t`type.

Fields

Field Description

`api_endpoint`

(optional) The GitHub service endpoint. Example: `https://github.com/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_T Type

The properties that define a configuration source provider of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_gitlab_access_token_configuration_source_provider_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Git service endpoint. Example: `https://gitlab.com`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type

Summary information for a configuration source provider of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_gitlab_access_token_configuration_source_provider_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_configuration_source_provider_summary_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Git service endpoint. Example: `https://gitlab.com`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_IMPORT_TF_STATE_JOB_OPERATION_DETAILS_T Type

Job details that are specific to import Terraform state operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_import_tf_state_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_t`type.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_IMPORT_TF_STATE_JOB_OPERATION_DETAILS_SUMMARY_T Type

Job details that are specific to import Terraform state operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_import_tf_state_job_operation_details_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_summary_t`type.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_T Type

The properties of a job. A job performs the actions that are defined in your Terraform configuration. For instructions on managing jobs, see[Managing Jobs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/jobs.htm). For more information about jobs, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__jobdefinition).

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`stack_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack that is associated with the job.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which the job's associated stack resides.

`display_name`

(optional) The job's display name.

`operation`

(optional) The type of job executing.

Allowed values are: 'PLAN', 'APPLY', 'DESTROY', 'IMPORT_TF_STATE', 'PLAN_ROLLBACK', 'APPLY_ROLLBACK'

`is_third_party_provider_experience_enabled`

(optional) When `true`, the stack sources third-party Terraform providers from[Terraform Registry](https://registry.terraform.io/browse/providers)and allows`CUSTOM_TERRAFORM_PROVIDER`Function. For more information about stack sourcing of third-party Terraform providers, see[Third-party Provider Configuration](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers).

`is_provider_upgrade_required`

(optional) Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see[Dependency Lock File (terraform.io)](https://www.terraform.io/language/files/dependency-lock).

`job_operation_details`

(optional)

`apply_job_plan_resolution`

(optional)

`resolved_plan_job_id`

(optional) Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead. The plan job[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that was used (if this was an apply job and was not auto-approved).

`time_created`

(optional) The date and time when the job was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`time_finished`

(optional) The date and time when the job stopped running, irrespective of whether the job ran successfully. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) Current state of the specified job. For more information about job lifecycle states in Resource Manager, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__JobStates).

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`failure_details`

(optional)

`cancellation_details`

(optional)

`working_directory`

(optional) File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see[File Structure (Terraform Configurations for Resource Manager)](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#filestructure).

`variables`

(optional) Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`

`config_source`

(optional)

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OUTPUT_SUMMARY_T Type

Terraform output associated with a job.

Syntax
```

```

Fields

Field Description

`output_name`

(optional) Name of the output.

`output_type`

(optional) Output resource type.

`output_value`

(optional) Value of the Terraform output.

`is_sensitive`

(optional) When `true`, output is sensitive.

`description`

(optional) Description of the output.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OUTPUT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_job_output_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OUTPUTS_COLLECTION_T Type

The list of outputs associated with a job.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of output summaries.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_SUMMARY_T Type

Summary information for a job.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`stack_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack that is associated with the specified job.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the stack of the associated job resides.

`display_name`

(optional) The job's display name.

`operation`

(optional) The type of job executing

`job_operation_details`

(optional)

`apply_job_plan_resolution`

(optional)

`resolved_plan_job_id`

(optional) Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead. The plan job[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that was used (if this was an apply job and was not auto-approved).

`time_created`

(optional) The date and time the job was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`time_finished`

(optional) The date and time the job succeeded or failed. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) Current state of the specified job. For more information about job lifecycle states in Resource Manager, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__JobStates). Allowable values: - ACCEPTED - IN_PROGRESS - FAILED - SUCCEEDED - CANCELING - CANCELED

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_LOG_ENTRY_T Type

Log entry for an operation resulting from a job's execution.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) Specifies the log type for the log entry.

Allowed values are: 'TERRAFORM_CONSOLE'

`l_level`

(optional) Specifies the severity level of the log entry.

Allowed values are: 'TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'

`l_timestamp`

(optional) The date and time of the log entry. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`message`

(optional) The log entry value.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_OBJECT_STORAGE_CONFIG_SOURCE_T Type

Metadata about the Object Storage configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_object_storage_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

Fields

Field Description

`l_region`

(required) The name of the bucket's region. Example: `us-phoenix-1`

`namespace`

(required) The Object Storage namespace that contains the bucket.

`bucket_name`

(required) The name of the bucket that contains the Terraform configuration files. Maximum file size (applies to each file in the bucket): 100 MB. (In a bucket, a file is an object.)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_OBJECT_STORAGE_CONFIG_SOURCE_RECORD_T Type

Metadata about the Object Storage configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_object_storage_config_source_record_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_record_t`type.

Fields

Field Description

`l_region`

(required) The name of the bucket's region. Example: `us-phoenix-1`

`namespace`

(required) The Object Storage namespace that contains the bucket.

`bucket_name`

(required) The name of the bucket that contains the Terraform configuration files.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_JOB_OPERATION_DETAILS_T Type

Job details that are specific to plan operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_plan_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_JOB_OPERATION_DETAILS_SUMMARY_T Type

Job details that are specific to plan operations.

Syntax
```

```

`dbms_cloud_oci_resource_manager_plan_job_operation_details_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_summary_t`type.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_ROLLBACK_JOB_OPERATION_DETAILS_T Type

Job details that are specific to a plan rollback job. For more information about plan rollback jobs, see[Creating a Plan Rollback Job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm).

Syntax
```

```

`dbms_cloud_oci_resource_manager_plan_rollback_job_operation_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_t`type.

Fields

Field Description

`terraform_advanced_options`

(optional)

`target_rollback_job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a successful apply job to use for the plan rollback job.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_ROLLBACK_JOB_OPERATION_DETAILS_SUMMARY_T Type

Job details that are specific to a plan rollback job. For more information about plan rollback jobs, see[Creating a Plan Rollback Job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm).

Syntax
```

```

`dbms_cloud_oci_resource_manager_plan_rollback_job_operation_details_summary_t`is a subtype of the`dbms_cloud_oci_resource_manager_job_operation_details_summary_t`type.

Fields

Field Description

`target_rollback_job_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a successful apply job to use for the plan rollback job.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_T Type

A private endpoint allowing Resource Manager to access nonpublic cloud resources. For more information about private endpoints, see[Private Endpoint Management](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this private endpoint.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description of the private endpoint. Avoid entering confidential information.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN for the private endpoint.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet within the VCN for the private endpoint.

`source_ips`

(optional) The source IP addresses that Resource Manager uses to connect to your network. Automatically assigned by Resource Manager.

`nsg_id_list`

(optional) The[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of[network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for the private endpoint. Order does not matter.

`is_used_with_configuration_source_provider`

(optional) When `true`, allows the private endpoint to be used with a configuration source provider.

`dns_zones`

(optional) DNS zones to use for accessing private Git servers. For private Git server instructions, see[Private Git Server](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git). Specify DNS fully qualified domain names (FQDNs); DNS Proxy forwards related DNS FQDN queries to the consumer DNS resolver. For DNS FQDNs not specified, queries go to service provider VCN resolver. Example: `abc.oraclevcn.com`

`time_created`

(optional) The date and time at which the private endpoint was created. Format is defined by RFC3339. Example: `2020-11-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current lifecycle state of the private endpoint.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_SUMMARY_T Type

The summary metadata associated with the private endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this private endpoint.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) Description of the private endpoint. Avoid entering confidential information.

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN for the private endpoint.

`is_used_with_configuration_source_provider`

(optional) When `true`, allows the private endpoint to be used with a configuration source provider.

`dns_zones`

(optional) DNS zones to use for accessing private Git servers. For private Git server instructions, see[Private Git Server](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git). DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.

`time_created`

(optional) The date and time when the private endpoint was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current lifecycle state of the private endpoint. Allowable values: - ACTIVE - CREATING - DELETING - DELETED - FAILED

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_private_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_COLLECTION_T Type

A list of private endpoints that match filter criteria, if any. Results contain `PrivateEndpointSummary` objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of private endpoints.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_REACHABLE_IP_T Type

The reachable, or alternative, IP address for a nonpublic IP address that is associated with the private endpoint. Resource Manager uses this IP address to connect to nonpublic resources through the associated private endpoint.

Syntax
```

```

Fields

Field Description

`ip_address`

(required) Reachable IP address associated with the private endpoint.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_RESOURCE_DISCOVERY_SERVICE_SUMMARY_T Type

A service supported for use with[Resource Discovery](https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).

Syntax
```

```

Fields

Field Description

`name`

(optional) A supported service. Example: `core` For reference on service names, see the[Terraform provider documentation](https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).

`discovery_scope`

(optional) The scope of the service as used with Resource Discovery. This property determines the type of compartment OCID required: root compartment (`TENANCY`) or not (`COMPARTMENT`). For example, `identity` is at the root compartment scope while `database` is at the compartment scope.

Allowed values are: 'TENANCY', 'COMPARTMENT'

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_RESOURCE_DISCOVERY_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_resource_discovery_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_RESOURCE_DISCOVERY_SERVICE_COLLECTION_T Type

The list of[services supported for use with Resource Discovery](https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of supported services for Resource Discovery.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_T Type

The properties that define a stack. A stack is the collection of Oracle Cloud Infrastructure resources corresponding to a given Terraform configuration. For instructions on managing stacks, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm). For more information about stacks, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__stackdefinition).

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the stack.

`compartment_id`

(optional) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the compartment where the stack is located.

`display_name`

(optional) Human-readable name of the stack.

`description`

(optional) Description of the stack.

`time_created`

(optional) The date and time at which the stack was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current lifecycle state of the stack. For more information about stack lifecycle states in Resource Manager, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates).

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`config_source`

(optional)

`custom_terraform_provider`

(optional)

`is_third_party_provider_experience_enabled`

(optional) When `true`, the stack sources third-party Terraform providers from[Terraform Registry](https://registry.terraform.io/browse/providers)and allows`CUSTOM_TERRAFORM_PROVIDER`Function. For more information about stack sourcing of third-party Terraform providers, see[Third-party Provider Configuration](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers).

`variables`

(optional) Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`

`terraform_version`

(optional) The version of Terraform specified for the stack. Example: `0.12.x`

`stack_drift_status`

(optional) Drift status of the stack. Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.

Allowed values are: 'NOT_CHECKED', 'IN_SYNC', 'DRIFTED'

`time_drift_last_checked`

(optional) The date and time when the drift detection was last executed. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_RESOURCE_DRIFT_SUMMARY_T Type

Drift status details for the indicated resource and stack. Includes actual and expected (defined) properties.

Syntax
```

```

Fields

Field Description

`stack_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stack.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the stack is located.

`resource_name`

(optional) The name of the resource as defined in the stack.

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource provisioned by Terraform.

`resource_type`

(optional) The provider resource type. Must be supported by the[Oracle Cloud Infrastructure provider](https://www.terraform.io/docs/providers/oci/index.html). Example: `oci_core_instance`

`resource_drift_status`

(optional) The drift status of the resource. A drift status value indicates whether or not the actual state of the resource differs from the expected (defined) state for that resource.

Allowed values are: 'NOT_CHECKED', 'IN_SYNC', 'MODIFIED', 'DELETED'

`actual_properties`

(optional) Actual values of properties that the stack defines for the indicated resource. Each property and value is provided as a key-value pair. The following example shows actual values for the resource's display name and server type: `{\"display_name\": \"tf-default-dhcp-options-new\", \"options.0.server_type\": \"VcnLocalPlusInternet\"}`

`expected_properties`

(optional) Expected values of properties that the stack defines for the indicated resource. Each property and value is provided as a key-value pair. The following example shows expected (defined) values for the resource's display name and server type: `{\"display_name\": \"tf-default-dhcp-options\", \"options.0.server_type\": \"VcnLocalPlusInternet\"}`

`time_drift_checked`

(optional) The date and time when the drift detection was executed. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_RESOURCE_DRIFT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_stack_resource_drift_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_RESOURCE_DRIFT_COLLECTION_T Type

Drift status details for resources in the stack.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of drift status details for all resources defined in the stack.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_SUMMARY_T Type

Summary information for a stack.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier of the specified stack.

`compartment_id`

(optional) Unique identifier of the compartment in which the stack resides.

`display_name`

(optional) Human-readable display name for the stack.

`description`

(optional) General description of the stack.

`time_created`

(optional) The date and time when the stack was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current lifecycle state of the stack. For more information about stack lifecycle states in Resource Manager, see[Key Concepts](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates). Allowable values: - CREATING - ACTIVE - DELETING - DELETED - FAILED

`terraform_version`

(optional) The version of Terraform specified for the stack. Example: `0.12.x`

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CONFIG_SOURCE_T Type

Information about the Template.

Syntax
```

```

Fields

Field Description

`template_config_source_type`

(required) The type of configuration source to use for the template configuration.

Allowed values are: 'ZIP_UPLOAD'

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_T Type

The properties that define a template. A template is a pre-built Terraform configuration that provisions a set of resources used in a common scenario.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the template.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this template.

`category_id`

(optional) Unique identifier for the category where the template is located. Possible values are `0` (Quick Starts), `1` (Service), `2` (Architecture), and `3` (Private).

`display_name`

(optional) Human-readable name of the template.

`description`

(optional) Brief description of the template.

`long_description`

(optional) Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.

`is_free_tier`

(optional) whether the template will work for free tier tenancy.

`time_created`

(optional) The date and time at which the template was created. Format is defined by RFC3339. Example: `2020-11-25T21:10:29.600Z`

`template_config_source`

(optional)

`lifecycle_state`

(optional) The current lifecycle state of the template.

Allowed values are: 'ACTIVE'

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CATEGORY_SUMMARY_T Type

Summary information for the template category.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier for the template category. Possible values are `0` (Quickstarts), `1` (Service), `2` (Architecture), and `3` (Private). Template category labels are displayed in the Console page listing templates. Quickstarts, Service, and Architecture templates (categories 0, 1, and 2) are available in all compartments. Each private template (category 3) is available in the compartment where it was created.

`display_name`

(optional) The name of the template category.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CATEGORY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_template_category_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CATEGORY_SUMMARY_COLLECTION_T Type

Results of a `ListTemplateCategories` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of template categories.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_SUMMARY_T Type

Summary information for a template.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier of the specified template.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this template.

`display_name`

(optional) Human-readable display name for the template.

`description`

(optional) Brief description of the template.

`is_free_tier`

(optional) whether the template will work for free tier tenancy.

`time_created`

(optional) The date and time at which the template was created. Format is defined by RFC3339. Example: `2020-11-25T21:10:29.600Z`

`lifecycle_state`

(optional) The current lifecycle state of the template. Allowable values: - ACTIVE

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_template_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_SUMMARY_COLLECTION_T Type

Results of a `ListTemplates` operation.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of template summaries.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_ZIP_UPLOAD_CONFIG_SOURCE_T Type

Metadata about the zip file containing the Terraform configuration for the template.

Syntax
```

```

`dbms_cloud_oci_resource_manager_template_zip_upload_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_template_config_source_t`type.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_VERSION_SUMMARY_T Type

A Terraform version supported for use with stacks.

Syntax
```

```

Fields

Field Description

`name`

(optional) A supported Terraform version. Example: `0.12.x`

`is_default`

(optional) Indicates whether this Terraform version is used by default in`CREATE_STACK`Function.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_terraform_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_VERSION_COLLECTION_T Type

The list of Terraform versions supported for use with stacks.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of supported Terraform versions.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_CONFIG_SOURCE_DETAILS_T Type

Update details for a configuration source.

Syntax
```

```

Fields

Field Description

`config_source_type`

(required) Specifies the `configSourceType` for uploading the Terraform configuration.

`working_directory`

(optional) File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see[File Structure (Terraform Configurations for Resource Manager)](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#filestructure).

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_CLOUD_CONFIG_SOURCE_DETAILS_T Type

Update details for a Bitbucket Cloud configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_bitbucket_cloud_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_config_source_details_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Bitbucket Cloud configuration source.

`repository_url`

(optional) The URL of the Bitbucket Cloud repository for the configuration source.

`branch_name`

(optional) The name of the branch in the Bitbucket Cloud repository for the configuration source.

`workspace_id`

(optional) The id of the workspace in Bitbucket Cloud for the configuration source

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Update details for a configuration source provider.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Human-readable name of the configuration source provider. Avoid entering confidential information.

`description`

(optional) Description of the configuration source provider. Avoid entering confidential information.

`config_source_provider_type`

(optional) The type of configuration source provider. The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud. The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab. The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.

`private_server_config_details`

(optional)

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Update details for a configuration source provider of the type `BITBUCKET_CLOUD_USERNAME_APPPASSWORD`. This type corresponds to a configuration source provider in Bitbucket that is authenticated with a username and app password.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_bitbucket_cloud_username_app_password_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_configuration_source_provider_details_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Bitbucket service endpoint. Example: `https://bitbucket.org/`

`username`

(optional) The username for the user of the Bitbucket cloud repository.

`secret_id`

(optional) The secret ocid which is used to authorize the user.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

The details for creating a configuration source provider of the type `BITBUCKET_SERVER_ACCESS_TOKEN`. This type corresponds to a configuration source provider in Bitbucket server that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_bitbucket_server_access_token_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_configuration_source_provider_details_t`type.

Fields

Field Description

`secret_id`

(optional) The secret ocid which is used to authorize the user.

`api_endpoint`

(optional) The Bitbucket server service endpoint Example: `https://bitbucket.org/`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_SERVER_CONFIG_SOURCE_DETAILS_T Type

Update details for a Bitbucket Server configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_bitbucket_server_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_config_source_details_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Bitbucket Server configuration source.

`repository_url`

(optional) The URL of the Bitbucket Server repository.

`branch_name`

(optional) The name of the branch within the Bitbucket Server repository.

`project_id`

(optional) Unique identifier for a Bitbucket Server project.

`repository_id`

(optional) Bitbucket Server repository identifier, usually identified as &lt;repository&gt;.git.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_DEV_OPS_CONFIG_SOURCE_DETAILS_T Type

Update details for a[DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm)configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_dev_ops_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_config_source_details_t`type.

Fields

Field Description

`project_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`PROJECT`Type.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`REPOSITORY`Type.

`branch_name`

(optional) The name of the branch that contains the Terraform configuration.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_GIT_CONFIG_SOURCE_DETAILS_T Type

Update details for a Git configuration source.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_git_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_config_source_details_t`type.

Fields

Field Description

`configuration_source_provider_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the Git configuration source.

`repository_url`

(optional) The URL of the Git repository.

`branch_name`

(optional) The name of the branch within the Git repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Update details for a configuration source provider of the type `GITHUB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitHub that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_github_access_token_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_configuration_source_provider_details_t`type.

Fields

Field Description

`api_endpoint`

(optional) The GitHub service endpoint. Example: `https://github.com/`

`access_token`

(optional) The personal access token to be configured on the GitHub repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type

Update details for configuration source provider of the type `GITLAB_ACCESS_TOKEN`. This type corresponds to a configuration source provider in GitLab that is authenticated with a personal access token.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_gitlab_access_token_configuration_source_provider_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_configuration_source_provider_details_t`type.

Fields

Field Description

`api_endpoint`

(optional) The Git service endpoint. Example: `https://gitlab.com`

`access_token`

(optional) The personal access token to be configured on the GitLab repository.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_JOB_DETAILS_T Type

Update details for a job.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The new display name to set.

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_OBJECT_STORAGE_CONFIG_SOURCE_DETAILS_T Type

Update details for an Object Storage bucket that contains Terraform configuration files.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_object_storage_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_config_source_details_t`type.

Fields

Field Description

`l_region`

(optional) The name of the bucket's region. Example: `us-phoenix-1`

`namespace`

(optional) The Object Storage namespace that contains the bucket.

`bucket_name`

(optional) The name of the bucket that contains the Terraform configuration files.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_PRIVATE_ENDPOINT_DETAILS_T Type

Update details for a private endpoint.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The private endpoint display name. Avoid entering confidential information.

`description`

(optional) Description of the private endpoint. Avoid entering confidential information.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN for the private endpoint.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet within the VCN for the private endpoint.

`dns_zones`

(optional) DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.

`nsg_id_list`

(optional) The[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of[network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for the private endpoint. Order does not matter.

`is_used_with_configuration_source_provider`

(optional) When `true`, allows the private endpoint to be used with a configuration source provider.

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_STACK_DETAILS_T Type

Update details for a stack.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the stack.

`description`

(optional) Description of the stack.

`config_source`

(optional)

`custom_terraform_provider`

(optional)

`is_third_party_provider_experience_enabled`

(optional) When `true`, changes the stack's sourcing of third-party Terraform providers to[Terraform Registry](https://registry.terraform.io/browse/providers)and allows`CUSTOM_TERRAFORM_PROVIDER`Function. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see[Third-party Provider Configuration](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers).

`variables`

(optional) Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`

`terraform_version`

(optional) The version of Terraform to use with the stack. Example: `0.12.x`

`freeform_tags`

(optional) Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_TEMPLATE_CONFIG_SOURCE_DETAILS_T Type

Update details for a configuration source for a template.

Syntax
```

```

Fields

Field Description

`template_config_source_type`

(required) Specifies the `configSourceType` for uploading the Terraform configuration.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_TEMPLATE_DETAILS_T Type

Update details for a template.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The template's display name. Avoid entering confidential information.

`description`

(optional) Description of the template. Avoid entering confidential information.

`long_description`

(optional) Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.

`logo_file_base64_encoded`

(optional) Base64-encoded logo for the template.

`template_config_source`

(optional)

`freeform_tags`

(optional) Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_TEMPLATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type

Update details for a configuration zip file.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_template_zip_upload_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_template_config_source_details_t`type.

Fields

Field Description

`zip_file_base64_encoded`

(optional)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type

Update details for a Terraform configuration zip file.

Syntax
```

```

`dbms_cloud_oci_resource_manager_update_zip_upload_config_source_details_t`is a subtype of the`dbms_cloud_oci_resource_manager_update_config_source_details_t`type.

Fields

Field Description

`zip_file_base64_encoded`

(optional)

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS'

`entity_type`

(required) The resource type the work request affects.

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier for the resource.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_resource_manager_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_T Type

The status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CHANGE_STACK_COMPARTMENT', 'CREATE_STACK_FROM_COMPARTMENT', 'DRIFT_DETECTION', 'CREATE_PRIVATE_ENDPOINT', 'UPDATE_PRIVATE_ENDPOINT', 'DELETE_PRIVATE_ENDPOINT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)identifying this work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The amount of work done relative to the total amount of work.

`time_accepted`

(required) The date and time when the work request was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`time_started`

(optional) The date and time when the work request transitioned from ACCEPTED to IN_PROGRESS. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`time_finished`

(optional) The date and time when the work request reached a terminal state (FAILED or SUCCEEDED). Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time when the error happened. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time when the log message was written. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

`status`

(required) The status of the specified work request.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)identifying this work request.

`compartment_id`

(required) Unique identifier ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the compartment that contains the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the work request completed.

`time_accepted`

(required) The date and time when the work request was created. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`time_started`

(optional) The date and time when the work request transitioned from ACCEPTED to IN_PROGRESS. Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

`time_finished`

(optional) The date and time when the work request reached a terminal state (FAILED or SUCCEEDED). Format is defined by RFC3339. Example: `2020-01-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_ZIP_UPLOAD_CONFIG_SOURCE_T Type

Metadata about the zip file containing the Terraform configuration.

Syntax
```

```

`dbms_cloud_oci_resource_manager_zip_upload_config_source_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_t`type.

### DBMS_CLOUD_OCI_RESOURCE_MANAGER_ZIP_UPLOAD_CONFIG_SOURCE_RECORD_T Type

Information about the user-provided Terraform configuration zip file.

Syntax
```

```

`dbms_cloud_oci_resource_manager_zip_upload_config_source_record_t`is a subtype of the`dbms_cloud_oci_resource_manager_config_source_record_t`type.

- [Resource Manager Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-F7C819C2-C9E7-4949-B578-FF52EE8561DB)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-CB593218-DBBA-432F-9359-139D86F90580)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_ADVANCED_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-AE95AC1E-26A9-41B1-9B0A-58D054426CDA)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3246A7DB-5015-409F-B3F5-3D0C00EF9622)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-94C144ED-4B83-4DFB-A63C-B92F1A652BBB)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-D9709992-390E-4DCA-9A88-E6A8C8D8C8A7)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B640630A-189B-41BA-A873-B908B2F3F912)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_JOB_PLAN_RESOLUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-A9E33B15-86D1-4F30-A31E-F32CFD365496)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_ROLLBACK_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-0F94C458-B583-4ABF-AC3F-9BA024202ABD)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_APPLY_ROLLBACK_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-088FC6E7-C305-4AEE-A91B-9F24959F6A5B)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_ASSOCIATED_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-FFDAE74D-4C10-400F-9DAE-BFBD653A9D54)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_ASSOCIATED_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-E718C6FB-A56B-4812-9B0E-A883C6D8DDC2)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_ASSOCIATED_RESOURCES_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-70373559-2893-4391-AEAB-C917A574BA66)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-A6E397E5-2ABD-4C5D-BD8A-0E8CACAEDF9A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-4CC82F89-B9DE-4735-AE2B-8584825B16BC)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-27D7691C-B992-4E98-BD42-1FCB067D65C6)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-2818F439-455C-4E70-AD4B-C66F9725C91F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_SERVER_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-9385DEB0-0348-4E57-9257-EBECFC86C327)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-692EB261-053F-4108-9568-C5B5B291B163)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-0AD21B02-9DD5-4ED6-8B9D-0A68948FE7D6)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-7DDFED08-9EE1-4405-9F30-CA7261447B21)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-A9055164-2EBD-4948-A80F-78FB7B2168CA)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B3D2E626-01A3-4F0E-9BCD-4C538B03A37C)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-5FE6BE6E-3373-45B9-A078-F512190D7BF3)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-FEDC5A47-D538-4E15-8825-D9307F430396)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_BITBUCKET_SERVER_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-2DBB7525-AC97-42CF-8023-099EDB56F0FC)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CANCELLATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B0B8A3C5-509F-4D46-93BF-5A11DFF3870F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_CONFIGURATION_SOURCE_PROVIDER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-83406F07-69BB-4599-9567-EB47466CF9D9)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-0B923C2F-6ACD-41D2-B772-BABEB40C986F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_STACK_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3294F494-E5B0-4DD4-943D-02BA36FEE8DD)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CHANGE_TEMPLATE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C196EC97-E197-4928-B532-9DC0E432E0DB)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_COMPARTMENT_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-36E7B9AE-F357-49BB-89EB-27C79A39D9B8)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-104FB6F1-2E1C-4208-810D-159F6070E50A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CONFIGURATION_SOURCE_PROVIDER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-81AC85AD-2B3C-4251-B299-C8522EEB93CB)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-10AD4EF4-4311-4D7D-891D-F1A8FB41C6D5)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_APPLY_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-611FDCF2-4EAF-48F9-B7C4-252FA4F9C020)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_APPLY_ROLLBACK_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-35F26462-5A0F-41DA-934F-6C2769DBFB60)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C6A4A683-9FE3-44F0-B579-8EA288C99316)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_CLOUD_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-59C8C48F-2803-4CBC-83A3-88771FC28D15)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-41493235-2A0A-4CCF-8329-2E0790F14347)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-21793ADF-8E7C-4AA0-A1A7-CD25A645C60C)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3FD3C6FA-40CB-49C8-9CAC-978E227A05E8)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_BITBUCKET_SERVER_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-A5EC2E04-2039-4AD8-ACE0-CFB602607404)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_COMPARTMENT_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-198F624B-55AC-47B2-ACDB-027E2DDCD886)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_DESTROY_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-80A7AF77-56F8-484B-8863-7316ED907374)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_DEV_OPS_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-87977468-8408-426B-B75D-FAD41A2F2C22)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_GIT_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-E8F265D2-393E-44B2-AEDF-AB916C5E0F93)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-281711C2-5FCC-454C-925E-F327907CBC2A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-EC077D13-F578-4F54-BD45-1EAE7C412A04)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_IMPORT_TF_STATE_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-12EC3846-2053-491B-9280-92F2C4FC9E8B)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-024F5072-FD5F-4F88-8E5B-096536D19D1A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_OBJECT_STORAGE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C090986E-F4FE-403A-A620-FB20363F4621)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_PLAN_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-93FA269E-86D9-409F-BEC9-0E372BCA6F90)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_PLAN_ROLLBACK_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B4D7DB33-756B-40BD-BB8E-A0CEBB4F70ED)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-8049DD73-D968-4587-BF12-DFCAF3E68176)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CUSTOM_TERRAFORM_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-523AFC86-4B7E-42F8-BFCE-7AE3410CB042)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_STACK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-9189F2C5-B76E-46D1-8280-EF6BEFDCE1FF)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_STACK_TEMPLATE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-CD7E8541-088C-4AE0-BD75-335B3633DF6D)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_TEMPLATE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-D722E275-780F-44EF-B7DD-FEB663273DD1)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_TEMPLATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-CDD17739-44D7-4012-A76B-3B085359AE1A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_TEMPLATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-323F8AF3-9539-491C-8007-1430F9601348)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_CREATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-2585F497-6BB3-4BD1-9176-1E5BD6749DF2)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_DESTROY_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-78C8EE14-79AD-45F9-841B-BD23966CFB28)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_DESTROY_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-579B3F7B-E0F8-467C-B3D0-40BACBB1BEC3)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_DETECT_STACK_DRIFT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-58D69AA3-BE85-4768-9971-FD58B4CB2214)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_DEV_OPS_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-AD1A47F1-BB1F-416B-AAD1-AC2EEAB7A18F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_DEV_OPS_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-D45E28DD-3461-4E9F-B7D6-2D14E9054A5A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B00FABF2-825E-4C2C-8ED4-9B1FB04AA65B)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_FAILURE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-010BBBCF-9780-4A6F-AD1F-5B31EE087D84)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_GIT_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-AA8A0C50-AC5B-4657-808C-574D569C5F40)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_GIT_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-DF5C4298-1EBF-45EC-BB88-164FDC0195DB)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-BC124CE5-5F2D-4C00-B0A8-8F88F4F7F20D)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-69FED482-F026-45C7-96DE-53DC246DDB8E)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B09E250E-8448-4430-8768-A84D3BFA875E)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-BC578EDF-A44E-489E-8F21-29674791DC45)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_IMPORT_TF_STATE_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-208E9952-3C01-4D2D-8271-D6646B15821E)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_IMPORT_TF_STATE_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-94339F06-A4A7-4ABE-98D0-C00D6BC9E704)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-94F10F95-F73D-4A10-B93E-E4EA9AA8D25F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OUTPUT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3E29DC87-CBC4-4B26-A212-C2C2CA040E22)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OUTPUT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C720DD3A-F74B-424D-8D8D-815E65F442EF)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_OUTPUTS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-F6B28D7F-2E50-49B1-A187-A5534BC0AB48)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B5D23615-9614-4FB4-BF4F-5674D26FD75D)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C6F14353-8263-4855-882B-03CB8CAB953F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_OBJECT_STORAGE_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-36068F30-7693-465B-AE8F-EDCA92A0CBA2)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_OBJECT_STORAGE_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-369B4FA2-9E1B-4A77-9198-3C38E9DBEEC4)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C9567941-87D2-4D3E-A018-015DB2394ACF)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-43E84098-4CF6-402A-81A1-1539E2490C9E)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_ROLLBACK_JOB_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-8C040B98-9AE6-426F-B515-CB0BF0EF5483)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PLAN_ROLLBACK_JOB_OPERATION_DETAILS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B0FA3616-CDD8-4844-AF23-27870D1F8BB2)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-CE0F6FF3-0191-4987-A8D6-5A18EB6EDB69)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-29F0B245-BED3-4A9A-B927-B318532A9342)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-11723579-8230-47C8-BD36-A3836FF11197)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_PRIVATE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-976865F1-0E06-448D-BBD9-8F8E3C4D677F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_REACHABLE_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-77AEAC16-F57B-45C1-AE35-6E9759A8A126)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_RESOURCE_DISCOVERY_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-217AC2C6-9726-4F56-B84C-59F4E3436F80)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_RESOURCE_DISCOVERY_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-2A8C3C11-DBFA-46A4-92F4-F557BD630467)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_RESOURCE_DISCOVERY_SERVICE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-35529F38-C400-418E-ADAD-BB7A2C2C50D7)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-01820052-989C-4A4D-9362-B7F3959E99D1)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_RESOURCE_DRIFT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3181FAAA-E3E4-4B38-B4C7-5AFC45B65FF1)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_RESOURCE_DRIFT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-DB556B36-115B-4F55-8692-7C79B9E42075)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_RESOURCE_DRIFT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-0FACABB3-2003-4D3C-BBCC-FB55F34C9C5E)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_STACK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-9F40B7E5-AE09-41D6-B663-88CFEAEC7764)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-FB6F6EE0-C537-4BB8-8FBA-4A3A9B3B9776)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-139F319A-B467-4F95-B12A-3484640F48F6)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CATEGORY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-9680E213-2B3E-4456-9DC5-1DB786B9D2CA)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CATEGORY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B56A51C8-0A1B-4C33-B61D-C81E12C474E4)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_CATEGORY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-06B7D397-531A-4452-9561-1937995C99DF)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-CC1E194E-88D2-4FC0-9B58-62BBB41EC202)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-F9AEACA9-0462-44EA-B39F-078D65DD7281)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-01F20EAB-3ECC-453E-A24F-8373BB3BED0F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TEMPLATE_ZIP_UPLOAD_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-F6FA296A-93CD-41AB-8D46-82200CB162B5)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3365E7E4-1ADE-419A-9D42-C6AD54B7B526)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-177047E5-8E06-4AC5-952E-122FBC44A13A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_TERRAFORM_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-AB23449E-D1B6-472A-A258-385A267E63C4)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-EE7ED08E-D077-49F9-AC1C-94A3D0DD6719)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_CLOUD_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-3FF74257-88EB-4A3F-9F81-CCC698CE8724)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-B9EFCCA0-BFA4-49D6-8ED3-C27C23BAC025)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_CLOUD_USERNAME_APP_PASSWORD_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-ABDD2B45-CB3A-4006-8DFC-30318C1048A2)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_SERVER_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-FD94EC56-69EF-4BF4-ACB9-EE2536F6A3FA)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_BITBUCKET_SERVER_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-54403399-00A0-49D5-9853-8B595E89A9EC)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_DEV_OPS_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-5C9CD442-284D-4BAC-8F9D-E32038A7539A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_GIT_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-2DC0C2C7-B8A1-4BEE-BA49-D5074CA76FF2)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_GITHUB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-69257027-09E0-4A84-8317-1989E6935603)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_GITLAB_ACCESS_TOKEN_CONFIGURATION_SOURCE_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-4422E1F8-92C3-4714-ACB4-218622E59F05)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-6DA24B8D-73DF-4B4A-8AA7-A268628981A6)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_OBJECT_STORAGE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-986582BA-A9F6-4475-98DC-EC3F3116FD7A)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-5A5D020D-734F-4837-A47A-E5D70DBD8F07)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_STACK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-CDF3BE9F-29C6-44A1-9443-95C2114A7DBC)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_TEMPLATE_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-EC9A104C-0626-4690-8148-D6FEDAA28DAD)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_TEMPLATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-51C1E969-0A79-462A-9D29-ECB824F458BF)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_TEMPLATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-7F736281-CC22-482D-A5A1-63678791D688)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_UPDATE_ZIP_UPLOAD_CONFIG_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-737427C2-EEE7-4730-9BA1-1AB6A31A69D7)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-03CD8ECD-2DEA-4FC1-A50B-5BE3D249B180)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-6E105E62-C9CE-4EBF-ACAB-DF9DDE1369C3)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-213E37A4-8FAF-42BF-8D0C-CB77C1FF10A9)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-E1373AF9-96D2-4385-89F2-56AD704A7C77)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-991706AD-DFFB-46BD-B5CE-41EE42F3D41F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-F924E003-FF6C-4C45-85C9-78C087C79E10)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_ZIP_UPLOAD_CONFIG_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-C8F13924-9664-4488-BB64-565697853C7F)
- [DBMS_CLOUD_OCI_RESOURCE_MANAGER_ZIP_UPLOAD_CONFIG_SOURCE_RECORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_manager_t.html#ADSDK-GUID-443AEF8C-B37B-4190-A2A8-9C5350B376A1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
